from buildbot.changes.pb import PBChangeSource
from buildbot.scheduler import Scheduler, Dependent

import buildbotcustom.l10n
import buildbotcustom.misc
import buildbotcustom.process.factory

from buildbotcustom.l10n import DependentL10n
from buildbotcustom.misc import get_l10n_repositories, isHgPollerTriggered
from buildbotcustom.process.factory import StagingRepositorySetupFactory, \
  ReleaseTaggingFactory, SingleSourceFactory, ReleaseBuildFactory, \
  ReleaseUpdatesFactory, UpdateVerifyFactory, ReleaseFinalVerification, \
  L10nVerifyFactory, ReleaseRepackFactory
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

builders = []
schedulers = []
change_source = []
status = []

##### Change sources and Schedulers
change_source.append(PBChangeSource())
change_source.append(FtpPoller(
	branch="post_signing",
	ftpURLs=["http://%s/pub/mozilla.org/%s/nightly/%s-candidates/build%s/" \
	  % (stagingServer, productName, version, buildNumber)],
	pollInterval=60*10,
	searchString='win32_signing_build'
))

tag_scheduler = Scheduler(
    name='tag',
    branch=sourceRepoPath,
    treeStableTimer=0,
    builderNames=['tag'],
    fileIsImportant=lambda c: not isHgPollerTriggered(c, nightly_config.HGURL)
)
schedulers.append(tag_scheduler)
source_scheduler = Dependent(
    name='source',
    upstream=tag_scheduler,
    builderNames=['source']
)
schedulers.append(source_scheduler)
for platform in ['macosx']:
    build_scheduler = Dependent(
        name='%s_build' % platform,
        upstream=tag_scheduler,
        builderNames=['%s_build' % platform]
    )
    repack_scheduler = DependentL10n(
        name='%s_repack' % platform,
        platform=platform,
        upstream=build_scheduler,
        builderNames=['%s_repack' % platform],
        repoType='hg',
        branch=sourceRepoPath,
        baseTag='%s_RELEASE' % baseTag,
        localesFile='browser/locales/shipped-locales',
        tree='release'
    )
    schedulers.append(build_scheduler)
    schedulers.append(repack_scheduler)
