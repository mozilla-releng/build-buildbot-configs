from copy import deepcopy

from production_config import \
    GLOBAL_VARS, SLAVES, TRY_SLAVES, GRAPH_CONFIG


GLOBAL_VARS = deepcopy(GLOBAL_VARS)

GLOBAL_VARS['disable_tinderbox_mail'] = True
GLOBAL_VARS['stage_username'] = 'tbirdbld'
GLOBAL_VARS['stage_ssh_key'] = 'tbirdbld_dsa'

# Local branch overrides
BRANCHES = {
    'comm-central': {
        'tinderbox_tree': 'ThunderbirdTrunk',
    },
    'comm-release': {
        'tinderbox_tree': 'Thunderbird-Release',
    },
    'comm-esr10': {
        'tinderbox_tree': 'Thunderbird-Esr10',
    },
    'comm-beta': {
        'tinderbox_tree': 'Thunderbird-Beta',
    },
    'comm-aurora': {
        'tinderbox_tree': 'Thunderbird-Aurora',
    },
    'try-comm-central': {
        'tinderbox_tree': 'ThunderbirdTry',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'enable_merging': False,
        'slave_key': 'try_slaves',
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/thunderbird/try-builds',
        'package_dir': '%(who)s-%(got_revision)s',
        'stage_username': 'tbirdbld',
        'stage_ssh_key': 'tbirdbld_dsa',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}

