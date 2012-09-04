# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    'accessibility': {
        'mozconfig_dir': 'accessibility',
        'enable_nightly': True,
        'enabled_products': ['firefox'],
        # only want a11y which is run within the "chrome" suite
        # turn other suites off
        'talos_suites': {
            'dirty': 0,
            'tp4': 0,
            'tp': 0,
            'chrome_twinopen': 0,
            'chrome_mac': 0,
            'chrome': 0,
            'nochrome': 0,
            'dromaeo': 0,
            'svg': 0,
            'paint': 0,
        },
        'add_test_suites': [
            ('macosx64', 'snowleopard', 'opt', 'mochitest-other', 'mochitest-a11y'),
            ('macosx64', 'snowleopard', 'debug', 'mochitest-other', 'mochitest-a11y'),
        ]
    },
    'build-system': {
        'pgo_strategy': 'per-checkin',
        'platforms': {
            'win32': {
                'pgo_platform': 'win64',
            },
            'win64': {
                'enable_pymake': True,
            },
        },
    },
    'devtools':{
        'enable_nightly': True,
        'enabled_products': ['firefox'],
        'platforms': {
            'macosx64': {
                'slave_platforms': ['snowleopard', 'lion', 'mountainlion'],
            },
            'android': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'tegra_android': {},
            },
        },
    },
    # DISABLED because of builder limit problems - bug 721854
    #'electrolysis': {
    #    'mozconfig_dir': 'electrolysis',
    #    'enable_talos': True,
    #},
    'fx-team': {
        'repo_path': 'integration/fx-team',
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': True,
        'pgo_strategy': 'periodic',
    },
    # Turning off graphics - bug 649507
    #'graphics':{
    #    'enable_unittests': False,
    #    'enable_talos': False,
    #},
    'ionmonkey': {
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'pgo_strategy': 'periodic',
        'talos_suites': {
            'v8': 1,
        },
    },
    'jaegermonkey': {
        'mozconfig_dir': 'jaegermonkey',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
    },
    'mozilla-inbound': {
        'repo_path': 'integration/mozilla-inbound',
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': False,
        'enable_weekly_bundle': True,
        'pgo_strategy': 'periodic',
        'periodic_pgo_interval': 3,
        'platforms': {
            'linux64': {
                'build_space': 7,
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux': {
                'build_space': 7,
                'nightly_signing_servers': 'nightly-signing',
            },
            'macosx64-debug': {
                'enable_leaktests': True,
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'macosx64': {
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
        },
    },
    # DISABLED because of builder limit problems - bug 721854
#    'places': {
#        'platforms': {
#            'linux64': {
#                'build_space': 6,
#            },
#            'linux': {
#                'build_space': 6,
#            },
#        },
#    },
    'profiling': {
        'enable_talos': False,
        'platforms': {
            'macosx64-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'macosx64': {
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
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
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win64': {
                'nightly_signing_servers': 'nightly-signing',
            },
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
        'mozconfig_dir' : 'ux',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'enable_unittests': False,
        'enable_talos': False,
        'platforms': {
            'macosx64-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'macosx64': {
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
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
    },
    #####  TWIGS aka RENTABLE BRANCHES
    # customizations while booked for bug 687570 - WebRTC project
    'alder': {
        'platforms': {
            'android': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'enable_talos': False,
                'tegra_android': {},
            },
        },
    },
    'ash': {},
    # customizations for building OS X only (testing gcc OS X builds still work)
    'birch': {
        'lock_platforms': True,
        'platforms': {
            'macosx64': {},
            'macosx64-debug': {},
        },
    },
    'cedar': {},
    # customizations for windows update service changes (bug 481815)
    'elm': {
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'lock_platforms': True,
        'platforms': {
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
                'enable_pymake': False,
            },
            'win64': {
                'nightly_signing_servers': 'nightly-signing',
                'enable_pymake': False,
            },
            'win32-debug': {
                'enable_pymake': False,
            },
            'win32-metro': {
                'enable_pymake': False,
            },
        },
        'enable_talos': False,
    },
    'holly': {},
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
