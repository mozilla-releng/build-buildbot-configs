SLAVES = {
    'fedora': ["talos-r3-fed-%03i" % x for x in range(1,4)],
    'fedora64' : ["talos-r3-fed64-%03i" % x for x in range (1,4)],
    'xp': ["talos-r3-xp-%03i" % x for x in range(1,4)],
    'win7': ["talos-r3-w7-%03i" % x for x in range(1,4)],
    'w764': ["t-r3-w764-%03i" % x for x in range(1,4)],
    'leopard': ["talos-r3-leopard-%03i" % x for x in range(1,4)],
    'snowleopard': ["talos-r3-snow-%03i" % x for x in range(1,4)],
}

GRAPH_CONFIG = ['--resultsServer', 'graphs-stage.mozilla.org',
    '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'tinderbox_tree': 'MozillaTest',
    'build_tools_repo_path': 'users/stage-ffxbld/tools',
}

BRANCHES = {
        'tryserver': {
            # Disable this on staging so people don't get notified of staging tests
            'enable_mail_notifier': False,
            'package_url': 'http://staging-stage.build.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
            'package_dir': '%(who)s-%(got_revision)s',
        },
}

PLATFORM_VARS = {
}
