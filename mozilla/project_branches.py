PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    'build-system': {
        'pgo_strategy': 'periodic',
        'platforms': {
            'win32': {
                'pgo_platform': 'win64',
            },
        },
    },
    'fx-team': {
        'enable_perproduct_builds': True,
        'repo_path': 'integration/fx-team',
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': False,
        'pgo_strategy': 'periodic',
        'periodic_interval': 3,
        'enable_weekly_bundle': True,
    },
    'graphics': {
        'enable_talos': False,
    },
    'ionmonkey': {
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'pgo_strategy': 'periodic',
        'branch_projects': ['spidermonkey_tier_1', 'spidermonkey_info'],
    },
    'mozilla-inbound': {
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'enable_weekly_bundle': True,
        'pgo_strategy': 'periodic',
        'periodic_interval': 3,
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
        'periodic_interval': 3,
        'enable_weekly_bundle': True,
        'talos_suites': {
            'xperf': 1,
        },
        'platforms': {
            'win32': {
                'enable_checktests': False,
                'slave_platforms': ['win8'],
                'talos_slave_platforms': ['win8'],
            },
            'win32-debug': {
                'enable_checktests': False,
                'slave_platforms': ['win8'],
            },
            'macosx64': {
                'enable_checktests': False,
                'slave_platforms': ['mountainlion'],
                'talos_slave_platforms': ['mountainlion'],
            },
            'macosx64-debug': {
                'enable_checktests': False,
                'slave_platforms': ['mountainlion'],
            },
        },
    },
    'services-central': {
        'repo_path': 'services/services-central',
        'enable_weekly_bundle': True,
        'pgo_strategy': 'periodic',
    },
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
                'nightly_signing_servers': 'mac-nightly-signing',
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
        },
    },
    # Not needed while booked for Thunderbird
    #'alder': {
    #},
    'ash': {
        'mozharness_repo_path': 'users/asasaki_mozilla.com/ash-mozharness',
        'mozharness_repo': 'https://hg.mozilla.org/users/asasaki_mozilla.com/ash-mozharness',
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
            'macosx64-debug': {},
            'win32-debug': {},
        },
        'mobile_platforms': {
            'android': {
                'slave_platforms': ['panda_android', 'vm_android_2_3'],
            },
            'android-x86': {
                'enable_opt_unittests': True,
            },
        },
    },
    'birch': {
        'enable_merging': False,
        'pgo_strategy': 'periodic',
        'enable_nightly': True,
        'create_snippet': True,
        'create_mobile_snippet': True,
        'enable_l10n': True,
        'enable_l10n_onchange': False,
        'l10n_platforms': ['linux', 'linux64'],
        'l10n_tree': 'fxcentral',
        'l10n_repo_path': 'l10n-central',
        'enUS_binaryURL': '/nightly/latest-birch',
        'enable_valgrind': False,
        'branch_projects': [],
        'enable_nightly': False,
        'lock_platforms': True,
        'platforms': {
            'linux': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'talos_slave_platforms': [],
            },
            'linux-debug': {},
            'linux64': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'talos_slave_platforms': [],
            },
            'linux64-debug': {},
        }
    },
    'cedar': {
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
        'mozharness_tag': 'default',
        'enable_talos': True,
        # once ready, we can flip this switch and any platform with
        # mozharness_config in its build config will use mozharness instead
        # of MozharnessBuildFactory on only cypress
        'desktop_mozharness_builds_enabled': False,
    },
    'date': {
        'lock_platforms': True,
        'platforms': {
            'win32': {
                'enable_opt_unittests': True,
            },
            'win64': {
                'enable_opt_unittests': True,
                'slave_platforms': ['win64_vm', 'win8_64'],
            },
            'win64-debug': {
                'enable_debug_unittests': True,
            },
        },
        'enable_merging': False,
    },
    'elm': {},
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
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
        },
        'enable_talos': False,
    },
    'jamun': {},
    'larch': {},
    'maple': {},
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
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'win32': {
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
