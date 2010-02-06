from buildbot.scheduler import Scheduler, Dependent
from buildbot.status.tinderbox import TinderboxMailNotifier

import buildbotcustom.l10n
import buildbotcustom.misc
import buildbotcustom.process.factory

from buildbotcustom.l10n import DependentL10n
from buildbotcustom.misc import get_l10n_repositories, isHgPollerTriggered, \
  generateTestBuilderNames, generateCCTestBuilder
from buildbotcustom.process.factory import StagingRepositorySetupFactory, \
  ReleaseTaggingFactory, CCSourceFactory, CCReleaseBuildFactory, \
  ReleaseUpdatesFactory, UpdateVerifyFactory, ReleaseFinalVerification, \
  L10nVerifyFactory, CCReleaseRepackFactory
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
            localesFile='suite/locales/shipped-locales',
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
for platform in sorted(verifyConfigs.keys()):
    updateBuilderNames.append('%s_update_verify' % platform)
update_verify_scheduler = Dependent(
    name='update_verify',
    upstream=updates_scheduler,
    builderNames=updateBuilderNames
)
schedulers.append(update_verify_scheduler)

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
if chatzillaRepoPath:
    repositories[chatzillaRepoPath] = {
        'revision': chatzillaRepoRevision,
        'relbranchOverride': chatzillaRelbranchOverride,
        'bumpFiles': []
    }

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
    appName=appName,
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
    'factory': dummy_factory #tag_factory
})


source_factory = CCSourceFactory(
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
    mozRepoPath=mozillaRepoPath,
    inspectorRepoPath=inspectorRepoPath,
    venkmanRepoPath=venkmanRepoPath,
    chatzillaRepoPath=chatzillaRepoPath,
    cvsroot=cvsroot,
    autoconfDirs=['.', 'mozilla', 'mozilla/js/src'],
    clobberURL=branchConfig['base_clobber_url'],
)

builders.append({
    'name': 'source',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'source',
    'factory': dummy_factory #source_factory
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

    build_factory = CCReleaseBuildFactory(
        env=pf['env'],
        objdir=pf['platform_objdir'],
        platform=platform,
        hgHost=branchConfig['hghost'],
        repoPath=sourceRepoPath,
        mozRepoPath=mozillaRepoPath,
        inspectorRepoPath=inspectorRepoPath,
        venkmanRepoPath=venkmanRepoPath,
        chatzillaRepoPath=chatzillaRepoPath,
        cvsroot=cvsroot,
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
        'slavenames': branchConfig['nightly_slaves'][platform],
        'category': 'release',
        'builddir': '%s_build' % platform,
        'factory': dummy_factory #build_factory
    })

    if platform in ('win32',): #l10nPlatforms:
        repack_factory = CCReleaseRepackFactory(
            hgHost=branchConfig['hghost'],
            project=productName,
            appName=appName,
            brandName=brandName,
            repoPath=sourceRepoPath,
            mozRepoPath=mozillaRepoPath,
            inspectorRepoPath=inspectorRepoPath,
            venkmanRepoPath=venkmanRepoPath,
            chatzillaRepoPath=chatzillaRepoPath,
            cvsroot=cvsroot,
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

            test_builders.extend(generateCCTestBuilder(
                branchConfig, 'release', platform, "%s_test" % platform,
                "release-%s-unittest" % (platform,),
                suites_name, suites, mochitestLeakThreshold,
                crashtestLeakThreshold))

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
    ausUser=branchConfig['aus2_user'],
    ausHost=branchConfig['aus2_host'],
    ausServerUrl=ausServerUrl,
    hgSshKey=hgSshKey,
    hgUsername=hgUsername,
    clobberURL=branchConfig['base_clobber_url'],
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

status.append(TinderboxMailNotifier(
    fromaddr="comm.buildbot@build.mozilla.org",
    tree=branchConfig["tinderbox_tree"] + "-Release",
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org",],
    relayhost="mail.build.mozilla.org",
    builders=[b['name'] for b in builders],
    logCompression="bzip2")
)

status.append(TinderboxMailNotifier(
    fromaddr="comm.buildbot@build.mozilla.org",
    tree=branchConfig["tinderbox_tree"] + "-Release",
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org",],
    relayhost="mail.build.mozilla.org",
    builders=[b['name'] for b in test_builders],
    logCompression="bzip2",
    errorparser="unittest")
)

builders.extend(test_builders)
