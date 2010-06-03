SLAVES = {
    'linux': ['debsign1'],
}
NIGHTLY_ENV = {
    'STAGE_USERNAME': 'ffxbld',
    'STAGE_SERVER': 'stage.mozilla.org',
    'BASE_STAGE_PATH': '/home/ftp',
    'BASE_STAGE_URL': 'http://ftp.mozilla.org',
    'STAGE_DIR': '/pub/mozilla.org/mobile/repos',
    'SSH_KEY': '/home/cltbld/.ssh/ffxbld_dsa',
}
REAL_RELEASE_ENV = {
    'STAGE_USERNAME': 'ffxbld',
    'STAGE_SERVER': 'stage.mozilla.org',
    'BASE_STAGE_PATH': '/home/ftp',
    'BASE_STAGE_URL': 'http://ftp.mozilla.org',
    'STAGE_DIR': '/pub/mozilla.org/mobile/repos',
    'SSH_KEY': '/home/cltbld/.ssh/ffxbld_dsa',
}
CANDIDATES_RELEASE_ENV = {
    'STAGE_USERNAME': 'ffxbld',
    'STAGE_SERVER': 'stage.mozilla.org',
    'BASE_STAGE_PATH': '/home/ftp',
    'BASE_STAGE_URL': 'http://ftp.mozilla.org',
    'STAGE_DIR': '/pub/mozilla.org/mobile/candidates/1.1rc1-candidates/repos',
    'SSH_KEY': '/home/cltbld/.ssh/ffxbld_dsa',
}
 

# Change for real release
RELEASE_ENV = CANDIDATES_RELEASE_ENV

DEBSIGN_CONFIG = {}
TRIGGER_CONFIG = {}

DEBSIGN_CONFIG['slaves'] = SLAVES['linux']
DEBSIGN_CONFIG['tools_repo_path'] = "http://hg.mozilla.org/build/tools"
DEBSIGN_CONFIG['branches'] = {
    'trunk': {'nightly': {},
              'release': {}},
    '1.9.2': {'nightly': {},
              'release': {}},
}
DEBSIGN_CONFIG['branches']['trunk']['nightly']['base_stage_path'] = '/home/ftp'
DEBSIGN_CONFIG['branches']['trunk']['nightly']['base_stage_url'] = 'http://ftp.mozilla.org'
DEBSIGN_CONFIG['branches']['trunk']['nightly']['stage_dir'] = '/pub/mozilla.org/mobile/nightly/latest-mobile-trunk'
DEBSIGN_CONFIG['branches']['trunk']['nightly']['env'] = NIGHTLY_ENV
DEBSIGN_CONFIG['branches']['trunk']['nightly']['extra_debs_list'] = None
DEBSIGN_CONFIG['branches']['trunk']['enable_release'] = False
DEBSIGN_CONFIG['branches']['1.9.2']['nightly']['base_stage_path'] = '/home/ftp'
DEBSIGN_CONFIG['branches']['1.9.2']['nightly']['base_stage_url'] = 'http://ftp.mozilla.org'
DEBSIGN_CONFIG['branches']['1.9.2']['nightly']['stage_dir'] = '/pub/mozilla.org/mobile/nightly/latest-mobile-1.9.2'
DEBSIGN_CONFIG['branches']['1.9.2']['nightly']['env'] = NIGHTLY_ENV
DEBSIGN_CONFIG['branches']['1.9.2']['nightly']['extra_debs_list'] = None
DEBSIGN_CONFIG['branches']['1.9.2']['enable_release'] = True
DEBSIGN_CONFIG['branches']['1.9.2']['release']['base_stage_path'] = '/home/ftp'
DEBSIGN_CONFIG['branches']['1.9.2']['release']['base_stage_url'] = 'http://ftp.mozilla.org'
DEBSIGN_CONFIG['branches']['1.9.2']['release']['stage_dir'] = '/pub/mozilla.org/mobile/candidates/1.1rc1-candidates/build2/maemo4'
DEBSIGN_CONFIG['branches']['1.9.2']['release']['env'] = RELEASE_ENV
DEBSIGN_CONFIG['branches']['1.9.2']['release']['extra_debs_list'] = []

#
# Trigger config
#

TRIGGER_CONFIG['sendchange_master'] = "production-mobile-master.build.mozilla.org:9011"
TRIGGER_CONFIG['branches'] = {
    'trunk': {},
    '1.9.2': {},
}
TRIGGER_CONFIG['branches']['trunk']['env'] = NIGHTLY_ENV
TRIGGER_CONFIG['branches']['1.9.2']['env'] = NIGHTLY_ENV
TRIGGER_CONFIG['branches']['1.9.2']['release_mobile_tag'] = 'FENNEC_1_1rc1_RELEASE'
TRIGGER_CONFIG['mobile_repo'] = 'http://hg.mozilla.org/releases/mobile-1.1'
TRIGGER_CONFIG['locales_file'] = 'mobile/locales/all-locales'
