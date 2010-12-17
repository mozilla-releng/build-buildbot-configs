import os
from buildbot.changes.pb import PBChangeSource
from buildbot.scheduler import Scheduler, Dependent, Triggerable
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
  TuxedoEntrySubmitterFactory
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
        'sourceRepoRevision'         : 'f85a2c5971a3',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        'relbranchOverride'          : 'COMM19213_20101129_RELBRANCH',
        'mozillaRepoPath'            : 'releases/mozilla-1.9.2',
        'mozillaRepoRevision'        : '0c159bd1d600',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        # 'You' typically want to set this to the gecko relbranch if doing a release off
        # 'a' specific gecko version.
        'mozillaRelbranchOverride'   : 'GECKO19213_20101122_RELBRANCH', # put Gecko relbranch here that we base upon
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
        'cvsroot'                    : ':ext:cltbld@cvs.mozilla.org:/cvsroot', # for patcher, etc.
        'productVersionFile'         : 'mail/config/version-192.txt',
        'productName'                : 'thunderbird',
        'brandName'                  : 'Thunderbird',
        'appName'                    : APP_NAME,
        'ftpName'                    : APP_NAME,
        # 'Sometimes' we need the application version to be different from what we "call"
        # 'the' build, eg public release candidates for a major release (3.1 RC1).
        # 'appVersion' and oldAppVersion are optional definitions used in places that
        # 'don''t care about what we call it. Eg, when version bumping we will bump to
        # 'appVersion', not version.
        'version'                    : '3.1.7',
        #'appVersion'                 : version,
        #XXX: 'Not' entirely certain if/where this is used.
        # 'Derived' from mozillaRelbranchOverride. eg: COMM19211_20101004_RELBRANCH == 1.9.2.11
        'milestone'                  : '1.9.2.13',
        'buildNumber'                : 3,
        'baseTag'                    : 'THUNDERBIRD_3_1_7',
        # 'The' old version is the revision from which we should generate update snippets.
        'oldVersion'                 : '3.1.6',
        #'oldAppVersion'              : oldVersion,
        'oldBuildNumber'             : 1,
        'oldBaseTag'                 : 'THUNDERBIRD_3_1_6',
        'enUSPlatforms'              : ('linux', 'win32', 'macosx'),
        'unittestPlatforms'          : (),
        'xulrunnerPlatforms'         : (),
        'patcherConfig'              : 'moz192-thunderbird-branch-patcher2.cfg',
        'patcherToolsTag'            : 'UPDATE_PACKAGING_R11',
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
        'useBetaChannel'             : 1,
        'verifyConfigs'              : {'linux':  'moz192-thunderbird-linux.cfg',
                                      'macosx': 'moz192-thunderbird-mac.cfg',
                                      'win32':  'moz192-thunderbird-win32.cfg'},
        'packageTests'               : False,
        'unittestMasters'            : (),
        
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
                                    'macosx': '',
                                    'win32':  ''},

    },
    '33': {
        'hgUsername'                 : 'tbirdbld',
        'hgSshKey'                   : '~cltbld/.ssh/tbirdbld_dsa',
        'relbranchPrefix'            : 'COMM',
        'sourceRepoName'             : 'comm-central-trunk', # buildbot branch name
        'sourceRepoPath'             : 'comm-central',
        'sourceRepoRevision'         : '21431d746abf',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        'relbranchOverride'          : '',
        'mozillaRepoPath'            : 'mozilla-central',
        'mozillaRepoRevision'        : 'da98fe199be0',
        # 'If' blank, automation will create its own branch based on COMM_<date>_RELBRANCH
        # 'You' typically want to set this to the gecko relbranch if doing a release off
        # 'a' specific gecko version.
        'mozillaRelbranchOverride'   : '', # put Gecko relbranch here that we base upon
        'inspectorRepoPath'          : 'dom-inspector', # leave empty if inspector is not to be tagged
        'inspectorRepoRevision'      : '2001a7394d4f',
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
        'l10nRepoPath'               : 'l10n-central',
        'l10nRevisionFile'           : 'l10n-thunderbird-changesets-3.3',
        'toolsRepoPath'              : 'build/tools',
        'buildToolsRepoPath'	   : '',
        'cvsroot'                    : ':ext:cltbld@cvs.mozilla.org:/cvsroot', # for patcher, etc.
        'productVersionFile'         : 'mail/config/version.txt',
        'productName'                : 'thunderbird',
        'brandName'                  : 'Miramar',
        'appName'                    : APP_NAME,
        'ftpName'                    : APP_NAME,
        # 'Sometimes' we need the application version to be different from what we "call"
        # 'the' build, eg public release candidates for a major release (3.1 RC1).
        # 'appVersion' and oldAppVersion are optional definitions used in places that
        # 'don''t care about what we call it. Eg, when version bumping we will bump to
        # 'appVersion', not version.
        'version'                    : '3.3a1',
        #'appVersion'                 : version,
        #XXX: 'Not' entirely certain if/where this is used.
        # 'Derived' from mozillaRelbranchOverride. eg: COMM19211_20101004_RELBRANCH == 1.9.2.11
        'milestone'                  : '2.0.0.0',
        'buildNumber'                : 1,
        'baseTag'                    : 'THUNDERBIRD_3_3a1',
        # 'The' old version is the revision from which we should generate update snippets.
        'oldVersion'                 : '3.3a1',
        'oldAppVersion'              : '3.3a1',
        'oldBuildNumber'             : 1,
        'oldBaseTag'                 : '',
        'enUSPlatforms'              : ('linux', 'linux64', 'win32', 'macosx64'),
        'l10nPlatforms'              : (),
        'xulrunnerPlatforms'         : (),
        'patcherConfig'              : 'moz20-thunderbird-branch-patcher2.cfg',
        'patcherToolsTag'            : 'UPDATE_PACKAGING_R12',
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
    cvsroot                    = gloConfig[gloKey]['cvsroot']
    oldVersion                 = gloConfig[gloKey]['oldVersion']
    oldBuildNumber             = gloConfig[gloKey]['oldBuildNumber']
    patcherToolsTag            = gloConfig[gloKey]['patcherToolsTag']
    patcherConfig              = gloConfig[gloKey]['patcherConfig']
    oldAppVersion              = gloConfig[gloKey]['oldAppVersion']
    oldBaseTag                 = gloConfig[gloKey]['oldBaseTag']
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
        partner_scheduler = Scheduler(
            name='partner_repacks_%s' % gloKey,
            treeStableTimer=0,
            branch='post_signing_%s' % gloKey,
            builderNames=['partner_repack_%s' % gloKey],
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
            platform_test_builders = []
            base_name = branchConfig['platforms'][platform]['base_name']
            #for suites_name, suites in branchConfig['unittest_suites']:
            for suites_name, suites in [('xpcshell', ['xpcshell']),('mozmill', ['mozmill'])]:
                #platform_test_builders.extend(generateTestBuilderNames('%s_test_%s' % (platform, gloKey), suites_name, suites))
                platform_test_builders.append('%s_unittest_%s_%s' % (platform, suites_name, gloKey))
            s = Scheduler(
             name='%s_release_unittest_%s' % (platform, gloKey),
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
                platform=platform + '-release',
                buildRevision='%s_RELEASE' % baseTag,
                version=version,
                buildNumber=buildNumber,
                clobberURL=branchConfig['base_clobber_url'],
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
              
                release_packaged_tests_factory = UnittestPackagedBuildFactory(
                    platform=platform,
                    test_suites=suites,
                    productName=productName,
                    hgHost=branchConfig['hghost'],
                    repoPath=sourceRepoPath,
                    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
                    buildSpace=1.0,
                    downloadSymbols=True,
                    buildsBeforeReboot=pf.get('builds_before_reboot', 0),
                    env={},
                )
  
                unittest_builder_name = '%s_unittest_%s_%s' % (platform, suites_name, gloKey)
  
                builder = {
                    'name': unittest_builder_name,
                    'slavenames': pf['slaves'],
                    'builddir': '%s-unittest-%s-%s' % (platform, suites_name, gloKey),
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
        partner_repack_factory = PartnerRepackFactory(
            hgHost=branchConfig['hghost'],
            repoPath=sourceRepoPath,
            buildToolsRepoPath=branchConfig['build_tools_repo_path'],
            productName=productName,
            version=version,
            buildNumber=buildNumber,
            partnersRepoPath=partnersRepoPath,
            stagingServer=stagingServer,
            stageUsername=branchConfig['stage_username'],
            stageSshKey=branchConfig['stage_ssh_key'],    
        )
    
        builders.append({
            'name': 'partner_repack_%s' % gloKey,
            'slavenames': branchConfig['platforms']['macosx']['slaves'],
            'category': 'release',
            'builddir': 'partner_repack_%s' % gloKey,
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
        oldRepoPath=sourceRepoPath,
        releaseNotesUrl=releaseNotesUrl,
        testOlderPartials=testOlderPartials,
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
            oldRepoPath=sourceRepoPath,
            triggerSchedulers=['major_update_verify_%s' % gloKey],
            releaseNotesUrl=majorUpdateReleaseNotesUrl,
            testOlderPartials=testOlderPartials
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
