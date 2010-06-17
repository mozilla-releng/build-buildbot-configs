MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in range(1,51)]
MAC_MINIS      = ['moz2-darwin9-slave%02i' % x for x in range(1,69)]
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
    'macosx-snow': MAC_SNOW_MINIS,
}

TRY_SLAVES = SLAVES

GLOBAL_VARS = {
    'config_subdir': 'mozilla2-staging',
    'stage_server': 'staging-stage.build.mozilla.org',
    'aus2_host': 'staging-stage.build.mozilla.org',
    'download_base_url': 'http://staging-stage.build.mozilla.org/pub/mozilla.org/firefox',
    'graph_server': 'graphs-stage.mozilla.org',
    'build_tools_repo_path': 'users/stage-ffxbld/tools',
    'base_clobber_url': 'http://build.mozilla.org/stage-clobberer/index.php',
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning
    'talos_masters': [
        ('talos-staging-master02.build.mozilla.org:9010', False),
        ('talos-staging-master02.build.mozilla.org:9012', False),
    ],
    # List of unittest masters to notify of new builds to test,
    # and if a failure to notify the master should result in a warning
    'unittest_masters': [
        ('localhost:9009', True, 0),
        ('talos-staging-master02.build.mozilla.org:9010', True, 0),
        ('talos-staging-master02.build.mozilla.org:9012', True, 0),
        ],
    'xulrunner_tinderbox_tree': 'MozillaTest',
    'weekly_tinderbox_tree': 'MozillaTest',
    'l10n_tinderbox_tree': 'MozillaStaging',
    'packaged_unittest_tinderbox_tree': 'MozillaTest',
    'tinderbox_tree': 'MozillaTest',
}

BUILDS_BEFORE_REBOOT = 5
SYMBOL_SERVER_HOST = 'staging-stage.build.mozilla.org'

# Local branch overrides
BRANCHES = {
    'tryserver': {
        'download_base_url': 'http://staging-stage.build.mozilla.org/pub/mozilla.org/firefox',
        'enable_mail_notifier': False,
        'package_url': 'http://staging-stage.build.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
    }
}

PLATFORM_VARS = {
}
