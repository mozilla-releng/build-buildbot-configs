PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    # 'build-system': {},  # Bug 1010674
    'fx-team': {
        'enable_perproduct_builds': True,
        'repo_path': 'integration/fx-team',
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': False,
        'pgo_strategy': 'periodic',
        'periodic_start_hours': range(2, 24, 3),
        'enable_weekly_bundle': True,
    },
    'mozilla-inbound': {
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
    'alder': {
        # Per bug 1083853, this disable mozharness mach and other
        # mozilla-central oriented features
        'gecko_version': 33,
        # Make every checkin trigger builds, remove after 33.1 (or sooner)
        'enable_perproduct_builds': False,
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'nightly_signing_servers': 'nightly-signing',
        'l10n_repo_path': 'releases/l10n/mozilla-release',
        'pgo_strategy': 'per-checkin',
        'enable_mac_a11y': True,
        'enable_l10n': True,
        'enable_l10n_onchange': True,
        'enUS_binaryURL': '/nightly/latest-alder',
        'l10nNightlyUpdate': True,
        'l10n_tree': 'fxrel',
        'l10n_platforms': ['linux', 'linux64', 'win32', 'macosx64'],
        # explicitly set the server to avoid using variables
        'localesURL': 'http://hg.mozilla.org/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.alder',
        'enable_multi_locale': True,
        'upload_mobile_symbols': True,
        'enable_valgrind': False,
        'enabled_products': ['firefox'],
        'lock_platforms': True,
        'platforms': {
            'macosx64': {
                'test_pretty_names': True,
            },
            'linux': {
                'test_pretty_names': True,
            },
            'linux64': {
                'test_pretty_names': True,
            },
            'win32': {
                'test_pretty_names': True,
            },
            'win64': {},
            'linux-debug': {},
            'linux64-br-haz': {},
            'linux64-debug': {},
            'linux64-asan': {},
            'linux64-asan-debug': {},
            'linux64-st-an-debug': {},
            'linux64-cc': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'win64-debug': {},
        },
    },
    'ash': {
        'enable_perproduct_builds': False,
        'desktop_mozharness_repacks_enabled': True,
        'enable_nightly': True,
        'mozharness_repo_path': 'build/ash-mozharness',
        'mozharness_repo': 'https://hg.mozilla.org/build/ash-mozharness',
        'mozharness_tag': 'default',
        'lock_platforms': True,
        'talos_suites': {
            'xperf': 1,
        },
        'platforms': {
            'linux': {},
            'linux64': {},
            'win32': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'linux64-br-haz': {},
            'linux64-sh-haz': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
        },
        'mobile_platforms': {
            'android': {
                'slave_platforms': ['panda_android', 'ubuntu64_vm_large'],
            },
            'android-x86': {
                'enable_opt_unittests': True,
            },
        },
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
        'mozharness_tag': 'default',
        'enable_talos': True,
    },
    'date': {
        'lock_platforms': True,
        'platforms': {
            'win32': {
                'enable_opt_unittests': True,
            },
            'win64': {
                'enable_opt_unittests': True,
            },
            'win64-debug': {
                'enable_debug_unittests': True,
            },
        },
        'enable_merging': False,
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
    'gum': {},
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
            'android': {},
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
