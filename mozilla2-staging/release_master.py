from buildbot.changes.pb import PBChangeSource
from buildbot.scheduler import Scheduler, Dependent

import buildbotcustom.misc
import buildbotcustom.process.factory
reload(buildbotcustom.misc)
reload(buildbotcustom.process.factory)

from buildbotcustom.misc import get_l10n_repositories, isHgPollerTriggered
from buildbotcustom.process.factory import StagingRepositorySetupFactory, \
  ReleaseTaggingFactory, SingleSourceFactory, MercurialBuildFactory, \
  ReleaseUpdatesFactory

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

repo_setup_scheduler = Scheduler(
    name='repo_setup',
    branch='mozilla-central',
    treeStableTimer=0,
    builderNames=['repo_setup'],
    fileIsImportant=lambda c: not isHgPollerTriggered(c, nightly_config.HGURL)
)
tag_scheduler = Dependent(
    name='tag',
    upstream=repo_setup_scheduler,
    builderNames=['tag']
)
build_scheduler = Dependent(
    name='build',
    upstream=tag_scheduler,
    builderNames=['source', 'linux_build', 'win32_build', 'macosx_build']
)

schedulers.append(repo_setup_scheduler)
schedulers.append(tag_scheduler)
schedulers.append(build_scheduler)

##### Builders
repositories = {
    mozillaCentral: {
        'revision': mozillaCentralRevision,
        'relbranchOverride': relbranchOverride,
        'bumpFiles': ['config/milestone.txt', 'browser/config/version.txt',
                      'browser/app/module.ver']
    }
}
l10n_repos = get_l10n_repositories(l10nRevisionFile, l10nCentral,
                                   relbranchOverride)
repositories.update(l10n_repos)

repository_setup_factory = StagingRepositorySetupFactory(
    hgHost=hgHost,
    username=hgUsername,
    sshKey=hgSshKey,
    repositories=repositories
)

builders.append({
    'name': 'repo_setup',
    'slavenames': ['moz2-linux-slave04'],
    'category': 'release',
    'builddir': 'repo_setup',
    'factory': repository_setup_factory
})


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
    'slavenames': ['moz2-linux-slave04'],
    'category': 'release',
    'builddir': 'tag',
    'factory': tag_factory
})


source_factory = SingleSourceFactory(
    repository=mozillaCentral,
    productName=productName,
    appVersion=appVersion,
    baseTag=baseTag
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
    pf = nightly_config.BRANCHES['mozilla-central']['platforms'][platform]

    build_factory = MercurialBuildFactory(
        env=pf['env'],
        objdir=pf['platform_objdir'],
        platform=platform + '-release',
        branch='mozilla-central',
        sourceRepo=mozillaCentral.replace('mozilla-central', ''),
        configRepo=nightly_config.CONFIG_REPO_URL,
        configSubDir=nightly_config.CONFIG_SUBDIR,
        profiledBuild=pf['profiled_build'],
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
        doCleanup=True # this will clean-up the mac build dirs, but not delete
                       # the entire thing
    )

    builders.append({
        'name': '%s_build' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': '%s_build' % platform,
        'factory': build_factory
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
