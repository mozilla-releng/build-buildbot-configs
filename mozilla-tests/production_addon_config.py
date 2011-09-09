SLAVES = {
    'fedora': dict([("addon-r3-fed-%03i" % x, {}) for x in range(1,4)]),
    'fedora64' : dict([("addon-r3-fed64-%03i" % x, {}) for x in range (1,4)]),
    'xp': dict([("addon-r3-xp-%03i" % x, {}) for x in range(1,4)]),
    'win7': dict([("addon-r3-w7-%03i" % x, {}) for x in range(1,4)]),
    'w764': dict([("addon-r3-w764-%03i" % x, {}) for x in range(1,4)]),
    'leopard': dict([("addon-r3-leopard-%03i" % x, {}) for x in range(1,4)]),
    'snowleopard': dict([("addon-r3-snow-%03i" % x, {}) for x in range(1,4)]),
    'tegra_android': dict([('tegra-%03i' % x, {'http_port': '30%03i' % x, 'ssl_port': '31%03i' % x}) for x in range(1,4)]),
}

TRY_SLAVES = {}

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org',
    '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'build_tools_repo_path': 'build/tools',
    'stage_server': 'stage.mozilla.org',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_dsa',
}

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'tinderbox_tree': 'Firefox',
        'mobile_tinderbox_tree': 'Firefox',
    },
    'shadow-central': {
        'tinderbox_tree': 'Shadow-Central',
        'mobile_tinderbox_tree': 'Shadow-Central',
        'stage_server': 'dm-pvtbuild01.mozilla.org',
    },
    'mozilla-release': {
        'tinderbox_tree': 'Mozilla-Release',
        'mobile_tinderbox_tree': 'Mozilla-Release',
    },
    'mozilla-beta': {
        'tinderbox_tree': 'Mozilla-Beta',
        'mobile_tinderbox_tree': 'Mozilla-Beta',
    },
    'mozilla-aurora': {
        'tinderbox_tree': 'Mozilla-Aurora',
        'mobile_tinderbox_tree': 'Mozilla-Aurora',
    },
    'mozilla-1.9.1': {
        'tinderbox_tree': 'Firefox3.5',
        'mobile_tinderbox_tree': 'Firefox3.5',
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'Firefox3.6',
        'mobile_tinderbox_tree': 'Mobile1.1',
    },
    'places': {
        'tinderbox_tree': 'Places',
        'mobile_tinderbox_tree': 'Places',
    },
    'electrolysis': {
        'tinderbox_tree': 'Electrolysis',
        'mobile_tinderbox_tree': 'Electrolysis',
    },
    'addontester': {
        'tinderbox_tree': 'AddonTester',
        'mobile_tinderbox_tree': 'AddonTester',
    },
    'addonbaselinetester': {
        'tinderbox_tree': 'AddonTester',
        'mobile_tinderbox_tree': 'AddonTester',
    },
    'try': {
        'tinderbox_tree': 'Try',
        'mobile_tinderbox_tree': 'Try',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'enable_merging': False,
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'package_dir': '%(who)s-%(got_revision)s',
        'stage_username': 'trybld',
        'stage_ssh_key': 'trybld_dsa',
    },
    'jaegermonkey': {
        'tinderbox_tree': 'Jaegermonkey',
        'mobile_tinderbox_tree': 'Jaegermonkey',
    },
}

PLATFORM_VARS = {
}

PROJECTS = {
    'jetpack': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'tinderbox_tree': 'Jetpack',
    },
}
