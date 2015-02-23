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
        'updates_enabled': True,
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
        'desktop_mozharness_builds_enabled': True,
        'desktop_mozharness_repacks_enabled': True,
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'use_mozharness_repo_cache': False,
        'lock_platforms': True,
        'talos_suites': {
            'xperf': 1,
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
        'platforms': {
            # Bug 1094364 - switch win64 builds to use mozharness mach
            #   testing on cedar first. to land across trunk: remove below and add to:
            # win64 - http://hg.mozilla.org/build/buildbot-configs/file/828d626c2603/mozilla/config.py#l948
            # win64-debug - http://hg.mozilla.org/build/buildbot-configs/file/828d626c2603/mozilla/config.py#l1362
            'win64': {
                'mozharness_desktop_build': {
                    'script_name': 'scripts/fx_desktop_build.py',
                    'extra_args': [
                        '--config', 'builds/releng_base_windows_64_builds.py',
                    ],
                    'script_timeout': 3 * 3600,
                    'script_maxtime': int(5.5 * 3600),
                },
            },
            'win64-debug': {
                'mozharness_desktop_build': {
                    'script_name': 'scripts/fx_desktop_build.py',
                    'extra_args': [
                        '--config', 'builds/releng_base_windows_64_builds.py',
                        '--custom-build-variant-cfg', 'debug',
                    ],
                    'script_timeout': 3 * 3600,
                    'script_maxtime': int(5.5 * 3600),
                },
            }
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
        'enable_nightly': True,
        'pgo_strategy': 'per-checkin',
        'branch_projects': [],
        'lock_platforms': True,
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
            'macosx64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux-debug': {},
            'linux64-asan': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'win64-debug': {},
        },
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
        'updates_enabled': True,
        'create_partial': True,
        'nightly_signing_servers': 'nightly-signing',
    },
    # customizations for integration work for bugs 481815 and 307181
    'oak': {
        'enable_nightly': True,
        'updates_enabled': True,
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
