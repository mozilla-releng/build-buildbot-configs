import buildbot, twisted
from buildbot.changes.base import ChangeSource
from buildbot.changes.changes import Change
from buildbot.process.base import Build
from buildbot.process.buildstep import BuildStep, render_properties
from buildbot.steps.source import Mercurial
from buildbot.steps.shell import Compile, ShellCommand, WithProperties
from buildbot.status.builder import SUCCESS, WARNINGS, FAILURE, SKIPPED
from buildbot.scheduler import Periodic, Nightly
from buildbot.sourcestamp import SourceStamp
from twisted.python import log
from twisted.internet import defer, reactor, threads
from twisted.internet.task import LoopingCall
from buildbotcustom.changes.hgpoller import parse_date
import urllib
from xml.dom import minidom, Node
from calendar import timegm
import time
import re

from buildbotcustom.steps.transfer import MozillaStageUpload
from buildbotcustom.steps.updates import CreateCompleteUpdateSnippet
from buildbotcustom.steps.l10n import SetLocalesStep, LocaleCompile, NonLocaleMercurial, LocaleMercurial, getLocalesForRequests

try:
    # The buildbot 0.7.7 version
    from buildbot.process.buildstep import render_properties
except ImportError:
    # The buildbot 0.7.8 version
    def render_properties(s, build):
        return build.getProperties().render(s)


def callDeferredOnThread(deferred, f, *args, **kwargs):
    """This is a lot like twisted.internet.threads.deferToThread, except
    the caller provides a Deferred, which can have callbacks already
    added to it, which means there is no possibility of a race."""
    reactor.callInThread(twisted.internet.threads._putResultInDeferred,
                         deferred, f, args, kwargs)

allLocalesURL = 'http://hg.mozilla.org/comm-central/raw-file/tip/mail/locales/all-locales'

# Periodic Scheduler which calculates all-locales

def doPeriodicBuild(self):
    d = defer.Deferred()
    d.addCallback(self.process_all_locales)
    d.addErrback(self.finished_failure)
    callDeferredOnThread(d, urllib.urlopen, allLocalesURL)

def process_all_locales(self, result):
    locales = [l.strip() for l in result if l.strip() != '']
    source = SourceStamp(branch=self.branch)
    source.allLocales = locales
    bs = buildbot.buildset.BuildSet(self.builderNames, source, self.reason)
    self.submit(bs)

def finished_failure(self, result):
    log.msg("Couldn't retrieve all-locales in L10nPeriodic: %s" % result)
    return None

class L10nPeriodic(Periodic):
    doPeriodicBuild = doPeriodicBuild
    process_all_locales = process_all_locales
    finished_failure = finished_failure

class L10nNightly(Nightly):
    doPeriodicBuild = doPeriodicBuild
    process_all_locales = process_all_locales
    finished_failure = finished_failure

class LocaleShellCommand(ShellCommand):
    """Subclass of ShellCommand step for localized builds."""
    def __init__(self, locale, **kwargs):
        ShellCommand.__init__(self, **kwargs)
        self.locale = locale
        self.addFactoryArguments(locale=locale)

    def describe(self, done=False):
        d = ShellCommand.describe(self, done)
        if isinstance(d, (str, unicode)):
            return "%s: %s" % (self.locale, d)

        d = list(d)
        d.insert(0, "%s:" % self.locale)
        return d

    def commandComplete(self, cmd):
        self.step_status.locale = self.locale

class LocaleGetBuildProperties(LocaleShellCommand):
    """Retrieves the BuildID from a Mozilla tree (using application.ini) and sets
    it as a build property ('buildid'). If defined, uses objdir as it's base.
    """
    description=['getting buildid']
    descriptionDone=['get buildid']
    haltOnFailure=False

    def __init__(self, builddir="", **kwargs):
        LocaleShellCommand.__init__(self, **kwargs)
        self.builddir = builddir
        self.addFactoryArguments(builddir=builddir)
        self.command = ['python', 'config/printconfigsetting.py',
                        '%s/application.ini' % self.builddir,
                        'App', 'BuildID']

    def commandComplete(self, cmd):
        LocaleShellCommand.commandComplete(self, cmd)
        buildid = ""
        try:
            buildid = cmd.logs['stdio'].getText().strip().rstrip()
            if re.match(r"\d+$", buildid):
                self.setProperty('buildid', buildid)
        except:
            log.msg("Could not find BuildID or BuildID invalid")
            log.msg("Found: %s" % buildid)
            return FAILURE
        return SUCCESS

