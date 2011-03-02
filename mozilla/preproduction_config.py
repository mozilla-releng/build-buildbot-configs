MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in range(1,30) + range(40,55)]
MAC_MINIS      = ['moz2-darwin9-slave%02i' % x for x in range(1,4) + range(5,73)]
XSERVES        = ['bm-xserve%02i' % x for x in [6,7,9,11,12,15,16,17,18,19,21,22]]
WIN32_VMS      = ['win32-slave%02i' % x for x in range(1,61)]
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in range(1,26)]
LINUX_VMS      = ['moz2-linux-slave%02i' % x for x in range(1,61)]
LINUX_IXS      = ['mv-moz2-linux-ix-slave%02i' % x for x in range(1,25)]
SLAVES = {
    'linux':       LINUX_VMS + LINUX_IXS,
    'linux64':     ['moz2-linux64-slave%02i' % x for x in range(1,13)],
    'win32':       WIN32_VMS + WIN32_IXS,
    'macosx':      MAC_MINIS + XSERVES,
    'macosx64': MAC_SNOW_MINIS,
}

TRY_LINUX      = ['try-linux-slave%02i' % x for x in range (1,26)]
TRY_LINUX_IXS  = []
TRY_LINUX64    = ['try-linux64-slave%02i' % x for x in range (1,11)]
TRY_MAC        = ['try-mac-slave%02i' % x for x in range (1,48)]
TRY_MAC64      = ['try-mac64-slave%02i' % x for x in range (1,27)]
TRY_WIN32      = ['try-w32-slave%02i' % x for x in range (1,32)]
TRY_WIN32_IXS  = []

TRY_SLAVES = SLAVES
TRY_SLAVES['linux'] += TRY_LINUX + TRY_LINUX_IXS
TRY_SLAVES['linux64'] += TRY_LINUX64
TRY_SLAVES['macosx'] += TRY_MAC
TRY_SLAVES['macosx64'] += TRY_MAC64
TRY_SLAVES['win32'] += TRY_WIN32 + TRY_WIN32_IXS


GLOBAL_VARS = {
    'config_repo_path': 'build/buildbot-configs',
    'stage_server': 'preproduction-stage.build.mozilla.org',
    'aus2_host': 'preproduction-stage.build.mozilla.org',
    'download_base_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/firefox',
    'mobile_download_base_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/mobile',
    'graph_server': 'graphs-stage.mozilla.org',#TODO
    'build_tools_repo_path': 'users/prepr-ffxbld/tools',#TODO
    'base_clobber_url': 'http://build.mozilla.org/preproduction-clobberer/index.php', #TODO
    'pollInterval': 6*60*60,
    'l10nPollInterval': 6*60*60,
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('preproduction-master.build.mozilla.org:9009', True, 1), #TODO
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('preproduction-master.build.mozilla.org:9009', True, 1), #TODO
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
    'tryserver': {
        'download_base_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/firefox',
        'mobile_download_base_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/mobile',
        'enable_mail_notifier': False,
        'package_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
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
        'fuzzing_remote_host': 'ffxbld@staging-stage.build.mozilla.org',
        'fuzzing_base_dir': '/mnt/eql/builds/firefox/pvt-builds/fuzzing/',
        'idle_slaves': 0,
    },
    'nanojit': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Releng-Preproduction',
    },
    'valgrind': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Releng-Preproduction',
    },
    'spidermonkey': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Releng-Preproduction',
    },
}
