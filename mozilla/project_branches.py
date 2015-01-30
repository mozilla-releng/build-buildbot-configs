PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    # 'build-system': {},  # Bug 1010674
    'fx-team': {
        'merge_builds': False,
        'enable_perproduct_builds': True,
        'repo_path': 'integration/fx-team',
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': False,
        'pgo_strategy': 'periodic',
        'periodic_start_hours': range(2, 24, 3),
        'enable_weekly_bundle': True,
    },
    'mozilla-inbound': {
        'merge_builds': False,
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'enable_weekly_bundle': True,
        'pgo_strategy': 'periodic',
        'periodic_start_hours': range(1, 24, 3),
        'talos_suites': {
            'xperf': 1,
        },
        'branch_projects': ['spidermonkey_tier_1', 'spidermonkey_info'],
    },
    'b2g-inbound': {
        'merge_builds': False,
        'repo_path': 'integration/b2g-inbound',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'pgo_strategy': 'periodic',
        'periodic_start_hours': range(2, 24, 3),
        'enable_weekly_bundle': True,
        'talos_suites': {
            'xperf': 1,
        },
        'platforms': {
            'win32': {
                'enable_checktests': False,
                'slave_platforms': ['win7-ix'],
                'talos_slave_platforms': ['win7-ix'],
            },
            'win32-debug': {
                'enable_checktests': False,
                'slave_platforms': ['win7-ix'],
            },
            'macosx64': {
                'enable_checktests': False,
                'slave_platforms': ['snowleopard'],
                'talos_slave_platforms': ['snowleopard'],
            },
            'macosx64-debug': {
                'enable_checktests': False,
                'slave_platforms': ['snowleopard'],
            },
        },
    },
    #'services-central': {},  # Bug 1010674
    'ux': {
        'branch_name': 'UX',
        'mobile_branch_name': 'UX',
        'build_branch': 'UX',
        'tinderbox_tree': 'UX',
        'mobile_tinderbox_tree': 'UX',
        'packaged_unittest_tinderbox_tree': 'UX',
        'enabled_products': ['firefox'],
        'enable_weekly_bundle': True,
        'mozconfig_dir': 'ux',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'enable_talos': False,
        'lock_platforms': True,
        'platforms': {
            'macosx64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win64': {
                'nightly_signing_servers': 'nightly-signing',
            },
        },
    },
    # no desktop builds for bug 1100150
    # 'alder': {},
    'ash': {
        'enable_perproduct_builds': False,
    },
    #'birch': {},  # Bug 1010674
    'cedar': {
        'enable_perproduct_builds': False,
        'mozharness_tag': 'default',
        'enable_talos': True,
        'talos_suites': {
            'xperf': 1,
        },
        'enable_opt_unittests': True,
        'mobile_platforms': {
            'android-x86': {
                'enable_opt_unittests': True,
            },
        },
    },
    'cypress': {
        'enable_perproduct_builds': False,
        'enable_talos': True,
    },
    'date': {
        'gecko_version': 36,
        'mozharness_repo_path': 'users/nthomas_mozilla.com/mozharness-build-promotion',
        'mozharness_repo': 'https://hg.mozilla.org/users/nthomas_mozilla.com/mozharness-build-promotion',
        'mozharness_tag': 'default',
        'desktop_mozharness_builds_enabled': True,
        'use_mozharness_repo_cache': False,
        'branch_projects': [],
        'enable_talos': True,
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux64': {},
            'win32': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'linux64-asan': {},
            'linux64-asan-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
        },
        'enable_valgrind': False,
        'pgo_strategy': 'per-checkin',
    },
    'elm': {
        'branch_projects': [],
        'enable_talos': True,
        'enable_valgrind': False,
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux64': {},
            'linux-debug': {},
            'linux64-debug': {},
        },
    },
    'fig': {},
    'gum': {
        'gecko_version': 35,
        'enable_perproduct_builds': False,
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'nightly_signing_servers': 'nightly-signing',
        'l10n_repo_path': 'releases/l10n/mozilla-aurora',
        'pgo_strategy': 'per-checkin',
        'enable_mac_a11y': True,
        'enable_l10n': True,
        'enable_l10n_onchange': False,
        'enUS_binaryURL': '/nightly/latest-gum',
        'l10nNightlyUpdate': True,
        'l10nDatedDirs': True,
        'l10n_tree': 'fxrel',
        'l10n_platforms': ['linux', 'linux64', 'win32', 'macosx64'],
        # explicitly set the server to avoid using variables
        'localesURL': 'http://hg.mozilla.org/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-aurora',
        'enable_multi_locale': True,
        'upload_mobile_symbols': True,
        'enable_valgrind': False,
        'enabled_products': ['firefox'],
    },
    'holly': {
        'branch_projects': [],
        'pgo_strategy': None,
        'lock_platforms': True,
        'enable_nightly': False,
        'platforms': {
            'linux': {},
            'linux64': {},
            'win32': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-asan': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
        },
        'enable_talos': True,
    },
    'jamun': {},
    'larch': {
        'lock_platforms': True,
        'platforms': {
            'android-api-9': {},
            'android-api-11': {},
            'android-api-9-debug': {},
            'android-api-11-debug': {},
            'android-x86': {},
            'android-debug': {},
        },
    },
    'maple': {
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'nightly_signing_servers': 'nightly-signing',
    },
    # customizations for integration work for bugs 481815 and 307181
    'oak': {
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'enable_talos': False,
        'platforms': {
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'macosx64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win64': {
                'nightly_signing_servers': 'nightly-signing',
            },
        },
    },
    # Not needed whilst booked for bug 929203.
    #'pine': {}
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = PROJECT_BRANCHES[branch].get('tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('mobile_tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['packaged_unittest_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('packaged_unittest_tinderbox_tree', branch.title())
