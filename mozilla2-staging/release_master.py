from buildbot.scheduler import Scheduler, Dependent, Triggerable
from buildbot.status.tinderbox import TinderboxMailNotifier

import buildbotcustom.l10n
import buildbotcustom.misc
import buildbotcustom.process.factory

from buildbotcustom.l10n import DependentL10n
from buildbotcustom.misc import get_l10n_repositories, isHgPollerTriggered, \
  generateTestBuilderNames, generateTestBuilder
from buildbotcustom.process.factory import StagingRepositorySetupFactory, \
  ReleaseTaggingFactory, SingleSourceFactory, ReleaseBuildFactory, \
  ReleaseUpdatesFactory, UpdateVerifyFactory, ReleaseFinalVerification, \
  L10nVerifyFactory, ReleaseRepackFactory, UnittestPackagedBuildFactory, \
  PartnerRepackFactory, MajorUpdateFactory
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
if doPartnerRepacks:
    partner_scheduler = Scheduler(
        name='partner_repacks',
        treeStableTimer=0,
        branch='post_signing',
        builderNames=['partner_repack'],
    )
    schedulers.append(partner_scheduler)
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
    platform_test_builders = []
    base_name = branchConfig['platforms'][platform]['base_name']
    for suites_name, suites in branchConfig['unittest_suites']:
        platform_test_builders.extend(generateTestBuilderNames('%s_test' % platform, suites_name, suites))

    s = Scheduler(
     name='%s_release_unittest' % platform,
     treeStableTimer=0,
     branch='%s-release-unittest' % platform,
     builderNames=platform_test_builders,
    )
    schedulers.append(s)

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
if len(l10nPlatforms) > 0:
    l10n_clone_repos = get_l10n_repositories(l10nRevisionFile,
                                             l10nRepoClonePath,
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
if len(l10nPlatforms) > 0:
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
    hgSshKey=hgSshKey,
    clobberURL=branchConfig['base_clobber_url'],
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
    autoconfDirs=['.', 'js/src'],
    clobberURL=branchConfig['base_clobber_url'],
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
    if platform in talosTestPlatforms:
        talosMasters = branchConfig['talos_masters']
    else:
        talosMasters = None

    if platform in unittestPlatforms:
        packageTests = True
        unittestMasters = branchConfig['unittest_masters']
        unittestBranch = '%s-release-unittest' % platform
    else:
        packageTests = False
        unittestMasters = None
        unittestBranch = None

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
        buildNumber=buildNumber,
        talosMasters=talosMasters,
        packageTests=packageTests,
        unittestMasters=unittestMasters,
        unittestBranch=unittestBranch,
        clobberURL=branchConfig['base_clobber_url'],
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
            tree='release',
            clobberURL=branchConfig['base_clobber_url'],
        )

        builders.append({
            'name': '%s_repack' % platform,
            'slavenames': branchConfig['l10n_slaves'][platform],
            'category': 'release',
            'builddir': '%s_repack' % platform,
            'factory': repack_factory
        })

    if platform in unittestPlatforms:
        mochitestLeakThreshold = pf.get('mochitest_leak_threshold', None)
        crashtestLeakThreshold = pf.get('crashtest_leak_threshold', None)
        for suites_name, suites in branchConfig['unittest_suites']:
            # Release builds on mac don't have a11y enabled, do disable the mochitest-a11y test
            if platform == 'macosx' and 'mochitest-a11y' in suites:
                suites = suites[:]
                suites.remove('mochitest-a11y')

            test_builders.extend(generateTestBuilder(
                branchConfig, 'release', platform, "%s_test" % platform,
                "release-%s-unittest" % (platform,),
                suites_name, suites, mochitestLeakThreshold,
                crashtestLeakThreshold))

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
        'name': 'partner_repack',
        'slavenames': branchConfig['platforms']['macosx']['slaves'],
        'category': 'release',
        'builddir': 'partner_repack',
        'factory': partner_repack_factory
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
    oldBuildNumber=oldBuildNumber,
    clobberURL=branchConfig['base_clobber_url'],
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
    ausSshKey=branchConfig['aus2_ssh_key'],
    ausHost=branchConfig['aus2_host'],
    ausServerUrl=ausServerUrl,
    hgSshKey=hgSshKey,
    hgUsername=hgUsername,
    # We disable this on staging, because we don't have a CVS mirror to
    # commit to
    commitPatcherConfig=False,
    clobberURL=branchConfig['base_clobber_url'],
    oldRepoPath=sourceRepoPath
)

builders.append({
    'name': 'updates',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'updates',
    'factory': updates_factory
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
        'factory': update_verify_factory
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
    'factory': final_verification_factory
})

if majorUpdateRepoPath:
    # Not attached to any Scheduler
    major_update_factory = MajorUpdateFactory(
        hgHost=branchConfig['hghost'],
        repoPath=majorUpdateRepoPath,
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        cvsroot=cvsroot,
        patcherToolsTag=patcherToolsTag,
        patcherConfig=majorUpdatePatcherConfig,
        verifyConfigs=majorUpdateVerifyConfigs,
        appName=appName,
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
        ausUser=branchConfig['aus2_user'],
        ausSshKey=branchConfig['aus2_ssh_key'],
        ausHost=branchConfig['aus2_host'],
        ausServerUrl=ausServerUrl,
        hgSshKey=hgSshKey,
        hgUsername=hgUsername,
        # We disable this on staging, because we don't have a CVS mirror to
        # commit to
        commitPatcherConfig=False,
        clobberURL=branchConfig['base_clobber_url'],
        oldRepoPath=sourceRepoPath,
        triggerSchedulers=['major_update_verify']
    )
    
    builders.append({
        'name': 'major_update',
        'slavenames': branchConfig['platforms']['linux']['slaves'],
        'category': 'release',
        'builddir': 'major_update',
        'factory': major_update_factory
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
            'factory': major_update_verify_factory
        })


status.append(TinderboxMailNotifier(
    fromaddr="mozilla2.buildbot@build.mozilla.org",
    tree=branchConfig["tinderbox_tree"] + "-Release",
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org",],
    relayhost="mail.build.mozilla.org",
    builders=[b['name'] for b in builders],
    logCompression="bzip2")
)

status.append(TinderboxMailNotifier(
    fromaddr="mozilla2.buildbot@build.mozilla.org",
    tree=branchConfig["tinderbox_tree"] + "-Release",
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org",],
    relayhost="mail.build.mozilla.org",
    builders=[b['name'] for b in test_builders],
    logCompression="bzip2",
    errorparser="unittest")
)

builders.extend(test_builders)
