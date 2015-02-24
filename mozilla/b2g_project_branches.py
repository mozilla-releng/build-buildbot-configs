# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    # 'build-system': {},  # Bug 1010674
    'fx-team': {
        'repo_path': 'integration/fx-team',
        'periodic_start_hours': range(2, 24, 3),
        'enable_perproduct_builds': True,
        'enable_nightly': False,
    },
    # Please sync any customizations made to mozilla-inbound to cypress.
    'mozilla-inbound': {
        'repo_path': 'integration/mozilla-inbound',
        'periodic_start_hours': range(1, 24, 3),
        'enable_perproduct_builds': True,
    },
    'b2g-inbound': {
        'repo_path': 'integration/b2g-inbound',
        'periodic_start_hours': range(2, 24, 3),
        'enable_perproduct_builds': True,
        'platforms': {
            'macosx64_gecko': {
                'enable_checktests': False,
            },
            'win32_gecko': {
                'enable_checktests': False,
            },
        },
    },
    #'services-central': {},  # Bug 1010674
    # B2G builds not required on the UX branch
    #'ux': {
    #    'branch_name': 'UX',
    #    'mobile_branch_name': 'UX',
    #    'build_branch': 'UX',
    #    'enable_nightly': True,
    #},
    #####  TWIGS aka RENTABLE BRANCHES
    'alder': {
        'lock_platforms': True,
        'platforms': {
            'linux32_gecko': {},
            'linux64_gecko': {},
            'linux64_gecko-debug': {},
            'linux64-mulet': {},
        },
    },
    'ash': {
        'enable_nightly': True,
        'platforms': {
            'nexus-4': {
                'enable_nightly': True,
            },
            'nexus-4_eng': {
                'enable_nightly': True,
                'consider_for_nightly': False,
            },
            'nexus-5-l': {
                'enable_nightly': True,
            },
            'nexus-5-l_eng': {
                'enable_nightly': True,
                'consider_for_nightly': False,
            },
            'flame-kk': {
                'enable_nightly': True,
            },
            'flame-kk_eng': {
                'enable_nightly': True,
            },
            'emulator': {
                'enable_nightly': True,
            },
            'emulator-debug': {
                'enable_nightly': True,
            },
            'emulator-jb': {
                'enable_nightly': True,
            },
            'emulator-jb-debug': {
                'enable_nightly': True,
            },
            'linux64-b2g-haz': {
                'enable_nightly': False,
            },
            'emulator-kk': {
                'enable_nightly': True,
            },
            'emulator-kk-debug': {
                'enable_nightly': True,
            },
            'dolphin': {
                'enable_nightly': True,
            },
            'dolphin_eng': {
                'enable_nightly': True,
            },
        },
    },
    # Not needed on Birch at the moment, bug 977420.
    #'birch': {},
    'cedar': {
        'mozharness_tag': 'default',
    },
    'cypress': {},
    # B2G builds not required on date
    # 'date': {},
    'fig': {
        'lock_platforms': True,
        'platforms': {},
    },
    # disabled by bug 1134508
    # 'gum': {},
    # disabled for bug 985718
    #'holly': {},
    'jamun': {},
    'larch': {
        "desktop_mozharness_builds_enabled": True,
        "platforms": {
            "linux64_graphene": {},
        },
    },
    'maple': {},
    # Customizations for integration work for bugs 481815 and 307181
    'oak': {
        'enable_nightly': True
    },
    'pine': {}
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()
