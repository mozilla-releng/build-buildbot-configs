SLAVES = {
    'fedora': ["talos-r3-fed-%03i" % x for x in range(3,10) + range(11,54)],
    'fedora64' : ["talos-r3-fed64-%03i" % x for x in range (3,10) + range(11,56)],
    'xp': ["talos-r3-xp-%03i" % x for x in range(4,10) + range(11,54)],
    'win7': ["talos-r3-w7-%03i" % x for x in range(4,10) + range(11,40) + range(41,54)],
    'w764': ["t-r3-w764-%03i" % x for x in range(3,10) + range(11,51)],
    'leopard': ["talos-r3-leopard-%03i" % x for x in range(3,10) + range(11,54)],
    'snowleopard': ["talos-r3-snow-%03i" % x for x in range(3,10) + range(11,56)],
    'tegra_android': ['tegra-%03i' % x for x in range(1,15)],
}

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
        'mobile_tinderbox_tree': 'Mobile',
    },
    'shadow-central': {
        'tinderbox_tree': 'Shadow-Central',
        'mobile_tinderbox_tree': 'Shadow-Central',
    },
    'mozilla-2.0': {
        'tinderbox_tree': 'Firefox4.0',
        'mobile_tinderbox_tree': 'Mobile4.0',
    },
    'mozilla-1.9.1': {
        'tinderbox_tree': 'Firefox3.5',
        'mobile_tinderbox_tree': 'Firefox3.5',
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'Firefox3.6',
        'mobile_tinderbox_tree': 'Mobile1.1',
    },
    'tracemonkey': {
        'tinderbox_tree': 'TraceMonkey',
        'mobile_tinderbox_tree': 'TraceMonkey',
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
        'tinderbox_tree': 'Firefox3.6',
        'mobile_tinderbox_tree': 'Firefox3.6',
    },
    'tryserver': {
        'tinderbox_tree': 'MozillaTry',
        'mobile_tinderbox_tree': 'MozillaTry',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'enable_merging': False,
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
        'package_dir': '%(who)s-%(got_revision)s',
        'stage_username': 'trybld',
        'stage_ssh_key': 'trybld_dsa',
    },
    'birch': {
        'tinderbox_tree': 'Birch',
        'mobile_tinderbox_tree': 'Birch',
    },
    'cedar': {
        'tinderbox_tree': 'Cedar',
        'mobile_tinderbox_tree': 'Cedar',
    },
    'maple': {
        'tinderbox_tree': 'Maple',
        'mobile_tinderbox_tree': 'Maple',
    },
    'jaegermonkey': {
        'tinderbox_tree': 'Jaegermonkey',
        'mobile_tinderbox_tree': 'Jaegermonkey',
    },

}

PLATFORM_VARS = {
}