l10n_verify_scheduler = Scheduler(
    name='l10n_verification',
    treeStableTimer=0,
    branch='post_signing',
    builderNames=['l10n_verification']
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
for platform in releasePlatforms:
    updateBuilderNames.append('%s_update_verify' % platform)
update_verify_scheduler = Dependent(
    name='update_verify',
    upstream=updates_scheduler,
    builderNames=updateBuilderNames
)
schedulers.append(update_verify_scheduler)

# Purposely, there is not a Scheduler for ReleaseFinalVerification
# This is a step run very shortly before release, and is triggered manually
# from the waterfall

##### Builders
repositories = {
    sourceRepoPath: {
        'revision': sourceRepoRevision,
        'relbranchOverride': relbranchOverride,
        'bumpFiles': ['config/milestone.txt', 'js/src/config/milestone.txt',
                      'browser/config/version.txt']
    }
}
l10n_repos = get_l10n_repositories(l10nRevisionFile, l10nRepoPath,
                                   relbranchOverride)
repositories.update(l10n_repos)

from buildbot.process import factory
from buildbot.steps.dummy import Dummy
dummy_factory = factory.BuildFactory()
dummy_factory.addStep(Dummy())

tag_factory = ReleaseTaggingFactory(
    hgHost=nightly_config.HGHOST,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    repositories=repositories,
    productName=productName,
    appName=appName,
    version=version,
    appVersion=appVersion,
    milestone=milestone,
    baseTag=baseTag,
    buildNumber=buildNumber,
    hgUsername=hgUsername,
    hgSshKey=hgSshKey
)

builders.append({
    'name': 'tag',
    'slavenames': nightly_config.BRANCHES[sourceRepoName]['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'tag',
    'factory': dummy_factory
})


source_factory = SingleSourceFactory(
    hgHost=nightly_config.HGHOST,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    repoPath=sourceRepoPath,
    productName=productName,
    version=version,
    baseTag=baseTag,
    stagingServer=nightly_config.STAGE_SERVER,
    stageUsername=nightly_config.STAGE_USERNAME,
    stageSshKey=nightly_config.STAGE_SSH_KEY,
    buildNumber=buildNumber,
    autoconfDirs=['.', 'js/src']
)

builders.append({
    'name': 'source',
    'slavenames': nightly_config.BRANCHES[sourceRepoName]['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'source',
    'factory': dummy_factory
})


for platform in releasePlatforms:
    # shorthand
    pf = nightly_config.BRANCHES[sourceRepoName]['platforms'][platform]
    mozconfig = '%s/%s/release' % (platform, sourceRepoName)

    build_factory = ReleaseBuildFactory(
        env=pf['env'],
        objdir=pf['platform_objdir'],
        platform=platform,
        hgHost=nightly_config.HGHOST,
        repoPath=sourceRepoPath,
        buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
        configRepoPath=nightly_config.CONFIG_REPO_PATH,
        configSubDir=nightly_config.CONFIG_SUBDIR,
        profiledBuild=pf['profiled_build'],
        mozconfig=mozconfig,
        buildRevision='%s_RELEASE' % baseTag,
        stageServer=nightly_config.STAGE_SERVER,
        stageUsername=nightly_config.STAGE_USERNAME,
        stageGroup=nightly_config.STAGE_GROUP,
        stageSshKey=nightly_config.STAGE_SSH_KEY,
        stageBasePath=nightly_config.STAGE_BASE_PATH,
        codesighs=False,
        uploadPackages=True,
        uploadSymbols=True,
        createSnippet=False,
        doCleanup=True, # this will clean-up the mac build dirs, but not delete
                        # the entire thing
        buildSpace=10,
        productName=productName,
        version=version,
        buildNumber=buildNumber
    )

    builders.append({
        'name': '%s_build' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': '%s_build' % platform,
        'factory': dummy_factory
    })

    repack_factory = ReleaseRepackFactory(
        hgHost=nightly_config.HGHOST,
        project=productName,
        appName=appName,
        repoPath=sourceRepoPath,
        l10nRepoPath=l10nRepoPath,
        stageServer=nightly_config.STAGE_SERVER,
        stageUsername=nightly_config.STAGE_USERNAME,
        stageSshKey=nightly_config.STAGE_SSH_KEY,
        buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
        compareLocalesRepoPath=nightly_config.COMPARE_LOCALES_REPO_PATH,
        compareLocalesTag=nightly_config.COMPARE_LOCALES_TAG,
        buildSpace=2,
        configRepoPath=nightly_config.CONFIG_REPO_PATH,
        configSubDir=nightly_config.CONFIG_SUBDIR,
        mozconfig=mozconfig,
        platform=platform + '-release',
        buildRevision='%s_RELEASE' % baseTag,
        version=version,
        buildNumber=buildNumber,
        tree='release'
    )

    builders.append({
        'name': '%s_repack' % platform,
        'slavenames': nightly_config.L10N_SLAVES[platform],
        'category': 'release',
        'builddir': '%s_repack' % platform,
        'factory': repack_factory
    })


l10n_verification_factory = L10nVerifyFactory(
    hgHost=nightly_config.HGHOST,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    cvsroot=cvsroot,
    stagingServer=stagingServer,
    productName=productName,
    version=version,
    buildNumber=buildNumber,
    oldVersion=oldVersion,
    oldBuildNumber=oldBuildNumber
)

builders.append({
    'name': 'l10n_verification',
    'slavenames': nightly_config.BRANCHES[sourceRepoName]['platforms']['macosx']['slaves'],
    'category': 'release',
    'builddir': 'l10n_verification',
    'factory': l10n_verification_factory
})


updates_factory = ReleaseUpdatesFactory(
    hgHost=nightly_config.HGHOST,
    repoPath=sourceRepoPath,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    cvsroot=cvsroot,
    patcherToolsTag=patcherToolsTag,
    patcherConfig=patcherConfig,
    verifyConfigs=verifyConfigs,
    appName=appName,
    productName=productName,
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
    stageUsername=nightly_config.STAGE_USERNAME,
    stageSshKey=nightly_config.STAGE_SSH_KEY,
    ausUser=nightly_config.AUS2_USER,
    ausHost=nightly_config.AUS2_HOST,
    ausServerUrl=ausServerUrl,
    hgSshKey=hgSshKey,
    hgUsername=hgUsername,
)

builders.append({
    'name': 'updates',
    'slavenames': nightly_config.BRANCHES[sourceRepoName]['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'updates',
    'factory': updates_factory
})


for platform in releasePlatforms:
    update_verify_factory = UpdateVerifyFactory(
        hgHost=nightly_config.HGHOST,
        buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
        verifyConfig=verifyConfigs[platform],
    )

    builders.append({
        'name': '%s_update_verify' % platform,
        'slavenames': nightly_config.BRANCHES[sourceRepoName]['platforms'][platform]['slaves'],
        'category': 'release',
        'builddir': '%s_update_verify' % platform,
        'factory': update_verify_factory
    })


final_verification_factory = ReleaseFinalVerification(
    hgHost=nightly_config.HGHOST,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    verifyConfigs=verifyConfigs,
)

builders.append({
    'name': 'final_verification',
    'slavenames': nightly_config.BRANCHES[sourceRepoName]['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'final_verification',
    'factory': final_verification_factory
})
