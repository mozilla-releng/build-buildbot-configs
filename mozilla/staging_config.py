from copy import deepcopy
import production_config as pc
reload(pc)

# Import all of our slave information from production.
SLAVES = deepcopy(pc.SLAVES)
TRY_SLAVES = deepcopy(pc.TRY_SLAVES)

# Add a small stockpile of AWS dev instances.
LINUX64_EC2_DEV    = ['dev-linux64-ec2-%03d' % x for x in range(1, 50)]
SLAVES['mock'].extend(LINUX64_EC2_DEV)
TRY_SLAVES['mock'].extend(LINUX64_EC2_DEV)

LINUX64_AV_EC2_DEV = ['dev-av-linux64-ec2-001']
SLAVES['linux64-av'].extend(LINUX64_AV_EC2_DEV)

WIN64_RELOPS     = ['ix-mn-w0864-%03d' % x for x in range(1,3)]
SLAVES['win64-rev2'].extend(WIN64_RELOPS)
TRY_SLAVES['win64-rev2'].extend(WIN64_RELOPS)

# AWS EC2 (b|y)-2008 spot and on-demand staging instances.
B2008 = ['b-2008-spot-%03d' % x for x in range(990, 1000)] + \
        ['b-2008-ec2-%04d' % x for x in range(990, 1000)]
Y2008 = ['y-2008-spot-%03d' % x for x in range(990, 1000)] + \
        ['y-2008-ec2-%04d' % x for x in range(990, 1000)]
SLAVES['win64-rev2'].extend(B2008)
TRY_SLAVES['win64-rev2'].extend(Y2008)

GLOBAL_VARS = {
    'staging': True,
    'config_repo_path': 'users/stage-ffxbld/buildbot-configs',
    'buildbotcustom_repo_path': 'users/stage-ffxbld/buildbotcustom',
    'stage_server': 'upload.ffxbld.productdelivery.stage.mozaws.net',
    'download_base_url': 'http://ftp.stage.mozaws.net/pub/firefox',
    'mobile_download_base_url': 'http://ftp.stage.mozaws.net/pub/mobile',
    'graph_server': None,
    'balrog_vpn_proxy': 'balrogStageVPNProxy',
    'balrog_api_root': 'https://balrog-admin.stage.mozaws.net/api',
    # Used by special docker workers with balrogVpnProxy feature enabled
    'funsize_balrog_api_root': 'http://balrog/api',
    'balrog_username': 'balrog-stage-ffxbld',
    'build_tools_repo_path': 'users/stage-ffxbld/tools',
    'base_clobber_url': 'https://api-pub-build.allizom.org/clobberer/lastclobber',
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('dev-master1.srv.releng.scl3.mozilla.com:9901', True, 1),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('dev-master1.srv.releng.scl3.mozilla.com:9901', True, 1),
        ],
    'tinderbox_tree': 'MozillaTest',
    'mobile_tinderbox_tree': 'MobileTest',
    'hg_username': 'stage-ffxbld',
    'tooltool_url_list': ['https://api.pub.build.mozilla.org/tooltool/'],
    'blob_upload': True,
    'mozharness_configs': {
        'balrog': 'balrog/staging.py',
        'single_locale_environment': 'single_locale/staging.py',
    },
    'bucket_prefix': 'net-mozaws-stage-delivery',
}

BUILDS_BEFORE_REBOOT = 5

# Local branch overrides
BRANCHES = {
    'mozilla-esr52': {
        'enable_blocklist_update': False,
        'enable_hsts_update': False,
        'enable_hpkp_update': False,
        'file_update_on_closed_tree': False,
    },
    'try': {
        'enable_mail_notifier': False, # Set to True when testing
        'email_override': [], # Set to your address when testing
        'package_url': 'http://ftp.stage.mozaws.net/pub/firefox/try-builds',
        'talos_masters': [],
    },
}

PLATFORM_VARS = {}

PROJECTS = {}

BRANCH_PROJECTS = {
    'spidermonkey_tier_1': {
        'scripts_repo': 'https://hg.mozilla.org/users/stage-ffxbld/tools',
        'idle_slaves': 0,
    }
}
