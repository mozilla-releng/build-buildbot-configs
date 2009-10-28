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
}

### mozilla-central
MOBILE_BRANCHES['mobile-trunk']['main_config'] = config.BRANCHES['mozilla-central']
MOBILE_BRANCHES['mobile-trunk']['repo_path'] = 'mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['l10n_repo_path'] = 'l10n-central'
MOBILE_BRANCHES['mobile-trunk']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-trunk']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-trunk']['app_name'] = 'mobile'
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
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-browser/nightly'
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
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build' % SBOX_HOME
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-gnueabi-arm']['base_l10n_workdir'] = '%s/l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_l10n_workdir'] = 'l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_l10n_workdir'] = 'l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_builddir'] = 'w32mob-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_l10n_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['base_builddir'] = 'winmo-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['base_l10n_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-trunk']['l10n_tree'] = 'fennec10x_mc'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['linux-gnueabi-arm'] = 'linux'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['linux-i686'] = 'linux'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['macosx-i686'] = 'macosx'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['win32-i686'] = 'win32'
MOBILE_BRANCHES['mobile-trunk']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-trunk']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mobile-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['enUS_binaryURL'] = \
    config.BRANCHES['mozilla-central']['download_base_url'] + '/nightly/latest-mobile-trunk'
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
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['env'] = MozillaEnvironments['win32-fennec']
MOBILE_BRANCHES['mobile-trunk']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']



### mobile-1.9.2
MOBILE_BRANCHES['mobile-1.9.2']['main_config'] = config.BRANCHES['mozilla-1.9.2']
MOBILE_BRANCHES['mobile-1.9.2']['repo_path'] = 'releases/mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-1.9.2']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-1.9.2']['app_name'] = 'mobile'
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
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-browser/nightly'
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
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-gnueabi-arm']['base_l10n_workdir'] = '%s/l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_l10n_workdir'] = 'l10n'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_l10n_workdir'] = 'l10n'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_builddir'] = 'w32mob-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_l10n_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['base_builddir'] = 'winmo-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['base_l10n_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.2']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-1.9.2']['l10n_tree'] = 'fennec10x_192'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['linux-gnueabi-arm'] = 'linux'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['linux-i686'] = 'linux'
#MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['macosx-i686'] = 'macosx'
#MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['win32-i686'] = 'win32'
MOBILE_BRANCHES['mobile-1.9.2']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-1.9.2']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mobile-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['enUS_binaryURL'] = \
    config.BRANCHES['mozilla-central']['download_base_url'] + '/nightly/latest-mobile-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_tinderbox_tree'] = 'MozillaStaging'
MOBILE_BRANCHES['mobile-1.9.2']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-1.9.2']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mobile-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-1.9.2']['main_config']['download_base_url'] + '/nightly/latest-mobile-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_tinderbox_tree'] = 'MozillaStaging'
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
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['env'] = MozillaEnvironments['win32-fennec']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']

### mobile-tracemonkey
MOBILE_BRANCHES['mobile-tracemonkey']['main_config'] = config.BRANCHES['tracemonkey']
MOBILE_BRANCHES['mobile-tracemonkey']['repo_path'] = 'tracemonkey'
MOBILE_BRANCHES['mobile-tracemonkey']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-tracemonkey']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-tracemonkey']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms'] = {
    'linux-gnueabi-arm': {},
}
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['base_name'] = 'Maemo Tracemonkey'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build' % SBOX_HOME
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-tracemonkey'
MOBILE_BRANCHES['mobile-tracemonkey']['enable_l10n'] = False
MOBILE_BRANCHES['mobile-tracemonkey']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['slaves'] = mobile_slaves['linux-gnueabi-arm']
MOBILE_BRANCHES['mobile-tracemonkey']['platforms']['linux-gnueabi-arm']['env'] = {}

### electrolysis
MOBILE_BRANCHES['mobile-electrolysis']['main_config'] = config.BRANCHES['electrolysis']
MOBILE_BRANCHES['mobile-electrolysis']['repo_path'] = 'projects/electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-electrolysis']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-electrolysis']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-electrolysis']['platforms'] = {
    'linux-gnueabi-arm': {},
    'linux-i686': {},
    'winmo-arm': {},
}
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['mozconfig'] = 'linux/mobile-desktop/nightly'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['mozconfig'] = 'winmo/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['base_name'] = 'Maemo electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['base_name'] = 'WinMo electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['base_workdir'] = '%s/build' % SBOX_HOME
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['base_builddir'] = 'maemo-electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['base_l10n_workdir'] = '%s/l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['base_l10n_workdir'] = 'l10n'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['base_builddir'] = 'winmo-electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['base_l10n_workdir'] = '.'
MOBILE_BRANCHES['mobile-electrolysis']['enable_l10n'] = False
MOBILE_BRANCHES['mobile-electrolysis']['enUS_binaryURL'] = \
    config.BRANCHES['electrolysis']['download_base_url'] + '/nightly/latest-mobile-electrolysis'
MOBILE_BRANCHES['mobile-electrolysis']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['slaves'] = mobile_slaves['linux-gnueabi-arm']
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['slaves'] = mobile_slaves['linux-i686']
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['slaves'] = mobile_slaves['winmo-arm']
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-gnueabi-arm']['env'] = {}
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['linux-i686']['env'] = {}
MOBILE_BRANCHES['mobile-electrolysis']['platforms']['winmo-arm']['env'] = MozillaEnvironments['winmo-arm']
