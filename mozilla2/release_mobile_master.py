from buildbot.scheduler import Scheduler, Dependent
from buildbot.process.factory import BuildFactory
from buildbot.steps.dummy import Dummy

import buildbotcustom.l10n
import buildbotcustom.misc
import buildbotcustom.process.factory

from buildbotcustom.l10n import DependentL10n
from buildbotcustom.misc import get_locales_from_json, \
                                isHgPollerTriggered
from buildbotcustom.process.factory import ReleaseTaggingFactory, \
  MultiSourceFactory, MaemoReleaseBuildFactory, MaemoReleaseRepackFactory, \
  PartnerRepackFactory, ReleaseMobileDesktopBuildFactory
from buildbotcustom.changes.ftppoller import FtpPoller

# this is where all of our important configuration is stored. build number,
# version number, sign-off revisions, etc.
import release_mobile_config
reload(release_mobile_config)
from release_mobile_config import *

import mobile_master
reload(mobile_master)
from mobile_master import MOBILE_L10N_SLAVES

# for the 'build' step we use many of the same vars as the nightlies do.
# we import those so we don't have to duplicate them in release_config
import config as nightly_config
import mobile_config as mobile_nightly_config

branchConfig = nightly_config.BRANCHES[mozSourceRepoName]
mobileBranchConfig = mobile_nightly_config.MOBILE_BRANCHES[mobileBranchNick]

builders = []
schedulers = []
change_source = []
status = []

##### Change sources and Schedulers

(l10n_repos, platform_locales) = get_locales_from_json(l10nRevisionFile,
                                                       l10nRepoPath,
                                                       l10nRelbranchOverride)

tag_scheduler = Scheduler(
    name='mobile_tag',
    branch=mobileSourceRepoPath,
    builderNames=['mobile_tag'],
    treeStableTimer=0,
    fileIsImportant=lambda c: not isHgPollerTriggered(c, branchConfig['hgurl'])
)
schedulers.append(tag_scheduler)
source_scheduler = Dependent(
    name='mobile_source',
    upstream=tag_scheduler,
    builderNames=['mobile_source']
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
        l10nPlatform = platform
        if l10nPlatform.startswith('maemo'):
            l10nPlatform = 'maemo'
        repack_scheduler = DependentL10n(
            name='%s_repack' % platform,
            platform=l10nPlatform,
            upstream=build_scheduler,
            builderNames=['%s_repack' % platform],
            repoType='hg',
            branch=mobileSourceRepoPath,
            baseTag='%s_RELEASE' % baseTag,
            locales=platform_locales[l10nPlatform],
            tree='release'
        )
        schedulers.append(repack_scheduler)
for platform in enUSDesktopPlatforms:
    build_scheduler = Dependent(
        name='mobile_%s_desktop_build' % platform,
        upstream=tag_scheduler,
        builderNames=['mobile_%s_desktop_build' % platform]
    )
    schedulers.append(build_scheduler)
    if platform in l10nDesktopPlatforms:
        repack_scheduler = DependentL10n(
            name='mobile_%s_desktop_repack' % platform,
            platform=platform,
            upstream=build_scheduler,
            builderNames=['mobile_%s_desktop_repack' % platform],
            repoType='hg',
            branch=mobileSourceRepoPath,
            baseTag='%s_RELEASE' % baseTag,
            locales=platform_locales[platform],
            tree='release'
        )
        schedulers.append(repack_scheduler)
if doPartnerRepacks:
    partner_scheduler = Dependent(
        name='mobile_partner_repacks',
        upstream=build_scheduler,
        builderNames=['mobile_partner_repack']
    )
    schedulers.append(partner_scheduler)

##### Builders
repositories = {
    mozSourceRepoPath: {
        'revision': mozSourceRepoRevision,
        'relbranchOverride': mozRelbranchOverride,
        'bumpFiles': ['config/milestone.txt', 'js/src/config/milestone.txt'],
    },
    mobileSourceRepoPath: {
        'revision': mobileSourceRepoRevision,
        'relbranchOverride': mobileRelbranchOverride,
        'bumpFiles': ['default-version.txt'],
    },
}
repositories.update(l10n_repos)


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
    hgSshKey=hgSshKey
)

builders.append({
    'name': 'mobile_tag',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'mobile_tag',
    'factory': tag_factory
})

