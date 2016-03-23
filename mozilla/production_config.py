MAC_LION_MINIS = ['bld-lion-r5-%03d' % x for x in range(1,7) + range(41,55) + range(56,69) + \
                  range(70,87) + range(88,95)]

WIN64_REV2     = ['b-2008-ix-%04i' % x for x in range(1,18) + range(65,89) + range(90,159) + range(161,173)] + \
                 ['b-2008-ec2-%04d' % x for x in range(1, 31)] + \
                 ['b-2008-spot-%03d' % x for x in range(1, 201)]

LINUX64_EC2    = ['bld-linux64-ec2-%03d' % x for x in range(1, 50) + range(301, 350)] + \
                 ['bld-linux64-spot-%03d' % x for x in range(1, 300) + range(300, 600)] + \
                 ['bld-linux64-spot-%d' % x for x in range(1000, 1100)]

LINUX64_AV_EC2 = ['av-linux64-ec2-%03d' % x for x in range(1,5)] + \
    ['av-linux64-spot-%03d' % x for x in range(1,5)]

SLAVES = {
    'win64-rev2':       WIN64_REV2,
    'macosx64-lion':    MAC_LION_MINIS,
    'mock':             LINUX64_EC2,
    'linux64-av':       LINUX64_AV_EC2,
}

TRY_MAC64       = []
TRY_LINUX64_EC2 = ['try-linux64-ec2-%03d' % x for x in range(1, 60) + range(301,340)] + \
                  ['try-linux64-spot-%03d' % x for x in range(1, 200) + range(300,500)] + \
                  ['try-linux64-spot-%d' % x for x in range(1000, 1100)]
TRY_WIN64_REV2  = ['b-2008-ix-%04i' % x for x in range(18, 65) + range(173, 175) + range(176, 185)] + \
                  ['y-2008-ec2-%04d' % x for x in range(1, 31)] + \
                  ['y-2008-spot-%03d' % x for x in range(1, 201)]
TRY_LION        = ['bld-lion-r5-%03d' % x for x in range(7,31) + range(32,37)] + \
                  ['bld-lion-r5-%03d' % x for x in range(95,97)]

if set(TRY_WIN64_REV2).intersection(WIN64_REV2):
    raise Exception('TRY_WIN64_REV2 and WIN64_REV2 overlap')

TRY_SLAVES = {
    'win64-rev2':  TRY_WIN64_REV2,
    'macosx64':    TRY_MAC64,
    'macosx64-lion': TRY_LION,
    'mock':        TRY_LINUX64_EC2,
}

# Local overrides for default values
GLOBAL_VARS = {
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'upload.ffxbld.productdelivery.prod.mozaws.net',
    'download_base_url': 'http://archive.mozilla.org/pub/firefox',
    'mobile_download_base_url': 'http://archive.mozilla.org/pub/mobile',
    'graph_server': 'graphs.mozilla.org',
    'balrog_api_root': 'https://aus4-admin.mozilla.org/api',
    # Used by special docker workers with balrogVpnProxy feature enabled
    'funsize_balrog_api_root': 'http://balrog/api',
    'balrog_username': 'ffxbld',
    'balrog_submitter_extra_args': ['--url-replacement',
                                    'ftp.mozilla.org,download.cdn.mozilla.net'],
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'https://api.pub.build.mozilla.org/clobberer/lastclobber',
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('buildbot-master81.build.mozilla.org:9301', True, 5),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('buildbot-master81.build.mozilla.org:9301', True, 5),
    ],
    'base_bundle_urls': ['https://ftp-ssl.mozilla.org/pub/mozilla.org/firefox/bundles'],
    'tooltool_url_list': ['https://api.pub.build.mozilla.org/tooltool/'],
    'blob_upload': True,
    'mozharness_configs': {
        'balrog': 'balrog/production.py',
        'single_locale_environment': 'single_locale/production.py',
    },
    'bucket_prefix': 'net-mozaws-prod-delivery',
}

BUILDS_BEFORE_REBOOT = 1
SYMBOL_SERVER_HOST = 'symbolpush.mozilla.org'

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'tinderbox_tree': 'Firefox',
        'mobile_tinderbox_tree': 'Mobile',
        'mobile_build_failure_emails': ['<mobile-build-failures@mozilla.org>'],
    },
    'mozilla-release': {
        'tinderbox_tree': 'Mozilla-Release',
        'mobile_tinderbox_tree': 'Mozilla-Release',
    },
    'mozilla-esr38': {
        'tinderbox_tree': 'Mozilla-Esr38',
        'mobile_tinderbox_tree': 'Mozilla-Esr38',
    },
    'mozilla-esr45': {
        'tinderbox_tree': 'Mozilla-Esr45',
        'mobile_tinderbox_tree': 'Mozilla-Esr45',
    },
    'mozilla-b2g44_v2_5': {
        'tinderbox_tree': 'Mozilla-B2g44-v2.5',
        'mobile_tinderbox_tree': 'Mozilla-B2g44-v2.5',
    },
    'mozilla-beta': {
        'tinderbox_tree': 'Mozilla-Beta',
        'mobile_tinderbox_tree': 'Mozilla-Beta',
    },
    'mozilla-aurora': {
        'tinderbox_tree': 'Mozilla-Aurora',
        'mobile_tinderbox_tree': 'Mozilla-Aurora',
    },
    'try': {
        'tinderbox_tree': 'Try',
        'stage_server': 'upload.trybld.productdelivery.prod.mozaws.net',
        'mobile_tinderbox_tree': 'Try',
        'download_base_url': 'https://ftp-ssl.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'mobile_download_base_url': 'https://ftp-ssl.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'package_url': 'https://archive.mozilla.org/pub/firefox/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'relengweb1.dmz.scl3.mozilla.com',
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
        'scripts_repo': 'https://hg.mozilla.org/build/tools',
        'lithium_repo': 'https://git.mozilla.org/mozsec/lithium.git',
        'funfuzz_repo': 'https://git.mozilla.org/mozsec/funfuzz.git',
        'fuzzmanager_repo': 'https://git.mozilla.org/mozsec/FuzzManager.git',
        'funfuzz_private_repo': 'git+ssh://git.mozilla.org/private/funfuzz-private.git',
        'fuzzing_remote_host': 'ffxbld@pvtbuilds2.dmz.scl3.mozilla.com',
        # Path needs extra leading slash due to optparse expansion on Win32
        'fuzzing_base_dir': '//mnt/pvt_builds/fuzzing/',
        # This is # of idle slaves per master
        'idle_slaves': 2,
    },
}

BRANCH_PROJECTS = {
    'spidermonkey_tier_1': {
        'scripts_repo': 'https://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
    },
    'spidermonkey_try': {
        'scripts_repo': 'https://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
    },
    'spidermonkey_info': {
        'scripts_repo': 'https://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
    },
}

if __name__ == "__main__":
    import sys
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
