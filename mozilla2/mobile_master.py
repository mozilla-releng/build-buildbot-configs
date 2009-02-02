# -*- python -*-
# ex: set syntax=python:

####### BUILDSLAVES


####### SCHEDULERS AND CHANGE SOURCES

import buildbotcustom.changes.hgpoller
from buildbotcustom.changes.hgpoller import HgPoller
from buildbot.scheduler import Scheduler, Nightly

import buildbot.status.tinderbox
from buildbot.status.tinderbox import TinderboxMailNotifier

import buildbotcustom.misc
from buildbotcustom.misc import isHgPollerTriggered

import buildbotcustom.process.factory
from buildbotcustom.process.factory import MaemoBuildFactory, WinceBuildFactory

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
    pushlogUrlOverride='http://hg.mozilla.org/mobile-browser/index.cgi/pushlog',
    pollInterval=1*60
))

# blassey's wince patches.  to be phased out eventually.
change_source.append(HgPoller(
    hgURL=config.HGURL,
    branch='wince-patches',
    pushlogUrlOverride='http://hg.mozilla.org//users/blassey_mozilla.com/wince-patches/index.cgi/pushlog',
    pollInterval=1*60
))

schedulers.append(Scheduler(
    name="mobile mozilla-central dep scheduler",
    branch="mozilla-central",
    treeStableTimer=3*60,
    builderNames=["mobile-linux-arm-dep", "mobile-wince-arm-dep"],
    fileIsImportant=lambda c: isHgPollerTriggered(c, config.HGURL)
))

schedulers.append(Scheduler(
    name="mobile mobile-browser dep scheduler",
    branch="mobile-browser",
    treeStableTimer=3*60,
    builderNames=["mobile-linux-arm-dep", "mobile-wince-arm-dep"],
    fileIsImportant=lambda c: isHgPollerTriggered(c, config.HGURL)
))

schedulers.append(Scheduler(
    name="mobile wince-patches dep scheduler",
    branch="wince-patches",
    treeStableTimer=3*60,
    builderNames=["mobile-wince-arm-dep"],
    fileIsImportant=lambda c: isHgPollerTriggered(c, config.HGURL)
))

status.append(TinderboxMailNotifier(
    fromaddr="mozilla2.buildbot@build.mozilla.org",
    tree='Mobile',
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org"],
    relayhost="mail.build.mozilla.org",
    builders=["mobile-linux-arm-dep", "mobile-wince-arm-dep"],
    logCompression="bzip2"
))

####### BUILDERS


linux_arm_dep_factory = MaemoBuildFactory(
    hgHost = HGHOST,
    repoPath = 'mozilla-central',
    configRepoPath = CONFIG_REPO_PATH,
    configSubDir = CONFIG_SUBDIR,
    mozconfig = "linux/mobile-browser/nightly",
    stageUsername = STAGE_USERNAME,
    stageGroup = STAGE_GROUP,
    stageSshKey = STAGE_SSH_KEY,
    stageServer = STAGE_SERVER,
    stageBasePath = STAGE_BASE_PATH,
    packageGlob = "mobile/dist/*.tar.bz2 xulrunner/xulrunner/*.deb mobile/mobile/*.deb",
    mobileRepoPath = 'mobile-browser',
    platform = 'linux-arm',
    baseWorkDir = '%s/build' % mobile_config.SBOX_HOME,
    buildToolsRepoPath = BUILD_TOOLS_REPO_PATH,
    buildSpace = 5 
)

linux_arm_dep_builder = {
    'name': 'mobile-linux-arm-dep',
    'slavenames': [
        'moz2-linux-slave01',
        'moz2-linux-slave02',
        'moz2-linux-slave05',
        'moz2-linux-slave06',
        'moz2-linux-slave07',
        'moz2-linux-slave08',
        'moz2-linux-slave09',
        'moz2-linux-slave10',
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

wince_arm_dep_factory = WinceBuildFactory(
    hgHost = HGHOST,
    repoPath = 'mozilla-central',
    configRepoPath = CONFIG_REPO_PATH,
    configSubDir = CONFIG_SUBDIR,
    mozconfig = "wince/mobile-browser/nightly",
    stageUsername = STAGE_USERNAME,
    stageGroup = STAGE_GROUP,
    stageSshKey = STAGE_SSH_KEY,
    stageServer = STAGE_SERVER,
    stageBasePath = STAGE_BASE_PATH,
    packageGlob = "xulrunner/dist/*.zip mobile/dist/*.zip",
    mobileRepoPath = 'mobile-browser',
    patchRepoPath = 'users/blassey_mozilla.com/wince-patches',
    platform = 'wince-arm',
    baseWorkDir = ".",
    buildToolsRepoPath = BUILD_TOOLS_REPO_PATH,
    buildSpace = 0
)

wince_arm_dep_builder = {
    'name': 'mobile-wince-arm-dep',
    'slavenames': [
        'mobile-win32-experiment01',
        'mobile-win32-experiment02',
        ],
    'builddir': 'wince-arm-dep',
    'factory': wince_arm_dep_factory,
    'category': 'mobile'
}
builders.append(wince_arm_dep_builder)
