from copy import deepcopy
import production_config as pc

MAC_SNOW_MINIS = ['moz2-darwin10-slave02']
LINUX_IXS      = ['mv-moz2-linux-ix-slave01'] + \
                 ['linux-ix-slave%02i' % x for x in (3,4,5)]
LINUX64_IXS    = ['linux64-ix-slave%02i' % x for x in (1,2)]
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in (1, 19, 21)]
WIN64_IXS      = ['w64-ix-slave%02i' % x for x in (4, 5)]
MOCK_DL120G7   = ['bld-centos6-hp-%03d' % x for x in range(1, 6)]

STAGING_SLAVES = {
    'linux':            LINUX_IXS,
    'linux64':          LINUX64_IXS,
    'macosx64':         MAC_SNOW_MINIS,
    'win32':            WIN32_IXS,
    'win64':            WIN64_IXS,
    'android':          LINUX_IXS,
    'mock':             MOCK_DL120G7
}

SLAVES = deepcopy(STAGING_SLAVES)

for p, slaves in pc.SLAVES.items() + pc.TRY_SLAVES.items():
    if p not in SLAVES:
        SLAVES[p] = list(slaves)
    else:
        SLAVES[p].extend(slaves)


TRY_SLAVES = deepcopy(SLAVES)

GLOBAL_VARS = {
    'staging': True,
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'dev-stage01.srv.releng.scl3.mozilla.com',
    'aus2_host': 'dev-stage01.srv.releng.scl3.mozilla.com',
    'aus2_user': 'ffxbld',
    'aus2_ssh_key': 'ffxbld_dsa',
    'download_base_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox',
    'mobile_download_base_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/mobile',
    'graph_server': 'graphs.allizom.org',
    # XXX: should point at aus4-admin-dev once production is pointing elsewhere
    #'balrog_api_root': 'https://aus4-admin-dev.allizom.org',
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://clobberer-stage.pvt.build.mozilla.org/index.php',
    'disable_tinderbox_mail': True,
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('dev-master01.build.scl1.mozilla.com:9901', True, 1),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('dev-master01.build.scl1.mozilla.com:9901', True, 1),
        ],
    'xulrunner_tinderbox_tree': 'MozillaTest',
    'weekly_tinderbox_tree': 'MozillaTest',
    'l10n_tinderbox_tree': 'MozillaStaging',
    'packaged_unittest_tinderbox_tree': 'MozillaTest',
    'tinderbox_tree': 'MozillaTest',
    'mobile_tinderbox_tree': 'MobileTest',
    'hg_username': 'stage-ffxbld',
    'base_mirror_urls': ['http://hg-internal.dmz.scl3.mozilla.com'],
    'base_bundle_urls': ['http://dev-stage01.build.mozilla.org/pub/mozilla.org/firefox/bundles'],
    'tooltool_url_list': ['http://runtime-binaries.pvt.build.mozilla.org/tooltool'],
}

BUILDS_BEFORE_REBOOT = 5
SYMBOL_SERVER_HOST = 'dev-stage01.srv.releng.scl3.mozilla.com'

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
    'mozilla-esr10': {
        'enable_blocklist_update': False,
        'blocklist_update_on_closed_tree': False,
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
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows (x64)/srcsrv/pdbstr.exe',
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
    'fuzzing': {
        'disable_tinderbox_mail': True,
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'fuzzing_repo': 'ssh://stage-ffxbld@hg.mozilla.org/private/fuzzing',
        'fuzzing_remote_host': 'stage-ffxbld@pvtbuilds2.dmz.scl3.mozilla.com',
        # Path needs extra leading slash due to optparse expansion on Win32
        'fuzzing_base_dir': '//mnt/pvt_builds/staging/fuzzing/',
        'idle_slaves': 0,
    },
    'nanojit': {
        'disable_tinderbox_mail': True,
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'MozillaTest',
    },
    'spidermonkey_mozilla-inbound': {
        'disable_tinderbox_mail': True,
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'MozillaTest',
    },
    'spidermonkey_ionmonkey': {
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
