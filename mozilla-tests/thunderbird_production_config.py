from copy import deepcopy

from production_config import \
    GLOBAL_VARS, SLAVES, TRY_SLAVES, GRAPH_CONFIG


GLOBAL_VARS = deepcopy(GLOBAL_VARS)

GLOBAL_VARS['stage_username'] = 'tbirdbld'
GLOBAL_VARS['stage_ssh_key'] = 'tbirdbld_dsa'

# Local branch overrides
BRANCHES = {
    'comm-central': {
        'tinderbox_tree': 'Thunderbird',
    },
    'comm-esr38': {
        'tinderbox_tree': 'Thunderbird-Esr38',
    },
    'comm-esr45': {
        'tinderbox_tree': 'Thunderbird-Esr45',
    },
    'comm-beta': {
        'tinderbox_tree': 'Thunderbird-Beta',
    },
    'comm-aurora': {
        'tinderbox_tree': 'Thunderbird-Aurora',
    },
    'try-comm-central': {
        'tinderbox_tree': 'Try-Comm-Central',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'enable_merging': False,
        'slave_key': 'try_slaves',
        'package_url': 'https://archive.mozilla.org/pub/thunderbird/try-builds',
        'package_dir': '%(who)s-%(got_revision)s/',
        'stage_username': 'tbirdbld',
        'stage_ssh_key': 'tbirdbld_dsa',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
B2G_PROJECTS = {}
