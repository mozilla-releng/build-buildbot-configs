SLAVES = {
    'linux': ['debsign1'],
}

DEBSIGN_CONFIG = {}
TRIGGER_CONFIG = {}

DEBSIGN_CONFIG['slaves'] = SLAVES['linux']
DEBSIGN_CONFIG['tools_repo_path'] = "http://hg.mozilla.org/build/tools"
DEBSIGN_CONFIG['branches'] = {
    'trunk': {},
    '1.9.2': {},
}
DEBSIGN_CONFIG['branches']['trunk']['nightly_base_xulrunner_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-trunk'
DEBSIGN_CONFIG['branches']['1.9.2']['nightly_base_xulrunner_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-1.9.2'
DEBSIGN_CONFIG['env'] = {
    'STAGE_USERNAME': 'ffxbld',
    'STAGE_SERVER': 'stage.mozilla.org',
    'BASE_STAGE_PATH': '/home/ftp/pub/mozilla.org/mobile/repos',
    'BASE_STAGE_URL': 'http://ftp.mozilla.org/pub/mozilla.org/mobile/repos',
    'SSH_KEY': '/home/cltbld/.ssh/ffxbld_dsa',
}

TRIGGER_CONFIG['sendchange_master'] = "production-mobile-master.mv.mozilla.com:9011"
TRIGGER_CONFIG['branches'] = {
    'trunk': {},
    '1.9.2': {},
}
TRIGGER_CONFIG['nightly_base_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-'
TRIGGER_CONFIG['mobile_repo'] = 'http://hg.mozilla.org/mobile-browser'
TRIGGER_CONFIG['locales_file'] = 'mobile/locales/all-locales'
TRIGGER_CONFIG['conf_file'] = 'mobile/confvars.sh'