class LocaleCreateCompleteUpdateSnippet(CreateCompleteUpdateSnippet):
    """Subclass of CreateCompleteUpdateSnippet step for localized builds."""
    def __init__(self, locale, **kwargs):
        CreateCompleteUpdateSnippet.__init__(self, **kwargs)
        self.locale = locale
        self.addFactoryArguments(locale=locale)

    def describe(self, done=False):
        d = CreateCompleteUpdateSnippet.describe(self, done)
        if isinstance(d, (str, unicode)):
            return "%s: %s" % (self.locale, d)

        d = list(d)
        d.insert(0, "%s:" % self.locale)
        return d

    def commandComplete(self, cmd):
        self.step_status.locale = self.locale

class CCRepackFactory(buildbot.util.ComparableMixin):
    buildClass = Build
    compare_attrs = ['mainRepoURL',
                     'localesRepoURL',
                     'configRepoURL',
                     'repackLocation',
                     'mainBranch',
                     'localesBranch',
                     'configDir',
                     'product',
                     'platform',
                     'appname',
                     'brandname',
                     'stage_username',
                     'stage_server',
                     'stage_base_path',
                     'stage_group',
                     'stage_ssh_key',
                     'update_download_base_url',
                     'update_base_upload_dir',
                     'update_platform',
                     'update_user',
                     'update_host',
                     'cvsroot',
                     ]

    # This dummy attribute exists so that buildbot configuration can succeed
    steps = ()

    def __init__(self, mainRepoURL, localesRepoURL, configRepoURL,
                 repackLocation, mainBranch, localesBranch, configDir,
                 product, platform, appname, brandname, stage_username,
                 stage_server, stage_base_path, stage_group, stage_ssh_key,
                 createSnippets, update_download_base_url, update_base_upload_dir,
                 update_platform, update_user, update_host, cvsroot):
        """
        @param mainRepoURL: the repoURL to check out the main codebase
        @param localesRepoURL: the repoURL pattern to check out localized
                               files. %(locale)s will be substituted
        @param configRepoURL:  the repoURL pattern to check out buildbot
                               config files.
        @param repackLocation: the directory from which the main binaries
                               should be downloaded
        @param mainBranch:     the branch name used for Changes from the
                               main codebase
        @param localesBranch:  the branch name used for Changes to
                               localizations. These Changes must have a .locale
                               property.
        @param configDir:      the configuration subdirectory in the config repo
        @param product:        the Mozilla product, e.g. suite or mail
        @param appname:        the Mozilla app name, e.g. seamonkey or thunderbird
        @param brandname:      the app brand name, e.g. SeaMonkey or Thunderbird
        @param platform:       the platform we're building on
        @param stage_username: the stage username for MozillaStageUpload
        @param stage_server:   the stage server for MozillaStageUpload
        @param stage_base_path: the stage base path for MozillaStageUpload
        @param stage_group:    the stage group for MozillaStageUpload
        @param stage_ssh_key:  the stage ssh key for MozillaStageUpload
        @param createSnippets: create update snippets for locale builds
        @param update_download_base_url: download base directory, for AUS snippets
        @param update_base_upload_dir: upload directory, for AUS snippets
        @param update_platform: platform indicator for AUS snippets
        @param update_user:    username on the AUS stage server, for AUS snippets
        @param update_host:    host name of the AUS stage server, for AUS snippets
        @param cvsroot:        cvsroot to use for CVS operations
        """

        self.mainRepoURL = mainRepoURL
        self.localesRepoURL = localesRepoURL
        self.configRepoURL = configRepoURL
        self.repackLocation = repackLocation
        self.mainBranch = mainBranch
        self.localesBranch = localesBranch
        self.configDir = configDir
        self.product = product
        self.platform = platform
        self.appname = appname
        self.brandname = brandname
        self.stage_username = stage_username
        self.stage_server = stage_server
        self.stage_base_path = stage_base_path
        self.stage_group = stage_group
        self.stage_ssh_key = stage_ssh_key
        self.createSnippets = createSnippets
        self.update_download_base_url = update_download_base_url
        self.update_base_upload_dir = update_base_upload_dir
        self.update_platform = update_platform
        self.update_user = update_user
        self.update_host = update_host
        self.cvsroot = cvsroot

    def newBuild(self, requests):
        """Create a list of steps to build these possibly coalesced requests.
        After initial steps, loop over the locales which need building
        and insert steps for each locale."""

        locales = getLocalesForRequests(requests)

        if self.platform.startswith("macosx"):
            appIniDir = '../obj/mozilla/dist/l10n-stage/%s/%s.app/Contents/MacOS' % \
                        (self.appname, self.brandname)
        else:
            appIniDir = '../obj/mozilla/dist/l10n-stage/%s' % self.appname

        steps = []
        if len(locales) > 0:
            steps.append(SetLocalesStep(locales=locales))
            steps.append(NonLocaleMercurial(
                repourl=self.mainRepoURL,
                mainBranch=self.mainBranch,
            ))
            extra_args = []
        if self.cvsroot:
            extra_args = [ '--cvsroot' , self.cvsroot ] 
            steps.append(ShellCommand(
                command=['python', 'client.py', 'checkout'] + extra_args,
                description=['running', 'client.py', 'checkout'] + extra_args,
                descriptionDone=['client.py', 'checkout'],
                haltOnFailure=True,
            ))
            steps.append(ShellCommand(
                command=['rm', '-rf', 'obj'],
                description=['removing', 'objdir'],
                descriptionDone=['remove', 'objdir'],
                flunkOnFailure=False,
            ))
            steps.append(ShellCommand(
                command=['sh', '-c', 'mkdir -p l10n obj/mozilla/dist/bin'],
                description=['creating', 'l10n', 'and', 'dist/bin', 'dirs'],
                descriptionDone=['create', 'l10n', 'and', 'dist/bin', 'dirs'],
                flunkOnFailure=False,
            ))
            if self.platform.startswith("macosx"):
                steps.append(ShellCommand(
                    command=['mkdir', '-p', 'obj/mozilla/dist/branding'],
                    description=['creating', 'branding', 'dir'],
                    descriptionDone=['create', 'branding', 'dir'],
                    haltOnFailure=True,
                ))
            steps.append(ShellCommand(
                command=['rm', '-rf', 'configs'],
                description=['removing', 'configs'],
                descriptionDone=['remove', 'configs'],
                haltOnFailure=True,
            ))
            steps.append(ShellCommand(
                command=['hg', 'clone', self.configRepoURL, 'configs'],
                description=['checking', 'out', 'configs'],
                descriptionDone=['checkout', 'configs'],
                haltOnFailure=True,
            ))
            steps.append(ShellCommand(
                # cp configs/seamonkey/$platform/mozconfig-l10n .mozconfig
                command=['cp', 'configs/%s/%s/mozconfig-l10n' % \
                               (self.configDir, self.platform),
                         '.mozconfig'],
                description=['copying', 'mozconfig'],
                descriptionDone=['copy', 'mozconfig'],
                haltOnFailure=True,
            ))

            steps.append(Compile(
                command=['make', '-f', 'client.mk', 'configure'],
                env = {'MOZ_OBJDIR': 'obj'},
                haltOnFailure=True,
            ))
            # the next three steps are needed so we have a mar tool
            steps.append(ShellCommand(
                command=['make', '-C', 'obj/mozilla/config'],
                description=['making', 'config'],
                descriptionDone=['make', 'config'],
                haltOnFailure=True,
            ))
            steps.append(ShellCommand(
                command=['make', '-C', 'obj/mozilla/nsprpub'],
                description=['making', 'nsprpub'],
                descriptionDone=['make', 'nsprpub'],
                haltOnFailure=True,
            ))
            steps.append(ShellCommand(
                command=['make', '-C', 'obj/mozilla/modules/libmar'],
                description=['making', 'libmar'],
                descriptionDone=['make', 'libmar'],
                haltOnFailure=True,
            ))
            steps.append(ShellCommand(
                command=['make', '-C', 'obj/%s/locales' % self.product,
                         'wget-en-US', 'EN_US_BINARY_URL=%s' % self.repackLocation],
                description=['getting', 'en-US', 'file(s)'],
                descriptionDone=['get', 'en-US', 'file(s)'],
                haltOnFailure=True,
            ))

            for locale in locales:
                steps.append(LocaleMercurial(
                    locale=locale,
                    localesBranch=self.localesBranch,
                    workdir='build/l10n/%s' % locale,
                    repourl=self.localesRepoURL % {'locale': locale},
                ))
                if self.platform.startswith("macosx") and self.product == "suite":
                    steps.append(LocaleShellCommand(
                        locale=locale,
                        command=['cp', 'l10n/%s/%s/installer/mac/README.txt' % \
                                       (locale, self.product),
                                 'obj/mozilla/dist/bin/'],
                        description=['copying', 'README'],
                        descriptionDone=['copy', 'README'],
                        haltOnFailure=True,
                    ))
                steps.append(LocaleCompile(
                    locale=locale,
                    command=['make', '-C', 'obj/%s/locales' % self.product,
                             'installers-%s' % locale],
                    haltOnFailure=False,
                ))
                # the slightly hacky command below is to ensure we don't
                # package updates on failure even though we don't halt
                steps.append(LocaleShellCommand(
                    locale=locale,
                    command=['sh', '-c',
                             'if [ -z `ls %s-*.%s.*` ]; then rm -rf l10n-stage; fi' % \
                             (self.appname, locale)],
                    workdir='build/obj/mozilla/dist',
                    haltOnFailure=False,
                ))
                steps.append(LocaleShellCommand(
                    locale=locale,
                    command=['make', '-C', 'obj/mozilla/tools/update-packaging',
                             'complete-patch', 'AB_CD=%s' % locale,
                             'DIST=../../dist/l10n-stage',
                             'STAGE_DIR=../../dist/update',
                             'MAR_BIN=../../dist/host/bin/mar'],
                    description=['create', 'complete', 'update'],
                    haltOnFailure=False,
                ))
                steps.append(LocaleGetBuildProperties(
                    locale=locale,
                    builddir=appIniDir,
                    workdir='build/mozilla',
                ))
                if self.createSnippets:
                    # this is a tad ugly because we need to python interpolation
                    # as well as WithProperties
                    # here's an example of what it translates to:
                    # /opt/aus2/build/0/SeaMonkey/mozilla2/WINNT_x86-msvc/2008010103/en-GB
                    AUS2_FULL_UPLOAD_DIR = '%s/%s/%%(buildid)s/%s' % \
                        (self.update_base_upload_dir, self.update_platform, locale)
                    steps.append(LocaleCreateCompleteUpdateSnippet(
                        objdir='build/obj/mozilla',
                        milestone=self.mainBranch,
                        baseurl='%s/nightly' % self.update_download_base_url
                    ))
                    steps.append(LocaleShellCommand(
                        command=['ssh', '-l', self.update_user, self.update_host,
                                 WithProperties('mkdir -p %s' % AUS2_FULL_UPLOAD_DIR)],
                        description=['create', 'aus2', 'upload', 'dir'],
                        haltOnFailure=True,
                    ))
                    steps.append(LocaleShellCommand(
                        command=['scp', '-o', 'User=%s' % self.update_user,
                                 'dist/update/complete.update.snippet',
                                 WithProperties('%s:%s/complete.txt' % \
                                     (self.update_host, AUS2_FULL_UPLOAD_DIR))],
                        workdir='build/obj/mozilla',
                        description=['upload', 'complete', 'snippet'],
                        haltOnFailure=True,
                    ))

            steps.append(ShellCommand(
                command="rm -rf %s-*.en-US.* install/sea/%s-*.en-US.*" % \
                            (self.appname, self.appname),
                workdir='build/obj/mozilla/dist',
                description=['removing', 'en-US', 'file(s)'],
                descriptionDone=['remove', 'en-US', 'file(s)'],
                warnOnFailure=True,
            ))
            steps.append(MozillaStageUpload(
                objdir='obj/mozilla',
                username=self.stage_username,
                milestone=self.localesBranch,
                remoteHost=self.stage_server,
                remoteBasePath=self.stage_base_path,
                platform=self.platform,
                group=self.stage_group,
                sshKey=self.stage_ssh_key,
                releaseToDated=False,
                releaseToLatest=True,
                releaseToTinderboxBuilds=False,
                tinderboxBuildsDir='%s-%s' % (self.localesBranch, self.platform),
                uploadLangPacks=True,
            ))

        b = self.buildClass(requests)
        b.useProgress = False
        b.setStepFactories([step.getStepFactory() for step in steps])
        return b

