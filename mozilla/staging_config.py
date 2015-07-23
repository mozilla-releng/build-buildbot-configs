from copy import deepcopy
import production_config as pc

# Import all of our slave information from production.
SLAVES = deepcopy(pc.SLAVES)
TRY_SLAVES = deepcopy(pc.TRY_SLAVES)

# Add a small stockpile of AWS dev instances.
LINUX64_EC2_DEV    = ['dev-linux64-ec2-%03d' % x for x in range(1, 50)]
SLAVES['mock'].extend(LINUX64_EC2_DEV)
TRY_SLAVES['mock'].extend(LINUX64_EC2_DEV)

WIN64_RELOPS     = ['ix-mn-w0864-%03d' % x for x in range(1,3)]
SLAVES['win64-rev2'].extend(WIN64_RELOPS)
TRY_SLAVES['win64-rev2'].extend(WIN64_RELOPS)

GLOBAL_VARS = {
    'staging': True,
    'config_repo_path': 'users/stage-ffxbld/buildbot-configs',
    'buildbotcustom_repo_path': 'users/stage-ffxbld/buildbotcustom',
    'stage_server': 'dev-stage01.srv.releng.scl3.mozilla.com',
    'download_base_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox',
    'mobile_download_base_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/mobile',
    'graph_server': 'graphs.allizom.org',
    'balrog_api_root': 'https://aus4-admin-dev.allizom.org/api',
    'balrog_username': 'stage-ffxbld',
    'build_tools_repo_path': 'users/stage-ffxbld/tools',
    'base_clobber_url': 'https://api-pub-build.allizom.org/clobberer/lastclobber',
    'disable_tinderbox_mail': True,
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('dev-master1.srv.releng.scl3.mozilla.com:9901', True, 1),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('dev-master1.srv.releng.scl3.mozilla.com:9901', True, 1),
        ],
    'xulrunner_tinderbox_tree': 'MozillaTest',
    'weekly_tinderbox_tree': 'MozillaTest',
    'l10n_tinderbox_tree': 'MozillaStaging',
    'packaged_unittest_tinderbox_tree': 'MozillaTest',
    'tinderbox_tree': 'MozillaTest',
    'mobile_tinderbox_tree': 'MobileTest',
    'hg_username': 'stage-ffxbld',
    'base_bundle_urls': ['http://dev-stage01.build.mozilla.org/pub/mozilla.org/firefox/bundles'],
    'tooltool_url_list': ['http://tooltool.pvt.build.mozilla.org/build'],
    'blob_upload': True,
    'mozharness_configs': {
        'balrog': 'balrog/staging.py',
    },
}

BUILDS_BEFORE_REBOOT = 5
SYMBOL_SERVER_HOST = 'dev-stage01.srv.releng.scl3.mozilla.com'

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'mozilla-release': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'mozilla-beta': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'mozilla-aurora': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'mozilla-esr31': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'mozilla-esr38': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'mozilla-b2g34_v2_1s': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'mozilla-b2g37_v2_2': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'mozilla-b2g37_v2_2r': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'try': {
        'download_base_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox',
        'mobile_download_base_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/mobile',
        'enable_mail_notifier': False, # Set to True when testing
        'email_override': [], # Set to your address when testing
        'package_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'dev-stage01.srv.releng.scl3.mozilla.com',
                    'MOZ_OBJDIR': 'obj-firefox',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                    'BINSCOPE': 'C:\Program Files\Microsoft\SDL BinScope\Binscope.exe',
                    'PATH': "${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                }
            }
        }
    },
}

PLATFORM_VARS = {}

PROJECTS = {
    'fuzzing': {
        'disable_tinderbox_mail': True,
        'scripts_repo': 'https://hg.mozilla.org/users/stage-ffxbld/tools',
        'fuzzing_bundle': 'http://pvtbuilds.pvt.build.mozilla.org/bundles/fuzzing.hg',
        'fuzzing_repo': 'ssh://stage-ffxbld@hg.mozilla.org/private/fuzzing',
        'fuzzing_remote_host': 'stage-ffxbld@stage.mozilla.org',
        # Path needs extra leading slash due to optparse expansion on Win32
        'fuzzing_base_dir': '//mnt/pvt_builds/staging/fuzzing/',
        'idle_slaves': 0,
    },
}

BRANCH_PROJECTS = {
    'spidermonkey_tier_1': {
        'scripts_repo': 'https://hg.mozilla.org/users/stage-ffxbld/tools',
        'idle_slaves': 0,
        'disable_tinderbox_mail': False,
    },
    'spidermonkey_try': {
        'scripts_repo': 'https://hg.mozilla.org/users/stage-ffxbld/tools',
        'idle_slaves': 0,
        'disable_tinderbox_mail': False,
    },
    'spidermonkey_info': {
        'scripts_repo': 'https://hg.mozilla.org/users/stage-ffxbld/tools',
        'idle_slaves': 0,
        'disable_tinderbox_mail': False,
    },
}
