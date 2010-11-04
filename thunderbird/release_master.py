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
import release_config
reload(release_config)
from release_config import *

# for the 'build' step we use many of the same vars as the nightlies do.
# we import those so we don't have to duplicate them in release_config
import config as nightly_config
reload(nightly_config)

#XXX: Our current buildbot config is inconsistent with the branch name itself, fix it
nightly_config.BRANCHES['comm-1.9.1'] = nightly_config.BRANCHES['comm-central'].copy()

branchConfig = nightly_config.BRANCHES[sourceRepoName]

for v in ['hgurl', 'stage_username','stage_server', 'stage_ssh_key','stage_group','stage_base_path', 'clobber_url']:
    branchConfig[v] = nightly_config.DEFAULTS[v]
    
branchConfig['hghost'] = nightly_config.HGHOST
branchConfig['build_tools_repo_path'] = toolsRepoPath
branchConfig['aus2_host'] = nightly_config.AUS2_HOST
branchConfig['base_clobber_url'] = nightly_config.BRANCHES[sourceRepoName]['clobber_url']

builders = []
test_builders = []
schedulers = []
change_source = []
status = []

##### Change sources and Schedulers
change_source.append(FtpPoller(
    branch="post_signing",
    ftpURLs=["http://%s/pub/mozilla.org/%s/nightly/%s-candidates/build%s/" \
             % (stagingServer, productName, version, buildNumber)],
    pollInterval= 60*10,
    searchString='win32_signing_build'
))

tag_scheduler = Scheduler(
    name='tag',
    branch=sourceRepoPath,
    treeStableTimer=0,
    builderNames=['tag'],
    fileIsImportant=lambda c: not isHgPollerTriggered(c, branchConfig['hgurl'])
)
schedulers.append(tag_scheduler)
source_scheduler = Dependent(
    name='source',
    upstream=tag_scheduler,
    builderNames=['source']
)
schedulers.append(source_scheduler)

if xulrunnerPlatforms:
    xulrunner_source_scheduler = Dependent(
        name='xulrunner_source',
        upstream=tag_scheduler,
        builderNames=['xulrunner_source']
    )
    schedulers.append(xulrunner_source_scheduler)

for platform in enUSPlatforms:
    build_scheduler = Dependent(
        name='%s_build' % platform,
        upstream=tag_scheduler,
        builderNames=['%s_build' % platform]
    )
    schedulers.append(build_scheduler)
    if platform in l10nPlatforms:
        repack_scheduler = DependentL10n(
            name='%s_repack' % platform,
            platform=platform,
            upstream=build_scheduler,
            builderNames=['%s_repack' % platform],
            repoType='hg',
            branch=sourceRepoPath,
            baseTag='%s_RELEASE' % baseTag,
            localesFile='%s/locales/shipped-locales' % appName,
            tree='release',
            # If a few locales are needed, do this instead:
            #locales={ 'zh-TW': ['linux']},
        )
        schedulers.append(repack_scheduler)

for platform in xulrunnerPlatforms:
    xulrunner_build_scheduler = Dependent(
        name='xulrunner_%s_build' % platform,
        upstream=tag_scheduler,
        builderNames=['xulrunner_%s_build' % platform]
    )
    schedulers.append(xulrunner_build_scheduler)

if doPartnerRepacks:
    partner_scheduler = Scheduler(
        name='partner_repacks',
        treeStableTimer=0,
        branch='post_signing',
        builderNames=['partner_repack'],
    )
    schedulers.append(partner_scheduler)

for platform in l10nPlatforms:
    l10n_verify_scheduler = Scheduler(
        name='%s_l10n_verification' % platform,
        treeStableTimer=0,
        branch='post_signing',
        builderNames=['%s_l10n_verification' % platform]
    )
    schedulers.append(l10n_verify_scheduler)

updates_scheduler = Scheduler(
    name='updates',
    treeStableTimer=0,
    branch='post_signing',
    builderNames=['updates']
)
schedulers.append(updates_scheduler)

updateBuilderNames = []
for platform in sorted(verifyConfigs.keys()):
    updateBuilderNames.append('%s_update_verify' % platform)
update_verify_scheduler = Dependent(
    name='update_verify',
    upstream=updates_scheduler,
    builderNames=updateBuilderNames
)
schedulers.append(update_verify_scheduler)

if majorUpdateRepoPath:
    majorUpdateBuilderNames = []
    for platform in sorted(majorUpdateVerifyConfigs.keys()):
        majorUpdateBuilderNames.append('%s_major_update_verify' % platform)
    major_update_verify_scheduler = Triggerable(
        name='major_update_verify',
        builderNames=majorUpdateBuilderNames
    )
    schedulers.append(major_update_verify_scheduler)

for platform in unittestPlatforms:
    if branchConfig['platforms'][platform]['enable_opt_unittests']:
        platform_test_builders = []
        base_name = branchConfig['platforms'][platform]['base_name']
        for suites_name, suites in branchConfig['unittest_suites']:
            platform_test_builders.extend(generateTestBuilderNames('%s_test' % platform, suites_name, suites))

        s = Scheduler(
         name='%s_release_unittest' % platform,
         treeStableTimer=0,
         branch='release-%s-%s-opt-unittest' % (sourceRepoName, platform),
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
    'name': 'tag',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'tag',
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
    'name': 'source',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'source',
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
       'name': 'xulrunner_source',
       'slavenames': branchConfig['platforms']['linux']['slaves'],
       'category': 'release',
       'builddir': 'xulrunner_source',
       'factory': xulrunner_source_factory
    })

for platform in enUSPlatforms:
    # shorthand
    pf = nightly_config.BRANCHES[sourceRepoName]['platforms'][platform]
    mozconfig = '%s/%s/release' % (platform, sourceRepoName)

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
    )

    builders.append({
        'name': '%s_build' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': '%s_build' % platform,
        'factory': build_factory,
    })

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
        'name': '%s_repack' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': '%s_repack' % platform,
        'factory': repack_factory,
    })


if doPartnerRepacks:
    partner_repack_factory = PartnerRepackFactory(
        hgHost=branchConfig['hghost'],
        repoPath=mozillaRepoPath,
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
        'name': 'partner_repack',
        'slavenames': branchConfig['platforms']['macosx']['slaves'],
        'category': 'release',
        'builddir': 'partner_repack',
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

    builders.append({
        'name': '%s_l10n_verification' % platform,
        'slavenames': branchConfig['platforms']['macosx']['slaves'],
        'category': 'release',
        'builddir': '%s_l10n_verification' % platform,
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
    'name': 'updates',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'updates',
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
        'name': '%s_update_verify' % platform,
        'slavenames': branchConfig['platforms'][platform]['slaves'],
        'category': 'release',
        'builddir': '%s_update_verify' % platform,
        'factory': update_verify_factory,
    })


final_verification_factory = ReleaseFinalVerification(
    hgHost=branchConfig['hghost'],
    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
    verifyConfigs=verifyConfigs,
    clobberURL=branchConfig['base_clobber_url'],
)

builders.append({
    'name': 'final_verification',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'final_verification',
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
        triggerSchedulers=['major_update_verify'],
        releaseNotesUrl=majorUpdateReleaseNotesUrl,
        testOlderPartials=testOlderPartials
    )
    
    builders.append({
        'name': 'major_update',
        'slavenames': branchConfig['platforms']['linux']['slaves'],
        'category': 'release',
        'builddir': 'major_update',
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
            'name': '%s_major_update_verify' % platform,
            'slavenames': branchConfig['platforms'][platform]['slaves'],
            'category': 'release',
            'builddir': '%s_major_update_verify' % platform,
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
