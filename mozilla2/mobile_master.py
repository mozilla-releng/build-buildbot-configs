# -*- python -*-
# ex: set syntax=python:

####### BUILDSLAVES


####### SCHEDULERS AND CHANGE SOURCES

import buildbotcustom.changes.hgpoller
reload(buildbotcustom.changes.hgpoller)
from buildbotcustom.changes.hgpoller import HgPoller
from buildbot.scheduler import Scheduler, Nightly

import buildbot.status.tinderbox
reload(buildbot.status.tinderbox)
from buildbot.status.tinderbox import TinderboxMailNotifier

import buildbotcustom.misc
reload(buildbotcustom.misc)
from buildbotcustom.misc import isHgPollerTriggered

# most of the config is in an external file
import config
reload(config)
from config import *
import mobile_config
reload(mobile_config)

builders = []
schedulers = []
change_source = []
status = []

change_source.append(HgPoller(
    hgURL=config.HGURL,
    branch='mobile-browser',
    pushlogUrlOverride='http://hg.mozilla.org//mobile-browser/index.cgi/pushlog',
    pollInterval=1*60
))

schedulers.append(Scheduler(
    name="mobile mozilla-central dep scheduler",
    branch="mozilla-central",
    treeStableTimer=3*60,
    builderNames=["mobile-linux-arm-dep"],
    fileIsImportant=lambda c: isHgPollerTriggered(c, config.HGURL)
))

schedulers.append(Scheduler(
    name="mobile mobile-browser dep scheduler",
    branch="mobile-browser",
    treeStableTimer=3*60,
    builderNames=["mobile-linux-arm-dep"]
))

status.append(TinderboxMailNotifier(
    fromaddr="mozilla2.buildbot@build.mozilla.org",
    tree='Mobile',
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org"],
    relayhost="mail.build.mozilla.org",
    builders="mobile-linux-arm-dep",
    logCompression="bzip2"
))

####### BUILDERS

from buildbot.process import factory
from buildbot.steps.transfer import FileDownload
from buildbot.steps.source import Mercurial
from buildbot.steps.shell import Compile, ShellCommand, WithProperties


linux_arm_dep_factory = factory.BuildFactory()
linux_arm_dep_factory.addStep(ShellCommand(
    command = "rm /tmp/*_cltbld.log",
    description=['removing', 'logfile'],
    descriptionDone=['remove', 'logfile'],
    haltOnFailure=False,
    flunkOnFailure=False,
    warnOnFailure=False
))

linux_arm_dep_factory.addStep(ShellCommand,
    command=['bash', '-c', 'rm -rf ../*-nightly/build'],
    description=['cleaning', 'old', 'builds'],
    descriptionDone=['clean', 'old', 'builds'],
    warnOnFailure=True,
    flunkOnFailure=False)

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p',
               'mkdir -p build'],
    description=['creating', 'build dir'],
    descriptionDone=['created', 'build dir'],
    haltOnFailure=True
))

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['bash', '-c', 'rm -rf ' + \
               '/scratchbox/users/cltbld/home/cltbld//build/mozilla-central/objdir/mobile/dist/fennec* ' + \
               '/scratchbox/users/cltbld/home/cltbld//build/mozilla-central/objdir/xulrunner/xulrunner/*.deb ' + \
               '/scratchbox/users/cltbld/home/cltbld//build/mozilla-central/objdir/mobile/mobile/*.deb'],
    description=['removing', 'old', 'builds'],
    descriptionDone=['remove', 'old', 'builds'],
    haltOnFailure=False,
    flunkOnFailure=False,   
    warnOnFailure=False
))

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build',
    'hg', 'clone', 'http://hg.mozilla.org/mozilla-central', 'mozilla-central'],
    description=['checking', 'out', 'mozilla-central'],
    descriptionDone=['checked out', 'mozilla-central'],
    haltOnFailure=False,
    flunkOnFailure=False
))

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build/mozilla-central',
    'hg', 'pull', '-u'],
    description=['updating', 'from', 'mozilla-central'],
    descriptionDone=['updated', 'from', 'mozilla-central'],
    haltOnFailure=True
))

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build/mozilla-central',
    'hg', 'clone', 'http://hg.mozilla.org/mobile-browser', 'mobile'],
    description=['checking', 'out', 'mobile-browser'],
    descriptionDone=['checked out', 'mobile-browser'],
    haltOnFailure=False,
    flunkOnFailure=False
))

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build/mozilla-central/mobile',
    'hg', 'pull', '-u'],
    description=['updating', 'mobile-browser'],
    descriptionDone=['updating', 'mobile-browser'],
    haltOnFailure=True
))


linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build',
    'hg', 'clone', CONFIG_REPO_URL, 'buildbot-configs'],
    description=['checking', 'out', 'configs'],
    descriptionDone=['checkout', 'configs'],
    haltOnFailure=False,
    flunkOnFailure=False
))

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build/buildbot-configs',
    'hg', 'pull', '-u'],
    description=['updating', 'buildbot-configs'],
    descriptionDone=['updated', 'buildbot-configs'],
    haltOnFailure=True
))

# cp configs/mozilla2/$platform/mozconfig .mozconfig
linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p',
    'cp', 'build/buildbot-configs/%s/linux-arm/mozconfig' % (CONFIG_SUBDIR),
    'build/mozilla-central/.mozconfig'],
    description=['copying', 'mozconfig'],
    descriptionDone=['installed', 'mozconfig'],
    haltOnFailure=True
))

linux_arm_dep_factory.addStep(ShellCommand(
    command=['/scratchbox/moz_scratchbox', '-p', '-d', 'build/mozilla-central', 'cat', '.mozconfig'],
    description=['echo', 'mozconfig'],
    descriptionDone=['echo', 'mozconfig'],
))

linux_arm_dep_factory.addStep(Compile(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build/mozilla-central',
               'make -f client.mk build'],
    env={'PKG_CONFIG_PATH': '/usr/lib/pkgconfig/:/usr/local/lib/pkgconfig'},
    haltOnFailure=True
))

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build/mozilla-central/%s/mobile' % mobile_config.OBJDIR,
               'make package'],
    description=['make package'],
    haltOnFailure=True
))

# build deb packages
linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build/mozilla-central/%s/xulrunner' % mobile_config.OBJDIR,
               'make deb'],
    description=['make package'],
    haltOnFailure=True
))

linux_arm_dep_factory.addStep(ShellCommand(
    command = ['/scratchbox/moz_scratchbox', '-p', '-d', 'build/mozilla-central/%s/mobile' % mobile_config.OBJDIR,
               'make deb'],
    description=['make package'],
    haltOnFailure=True
))


linux_arm_dep_factory.addStep(ShellCommand(
    command = ['bash', '-c',
               'scp -p -oIdentityFile=~/.ssh/%s %s/build/mozilla-central/%s/mobile/dist/*.tar.bz2 ' % (STAGE_SSH_KEY, mobile_config.SBOX_HOME, mobile_config.OBJDIR) + \
               '%s/build/mozilla-central/%s/xulrunner/xulrunner/*.deb ' % (mobile_config.SBOX_HOME, mobile_config.OBJDIR) + \
               '%s/build/mozilla-central/%s/mobile/mobile/*.deb ' % (mobile_config.SBOX_HOME, mobile_config.OBJDIR) + \
               '%s@%s:%s/tinderbox-builds/mobile-browser-linux-arm' % (STAGE_USERNAME, STAGE_SERVER, STAGE_BASE_PATH)],
    description=['uploading', 'build'],
    descriptionDone=['upload', 'build'],
    haltOnFailure=True
))

linux_arm_dep_builder = {
    'name': 'mobile-linux-arm-dep',
    'slavenames': [
        'moz2-linux-slave1',
        'moz2-linux-slave02',
        'moz2-linux-slave03',
        'moz2-linux-slave05',
        'moz2-linux-slave06',
        'moz2-linux-slave11',
        'moz2-linux-slave12',
        'moz2-linux-slave13',
        'moz2-linux-slave14',
        'moz2-linux-slave15',
        'moz2-linux-slave16',
        ],
    'builddir': 'mobile-linux-arm-dep',
    'factory': linux_arm_dep_factory,
    'category': 'mobile'
}
builders.append(linux_arm_dep_builder)

