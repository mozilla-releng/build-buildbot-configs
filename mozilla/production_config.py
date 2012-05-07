MAC_LION_MINIS = ['bld-lion-r5-%03d' % x for x in range(41,81)]
MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in [2] + range(40,57) if x not in (51,52,)] # bug683792
LINUX_VMS      = ['moz2-linux-slave%02i' % x for x in [1,2] + range(5,47) \
                 if x not in (10,17)] + \
                 ['bld-centos5-32-vmw-%03i' % x for x in range(1,23)]
LINUX_IXS      = ['mv-moz2-linux-ix-slave%02i' % x for x in range(2,22)] + \
                 ['linux-ix-slave%02i' % x for x in [1,2,6] + range(12,43)]
LINUX64_VMS    = ['moz2-linux64-slave%02i' % x for x in range(1,13) \
                 if x not in (7,10)] + \
                 ['bld-centos5-64-vmw-%03i' % x for x in range(1, 7)]
LINUX64_IXS    = ['linux64-ix-slave%02i' % x for x in range(3,22)]
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in range(2,16) + [20, 26]] + \
                 ['w32-ix-slave%02i' % x for x in range(24,45)]
WIN64_IXS      = ['w64-ix-slave%02i' % x for x in [2] + range(6,25)]
MOCK_DL120G7   = ['bld-centos6-hp-%03d' % x for x in range(6,24)] # 5 staging, 17 prod, 17 try

SLAVES = {
    'linux':            LINUX_VMS + LINUX_IXS,
    'linux64':          LINUX64_VMS + LINUX64_IXS,
    'win32':            WIN32_IXS,
    'win64':            WIN64_IXS,
    'macosx':           [],
    'macosx64':         MAC_SNOW_MINIS,
    'macosx64-lion':    MAC_LION_MINIS,
    'linux-android':    LINUX_VMS + LINUX_IXS,
    'android':          LINUX_VMS + LINUX_IXS,
    'android-xul':      LINUX_VMS + LINUX_IXS,
    'mock':             MOCK_DL120G7
}

TRY_LINUX      = ['try-linux-slave%02i' % x for x in range(1,5) + range(6,31)] + \
                 ['moz2-linux-slave%02i' % x for x in range(47,51)] + \
                 ['bld-centos5-32-vmw-%03i' % x for x in range(23,40)]
TRY_LINUX_IXS  = ['mv-moz2-linux-ix-slave%02i' % x for x in range(22,24)] + \
                 ['linux-ix-slave%02i' % x for x in range(7,12)]
TRY_LINUX64    = ['try-linux64-slave%02i' % x for x in range(1,11)] + \
                 ['bld-centos5-64-vmw-%03i' % x for x in range(7, 12)]
TRY_LINUX64_IXS= ['linux64-ix-slave%02i' % x for x in range(22,42)]
TRY_MAC64      = ['try-mac64-slave%02i' % x for x in range(27,32)]
TRY_WIN32_IXS  = ['mw32-ix-slave%02i' % x for x in range(16,19) + range(22,26)] + \
                 ['w32-ix-slave%02i' % x for x in range(2,24)]
TRY_WIN64_IXS  = ['w64-ix-slave%02i' % x for x in range(25,43)]
TRY_MOCK_DL120G7 = ['bld-centos6-hp-%03d' % x for x in range(24,43)]
TRY_LION         = ['bld-lion-r5-%03d' % x for x in range(1,41)]

TRY_SLAVES = {
    'linux':       TRY_LINUX + TRY_LINUX_IXS,
    'linux64':     TRY_LINUX64 + TRY_LINUX64_IXS,
    'win32':       TRY_WIN32_IXS,
    'win64':       TRY_WIN64_IXS,
    'macosx64':    TRY_MAC64,
    'macosx64-lion': TRY_LION,
    'mock':        TRY_MOCK_DL120G7,
}

# Local overrides for default values
GLOBAL_VARS = {
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'stage.mozilla.org',
    'aus2_host': 'aus3-staging.mozilla.org',
    'aus2_user': 'ffxbld',
    'aus2_ssh_key': 'auspush',
    'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox',
    'mobile_download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/mobile',
    'graph_server': 'graphs.mozilla.org',
    'balrog_api_root': 'https://aus4-admin-dev.allizom.org',
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://build.mozilla.org/clobberer/index.php',
    'disable_tinderbox_mail': True,
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('buildbot-master36.build.mozilla.org:9301', True, 5),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('buildbot-master36.build.mozilla.org:9301', True, 5),
    ],
    'xulrunner_tinderbox_tree': 'XULRunner',
    'weekly_tinderbox_tree': 'Testing',
    'l10n_tinderbox_tree': 'Mozilla-l10n',
    'base_mirror_urls': ['http://hg-internal.dmz.scl3.mozilla.com', 'http://hg.build.scl1.mozilla.com'],
    'base_bundle_urls': ['http://ftp.mozilla.org/pub/mozilla.org/firefox/bundles'],
}

