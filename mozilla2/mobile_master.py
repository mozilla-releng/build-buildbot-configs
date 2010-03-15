# ex: set syntax=python:

####### BUILDSLAVES


####### SCHEDULERS AND CHANGE SOURCES

import buildbotcustom.changes.hgpoller
from buildbotcustom.changes.hgpoller import HgPoller, HgAllLocalesPoller
from buildbot.scheduler import Scheduler, Nightly

import buildbot.status.tinderbox
from buildbot.status.tinderbox import TinderboxMailNotifier

import buildbotcustom.misc
from buildbotcustom.misc import isHgPollerTriggered

from buildbotcustom.scheduler import MozScheduler

import buildbotcustom.process.factory
from buildbotcustom.process.factory import MaemoBuildFactory, \
   WinmoBuildFactory, MaemoNightlyRepackFactory, \
   MobileDesktopBuildFactory, MobileDesktopNightlyRepackFactory

from buildbot.steps import trigger
from buildbot.steps.shell import WithProperties

from buildbotcustom.l10n import MultiNightlyL10n, NightlyL10n, Scheduler as SchedulerL10n


# most of the config is in an external file
import config
reload(config)
from config import *
import mobile_config
reload(mobile_config)
from mobile_config import MOBILE_BRANCHES

m = {}

m['builders'] = []
m['schedulers'] = []
m['change_source'] = []
m['status'] = []

mobileBuilders = []