class TriggerLocalesStep(ShellCommand):
    """
    This step can be added at the end of a regular product build. It will
    trigger a localization repack of that build.
    """

    name = "triggerlocales"

    def __init__(self, product, schedulerNames, **kwargs):
        """
        @param product        The product directory to get an all-locales file.
                              e.g. "browser" for browser/locales/all-locales
        @param schedulerNames The names of schedulers to trigger from this step.
        """
        self.command = ['cat', '%s/locales/all-locales' % product]
        ShellCommand.__init__(self, **kwargs)
        self.schedulerNames = schedulerNames
        self.addFactoryArguments(product=product,
                                 schedulerNames=schedulerNames)

    def commandComplete(self, cmd):
        if cmd.rc == 0:
            out = cmd.logs['stdio'].getText()

            change = Change(who='dummy-l10n',
                            files=[],
                            comments="Dummy l10n change",
                            revision=self.build.getProperty('got_revision'),
                            branch=self.build.getSourceStamp().branch)

            ss = buildbot.sourcestamp.SourceStamp(changes=[change])
            ss.allLocales = [l for l in out.splitlines() if l != '']

            all_schedulers = dict([(sch.name, sch)
                                   for sch in self.build.builder.botmaster.parent.allSchedulers()])

            for sname in self.schedulerNames:
                sname = render_properties(sname, self.build)
                s = all_schedulers[sname]
                s.trigger(ss)
