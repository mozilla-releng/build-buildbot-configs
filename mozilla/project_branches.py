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
    'graphics': {
        'enable_talos': False,
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
                'slave_platforms': ['win8'],
                'talos_slave_platforms': ['win8'],
            },
            'win32-debug': {
                'enable_checktests': False,
                'slave_platforms': ['win8'],
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
            'linux64-br-haz': {},
            'linux64-sh-haz': {},
            'macosx64-debug': {},
            'win32-debug': {},
        },
        'mobile_platforms': {
            'android': {
                'slave_platforms': ['panda_android', 'ubuntu64_hw_mobile'],
            },
            'android-x86': {
                'enable_opt_unittests': True,
            },
            'android-armv6': {
                'enable_opt_unittests': True,
            }

        },
    },
    #'birch': {},  # Bug 1010674
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
        # once ready, we can flip this switch and any platform with
        # mozharness_config in its build config will use mozharness instead
        # of MozharnessBuildFactory
        'desktop_mozharness_builds_enabled': True,
    },
    'cypress': {
        'mozharness_tag': 'default',
        'enable_talos': True,
        # once ready, we can flip this switch and any platform with
        # mozharness_config in its build config will use mozharness instead
        # of MozharnessBuildFactory
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
    'fig': {
        'lock_platforms': True,
        'platforms': {
            'linux64-mulet': {},
            'macosx64-mulet': {},
        }
    },
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
    'larch': {
        'lock_platforms': True,
        'platforms': {
            'android': {},
            'android-armv6': {},
            'android-x86': {},
            'android-debug': {},
        },
    },
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
