from copy import deepcopy

import defaults
reload(defaults)
from defaults import default_n900

base_dep_location = 'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox_builds/'
base_nightly_location = 'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/'

def generate_platform(base_platform, build_branch, nightly_unit, nightly_talos, dep_unit, dep_talos):
    new_platform = deepcopy(base_platform)
    if dep_talos:
        new_platform['talos_build_dir'] = base_dep_location + build_branch
    if dep_unit:
        new_platform['unit_build_dir'] = base_dep_location + build_branch
    if nightly_talos:
        new_platform['talos_build_dir'] = "%slatest-%s" % (base_nightly_location,build_branch)
    if nightly_unit:
        new_platform['unit_build_dir'] = "%slatest-%s" % (base_nightly_location,build_branch)
    return new_platform


SLAVES = {
    'n900': ['n900-%03i' % x for x in range(1,51)],
}

default_n900['slaves'] = SLAVES['n900']

MASTER = {'name': 'staging-mobile-master',
          'slave_port': 9020,
          'http_port': 8020,
          'admin_emails': [],
}

BRANCHES = {
    'mozilla-central': {
        'talos_branch': 'mobile',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'platforms': {
            'n900-gtk': generate_platform(default_n900,
                build_branch='mobile-trunk-maemo5-gtk',
                nightly_unit=True, dep_unit=True,
                nightly_talos=True, dep_talos=True),
            'n900-qt': generate_platform(default_n900,
                build_branch='mobile-trunk-maemo5-qt',
                nightly_unit=True, dep_unit=False,
                nightly_talos=True, dep_talos=False),
        },
    },
    'mozilla-1.9.2': {
        'talos_branch': 'mobile-1.9.2',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'platforms': {
            'n900-gtk': generate_platform(default_n900,
                build_branch='mobile-1.9.2-maemo5-gtk',
                nightly_unit=True, dep_unit=True,
                nightly_talos=True, dep_talos=True),
        },
    },
    'tracemonkey': {
        'talos_branch': 'mobile-tracemonkey',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'platforms': {
            'n900-gtk': generate_platform(default_n900,
                build_branch='mobile-tracemonkey-maemo5-gtk',
                nightly_unit=True, dep_unit=False,
                nightly_talos=True, dep_talos=True),
            'n900-qt': generate_platform(default_n900,
                build_branch='mobile-tracemonkey-maemo5-qt',
                nightly_unit=False, dep_unit=False,
                nightly_talos=True, dep_talos=False),
        },
    },
    'electrolysis': {
        'talos_branch': 'mobile-electrolysis',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'platforms': {
            'n900-gtk': generate_platform(default_n900,
                build_branch='mobile-electrolysis-maemo5-gtk',
                nightly_unit=True, dep_unit=False,
                nightly_talos=True, dep_talos=False),
            'n900-qt': generate_platform(default_n900,
                build_branch='mobile-electrolysis-maemo5-qt',
                nightly_unit=True, dep_unit=False,
                nightly_talos=True, dep_talos=False),
        },
    },
}
