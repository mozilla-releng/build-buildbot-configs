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
    },
    'mozilla-inbound': {
        'merge_builds': False,
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
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
        'pgo_strategy': None,
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
    # customized for bug 1156408
    # 'alder': {},
    'ash': {
        'merge_builds': False,
        'enable_perproduct_builds': True,
        'pgo_strategy': 'per-checkin',
        'enable_l10n': True,
        'enable_l10n_onchange': False,
        'l10n_repo_path': 'l10n-central',
        'l10n_platforms': ['linux', 'linux64', 'win32', 'macosx64', 'win64'],
        'l10nDatedDirs': True,
        'l10n_tree': 'fxcentral',
        'updates_enabled': True,
        'l10nNightlyUpdate': True,
        'enUS_binaryURL': '/nightly/latest-ash',
        'enable_mac_a11y': True,
        'enable_multi_locale': True,
        'create_partial': True,
        'create_partial_l10n': True,
        'upload_mobile_symbols': True,
        'desktop_mozharness_repacks_enabled': True,
        'l10n_extra_configure_args': ['--with-macbundlename-prefix=Firefox'],
        'enable_nightly': True,
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
        'lock_platforms': True,
        'platforms': {
            # Limit Firefox to none for Bug 787208
        },
    },
    'date': {
        'desktop_mozharness_builds_enabled': True,
        'use_mozharness_repo_cache': False,
        'branch_projects': [],
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'lock_platforms': True,
        'platforms': {
            'linux': {
                'dep_signing_servers': 'release-signing',
            },
            'linux64': {
                'dep_signing_servers': 'release-signing',
            },
            'macosx64': {
                'dep_signing_servers': 'release-signing',
            },
            'win32': {
                'dep_signing_servers': 'release-signing',
            },
            'win64': {
                'dep_signing_servers': 'release-signing',
            },
            'linux-debug': {},
            'linux64-debug': {},
            'linux64-asan': {},
            'linux64-asan-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'win64-debug': {},
        },
        'enable_valgrind': False,
        'pgo_strategy': 'per-checkin',
        'enable_release_promotion': True,
        'build_tools_repo_path': 'users/raliiev_mozilla.com/tools',
        'partners_repo_path': 'build/partner-repacks',
        'partner_repack_platforms': ('linux', 'linux64', 'win32', 'win64', 'macosx64'),
        "release_platforms": ("linux", "linux64", "win32", "win64", "macosx64"),
        "l10n_release_platforms": ("linux", "linux64", "win32", "win64", "macosx64"),
        "release_channels": ("date", ),
        # temp balrog
        'balrog_api_root': 'http://ec2-54-241-39-23.us-west-1.compute.amazonaws.com:443/api',
        'funsize_balrog_api_root': 'http://ec2-54-241-39-23.us-west-1.compute.amazonaws.com:443/api',
        'tuxedoServerUrl': 'https://admin-bouncer.stage.mozaws.net/api',
        'bouncer_submitter_config': "releases/bouncer_firefox_date.py",
        'bouncer_branch': "releases/date",
        'bouncer_enabled': True,
        'postrelease_version_bump_enabled': True,
        'postrelease_version_bump_config': 'releases/postrelease_date.py',
        'push_to_candidates_enabled': True,
        'updates_config': 'releases/updates_date.py',
        'update_verify_chunks': 6,
        'beetmover_credentials': '/builds/dev-beetmover-s3.credentials',
        'beetmover_buckets': {
            'firefox': 'net-mozaws-stage-delivery-firefox',
            # TODO - add fennec support
            # 'fennec': 'net-mozaws-stage-delivery-archive',
        },
        'stage_product': {
            'firefox': 'firefox',
            'fennec': 'mobile',
        },
        'push_to_releases_automatic': False,
        'merge_builds': False,
    },
    'elm': {
        'branch_projects': [],
        'enable_talos': True,
        'enable_valgrind': False,
        'lock_platforms': True,
        'platforms': {
            # dep signing with nightly key, see bug 1176152
            'linux': {
                'dep_signing_servers': 'nightly-signing',
            },
            'linux64': {
                'dep_signing_servers': 'nightly-signing',
            },
            'linux-debug': {},
            'linux64-debug': {},
        },
    },
    # Dsiabled by Bug 1135702
    # 'fig': {},
    # Disabled by Bug 1206269
    # 'gum': {},
    # disabled in bug 1215527
    # 'holly': {},
    'jamun': {
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux64': {},
            'linux-debug': {},
            'linux64-br-haz': {},
            'linux64-asan': {},
            'linux64-asan-debug': {},
            'linux64-debug': {},
            'linux64-st-an-debug': {},
            'macosx64-debug': {},
            'win32': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
            'macosx64': {},
            'macosx64-st-an-debug': {},
        }
    },
    'larch': {
        'lock_platforms': True,
        'platforms': {
        },
    },
    # disabled in bug 1215527
    # 'maple': {},
    # customizations for integration work for bugs 481815 and 307181
    'oak': {
        'enable_nightly': True,
        'updates_enabled': True,
        'create_partial': True,
        'enable_talos': False,
        'pgo_strategy': 'periodic',
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
