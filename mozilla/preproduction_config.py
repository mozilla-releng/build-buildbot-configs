from staging_config import SLAVES, TRY_SLAVES

GLOBAL_VARS = {
    'staging': True,
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'build_tools_repo_path': 'build/tools',
    'stage_server': 'preproduction-stage.srv.releng.scl3.mozilla.com',
    'aus2_host': 'preproduction-stage.srv.releng.scl3.mozilla.com',
    'aus2_user': 'cltbld',
    'aus2_ssh_key': 'cltbld_dsa',
    'download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox',
    'mobile_download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/mobile',
    'graph_server': 'graphs.allizom.org',
    # XXX: should point at aus4-admin-dev once production is pointing elsewhere
    #'balrog_api_root': 'https://aus4-admin-dev.allizom.org',
    'base_clobber_url': 'http://clobberer-preproduction.pvt.build.mozilla.org/index.php',
    'pollInterval': 6*60*60,
    'l10nPollInterval': 6*60*60,
    'disable_tinderbox_mail': True,
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('preproduction-master.srv.releng.scl3.mozilla.com:9008', True, 1),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('preproduction-master.srv.releng.scl3.mozilla.com:9008', True, 1),
        ],
    'xulrunner_tinderbox_tree': 'MozillaTest',
    'weekly_tinderbox_tree': 'MozillaTest',
    'l10n_tinderbox_tree': 'MozillaStaging',
    'packaged_unittest_tinderbox_tree': 'MozillaTest',
    'tinderbox_tree': 'MozillaTest',
    'mobile_tinderbox_tree': 'MobileTest',
    'hg_username': 'stage-ffxbld',
    'base_mirror_urls': ['http://hg-internal.dmz.scl3.mozilla.com'],
    'base_bundle_urls': ['http://preproduction-master.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox/bundles'],
    'tooltool_url_list': ['http://runtime-binaries.pvt.build.mozilla.org/tooltool'],
}

BUILDS_BEFORE_REBOOT = 1
SYMBOL_SERVER_HOST = 'preproduction-stage.srv.releng.scl3.mozilla.com'

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'mozilla-release': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'mozilla-beta': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'mozilla-aurora': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'mozilla-esr17': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'mozilla-b2g18': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'mozilla-b2g18_v1_0_1': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'mozilla-b2g18_v1_1_0_hd': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'try': {
        'email_override': [], # Set to your address when testing
        'download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox',
        'mobile_download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/mobile',
        'enable_mail_notifier': False,
        'package_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'preproduction-stage.srv.releng.scl3.mozilla.com',
                    'MOZ_OBJDIR': 'obj-firefox',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows (x64)/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                    'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
                },
            },
        }
    }
}

PLATFORM_VARS = {
}

PROJECTS = {
    'fuzzing': {
        'disable_tinderbox_mail': True,
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'fuzzing_bundle': 'http://pvtbuilds.pvt.build.mozilla.org/bundles/fuzzing.hg',
        'fuzzing_repo': 'ssh://stage-ffxbld@hg.mozilla.org/private/fuzzing',
        'fuzzing_remote_host': 'ffxbld@preproduction-stage.srv.releng.scl3.mozilla.com',
        # Path needs extra leading slash due to optparse expansion on Win32
        'fuzzing_base_dir': '/pub/mozilla.org/firefox/tinderbox-builds/fuzzing/',
        'idle_slaves': 0,
    },
    'nanojit': {
        'disable_tinderbox_mail': True,
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'MozillaTest',
    },
    'dxr_mozilla-central': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'upload_host': GLOBAL_VARS['stage_server'],
        'upload_user': 'ffxbld',
        'upload_sshkey': '/home/cltbld/.ssh/ffxbld_dsa',
    },
}

BRANCH_PROJECTS = {
    'spidermonkey_tier_1': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'disable_tinderbox_mail': False,
    },
    'spidermonkey_try': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'disable_tinderbox_mail': False,
    },
    'spidermonkey_info': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'disable_tinderbox_mail': False,
    },
}
