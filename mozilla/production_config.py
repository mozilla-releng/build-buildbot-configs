MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in range(1,51)]
MAC_MINIS      = ['moz2-darwin9-slave%02i' % x for x in [2,5,6,7] + range(9,27) + range(29,68)]
XSERVES        = ['bm-xserve%02i' % x for x in [6,7,9,11,12,16,17,18,19,21,22]]
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
        ('talos-staging-master02.build.mozilla.org:9010', False),
        ('talos-staging-master02.build.mozilla.org:9012', False),
    ],
    # List of unittest masters to notify of new builds to test,
    # and if a failure to notify the master should result in a warning
    'unittest_masters': [
        ('production-master01.build.mozilla.org:9009', False, 0),
        ('talos-master02.build.mozilla.org:9012', False, 0),
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
    },
    'mozilla-1.9.1': {
        'packaged_unittest_tinderbox_tree': 'Firefox3.5',
        'tinderbox_tree': 'Firefox3.5',
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'Firefox3.6',
        'packaged_unittest_tinderbox_tree': 'Firefox3.6',
    },
    'tracemonkey': {
        'tinderbox_tree': 'TraceMonkey',
        'packaged_unittest_tinderbox_tree': 'TraceMonkey',
    },
    'places': {
        'tinderbox_tree': 'Places',
        'packaged_unittest_tinderbox_tree': 'Places',
    },
    'electrolysis': {
        'tinderbox_tree': 'Electrolysis',
        'packaged_unittest_tinderbox_tree': 'Electrolysis',
    },
    'addonsmgr': {
        'tinderbox_tree': 'AddonsMgr',
        'packaged_unittest_tinderbox_tree': 'AddonsMgr',
    },
}

PLATFORM_VARS = {
}
