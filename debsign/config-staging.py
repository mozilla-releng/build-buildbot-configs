SLAVES = {
    'linux': ['debsign1', 'debsign2'],
}

NIGHTLY_ENV = {
    'STAGE_USERNAME': 'cltbld',
    'STAGE_SERVER': 'staging-mobile-master.build.mozilla.org',
    'BASE_STAGE_PATH': '/var/www/html',
    'BASE_STAGE_URL': 'http://staging-mobile-master.build.mozilla.org',
    'STAGE_DIR': '/debtest',
    'SSH_KEY': '/home/cltbld/.ssh/id_rsa',
    'SIGNDEBS_BASEDIR': 'sign-debs-staging',
}

# Needed in staging only
NIGHTLY_TRIGGER_ENV = {
    'STAGE_USERNAME': 'ffxbld',
    'STAGE_SERVER': 'stage.mozilla.org',
    'SSH_KEY': '/home/cltbld/.ssh/ffxbld_dsa',
}

REAL_RELEASE_ENV = {
    'STAGE_USERNAME': 'cltbld',
    'STAGE_SERVER': 'staging-mobile-master.build.mozilla.org',
    'BASE_STAGE_PATH': '/var/www/html',
    'BASE_STAGE_URL': 'http://staging-mobile-master.build.mozilla.org/debtest',
    'STAGE_DIR': '/debtest',
    'SSH_KEY': '/home/cltbld/.ssh/id_rsa',
    'SIGNDEBS_BASEDIR': 'sign-debs-staging',
}
CANDIDATES_RELEASE_ENV = {
    'STAGE_USERNAME': 'cltbld',
    'STAGE_SERVER': 'staging-mobile-master.build.mozilla.org',
    'BASE_STAGE_PATH': '/var/www/html',
    'BASE_STAGE_URL': 'http://staging-mobile-master.build.mozilla.org',
    'STAGE_DIR': '/debtest/candidates',
    'SSH_KEY': '/home/cltbld/.ssh/id_rsa',
    'SIGNDEBS_BASEDIR': 'sign-debs-staging',
}


# Change for real release
RELEASE_ENV = CANDIDATES_RELEASE_ENV

DEBSIGN_CONFIG = {}
TRIGGER_CONFIG = {}

DEBSIGN_CONFIG['slaves'] = SLAVES['linux']
DEBSIGN_CONFIG['tools_repo_path'] = "http://hg.mozilla.org/build/tools"
DEBSIGN_CONFIG['branches'] = {
    'trunk': {},
    '1.9.2': {},
}
DEBSIGN_CONFIG['branches']['trunk']['nightly_base_stage_path'] = '/home/ftp'
DEBSIGN_CONFIG['branches']['trunk']['nightly_base_stage_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-trunk'
DEBSIGN_CONFIG['branches']['trunk']['nightly_stage_dir'] = '/pub/mozilla.org/firefox/nightly/latest-mobile-trunk'
DEBSIGN_CONFIG['branches']['trunk']['nightly_env'] = NIGHTLY_ENV
DEBSIGN_CONFIG['branches']['trunk']['enable_release'] = False
DEBSIGN_CONFIG['branches']['1.9.2']['nightly_base_stage_path'] = '/home/ftp'
DEBSIGN_CONFIG['branches']['1.9.2']['nightly_base_stage_url'] = 'http://ftp.mozilla.org'
DEBSIGN_CONFIG['branches']['1.9.2']['nightly_stage_dir'] = '/pub/mozilla.org/firefox/nightly/latest-mobile-1.9.2'
DEBSIGN_CONFIG['branches']['1.9.2']['nightly_env'] = NIGHTLY_ENV
DEBSIGN_CONFIG['branches']['1.9.2']['enable_release'] = True
DEBSIGN_CONFIG['branches']['trunk']['release_base_stage_path'] = '/var/www/html'
DEBSIGN_CONFIG['branches']['1.9.2']['release_base_stage_url'] = 'http://staging-mobile-master.build.mozilla.org'
DEBSIGN_CONFIG['branches']['1.9.2']['release_stage_dir'] = '/candidates/1.0rc2-candidates/build3/maemo'
DEBSIGN_CONFIG['branches']['1.9.2']['release_env'] = RELEASE_ENV

#
# Trigger config
#

TRIGGER_CONFIG['sendchange_master'] = "staging-mobile-master.build.mozilla.org:9011"
TRIGGER_CONFIG['branches'] = {
    'trunk': {},
    '1.9.2': {},
}
TRIGGER_CONFIG['branches']['trunk']['env'] = NIGHTLY_TRIGGER_ENV
TRIGGER_CONFIG['branches']['1.9.2']['env'] = NIGHTLY_TRIGGER_ENV
TRIGGER_CONFIG['branches']['1.9.2']['release_mobile_tag'] = 'FENNEC_1_0rc2_RELEASE'
TRIGGER_CONFIG['mobile_repo'] = 'http://hg.mozilla.org/mobile-browser'
TRIGGER_CONFIG['locales_file'] = 'mobile/locales/all-locales'
TRIGGER_CONFIG['conf_file'] = 'mobile/confvars.sh'
