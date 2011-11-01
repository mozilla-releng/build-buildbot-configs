import os
from buildbot.changes.pb import PBChangeSource
from buildbot.scheduler import Scheduler, Dependent, Triggerable, Nightly
from buildbot.status.tinderbox import TinderboxMailNotifier

import buildbotcustom.l10n
import buildbotcustom.misc
import buildbotcustom.process.factory

from buildbotcustom.l10n import DependentL10n
from buildbotcustom.misc import get_l10n_repositories, isHgPollerTriggered, \
  generateTestBuilderNames, generateTestBuilder, _nextFastSlave
from buildbotcustom.process.factory import StagingRepositorySetupFactory, \
  ReleaseTaggingFactory, CCSourceFactory, CCReleaseBuildFactory, \
  ReleaseUpdatesFactory, UpdateVerifyFactory, ReleaseFinalVerification, \
  L10nVerifyFactory, CCReleaseRepackFactory, UnittestPackagedBuildFactory, \
  PartnerRepackFactory, MajorUpdateFactory, XulrunnerReleaseBuildFactory, \
  TuxedoEntrySubmitterFactory, ScriptFactory
from buildbotcustom.changes.ftppoller import FtpPoller

# this is where all of our important configuration is stored. build number,
# version number, sign-off revisions, etc.
#import release_config
#reload(release_config)
#from release_config import *

# for the 'build' step we use many of the same vars as the nightlies do.
# we import those so we don't have to duplicate them in release_config
import config as nightly_config
reload(nightly_config)

APP_NAME = 'mail'

