SLAVES = {
    'fedora': dict([("talos-r3-fed-%03i" % x, {}) for x in range(1,64)]),
    'fedora64' : dict([("talos-r3-fed64-%03i" % x, {}) for x in range (1,64)]),
    'xp': dict([("talos-r3-xp-%03i" % x, {}) for x in range(1,63)]),
    'win7': dict([("talos-r3-w7-%03i" % x, {}) for x in range(1,65)]),
    'w764': dict([("t-r3-w764-%03i" % x, {}) for x in range(1,6)]),
    'leopard': dict([("talos-r3-leopard-%03i" % x, {}) for x in range(1,60)]),
    'snowleopard': dict([("talos-r3-snow-%03i" % x, {}) for x in range(1,60)]),
    'snowleopard-r4': dict([("talos-r4-snow-%03i" % x, {}) for x in range(1,160)]),
    'tegra_android': dict([('tegra-%03i' % x, {'http_port': '30%03i' % x, 'ssl_port': '31%03i' % x}) for x in range(1,154)]),
}

SLAVES['leopard-o'] = SLAVES['leopard']

TRY_SLAVES = {}

GRAPH_CONFIG = ['--resultsServer', 'graphs-stage.mozilla.org',
    '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'disable_tinderbox_mail': True,
    'tinderbox_tree': 'MozillaTest',
    'mobile_tinderbox_tree': 'MobileTest',
    'build_tools_repo_path': 'users/prepr-ffxbld/tools',
    'stage_server': 'preproduction-stage.build.mozilla.org',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_dsa',
}

BRANCHES = {
        'try': {
            'enable_mail_notifier': False, # Set to True when testing
            'email_override': [], # Set to your address when testing
            'package_url': 'http://preproduction-stage.build.mozilla.org/pub/mozilla.org/firefox/try-builds',
            'package_dir': '%(who)s-%(got_revision)s',
            'stage_username': 'trybld',
            'stage_ssh_key': 'trybld_dsa',
        },
}

PLATFORM_VARS = {
}

PROJECTS = {
    'jetpack': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'tinderbox_tree': 'Releng-Preproduction',
    },
}
