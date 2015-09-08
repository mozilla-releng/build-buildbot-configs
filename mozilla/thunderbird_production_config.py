from copy import deepcopy

from localconfig import \
    GLOBAL_VARS, MAC_LION_MINIS, \
    LINUX64_EC2, \
    TRY_MAC64, \
    TRY_LION, WIN64_REV2, TRY_WIN64_REV2, \
    TRY_LINUX64_EC2, \
    BUILDS_BEFORE_REBOOT, SYMBOL_SERVER_HOST

GLOBAL_VARS = deepcopy(GLOBAL_VARS)

SLAVES = {
    'win64-rev2':       WIN64_REV2,
    'macosx64-lion':    MAC_LION_MINIS,
    'mock':             LINUX64_EC2,
}

TRY_SLAVES = {
    'win64-rev2':  TRY_WIN64_REV2,
    'macosx64':    TRY_MAC64,
    'macosx64-lion': TRY_LION,
    'mock':        TRY_LINUX64_EC2,
}

# Local overrides for default values
GLOBAL_VARS.update({
    'balrog_username': 'tbirdbld',
    'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/thunderbird',
    'talos_masters': [],

    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('buildbot-master81.build.mozilla.org:9301', True, 5),
    ],
    'xulrunner_tinderbox_tree': None,
    'weekly_tinderbox_tree': 'Thunderbird',
    'l10n_tinderbox_tree': 'Mozilla-l10n',
    'base_bundle_urls': ['https://ftp-ssl.mozilla.org/pub/mozilla.org/thunderbird/bundles'],

    'tooltool_url_list': ['https://api.pub.build.mozilla.org/tooltool/'],
})

# Local branch overrides
BRANCHES = {
    'comm-central': {
        'packaged_unittest_tinderbox_tree': 'Thunderbird',
        'tinderbox_tree': 'Thunderbird',
    },
    'comm-esr38': {
        'packaged_unittest_tinderbox_tree': 'Thunderbird-Esr38',
        'tinderbox_tree': 'Thunderbird-Esr38',
    },
    'comm-beta': {
        'packaged_unittest_tinderbox_tree': 'Thunderbird-Beta',
        'tinderbox_tree': 'Thunderbird-Beta',
    },
    'comm-aurora': {
        'packaged_unittest_tinderbox_tree': 'Thunderbird-Aurora',
        'tinderbox_tree': 'Thunderbird-Aurora',
    },
    'try-comm-central': {
        'tinderbox_tree': 'Try-Comm-Central',
        'packaged_unittest_tinderbox_tree': 'Try-Comm-Central',
        'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/thunderbird/try-builds',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'package_url': 'https://ftp-ssl.mozilla.org/pub/mozilla.org/thunderbird/try-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'build.mozilla.org',
                    'MOZ_OBJDIR': 'objdir-tb',
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

PROJECTS = {}
