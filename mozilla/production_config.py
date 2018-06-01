MAC_LION_MINIS = ['bld-lion-r5-%03d' % x for x in range(1,7) + range(43,44) + range(50,54) + \
                  range(56,69) + range(70,72)]   # Omit 72 - Bug 1402830 // Omit 54 - Bug 1455729

WIN64_REV2     = ['b-2008-ec2-%04d' % x for x in range(1, 31)] + \
                 ['b-2008-spot-%03d' % x for x in range(1, 51) + range(101, 151)]

LINUX64_EC2    = ['bld-linux64-ec2-%03d' % x for x in range(1, 50) + range(301, 350)] + \
                 ['bld-linux64-spot-%03d' % x for x in range(1, 101) + range(300, 351)]

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
                  ['try-linux64-spot-%03d' % x for x in range(1, 11) + range(300,310)]
TRY_WIN64_REV2  = ['y-2008-ec2-%04d' % x for x in range(1, 31)] + \
                  ['y-2008-spot-%03d' % x for x in range(1, 81) + range(101, 120)]
TRY_LION        = ['bld-lion-r5-%03d' % x for x in range(8,10) + range(11,14) + range(15,23)] # Omit 7,10,14 and 28 for bld-lion-r5 // Bug 1402830

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
    'graph_server': None,
    'balrog_vpn_proxy': 'balrogVPNProxy',
    'balrog_api_root': 'https://aus4-admin.mozilla.org/api',
    # Used by special docker workers with balrogVpnProxy feature enabled
    'funsize_balrog_api_root': 'http://balrog/api',
    'balrog_username': 'balrog-ffxbld',
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
    'mozilla-esr52': {
        'tinderbox_tree': 'Mozilla-Esr52',
        'mobile_tinderbox_tree': 'Mozilla-Esr52',
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
    },
}

PLATFORM_VARS = {}

PROJECTS = {
}

BRANCH_PROJECTS = {
    'spidermonkey_tier_1': {
        'scripts_repo': 'https://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
    }
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
