SLAVES = {
    'fedora': ["talos-r3-fed-%03i" % x for x in range(1,54)],
    'fedora64' : ["talos-r3-fed64-%03i" % x for x in range (1,56)],
    'xp': ["talos-r3-xp-%03i" % x for x in range(1,54)],
    'win7': ["talos-r3-w7-%03i" % x for x in range(1,40) + range(41,54)],
    'w764': ["t-r3-w764-%03i" % x for x in range(1,51)],
    'leopard': ["talos-r3-leopard-%03i" % x for x in range(1,54)],
    'snowleopard': ["talos-r3-snow-%03i" % x for x in range(1,56)],
    'tegra_android': ['tegra-%03i' % x for x in range(1,15)],
}

GRAPH_CONFIG = ['--resultsServer', 'graphs-stage.mozilla.org',
    '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'tinderbox_tree': 'MozillaTest',
    'mobile_tinderbox_tree': 'MobileTest',
    'build_tools_repo_path': 'users/prepr-ffxbld/tools',
    'stage_server': 'preproduction-stage.build.mozilla.org',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_dsa',
}

BRANCHES = {
        'tryserver': {
            'enable_mail_notifier': False, # Set to True when testing
            'email_override': [], # Set to your address when testing
            'package_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
            'package_dir': '%(who)s-%(got_revision)s',
            'stage_username': 'trybld',
            'stage_ssh_key': 'trybld_dsa',
        },
}

PLATFORM_VARS = {
}
