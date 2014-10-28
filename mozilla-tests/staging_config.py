from copy import deepcopy
import production_config as pc

SLAVES = deepcopy(pc.SLAVES)
TRY_SLAVES = deepcopy(SLAVES)

GRAPH_CONFIG = ['--resultsServer', 'graphs.allizom.org',
    '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'disable_tinderbox_mail': True,
    'tinderbox_tree': 'MozillaTest',
    'mobile_tinderbox_tree': 'MobileTest',
    'build_tools_repo_path': 'build/tools',
    'mozharness_repo': 'https://hg.mozilla.org/build/mozharness',
    'mozharness_tag': 'production',
    'stage_server': 'dev-stage01.srv.releng.scl3.mozilla.com',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_rsa',
    'datazilla_url': 'https://datazilla.mozilla.org/test',
    'blob_upload': True,
}

BRANCHES = {
        'try': {
            'enable_mail_notifier': False, # Set to True when testing
            'email_override': [], # Set to your address when testing
            'package_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/firefox/try-builds',
            'package_dir': '%(who)s-%(got_revision)s',
            'stage_username': 'trybld',
            'stage_ssh_key': 'trybld_dsa',
        },
}

PLATFORM_VARS = {
}

PROJECTS = {
    'jetpack': {
        'scripts_repo': 'https://hg.mozilla.org/build/tools',
        'tinderbox_tree': 'MozillaTest',
    },
}
B2G_PROJECTS = {}