gloConfig = {
    '31': {
        'hgUsername'                 : 'tbirdbld',
        'hgSshKey'                   : '~cltbld/.ssh/tbirdbld_dsa',
        'relbranchPrefix'            : 'COMM',
        'sourceRepoName'             : 'comm-1.9.2', # buildbot branch name
        'sourceRepoPath'             : 'releases/comm-1.9.2',
        'sourceRepoRevision'         : 'e934a6ddfdad',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        'relbranchOverride'          : '',
        'mozillaRepoPath'            : 'releases/mozilla-1.9.2',
        'mozillaRepoRevision'        : '10763253c915',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        # 'You' typically want to set this to the gecko relbranch if doing a release off
        # 'a' specific gecko version.
        'mozillaRelbranchOverride'   : 'GECKO19224_2011103116_RELBRANCH', # put Gecko relbranch here that we base upon
        'inspectorRepoPath'          : 'dom-inspector', # leave empty if inspector is not to be tagged
        'inspectorRepoRevision'      : 'c1b38e365772',
        'inspectorRelbranchOverride' : 'COMM1929_20100910_RELBRANCH',
        'buildToolsRepoPath'            : '', # leave empty if buildTools is not to be tagged
        'buildToolsRepoRevision'        : '',
        #buildToolsRepoRevision        : '479375734669'
        'buildToolsRelbranchOverride'   : '',
        'venkmanRepoPath'            : '', # leave empty if venkman is not to be tagged
        'venkmanRepoRevision'        : '',
        'venkmanRelbranchOverride'   : '',
        'chatzillaCVSRoot'           : '',
        'chatzillaTimestamp'         : '', # leave empty if chatzilla is not to be tagged
        'l10nRepoPath'               : 'releases/l10n-mozilla-1.9.2',
        'l10nRevisionFile'           : 'l10n-thunderbird-changesets-3.1',
        'toolsRepoPath'              : 'build/tools',
        'buildToolsRepoPath'	   : '',
        'mergeLocales'               : False,
        'cvsroot'                    : ':ext:tbirdbld@cvs.mozilla.org:/cvsroot', # for patcher, etc.
        'productVersionFile'         : 'mail/config/version-192.txt',
        'productName'                : 'thunderbird',
        'binaryName'                 : 'thunderbird',
        'brandName'                  : 'Thunderbird',
        'appName'                    : APP_NAME,
        'ftpName'                    : APP_NAME,
        # 'Sometimes' we need the application version to be different from what we "call"
        # 'the' build, eg public release candidates for a major release (3.1 RC1).
        # 'appVersion' and oldAppVersion are optional definitions used in places that
        # 'don''t care about what we call it. Eg, when version bumping we will bump to
        # 'appVersion', not version.
        'version'                    : '3.1.16',
        #'appVersion'                 : version,
        #XXX: 'Not' entirely certain if/where this is used.
        # 'Derived' from mozillaRelbranchOverride. eg: COMM19211_20101004_RELBRANCH == 1.9.2.11
        'milestone'                  : '1.9.2.24',
        'buildNumber'                : 1,
        'baseTag'                    : 'THUNDERBIRD_3_1_16',
        # 'The' old version is the revision from which we should generate update snippets.
        'oldVersion'                 : '3.1.15',
        #'oldAppVersion'              : oldVersion,
        'oldBuildNumber'             : 1,
        'oldBaseTag'                 : 'THUNDERBIRD_3_1_15',
        'oldBinaryName'              : 'thunderbird',
        'enable_weekly_bundle'       : False,
        'enUSPlatforms'              : ('linux', 'win32', 'macosx'),
        'unittestPlatforms'          : (),
        'xulrunnerPlatforms'         : (),
        'patcherConfig'              : 'moz192-thunderbird-branch-patcher2.cfg',
        'patcherToolsTag'            : 'UPDATE_PACKAGING_R11_1_MU',
        'snippetSchema'              : 1,
        'ftpServer'                  : 'ftp.mozilla.org',
        'stagingServer'              : 'stage-old.mozilla.org',
        'bouncerServer'              : 'download.mozilla.org',
        'releaseNotesUrl'            : 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%',
        'ausUser'                    : 'tbirdbld',
        'ausSshKey'                  : 'tbirdbld_dsa',
        'ausServerUrl'               : 'https://aus2.mozillamessaging.com',
        'testOlderPartials'          : False,
        'doPartnerRepacks'           : True,
        'partnersRepoPath'           : 'users/bugzilla_standard8.plus.com/tb-partner-repacks',
        'useBetaChannel'             : 1,
        'verifyConfigs'              : {'linux':  'moz192-thunderbird-linux.cfg',
                                      'macosx': 'moz192-thunderbird-mac.cfg',
                                      'win32':  'moz192-thunderbird-win32.cfg'},
        'packageTests'               : False,
        'unittestMasters'            : (),
        
        # 'Version' numbers we are updating _TO_
        # 'N'/A for Thunderbird 3.x (until the next major version is released)
        'majorUpdateRepoPath'    : 'releases/mozilla-release',
        'majorUpdateSourceRepoPath' : 'releases/comm-release',
        'majorUpdateToVersion'   : '7.0.1',
        #'majorUpdateAppVersion'  : majorUpdateToVersion,
        'majorUpdateBuildNumber' : 1,
        'majorUpdateBaseTag'     : 'THUNDERBIRD_7_0_1',
        'majorUpdateReleaseNotesUrl' : 'https://www.mozilla.org/%locale%/thunderbird/7.0/details/index.html',
        'majorUpdatePatcherConfig' : 'moz20-thunderbird-branch-major-update-patcher2.cfg',
        'majorUpdateVerifyConfigs' : {'linux':  'moz20-thunderbird-linux-major.cfg',
                                    'macosx': 'moz20-thunderbird-mac64-major.cfg',
                                    'win32':  'moz20-thunderbird-win32-major.cfg'},
    },
    'beta': {
        'hgUsername'                 : 'tbirdbld',
        'hgSshKey'                   : '~cltbld/.ssh/tbirdbld_dsa',
        'relbranchPrefix'            : 'COMM',
        'sourceRepoName'             : 'comm-beta', # buildbot branch name
        'sourceRepoPath'             : 'releases/comm-beta',
        'oldRepoPath'                : 'releases/comm-beta',
        'sourceRepoRevision'         : '7d3a510fc227',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        'relbranchOverride'          : 'COMM80_20111031_RELBRANCH',
        'mozillaRepoPath'            : 'releases/mozilla-beta',
        'mozillaRepoRevision'        : '92635f5299af',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        # 'You' typically want to set this to the gecko relbranch if doing a release off
        # 'a' specific gecko version.
        'mozillaRelbranchOverride'   : 'GECKO80_2011103118_RELBRANCH', # put Gecko relbranch here that we base upon
        'inspectorRepoPath'          : '', #'dom-inspector', # leave empty if inspector is not to be tagged
        'inspectorRepoRevision'      : '',
        'inspectorRelbranchOverride' : '',
        'buildToolsRepoPath'            : '', # leave empty if buildTools is not to be tagged
        'buildToolsRepoRevision'        : '',
        #buildToolsRepoRevision        : '479375734669'
        'buildToolsRelbranchOverride'   : '',
        'venkmanRepoPath'            : '', # leave empty if venkman is not to be tagged
        'venkmanRepoRevision'        : '',
        'venkmanRelbranchOverride'   : '',
        'chatzillaCVSRoot'           : '',
        'chatzillaTimestamp'         : '', # leave empty if chatzilla is not to be tagged
        'l10nRepoPath'               : 'releases/l10n/mozilla-beta',
        'l10nRevisionFile'           : 'l10n-thunderbird-changesets-beta',
        'toolsRepoPath'              : 'build/tools',
        'buildToolsRepoPath'	   : '',
        'mergeLocales'               : True,
        'cvsroot'                    : ':ext:tbirdbld@cvs.mozilla.org:/cvsroot', # for patcher, etc.
        'productVersionFile'         : 'mail/config/version.txt',
        'productName'                : 'thunderbird',
        'binaryName'                 : 'thunderbird',
        'oldBinaryName'              : 'thunderbird',
        'brandName'                  : 'Thunderbird',
        'appName'                    : APP_NAME,
        'ftpName'                    : APP_NAME,
        # 'Sometimes' we need the application version to be different from what we "call"
        # 'the' build, eg public release candidates for a major release (3.1 RC1).
        # 'appVersion' and oldAppVersion are optional definitions used in places that
        # 'don''t care about what we call it. Eg, when version bumping we will bump to
        # 'appVersion', not version.
        'version'                    : '8.0b4',
        'oldVersion'                 : '8.0b3',
        'appVersion'                 : '8.0', # no 'b1' suffix for betas
        'oldAppVersion'              : '8.0',
        'buildNumber'                : 2,
        'oldBuildNumber'             : 2,
        'baseTag'                    : 'THUNDERBIRD_8_0b4',
        'oldBaseTag'                 : 'THUNDERBIRD_8_0b3',
        #XXX: 'Not' entirely certain if/where this is used.
        # 'Derived' from mozillaRelbranchOverride. eg: COMM19211_20101004_RELBRANCH == 1.9.2.11
        'milestone'                  : '8.0',
        # 'The' old version is the revision from which we should generate update snippets.
        'enable_weekly_bundle'       : True,
        'enUSPlatforms'              : ('linux', 'linux64', 'win32', 'macosx64'),
        #'l10nPlatforms'              : (),
        'xulrunnerPlatforms'         : (),
        'patcherConfig'              : 'mozBeta-thunderbird-branch-patcher2.cfg',
        'patcherToolsTag'            : 'UPDATE_PACKAGING_R15',
        'snippetSchema'              : 1,
        'ftpServer'                  : 'ftp.mozilla.org',
        'stagingServer'              : 'stage-old.mozilla.org',
        'bouncerServer'              : 'download.mozilla.org',
        'releaseNotesUrl'            : 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%',
        'ausUser'                    : 'tbirdbld',
        'ausSshKey'                  : 'tbirdbld_dsa',
        'ausServerUrl'               : 'https://aus2.mozillamessaging.com',
        'testOlderPartials'          : False,
        'doPartnerRepacks'           : False,
        'partnersRepoPath'           : 'users/bugzilla_standard8.plus.com/tb-partner-repacks',
        # All of the beta and (if applicable) release channel information
        # is dependent on the useBetaChannel flag
        'useBetaChannel'             : 0,
        'verifyConfigs'              : {'linux'   : 'moz20-thunderbird-linux.cfg',
                                        'linux64' : 'moz20-thunderbird-linux64.cfg',
                                        'macosx64': 'moz20-thunderbird-mac64.cfg',
                                        'win32'   : 'moz20-thunderbird-win32.cfg'},
        'packageTests'               : True,
        #XXX: Should really be obtained from config.py, but this will do for now.
        'unittestMasters'            : [ ('momo-vm-03.sj.mozillamessaging.com:9010',False,3), ],

        # 'Version' numbers we are updating _TO_
        # 'N'/A for Thunderbird 3.x (until the next major version is released)
        'majorUpdateRepoPath'    : '',
        'majorUpdateSourceRepoPath' : '',
        'majorUpdateToVersion'   : '',
        'majorUpdateAppVersion'  : '',
        'majorUpdateBuildNumber' : '',
        'majorUpdateBaseTag'     : '',
        'majorUpdateReleaseNotesUrl' : '',
        'majorUpdatePatcherConfig' : '',
        'majorUpdateVerifyConfigs' : {'linux':  '',
                                    'linux64': '',
                                    'macosx64': '',
                                    'win32':  ''},
    },
    'release': {
        'hgUsername'                 : 'tbirdbld',
        'hgSshKey'                   : '~cltbld/.ssh/tbirdbld_dsa',
        'relbranchPrefix'            : 'COMM',
        'sourceRepoName'             : 'comm-release', # buildbot branch name
        'sourceRepoPath'             : 'releases/comm-release',
        'oldRepoPath'                : 'releases/comm-release',
        'sourceRepoRevision'         : 'e69130e0a43e',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        'relbranchOverride'          : '',
        'mozillaRepoPath'            : 'releases/mozilla-release',
        'mozillaRepoRevision'        : '58f3edbff1b9',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        # 'You' typically want to set this to the gecko relbranch if doing a release off
        # 'a' specific gecko version.
        'mozillaRelbranchOverride'   : 'GECKO701_2011092812_RELBRANCH', # put Gecko relbranch here that we base upon
        'inspectorRepoPath'          : '', #'dom-inspector', # leave empty if inspector is not to be tagged
        'inspectorRepoRevision'      : '',
        'inspectorRelbranchOverride' : '',
        'buildToolsRepoPath'            : '', # leave empty if buildTools is not to be tagged
        'buildToolsRepoRevision'        : '',
        #buildToolsRepoRevision        : '479375734669'
        'buildToolsRelbranchOverride'   : '',
        'venkmanRepoPath'            : '', # leave empty if venkman is not to be tagged
        'venkmanRepoRevision'        : '',
        'venkmanRelbranchOverride'   : '',
        'chatzillaCVSRoot'           : '',
        'chatzillaTimestamp'         : '', # leave empty if chatzilla is not to be tagged
        'l10nRepoPath'               : 'releases/l10n/mozilla-release',
        'l10nRevisionFile'           : 'l10n-thunderbird-changesets-release',
        'toolsRepoPath'              : 'build/tools',
        'buildToolsRepoPath'	   : '',
        'mergeLocales'               : True,
        'cvsroot'                    : ':ext:tbirdbld@cvs.mozilla.org:/cvsroot', # for patcher, etc.
        'productVersionFile'         : 'mail/config/version.txt',
        'productName'                : 'thunderbird',
        'binaryName'                 : 'thunderbird',
        'oldBinaryName'              : 'thunderbird',
        'brandName'                  : 'Thunderbird',
        'appName'                    : APP_NAME,
        'ftpName'                    : APP_NAME,
        # 'Sometimes' we need the application version to be different from what we "call"
        # 'the' build, eg public release candidates for a major release (3.1 RC1).
        # 'appVersion' and oldAppVersion are optional definitions used in places that
        # 'don''t care about what we call it. Eg, when version bumping we will bump to
        # 'appVersion', not version.
        'version'                    : '7.0.1',
        'oldVersion'                 : '7.0',
        'appVersion'                 : '7.0.1', # no 'b1' suffix for betas
        'oldAppVersion'              : '7.0',
        'buildNumber'                : 1,
        'oldBuildNumber'             : 1,
        'baseTag'                    : 'THUNDERBIRD_7_0_1',
        'oldBaseTag'                 : 'THUNDERBIRD_7_0',
        #XXX: 'Not' entirely certain if/where this is used.
        # 'Derived' from mozillaRelbranchOverride. eg: COMM19211_20101004_RELBRANCH == 1.9.2.11
        'milestone'                  : '7.0.1',
        'enable_weekly_bundle'       : False,
        'enUSPlatforms'              : ('linux', 'linux64', 'win32', 'macosx64'),
        #'l10nPlatforms'              : (),
        'xulrunnerPlatforms'         : (),
        'patcherConfig'              : 'mozRelease-thunderbird-branch-patcher2.cfg',
        'patcherToolsTag'            : 'UPDATE_PACKAGING_R15',
        'snippetSchema'              : 1,
        'ftpServer'                  : 'ftp.mozilla.org',
        'stagingServer'              : 'stage-old.mozilla.org',
        'bouncerServer'              : 'download.mozilla.org',
        'releaseNotesUrl'            : 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%',
        'ausUser'                    : 'tbirdbld',
        'ausSshKey'                  : 'tbirdbld_dsa',
        'ausServerUrl'               : 'https://aus2.mozillamessaging.com',
        'testOlderPartials'          : False,
        'doPartnerRepacks'           : False,
        'partnersRepoPath'           : 'users/bugzilla_standard8.plus.com/tb-partner-repacks',
        # All of the beta and (if applicable) release channel information
        # is dependent on the useBetaChannel flag
        'useBetaChannel'             : 1,
        'verifyConfigs'              : {'linux'   : 'moz20-thunderbird-linux.cfg',
                                        'linux64' : 'moz20-thunderbird-linux64.cfg',
                                        'macosx64': 'moz20-thunderbird-mac64.cfg',
                                        'win32'   : 'moz20-thunderbird-win32.cfg'},
        'packageTests'               : True,
        #XXX: Should really be obtained from config.py, but this will do for now.
        'unittestMasters'            : [ ('momo-vm-03.sj.mozillamessaging.com:9010',False,3), ],

        # 'Version' numbers we are updating _TO_
        # 'N'/A for Thunderbird 3.x (until the next major version is released)
        'majorUpdateRepoPath'    : '',
        'majorUpdateSourceRepoPath' : '',
        'majorUpdateToVersion'   : '',
        'majorUpdateAppVersion'  : '',
        'majorUpdateBuildNumber' : '',
        'majorUpdateBaseTag'     : '',
        'majorUpdateReleaseNotesUrl' : '',
        'majorUpdatePatcherConfig' : '',
        'majorUpdateVerifyConfigs' : {'linux':  '',
                                    'linux64': '',
                                    'macosx64': '',
                                    'win32':  ''},
    },
}

