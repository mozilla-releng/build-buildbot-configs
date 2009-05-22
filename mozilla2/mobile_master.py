# -*- python -*-
# ex: set syntax=python:

####### BUILDSLAVES


####### SCHEDULERS AND CHANGE SOURCES

import buildbotcustom.changes.hgpoller
from buildbotcustom.changes.hgpoller import HgPoller, HgAllLocalesPoller
from buildbot.scheduler import Scheduler, Nightly

import buildbot.status.tinderbox
from buildbot.status.tinderbox import TinderboxMailNotifier

import buildbotcustom.misc
from buildbotcustom.misc import isHgPollerTriggered

from buildbotcustom.scheduler import MozScheduler

import buildbotcustom.process.factory
from buildbotcustom.process.factory import MaemoBuildFactory, \
   WinceBuildFactory, MaemoNightlyRepackFactory

from buildbot.steps.shell import WithProperties

from buildbotcustom.l10n import NightlyL10n, Scheduler as SchedulerL10n


# most of the config is in an external file
import config
reload(config)
from config import *
import mobile_config
reload(mobile_config)
from mobile_config import MOBILE_BRANCHES

m = {}

m['builders'] = []
m['schedulers'] = []
m['change_source'] = []
m['status'] = []

mobileBuilders = []

# Like the main cfg, except mobile
for name in sorted(MOBILE_BRANCHES.keys()):
    branch = MOBILE_BRANCHES[name]
    builders = []
    nightlyBuilders = []
    l10nNightlyBuilders = {}
    for platform in branch['platforms'].keys():
        base_name = branch['platforms'][platform]['base_name']
        builders.append('%s build' % base_name)
        mobileBuilders.append('%s build' % base_name)

        builder = '%s nightly' % base_name
        nightlyBuilders.append(builder)
        if branch['enable_l10n'] and platform in branch['l10n_platforms']:
            l10nNightlyBuilders[builder] = {}
            l10nNightlyBuilders[builder]['tree'] = branch['l10n_tree']
            l10nNightlyBuilders[builder]['l10n_builder'] = '%s l10n' % base_name
            l10nNightlyBuilders[builder]['platform'] = branch['l10n_platforms'][platform]

    m['status'].append(TinderboxMailNotifier(
        fromaddr="mozilla2.buildbot@build.mozilla.org",
        tree=branch['tinderbox_tree'],
        extraRecipients=['tinderbox-daemon@tinderbox.mozilla.org'],
        relayhost='mail.build.mozilla.org',
        builders=builders + nightlyBuilders,
        logCompression='bzip2'
    ))

    if branch['enable_l10n']:
        l10n_builders = []
        for b in l10nNightlyBuilders:
            l10n_builders.append(l10nNightlyBuilders[b]['l10n_builder'])
        # General tinderbox page
        m['status'].append(TinderboxMailNotifier(
            fromaddr="buildbot@mozilla.com",
            tree=branch['l10n_tinderbox_tree'],
            extraRecipients=['tinderbox-daemon@tinderbox.mozilla.org'],
            relayhost='mail.build.mozilla.org',
            logCompression='bzip2',
            builders=l10n_builders,
            binaryURL='http://%s/pub/mozilla.org/firefox/nightly/latest-%s-l10n' \
                      % (STAGE_SERVER, name)
        ))
        # Locale-specific page
        m['status'].append(TinderboxMailNotifier(
            fromaddr="buildbot@mozilla.com",
            tree=WithProperties(branch['l10n_tinderbox_tree'] + '-%(locale)s'),
            extraRecipients=['tinderbox-daemon@tinderbox.mozilla.org'],
            relayhost='mail.build.mozilla.org',
            logCompression='bzip2',
            builders=l10n_builders,
            binaryURL='http://%s/pub/mozilla.org/firefox/nightly/latest-%s-l10n' \
                      % (STAGE_SERVER, name)
        ))

    #
    # For now, there are no additional change_sources (except for
    # mobile-browser below) since mobile only builds on branches that
    # are already being polled in master.cfg
    #

    # nightly builders
    for builder in nightlyBuilders:
        nightly_scheduler=Nightly(
            name=builder,
            branch=branch['mobile_repo_path'], # mobile_repo_path
            hour=[1],
            builderNames=[builder]
        )
        m['schedulers'].append(nightly_scheduler)
        if branch['enable_l10n'] and builder in l10nNightlyBuilders:
            l10n_builder = l10nNightlyBuilders[builder]['l10n_builder']
            l10nPlatform = l10nNightlyBuilders[builder]['platform']
            tree = l10nNightlyBuilders[builder]['tree']
            m['schedulers'].append(NightlyL10n(
                name=l10n_builder,
                platform=l10nPlatform,
                tree=tree,
                hour=[4],
                builderNames=[l10n_builder],
                repoType='hg',
                branch=branch['mobile_repo_path'],
                baseTag='default',
                localesFile=branch['allLocalesFile']
            ))
    m['schedulers'].append(MozScheduler(
        name='mobile %s' % name,
        branch=branch['repo_path'],
        treeStableTimer=3*60,
        idleTimeout=branch.get('idle_timeout', None),
        builderNames=builders,
        fileIsImportant=lambda c: isHgPollerTriggered(c, HGURL)
    ))

    for platform in sorted(branch['platforms'].keys()):
        pf = branch['platforms'][platform]

        buildSpace = pf.get('build_space', DEFAULT_BUILD_SPACE)
        clobberTime = pf.get('clobber_time', DEFAULT_CLOBBER_TIME)

        mobile_dep_factory = None
        mobile_nightly_factory = None

        if platform == 'linux-arm':
            mobile_dep_factory = MaemoBuildFactory(
                hgHost=HGHOST,
                repoPath=branch['repo_path'],
                configRepoPath=CONFIG_REPO_PATH,
                configSubDir=CONFIG_SUBDIR,
                mozconfig=pf['mozconfig'],
                stageUsername=STAGE_USERNAME,
                stageGroup=STAGE_GROUP,
                stageSshKey=STAGE_SSH_KEY,
                stageServer=STAGE_SERVER,
                stageBasePath=STAGE_BASE_PATH,
                mobileRepoPath=branch['mobile_repo_path'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=BUILD_TOOLS_REPO_PATH,
                clobberURL=BASE_CLOBBER_URL,
                clobberTime=clobberTime,
                buildSpace=buildSpace
            )
            mobile_nightly_factory = MaemoBuildFactory(
                hgHost=HGHOST,
                repoPath=branch['repo_path'],
                configRepoPath=CONFIG_REPO_PATH,
                configSubDir=CONFIG_SUBDIR,
                mozconfig=pf['mozconfig'],
                stageUsername=STAGE_USERNAME,
                stageGroup=STAGE_GROUP,
                stageSshKey=STAGE_SSH_KEY,
                stageServer=STAGE_SERVER,
                stageBasePath=STAGE_BASE_PATH,
                mobileRepoPath=branch['mobile_repo_path'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=BUILD_TOOLS_REPO_PATH,
                clobberURL=BASE_CLOBBER_URL,
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                nightly = True
            )
        else:
            mobile_dep_factory=WinceBuildFactory(
                hgHost=HGHOST,
                repoPath=branch['repo_path'],
                configRepoPath=CONFIG_REPO_PATH,
                configSubDir=CONFIG_SUBDIR,
                env=pf['env'],
                mozconfig=pf['mozconfig'],
                stageUsername=STAGE_USERNAME,
                stageGroup=STAGE_GROUP,
                stageSshKey=STAGE_SSH_KEY,
                stageServer=STAGE_SERVER,
                stageBasePath=STAGE_BASE_PATH,
                mobileRepoPath=branch['mobile_repo_path'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=BUILD_TOOLS_REPO_PATH,
                clobberURL=BASE_CLOBBER_URL,
                clobberTime=clobberTime,
                buildSpace=buildSpace,
            )
            mobile_nightly_factory=WinceBuildFactory(
                hgHost=HGHOST,
                repoPath=branch['repo_path'],
                configRepoPath=CONFIG_REPO_PATH,
                configSubDir=CONFIG_SUBDIR,
                env=pf['env'],
                mozconfig=pf['mozconfig'],
                stageUsername=STAGE_USERNAME,
                stageGroup=STAGE_GROUP,
                stageSshKey=STAGE_SSH_KEY,
                stageServer=STAGE_SERVER,
                stageBasePath=STAGE_BASE_PATH,
                mobileRepoPath=branch['mobile_repo_path'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=BUILD_TOOLS_REPO_PATH,
                clobberURL=BASE_CLOBBER_URL,
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                nightly=True,
            )
        mobile_dep_builder = {
            'name': '%s build' % pf['base_name'],
            'slavenames': pf['slaves'],
            'builddir': pf['base_builddir'],
            'factory': mobile_dep_factory,
            'category': name
        }
        nightly_builder = '%s nightly' % pf['base_name']
        mobile_nightly_builder = {
            'name': nightly_builder,
            'slavenames': pf['slaves'],
            'builddir': '%s-nightly' % (pf['base_builddir']),
            'factory': mobile_nightly_factory,
            'category': name
        }
        m['builders'].append(mobile_dep_builder)
        m['builders'].append(mobile_nightly_builder)

        if branch['enable_l10n'] and platform in branch['l10n_platforms']:
            mobile_l10n_nightly_factory = None
            if platform == 'linux-arm':
                mobile_l10n_nightly_factory = MaemoNightlyRepackFactory(
                    hgHost=HGHOST,
                    tree=branch['l10n_tree'],
                    project=branch['product_name'],
                    appName=branch['app_name'],
                    packageGlob='fennec-*.%(locale)s.linux-arm.tar.bz2',
                    enUSBinaryURL=branch['enUS_binaryURL'],
                    stageServer=STAGE_SERVER,
                    stageUsername=STAGE_USERNAME,
                    stageSshKey=STAGE_SSH_KEY,
                    stageBasePath=STAGE_BASE_PATH,
                    repoPath=branch['repo_path'],
                    l10nRepoPath=branch['l10n_repo_path'],
                    mobileRepoPath=branch['mobile_repo_path'],
                    buildToolsRepoPath=BUILD_TOOLS_REPO_PATH,
                    buildSpace=2,
                    baseWorkDir=pf['base_l10n_workdir'],
                    baseUploadDir='%s-l10n' % name,
                    clobberURL=BASE_CLOBBER_URL,
                    clobberTime=clobberTime,
               )
            else:
                print 'platform %s is not linux-arm' % platform
                continue # TODO when we have WinceNightlyRepackFactory

            mobile_l10n_nightly_builder = {
                'name': l10nNightlyBuilders[nightly_builder]['l10n_builder'],
                'slavenames': pf['slaves'],
                'builddir': '%s-l10n-nightly' % (pf['base_builddir']),
                'factory': mobile_l10n_nightly_factory,
                'category': name,
            }
            m['builders'].append(mobile_l10n_nightly_builder)


# mobile-browser, which is shared
m['change_source'].append(HgPoller(
    hgURL=HGURL,
    branch='mobile-browser',
    pushlogUrlOverride='http://hg.mozilla.org/mobile-browser/index.cgi/pushlog',
    pollInterval=1*60
))
m['schedulers'].append(Scheduler(
    name="mobile-browser",
    branch="mobile-browser",
    treeStableTimer=3*60,
    builderNames=mobileBuilders,
    fileIsImportant=lambda c: isHgPollerTriggered(c, HGURL)
))
