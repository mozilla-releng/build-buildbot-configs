from copy import deepcopy

from staging_config import GLOBAL_VARS, SLAVES, TRY_SLAVES

GLOBAL_VARS = deepcopy(GLOBAL_VARS)

GLOBAL_VARS['disable_tinderbox_mail'] = True
GLOBAL_VARS['tinderbox_tree'] = 'ThunderbirdTest'
GLOBAL_VARS['stage_username'] = 'tbirdbld'
GLOBAL_VARS['stage_ssh_key'] = 'tbirdbld_dsa'

BRANCHES = {
    'try-comm-central': {
            'enable_mail_notifier': False, # Set to True when testing
            'email_override': [], # Set to your address when testing
            'package_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/thunderbird/try-builds',
            'package_dir': '%(who)s-%(got_revision)s',
            'stage_username': 'tbirdbld',
            'stage_ssh_key': 'tbirdbld_dsa',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
B2G_PROJECTS = {}
