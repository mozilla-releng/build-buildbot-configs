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
        'branch_projects': [ 'spidermonkey_tier_1', 'spidermonkey_info' ],
    },
    # Please sync any customizations made to mozilla-inbound to cypress.
    'mozilla-inbound': {
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'enable_weekly_bundle': True,
        'pgo_strategy': 'periodic',
        'periodic_pgo_interval': 3,
        'talos_suites': {
            'xperf': 1,
        },
        'branch_projects': [ 'spidermonkey_tier_1', 'spidermonkey_info' ],
    },
    # Customized to be the same as inbound. bug 866314
    'cypress': {
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'enable_weekly_bundle': True,
        'pgo_strategy': 'periodic',
        'periodic_pgo_interval': 3,
        'talos_suites': {
            'xperf': 1,
        },
        'branch_projects': [ 'spidermonkey_tier_1', 'spidermonkey_info' ],
    },
    'b2g-inbound': {
        'repo_path': 'integration/b2g-inbound',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'pgo_strategy': 'periodic',
        'periodic_pgo_interval': 3,
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
            },
            'macosx64-debug': {
                'enable_checktests': False,
                'slave_platforms': ['mountainlion'],
            },
        },
    },
    'profiling': {
        'pgo_strategy': 'periodic',
        'platforms': {
            'macosx64-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'linux-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'linux64-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'win32-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
        },
        'mobile_platforms': {
            'android-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
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
        'pgo_strategy': 'periodic',
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
        },
    },
    #####  TWIGS aka RENTABLE BRANCHES
    # customizations while booked for bug 687570 - WebRTC project
    'alder': {
        'platforms': {},
        'mobile_platforms': {
            'android': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'enable_talos': False,
                'tegra_android': {},
            },
            'android-armv6': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'enable_talos': False,
                'tegra_android': {},
            },
        },
    },
    'ash': {
        'mozharness_repo_path': 'users/asasaki_mozilla.com/ash-mozharness',
        'mozharness_repo': 'http://hg.mozilla.org/users/asasaki_mozilla.com/ash-mozharness',
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
                'slave_platforms': ['panda_android', 'panda_android-nomozpool'],
            },
        },
    },
    'birch': {},
    'cedar': {
        'mozharness_tag': 'default',
        'lock_platforms': True,
        'enable_talos': True,
        'talos_suites': {
            'xperf': 1,
        },
        'blob_upload': True,
        'enable_nightly': True,
        'create_snippet': True,
        'create_mobile_snippet': True,
        'platforms': {
            'linux': {
                'enable_nightly': False,
                'create_snippet': False,
            },
            'linux64': {
                'enable_nightly': False,
                'create_snippet': False,
            },
            'win32': {
                'enable_nightly': False,
                'create_snippet': False,
            },
            'macosx64': {
                'enable_nightly': False,
                'create_snippet': False,
            },
            'linux-debug': {
                'enable_nightly': False,
                'create_snippet': False,
            },
            'linux64-debug': {
                'enable_nightly': False,
                'create_snippet': False,
            },
            'macosx64-debug': {
                'enable_nightly': False,
                'create_snippet': False,
            },
            'win32-debug': {
                'enable_nightly': False,
                'create_snippet': False,
            },
        },
        'mobile_platforms': {
            'android': {
                'enable_nightly': True,
                'create_snippet': True,
                'create_mobile_snippet': True,
            },
            'android-debug': {
                'enable_nightly': False,
                'create_snippet': False,
                'create_mobile_snippet': False,
            },
        },
    },
    'date': {
        'lock_platforms': True,
        'platforms': {
            'win64': {
                'enable_opt_unittests': True,
            },
        },
    },
    # customizations for PICL (bug 900212)
    'elm': {
        'enable_nightly': True,
        'enable_weekly_bundle': True,
        'create_snippet': True,
        'create_partial': True,
        'enable_talos': False,
        'lock_platforms': True,
        'platforms': {
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux-debug': {},
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux64-debug': {},
            'macosx64-debug': {},
            'macosx64': {
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win32-debug': {},
        },
        'mobile_platforms': {
            'android': {},
            'android-debug': {},
            'android-armv6': {},
            'android-x86': {},
        },
    },
    'fig': {
        'lock_platforms': True,
        'platforms': {},
        'enable_nightly': True,
        'create_snippet': True,
        'create_mobile_snippet': True,
        'mobile_platforms': {
            'android': {
                'enable_nightly': True,
                'create_snippet': True,
                'create_mobile_snippet': True,
            },
            'android-debug': {
                'enable_nightly': False,
                'create_snippet': False,
                'create_mobile_snippet': False,
            },
            'android-noion': {
                'enable_nightly': False,
                'create_snippet': False,
                'create_mobile_snippet': False,
            },
            'android-armv6': {
                'enable_nightly': False,
                'create_snippet': False,
                'create_mobile_snippet': False,
            },
            'android-x86': {
                'enable_nightly': False,
                'create_snippet': False,
                'create_mobile_snippet': False,
            },
        },
    },
    'gum': {},
    'holly': {},
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
    'pine': {},
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = PROJECT_BRANCHES[branch].get('tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('mobile_tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['packaged_unittest_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('packaged_unittest_tinderbox_tree', branch.title())
