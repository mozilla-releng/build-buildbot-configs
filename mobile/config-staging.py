from copy import deepcopy

import defaults
reload(defaults)
from defaults import default_n900, default_n810

base_dep_location = 'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds'
base_nightly_location = 'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly'

def generate_platform(base_platform, build_branch, talos_branch,
                      nightly_multi=False, nightly_unit=False,
                      nightly_talos=False, dep_unit=False, dep_talos=False):
    new_platform = deepcopy(base_platform)
    nightly_location = "%s/latest-%s/" % (base_nightly_location, build_branch)
    if nightly_multi:
        nightly_location += "en-US/"
    if dep_talos:
        new_platform['talos_build_dirs'].append('%s/%s/' % (base_dep_location, build_branch))
    if dep_unit:
        new_platform['unit_build_dirs'].append('%s/%s/' % (base_dep_location, build_branch))
    if nightly_talos:
        new_platform['talos_build_dirs'].append(nightly_location)
    if nightly_unit:
        new_platform['unit_build_dirs'].append(nightly_location)
    new_platform['talos_branch'] = talos_branch
    return new_platform


SLAVES = {
    'n900': ['n900-%03i' % x for x in range(1,91)],
    'n810': ['maemo-n810-%02i' % x for x in range(1,81)],
}

default_n900['slaves'] = SLAVES['n900']
default_n810['slaves'] = SLAVES['n810']
default_n900['talos_tarball'] = 'http://10.250.48.136/maemo5/talos.tar.bz2'
default_n900['pageloader_tarball'] = 'http://10.250.48.136/maemo5/pageloader.tar.bz2'
default_n900['maemkit_tarball'] = 'http://10.250.48.136/maemo5/maemkit.tar.bz2'
default_n900['tp4_tarball'] = 'http://10.250.48.136/maemo5/tp4.tar.bz2'
default_n810['talos_tarball'] = 'http://10.250.48.136/maemo/talos.tar.bz2'
default_n810['pageloader_tarball'] = 'http://10.250.48.136/maemo/pageloader.tar.bz2'
default_n810['maemkit_tarball'] = 'http://10.250.48.136/maemo/maemkit.tar.bz2'
default_n810['tp4_tarball'] = 'http://10.250.48.136/maemo/tp4.tar.bz2'

MASTER = {'name': 'staging-mobile-master',
          'slave_port': 9020,
          'http_port': 8020,
          'admin_emails': [],
}

BRANCHES = {
    'mozilla-central': {
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'platforms': {
            'n900-gtk': generate_platform(default_n900,
                build_branch='mozilla-central-maemo5-gtk',
                talos_branch='mobile',
                nightly_multi=True,
                nightly_unit=True, dep_unit=True,
                nightly_talos=True, dep_talos=True),
            'n900-qt': generate_platform(default_n900,
                build_branch='mozilla-central-maemo5-qt',
                talos_branch='mobile-qt',
                nightly_multi=True,
                nightly_unit=True, dep_unit=False,
                nightly_talos=True, dep_talos=False),
        },
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'platforms': {
            'n900-gtk': generate_platform(default_n900,
                build_branch='mozilla-1.9.2-maemo5-gtk',
                talos_branch='mobile-1.9.2',
                nightly_multi=True,
                nightly_unit=True, dep_unit=True,
                nightly_talos=True, dep_talos=True),
            'n810': generate_platform(default_n810,
                build_branch='mozilla-1.9.2-maemo4',
                talos_branch='mobile-1.9.2',
                nightly_multi=True,
                nightly_unit=True, dep_unit=True,
                nightly_talos=True, dep_talos=True),
        },
    },
    'tracemonkey': {
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'platforms': {
            'n900-gtk': generate_platform(default_n900,
                build_branch='tracemonkey-maemo5-gtk',
                talos_branch='mobile-tracemonkey',
                nightly_unit=True, dep_unit=False,
                nightly_talos=True, dep_talos=True),
            'n900-qt': generate_platform(default_n900,
                build_branch='tracemonkey-maemo5-qt',
                talos_branch='mobile-tracemonkey-qt',
                nightly_unit=False, dep_unit=False,
                nightly_talos=True, dep_talos=False),
        },
    },
    'electrolysis': {
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'platforms': {
            'n900-gtk': generate_platform(default_n900,
                build_branch='electrolysis-maemo5-gtk',
                talos_branch='mobile-electrolysis',
                nightly_unit=True, dep_unit=False,
                nightly_talos=True, dep_talos=False),
            'n900-qt': generate_platform(default_n900,
                build_branch='electrolysis-maemo5-qt',
                talos_branch='mobile-electrolysis-qt',
                nightly_unit=True, dep_unit=False,
                nightly_talos=True, dep_talos=False),
        },
    },
}
