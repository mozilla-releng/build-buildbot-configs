from localconfig import SLAVES

GLOBAL_VARS = {
    'staging': True,
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'upload.tbirdbld.productdelivery.stage.mozaws.net',
    'balrog_username': 'balrog-stage-tbirdbld',
    'download_base_url': 'http://ftp.stage.mozaws.net/pub/thunderbird',
    'graph_server': None,
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'https://api-pub-build.allizom.org/clobberer/lastclobber',
    'talos_masters': [],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('dev-master1.srv.releng.scl3.mozilla.com:9901', True, 1),
        ],
    'tinderbox_tree': 'ThunderbirdTest',
    'hg_username': 'stage-tbirdbld',

    'tooltool_url_list': ['https://api.pub.build.mozilla.org/tooltool/'],
}

BUILDS_BEFORE_REBOOT = 5

# Local branch overrides
BRANCHES = {
    'comm-central': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'comm-beta': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'comm-esr52': {
        'enable_blocklist_update': False,
        'file_update_on_closed_tree': False,
    },
    'try-comm-central': {
        # all try builds go via trybld hosts
        'stage_server': 'upload.trybld.productdelivery.stage.mozaws.net',
        'download_base_url': 'http://ftp.stage.mozaws.net/pub/thunderbird/try-builds',
        'enable_mail_notifier': False, # Set to True when testing
        'email_override': [], # Set to your address when testing
        'package_url': 'http://ftp.stage.mozaws.net/pub/thunderbird/try-builds',
        'talos_masters': [],
    },
}

PLATFORM_VARS = {
}

PROJECTS = {
}
