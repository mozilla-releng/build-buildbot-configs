# -*- python -*-
# ex: set syntax=python:

import config
reload(config)

import buildbotcustom.env
reload(buildbotcustom.env)
from buildbotcustom.env import MozillaEnvironments

OBJDIR = 'objdir'
SBOX_HOME = '/scratchbox/users/cltbld/home/cltbld'

mobile_slaves = {
    'linux-gnueabi-arm': config.SLAVES['linux'],
    'linux-i686': config.SLAVES['linux'],
    'macosx-i686': config.SLAVES['macosx'],
    'winmo-arm': config.SLAVES['win32'],
    'win32-i686': config.SLAVES['win32'],
}

MOBILE_BRANCHES = {
    'mobile-trunk': {},
    'mobile-1.9.2': {},
    'mobile-tracemonkey': {},
    'mobile-electrolysis': {},
    'mobile-lorentz': {},
    'mobile-addonsmgr': {},
}

### mozilla-central
MOBILE_BRANCHES['mobile-trunk']['main_config'] = config.BRANCHES['mozilla-central']
MOBILE_BRANCHES['mobile-trunk']['repo_path'] = 'mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['l10n_repo_path'] = 'l10n-central'
MOBILE_BRANCHES['mobile-trunk']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-trunk']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-trunk']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-trunk']['aus2_base_upload_dir'] = '/opt/aus2/build/0/{a23983c0-fd0e-11dc-95ff-0800200c9a66}/mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['download_base_url'] = 'http://staging-stage.build.mozilla.org/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-trunk']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-trunk']['platforms'] = {
    'linux-gnueabi-arm': {},
    'linux-i686': {},
    'macosx-i686': {},
    'win32-i686': {},
    'winmo-arm': {},
}
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms'] = {}
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['mozconfig'] = 'linux/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['mozconfig'] = 'macosx/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['mozconfig'] = 'win32/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-trunk/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['base_name'] = 'Maemo mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_name'] = 'OS X Fennec Desktop mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_name'] = 'Win32 Fennec Desktop mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['base_name'] = 'WinMo mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build/maemo-trunk' % SBOX_HOME
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-trunk'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['base_l10n_workdir'] = '%s/build/maemo-trunk-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_l10n_workdir'] = 'build/macosx-fennec-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_builddir'] = 'w32mob-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_l10n_workdir'] = 'w32mob-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['base_builddir'] = 'winmo-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['base_l10n_workdir'] = 'winmo-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-trunk']['enable_l10n_onchange'] = True
MOBILE_BRANCHES['mobile-trunk']['enable_multi_locale'] = True
MOBILE_BRANCHES['mobile-trunk']['l10n_tree'] = 'fennec10x_mc'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['linux-gnueabi-arm'] = 'linux'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['linux-i686'] = 'linux'
#MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['macosx-i686'] = 'macosx'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['win32-i686'] = 'win32'
MOBILE_BRANCHES['mobile-trunk']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-trunk']['multiLocalesFile'] = "locales/maemo-locales"
MOBILE_BRANCHES['mobile-trunk']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/mobile/nightly/latest-mobile-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-trunk']['download_base_url'] + '/nightly/latest-mobile-trunk'
MOBILE_BRANCHES['mobile-trunk']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-trunk']['l10n_tinderbox_tree'] = 'MozillaStaging'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['slaves'] = mobile_slaves['linux-gnueabi-arm']
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['slaves'] = mobile_slaves['linux-i686']
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['slaves'] = mobile_slaves['macosx-i686']
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['slaves'] = mobile_slaves['win32-i686']
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['slaves'] = mobile_slaves['winmo-arm']
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['env'] = {}
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['env'] = {}
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['env'] = {
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['env'] = {}
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['create_snippet'] = False

### mobile-1.9.2
MOBILE_BRANCHES['mobile-1.9.2']['main_config'] = config.BRANCHES['mozilla-1.9.2']
MOBILE_BRANCHES['mobile-1.9.2']['repo_path'] = 'releases/mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-1.9.2']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-1.9.2']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-1.9.2']['aus2_base_upload_dir'] = '/opt/aus2/build/0/{a23983c0-fd0e-11dc-95ff-0800200c9a66}/mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['download_base_url'] = 'http://staging-stage.build.mozilla.org/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-1.9.2']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-1.9.2']['platforms'] = {
    'linux-gnueabi-arm': {},
    'linux-i686': {},
    'macosx-i686': {},
    'win32-i686': {},
    'winmo-arm': {},
}
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms'] = {}
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['mozconfig'] = 'linux/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['mozconfig'] = 'macosx/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['mozconfig'] = 'win32/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-1.9.2/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['base_name'] = 'Maemo mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_name'] = 'OS X Fennec Desktop mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_name'] = 'Win32 Fennec Desktop mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['base_name'] = 'WinMo mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build/maemo-1.9.2' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-1.9.2'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['base_l10n_workdir'] = '%s/build/maemo-1.9.2-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_l10n_workdir'] = 'build/macosx-fennec-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_builddir'] = 'w32mob-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_l10n_workdir'] = 'w32mob-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['base_builddir'] = 'winmo-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['base_l10n_workdir'] = 'winmo-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-1.9.2']['enable_l10n_onchange'] = True
MOBILE_BRANCHES['mobile-1.9.2']['enable_multi_locale'] = True
MOBILE_BRANCHES['mobile-1.9.2']['l10n_tree'] = 'fennec10x_192'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['linux-gnueabi-arm'] = 'linux'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['linux-i686'] = 'linux'
#MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['macosx-i686'] = 'macosx'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['win32-i686'] = 'win32'
MOBILE_BRANCHES['mobile-1.9.2']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-1.9.2']['multiLocalesFile'] = "locales/maemo-locales"
MOBILE_BRANCHES['mobile-1.9.2']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/mobile/nightly/latest-mobile-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_tinderbox_tree'] = 'MozillaStaging'
MOBILE_BRANCHES['mobile-1.9.2']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-1.9.2']['download_base_url'] + '/nightly/latest-mobile-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['slaves'] = mobile_slaves['linux-gnueabi-arm']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['slaves'] = mobile_slaves['linux-i686']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['slaves'] = mobile_slaves['macosx-i686']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['slaves'] = mobile_slaves['win32-i686']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['slaves'] = mobile_slaves['winmo-arm']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['env'] = {}
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['env'] = {}
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['env'] = {
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['env'] = {}
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['create_snippet'] = True

### mobile-tracemonkey
MOBILE_BRANCHES['mobile-tracemonkey']['main_config'] = config.BRANCHES['tracemonkey']
MOBILE_BRANCHES['mobile-tracemonkey']['repo_path'] = 'tracemonkey'
MOBILE_BRANCHES['mobile-tracemonkey']['l10n_repo_path'] = 'l10n-central'
MOBILE_BRANCHES['mobile-tracemonkey']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-tracemonkey']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-tracemonkey']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-tracemonkey']['aus2_base_upload_dir'] = None
MOBILE_BRANCHES['mobile-tracemonkey']['download_base_url'] = 'http://staging-stage.build.mozilla.org/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-tracemonkey']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms'] = {
    'linux-gnueabi-arm': {},
    'winmo-arm': {},
}
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-trunk/nightly'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['base_name'] = 'Maemo Tracemonkey'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['base_name'] = 'WinMo Tracemonkey'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build/maemo-tracemonkey' % SBOX_HOME
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-tracemonkey'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['base_builddir'] = 'winmo-tm'
MOBILE_BRANCHES['mobile-tracemonkey']['enable_l10n'] = False
MOBILE_BRANCHES['mobile-tracemonkey']['enable_l10n_onchange'] = False
MOBILE_BRANCHES['mobile-tracemonkey']['enable_multi_locale'] = False
MOBILE_BRANCHES['mobile-tracemonkey']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['slaves'] = mobile_slaves['linux-gnueabi-arm']
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['slaves'] = mobile_slaves['winmo-arm']
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['env'] = {}
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['winmo-arm']['create_snippet'] = False

