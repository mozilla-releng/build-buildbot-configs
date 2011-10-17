MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in range(1,30) + range(40,57)]
MAC_MINIS      = ['moz2-darwin9-slave%02i' % x for x in range(1,73) if x not in (4,5,20,40,59)]
XSERVES        = ['bm-xserve%02i' % x for x in range(6,13) + range(15,25)]
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in range(1,26)] + ['w32-ix-slave%02i' % x for x in range(1,43)]
WIN64_IXS      = ['mw64-ix-slave01'] + ['w64-ix-slave%02i' % x for x in range(1,43)]
LINUX_VMS      = ['moz2-linux-slave%02i' % x for x in range(1,61)]
LINUX_IXS      = ['mv-moz2-linux-ix-slave%02i' % x for x in range(1,24)] + ['linux-ix-slave%02i' % x for x in range(1,43)]
LINUX64_VMS    = ['moz2-linux64-slave%02i' % x for x in range(1,13)]
LINUX64_IXS    = ['linux64-ix-slave%02i' % x for x in range(1,42)]
SLAVES = {
    'linux':            LINUX_VMS + LINUX_IXS,
    'linux64':          LINUX64_VMS + LINUX64_IXS,
    'win32':            WIN32_IXS,
    'win64':            WIN64_IXS,
    'macosx':           MAC_MINIS + XSERVES,
    'macosx64':         MAC_SNOW_MINIS,
    'linux-android':    LINUX_VMS + LINUX_IXS,
    'linux-maemo5-gtk': LINUX_VMS + LINUX_IXS,
    'linux-mobile':     LINUX_VMS + LINUX_IXS,
    'macosx-mobile':    MAC_MINIS + XSERVES,
    'win32-mobile':     WIN32_IXS,
}

TRY_LINUX      = ['try-linux-slave%02i' % x for x in range (1,31)]
TRY_LINUX_IXS  = []
TRY_LINUX64    = ['try-linux64-slave%02i' % x for x in range (1,11)]
TRY_LINUX64_IXS= ['linux64-ix-slave%02i' % x for x in range(22,41)]
TRY_MAC        = ['try-mac-slave%02i' % x for x in range (1,48)]
TRY_MAC64      = ['try-mac64-slave%02i' % x for x in range (1,32)]
TRY_WIN32_IXS  = []

TRY_SLAVES = SLAVES
TRY_SLAVES['linux'] += TRY_LINUX + TRY_LINUX_IXS
TRY_SLAVES['linux64'] += TRY_LINUX64 + TRY_LINUX64_IXS
TRY_SLAVES['macosx'] += TRY_MAC
TRY_SLAVES['macosx64'] += TRY_MAC64
TRY_SLAVES['win32'] += TRY_WIN32_IXS


GLOBAL_VARS = {
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'compare_locales_repo_path': 'build/compare-locales',
    'build_tools_repo_path': 'build/tools',
    'stage_server': 'preproduction-stage.build.mozilla.org',
    'aus2_host': 'preproduction-stage.build.mozilla.org',
    'download_base_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/firefox',
    'mobile_download_base_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/mobile',
    'graph_server': 'graphs-stage.mozilla.org',#TODO
    'base_clobber_url': 'http://build.mozilla.org/preproduction-clobberer/index.php',
    'pollInterval': 6*60*60,
    'l10nPollInterval': 6*60*60,
    'disable_tinderbox_mail': True,
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('preproduction-master.build.mozilla.org:9009', True, 1),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('preproduction-master.build.mozilla.org:9009', True, 1),
        ],
    'xulrunner_tinderbox_tree': 'Releng-Preproduction',
    'weekly_tinderbox_tree': 'Releng-Preproduction',
    'l10n_tinderbox_tree': 'Releng-Preproduction',
    'packaged_unittest_tinderbox_tree': 'Releng-Preproduction',
    'tinderbox_tree': 'Releng-Preproduction',
    'mobile_tinderbox_tree': 'Releng-Preproduction',
}

BUILDS_BEFORE_REBOOT = 1
SYMBOL_SERVER_HOST = 'preproduction-stage.build.mozilla.org'

# Local branch overrides
BRANCHES = {
    'try': {
        'download_base_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/firefox',
        'mobile_download_base_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/mobile',
        'enable_mail_notifier': False,
        'package_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'build.mozilla.org', # TODO
                    'CVS_RSH': 'ssh',
                    'MOZ_OBJDIR': 'obj-firefox',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',

                },
            },
        }
    }
}

PLATFORM_VARS = {
}

PROJECTS = {
    'fuzzing': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'fuzzing_repo': 'ssh://stage-ffxbld@hg.mozilla.org/private/fuzzing',
        'fuzzing_remote_host': 'ffxbld@dev-stage01.build.sjc1.mozilla.com',
        'fuzzing_base_dir': '/mnt/eql/builds/firefox/pvt-builds/fuzzing/',
        'idle_slaves': 0,
    },
    'nanojit': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Releng-Preproduction',
    },
    'spidermonkey_mozilla-inbound': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Releng-Preproduction',
    },
    'spidermonkey_ionmonkey': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Releng-Preproduction',
    },
}
