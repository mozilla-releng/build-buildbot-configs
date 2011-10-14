MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in range(5,10) + range(15,30) + range(40,57)]
MAC_MINIS      = ['moz2-darwin9-slave%02i' % x for x in range(1,73) if x not in (3,4,5,8,10,20,27,28,40,59,68)]
XSERVES        = ['bm-xserve%02i' % x for x in [6,7,9,11,12,15,16,17,18,19,21,22]]
LINUX_VMS      = ['moz2-linux-slave%02i' % x for x in [1,2] + range(5,10) + range(11,17) + range(18,47)]
LINUX_IXS      = ['mv-moz2-linux-ix-slave%02i' % x for x in range(2,22)] + \
                 ['linux-ix-slave%02i' % x for x in range(12,43)] + \
                 ['linux-ix-slave%02i' % x for x in (1,2,6)] # added for bug 638309
LINUX64_VMS    = ['moz2-linux64-slave%02i' % x for x in range(1,7) + range(8,10) + range(11,13)]
LINUX64_IXS    = ['linux64-ix-slave%02i' % x for x in range(3,22)]
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in range(2,16) + [20]] + ['w32-ix-slave%02i' % x for x in range(1,2) + range(24,43)]
WIN64_IXS      = ['w64-ix-slave%02i' % x for x in [2] + range(6,25)]

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

TRY_LINUX      = ['try-linux-slave%02i' % x for x in range(1,5) + range(6,31)] + \
                 ['moz2-linux-slave%02i' % x for x in range(47,51)]
TRY_LINUX_IXS  = ['mv-moz2-linux-ix-slave%02i' % x for x in range(22,24)] + \
                 ['linux-ix-slave%02i' % x for x in range(7,12)]
TRY_LINUX64    = ['try-linux64-slave%02i' % x for x in range(1,11)]
TRY_LINUX64_IXS= ['linux64-ix-slave%02i' % x for x in range(22,42)]
TRY_MAC        = ['try-mac-slave%02i' % x for x in range(1,5) + range(6,48)]
TRY_MAC.remove('try-mac-slave35') # Bug 650297
TRY_XSERVES    = ['bm-xserve%02i' % x for x in [8,10,20,23,24]]
TRY_MAC64      = ['try-mac64-slave%02i' % x for x in range(1,32)] + \
                 ['moz2-darwin10-slave%02i' % x for x in range(11,15)]
TRY_WIN32_IXS  = ['mw32-ix-slave%02i' % x for x in range(16,19) + range(22,26)] + \
                 ['w32-ix-slave%02i' % x for x in range(2,24)]
TRY_WIN64_IXS  = ['w64-ix-slave%02i' % x for x in range(25,43)]
TRY_SLAVES = {
    'linux':       TRY_LINUX + TRY_LINUX_IXS,
    'linux64':     TRY_LINUX64 + TRY_LINUX64_IXS,
    'win32':       TRY_WIN32_IXS,
    'win64':       TRY_WIN64_IXS,
    'macosx':      TRY_MAC + TRY_XSERVES,
    'macosx64':    TRY_MAC64,
}

# Local overrides for default values
GLOBAL_VARS = {
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'stage.mozilla.org',
    'aus2_host': 'aus2-staging.mozilla.org',
    'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox',
    'mobile_download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/mobile',
    'graph_server': 'graphs.mozilla.org',
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://build.mozilla.org/clobberer/index.php',
    'disable_tinderbox_mail': True,
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('buildbot-master10.build.mozilla.org:9301', True, 5),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('buildbot-master10.build.mozilla.org:9301', True, 5),
        ('geriatric-master.build.mozilla.org:9989', False, 1),
    ],
    'xulrunner_tinderbox_tree': 'XULRunner',
    'weekly_tinderbox_tree': 'Testing',
    'l10n_tinderbox_tree': 'Mozilla-l10n',
}