### electrolysis
MOBILE_BRANCHES['mobile-electrolysis']['main_config'] = config.BRANCHES['electrolysis']
MOBILE_BRANCHES['mobile-electrolysis']['repo_path'] = 'projects/electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['l10n_repo_path'] = 'l10n-central'
MOBILE_BRANCHES['mobile-electrolysis']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-electrolysis']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-electrolysis']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-electrolysis']['aus2_base_upload_dir'] = None
MOBILE_BRANCHES['mobile-electrolysis']['download_base_url'] = 'http://staging-stage.build.mozilla.org/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-electrolysis']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-electrolysis']['platforms'] = {
    'linux-gnueabi-arm': {},
    'linux-i686': {},
    'winmo-arm': {},
}
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['mozconfig'] = 'linux/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-trunk/nightly'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['base_name'] = 'Maemo electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['base_name'] = 'WinMo electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build/maemo-electrolysis' % SBOX_HOME
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-electrolysis'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['base_l10n_workdir'] = '%s/build/maemo-electrolysis-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-electrolysis'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-electrolysis-l10n'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['base_builddir'] = 'winmo-electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['base_l10n_workdir'] = 'winmo-electrolysis-l10n'
MOBILE_BRANCHES['mobile-electrolysis']['enable_l10n'] = False
MOBILE_BRANCHES['mobile-electrolysis']['enable_l10n_onchange'] = False
MOBILE_BRANCHES['mobile-electrolysis']['enable_multi_locale'] = False
MOBILE_BRANCHES['mobile-electrolysis']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-electrolysis']['download_base_url'] + '/nightly/latest-mobile-electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['slaves'] = mobile_slaves['linux-gnueabi-arm']
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['slaves'] = mobile_slaves['linux-i686']
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['slaves'] = mobile_slaves['winmo-arm']
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['env'] = {}
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['env'] = {}
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['create_snippet'] = False

