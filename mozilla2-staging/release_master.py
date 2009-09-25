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

branchConfig = nightly_config.BRANCHES[sourceRepoName]

builders = []
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

repo_setup_scheduler = Scheduler(
    name='repo_setup',
    branch=sourceRepoPath,
    treeStableTimer=0,
    builderNames=['repo_setup'],
    fileIsImportant=lambda c: not isHgPollerTriggered(c, branchConfig['hgurl'])
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
            localesFile='browser/locales/shipped-locales',
            tree='release'
        )
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
for platform in enUSPlatforms:
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
clone_repositories = {
    sourceRepoClonePath: {
        'revision': sourceRepoRevision,
        'relbranchOverride': relbranchOverride,
        'bumpFiles': ['config/milestone.txt', 'js/src/config/milestone.txt',
                      'browser/config/version.txt']
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
                      'browser/config/version.txt']
    }
}
l10n_tag_repos = get_l10n_repositories(l10nRevisionFile, l10nRepoPath,
                                       relbranchOverride)
tag_repositories.update(l10n_tag_repos)


repository_setup_factory = StagingRepositorySetupFactory(
    hgHost=branchConfig['hghost'],
    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
    username=hgUsername,
    sshKey=hgSshKey,
    repositories=clone_repositories
)

builders.append({
    'name': 'repo_setup',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'repo_setup',
    'factory': repository_setup_factory
})


tag_factory = ReleaseTaggingFactory(
    hgHost=branchConfig['hghost'],
    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
    repositories=tag_repositories,
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
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'tag',
    'factory': tag_factory
})


source_factory = SingleSourceFactory(
    hgHost=branchConfig['hghost'],
    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
    repoPath=sourceRepoPath,
    productName=productName,
    version=version,
    baseTag=baseTag,
    stagingServer=branchConfig['stage_server'],
    stageUsername=branchConfig['stage_username'],
    stageSshKey=branchConfig['stage_ssh_key'],
    buildNumber=buildNumber,
    autoconfDirs=['.', 'js/src']
)

builders.append({
   'name': 'source',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
   'category': 'release',
   'builddir': 'source',
   'factory': source_factory
})


for platform in enUSPlatforms:
    # shorthand
    pf = branchConfig['platforms'][platform]
    mozconfig = '%s/%s/release' % (platform, sourceRepoName)

    build_factory = ReleaseBuildFactory(
        env=pf['env'],
        objdir=pf['platform_objdir'],
        platform=platform,
        hgHost=branchConfig['hghost'],
        repoPath=sourceRepoPath,
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        configRepoPath=branchConfig['config_repo_path'],
        configSubDir=branchConfig['config_subdir'],
        profiledBuild=pf['profiled_build'],
        mozconfig=mozconfig,
        buildRevision='%s_RELEASE' % baseTag,
        stageServer=branchConfig['stage_server'],
        stageUsername=branchConfig['stage_username'],
        stageGroup=branchConfig['stage_group'],
        stageSshKey=branchConfig['stage_ssh_key'],
        stageBasePath=branchConfig['stage_base_path'],
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
        'factory': build_factory
    })

    if platform in l10nPlatforms:
        repack_factory = ReleaseRepackFactory(
            hgHost=branchConfig['hghost'],
            project=productName,
            appName=appName,
            repoPath=sourceRepoPath,
            l10nRepoPath=l10nRepoPath,
            stageServer=branchConfig['stage_server'],
            stageUsername=branchConfig['stage_username'],
            stageSshKey=branchConfig['stage_ssh_key'],
            buildToolsRepoPath=branchConfig['build_tools_repo_path'],
            compareLocalesRepoPath=branchConfig['compare_locales_repo_path'],
            compareLocalesTag=branchConfig['compare_locales_tag'],
            buildSpace=2,
            configRepoPath=branchConfig['config_repo_path'],
            configSubDir=branchConfig['config_subdir'],
            mozconfig=mozconfig,
            platform=platform + '-release',
            buildRevision='%s_RELEASE' % baseTag,
            version=version,
            buildNumber=buildNumber,
            tree='release'
        )

        builders.append({
            'name': '%s_repack' % platform,
            'slavenames': branchConfig['l10n_slaves'][platform],
            'category': 'release',
            'builddir': '%s_repack' % platform,
            'factory': repack_factory
        })


l10n_verification_factory = L10nVerifyFactory(
    hgHost=branchConfig['hghost'],
    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
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
    'slavenames': branchConfig['platforms']['macosx']['slaves'],
    'category': 'release',
    'builddir': 'l10n_verification',
    'factory': l10n_verification_factory
})


updates_factory = ReleaseUpdatesFactory(
    hgHost=branchConfig['hghost'],
    repoPath=sourceRepoPath,
    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
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
    stageUsername=branchConfig['stage_username'],
    stageSshKey=branchConfig['stage_ssh_key'],
    ausUser=branchConfig['aus2_user'],
    ausHost=branchConfig['aus2_host'],
    ausServerUrl=ausServerUrl,
    hgSshKey=hgSshKey,
    hgUsername=hgUsername,
    commitPatcherConfig=False # We disable this on staging, because we don't
                              # have a CVS mirror to commit to
)

builders.append({
    'name': 'updates',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'updates',
    'factory': updates_factory
})


for platform in enUSPlatforms:
    update_verify_factory = UpdateVerifyFactory(
        hgHost=branchConfig['hghost'],
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        verifyConfig=verifyConfigs[platform],
    )

    builders.append({
        'name': '%s_update_verify' % platform,
        'slavenames': branchConfig['platforms'][platform]['slaves'],
        'category': 'release',
        'builddir': '%s_update_verify' % platform,
        'factory': update_verify_factory
    })


final_verification_factory = ReleaseFinalVerification(
    hgHost=branchConfig['hghost'],
    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
    verifyConfigs=verifyConfigs,
)

builders.append({
    'name': 'final_verification',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'final_verification',
    'factory': final_verification_factory
})
