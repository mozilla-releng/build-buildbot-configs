MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in range(1,51)]
MAC_MINIS      = ['moz2-darwin9-slave%02i' % x for x in [2,5,6,7] + range(9,27) + range(29,68)]
XSERVES        = ['bm-xserve%02i' % x for x in [6,7,9,11,12,15,16,17,18,19,21,22]]
LINUX_VMS      = ['moz2-linux-slave%02i' % x for x in [1,2] + range(5,17) + range(18,51)]
LINUX64_VMS    = ['moz2-linux64-slave%02i' % x for x in range(1,7) + range(8,13)]
LINUX_IXS      = ['mv-moz2-linux-ix-slave%02i' % x for x in range(2,25)]
WIN32_VMS      = ['win32-slave%02i' % x for x in [1,2] + range(5,21) + range(22,60)]
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in range(2,26)]
SLAVES = {
    'linux':       LINUX_VMS + LINUX_IXS,
    'linux64':     LINUX64_VMS,
    'win32':       WIN32_VMS + WIN32_IXS,
    'macosx':      MAC_MINIS + XSERVES,
    'macosx-snow': MAC_SNOW_MINIS,
}

TRY_LINUX      = ['try-linux-slave%02i' % x for x in range (1,26)]
TRY_LINUX64    = ['try-linux64-slave%02i' % x for x in range (1,6)]
TRY_MAC        = ['try-mac-slave%02i' % x for x in range (1,40)]
TRY_MAC64      = ['try-mac64-slave%02i' % x for x in range (1,11)]
TRY_WIN32      = ['try-w32-slave%02i' % x for x in range (1,32)]
TRY_SLAVES = {
    'linux':       TRY_LINUX,
    'linux64':     TRY_LINUX64,
    'win32':       TRY_WIN32,
    'macosx':      TRY_MAC,
    'macosx-snow': TRY_MAC64,
}


# Local overrides for default values
GLOBAL_VARS = {
    'config_subdir': 'mozilla2',
    'stage_server': 'stage.mozilla.org',
    'aus2_host': 'aus2-staging.mozilla.org',
    'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox',
    'graph_server': 'graphs.mozilla.org',
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://build.mozilla.org/clobberer/index.php',
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning
    'talos_masters': [
        ('talos-master.mozilla.org:9010', True),
        ('talos-master02.build.mozilla.org:9012', True),
        ('test-master01.build.mozilla.org:9012', True),
        ('talos-staging-master02.build.mozilla.org:9010', False),
        ('talos-staging-master02.build.mozilla.org:9012', False),
    ],
    # List of unittest masters to notify of new builds to test,
    # and if a failure to notify the master should result in a warning
    'unittest_masters': [
        ('production-master01.build.mozilla.org:9009', False, 0),
        ('talos-master02.build.mozilla.org:9012', False, 0),
        ('test-master01.build.mozilla.org:9012', False, 0),
        ('talos-staging-master02.build.mozilla.org:9010', False, 0),
        ('talos-staging-master02.build.mozilla.org:9012', False, 0),
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
    'mozilla-1.9.1': {
        'packaged_unittest_tinderbox_tree': 'Firefox3.5',
        'tinderbox_tree': 'Firefox3.5',
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'Firefox3.6',
        'packaged_unittest_tinderbox_tree': 'Firefox3.6',
        'mobile_tinderbox_tree': 'Mobile1.1',
    },
    'mozilla-2.0': {
        'tinderbox_tree': 'Firefox4.0',
        'packaged_unittest_tinderbox_tree': 'Firefox4.0',
    },
    'tracemonkey': {
        'tinderbox_tree': 'TraceMonkey',
        'mobile_tinderbox_tree': 'TraceMonkey',
        'packaged_unittest_tinderbox_tree': 'TraceMonkey',
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
    'tryserver': {
        'tinderbox_tree': 'MozillaTry',
        'mobile_tinderbox_tree': 'MozillaTry',
        'packaged_unittest_tinderbox_tree': 'MozillaTry',
        'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
        'enable_mail_notifier': True,
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
        'unittest_masters': [('test-master01.build.mozilla.org:9012', True, 0),
            ('talos-staging-master02.build.mozilla.org:9012', True, 0),
            ('production-master01.build.mozilla.org:9009', True, 0)],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'build.mozilla.org',
                    'CVS_RSH': 'ssh',
                    'MOZ_OBJDIR': 'obj-firefox',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
                },
            },
        }
    },
   'maple': {
        'tinderbox_tree': 'Maple',
        'mobile_tinderbox_tree': 'Maple',
        'packaged_unittest_tinderbox_tree': 'Maple',
    },
    'cedar': {
        'tinderbox_tree': 'Cedar',
        'mobile_tinderbox_tree': 'Cedar',
        'packaged_unittest_tinderbox_tree': 'Cedar',
    },
    'birch': {
        'tinderbox_tree': 'Birch',
        'mobile_tinderbox_tree': 'Birch',
        'packaged_unittest_tinderbox_tree': 'Birch',
    },

}

PLATFORM_VARS = {
}