BUILDS_BEFORE_REBOOT = 1
SYMBOL_SERVER_HOST = 'symbols1.dmz.phx1.mozilla.com'

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'packaged_unittest_tinderbox_tree': 'Firefox',
        'tinderbox_tree': 'Firefox',
        'mobile_tinderbox_tree': 'Mobile',
        'mobile_build_failure_emails': ['mobile-build-failures@mozilla.org'],
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'Firefox3.6',
        'packaged_unittest_tinderbox_tree': 'Firefox3.6',
        'mobile_tinderbox_tree': 'Mobile1.1',
    },
    'mozilla-release': {
        'packaged_unittest_tinderbox_tree': 'Mozilla-Release',
        'tinderbox_tree': 'Mozilla-Release',
        'mobile_tinderbox_tree': 'Mozilla-Release',
    },
    'mozilla-esr10': {
        'packaged_unittest_tinderbox_tree': 'Mozilla-Esr10',
        'tinderbox_tree': 'Mozilla-Esr10',
        'mobile_tinderbox_tree': 'Mozilla-Esr10',
    },
    'mozilla-beta': {
        'packaged_unittest_tinderbox_tree': 'Mozilla-Beta',
        'tinderbox_tree': 'Mozilla-Beta',
        'mobile_tinderbox_tree': 'Mozilla-Beta',
    },
    'mozilla-aurora': {
        'packaged_unittest_tinderbox_tree': 'Mozilla-Aurora',
        'tinderbox_tree': 'Mozilla-Aurora',
        'mobile_tinderbox_tree': 'Mozilla-Aurora',
    },
    'places': {
        'tinderbox_tree': 'Places',
        'mobile_tinderbox_tree': 'Places',
        'packaged_unittest_tinderbox_tree': 'Places',
    },
    'electrolysis': {
        'tinderbox_tree': 'Electrolysis',
        'mobile_tinderbox_tree': 'Electrolysis',
        'packaged_unittest_tinderbox_tree': 'Electrolysis',
    },
    'addonsmgr': {
        'tinderbox_tree': 'AddonsMgr',
        'mobile_tinderbox_tree': 'AddonsMgr',
        'packaged_unittest_tinderbox_tree': 'AddonsMgr',
    },
    'jaegermonkey': {
        'tinderbox_tree': 'Jaegermonkey',
        'mobile_tinderbox_tree': 'Jaegermonkey',
        'packaged_unittest_tinderbox_tree': 'Jaegermonkey',
    },
    'try': {
        'tinderbox_tree': 'Try',
        'mobile_tinderbox_tree': 'Try',
        'packaged_unittest_tinderbox_tree': 'Try',
        'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'mobile_download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'relengweb1.dmz.scl3.mozilla.com',
                    'CVS_RSH': 'ssh',
                    'MOZ_OBJDIR': 'obj-firefox',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                    'BINSCOPE': 'C:\Program Files\Microsoft\SDL BinScope\Binscope.exe',
                    'PATH': "${MOZILLABUILD}buildbotve\\scripts;${PATH}",
                }
            }
        }
    },
}

PLATFORM_VARS = {}

PROJECTS = {
    'fuzzing': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'fuzzing_repo': 'ssh://ffxbld@hg.mozilla.org/private/fuzzing',
        'fuzzing_remote_host': 'ffxbld@pvtbuilds2.dmz.scl3.mozilla.com',
        # Path needs extra leading slash due to optparse expansion on Win32
        'fuzzing_base_dir': '//mnt/pvt_builds/fuzzing/',
        'idle_slaves': 3,
        'disable_tinderbox_mail': False,
    },
    'nanojit': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 3,
        'tinderbox_tree': 'Nanojit',
        'disable_tinderbox_mail': False,
    },
    'spidermonkey_mozilla-inbound': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Mozilla-Inbound',
        'disable_tinderbox_mail': False,
    },
    'spidermonkey_ionmonkey': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'Ionmonkey',
    },
}

if __name__ == "__main__":
    import sys, pprint
    args = sys.argv[1:]

    # print build slave details
    host_info = {
        'production': SLAVES,
        'try': TRY_SLAVES,
    }

    if len(args) > 0:
        list_names = args
    else:
        list_names = host_info.keys()

    for list_name in list_names:
        for host_platform in host_info[list_name]:
            for host_name in host_info[list_name][host_platform]:
                print("%s,%s,%s" % (list_name, host_platform, host_name))