# copy variables that are just aliases
for gloKey in gloConfig:
    for copy, orig in [
                   ['appVersion', 'version'],
                   ['oldAppVersion', 'oldVersion'],
                   ['l10nPlatforms', 'enUSPlatforms'],
                   ['unittestPlatforms', 'enUSPlatforms'],
                   ['appVersion', 'version'],
                   ['majorUpdateAppVersion', 'majorUpdateToVersion'],
                  ]:
         if not copy in gloConfig[gloKey]:
             gloConfig[gloKey][copy] = gloConfig[gloKey][orig]


builders = []
all_builders = []
test_builders = []
all_test_builders = []
schedulers = []
change_source = []
status = []
weeklyBuilders = []
 
for gloKey in gloConfig:

    sourceRepoName             = gloConfig[gloKey]['sourceRepoName']
    toolsRepoPath              = gloConfig[gloKey]['toolsRepoPath']
    stagingServer              = gloConfig[gloKey]['stagingServer']
    productName                = gloConfig[gloKey]['productName']
    version                    = gloConfig[gloKey]['version']
    buildNumber                = gloConfig[gloKey]['buildNumber']
    sourceRepoPath             = gloConfig[gloKey]['sourceRepoPath']
    xulrunnerPlatforms         = gloConfig[gloKey]['xulrunnerPlatforms']
    enUSPlatforms              = gloConfig[gloKey]['enUSPlatforms']
    l10nPlatforms              = gloConfig[gloKey]['l10nPlatforms']
    baseTag                    = gloConfig[gloKey]['baseTag']
    appName                    = gloConfig[gloKey]['appName']
    doPartnerRepacks           = gloConfig[gloKey]['doPartnerRepacks']
    verifyConfigs              = gloConfig[gloKey]['verifyConfigs']
    majorUpdateRepoPath        = gloConfig[gloKey]['majorUpdateRepoPath']
    majorUpdateVerifyConfigs   = gloConfig[gloKey]['majorUpdateVerifyConfigs']
    unittestPlatforms          = gloConfig[gloKey]['unittestPlatforms']
    sourceRepoRevision         = gloConfig[gloKey]['sourceRepoRevision']
    relbranchOverride          = gloConfig[gloKey]['relbranchOverride']
    productVersionFile         = gloConfig[gloKey]['productVersionFile']
    mozillaRepoRevision        = gloConfig[gloKey]['mozillaRepoRevision']
    mozillaRelbranchOverride   = gloConfig[gloKey]['mozillaRelbranchOverride']
    mozillaRepoPath            = gloConfig[gloKey]['mozillaRepoPath']
    buildToolsRepoPath         = gloConfig[gloKey]['buildToolsRepoPath']
    inspectorRepoPath          = gloConfig[gloKey]['inspectorRepoPath']
    inspectorRepoRevision      = gloConfig[gloKey]['inspectorRepoRevision']
    inspectorRelbranchOverride = gloConfig[gloKey]['inspectorRelbranchOverride']
    venkmanRepoPath            = gloConfig[gloKey]['venkmanRepoPath']
    l10nRevisionFile           = gloConfig[gloKey]['l10nRevisionFile']
    l10nRepoPath               = gloConfig[gloKey]['l10nRepoPath']
    ftpName                    = gloConfig[gloKey]['ftpName']
    appVersion                 = gloConfig[gloKey]['appVersion']
    milestone                  = gloConfig[gloKey]['milestone']
    hgUsername                 = gloConfig[gloKey]['hgUsername']
    hgSshKey                   = gloConfig[gloKey]['hgSshKey']
    relbranchPrefix            = gloConfig[gloKey]['relbranchPrefix']
    chatzillaCVSRoot           = gloConfig[gloKey]['chatzillaCVSRoot']
    brandName                  = gloConfig[gloKey]['brandName']
    binaryName                 = gloConfig[gloKey]['binaryName']
    cvsroot                    = gloConfig[gloKey]['cvsroot']
    oldVersion                 = gloConfig[gloKey]['oldVersion']
    oldBuildNumber             = gloConfig[gloKey]['oldBuildNumber']
    patcherToolsTag            = gloConfig[gloKey]['patcherToolsTag']
    patcherConfig              = gloConfig[gloKey]['patcherConfig']
    oldAppVersion              = gloConfig[gloKey]['oldAppVersion']
    oldRepoPath                = gloConfig[gloKey].get('oldRepoPath', sourceRepoPath)
    oldBaseTag                 = gloConfig[gloKey]['oldBaseTag']
    oldBinaryName              = gloConfig[gloKey]['oldBinaryName']
    enableWeeklyBundle         = gloConfig[gloKey]['enable_weekly_bundle']
    ftpServer                  = gloConfig[gloKey]['ftpServer']
    bouncerServer              = gloConfig[gloKey]['bouncerServer']
    useBetaChannel             = gloConfig[gloKey]['useBetaChannel']
    ausServerUrl               = gloConfig[gloKey]['ausServerUrl']
    releaseNotesUrl            = gloConfig[gloKey]['releaseNotesUrl']
    testOlderPartials          = gloConfig[gloKey]['testOlderPartials']
    majorUpdateSourceRepoPath  = gloConfig[gloKey]['majorUpdateSourceRepoPath']
    majorUpdatePatcherConfig   = gloConfig[gloKey]['majorUpdatePatcherConfig']
    majorUpdateToVersion       = gloConfig[gloKey]['majorUpdateToVersion']
    majorUpdateAppVersion      = gloConfig[gloKey]['majorUpdateAppVersion']
    majorUpdateBaseTag         = gloConfig[gloKey]['majorUpdateBaseTag']
    majorUpdateBuildNumber     = gloConfig[gloKey]['majorUpdateBuildNumber']
    ausUser                    = gloConfig[gloKey]['ausUser']
    ausSshKey                  = gloConfig[gloKey]['ausSshKey']
    majorUpdateReleaseNotesUrl = gloConfig[gloKey]['majorUpdateReleaseNotesUrl']
    partnersRepoPath           = gloConfig[gloKey]['partnersRepoPath']
    packageTests               = gloConfig[gloKey]['packageTests']
    unittestMasters            = gloConfig[gloKey]['unittestMasters']
    mergeLocales               = gloConfig[gloKey]['mergeLocales']
    snippetSchema              = gloConfig[gloKey]['snippetSchema']

    branchConfig = nightly_config.BRANCHES[sourceRepoName]

    for v in ['hgurl', 'stage_username','stage_server', 'stage_ssh_key','stage_group','stage_base_path', 'clobber_url']:
        branchConfig[v] = nightly_config.DEFAULTS[v]
        
    branchConfig['hghost'] = nightly_config.HGHOST
    branchConfig['build_tools_repo_path'] = toolsRepoPath
    branchConfig['aus2_host'] = nightly_config.AUS2_HOST
    branchConfig['base_clobber_url'] = nightly_config.BRANCHES[sourceRepoName]['clobber_url']
    
    ##### Change sources and Schedulers
    change_source.append(FtpPoller(
        branch="post_signing_%s" % gloKey,
        ftpURLs=["http://%s/pub/mozilla.org/%s/nightly/%s-candidates/build%s/" \
                 % (stagingServer, productName, version, buildNumber)],
        pollInterval= 60*10,
        searchString='win32_signing_build'
    ))
    
    tag_scheduler = Scheduler(
        name='tag_%s' % gloKey,
        branch=sourceRepoPath,
        treeStableTimer=0,
        builderNames=['tag_%s' % gloKey],
        fileIsImportant=lambda c: not isHgPollerTriggered(c, branchConfig['hgurl'])
    )
    schedulers.append(tag_scheduler)
    source_scheduler = Dependent(
        name='source_%s' % gloKey,
        upstream=tag_scheduler,
        builderNames=['source_%s' % gloKey]
    )
    schedulers.append(source_scheduler)
    
    if xulrunnerPlatforms:
        xulrunner_source_scheduler = Dependent(
            name='xulrunner_source_%s' % gloKey,
            upstream=tag_scheduler,
            builderNames=['xulrunner_source_%s' % gloKey]
        )
        schedulers.append(xulrunner_source_scheduler)
    
    for platform in enUSPlatforms:
        build_scheduler = Dependent(
            name='%s_build_%s' % (platform, gloKey),
            upstream=tag_scheduler,
            builderNames=['%s_build_%s' % (platform, gloKey)]
        )
        schedulers.append(build_scheduler)
        if platform in l10nPlatforms:
            repack_scheduler = DependentL10n(
                name='%s_repack_%s' % (platform, gloKey),
                platform=platform,
                upstream=build_scheduler,
                builderNames=['%s_repack_%s' % (platform, gloKey)],
                branch=sourceRepoPath,
                baseTag='%s_RELEASE' % baseTag,
                localesFile='%s/locales/shipped-locales' % appName,
                # If a few locales are needed, do this instead:
                #locales={ 'zh-TW': ['linux']},
            )
            schedulers.append(repack_scheduler)
    
    for platform in xulrunnerPlatforms:
        xulrunner_build_scheduler = Dependent(
            name='xulrunner_%s_build_%s' % (platform, gloKey),
            upstream=tag_scheduler,
            builderNames=['xulrunner_%s_build_%s' % (platform, gloKey)]
        )
        schedulers.append(xulrunner_build_scheduler)
    
    if doPartnerRepacks:
        for platform in l10nPlatforms:
            partner_scheduler = Scheduler(
                name='partner_repacks_%s_%s' % (platform, gloKey),
                treeStableTimer=0,
                branch='post_signing_%s_%s' % (platform, gloKey),
                builderNames=['partner_repack_%s_%s' % (platform, gloKey)],
            )
            schedulers.append(partner_scheduler)
    
    for platform in l10nPlatforms:
        l10n_verify_scheduler = Scheduler(
            name='%s_l10n_verification_%s' % (platform, gloKey),
            treeStableTimer=0,
            branch='post_signing_%s' % gloKey,
            builderNames=['%s_l10n_verification_%s' % (platform, gloKey)]
        )
        schedulers.append(l10n_verify_scheduler)
    
    updates_scheduler = Scheduler(
        name='updates_%s' % gloKey,
        treeStableTimer=0,
        branch='post_signing_%s' % gloKey,
        builderNames=['updates_%s' % gloKey]
    )
    schedulers.append(updates_scheduler)
    
    updateBuilderNames = []
    for platform in sorted(verifyConfigs.keys()):
        updateBuilderNames.append('%s_update_verify_%s' % (platform, gloKey))
    update_verify_scheduler = Dependent(
        name='update_verify_%s' % gloKey,
        upstream=updates_scheduler,
        builderNames=updateBuilderNames
    )
    schedulers.append(update_verify_scheduler)
    
    if majorUpdateRepoPath:
        majorUpdateBuilderNames = []
        for platform in sorted(majorUpdateVerifyConfigs.keys()):
            majorUpdateBuilderNames.append('%s_major_update_verify_%s' % (platform, gloKey))
        major_update_verify_scheduler = Triggerable(
            name='major_update_verify_%s' % gloKey,
            builderNames=majorUpdateBuilderNames
        )
        schedulers.append(major_update_verify_scheduler)
    
    for platform in unittestPlatforms:

        if unittestMasters:
            test_platforms = [platform]
            if platform == 'macosx64':
                test_platforms = ['macosx64', 'macosx']

            for test_platform in test_platforms:
                platform_test_builders = []
                #for suites_name, suites in branchConfig['unittest_suites']:
                for suites_name, suites in [('xpcshell', ['xpcshell']),('mozmill', ['mozmill'])]:
                    #platform_test_builders.extend(generateTestBuilderNames('%s_test_%s' % (platform, gloKey), suites_name, suites))
                    platform_test_builders.append('%s_unittest_%s_%s' % (test_platform, suites_name, gloKey))

                s = Scheduler(
                    name='%s_release_unittest_%s_%s' % (test_platform, suites_name, gloKey),
                    treeStableTimer=0,
                    branch='release-%s-%s-opt-unittest_%s' % (sourceRepoName, platform, gloKey),
                    builderNames=platform_test_builders,
                    )
                schedulers.append(s)
    
    # Purposely, there is not a Scheduler for ReleaseFinalVerification
    # This is a step run very shortly before release, and is triggered manually
    # from the waterfall
    
    ##### Builders
    repositories = {
        sourceRepoPath: {
            'revision': sourceRepoRevision,
            'relbranchOverride': relbranchOverride,
            'bumpFiles': [productVersionFile]
        },
        mozillaRepoPath: {
            'revision': mozillaRepoRevision,
            'relbranchOverride': mozillaRelbranchOverride,
            'bumpFiles': []
        },
    }
    
    if buildToolsRepoPath:
        repositories[buildToolsRepoPath] = {
            'revision': buildToolsRepoRevision,
            'relbranchOverride': buildToolsRelbranchOverride,
            'bumpFiles': []
        }
    
    if inspectorRepoPath:
        repositories[inspectorRepoPath] = {
            'revision': inspectorRepoRevision,
            'relbranchOverride': inspectorRelbranchOverride,
            'bumpFiles': []
        }
    if venkmanRepoPath:
        repositories[venkmanRepoPath] = {
            'revision': venkmanRepoRevision,
            'relbranchOverride': venkmanRelbranchOverride,
            'bumpFiles': []
        }
    if len(l10nPlatforms) > 0:
        l10n_repos = get_l10n_repositories(l10nRevisionFile, l10nRepoPath,
                                           relbranchOverride)
        repositories.update(l10n_repos)
    
    
    # dummy factory for TESTING purposes
    from buildbot.process.factory import BuildFactory
    from buildbot.steps.dummy import Dummy
    dummy_factory = BuildFactory()
    dummy_factory.addStep(Dummy())
    
    tag_factory = ReleaseTaggingFactory(
        hgHost=branchConfig['hghost'],
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        repositories=repositories,
        productName=productName,
        appName=ftpName,
        version=version,
        appVersion=appVersion,
        milestone=milestone,
        baseTag=baseTag,
        buildNumber=buildNumber,
        hgUsername=hgUsername,
        hgSshKey=hgSshKey,
        relbranchPrefix=relbranchPrefix,
        clobberURL=branchConfig['base_clobber_url'],
    )
    
    builders.append({
        'name': 'tag_%s' % gloKey,
        'slavenames': branchConfig['platforms']['linux']['slaves'],
        'category': 'release',
        'builddir': 'tag_%s' % gloKey,
        'factory': tag_factory,
    })
    
    
    source_factory = CCSourceFactory(
        hgHost=branchConfig['hghost'],
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        repoPath=sourceRepoPath,
        productName=productName,
        version=version,
        baseTag=baseTag,
        stagingServer=nightly_config.STAGE_SERVER,
        stageUsername=branchConfig['stage_username'],
        stageSshKey=branchConfig['stage_ssh_key'],
        buildNumber=buildNumber,
        mozRepoPath=mozillaRepoPath,
        inspectorRepoPath=inspectorRepoPath,
        venkmanRepoPath=venkmanRepoPath,
        cvsroot=chatzillaCVSRoot,
        autoconfDirs=['.', 'mozilla', 'mozilla/js/src'],
        clobberURL=branchConfig['base_clobber_url'],
    )
    
    builders.append({
        'name': 'source_%s' % gloKey,
        'slavenames': branchConfig['platforms']['linux']['slaves'],
        'category': 'release',
        'builddir': 'source_%s' % gloKey,
        'factory': source_factory,
    })
    
    if xulrunnerPlatforms:
        xulrunner_source_factory = SingleSourceFactory(
            hgHost=branchConfig['hghost'],
            buildToolsRepoPath=branchConfig['build_tools_repo_path'],
            repoPath=sourceRepoPath,
            productName='xulrunner',
            version=milestone,
            baseTag=baseTag,
            stagingServer=branchConfig['stage_server'],
            stageUsername=branchConfig['stage_username_xulrunner'],
            stageSshKey=branchConfig['stage_ssh_xulrunner_key'],
            buildNumber=buildNumber,
            autoconfDirs=['.', 'js/src'],
            clobberURL=branchConfig['base_clobber_url'],
        )
    
        builders.append({
           'name': 'xulrunner_source_%s' % gloKey,
           'slavenames': branchConfig['platforms']['linux']['slaves'],
           'category': 'release',
           'builddir': 'xulrunner_source_%s' % gloKey,
           'factory': xulrunner_source_factory
        })
    
    for platform in enUSPlatforms:
        # shorthand
        pf = nightly_config.BRANCHES[sourceRepoName]['platforms'][platform]
        mozconfig = '%s/%s/release' % (platform, sourceRepoName)

        if platform in unittestPlatforms:
            packageTests = True
            unittestMasters = branchConfig['unittest_masters']
            unittestBranch = 'release-%s-%s-opt-unittest_%s' % (sourceRepoName,
                                                                platform, gloKey)
        else:
            packageTests = False
            unittestMasters = None
            unittestBranch = None

        build_factory = CCReleaseBuildFactory(
            env=pf['env'],
            objdir=pf['platform_objdir'],
            platform=platform,
            hgHost=branchConfig['hghost'],
            repoPath=sourceRepoPath,
            mozRepoPath=mozillaRepoPath,
            inspectorRepoPath=inspectorRepoPath,
            venkmanRepoPath=venkmanRepoPath,
            cvsroot=chatzillaCVSRoot,
            buildToolsRepoPath=branchConfig['build_tools_repo_path'],
            configRepoPath=nightly_config.CONFIG_REPO_PATH,
            configSubDir=nightly_config.CONFIG_SUBDIR,
            profiledBuild=pf['profiled_build'],
            mozconfig=mozconfig,
            buildRevision='%s_RELEASE' % baseTag,
            stageServer=nightly_config.STAGE_SERVER,
            stageUsername=branchConfig['stage_username'],
            stageGroup=nightly_config.BRANCHES[sourceRepoName]['stage_group'],
            stageSshKey=branchConfig['stage_ssh_key'],
            stageBasePath=nightly_config.BRANCHES[sourceRepoName]['stage_base_path'],
            codesighs=False,
            uploadPackages=True,
            uploadSymbols=True,
            createSnippet=False,
            doCleanup=True, # this will clean-up the mac build dirs, but not delete
                            # the entire thing
            buildSpace=10,
            productName=productName,
            version=version,
            buildNumber=buildNumber,
            clobberURL=branchConfig['base_clobber_url'],
            packageTests=packageTests,
            unittestMasters=unittestMasters,
            unittestBranch=unittestBranch,
        )
    
        builders.append({
            'name': '%s_build_%s' % (platform, gloKey),
            'slavenames': pf['slaves'],
            'category': 'release',
            'builddir': '%s_build_%s' % (platform, gloKey),
            'factory': build_factory,
        })
        if platform in l10nPlatforms:
            repack_factory = CCReleaseRepackFactory(
                hgHost=branchConfig['hghost'],
                project=productName,
                appName=appName,
                brandName=brandName,
                repoPath=sourceRepoPath,
                mozRepoPath=mozillaRepoPath,
                inspectorRepoPath=inspectorRepoPath,
                venkmanRepoPath=venkmanRepoPath,
                cvsroot=chatzillaCVSRoot,
                l10nRepoPath=l10nRepoPath,
                stageServer=nightly_config.STAGE_SERVER,
                stageUsername=branchConfig['stage_username'],
                stageSshKey=branchConfig['stage_ssh_key'],
                buildToolsRepoPath=branchConfig['build_tools_repo_path'],
                compareLocalesRepoPath=nightly_config.COMPARE_LOCALES_REPO_PATH,
                compareLocalesTag=nightly_config.COMPARE_LOCALES_TAG,
                buildSpace=5,
                configRepoPath=nightly_config.CONFIG_REPO_PATH,
                configSubDir=nightly_config.CONFIG_SUBDIR,
                mozconfig=mozconfig,
                platform=platform,
                buildRevision='%s_RELEASE' % baseTag,
                version=version,
                buildNumber=buildNumber,
                clobberURL=branchConfig['base_clobber_url'],
                mergeLocales=mergeLocales,
            )

            builders.append({
                'name': '%s_repack_%s' % (platform, gloKey),
                'slavenames': pf['slaves'],
                'category': 'release',
                'builddir': '%s_repack_%s' % (platform, gloKey),
                'factory': repack_factory,
            })

        if unittestMasters:
            mochitestLeakThreshold = pf.get('mochitest_leak_threshold', None)
            crashtestLeakThreshold = pf.get('crashtest_leak_threshold', None)
            for suites_name, suites in [('xpcshell', ['xpcshell']),('mozmill', ['mozmill'])]:
                # Release builds on mac don't have a11y enabled, do disable the mochitest-a11y test
                if platform.startswith('macosx') and 'mochitest-a11y' in suites:
                    suites = suites[:]
                    suites.remove('mochitest-a11y')

                test_platforms = [platform]
                # want to run opt-unittests on osx 10.5 and 10.6
                if platform == 'macosx64':
                    test_platforms = ['macosx64', 'macosx']
                for test_platform in test_platforms:
                    #XXX: This is making a funny assumption, really
                    #XXX: Look for this unittest platform in the current branch/config
                    #XXX: Otherwise, also look at the bloat config, hoping to find it there
                    if branchConfig['platforms'].get(test_platform):
                       tpf = branchConfig['platforms'][test_platform]
                    elif nightly_config.BRANCHES['%s-bloat' % sourceRepoName]['platforms'].get(test_platform):
                       tpf = nightly_config.BRANCHES['%s-bloat' % sourceRepoName]['platforms'][test_platform]
                    else:
                       raise "Can't find os settings for %s on branch %s" % (test_platform, sourceRepoName)
              
                    release_packaged_tests_factory = UnittestPackagedBuildFactory(
                        platform=test_platform,
                        test_suites=suites,
                        productName=productName,
                        hgHost=branchConfig['hghost'],
                        repoPath=sourceRepoPath,
                        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
                        buildSpace=1.0,
                        downloadSymbols=True,
                        buildsBeforeReboot=tpf.get('builds_before_reboot', 0),
                        env={},
                    )
      
                    unittest_builder_name = '%s_unittest_%s_%s' % (test_platform, suites_name, gloKey)
      
                    builder = {
                        'name': unittest_builder_name,
                        'slavenames': tpf['test-slaves'],
                        'builddir': '%s-unittest-%s-%s' % (test_platform, suites_name, gloKey),
                        'factory': release_packaged_tests_factory,
                        'category': 'release',
                    }
                    test_builders.append(builder)

