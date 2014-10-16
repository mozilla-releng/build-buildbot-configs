from localconfig import SLAVES

GLOBAL_VARS = {
    'staging': True,
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'dev-stage01.srv.releng.scl3.mozilla.com',
    'balrog_username': 'stage-tbirdbld',
    'aus2_user': 'tbirdbld',
    'aus2_ssh_key': 'tbirdbld_dsa',
    'aus2_host': 'dev-stage01.srv.releng.scl3.mozilla.com',
    'download_base_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird',
    'graph_server': 'graphs.allizom.org',
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://clobberer-stage.pvt.build.mozilla.org/index.php',
    'disable_tinderbox_mail': True,
    'talos_masters': [],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('dev-master1.srv.releng.scl3.mozilla.com:9901', True, 1),
        ],
    'xulrunner_tinderbox_tree': 'ThunderbirdTest',
    'weekly_tinderbox_tree': 'ThunderbirdTest',
    'l10n_tinderbox_tree': 'MozillaStaging',
    'packaged_unittest_tinderbox_tree': 'ThunderbirdTest',
    'tinderbox_tree': 'ThunderbirdTest',
    'hg_username': 'stage-tbirdbld',
    'base_bundle_urls': ['http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird/bundles'],
}

BUILDS_BEFORE_REBOOT = 5
SYMBOL_SERVER_HOST = 'dev-stage01.srv.releng.scl3.mozilla.com'

# Local branch overrides
BRANCHES = {
    'comm-central': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'comm-beta': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'comm-aurora': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'comm-esr31': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'try-comm-central': {
        'download_base_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird',
        'enable_mail_notifier': False, # Set to True when testing
        'email_override': [], # Set to your address when testing
        'package_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'dev-stage01.srv.releng.scl3.mozilla.com',
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
