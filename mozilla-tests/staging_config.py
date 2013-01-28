from copy import deepcopy
import production_config as pc

STAGING_SLAVES = {
    'fedora': dict([("talos-r3-fed-%03i" % x, {}) for x in [1, 2, 10]]),
    'fedora64': dict([("talos-r3-fed64-%03i" % x, {}) for x in [1, 2, 10]]),
    'xp': dict([("talos-r3-xp-%03i" % x, {}) for x in [1, 2, 3, 10]]),
    'win7': dict([("talos-r3-w7-%03i" % x, {}) for x in [1, 2, 3, 10]]),
    'leopard': dict([("talos-r3-leopard-%03i" % x, {}) for x in [1, 2, 10]]),
    'snowleopard': dict([("talos-r4-snow-%03i" % x, {}) for x in [1, 2, 3, 10]]),
    'lion': dict([("talos-r4-lion-%03i" % x, {}) for x in [1, 2, 3, 10]]),
    'mountainlion': dict([("talos-mtnlion-r5-%03i" % x, {}) for x in [1, 2, 3, 10]]),
    'tegra_android': dict(
        [('tegra-%03i' % x, {'http_port': '30%03i' % x, 'ssl_port': '31%03i' % x}) for x in range(10,30)]
    ),
    'panda_android': dict(),
    'b2g_panda': dict(),
    'ubuntu32': dict(),
    'ubuntu64': dict(),
}

STAGING_SLAVES['leopard-o'] = STAGING_SLAVES['leopard']
STAGING_SLAVES['tegra_android-armv6'] = STAGING_SLAVES['tegra_android']
STAGING_SLAVES['tegra_android-noion'] = STAGING_SLAVES['tegra_android']
STAGING_SLAVES['fedora-b2g'] = STAGING_SLAVES['fedora']

SLAVES = deepcopy(STAGING_SLAVES)

for p, slaves in pc.SLAVES.items() + pc.TRY_SLAVES.items():
    if p not in SLAVES:
        SLAVES[p] = deepcopy(slaves)
    else:
        SLAVES[p] = dict(SLAVES[p].items() + slaves.items())

TRY_SLAVES = deepcopy(SLAVES)

GRAPH_CONFIG = ['--resultsServer', 'graphs.allizom.org',
    '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'disable_tinderbox_mail': True,
    'tinderbox_tree': 'MozillaTest',
    'mobile_tinderbox_tree': 'MobileTest',
    'build_tools_repo_path': 'build/tools',
    'mozharness_repo': 'http://hg.mozilla.org/build/mozharness',
    'mozharness_tag': 'production',
    'stage_server': 'dev-stage01.srv.releng.scl3.mozilla.com',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_dsa',
    'datazilla_url': 'https://datazilla.mozilla.org/test',
}

BRANCHES = {
        'try': {
            'enable_mail_notifier': False, # Set to True when testing
            'email_override': [], # Set to your address when testing
            'package_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox/try-builds',
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
        'tinderbox_tree': 'MozillaTest',
    },
}