sourceRepoConfig = [{
        'repoPath': mozSourceRepoPath,
        'location': mozSourceRepoName,
        'bundleName': '%s-%s_%s.bundle' % (productName, version,
                                           mozSourceRepoName),
    },{
        'repoPath': mobileSourceRepoPath,
        'location': '%s/mobile' % mozSourceRepoName,
        'bundleName': '%s-%s_%s.bundle' % (productName, version,
                                           mobileSourceRepoName),
    }
]
mobile_source_factory = MultiSourceFactory(
    hgHost=branchConfig['hghost'],
    buildToolsRepoPath=branchConfig['build_tools_repo_path'],
    repoPath=mozSourceRepoPath,
    repoConfig=sourceRepoConfig,
    productName=productName,
    uploadProductName='mobile',
    version=version,
    baseTag=baseTag,
    stagingServer=branchConfig['stage_server'],
    stageUsername=branchConfig['stage_username'],
    stageSshKey=branchConfig['stage_ssh_key'],
    buildNumber=buildNumber,
    stageNightlyDir="candidates",
    autoconfDirs=['.', 'js/src']
)
builders.append({
    'name': 'mobile_source',
    'slavenames': branchConfig['platforms']['linux']['slaves'],
    'category': 'release',
    'builddir': 'mobile_source',
    'factory': mobile_source_factory
})


for platform in enUSPlatforms:
    baseUploadDir='%s-candidates/build%d' % (version, buildNumber)
    candidatesPath = '%s/%s' % (stageBasePath, baseUploadDir)
    build_factory = None
    repack_factory = None

    if platform.startswith('maemo'):
        pf = mobileBranchConfig['platforms'][platform]
        clobberTime = pf.get('clobber_time', branchConfig['default_clobber_time'])
        mozconfig = 'mobile/%s/%s/release' % (platform, mobileSourceRepoName)
        releaseWorkDir  = pf['base_workdir'] + '-release'
        releaseBuildDir = pf['base_builddir'] + '-release'
        build_factory = MaemoReleaseBuildFactory(
            env=pf['env'],
            hgHost=branchConfig['hghost'],
            repoPath=mozSourceRepoPath,
            configRepoPath=branchConfig['config_repo_path'],
            configSubDir=branchConfig['config_subdir'],
            mozconfig=mozconfig,
            stageUsername=branchConfig['stage_username'],
            stageServer=branchConfig['stage_server'],
            stageSshKey=branchConfig['stage_ssh_key'],
            stageBasePath=candidatesPath,
            mobileRepoPath=mobileSourceRepoPath,
            mozRevision='%s_RELEASE' % baseTag,
            mobileRevision='%s_RELEASE' % baseTag,
            l10nTag='%s_RELEASE' % baseTag,
            platform=platform,
            uploadSymbols=True,
            buildsBeforeReboot=pf['builds_before_reboot'],
            baseWorkDir=releaseWorkDir,
            baseBuildDir=releaseBuildDir,
            baseUploadDir=baseUploadDir,
            buildToolsRepoPath=branchConfig['build_tools_repo_path'],
            clobberURL=branchConfig['base_clobber_url'],
            clobberTime=clobberTime,
            buildSpace=10,
            mergeLocales=mergeLocales,
            locales=platform_locales['maemo-multilocale'].keys(),
            multiLocale=mobileBranchConfig['enable_multi_locale'],
            l10nRepoPath=l10nRepoPath,
            triggerBuilds=False,
        )

    builders.append({
        'name': '%s_build' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': '%s_build' % platform,
        'factory': build_factory
    })

    if platform in l10nPlatforms:
        if platform.startswith('maemo'):
            releaseBuildDir = pf['base_builddir'] + '-l10n-release'
            repack_factory = MaemoReleaseRepackFactory(
                enUSBinaryURL='%s/%s' % (base_enUS_binaryURL, platform),
                stageServer=branchConfig['stage_server'],
                stageUsername=branchConfig['stage_username'],
                stageSshKey=branchConfig['stage_ssh_key'],
                stageBasePath='%s/%s-candidates/build%d/%s' % (stageBasePath,
                                                               version,
                                                               buildNumber,
                                                               platform),
                baseWorkDir='%s-release' % pf['base_l10n_workdir'],
                baseBuildDir=releaseBuildDir,
                l10nTag='%s_RELEASE' % baseTag,
                hgHost=branchConfig['hghost'],
                repoPath=mozSourceRepoPath,
                l10nRepoPath=l10nRepoPath,
                mobileRepoPath=mobileSourceRepoPath,
                packageGlobList=['-r', '%(locale)s'],
                buildToolsRepoPath=branchConfig['build_tools_repo_path'],
                compareLocalesRepoPath=branchConfig['compare_locales_repo_path'],
                compareLocalesTag=branchConfig['compare_locales_tag'],
                mergeLocales=mergeLocales,
                buildSpace=2,
                configRepoPath=branchConfig['config_repo_path'],
                configSubDir=branchConfig['config_subdir'],
                mozconfig=mozconfig,
                platform=platform,
                tree='release'
            )

        builders.append({
            'name': '%s_repack' % platform,
            'slavenames': MOBILE_L10N_SLAVES['maemo4'],
            'category': 'release',
            'builddir': '%s_repack' % platform,
            'factory': repack_factory
        })