#                test_builders.extend(generateTestBuilder(
#                    branchConfig, 'release', platform, "%s_test" % platform,
#                    'release-%s-%s-opt-unittest' % (sourceRepoName, platform),
#                    suites_name, suites, mochitestLeakThreshold,
#                    crashtestLeakThreshold))
    
    
    if doPartnerRepacks:
        for platform in l10nPlatforms:
            partner_repack_factory = PartnerRepackFactory(
                hgHost=branchConfig['hghost'],
                repoPath=sourceRepoPath,
                mozRepoPath=mozillaRepoPath,
                buildToolsRepoPath=branchConfig['build_tools_repo_path'],
                productName=productName,
                version=version,
                buildNumber=buildNumber,
                partnersRepoPath=partnersRepoPath,
                platformList=[platform], 
                stagingServer=stagingServer,
                stageUsername=branchConfig['stage_username'],
                stageSshKey=branchConfig['stage_ssh_key'],    
            )
        
            builders.append({
                'name': 'partner_repack_%s_%s' % (platform, gloKey),
                'slavenames': branchConfig['platforms']['macosx']['slaves'],
                'category': 'release',
                'builddir': 'partner_repack_%s_%s' % (platform, gloKey),
                'factory': partner_repack_factory,
            })
    
    for platform in l10nPlatforms:
        l10n_verification_factory = L10nVerifyFactory(
            hgHost=branchConfig['hghost'],
            buildToolsRepoPath=branchConfig['build_tools_repo_path'],
            cvsroot=cvsroot,
            stagingServer=stagingServer,
            stagingUser='tbirdbld',
            productName=productName,
            version=version,
            buildNumber=buildNumber,
            oldVersion=oldVersion,
            oldBuildNumber=oldBuildNumber,
            clobberURL=branchConfig['base_clobber_url'],
            platform=platform,
        )

        l10n_verification_slaves = []
        if ('macosx' in branchConfig['platforms']):
            l10n_verification_slaves = branchConfig['platforms']['macosx']['slaves']
        else:
            l10n_verification_slaves = branchConfig['platforms']['macosx64']['slaves']
        builders.append({
            'name': '%s_l10n_verification_%s' % (platform, gloKey),
            'slavenames': l10n_verification_slaves,
            'category': 'release',
            'builddir': '%s_l10n_verification_%s' % (platform, gloKey),
            'factory': l10n_verification_factory,
        })
    
    
    updates_factory = ReleaseUpdatesFactory(
        hgHost=branchConfig['hghost'],
        repoPath=sourceRepoPath,
        mozRepoPath=mozillaRepoPath,
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        cvsroot=cvsroot,
        patcherToolsTag=patcherToolsTag,
        patcherConfig=patcherConfig,
        verifyConfigs=verifyConfigs,
        appName=appName,
        binaryName=binaryName,
        productName=productName,
        brandName=brandName,
        version=version,
        appVersion=appVersion,
        baseTag=baseTag,
        buildNumber=buildNumber,
        oldVersion=oldVersion,
        oldAppVersion=oldAppVersion,
        oldBaseTag=oldBaseTag,
        oldBuildNumber=oldBuildNumber,
        oldBinaryName=oldBinaryName,
        ftpServer=ftpServer,
        bouncerServer=bouncerServer,
        stagingServer=stagingServer,
        useBetaChannel=useBetaChannel,
        stageUsername=branchConfig['stage_username'],
        stageSshKey=branchConfig['stage_ssh_key'],
        ausUser=nightly_config.AUS2_USER,
        ausSshKey=nightly_config.AUS2_SSH_KEY,
        ausHost=nightly_config.AUS2_HOST,
        ausServerUrl=ausServerUrl,
        hgSshKey=hgSshKey,
        hgUsername=hgUsername,
        clobberURL=branchConfig['base_clobber_url'],
        oldRepoPath=oldRepoPath,
        releaseNotesUrl=releaseNotesUrl,
        testOlderPartials=testOlderPartials,
        schema=snippetSchema,
    )
    
    builders.append({
        'name': 'updates_%s' % gloKey,
        'slavenames': branchConfig['platforms']['linux']['slaves'],
        'category': 'release',
        'builddir': 'updates_%s' % gloKey,
        'factory': updates_factory,
    })
    
    
    for platform in sorted(verifyConfigs.keys()):
        update_verify_factory = UpdateVerifyFactory(
            hgHost=branchConfig['hghost'],
            buildToolsRepoPath=branchConfig['build_tools_repo_path'],
            verifyConfig=verifyConfigs[platform],
            clobberURL=branchConfig['base_clobber_url'],
        )
    
        builders.append({
            'name': '%s_update_verify_%s' % (platform, gloKey),
            'slavenames': branchConfig['platforms'][platform]['slaves'],
            'category': 'release',
            'builddir': '%s_update_verify_%s' % (platform, gloKey),
            'factory': update_verify_factory,
        })
    
    
    final_verification_factory = ReleaseFinalVerification(
        hgHost=branchConfig['hghost'],
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        verifyConfigs=verifyConfigs,
        clobberURL=branchConfig['base_clobber_url'],
    )
    
    builders.append({
        'name': 'final_verification_%s' % gloKey,
        'slavenames': branchConfig['platforms']['linux']['slaves'],
        'category': 'release',
        'builddir': 'final_verification_%s' % gloKey,
        'factory': final_verification_factory,
    })
    
    if majorUpdateRepoPath:
        # Not attached to any Scheduler
        major_update_factory = MajorUpdateFactory(
            hgHost=branchConfig['hghost'],
            repoPath=majorUpdateSourceRepoPath,
            mozRepoPath=majorUpdateRepoPath,
            buildToolsRepoPath=branchConfig['build_tools_repo_path'],
            cvsroot=cvsroot,
            patcherToolsTag=patcherToolsTag,
            patcherConfig=majorUpdatePatcherConfig,
            verifyConfigs=majorUpdateVerifyConfigs,
            appName=ftpName,
            productName=productName,
            version=majorUpdateToVersion,
            appVersion=majorUpdateAppVersion,
            baseTag=majorUpdateBaseTag,
            buildNumber=majorUpdateBuildNumber,
            oldVersion=version,
            oldAppVersion=appVersion,
            oldBaseTag=baseTag,
            oldBuildNumber=buildNumber,
            ftpServer=ftpServer,
            bouncerServer=bouncerServer,
            stagingServer=stagingServer,
            useBetaChannel=useBetaChannel,
            stageUsername=branchConfig['stage_username'],
            stageSshKey=branchConfig['stage_ssh_key'],
            ausUser=ausUser,
            ausSshKey=ausSshKey,
            ausHost=branchConfig['aus2_host'],
            ausServerUrl=ausServerUrl,
            hgSshKey=hgSshKey,
            hgUsername=hgUsername,
            clobberURL=branchConfig['base_clobber_url'],
            oldRepoPath=oldRepoPath,
            triggerSchedulers=['major_update_verify_%s' % gloKey],
            releaseNotesUrl=majorUpdateReleaseNotesUrl,
            testOlderPartials=testOlderPartials,
            schema=snippetSchema,
        )
        
        builders.append({
            'name': 'major_update_%s' % gloKey,
            'slavenames': branchConfig['platforms']['linux']['slaves'],
            'category': 'release',
            'builddir': 'major_update_%s' % gloKey,
            'factory': major_update_factory,
        })
        
        for platform in sorted(majorUpdateVerifyConfigs.keys()):
            major_update_verify_factory = UpdateVerifyFactory(
                hgHost=branchConfig['hghost'],
                buildToolsRepoPath=branchConfig['build_tools_repo_path'],
                verifyConfig=majorUpdateVerifyConfigs[platform],
                clobberURL=branchConfig['base_clobber_url'],
            )
        
            builders.append({
                'name': '%s_major_update_verify_%s' % (platform, gloKey),
                'slavenames': branchConfig['platforms'][platform]['slaves'],
                'category': 'release',
                'builddir': '%s_major_update_verify_%s' % (platform, gloKey),
                'factory': major_update_verify_factory,
            })

    if enableWeeklyBundle:
        name = sourceRepoPath
        weeklyBuilders.append('%s hg bundle' % name)
        bundle_factory = ScriptFactory(
            branchConfig['hgurl'] + branchConfig['build_tools_repo_path'],
            'scripts/bundle/hg-bundle.sh',
            interpreter='bash',
            script_timeout=3600,
            script_maxtime=3600,
            extra_args=[
                name,
                sourceRepoPath,
                branchConfig['stage_server'],
                branchConfig['stage_username'],
                branchConfig['stage_base_path'],
                branchConfig['stage_ssh_key'],
                ],
        )
        slaves = set()
        # can bundle sources on any platform
        for p in sorted(branchConfig['platforms'].keys()):
            slaves.update(set(branchConfig['platforms'][p]['slaves']))
        bundle_builder = {
            'name': '%s hg bundle' % name,
            'slavenames': list(slaves),
            'builddir': '%s-bundle' % (name,),
            'slavebuilddir': ('%s-bundle' % (name,)),
            'factory': bundle_factory,
            'category': name,
            #'nextSlave': _nextSlowSlave,
            'properties': {'slavebuilddir': ('%s-bundle' % (name,))}
        }
        builders.append(bundle_builder)

    weekly_scheduler=Nightly(
            name='weekly-%s' % gloKey,
            branch=sourceRepoPath,
            dayOfWeek=5, # Saturday
            hour=[3], minute=[02],
            builderNames=weeklyBuilders,
            )
    schedulers.append(weekly_scheduler)
    
    status.append(TinderboxMailNotifier(
        fromaddr="thunderbird2.buildbot@build.mozilla.org",
        tree=branchConfig["tinderbox_tree"] + "-Release",
        extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org",],
        relayhost="mx.mozillamessaging.com",
        builders=[b['name'] for b in builders],
        logCompression="bzip2")
    )

    status.append(TinderboxMailNotifier(
        fromaddr="thunderbird2.buildbot@build.mozilla.org",
        tree=branchConfig["tinderbox_tree"] + "-Release",
        extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org",],
        relayhost="mx.mozillamessaging.com",
        builders=[b['name'] for b in test_builders],
        logCompression="bzip2",
        errorparser="unittest")
    )

    all_builders.extend(builders)
    all_test_builders.extend(test_builders)
    builders = []
    test_builders = []

builders = all_builders
builders.extend(all_test_builders)
