from localconfig import SLAVES

GLOBAL_VARS = {
    'staging': True,
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'preproduction-stage.srv.releng.scl3.mozilla.com',
    'aus2_user': 'cltbld',
    'aus2_ssh_key': 'cltbld_dsa',
    'aus2_host': 'preproduction-stage.srv.releng.scl3.mozilla.com',
    'download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird',
    'graph_server': 'graphs.allizom.org',
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://clobberer-preproduction.pvt.build.mozilla.org/index.php',
    'pollInterval': 6*60*60,
    'l10nPollInterval': 6*60*60,
    'disable_tinderbox_mail': True,
    'talos_masters': [],
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
    'hg_username': 'stage-tbirdbld',
    'base_bundle_urls': ['http://preproduction-master.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird/bundles'],
}

BUILDS_BEFORE_REBOOT = 1
SYMBOL_SERVER_HOST = 'preproduction-stage.srv.releng.scl3.mozilla.com'

# Local branch overrides
BRANCHES = {
    'comm-central': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
        'download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird',
    },
    'comm-beta': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'comm-aurora': {
        'enable_blocklist_update': False,
        'file__update_on_closed_tree': False,
        'download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird',
    },
    'comm-esr24': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'try-comm-central': {
        'download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird/',
        'enable_mail_notifier': False, # Set to True when testing
        'email_override': [], # Set to your address when testing
        'package_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'preproduction-stage.srv.releng.scl3.mozilla.com',
                    'MOZ_OBJDIR': 'objdir-tb',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                    'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
                }
            }
        }
    },
}

PLATFORM_VARS = {
}

PROJECTS = {
}