### mobile-lorentz
MOBILE_BRANCHES['mobile-lorentz']['main_config'] = config.BRANCHES['firefox-lorentz']
MOBILE_BRANCHES['mobile-lorentz']['repo_path'] = 'projects/firefox-lorentz'
MOBILE_BRANCHES['mobile-lorentz']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
MOBILE_BRANCHES['mobile-lorentz']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-lorentz']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-lorentz']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-lorentz']['aus2_base_upload_dir'] = '/opt/aus2/build/0/{a23983c0-fd0e-11dc-95ff-0800200c9a66}/lorentz'
MOBILE_BRANCHES['mobile-lorentz']['download_base_url'] = 'http://staging-stage.build.mozilla.org/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-lorentz']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-lorentz']['platforms'] = {
    'linux-gnueabi-arm': {},
    'linux-i686': {},
    'macosx-i686': {},
    'win32-i686': {},
    'winmo-arm': {},
}
MOBILE_BRANCHES['mobile-lorentz']['l10n_platforms'] = {}
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['mozconfig'] = 'linux/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['mozconfig'] = 'macosx/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['mozconfig'] = 'win32/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-lorentz/nightly'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['base_name'] = 'Maemo lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['base_name'] = 'OS X Fennec Desktop lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['base_name'] = 'Win32 Fennec Desktop lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['base_name'] = 'WinMo lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['builds_before_reboot'] = 1
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['builds_before_reboot'] = 1
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['builds_before_reboot'] = 1
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['builds_before_reboot'] = 1
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['builds_before_reboot'] = 1
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build/maemo-lorentz' % SBOX_HOME
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-lorentz'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['base_l10n_workdir'] = '%s/build/maemo-lorentz-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-lorentz-l10n'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['base_l10n_workdir'] = 'build/macosx-fennec-lorentz-l10n'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['base_builddir'] = 'w32mob-lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['base_l10n_workdir'] = 'w32mob-lorentz-l10n'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['base_builddir'] = 'winmo-lorentz'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['base_l10n_workdir'] = 'winmo-lorentz-l10n'
MOBILE_BRANCHES['mobile-lorentz']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-lorentz']['enable_l10n_onchange'] = True
MOBILE_BRANCHES['mobile-lorentz']['enable_multi_locale'] = True
MOBILE_BRANCHES['mobile-lorentz']['l10n_tree'] = 'fennec10x_192'
MOBILE_BRANCHES['mobile-lorentz']['l10n_platforms']['linux-gnueabi-arm'] = 'linux'
MOBILE_BRANCHES['mobile-lorentz']['l10n_platforms']['linux-i686'] = 'linux'
#MOBILE_BRANCHES['mobile-lorentz']['l10n_platforms']['macosx-i686'] = 'macosx'
MOBILE_BRANCHES['mobile-lorentz']['l10n_platforms']['win32-i686'] = 'win32'
MOBILE_BRANCHES['mobile-lorentz']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-lorentz']['multiLocalesFile'] = "locales/maemo-locales"
MOBILE_BRANCHES['mobile-lorentz']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/mobile/nightly/latest-mobile-lorentz-l10n'
MOBILE_BRANCHES['mobile-lorentz']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-lorentz']['download_base_url'] + '/nightly/latest-mobile-lorentz'
MOBILE_BRANCHES['mobile-lorentz']['tinderbox_tree'] = 'Firefox-Lorentz'
MOBILE_BRANCHES['mobile-lorentz']['l10n_tinderbox_tree'] = 'Mozilla-l10n'
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['slaves'] = mobile_slaves['linux-gnueabi-arm']
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['slaves'] = mobile_slaves['linux-i686']
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['slaves'] = mobile_slaves['macosx-i686']
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['slaves'] = mobile_slaves['win32-i686']
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['slaves'] = mobile_slaves['winmo-arm']
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-gnueabi-arm']['env'] = {}
MOBILE_BRANCHES['mobile-lorentz']['platforms']['linux-i686']['env'] = {}
MOBILE_BRANCHES['mobile-lorentz']['platforms']['macosx-i686']['env'] = {
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
MOBILE_BRANCHES['mobile-lorentz']['platforms']['win32-i686']['env'] = {}
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']
MOBILE_BRANCHES['mobile-lorentz']['platforms']['winmo-arm']['create_snippet'] = False

### mozilla-addonsmgr
MOBILE_BRANCHES['mobile-addonsmgr']['main_config'] = config.BRANCHES['addonsmgr']
MOBILE_BRANCHES['mobile-addonsmgr']['repo_path'] = 'projects/addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['l10n_repo_path'] = 'l10n-central'
MOBILE_BRANCHES['mobile-addonsmgr']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-addonsmgr']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-addonsmgr']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-addonsmgr']['aus2_base_upload_dir'] = '/opt/aus2/build/0/{a23983c0-fd0e-11dc-95ff-0800200c9a66}/addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['download_base_url'] = 'http://staging-stage.build.mozilla.org/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-addonsmgr']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms'] = {
    'linux-gnueabi-arm': {},
    'linux-i686': {},
    'macosx-i686': {},
    'win32-i686': {},
    'winmo-arm': {},
}
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['mozconfig'] = 'linux/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['mozconfig'] = 'macosx/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['mozconfig'] = 'win32/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-addonsmgr/nightly'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['base_name'] = 'Maemo Addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop Addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['base_name'] = 'OS X Fennec Desktop Addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['base_name'] = 'Win32 Fennec Desktop Addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['base_name'] = 'WinMo Addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build/maemo-addonsmgr' % SBOX_HOME
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-addonsmgr'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['base_l10n_workdir'] = '%s/build/maemo-addonsmgr-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-addonsmgr-l10n'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['base_l10n_workdir'] = 'build/macosx-fennec-addonsmgr-l10n'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['base_builddir'] = 'w32mob-addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['base_l10n_workdir'] = 'w32mob-addonsmgr-l10n'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['base_builddir'] = 'winmo-addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['base_l10n_workdir'] = 'winmo-addonsmgr-l10n'
MOBILE_BRANCHES['mobile-addonsmgr']['enable_l10n'] = False
MOBILE_BRANCHES['mobile-addonsmgr']['enable_l10n_onchange'] = False
MOBILE_BRANCHES['mobile-addonsmgr']['enable_multi_locale'] = False
MOBILE_BRANCHES['mobile-addonsmgr']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-addonsmgr']['download_base_url'] + '/nightly/latest-mobile-addonsmgr'
MOBILE_BRANCHES['mobile-addonsmgr']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['slaves'] = mobile_slaves['linux-gnueabi-arm']
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['slaves'] = mobile_slaves['linux-i686']
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['slaves'] = mobile_slaves['macosx-i686']
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['slaves'] = mobile_slaves['win32-i686']
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['slaves'] = mobile_slaves['winmo-arm']
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-gnueabi-arm']['env'] = {}
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['linux-i686']['env'] = {}
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['macosx-i686']['env'] = {
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['win32-i686']['env'] = {}
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']
MOBILE_BRANCHES['mobile-addonsmgr']['platforms']['winmo-arm']['create_snippet'] = False
