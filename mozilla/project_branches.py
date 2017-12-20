# noinspection PyInterpreter
PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    # 'build-system': {},  # Bug 1010674
    #'fx-team': {},  #bug 1296396
    'mozilla-inbound': {
        'merge_builds': False,
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'pgo_strategy': 'periodic',
        'periodic_start_hours': range(0, 24, 3),
        'talos_suites': {
            'xperf': 1,
        },
        'branch_projects': [],
    },
    #'services-central': {},  # Bug 1010674
    # 'alder': {},
    # Bug 1252292 - Schedule e10s tests on Ash for all desktop platforms
    'ash': {
        'enable_talos': False,
        'lock_platforms': True,
        'merge_builds': False,
        'periodic_start_hours': [9, 21],
        'pgo_strategy': 'periodic',
        'platforms': {
            'linux': {
                'slave_platforms': ['ubuntu32_vm'],
            },
            'linux64': {
                'slave_platforms': ['ubuntu64_vm'],
            },
            'linux64-asan': {
                'slave_platforms': ['ubuntu64-asan_vm'],
            },
            'linux64-debug': {
                'slave_platforms': ['ubuntu64_vm'],
            },
            'macosx64': {
                'slave_platforms': ['yosemite_r7'],
            },
            'macosx64-debug': {
                'slave_platforms': ['yosemite_r7'],
            },
            'win32': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
        },
    },
    'autoland': {
        'merge_builds': False,
        'repo_path': 'integration/autoland',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'pgo_strategy': 'periodic',
        'periodic_start_hours': range(0, 24, 3),
        'talos_suites': {
            'xperf': 1,
        },
        'branch_projects': [],
    },
    'birch': {
        'gecko_version': 58,
        'watch_all_branches': True,
        'desktop_mozharness_builds_enable': True,
        'use_mozharness_repo_cache': False,
        'branch_projects': [],
        'enable_opt_unittests': False,
        'enable_debug_unittests': False,
        'enable_talos': True,
        'platforms': {
            'linux': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'linux64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'win32': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'win64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'macosx64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
        },
        'pgo_strategy': 'per-checkin',
        'enable_release_promotion': {
            "firefox": True,
            "fennec": True,
        },
        'build_tools_repo_path': 'users/bhearsum_mozilla.com/tools',
        "release_platforms": ("linux", "linux64", "win32", "win64", "macosx64"),
        "l10n_release_platforms": ("linux", "linux64", "win32", "win64", "macosx64"),
        "single_locale_branch_config": {
            "firefox": "dev-mozilla-release",
        },
        "partner_repacks_platforms": {
            "firefox": ("linux", "linux64", "win32", "win64", "macosx64")
        },
        "eme_free_repacks_platforms": {
            "firefox": ("win32", "win64", "macosx64")
        },
        "partner_repack_config": {
            "firefox": {
                "script_name": "scripts/desktop_partner_repacks.py",
                "extra_args": [
                    "--cfg", "partner_repacks/release_mozilla-release_desktop.py",
                    "--s3cfg", "NO_UPLOADS_IN_STAGING",
                ],
            },
        },
        'release_channel_mappings': {
            "firefox": [
                [r"^\d+\.0$", ["beta", "release"]],  # RC, 45.0
                [r"^\d+\.\d+\.\d+$", ["release"]],  # Other (dot releaseas), 45.0.4
            ]
        },
        'uptake_monitoring_platforms': {
            "firefox": ("linux", "linux64", "win32", "win64", "macosx64"),
            "fennec": ("android-api-16", "android-x86"),
        },
        # temp balrog
        'balrog_api_root': 'http://54.90.211.22:8080/api',
        'funsize_balrog_api_root': 'http://54.90.211.22:8080/api',
        'tuxedoServerUrl': 'https://admin-bouncer-releng.stage.mozaws.net/api',
        'bouncer_submitter_config': {
            "firefox": "releases/bouncer_firefox_release.py",
            "fennec": "releases/bouncer_fennec_release.py",
        },
        'binary_transparency_enabled': True,
        'bouncer_enabled': True,
        'updates_builder_enabled': True,
        'update_verify_enabled': True,
        'postrelease_version_bump_enabled': {
            "firefox": True,
            "fennec": True,
        },
        'postrelease_version_bump_config': {
            "firefox": 'releases/dev_postrelease_firefox_release_birch.py',
            "fennec": 'releases/dev_postrelease_fennec_release.py',
        },
        'uptake_monitoring_enabled': True,
        'uptake_monitoring_config': {
            "firefox": 'releases/bouncer_firefox_release.py',
            "fennec": "releases/bouncer_fennec_release.py",
        },
        'postrelease_bouncer_aliases_enabled': True,
        'postrelease_bouncer_aliases_config': {
            "firefox": 'releases/bouncer_firefox_release.py',
            "fennec": "releases/bouncer_fennec_release.py",
        },
        'postrelease_mark_as_shipped_enabled': True,
        'postrelease_mark_as_shipped_config': {
            "firefox": 'releases/dev_postrelease_firefox_release_birch.py',
            "fennec": 'releases/dev_postrelease_fennec_release.py',
        },
        'push_to_candidates_enabled': True,
        'updates_config': {
            "firefox": 'releases/dev_updates_firefox_release_birch.py',
            "fennec": "",
        },
        'beetmover_credentials': '/builds/dev-beetmover-s3.credentials',
        'beetmover_buckets': {
            'firefox': 'net-mozaws-stage-delivery-firefox',
            'fennec': 'net-mozaws-stage-delivery-archive',
        },
        'stage_product': {
            'firefox': 'firefox',
            'fennec': 'mobile',
        },
        'signing_class': {
            "firefox": "release-signing",
            "fennec": "dep-signing",
        },
        'signing_cert': {
            "firefox": "release",
            "fennec": "depend",
        },
        'moz_disable_mar_cert_verification': False,
        'root_home_dir': {
            "firefox": "desktop",
            "fennec": "mobile",
        },
        'enabled_products': ['firefox', 'mobile'],
        'push_to_releases_automatic': False,
        'merge_builds': False,
        'snap_enabled': {"firefox": True},
        'update_verify_channel': {
            'firefox': 'release-localtest',
        },
        'tc_indexes': {
            "firefox": {
                "linux": {
                    "unsigned": "gecko.v2.birch.nightly.revision.{rev}.firefox.linux-opt",
                    "signed": "gecko.v2.birch.signed-nightly.revision.{rev}.firefox-l10n.linux-opt.en-US",
                    "repackage-signing": "gecko.v2.birch.nightly.revision.{rev}.firefox.linux-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "linux64": {
                    "unsigned": "gecko.v2.birch.nightly.revision.{rev}.firefox.linux64-opt",
                    "signed": "gecko.v2.birch.signed-nightly.revision.{rev}.firefox-l10n.linux64-opt.en-US",
                    "repackage-signing": "gecko.v2.birch.nightly.revision.{rev}.firefox.linux64-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "macosx64": {
                    "unsigned": "gecko.v2.birch.nightly.revision.{rev}.firefox.macosx64-opt",
                    "signed": "gecko.v2.birch.signed-nightly.revision.{rev}.firefox-l10n.macosx64-opt.en-US",
                    "repackage": "gecko.v2.birch.nightly.revision.{rev}.firefox.macosx64-nightly-repackage",
                    "repackage-signing": "gecko.v2.birch.nightly.revision.{rev}.firefox.macosx64-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "win32": {
                    "unsigned": "gecko.v2.birch.revision.{rev}.firefox-l10n.win32-opt.en-US",
                    "signed": "gecko.v2.birch.signed-nightly.revision.{rev}.firefox-l10n.win32-opt.en-US",
                    "repackage-signing": "gecko.v2.birch.revision.{rev}.firefox-l10n.win32-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
                "win64": {
                    "unsigned": "gecko.v2.birch.revision.{rev}.firefox-l10n.win64-opt.en-US",
                    "signed": "gecko.v2.birch.signed-nightly.revision.{rev}.firefox-l10n.win64-opt.en-US",
                    "repackage-signing": "gecko.v2.birch.revision.{rev}.firefox-l10n.win64-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
            },
            # TODO: fennec
        },
        'lzma_to_bz2': True,
    },
# Bug 1308544 - Enable automation jobs on Cedar twig
    'cedar': {
        'enable_perproduct_builds': False,
        'lock_platforms': True,
        'mozharness_tag': 'default',
        'enable_talos': True,
        'talos_suites': {
            'other': 1,
            'svgr': 1,
            'tp5o': 1,
            'other-e10s': 1,
            'svgr-e10s': 1,
            'tp5o-e10s': 1,
        },
        'enable_opt_unittests': True,
        'platforms': {
            'linux64': {},
            'linux64-debug': {},
            'macosx64': {},
            'macosx64-debug': {},
            'win32': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
        },
    },
    # Disabled by bug 1363047
    # 'cypress': {},
    'maple': {
        'gecko_version': 58,
        'watch_all_branches': True,
        'desktop_mozharness_builds_enabled': True,
        'use_mozharness_repo_cache': False,
        'branch_projects': [],
        ## TODO - enabled tests.
        # note - to enable tests you must also remove:
        # platforms[platform]["slave_platforms"] item override below
        'enable_opt_unittests': False,
        'enable_debug_unittests': False,
        'enable_talos': True,
        'platforms': {
            'linux': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'linux64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'win32': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'win64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'macosx64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'win32-devedition': {
                'dep_signing_servers': 'nightly-signing',
                "enable_dep": False,
            },
            'win64-devedition': {
                'dep_signing_servers': 'nightly-signing',
                "enable_dep": False,
            },
            'macosx64-devedition': {
                'dep_signing_servers': 'nightly-signing',
                "enable_dep": False,
            },
            'linux64-devedition': {
                'dep_signing_servers': 'nightly-signing',
                "enable_dep": False,
            },
        },
        'pgo_strategy': 'per-checkin',
        'enable_release_promotion': {
            "firefox": True,
            "devedition": True,
            "fennec": True,
        },
        'build_tools_repo_path': 'users/asasaki_mozilla.com/tools',
        "release_platforms": ("linux", "linux64", "win32", "win64", "macosx64"),
        "l10n_release_platforms": ("linux", "linux64", "win32", "win64", "macosx64"),
        "single_locale_branch_config": {
            "firefox": "dev-mozilla-beta",
            "devedition": "dev-mozilla-beta_devedition",
        },
        "partner_repacks_platforms": {
            "firefox": ("linux", "linux64", "win32", "win64", "macosx64")
        },
        "eme_free_repacks_platforms": {
            "firefox": ("win32", "win64", "macosx64")
        },
        "partner_repack_config": {
            "firefox": {
                "script_name": "scripts/desktop_partner_repacks.py",
                "extra_args": [
                    "--cfg", "partner_repacks/release_mozilla-release_desktop.py",
                    "--s3cfg", "NO_UPLOADS_IN_STAGING",
                ],
            },
        },
        'release_channel_mappings': {
            "firefox": [["^.*$", ["beta"]]],
            "devedition": [["^.*$", ["aurora"]]],
        },
        'uptake_monitoring_platforms': {
            "firefox": ("linux", "linux64", "win32", "win64", "macosx64"),
            "fennec": ("android-api-16", "android-x86"),
            "devedition": ("linux", "linux64", "win32", "win64", "macosx64"),
        },
        # temp balrog
        'balrog_api_root': 'http://54.90.211.22:8080/api',
        'funsize_balrog_api_root': 'http://54.90.211.22:8080/api',
        'tuxedoServerUrl': 'https://admin-bouncer-releng.stage.mozaws.net/api',
        'bouncer_submitter_config': {
            "firefox": "releases/bouncer_firefox_beta.py",
            "devedition": "releases/bouncer_firefox_devedition.py",
            "fennec": "releases/bouncer_fennec_beta.py",
        },
        'binary_transparency_enabled': True,
        'bouncer_enabled': True,
        'updates_builder_enabled': True,
        'update_verify_enabled': True,
        'postrelease_version_bump_enabled': {
            "firefox": True,
            "devedition": True,
            "fennec": True,
        },
        'postrelease_version_bump_config': {
            "firefox": 'releases/dev_postrelease_firefox_beta.py',
            "devedition": 'releases/dev_postrelease_firefox_beta.py',
            "fennec": 'releases/dev_postrelease_fennec_beta.py',
        },
        'uptake_monitoring_enabled': True,
        'uptake_monitoring_config': {
            "firefox": 'releases/bouncer_firefox_beta.py',
            "devedition": 'releases/bouncer_firefox_devedition.py',
            "fennec": "releases/bouncer_fennec_beta.py",
        },
        'postrelease_bouncer_aliases_enabled': True,
        'postrelease_bouncer_aliases_config': {
            "firefox": 'releases/bouncer_firefox_beta.py',
            "devedition": 'releases/bouncer_firefox_devedition.py',
            "fennec": "releases/bouncer_fennec_beta.py",
        },
        'postrelease_mark_as_shipped_enabled': True,
        'postrelease_mark_as_shipped_config': {
            "firefox": 'releases/dev_postrelease_firefox_beta.py',
            "devedition": 'releases/dev_postrelease_firefox_beta.py',
            "fennec": 'releases/dev_postrelease_fennec_beta.py',
        },
        'push_to_candidates_enabled': True,
        'updates_config': {
            "firefox": 'releases/dev_updates_firefox_beta.py',
            "devedition": 'releases/dev_updates_firefox_devedition.py',
            "fennec": "",
        },
        'beetmover_credentials': '/builds/dev-beetmover-s3.credentials',
        'beetmover_buckets': {
            'firefox': 'net-mozaws-stage-delivery-firefox',
            'devedition': 'net-mozaws-stage-delivery-archive',
            'fennec': 'net-mozaws-stage-delivery-archive',
        },
        'stage_product': {
            'firefox': 'firefox',
            'fennec': 'mobile',
            'devedition': 'devedition',
        },
        'signing_class': {
            "firefox": "release-signing",
            "devedition": "nightly-signing",
            "fennec": "dep-signing",
        },
        'signing_cert': {
            "firefox": "release",
            "devedition": "nightly",
            "fennec": "depend",
        },
        'moz_disable_mar_cert_verification': False,
        'accepted_mar_channel_id': {
            "firefox": "firefox-mozilla-beta",
            "devedition": "firefox-mozilla-aurora",
            # TODO: fennec
        },
        'root_home_dir': {
            "firefox": "desktop",
            "devedition": "desktop",
            "fennec": "mobile",
        },
        'enabled_products': ['firefox', 'mobile', 'devedition'],
        'push_to_releases_automatic': False,
        'merge_builds': False,
        'snap_enabled': {"firefox": True, "devedition": False},
        'update_verify_channel': {
            'firefox': 'beta-localtest',
            'devedition': 'aurora-localtest',
        },
        'tc_indexes': {
            "firefox": {
                "linux": {
                    "unsigned": "gecko.v2.maple.nightly.revision.{rev}.firefox.linux-opt",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.firefox-l10n.linux-opt.en-US",
                    "repackage-signing": "gecko.v2.maple.nightly.revision.{rev}.firefox.linux-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "linux64": {
                    "unsigned": "gecko.v2.maple.nightly.revision.{rev}.firefox.linux64-opt",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.firefox-l10n.linux64-opt.en-US",
                    "repackage-signing": "gecko.v2.maple.nightly.revision.{rev}.firefox.linux64-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "macosx64": {
                    "unsigned": "gecko.v2.maple.nightly.revision.{rev}.firefox.macosx64-opt",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.firefox-l10n.macosx64-opt.en-US",
                    "repackage": "gecko.v2.maple.nightly.revision.{rev}.firefox.macosx64-nightly-repackage",
                    "repackage-signing": "gecko.v2.maple.nightly.revision.{rev}.firefox.macosx64-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "win32": {
                    "unsigned": "gecko.v2.maple.revision.{rev}.firefox-l10n.win32-opt.en-US",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.firefox-l10n.win32-opt.en-US",
                    "repackage-signing": "gecko.v2.maple.revision.{rev}.firefox-l10n.win32-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
                "win64": {
                    "unsigned": "gecko.v2.maple.revision.{rev}.firefox-l10n.win64-opt.en-US",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.firefox-l10n.win64-opt.en-US",
                    "repackage-signing": "gecko.v2.maple.revision.{rev}.firefox-l10n.win64-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
            },
            "devedition": {
                "linux": {
                    "unsigned": "gecko.v2.maple.revision.{rev}.devedition-l10n.linux-opt.en-US",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.devedition-l10n.linux-opt.en-US",
                    "ci_system": "tc",
                },
                "linux64": {
                    "unsigned": "gecko.v2.maple.revision.{rev}.devedition-l10n.linux64-opt.en-US",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.devedition-l10n.linux64-opt.en-US",
                    "ci_system": "tc",
                },
                "macosx64": {
                    "unsigned": "gecko.v2.maple.nightly.revision.{rev}.devedition.macosx64-opt",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.devedition-l10n.macosx64-opt.en-US",
                    "repackage": "gecko.v2.maple.revision.{rev}.firefox-l10n.macosx64-devedition-nightly-repackage.en-US",
                    "repackage-signing": "gecko.v2.maple.revision.{rev}.firefox-l10n.macosx64-devedition-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
                "win32": {
                    "unsigned": "gecko.v2.maple.revision.{rev}.devedition-l10n.win32-opt.en-US",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.devedition-l10n.win32-opt.en-US",
                    "repackage-signing": "gecko.v2.maple.revision.{rev}.firefox-l10n.win32-devedition-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
                "win64": {
                    "unsigned": "gecko.v2.maple.revision.{rev}.devedition-l10n.win64-opt.en-US",
                    "signed": "gecko.v2.maple.signed-nightly.revision.{rev}.devedition-l10n.win64-opt.en-US",
                    "repackage-signing": "gecko.v2.maple.revision.{rev}.firefox-l10n.win64-devedition-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
            },
            # TODO: fennec
        },
        'lzma_to_bz2': True,
    },
    # Disabled by bug 1363047
    # 'elm': {},
    # Disabled by Bug 1135702
    # 'fig': {},
    # Disabled by Bug 1206269
    # 'gum': {},
    # Disabled by bug 1363047
    # 'holly': {},

    'jamun': {
        'gecko_version': 56,
        'watch_all_branches': True,
        'desktop_mozharness_builds_enabled': True,
        'use_mozharness_repo_cache': False,
        'branch_projects': [],
        ## TODO - enabled tests.
        # note - to enable tests you must also remove:
        # platforms[platform]["slave_platforms"] item override below
        'enable_opt_unittests': False,
        'enable_debug_unittests': False,
        'enable_talos': False,
        ##
        'lock_platforms': True,
        'platforms': {
            # use default 'dep-signing' for now while in development
            'linux': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'linux64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'win32': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'win64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'macosx64': {
                'dep_signing_servers': 'release-signing',
                "slave_platforms": [],
                "enable_dep": False,
            },
            'win32-devedition': {
                'dep_signing_servers': 'nightly-signing',
                "enable_dep": False,
            },
            'win64-devedition': {
                'dep_signing_servers': 'nightly-signing',
                "enable_dep": False,
            },
            'macosx64-devedition': {
                'dep_signing_servers': 'nightly-signing',
                "enable_dep": False,
            },
            'linux64-devedition': {
                'dep_signing_servers': 'nightly-signing',
                "enable_dep": False,
            },
        },
        'pgo_strategy': 'per-checkin',
        'enable_release_promotion': {
            "firefox": True,
            "devedition": True,
        },
        'build_tools_repo_path': 'users/stage-ffxbld/tools',
        "release_platforms": ("linux", "linux64", "win32", "win64", "macosx64"),
        "l10n_release_platforms": ("linux", "linux64", "win32", "win64", "macosx64"),
        "single_locale_branch_config": {
            "firefox": "dev-mozilla-release",
            "devedition": "dev-mozilla-beta_devedition",
        },
        'release_channel_mappings': {
            "firefox": [["^.*$", ["beta"]]],
            "devedition": [["^.*$", ["aurora"]]],
        },
        'uptake_monitoring_platforms': {
            "firefox": ("linux", "linux64", "win32", "win64", "macosx64"),
            "fennec": ("android-api-15", "android-x86"),
            "devedition": ("linux", "linux64", "win32", "win64", "macosx64"),
        },
        # temp balrog
        'balrog_vpn_proxy': 'balrogStageVPNProxy',
        'balrog_api_root': 'https://balrog-admin.stage.mozaws.net/api',
        'funsize_balrog_api_root': 'http://balrog/api',
        'tuxedoServerUrl': 'https://admin-bouncer-releng.stage.mozaws.net/api',
        'bouncer_submitter_config': {
            "firefox": "releases/bouncer_firefox_release.py",
            "devedition": "releases/bouncer_firefox_devedition.py",
        },
        'binary_transparency_enabled': True,
        'bouncer_enabled': True,
        'updates_builder_enabled': True,
        'update_verify_enabled': True,
        'postrelease_version_bump_enabled': {
            "firefox": True,
            "devedition": False,
            "fennec": True,
        },
        'postrelease_version_bump_config': {
            "firefox": 'releases/dev_postrelease_firefox_release.py',
            "devedition": 'disabled',
        },
        'uptake_monitoring_enabled': True,
        'uptake_monitoring_config': {
            "firefox": 'releases/bouncer_firefox_release.py',
            "devedition": 'releases/bouncer_firefox_devedition.py',
        },
        'postrelease_bouncer_aliases_enabled': True,
        'postrelease_bouncer_aliases_config': {
            "firefox": 'releases/bouncer_firefox_release.py',
            "devedition": 'releases/bouncer_firefox_devedition.py',
        },
        'postrelease_mark_as_shipped_enabled': True,
        'postrelease_mark_as_shipped_config': {
            "firefox": 'releases/dev_postrelease_firefox_release.py',
            "devedition": 'releases/dev_postrelease_firefox_beta.py',
        },
        'push_to_candidates_enabled': True,
        'updates_config': {
            "firefox": 'releases/dev_updates_firefox_release.py',
            "devedition": 'releases/dev_updates_firefox_devedition.py',
        },
        'beetmover_credentials': '/builds/dev-beetmover-s3.credentials',
        'beetmover_buckets': {
            'firefox': 'net-mozaws-stage-delivery-firefox',
            'devedition': 'net-mozaws-stage-delivery-archive',
        },
        'stage_product': {
            'firefox': 'firefox',
            'fennec': 'mobile',
            'devedition': 'devedition',
        },
        'signing_class': {
            "firefox": "release-signing",
            "devedition": "nightly-signing",
        },
        'signing_cert': {
            "firefox": "release",
            "devedition": "nightly",
        },
        'moz_disable_mar_cert_verification': False,
        'accepted_mar_channel_id': {
            "firefox": "firefox-mozilla-release",
            "devedition": "firefox-mozilla-aurora",
        },
        'root_home_dir': {
            "firefox": "desktop",
            "devedition": "desktop",
        },
        'enabled_products': ['firefox', 'mobile', 'devedition'],
        'push_to_releases_automatic': False,
        'merge_builds': False,
        'snap_enabled': {"firefox": True, "devedition": False},
        'update_verify_channel': {
            'firefox': 'release-localtest',
            'devedition': 'aurora-localtest',
        },
        'tc_indexes': {
            "firefox": {
                "linux": {
                    "unsigned": "gecko.v2.jamun.nightly.revision.{rev}.firefox.linux-opt",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.firefox-l10n.linux-opt.en-US",
                    "repackage-signing": "gecko.v2.jamun.nightly.revision.{rev}.firefox.linux-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "linux64": {
                    "unsigned": "gecko.v2.jamun.nightly.revision.{rev}.firefox.linux64-opt",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.firefox-l10n.linux64-opt.en-US",
                    "repackage-signing": "gecko.v2.jamun.nightly.revision.{rev}.firefox.linux64-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "macosx64": {
                    "unsigned": "gecko.v2.jamun.nightly.revision.{rev}.firefox.macosx64-opt",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.firefox-l10n.macosx64-opt.en-US",
                    "repackage": "gecko.v2.jamun.nightly.revision.{rev}.firefox.macosx64-nightly-repackage",
                    "repackage-signing": "gecko.v2.jamun.nightly.revision.{rev}.firefox.macosx64-nightly-repackage-signing",
                    "ci_system": "tc",
                },
                "win32": {
                    "unsigned": "gecko.v2.jamun.revision.{rev}.firefox-l10n.win32-opt.en-US",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.firefox-l10n.win32-opt.en-US",
                    "repackage-signing": "gecko.v2.jamun.revision.{rev}.firefox-l10n.win32-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
                "win64": {
                    "unsigned": "gecko.v2.jamun.revision.{rev}.firefox-l10n.win64-opt.en-US",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.firefox-l10n.win64-opt.en-US",
                    "repackage-signing": "gecko.v2.jamun.revision.{rev}.firefox-l10n.win64-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
            },
            "devedition": {
                "linux": {
                    "unsigned": "gecko.v2.jamun.revision.{rev}.devedition-l10n.linux-opt.en-US",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.devedition-l10n.linux-opt.en-US",
                    "ci_system": "tc",
                },
                "linux64": {
                    "unsigned": "gecko.v2.jamun.revision.{rev}.devedition-l10n.linux64-opt.en-US",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.devedition-l10n.linux64-opt.en-US",
                    "ci_system": "tc",
                },
                "macosx64": {
                    "unsigned": "gecko.v2.jamun.nightly.revision.{rev}.devedition.macosx64-opt",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.devedition-l10n.macosx64-opt.en-US",
                    "repackage": "gecko.v2.jamun.revision.{rev}.firefox-l10n.macosx64-devedition-nightly-repackage.en-US",
                    "repackage-signing": "gecko.v2.jamun.revision.{rev}.firefox-l10n.macosx64-devedition-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
                "win32": {
                    "unsigned": "gecko.v2.jamun.revision.{rev}.devedition-l10n.win32-opt.en-US",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.devedition-l10n.win32-opt.en-US",
                    "repackage-signing": "gecko.v2.jamun.revision.{rev}.firefox-l10n.win32-devedition-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
                "win64": {
                    "unsigned": "gecko.v2.jamun.revision.{rev}.devedition-l10n.win64-opt.en-US",
                    "signed": "gecko.v2.jamun.signed-nightly.revision.{rev}.devedition-l10n.win64-opt.en-US",
                    "repackage-signing": "gecko.v2.jamun.revision.{rev}.firefox-l10n.win64-devedition-nightly-repackage-signing.en-US",
                    "ci_system": "tc",
                },
            },
            # TODO: fennec
        },
        # Disable when running beta staging releases
        'lzma_to_bz2': False,
    },
    'larch': {
        'lock_platforms': True,
        'pgo_strategy': 'per-checkin',
        'platforms': {
            'linux': {},
            'linux64': {},
            'linux64-asan': {},
            'linux64-debug': {},
            'macosx64': {},
            'macosx64-debug': {},
            'win32': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
        },
    },
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
    'pine': {
        'enable_perproduct_builds': False,
        'mozharness_tag': 'default',
        'enable_opt_unittests': True,
        'enable_talos': True,
    },
    'graphics': {
        'enable_perproduct_builds': False,
        'mozharness_tag': 'default',
        'enable_opt_unittests': True,
        'enable_talos': True,
    },
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = PROJECT_BRANCHES[branch].get('tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('mobile_tinderbox_tree', branch.title())
