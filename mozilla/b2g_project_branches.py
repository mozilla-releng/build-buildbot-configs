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
        'enable_nightly': True,
        "enable_onchange_scheduler": False,
        "enable_nightly_scheduler": False,
        "enable_periodic_scheduler": False,
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
    'cypress': {
        'lock_platforms': True,
        'platforms': {
            # Limit B2G to none for Bug 1164935
        },
    },
    # B2G builds not required on date
    # 'date': {},
    # Dsiabled by Bug 1135702
    # 'fig': {},
    # disabled by bug 1134508
    # 'gum': {},
    # disabled for bug 985718
    #'holly': {},
    # disabled for bug 1150320
    #'jamun': {},
    'larch': {
        "desktop_mozharness_builds_enabled": True,
        'enable_nightly': True,
        "lock_platforms": True,
        "platforms": {
            "linux64_graphene": {},
            "macosx64_graphene": {},
            "win64_graphene": {},
            "linux64_horizon": {},
            "macosx64_horizon": {},
            "win64_horizon": {},
        }
    },
    'maple': {
        'enable_nightly': True,
        'platforms': {
            'macosx64_gecko': {
                'mozharness_desktop_build': {
                    'script_name': 'scripts/b2g_desktop_build.py',
                    'extra_args': ['--config', 'b2g/desktop_macosx64.py'],
                },
            },
            'macosx64_gecko-debug': {
                'mozharness_desktop_build': {
                    'script_name': 'scripts/b2g_desktop_build.py',
                    'extra_args': [
                        '--config', 'b2g/desktop_macosx64.py',
                    '--custom-build-variant-cfg', 'b2g-debug',
                    ],
                },
            },
            'win32_gecko': {
                'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
                'mozharness_desktop_build': {
                    'script_name': 'scripts/b2g_desktop_build.py',
                    'extra_args': ['--config', 'b2g/desktop_windows32.py'],
                },
            },
            'win32_gecko-debug': {
                'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
                'mozharness_desktop_build': {
                    'script_name': 'scripts/b2g_desktop_build.py',
                    'extra_args': [
                        '--config', 'b2g/desktop_windows32.py',
                    '--custom-build-variant-cfg', 'b2g-debug',
                    ],
                },
            },
        },
    },
    # Customizations for integration work for bugs 481815 and 307181
    'oak': {
        'enable_nightly': True
    },
    'pine': {}
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()