for platform in enUSDesktopPlatforms:
    baseUploadDir='%s-candidates/build%d' % (version, buildNumber)
    candidatesPath = '%s/%s' % (stageBasePath, baseUploadDir)
    build_factory = None
    repack_factory = None

    pf = mobileBranchConfig['platforms'][platform]
    clobberTime = pf.get('clobber_time', branchConfig['default_clobber_time'])
    packageGlobList = []
    if platform == 'linux-i686':
        packageGlobList = ['-r', 'dist/*.tar.bz2',
                           'dist/*.zip']
    elif platform == 'macosx-i686':
        packageGlobList = ['-r', 'dist/*.dmg']
    elif platform == 'win32-i686':
        packageGlobList = ['-r', 'dist/*.zip']
    
    build_factory = ReleaseMobileDesktopBuildFactory(
        hgHost=branchConfig['hghost'],
        repoPath=mozSourceRepoPath,
        configRepoPath=branchConfig['config_repo_path'],
        configSubDir=branchConfig['config_subdir'],
        mozconfig=pf['mozconfig'].replace('nightly', 'release'),
        env=pf['env'],
        stageUsername=branchConfig['stage_username'],
        stageGroup=branchConfig['stage_group'],
        stageSshKey=branchConfig['stage_ssh_key'],
        stageServer=branchConfig['stage_server'],
        stageBasePath='%s/%s' % (candidatesPath, platform),
        mobileRepoPath=mobileSourceRepoPath,
        mozRevision='%s_RELEASE' % baseTag,
        mobileRevision='%s_RELEASE' % baseTag,
        platform=platform,
        uploadSymbols=True,
        packageGlobList=packageGlobList,
        baseWorkDir=pf['base_workdir'],
        baseUploadDir=baseUploadDir,
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        clobberURL=branchConfig['base_clobber_url'],
        clobberTime=clobberTime,
        buildSpace=10,
        buildsBeforeReboot=pf['builds_before_reboot'],
        triggerBuilds=False,
    )

    builders.append({
        'name': 'mobile_%s_desktop_build' % platform,
        'slavenames': pf['slaves'],
        'category': 'release',
        'builddir': 'mobile_%s_desktop_build' % platform,
        'factory': build_factory
    })

    if platform in l10nDesktopPlatforms:
        # Not implemented yet
        pass

if doPartnerRepacks:
    partner_repack_factory = PartnerRepackFactory(
        hgHost=branchConfig['hghost'],
        repoPath='mozRepoPath',
        buildToolsRepoPath=branchConfig['build_tools_repo_path'],
        productName='mobile',
        version=version,
        buildNumber=buildNumber,
        partnersRepoPath=partnersRepoPath,
        stagingServer=stagingServer,
        stageUsername=branchConfig['stage_username'],
        stageSshKey=branchConfig['stage_ssh_key'],
        nightlyDir='candidates',
        platformList=partnerRepackPlatforms,
        baseWorkDir='%s-partner' % mobileBranchConfig['platforms']['maemo4']['base_workdir'],
        python='python2.5',
        packageDmg=False,
        createRemoteStageDir=True
    )
    builders.append({
        'name': 'mobile_partner_repack',
        'slavenames': branchConfig['platforms']['linux']['slaves'],
        'category': 'release',
        'builddir': 'mobile_partner_repack',
        'factory': partner_repack_factory
    })
