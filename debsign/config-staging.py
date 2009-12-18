SLAVES = {
    'linux': ['debsign1', 'debsign2'],
}
NIGHTLY_ENV = {
    'STAGE_USERNAME': 'cltbld',
    'STAGE_SERVER': 'staging-mobile-master.mv.mozilla.com',
    'BASE_STAGE_PATH': '/var/www/html/debtest',
    'BASE_STAGE_URL': 'http://staging-mobile-master.mv.mozilla.com/debtest',
    'SSH_KEY': '/home/cltbld/.ssh/id_rsa',
    'SIGNDEBS_BASEDIR': 'sign-debs-staging',
}

REAL_RELEASE_ENV = {
    'STAGE_USERNAME': 'cltbld',
    'STAGE_SERVER': 'staging-mobile-master.mv.mozilla.com',
    'BASE_STAGE_PATH': '/var/www/html/debtest',
    'BASE_STAGE_URL': 'http://staging-mobile-master.mv.mozilla.com/debtest',
    'SSH_KEY': '/home/cltbld/.ssh/id_rsa',
    'SIGNDEBS_BASEDIR': 'sign-debs-staging',
}
CANDIDATES_RELEASE_ENV = {
    'STAGE_USERNAME': 'cltbld',
    'STAGE_SERVER': 'staging-mobile-master.mv.mozilla.com',
    'BASE_STAGE_PATH': '/var/www/html/debtest/candidates',
    'BASE_STAGE_URL': 'http://staging-mobile-master.mv.mozilla.com/debtest/candidates',
    'SSH_KEY': '/home/cltbld/.ssh/id_rsa',
    'SIGNDEBS_BASEDIR': 'sign-debs-staging',
}


# Change for real release
RELEASE_ENV = CANDIDATES_RELEASE_ENV

DEBSIGN_CONFIG = {}
TRIGGER_CONFIG = {}

DEBSIGN_CONFIG['slaves'] = SLAVES['linux']
DEBSIGN_CONFIG['tools_repo_path'] = "http://hg.mozilla.org/users/asasaki_mozilla.com/test-tools"
DEBSIGN_CONFIG['branches'] = {
    'trunk': {},
    '1.9.2': {},
}
DEBSIGN_CONFIG['branches']['trunk']['nightly_base_xulrunner_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-trunk'
DEBSIGN_CONFIG['branches']['trunk']['nightly_env'] = NIGHTLY_ENV
DEBSIGN_CONFIG['branches']['trunk']['enable_release'] = False
DEBSIGN_CONFIG['branches']['1.9.2']['nightly_base_xulrunner_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-1.9.2'
DEBSIGN_CONFIG['branches']['1.9.2']['nightly_env'] = NIGHTLY_ENV
DEBSIGN_CONFIG['branches']['1.9.2']['enable_release'] = True
DEBSIGN_CONFIG['branches']['1.9.2']['release_base_xulrunner_url'] = 'http://staging-mobile-master.mv.mozilla.com/candidates/1.0-candidates/build1/maemo/multi'
DEBSIGN_CONFIG['branches']['1.9.2']['release_env'] = RELEASE_ENV

TRIGGER_CONFIG['sendchange_master'] = "staging-mobile-master.mv.mozilla.com:9011"
TRIGGER_CONFIG['branches'] = {
    'trunk': {},
    '1.9.2': {},
}
TRIGGER_CONFIG['nightly_base_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-'
TRIGGER_CONFIG['mobile_repo'] = 'http://hg.mozilla.org/mobile-browser'
TRIGGER_CONFIG['locales_file'] = 'mobile/locales/all-locales'
TRIGGER_CONFIG['conf_file'] = 'mobile/confvars.sh'

TRIGGER_CONFIG['release_base_url'] = 'http://staging-mobile-master.mv.mozilla.com/candidates/1.0-candidates/build1/maemo'
