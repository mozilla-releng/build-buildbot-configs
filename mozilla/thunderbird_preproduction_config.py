from preproduction_config import \
    MAC_LION_MINIS, MAC_SNOW_MINIS, MAC_MINIS, XSERVES, WIN32_IXS, WIN64_IXS, LINUX_VMS, \
    LINUX_IXS, LINUX64_VMS, LINUX64_IXS

SLAVES = {
    'linux':            LINUX_VMS + LINUX_IXS,
    'linux64':          LINUX64_VMS + LINUX64_IXS,
    'win32':            WIN32_IXS,
    'win64':            WIN64_IXS,
    'macosx':           MAC_MINIS + XSERVES,
    'macosx64':         MAC_SNOW_MINIS,
    'macosx64-lion':    MAC_LION_MINIS,
}

TRY_LINUX      = ['try-linux-slave%02i' % x for x in range (1,31)]
TRY_LINUX_IXS  = []
TRY_LINUX64    = ['try-linux64-slave%02i' % x for x in range (1,11)]
TRY_LINUX64_IXS= ['linux64-ix-slave%02i' % x for x in range(22,41)]
TRY_MAC        = ['try-mac-slave%02i' % x for x in range (1,48)]
TRY_MAC64      = ['try-mac64-slave%02i' % x for x in range (1,32)]
TRY_WIN32_IXS  = []

TRY_SLAVES = SLAVES
TRY_SLAVES['linux'] += TRY_LINUX + TRY_LINUX_IXS
TRY_SLAVES['linux64'] += TRY_LINUX64 + TRY_LINUX64_IXS
TRY_SLAVES['macosx'] += TRY_MAC
TRY_SLAVES['macosx64'] += TRY_MAC64
TRY_SLAVES['win32'] += TRY_WIN32_IXS


GLOBAL_VARS = {
    'staging': True,
    #XXX 'config_repo_path': 'build/buildbot-configs',
    'config_repo_path': 'users/john.hopkins_mozillamessaging.com/buildbot-configs-stage',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'preproduction-stage.srv.releng.scl3.mozilla.com',
    'aus2_user': 'cltbld',
    'aus2_ssh_key': 'cltbld_dsa',
    'aus2_host': 'preproduction-stage.srv.releng.scl3.mozilla.com',
    'download_base_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird-test',
    'graph_server': 'graphs.allizom.org',
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://build.mozilla.org/preproduction-clobberer/index.php',
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
    'base_mirror_urls': ['http://hg.build.scl1.mozilla.com'],
    'base_bundle_urls': ['http://preproduction-master.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird/bundles'],
}

BUILDS_BEFORE_REBOOT = 1
SYMBOL_SERVER_HOST = 'preproduction-stage.srv.releng.scl3.mozilla.com'

# Local branch overrides
BRANCHES = {
    'comm-central': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'comm-release': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'comm-beta': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'comm-aurora': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
    },
    'comm-esr10': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
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
                    'CVS_RSH': 'ssh',
                    'MOZ_OBJDIR': 'objdir-tb',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                    'PATH': "${MOZILLABUILD}buildbotve\\scripts;${PATH}",
                }
            }
        }
    },
}

PLATFORM_VARS = {
}

PROJECTS = {
}
