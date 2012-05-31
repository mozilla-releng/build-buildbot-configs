MAC_LION_MINIS = ['r5-mini-%03d' % x for x in range(1,7)] + \
                 ['bld-lion-r5-%03d' % x for x in range(1,81)]
MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in [2] + range(40,57) if x not in (51,52,)] # bug683792
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in range(1,27)]
WIN64_IXS      = ['w64-ix-slave%02i' % x for x in range(4,22) + range(23,40) + [41] + range(43,85)]
WIN64_METRO    = ['w64-ix-slave%02i' % x for x in [22,40,42]]
LINUX_VMS      = ['bld-centos5-32-vmw-%03i' % x for x in range(1,23)]
LINUX_IXS      = ['mv-moz2-linux-ix-slave%02i' % x for x in range(1,24)] + ['linux-ix-slave%02i' % x for x in range(1,43)]
LINUX64_VMS    = ['bld-centos5-64-vmw-%03i' % x for x in range(1, 7)]
LINUX64_IXS    = ['linux64-ix-slave%02i' % x for x in range(1,42)]
MOCK_DL120G7   = ['bld-centos6-hp-%03d' % x for x in range(1,43)]

SLAVES = {
    'linux':            LINUX_VMS + LINUX_IXS,
    'linux64':          LINUX64_VMS + LINUX64_IXS,
    'win32':            WIN32_IXS,
    'win64':            WIN64_IXS,
    'win64-metro':      WIN64_METRO,
    'macosx':           [],
    'macosx64':         MAC_SNOW_MINIS,
    'macosx64-lion':    MAC_LION_MINIS,
    'linux-android':    LINUX_VMS + LINUX_IXS,
    'android':          LINUX_VMS + LINUX_IXS,
    'android-xul':      LINUX_VMS + LINUX_IXS,
    'mock':             MOCK_DL120G7
}

TRY_LINUX      = ['bld-centos5-32-vmw-%03i' % x for x in range(23,40)]
TRY_LINUX_IXS  = []
TRY_LINUX64    = ['bld-centos5-64-vmw-%03i' % x for x in range(7, 12)]
TRY_LINUX64_IXS= ['linux64-ix-slave%02i' % x for x in range(22,41)]
TRY_MAC64      = ['try-mac64-slave%02i' % x for x in range (27,32)]
TRY_WIN32_IXS  = []
TRY_WIN64_IXS  = []

TRY_SLAVES = SLAVES
TRY_SLAVES['linux']    += TRY_LINUX + TRY_LINUX_IXS
TRY_SLAVES['linux64']  += TRY_LINUX64 + TRY_LINUX64_IXS
TRY_SLAVES['macosx64'] += TRY_MAC64
TRY_SLAVES['win32']    += TRY_WIN32_IXS
TRY_SLAVES['win64']    += TRY_WIN64_IXS

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
    'graph_server': 'graphs.allizom.org',#TODO
    # XXX: should point at aus4-admin-dev once production is pointing elsewhere
    #'balrog_api_root': 'https://aus4-admin-dev.allizom.org',
    'base_clobber_url': 'http://build.mozilla.org/preproduction-clobberer/index.php',
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
    'base_mirror_urls': ['http://hg-internal.dmz.scl3.mozilla.com', 'http://hg.build.scl1.mozilla.com'],
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
    'mozilla-esr10': {
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
                    'CVS_RSH': 'ssh',
                    'MOZ_OBJDIR': 'obj-firefox',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                    'PATH': "${MOZILLABUILD}buildbotve\\scripts;${PATH}",
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
}