# Like the main cfg, except mobile
for name in sorted(MOBILE_BRANCHES.keys()):
    branch = MOBILE_BRANCHES[name]
    mainConfig = branch['main_config']
    builders = []
    nightlyBuilders = []
    l10nNightlyBuilders = {}
    for platform in branch['platforms'].keys():
        base_name = branch['platforms'][platform]['base_name']

        # hack alert: no dep desktop builds
        if platform not in ['macosx-i686', 'win32-i686']:
            builders.append('%s build' % base_name)
            mobileBuilders.append('%s build' % base_name)

        builder = '%s nightly' % base_name
        nightlyBuilders.append(builder)
        if branch['enable_l10n'] and platform in branch['l10n_platforms']:
            l10nNightlyBuilders[builder] = {}
            l10nNightlyBuilders[builder]['tree'] = branch['l10n_tree']
            l10nNightlyBuilders[builder]['l10n_builder'] = '%s l10n' % base_name
            l10nNightlyBuilders[builder]['platform'] = branch['l10n_platforms'][platform]

    m['status'].append(TinderboxMailNotifier(
        fromaddr="mozilla2.buildbot@build.mozilla.org",
        tree=branch['tinderbox_tree'],
        extraRecipients=['tinderbox-daemon@tinderbox.mozilla.org'],
        relayhost='mail.build.mozilla.org',
        builders=builders + nightlyBuilders,
        logCompression='bzip2'
    ))

    if branch['enable_l10n']:
        l10n_builders = []
        for b in l10nNightlyBuilders:
            l10n_builders.append(l10nNightlyBuilders[b]['l10n_builder'])
            l10n_builders.append(l10nNightlyBuilders[b]['l10n_builder'] + " build")
        # General tinderbox page
        m['status'].append(TinderboxMailNotifier(
            fromaddr="buildbot@mozilla.com",
            tree=branch['l10n_tinderbox_tree'],
            extraRecipients=['tinderbox-daemon@tinderbox.mozilla.org'],
            relayhost='mail.build.mozilla.org',
            logCompression='bzip2',
            builders=l10n_builders,
            binaryURL='http://%s/pub/mozilla.org/mobile/nightly/latest-%s-l10n' \
                      % (mainConfig['stage_server'], name)
        ))
        # Locale-specific page
        m['status'].append(TinderboxMailNotifier(
            fromaddr="buildbot@mozilla.com",
            tree=WithProperties(branch['l10n_tinderbox_tree'] + '-%(locale)s'),
            extraRecipients=['tinderbox-daemon@tinderbox.mozilla.org'],
            relayhost='mail.build.mozilla.org',
            logCompression='bzip2',
            builders=l10n_builders,
            binaryURL='http://%s/pub/mozilla.org/mobile/nightly/latest-%s-l10n' \
                      % (mainConfig['stage_server'], name)
        ))

    #
    # For now, there are no additional change_sources (except for
    # mobile-browser below) since mobile only builds on branches that
    # are already being polled in master.cfg
    #

    # nightly builders
    for builder in nightlyBuilders:
        if builder in l10nNightlyBuilders and \
           branch['enable_l10n'] and branch['enable_multi_locale'] and \
           builder.startswith('Maemo') and builder.endswith('nightly') and \
           l10nNightlyBuilders[builder]['platform'] in ('linux-gnueabi-arm'):
            nightly_scheduler=MultiNightlyL10n(
                name=builder,
                branch=branch['mobile_repo_path'], # mobile_repo_path
                hour=[1],
                builderNames=[builder],
                localesFile=branch['multiLocalesFile'],
                platform=l10nNightlyBuilders[builder]['platform'],
            )
        else:
            nightly_scheduler=Nightly(
                name=builder,
                branch=branch['mobile_repo_path'], # mobile_repo_path
                hour=[1],
                builderNames=[builder],
            )
        m['schedulers'].append(nightly_scheduler)
        if branch['enable_l10n'] and builder in l10nNightlyBuilders:
            l10n_builder = l10nNightlyBuilders[builder]['l10n_builder']
            l10nPlatform = l10nNightlyBuilders[builder]['platform']
            tree = l10nNightlyBuilders[builder]['tree']
            m['schedulers'].append(NightlyL10n(
                name=l10n_builder,
                platform=l10nPlatform,
                tree=tree,
                builderNames=[l10n_builder],
                repoType='hg',
                branch=branch['mobile_repo_path'],
                baseTag='default',
                localesFile=branch['allLocalesFile']
            ))

    m['schedulers'].append(MozScheduler(
        name='mobile %s' % name,
        branch=branch['repo_path'],
        treeStableTimer=3*60,
        idleTimeout=branch.get('idle_timeout', None),
        builderNames=builders,
        fileIsImportant=lambda c: isHgPollerTriggered(c, mainConfig['hgurl'])
    ))

    for platform in sorted(branch['platforms'].keys()):
        pf = branch['platforms'][platform]

        buildSpace = pf.get('build_space', mainConfig['default_build_space'])
        clobberTime = pf.get('clobber_time', mainConfig['default_clobber_time'])

        mobile_dep_factory = None
        mobile_nightly_factory = None

        nightly_builder = '%s nightly' % pf['base_name']
        triggeredSchedulers=None
        if branch['enable_l10n'] and \
           platform in branch['l10n_platforms'] and \
           nightly_builder in l10nNightlyBuilders:
            triggeredSchedulers=[l10nNightlyBuilders[nightly_builder]['l10n_builder']]
            
        if platform == 'linux-gnueabi-arm':
            mobile_dep_factory = MaemoBuildFactory(
                hgHost=mainConfig['hghost'],
                repoPath=branch['repo_path'],
                configRepoPath=mainConfig['config_repo_path'],
                configSubDir=mainConfig['config_subdir'],
                mozconfig=pf['mozconfig'],
                stageUsername=mainConfig['stage_username'],
                stageGroup=mainConfig['stage_group'],
                stageSshKey=mainConfig['stage_ssh_key'],
                stageServer=mainConfig['stage_server'],
                stageBasePath=branch['stage_base_path'],
                mobileRepoPath=branch['mobile_repo_path'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseBuildDir=pf['base_builddir'],
                baseUploadDir=name,
                buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                clobberURL=mainConfig['base_clobber_url'],
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                buildsBeforeReboot=pf['builds_before_reboot'],
            )
            nightlyWorkDir  = pf['base_workdir']  + '-nightly'
            nightlyBuildDir = pf['base_builddir'] + '-nightly'
            mobile_nightly_factory = MaemoBuildFactory(
                hgHost=mainConfig['hghost'],
                repoPath=branch['repo_path'],
                configRepoPath=mainConfig['config_repo_path'],
                configSubDir=mainConfig['config_subdir'],
                mozconfig=pf['mozconfig'],
                stageUsername=mainConfig['stage_username'],
                stageGroup=mainConfig['stage_group'],
                stageSshKey=mainConfig['stage_ssh_key'],
                stageServer=mainConfig['stage_server'],
                stageBasePath=branch['stage_base_path'],
                mobileRepoPath=branch['mobile_repo_path'],
                platform=platform,
                baseWorkDir=nightlyWorkDir,
                baseBuildDir=nightlyBuildDir,
                baseUploadDir=name,
                buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                clobberURL=mainConfig['base_clobber_url'],
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                buildsBeforeReboot=pf['builds_before_reboot'],
                nightly = True,
                multiLocale = branch['enable_multi_locale'],
                l10nRepoPath = branch['l10n_repo_path'],
                triggerBuilds = True,
                triggeredSchedulers=triggeredSchedulers
            )
        elif platform == 'linux-i686':
            mobile_dep_factory = MobileDesktopBuildFactory(
                hgHost=mainConfig['hghost'],
                repoPath=branch['repo_path'],
                configRepoPath=mainConfig['config_repo_path'],
                configSubDir=mainConfig['config_subdir'],
                mozconfig=pf['mozconfig'],
                env=pf['env'],
                stageUsername=mainConfig['stage_username'],
                stageGroup=mainConfig['stage_group'],
                stageSshKey=mainConfig['stage_ssh_key'],
                stageServer=mainConfig['stage_server'],
                stageBasePath=branch['stage_base_path'],
                mobileRepoPath=branch['mobile_repo_path'],
                packageGlobList=['-r', 'mobile/dist/*.tar.bz2',
                                 'xulrunner/dist/*.tar.bz2'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                clobberURL=mainConfig['base_clobber_url'],
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                buildsBeforeReboot=pf['builds_before_reboot'],
            )
            mobile_nightly_factory = MobileDesktopBuildFactory(
                hgHost=mainConfig['hghost'],
                repoPath=branch['repo_path'],
                configRepoPath=mainConfig['config_repo_path'],
                configSubDir=mainConfig['config_subdir'],
                mozconfig=pf['mozconfig'],
                env=pf['env'],
                stageUsername=mainConfig['stage_username'],
                stageGroup=mainConfig['stage_group'],
                stageSshKey=mainConfig['stage_ssh_key'],
                stageServer=mainConfig['stage_server'],
                stageBasePath=branch['stage_base_path'],
                mobileRepoPath=branch['mobile_repo_path'],
                packageGlobList=['-r', 'mobile/dist/*.tar.bz2',
                                 'xulrunner/dist/*.tar.bz2'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                clobberURL=mainConfig['base_clobber_url'],
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                buildsBeforeReboot=pf['builds_before_reboot'],
                nightly = True,
                triggerBuilds = True,
                triggeredSchedulers=triggeredSchedulers
            )
        elif platform == 'macosx-i686':
            mobile_nightly_factory = MobileDesktopBuildFactory(
                hgHost=mainConfig['hghost'],
                repoPath=branch['repo_path'],
                configRepoPath=mainConfig['config_repo_path'],
                configSubDir=mainConfig['config_subdir'],
                mozconfig=pf['mozconfig'],
                env=pf['env'],
                stageUsername=mainConfig['stage_username'],
                stageGroup=mainConfig['stage_group'],
                stageSshKey=mainConfig['stage_ssh_key'],
                stageServer=mainConfig['stage_server'],
                stageBasePath=branch['stage_base_path'],
                mobileRepoPath=branch['mobile_repo_path'],
                packageGlobList=['-r', 'mobile/dist/*.dmg'],
                platform="macosx",
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                clobberURL=mainConfig['base_clobber_url'],
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                buildsBeforeReboot=pf['builds_before_reboot'],
                nightly = True,
                triggerBuilds = True,
                triggeredSchedulers=triggeredSchedulers
            )
        elif platform == 'win32-i686':
            mobile_nightly_factory = MobileDesktopBuildFactory(
                hgHost=mainConfig['hghost'],
                repoPath=branch['repo_path'],
                configRepoPath=mainConfig['config_repo_path'],
                configSubDir=mainConfig['config_subdir'],
                mozconfig=pf['mozconfig'],
                env=pf['env'],
                stageUsername=mainConfig['stage_username'],
                stageGroup=mainConfig['stage_group'],
                stageSshKey=mainConfig['stage_ssh_key'],
                stageServer=mainConfig['stage_server'],
                stageBasePath=branch['stage_base_path'],
                mobileRepoPath=branch['mobile_repo_path'],
                platform="win32",
                packageGlobList=['-r', 'mobile/dist/*.zip',
                                 'xulrunner/dist/*.zip'],
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                clobberURL=mainConfig['base_clobber_url'],
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                buildsBeforeReboot=pf['builds_before_reboot'],
                nightly = True,
                triggerBuilds = True,
                triggeredSchedulers=triggeredSchedulers
            )
        else:
            mobile_dep_factory=WinmoBuildFactory(
                hgHost=mainConfig['hghost'],
                repoPath=branch['repo_path'],
                configRepoPath=mainConfig['config_repo_path'],
                configSubDir=mainConfig['config_subdir'],
                env=pf['env'],
                mozconfig=pf['mozconfig'],
                stageUsername=mainConfig['stage_username'],
                stageGroup=mainConfig['stage_group'],
                stageSshKey=mainConfig['stage_ssh_key'],
                stageServer=mainConfig['stage_server'],
                stageBasePath=branch['stage_base_path'],
                mobileRepoPath=branch['mobile_repo_path'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                clobberURL=mainConfig['base_clobber_url'],
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                buildsBeforeReboot=pf['builds_before_reboot'],
            )
            mobile_nightly_factory=WinmoBuildFactory(
                hgHost=mainConfig['hghost'],
                repoPath=branch['repo_path'],
                configRepoPath=mainConfig['config_repo_path'],
                configSubDir=mainConfig['config_subdir'],
                env=pf['env'],
                mozconfig=pf['mozconfig'],
                stageUsername=mainConfig['stage_username'],
                stageGroup=mainConfig['stage_group'],
                stageSshKey=mainConfig['stage_ssh_key'],
                stageServer=mainConfig['stage_server'],
                stageBasePath=branch['stage_base_path'],
                mobileRepoPath=branch['mobile_repo_path'],
                platform=platform,
                baseWorkDir=pf['base_workdir'],
                baseUploadDir=name,
                buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                clobberURL=mainConfig['base_clobber_url'],
                clobberTime=clobberTime,
                buildSpace=buildSpace,
                buildsBeforeReboot=pf['builds_before_reboot'],
                nightly=True,
                createSnippet=pf['create_snippet'],
                downloadBaseURL=branch['download_base_url'],
                ausUser=mainConfig['aus2_user'],
                ausHost=mainConfig['aus2_host'],
                ausBaseUploadDir=branch['aus2_base_upload_dir'],
            )
        mobile_dep_builder = None
        if mobile_dep_factory is not None:
            mobile_dep_builder = {
                'name': '%s build' % pf['base_name'],
                'slavenames': pf['slaves'],
                'builddir': pf['base_builddir'],
                'factory': mobile_dep_factory,
                'category': name
            }
        nightly_builder = '%s nightly' % pf['base_name']
        mobile_nightly_builder = {
            'name': nightly_builder,
            'slavenames': pf['slaves'],
            'builddir': '%s-nightly' % (pf['base_builddir']),
            'factory': mobile_nightly_factory,
            'category': name
        }
        if mobile_dep_builder is not None:
            m['builders'].append(mobile_dep_builder)
        m['builders'].append(mobile_nightly_builder)

        if branch['enable_l10n'] and platform in branch['l10n_platforms']:
            mobile_l10n_nightly_factory = None
            if platform == 'linux-gnueabi-arm':
                nightlyBuildDir = pf['base_builddir'] + '-l10n'
                depBuildDir = pf['base_builddir'] + '-l10n-dep'
                mobile_l10n_nightly_factory = MaemoNightlyRepackFactory(
                    nightly = True,
                    hgHost=mainConfig['hghost'],
                    tree=branch['l10n_tree'],
                    project=branch['product_name'],
                    appName=branch['app_name'],
                    packageGlobList=['-r', '%(locale)s',
                                     'fennec-*.%(locale)s.linux-gnueabi-arm.tar.bz2',
                                     'install/fennec-*.%(locale)s.langpack.xpi'],
                    enUSBinaryURL=branch['enUS_binaryURL'],
                    stageServer=mainConfig['stage_server'],
                    stageUsername=mainConfig['stage_username'],
                    configSubDir=mainConfig['config_subdir'],
                    mozconfig=pf['mozconfig'],
                    configRepoPath=mainConfig['config_repo_path'],
                    stageSshKey=mainConfig['stage_ssh_key'],
                    stageBasePath=branch['stage_base_path'],
                    repoPath=branch['repo_path'],
                    l10nRepoPath=branch['l10n_repo_path'],
                    mobileRepoPath=branch['mobile_repo_path'],
                    buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                    compareLocalesRepoPath=mainConfig['compare_locales_repo_path'],
                    compareLocalesTag=mainConfig['compare_locales_tag'],
                    buildSpace=2,
                    baseWorkDir=pf['base_l10n_workdir'],
                    baseBuildDir=nightlyBuildDir,
                    baseUploadDir='%s-l10n' % name,
                    clobberURL=mainConfig['base_clobber_url'],
                    clobberTime=clobberTime,
                )
                if branch['enable_l10n_onchange']:
                    mobile_l10n_dep_factory = MaemoNightlyRepackFactory(
                        nightly = False,
                        hgHost=mainConfig['hghost'],
                        tree=branch['l10n_tree'],
                        project=branch['product_name'],
                        appName=branch['app_name'],
                        packageGlobList=['-r', '%(locale)s',
                                         'fennec-*.%(locale)s.linux-gnueabi-arm.tar.bz2',
                                         'install/fennec-*.%(locale)s.langpack.xpi'],
                        enUSBinaryURL=branch['enUS_binaryURL'],
                        stageServer=mainConfig['stage_server'],
                        stageUsername=mainConfig['stage_username'],
                        configSubDir=mainConfig['config_subdir'],
                        mozconfig=pf['mozconfig'],
                        configRepoPath=mainConfig['config_repo_path'],
                        stageSshKey=mainConfig['stage_ssh_key'],
                        stageBasePath=branch['stage_base_path'],
                        repoPath=branch['repo_path'],
                        l10nRepoPath=branch['l10n_repo_path'],
                        mobileRepoPath=branch['mobile_repo_path'],
                        buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                        compareLocalesRepoPath=mainConfig['compare_locales_repo_path'],
                        compareLocalesTag=mainConfig['compare_locales_tag'],
                        buildSpace=2,
                        baseWorkDir=pf['base_l10n_workdir'],
                        baseBuildDir=depBuildDir,
                        baseUploadDir='%s-l10n' % name,
                        clobberURL=mainConfig['base_clobber_url'],
                        clobberTime=clobberTime,
                    )
            elif platform.endswith('i686'):
                if platform == 'linux-i686':
                    realPlatform = 'linux'
                    packageGlobList = ['fennec-*.%(locale)s.linux-i686.tar.bz2',
                                       'install/fennec-*.%(locale)s.langpack.xpi']
                elif platform == 'macosx-i686':
                    realPlatform = 'macosx'
                    packageGlobList = ['-r', 'fennec-*.%(locale)s.mac.dmg']
                elif platform == 'win32-i686':
                    realPlatform = 'win32'
                    packageGlobList = ['fennec-*.%(locale)s.win32.zip']

                mobile_l10n_nightly_factory = MobileDesktopNightlyRepackFactory(
                    nightly=True,
                    hgHost=mainConfig['hghost'],
                    tree=branch['l10n_tree'],
                    project=branch['product_name'],
                    appName=branch['app_name'],
                    packageGlobList=packageGlobList,
                    enUSBinaryURL=branch['enUS_binaryURL'],
                    platform=realPlatform,
                    stageServer=mainConfig['stage_server'],
                    stageUsername=mainConfig['stage_username'],
                    stageSshKey=mainConfig['stage_ssh_key'],
                    stageBasePath=branch['stage_base_path'],
                    repoPath=branch['repo_path'],
                    l10nRepoPath=branch['l10n_repo_path'],
                    mobileRepoPath=branch['mobile_repo_path'],
                    buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                    compareLocalesRepoPath=mainConfig['compare_locales_repo_path'],
                    compareLocalesTag=mainConfig['compare_locales_tag'],
                    buildSpace=2,
                    baseWorkDir=pf['base_l10n_workdir'],
                    baseUploadDir='%s-l10n' % name,
                    clobberURL=mainConfig['base_clobber_url'],
                    clobberTime=clobberTime,
                )
                if branch['enable_l10n_onchange']:
                    mobile_l10n_dep_factory = MobileDesktopNightlyRepackFactory(
                        nightly=False,
                        hgHost=mainConfig['hghost'],
                        tree=branch['l10n_tree'],
                        project=branch['product_name'],
                        appName=branch['app_name'],
                        packageGlobList=packageGlobList,
                        enUSBinaryURL=branch['enUS_binaryURL'],
                        platform=realPlatform,
                        stageServer=mainConfig['stage_server'],
                        stageUsername=mainConfig['stage_username'],
                        stageSshKey=mainConfig['stage_ssh_key'],
                        stageBasePath=branch['stage_base_path'],
                        repoPath=branch['repo_path'],
                        l10nRepoPath=branch['l10n_repo_path'],
                        mobileRepoPath=branch['mobile_repo_path'],
                        buildToolsRepoPath=mainConfig['build_tools_repo_path'],
                        compareLocalesRepoPath=mainConfig['compare_locales_repo_path'],
                        compareLocalesTag=mainConfig['compare_locales_tag'],
                        buildSpace=2,
                        baseWorkDir=pf['base_l10n_workdir'],
                        baseUploadDir='%s-l10n' % name,
                        clobberURL=mainConfig['base_clobber_url'],
                        clobberTime=clobberTime,
                   )

            mobile_l10n_nightly_builder = {
                'name': l10nNightlyBuilders[nightly_builder]['l10n_builder'],
                'slavenames': pf['slaves'],
                'builddir': '%s-l10n-nightly' % (pf['base_builddir']),
                'factory': mobile_l10n_nightly_factory,
                'category': name,
            }
            m['builders'].append(mobile_l10n_nightly_builder)
            if branch['enable_l10n_onchange']:
                mobile_l10n_dep_builder = {
                    'name': l10nNightlyBuilders[nightly_builder]['l10n_builder'] + " build",
                    'slavenames': pf['slaves'],
                    'builddir': '%s-l10n-dep' % (pf['base_builddir']),
                    'factory': mobile_l10n_dep_factory,
                    'category': name,
                }
                m['builders'].append(mobile_l10n_dep_builder)


# mobile-browser, which is shared
m['change_source'].append(HgPoller(
    hgURL=mainConfig['hgurl'],
    branch='mobile-browser',
    pushlogUrlOverride='http://hg.mozilla.org/mobile-browser/pushlog',
    pollInterval=1*60
))
m['schedulers'].append(Scheduler(
    name="mobile-browser",
    branch="mobile-browser",
    treeStableTimer=3*60,
    builderNames=mobileBuilders,
    fileIsImportant=lambda c: isHgPollerTriggered(c, mainConfig['hgurl'])
))
