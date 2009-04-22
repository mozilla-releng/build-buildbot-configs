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
from buildbotcustom.process.factory import MaemoBuildFactory, \
   WinceBuildFactory, MaemoNightlyRepackFactory

from buildbotcustom.l10n import NightlyL10n, Scheduler as SchedulerL10n


# most of the config is in an external file
import config
reload(config)
from config import *
import mobile_config
reload(mobile_config)
from mobile_config import mobile_slaves

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

schedulers.append(Nightly(
    name="mobile nightly scheduler",
    branch="mobile-browser",
    hour=2,
    builderNames=["mobile-linux-arm-nightly", "mobile-wince-arm-nightly"]
))


status.append(TinderboxMailNotifier(
    fromaddr="mozilla2.buildbot@build.mozilla.org",
    tree='Mobile',
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org"],
    relayhost="mail.build.mozilla.org",
    builders=["mobile-linux-arm-dep", "mobile-linux-arm-nightly",
              "mobile-wince-arm-dep", "mobile-wince-arm-nightly"],
    logCompression="bzip2"
))

status.append(TinderboxMailNotifier(
    fromaddr="mozilla2.buildbot@build.mozilla.org",
    tree='Mozilla-l10n',
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org"],
    relayhost="mail.build.mozilla.org",
    builders=['Maemo mozilla-central l10n'],
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
    mobileRepoPath = 'mobile-browser',
    platform = 'linux-arm',
    baseWorkDir = '%s/build' % mobile_config.SBOX_HOME,
    buildToolsRepoPath = BUILD_TOOLS_REPO_PATH,
    clobberURL=BASE_CLOBBER_URL,
    clobberTime=DEFAULT_CLOBBER_TIME,
    buildSpace = 5
)
linux_arm_dep_builder = {
    'name': 'mobile-linux-arm-dep',
    'slavenames': mobile_slaves['linux-arm'],
    'builddir': 'mobile-linux-arm-dep',
    'factory': linux_arm_dep_factory,
    'category': 'mobile'
}
builders.append(linux_arm_dep_builder)

linux_arm_nightly_factory = MaemoBuildFactory(
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
    mobileRepoPath = 'mobile-browser',
    platform = 'linux-arm',
    baseWorkDir = '%s/build' % mobile_config.SBOX_HOME,
    buildToolsRepoPath = BUILD_TOOLS_REPO_PATH,
    buildSpace = 5,
    clobberURL=BASE_CLOBBER_URL,
    clobberTime=DEFAULT_CLOBBER_TIME,
    nightly = True
)
linux_arm_nightly_builder = {
    'name': 'mobile-linux-arm-nightly',
    'slavenames': mobile_slaves['linux-arm'],
    'builddir': 'mobile-linux-arm-nightly',
    'factory': linux_arm_nightly_factory,
    'category': 'mobile'
}
builders.append(linux_arm_nightly_builder)

wince_arm_dep_factory = WinceBuildFactory(
    hgHost = HGHOST,
    repoPath = 'mozilla-central',
    configRepoPath = CONFIG_REPO_PATH,
    configSubDir = CONFIG_SUBDIR,
    env = mobile_config.wince_arm_env,
    mozconfig = "wince/mobile-browser/nightly",
    stageUsername = STAGE_USERNAME,
    stageGroup = STAGE_GROUP,
    stageSshKey = STAGE_SSH_KEY,
    stageServer = STAGE_SERVER,
    stageBasePath = STAGE_BASE_PATH,
    mobileRepoPath = 'mobile-browser',
    platform = 'wince-arm',
    baseWorkDir = ".",
    buildToolsRepoPath = BUILD_TOOLS_REPO_PATH,
    clobberURL=BASE_CLOBBER_URL,
    clobberTime=DEFAULT_CLOBBER_TIME,
    buildSpace = 5
)
wince_arm_dep_builder = {
    'name': 'mobile-wince-arm-dep',
    'slavenames': mobile_slaves['wince-arm'],
    'builddir': 'wince-arm-dep',
    'factory': wince_arm_dep_factory,
    'category': 'mobile'
}
builders.append(wince_arm_dep_builder)

wince_arm_nightly_factory = WinceBuildFactory(
    hgHost = HGHOST,
    repoPath = 'mozilla-central',
    configRepoPath = CONFIG_REPO_PATH,
    configSubDir = CONFIG_SUBDIR,
    env = mobile_config.wince_arm_env,
    mozconfig = "wince/mobile-browser/nightly",
    stageUsername = STAGE_USERNAME,
    stageGroup = STAGE_GROUP,
    stageSshKey = STAGE_SSH_KEY,
    stageServer = STAGE_SERVER,
    stageBasePath = STAGE_BASE_PATH,
    mobileRepoPath = 'mobile-browser',
    platform = 'wince-arm',
    baseWorkDir = ".",
    buildToolsRepoPath = BUILD_TOOLS_REPO_PATH,
    buildSpace = 5,
    clobberURL=BASE_CLOBBER_URL,
    clobberTime=DEFAULT_CLOBBER_TIME,
    nightly = True
)
wince_arm_nightly_builder = {
    'name': 'mobile-wince-arm-nightly',
    'slavenames': mobile_slaves['wince-arm'],
    'builddir': 'wince-arm-nightly',
    'factory': wince_arm_nightly_factory,
    'category': 'mobile'
}
builders.append(wince_arm_nightly_builder)

maemo_trunk_l10n_nightly_factory = MaemoNightlyRepackFactory(
    hgHost=HGHOST,
    project='fennec',
    packageGlob='fennec-*.%(locale)s.linux-arm.tar.bz2',
    appName='mobile',
    enUSBinaryURL=DOWNLOAD_BASE_URL + '/nightly/latest-mobile-browser',
    stageServer=STAGE_SERVER,
    stageUsername=STAGE_USERNAME,
    stageSshKey=STAGE_SSH_KEY,
    stageBasePath=STAGE_BASE_PATH,
    repoPath='mozilla-central',
    l10nRepoPath='l10n-central',
    mobileRepoPath='mobile-browser',
    buildToolsRepoPath=BUILD_TOOLS_REPO_PATH,
    buildSpace=2,
    baseWorkDir='/scratchbox/users/cltbld/home/cltbld/l10n',
    clobberURL=BASE_CLOBBER_URL,
    clobberTime=DEFAULT_CLOBBER_TIME,
)
maemo_trunk_l10n_nightly_builder = {
    'name': 'Maemo mozilla-central l10n',
    'slavenames': mobile_slaves['linux-arm'],
    'builddir': 'maemo-trunk-l10n-nightly',
    'factory': maemo_trunk_l10n_nightly_factory,
    'category': 'l10n',
}
builders.append(maemo_trunk_l10n_nightly_builder)

maemo_191_l10n_nightly_factory = MaemoNightlyRepackFactory(
    hgHost=HGHOST,
    project='fennec',
    packageGlob='fennec-*.%(locale)s.linux-arm.tar.bz2',
    appName='mobile',
    enUSBinaryURL=DOWNLOAD_BASE_URL + '/nightly/latest-mobile-191',
    stageServer=STAGE_SERVER,
    stageUsername=STAGE_USERNAME,
    stageSshKey=STAGE_SSH_KEY,
    stageBasePath=STAGE_BASE_PATH,
    repoPath='releases/mozilla-1.9.1',
    l10nRepoPath='releases/l10n-mozilla-1.9.1',
    mobileRepoPath='mobile-browser',
    buildToolsRepoPath=BUILD_TOOLS_REPO_PATH,
    buildSpace=2,
    baseWorkDir='/scratchbox/users/cltbld/home/cltbld/l10n',
    clobberURL=BASE_CLOBBER_URL,
    clobberTime=DEFAULT_CLOBBER_TIME,
)
maemo_191_l10n_nightly_builder = {
    'name': 'Maemo mozilla-1.9.1 l10n',
    'slavenames': mobile_slaves['linux-arm'],
    'builddir': 'maemo-191-l10n-nightly',
    'factory': maemo_191_l10n_nightly_factory,
    'category': 'l10n',
}
builders.append(maemo_191_l10n_nightly_builder)

# TODO: add Maemo mozilla-1.9.1 l10n once we have 1.9.1 builds and
# bug 489313 is fixed.
for l10n_builder in ['Maemo mozilla-central l10n']:
    platform = 'linux'
    schedulers.append(NightlyL10n(
        name=l10n_builder,
        platform=platform,
        hour=[4],
        builderNames=[l10n_builder],
        repoType='hg',
        branch='mobile-browser',
        baseTag='default',
        localesFile="locales/all-locales",
    ))
