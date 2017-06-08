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
    'stage_server': 'upload.tbirdbld.productdelivery.prod.mozaws.net',
    'balrog_username': 'balrog-tbirdbld',
    'download_base_url': 'http://archive.mozilla.org/pub/thunderbird',
    'talos_masters': [],

    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('buildbot-master81.build.mozilla.org:9301', True, 5),
    ],

    'tooltool_url_list': ['https://api.pub.build.mozilla.org/tooltool/'],
})

# Local branch overrides
BRANCHES = {
    'comm-central': {
        'tinderbox_tree': 'Thunderbird',
    },
    'comm-esr45': {
        'tinderbox_tree': 'Thunderbird-Esr45',
    },
    'comm-esr52': {
        'tinderbox_tree': 'Thunderbird-Esr52',
    },
    'comm-beta': {
        'tinderbox_tree': 'Thunderbird-Beta',
    },
    'comm-aurora': {
        'tinderbox_tree': 'Thunderbird-Aurora',
    },
    'try-comm-central': {
        'stage_server': 'upload.trybld.productdelivery.prod.mozaws.net',
        'tinderbox_tree': 'Try-Comm-Central',
        'download_base_url': 'http://archive.mozilla.org/pub/thunderbird/try-builds',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'package_url': 'https://archive.mozilla.org/pub/thunderbird/try-builds',
        'talos_masters': [],
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
