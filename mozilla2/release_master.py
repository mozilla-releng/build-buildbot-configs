from buildbot.changes.pb import PBChangeSource
from buildbot.scheduler import Scheduler, Dependent

import buildbotcustom.l10n.scheduler
import buildbotcustom.misc
import buildbotcustom.process.factory

from buildbotcustom.l10n.scheduler import DependentL10n
from buildbotcustom.misc import get_l10n_repositories, isHgPollerTriggered
from buildbotcustom.process.factory import StagingRepositorySetupFactory, \
  ReleaseTaggingFactory, SingleSourceFactory, MercurialBuildFactory, \
  ReleaseUpdatesFactory, UpdateVerifyFactory, ReleaseFinalVerification, \
  L10nVerifyFactory, ReleaseRepackFactory

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

tag_scheduler = Scheduler(
    name='tag',
    branch='mozilla-central',
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
        repoPath='mozilla-central',
        baseTag='%s_RELEASE' % baseTag,
        localesFile='browser/locales/shipped-locales'
    )
    schedulers.append(build_scheduler)
    schedulers.append(repack_scheduler)

# Purposely, there is not a Scheduler for ReleaseFinalVerification
# This is a step run very shortly before release, and is triggered manually
# from the waterfall

##### Builders
repositories = {
    mozillaCentral: {
        'revision': mozillaCentralRevision,
        'relbranchOverride': relbranchOverride,
        'bumpFiles': ['config/milestone.txt', 'js/src/config/milestone.txt',
                      'browser/config/version.txt', 'browser/app/module.ver']
    }
}
l10n_repos = get_l10n_repositories(l10nRevisionFile, l10nCentral,
                                   relbranchOverride)
repositories.update(l10n_repos)

tag_factory = ReleaseTaggingFactory(
    repositories=repositories,
    buildToolsRepo=buildTools,
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
    'slavenames': ['moz2-linux-slave01', 'moz2-linux-slave02',
                   'moz2-linux-slave05',
                   'moz2-linux-slave06', 'moz2-linux-slave11',
                   'moz2-linux-slave12', 
                   'moz2-linux-slave14', 'moz2-linux-slave15',
                   'moz2-linux-slave16'],
    'category': 'release',
    'builddir': 'tag',
    'factory': tag_factory
})


source_factory = SingleSourceFactory(
    repository=mozillaCentral,
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
    'slavenames': ['moz2-linux-slave01', 'moz2-linux-slave02',
                   'moz2-linux-slave05',
                   'moz2-linux-slave06', 'moz2-linux-slave11',
                   'moz2-linux-slave12', 
                   'moz2-linux-slave14', 'moz2-linux-slave15',
                   'moz2-linux-slave16'],
    'category': 'release',
    'builddir': 'source',
    'factory': source_factory
})


for platform in releasePlatforms:
    # shorthand
    pf = nightly_config.BRANCHES['mozilla-central']['platforms'][platform]
    mozconfig = '%s/mozilla-central/release' % platform

    build_factory = MercurialBuildFactory(
        env=pf['env'],
        objdir=pf['platform_objdir'],
        platform=platform,
        branch='mozilla-central',
        sourceRepo=mozillaCentral.replace('mozilla-central', ''),
        buildToolsRepo=buildTools,
        configRepo=nightly_config.CONFIG_REPO_URL,
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
        uploadPackages=False,
        uploadSymbols=True,
        createSnippet=False,
        doCleanup=True, # this will clean-up the mac build dirs, but not delete
                        # the entire thing
        buildSpace=10,
    )

    builders.append({
        'name': '%s_build' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': '%s_build' % platform,
        'factory': build_factory
    })

    repack_factory = ReleaseRepackFactory(
        sourceRepo=nightly_config.HGURL,
        branch='mozilla-central',
        project=productName,
        repoPath='mozilla-central',
        l10nRepoPath='l10n-central',
        stageServer=nightly_config.STAGE_SERVER,
        stageUsername=nightly_config.STAGE_USERNAME,
        stageSshKey=nightly_config.STAGE_SSH_KEY,
        buildToolsRepo=nightly_config.BUILD_TOOLS_REPO_URL,
        buildSpace=2,
        configRepo=nightly_config.CONFIG_REPO_URL,
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
    cvsroot=cvsroot,
    buildTools=buildTools,
    stagingServer=stagingServer,
    productName=productName,
    appVersion=appVersion,
    buildNumber=buildNumber,
    oldAppVersion=oldVersion,
    oldBuildNumber=oldBuildNumber
)

builders.append({
    'name': 'l10n_verification',
    'slavenames': nightly_config.BRANCHES['mozilla-central']['platforms']['macosx']['slaves'],
    'category': 'release',
    'builddir': 'l10n_verification',
    'factory': l10n_verification_factory
})


updates_factory = ReleaseUpdatesFactory(
    cvsroot=cvsroot,
    patcherToolsTag=patcherToolsTag,
    mozillaCentral=mozillaCentral,
    buildTools=buildTools,
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
    ausHost=nightly_config.AUS2_HOST
)

builders.append({
    'name': 'updates',
    'slavenames': ['moz2-linux-slave01', 'moz2-linux-slave02',
                   'moz2-linux-slave05',
                   'moz2-linux-slave06', 'moz2-linux-slave11',
                   'moz2-linux-slave12',
                   'moz2-linux-slave14', 'moz2-linux-slave15',
                   'moz2-linux-slave16'],
    'category': 'release',
    'builddir': 'updates',
    'factory': updates_factory
})


for platform in releasePlatforms:
    pf = nightly_config.BRANCHES['mozilla-central']['platforms'][platform]

    platformVerifyConfig = None
    if platform == 'linux':
        platformVerifyConfig = linuxVerifyConfig
    if platform == 'macosx':
        platformVerifyConfig = macVerifyConfig
    if platform == 'win32':
        platformVerifyConfig = win32VerifyConfig

    update_verify_factory = UpdateVerifyFactory(
        mozillaCentral=mozillaCentral,
        buildTools=buildTools,
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


final_verification_factory = ReleaseFinalVerification(
    buildTools=buildTools,
    linuxConfig=linuxVerifyConfig,
    macConfig=macVerifyConfig,
    win32Config=win32VerifyConfig
)

builders.append({
    'name': 'final_verification',
    'slavenames': ['moz2-linux-slave01', 'moz2-linux-slave02',
                   'moz2-linux-slave05',
                   'moz2-linux-slave06', 'moz2-linux-slave11',
                   'moz2-linux-slave12', 
                   'moz2-linux-slave14', 'moz2-linux-slave15',
                   'moz2-linux-slave16'],
    'category': 'release',
    'builddir': 'final_verification',
    'factory': final_verification_factory
})