BUILDS_BEFORE_REBOOT = 1
SYMBOL_SERVER_HOST = 'dm-symbolpush01.mozilla.org'

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'packaged_unittest_tinderbox_tree': 'Firefox',
        'tinderbox_tree': 'Firefox',
        'mobile_tinderbox_tree': 'Mobile',
        'mobile_build_failure_emails': ['mobile-build-failures@mozilla.org'],
    },
    'shadow-central': {
        'packaged_unittest_tinderbox_tree': 'Shadow-Central',
        'tinderbox_tree': 'Shadow-Central',
        'mobile_tinderbox_tree': 'Shadow-Central',
        'mobile_build_failure_emails': ['mobile-build-failures@mozilla.org'],
        'build_tools_repo_path' : 'http://hg.mozilla.org/build/tools',
        'stage_server' : 'dm-pvtbuild01.mozilla.org',
        'hghost' : 'ssh://ffxbld@hgpvt.mozilla.org',
        'stage_base_path' : '/mnt/pvt_builds',
        'stage_log_base_url': 'https://dm-pvtbuild01.mozilla.org',
    },
    'mozilla-1.9.1': {
        'packaged_unittest_tinderbox_tree': 'Firefox3.5',
        'tinderbox_tree': 'Firefox3.5',
        'mobile_tinderbox_tree': 'MobileTest',
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'Firefox3.6',
        'packaged_unittest_tinderbox_tree': 'Firefox3.6',
        'mobile_tinderbox_tree': 'Mobile1.1',
    },
    'mozilla-release': {
        'packaged_unittest_tinderbox_tree': 'Mozilla-Release',
        'tinderbox_tree': 'Mozilla-Release',
        'mobile_tinderbox_tree': 'Mozilla-Release',
    },
    'mozilla-beta': {
        'packaged_unittest_tinderbox_tree': 'Mozilla-Beta',
        'tinderbox_tree': 'Mozilla-Beta',
        'mobile_tinderbox_tree': 'Mozilla-Beta',
    },
    'mozilla-aurora': {
        'packaged_unittest_tinderbox_tree': 'Mozilla-Aurora',
        'tinderbox_tree': 'Mozilla-Aurora',
        'mobile_tinderbox_tree': 'Mozilla-Aurora',
    },
    'places': {
        'tinderbox_tree': 'Places',
        'mobile_tinderbox_tree': 'Places',
        'packaged_unittest_tinderbox_tree': 'Places',
    },
    'electrolysis': {
        'tinderbox_tree': 'Electrolysis',
        'mobile_tinderbox_tree': 'Electrolysis',
        'packaged_unittest_tinderbox_tree': 'Electrolysis',
    },
    'addonsmgr': {
        'tinderbox_tree': 'AddonsMgr',
        'mobile_tinderbox_tree': 'AddonsMgr',
        'packaged_unittest_tinderbox_tree': 'AddonsMgr',
    },
    'jaegermonkey': {
        'tinderbox_tree': 'Jaegermonkey',
        'mobile_tinderbox_tree': 'Jaegermonkey',
        'packaged_unittest_tinderbox_tree': 'Jaegermonkey',
    },
    'try': {
        'tinderbox_tree': 'Try',
        'mobile_tinderbox_tree': 'Try',
        'packaged_unittest_tinderbox_tree': 'Try',
        'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'mobile_download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'build.mozilla.org',
                    'CVS_RSH': 'ssh',
                    'MOZ_OBJDIR': 'obj-firefox',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                }
            }
        }
    },
}

PLATFORM_VARS = {
    'macosx': {
        'talos_masters': GLOBAL_VARS['talos_masters'] + [('talos-master.mozilla.org:9010', True, 5)]
    }
}

PROJECTS = {
    'fuzzing': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'fuzzing_repo': 'ssh://ffxbld@hg.mozilla.org/private/fuzzing',
        'fuzzing_remote_host': 'ffxbld@dm-pvtbuild01.mozilla.org',
        # Path needs extra leading slash due to optparse expansion on Win32
        'fuzzing_base_dir': '//mnt/pvt_builds/fuzzing/',
        'idle_slaves': 3,
        'disable_tinderbox_mail': False,
    },
    'nanojit': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 3,
        'tinderbox_tree': 'Nanojit',
        'disable_tinderbox_mail': False,
    },
    'spidermonkey_mozilla-inbound': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Mozilla-Inbound',
        'disable_tinderbox_mail': False,
    },
    'spidermonkey_ionmonkey': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Ionmonkey',
    },
}
