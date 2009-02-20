from buildbot.changes.pb import PBChangeSource
from buildbot.scheduler import Scheduler, Dependent

import buildbotcustom.l10n.scheduler
import buildbotcustom.misc
import buildbotcustom.process.factory

from buildbotcustom.l10n.scheduler import DependentL10n
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
	  % (stagingServer, productName, appVersion, buildNumber)],
	pollInterval= 60*10,
	searchString='win32_signing_build'
))

repo_setup_scheduler = Scheduler(
    name='repo_setup',
    branch=sourceRepoPath,
    treeStableTimer=0,
    builderNames=['repo_setup'],
    fileIsImportant=lambda c: not isHgPollerTriggered(c, nightly_config.HGURL)
)
schedulers.append(repo_setup_scheduler)
tag_scheduler = Dependent(
    name='tag',
    upstream=repo_setup_scheduler,
    builderNames=['tag']
)
schedulers.append(tag_scheduler)
source_scheduler = Dependent(
    name='source',
    upstream=tag_scheduler,
    builderNames=['source']
)
schedulers.append(source_scheduler)
for platform in releasePlatforms:
    build_scheduler = Dependent(
        name='%s_build' % platform,
        upstream=tag_scheduler,
        builderNames=['%s_build' % platform]
    )
    repack_scheduler = DependentL10n(
        name='%s_repack' % platform,
        upstream=build_scheduler,
        builderNames=['%s_repack' % platform],
        repoType='hg',
        repoPath=sourceRepoPath,
        baseTag='%s_RELEASE' % baseTag,
        localesFile='browser/locales/shipped-locales'
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
    updateBuilderNames.append('%s_update_verify, ' % platform)
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
clone_repositories = {
    sourceRepoClonePath: {
        'revision': sourceRepoRevision,
        'relbranchOverride': relbranchOverride,
        'bumpFiles': ['config/milestone.txt', 'js/src/config/milestone.txt',
                      'browser/config/version.txt', 'browser/app/module.ver']
    }
}
l10n_clone_repos = get_l10n_repositories(l10nRevisionFile, l10nRepoClonePath,
                                         relbranchOverride)
clone_repositories.update(l10n_clone_repos)

tag_repositories = {
    sourceRepoPath: {
        'revision': sourceRepoRevision,
        'relbranchOverride': relbranchOverride,
        'bumpFiles': ['config/milestone.txt', 'js/src/config/milestone.txt',
                      'browser/config/version.txt', 'browser/app/module.ver']
    }
}
l10n_tag_repos = get_l10n_repositories(l10nRevisionFile, l10nRepoPath,
                                       relbranchOverride)
tag_repositories.update(l10n_tag_repos)


repository_setup_factory = StagingRepositorySetupFactory(
    hgHost=nightly_config.HGHOST,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    username=hgUsername,
    sshKey=hgSshKey,
    repositories=clone_repositories
)

builders.append({
    'name': 'repo_setup',
    'slavenames': ['moz2-linux-slave04'],
    'category': 'release',
    'builddir': 'repo_setup',
    'factory': repository_setup_factory
})


tag_factory = ReleaseTaggingFactory(
    hgHost=nightly_config.HGHOST,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    repositories=tag_repositories,
    productName=productName,
    appName=appName,
    appVersion=appVersion,
    milestone=milestone,
    baseTag=baseTag,
    buildNumber=buildNumber,
    hgUsername=hgUsername,
    hgSshKey=hgSshKey
)

builders.append({
    'name': 'tag',
    'slavenames': ['moz2-linux-slave04'],
    'category': 'release',
    'builddir': 'tag',
    'factory': tag_factory
})


source_factory = SingleSourceFactory(
    hgHost=nightly_config.HGHOST,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    repoPath=sourceRepoPath,
    productName=productName,
    appVersion=appVersion,
    baseTag=baseTag,
    stagingServer=nightly_config.STAGE_SERVER,
    stageUsername=nightly_config.STAGE_USERNAME,
    stageSshKey=nightly_config.STAGE_SSH_KEY,
    buildNumber=buildNumber,
    autoconfDirs=['.', 'js/src']
)

builders.append({
   'name': 'source',
   'slavenames': ['moz2-linux-slave04'],
   'category': 'release',
   'builddir': 'source',
   'factory': source_factory
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
        appVersion=appVersion,
        buildNumber=buildNumber
    )

    builders.append({
        'name': '%s_build' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': '%s_build' % platform,
        'factory': build_factory
    })

    repack_factory = ReleaseRepackFactory(
        hgHost=nightly_config.HGHOST,
        project=productName,
        repoPath=sourceRepoPath,
        l10nRepoPath=l10nRepoPath,
        stageServer=nightly_config.STAGE_SERVER,
        stageUsername=nightly_config.STAGE_USERNAME,
        stageSshKey=nightly_config.STAGE_SSH_KEY,
        buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
        buildSpace=2,
        configRepoPath=nightly_config.CONFIG_REPO_PATH,
        configSubDir=nightly_config.CONFIG_SUBDIR,
        mozconfig=mozconfig,
        platform=platform + '-release',
        buildRevision='%s_RELEASE' % baseTag,
        appVersion=appVersion,
        buildNumber=buildNumber
    )

    builders.append({
        'name': '%s_repack' % platform,
        'slavenames': pf['slaves'],
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
    appVersion=appVersion,
    buildNumber=buildNumber,
    oldAppVersion=oldVersion,
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
    baseTag=baseTag,
    appName=appName,
    productName=productName,
    appVersion=appVersion,
    oldVersion=oldVersion,
    buildNumber=buildNumber,
    ftpServer=ftpServer,
    bouncerServer=bouncerServer,
    stagingServer=stagingServer,
    useBetaChannel=useBetaChannel,
    stageUsername=nightly_config.STAGE_USERNAME,
    stageSshKey=nightly_config.STAGE_SSH_KEY,
    ausUser=nightly_config.AUS2_USER,
    ausHost=nightly_config.AUS2_HOST,
    commitPatcherConfig=False # We disable this on staging, because we don't
                              # have a CVS mirror to commit to
)

builders.append({
    'name': 'updates',
    'slavenames': ['moz2-linux-slave04'],
    'category': 'release',
    'builddir': 'updates',
    'factory': updates_factory
})

for platform in releasePlatforms:
    pf = nightly_config.BRANCHES[sourceRepoName]['platforms'][platform]

    platformVerifyConfig = None
    if platform == 'linux':
        platformVerifyConfig = linuxVerifyConfig
    if platform == 'macosx':
        platformVerifyConfig = macVerifyConfig
    if platform == 'win32':
        platformVerifyConfig = win32VerifyConfig

    update_verify_factory = UpdateVerifyFactory(
        hgHost=nightly_config.HGHOST,
        buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
        repoPath=sourceRepoPath,
        cvsroot=cvsroot,
        patcherToolsTag=patcherToolsTag,
        hgUsername=hgUsername,
        baseTag=oldBaseTag,
        appName=appName,
        platform=platform,
        productName=productName,
        oldVersion=oldVersion,
        oldBuildNumber=oldBuildNumber,
        version=appVersion,
        buildNumber=buildNumber,
        ausServerUrl=ausServerUrl,
        stagingServer=stagingServer,
        verifyConfig=platformVerifyConfig,
        hgSshKey=hgSshKey
    )

    builders.append({
        'name': '%s_update_verify' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': '%s_update_verify' % platform,
        'factory': update_verify_factory
    })


final_verification_factory= ReleaseFinalVerification(
    hgHost=nightly_config.HGHOST,
    buildToolsRepoPath=nightly_config.BUILD_TOOLS_REPO_PATH,
    linuxConfig=linuxVerifyConfig,
    macConfig=macVerifyConfig,
    win32Config=win32VerifyConfig
)

builders.append({
    'name': 'final_verification',
    'slavenames': ['moz2-linux-slave04'],
    'category': 'release',
    'builddir': 'final_verification',
    'factory': final_verification_factory
})
