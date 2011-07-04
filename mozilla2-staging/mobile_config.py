# -*- python -*-
# ex: set syntax=python:

from copy import deepcopy
import re

import config
reload(config)

OBJDIR = 'objdir'
SBOX_HOME = '/scratchbox/users/cltbld/home/cltbld'

MOBILE_SLAVES = {
    'maemo4': config.SLAVES['linux'],
    'maemo5-gtk': config.SLAVES['linux'],
    'maemo5-qt': config.SLAVES['linux'],
    'linux-i686': config.SLAVES['linux'],
    'macosx-i686': config.SLAVES['macosx'],
    'win32-i686': config.SLAVES['win32'],
    'android-r7': config.SLAVES['linux'],
}

MOBILE_BRANCHES = {
    'mobile-trunk': {},
    'mobile-2.0': {},
    'mozilla-mobile-5.0': {},
    'mobile-1.9.2': {},
}

DEFAULT_ENV = {
    'SYMBOL_SERVER_HOST': 'dev-stage01.build.sjc1.mozilla.com',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_mob/',
    'POST_SYMBOL_UPLOAD_CMD': '/usr/local/bin/post-symbol-upload.py',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'TINDERBOX_OUTPUT': '1',
}
DEFAULT_LINUX_ENV = DEFAULT_ENV.copy()
DEFAULT_LINUX_ENV['SYMBOL_SERVER_SSH_KEY'] = '/home/cltbld/.ssh/ffxbld_dsa'
DEFAULT_MACOSX_ENV = DEFAULT_ENV.copy()
DEFAULT_MACOSX_ENV['SYMBOL_SERVER_SSH_KEY'] = '/Users/cltbld/.ssh/ffxbld_dsa'
DEFAULT_MACOSX_ENV['CHOWN_ROOT'] = '~/bin/chown_root'
DEFAULT_MACOSX_ENV['CHOWN_REVERT'] = '~/bin/chown_revert'
DEFAULT_WIN32_ENV = DEFAULT_ENV.copy()
DEFAULT_WIN32_ENV['SYMBOL_SERVER_SSH_KEY'] = '/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa'

### mozilla-central
MOBILE_BRANCHES['mobile-trunk']['main_config'] = config.BRANCHES['mozilla-central']
MOBILE_BRANCHES['mobile-trunk']['repo_path'] = 'mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['l10n_repo_path'] = 'l10n-central'
MOBILE_BRANCHES['mobile-trunk']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-trunk']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-trunk']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-trunk']['aus2_base_upload_dir'] = '/opt/aus2/build/0/{a23983c0-fd0e-11dc-95ff-0800200c9a66}/mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['download_base_url'] = 'http://dev-stage01.build.sjc1.mozilla.com/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-trunk']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-trunk']['platforms'] = {
    'maemo5-gtk': {},
    'linux-i686': {},
    'macosx-i686': {},
    'win32-i686': {},
    'android-r7': {},
}
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['DISABLED'] = True
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['DISABLED'] = True
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms'] = {}
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['mozconfig'] = 'mobile/maemo5-gtk/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['sb_target'] = 'FREMANTLE_ARMEL'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['mozconfig'] = 'mobile/linux-i686/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['mozconfig'] = 'mobile/macosx-i686/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['mozconfig'] = 'mobile/win32-i686/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['mozconfig'] = 'mobile/android/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['base_upload_dir'] = 'mozilla-central-maemo5-gtk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_upload_dir'] = 'mozilla-central-linux'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_upload_dir'] = 'mozilla-central-macosx'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_upload_dir'] = 'mozilla-central-win32'
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['base_name'] = 'Maemo 5 GTK mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_name'] = 'OS X Fennec Desktop mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_name'] = 'Win32 Fennec Desktop mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['base_name'] = 'Android mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['base_workdir'] = '%s/build/mobile-trunk-maemo5-gtk' % SBOX_HOME
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['base_builddir'] = 'mobile-trunk-maemo5-gtk'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['base_l10n_workdir'] = '%s/build/mobile-trunk-maemo5-gtk-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['base_l10n_workdir'] = 'build/macosx-fennec-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_builddir'] = 'w32mob-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['base_l10n_workdir'] = 'w32mob-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['base_builddir'] = 'android-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['base_l10n_workdir'] = 'android-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-trunk']['enable_l10n_onchange'] = True
MOBILE_BRANCHES['mobile-trunk']['enable_multi_locale'] = True
MOBILE_BRANCHES['mobile-trunk']['l10n_tree'] = 'fennec_mc'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['maemo5-gtk'] = 'linux'
#MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['linux-i686'] = 'linux' # moved to 0.8
#MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['macosx-i686'] = 'macosx'
#MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['win32-i686'] = 'win32' # moved to 0.8
#MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['android-r7'] = 'linux'
MOBILE_BRANCHES['mobile-trunk']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-trunk']['multiLocalesFile'] = "locales/maemo-locales"
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-trunk']['download_base_url'] + '/nightly/latest-mozilla-central-maemo5-gtk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-trunk']['download_base_url'] + '/nightly/latest-mozilla-central-linux'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-trunk']['download_base_url'] + '/nightly/latest-mozilla-central-macosx'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-trunk']['download_base_url'] + '/nightly/latest-mozilla-central-win32'
MOBILE_BRANCHES['mobile-trunk']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-trunk']['l10n_tinderbox_tree'] = 'MozillaStaging'
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['slaves'] = MOBILE_SLAVES['maemo5-gtk']
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['slaves'] = MOBILE_SLAVES['linux-i686']
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['slaves'] = MOBILE_SLAVES['macosx-i686']
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['slaves'] = MOBILE_SLAVES['win32-i686']
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['slaves'] = MOBILE_SLAVES['android-r7']
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-trunk']['platforms']['maemo5-gtk']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-central-maemo5-gtk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['env'] = DEFAULT_MACOSX_ENV.copy()
MOBILE_BRANCHES['mobile-trunk']['platforms']['macosx-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['env'] = DEFAULT_WIN32_ENV.copy()
MOBILE_BRANCHES['mobile-trunk']['platforms']['win32-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['android-r7']['glob_list'] = ['embedding/android/*.apk']

### mozilla-mobile-5.0
MOBILE_BRANCHES['mozilla-mobile-5.0']['main_config'] = config.BRANCHES['mozilla-mobile-5.0']
MOBILE_BRANCHES['mozilla-mobile-5.0']['repo_path'] = 'releases/mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
MOBILE_BRANCHES['mozilla-mobile-5.0']['mobile_repo_path'] = 'releases/mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['product_name'] = 'fennec'
MOBILE_BRANCHES['mozilla-mobile-5.0']['app_name'] = 'mobile'
MOBILE_BRANCHES['mozilla-mobile-5.0']['aus2_base_upload_dir'] = '/opt/aus2/build/0/{a23983c0-fd0e-11dc-95ff-0800200c9a66}/mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['download_base_url'] = 'http://dev-stage01.build.sjc1.mozilla.com/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mozilla-mobile-5.0']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms'] = {
    'maemo5-gtk': {},
    'linux-i686': {},
    'macosx-i686': {},
    'win32-i686': {},
    'android-r7': {},
}
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['DISABLED'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['DISABLED'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['DISABLED'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['DISABLED'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['DISABLED'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_platforms'] = {}
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['mozconfig'] = 'mobile/maemo5-gtk/mozilla-beta/nightly'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['sb_target'] = 'FREMANTLE_ARMEL'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['mozconfig'] = 'mobile/linux-i686/mozilla-beta/nightly'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['mozconfig'] = 'mobile/macosx-i686/mozilla-beta/nightly'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['mozconfig'] = 'mobile/win32-i686/mozilla-beta/nightly'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['mozconfig'] = 'mobile/android/mozilla-beta/nightly'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['generate_symbols'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['base_upload_dir'] = 'mozilla-mobile-5.0-maemo5-gtk'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['base_upload_dir'] = 'mozilla-mobile-5.0-linux'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['base_upload_dir'] = 'mozilla-mobile-5.0-macosx'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['base_upload_dir'] = 'mozilla-mobile-5.0-win32'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['base_name'] = 'Maemo 5 GTK mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['base_name'] = 'OS X Fennec Desktop mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['base_name'] = 'Win32 Fennec Desktop mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['base_name'] = 'Android mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['build_space'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['build_space'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['build_space'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['build_space'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['base_workdir'] = '%s/build/mozilla-mobile-5.0-maemo5-gtk' % SBOX_HOME
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['base_builddir'] = 'mozilla-mobile-5.0-maemo5-gtk'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['base_l10n_workdir'] = '%s/build/mozilla-mobile-5.0-maemo5-gtk-l10n' % SBOX_HOME
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-5.0-l10n'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['base_l10n_workdir'] = 'build/macosx-fennec-5.0-l10n'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['base_builddir'] = 'w32mob-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['base_l10n_workdir'] = 'w32mob-5.0-l10n'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['base_workdir'] = 'build'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['base_builddir'] = 'android-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['base_l10n_workdir'] = 'android-5.0-l10n'
MOBILE_BRANCHES['mozilla-mobile-5.0']['enable_l10n'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['enable_l10n_onchange'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['enable_multi_locale'] = True
MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_tree'] = 'fennec_mc'
MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_platforms']['maemo5-gtk'] = 'linux'
#MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_platforms']['linux-i686'] = 'linux' # moved to 0.8
#MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_platforms']['macosx-i686'] = 'macosx'
#MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_platforms']['win32-i686'] = 'win32' # moved to 0.8
#MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_platforms']['android-r7'] = 'linux'
MOBILE_BRANCHES['mozilla-mobile-5.0']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mozilla-mobile-5.0']['multiLocalesFile'] = "locales/maemo-locales"
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mozilla-mobile-5.0']['download_base_url'] + '/nightly/latest-mozilla-mobile-5.0-maemo5-gtk'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mozilla-mobile-5.0']['download_base_url'] + '/nightly/latest-mozilla-mobile-5.0-linux'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mozilla-mobile-5.0']['download_base_url'] + '/nightly/latest-mozilla-mobile-5.0-macosx'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mozilla-mobile-5.0']['download_base_url'] + '/nightly/latest-mozilla-mobile-5.0-win32'
MOBILE_BRANCHES['mozilla-mobile-5.0']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mozilla-mobile-5.0']['l10n_tinderbox_tree'] = 'MozillaStaging'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['slaves'] = MOBILE_SLAVES['maemo5-gtk']
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['slaves'] = MOBILE_SLAVES['linux-i686']
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['slaves'] = MOBILE_SLAVES['macosx-i686']
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['slaves'] = MOBILE_SLAVES['win32-i686']
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['slaves'] = MOBILE_SLAVES['android-r7']
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['maemo5-gtk']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-mobile-5.0-maemo5-gtk'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['linux-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['env'] = DEFAULT_MACOSX_ENV.copy()
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['macosx-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['env'] = DEFAULT_WIN32_ENV.copy()
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['win32-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-mobile-5.0'
MOBILE_BRANCHES['mozilla-mobile-5.0']['platforms']['android-r7']['glob_list'] = ['embedding/android/*.apk']

### mobile-2.0
MOBILE_BRANCHES['mobile-2.0']['main_config'] = config.BRANCHES['mozilla-2.1']
MOBILE_BRANCHES['mobile-2.0']['repo_path'] = 'releases/mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['l10n_repo_path'] = 'releases/l10n-mozilla-2.0'
MOBILE_BRANCHES['mobile-2.0']['mobile_repo_path'] = 'releases/mobile-2.0'
MOBILE_BRANCHES['mobile-2.0']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-2.0']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-2.0']['aus2_base_upload_dir'] = '/opt/aus2/build/0/{a23983c0-fd0e-11dc-95ff-0800200c9a66}/mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['download_base_url'] = 'http://dev-stage01.build.sjc1.mozilla.com/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-2.0']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-2.0']['platforms'] = {
    'maemo5-gtk': {},
    'linux-i686': {},
    'macosx-i686': {},
    'win32-i686': {},
    'android-r7': {},
}
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['DISABLED'] = True
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['DISABLED'] = True
MOBILE_BRANCHES['mobile-2.0']['l10n_platforms'] = {}
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['mozconfig'] = 'mobile/maemo5-gtk/mobile-2.0/nightly'
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['sb_target'] = 'FREMANTLE_ARMEL'
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['mozconfig'] = 'mobile/linux-i686/mobile-2.0/nightly'
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['mozconfig'] = 'mobile/macosx-i686/mobile-2.0/nightly'
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['mozconfig'] = 'mobile/win32-i686/mobile-2.0/nightly'
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['mozconfig'] = 'mobile/android/mobile-2.0/nightly'
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['base_upload_dir'] = 'mozilla-2.1-maemo5-gtk'
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['base_upload_dir'] = 'mozilla-2.1-linux'
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['base_upload_dir'] = 'mozilla-2.1-macosx'
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['base_upload_dir'] = 'mozilla-2.1-win32'
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['base_name'] = 'Maemo 5 GTK mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['base_name'] = 'OS X Fennec Desktop mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['base_name'] = 'Win32 Fennec Desktop mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['base_name'] = 'Android mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['build_space'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['build_space'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['base_workdir'] = '%s/build/mobile-2.0-maemo5-gtk' % SBOX_HOME
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['base_builddir'] = 'mobile-2.0-maemo5-gtk'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['base_l10n_workdir'] = '%s/build/mobile-2.0-maemo5-gtk-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-2.0'
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-2.0-l10n'
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-2.0'
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['base_l10n_workdir'] = 'build/macosx-fennec-2.0-l10n'
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['base_builddir'] = 'w32mob-2.0'
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['base_l10n_workdir'] = 'w32mob-2.0-l10n'
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['base_builddir'] = 'android-2.0'
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['base_l10n_workdir'] = 'android-2.0-l10n'
MOBILE_BRANCHES['mobile-2.0']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-2.0']['enable_l10n_onchange'] = True
MOBILE_BRANCHES['mobile-2.0']['enable_multi_locale'] = True
MOBILE_BRANCHES['mobile-2.0']['l10n_tree'] = 'fennec_mc'
MOBILE_BRANCHES['mobile-2.0']['l10n_platforms']['maemo5-gtk'] = 'linux'
#MOBILE_BRANCHES['mobile-2.0']['l10n_platforms']['linux-i686'] = 'linux' # moved to 0.8
#MOBILE_BRANCHES['mobile-2.0']['l10n_platforms']['macosx-i686'] = 'macosx'
#MOBILE_BRANCHES['mobile-2.0']['l10n_platforms']['win32-i686'] = 'win32' # moved to 0.8
#MOBILE_BRANCHES['mobile-2.0']['l10n_platforms']['android-r7'] = 'linux'
MOBILE_BRANCHES['mobile-2.0']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-2.0']['multiLocalesFile'] = "locales/maemo-locales"
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-2.0']['download_base_url'] + '/nightly/latest-mozilla-2.1-maemo5-gtk'
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-2.0']['download_base_url'] + '/nightly/latest-mozilla-2.1-linux'
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-2.0']['download_base_url'] + '/nightly/latest-mozilla-2.1-macosx'
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-2.0']['download_base_url'] + '/nightly/latest-mozilla-2.1-win32'
MOBILE_BRANCHES['mobile-2.0']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-2.0']['l10n_tinderbox_tree'] = 'MozillaStaging'
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['slaves'] = MOBILE_SLAVES['maemo5-gtk']
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['slaves'] = MOBILE_SLAVES['linux-i686']
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['slaves'] = MOBILE_SLAVES['macosx-i686']
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['slaves'] = MOBILE_SLAVES['win32-i686']
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['slaves'] = MOBILE_SLAVES['android-r7']
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-2.0']['platforms']['maemo5-gtk']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-2.1-maemo5-gtk'
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-2.0']['platforms']['linux-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['env'] = DEFAULT_MACOSX_ENV.copy()
MOBILE_BRANCHES['mobile-2.0']['platforms']['macosx-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['env'] = DEFAULT_WIN32_ENV.copy()
MOBILE_BRANCHES['mobile-2.0']['platforms']['win32-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-2.1'
MOBILE_BRANCHES['mobile-2.0']['platforms']['android-r7']['glob_list'] = ['embedding/android/*.apk']

### mobile-1.9.2
MOBILE_BRANCHES['mobile-1.9.2']['main_config'] = config.BRANCHES['mozilla-1.9.2']
MOBILE_BRANCHES['mobile-1.9.2']['repo_path'] = 'releases/mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['mobile_repo_path'] = 'releases/mobile-1.1'
MOBILE_BRANCHES['mobile-1.9.2']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-1.9.2']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-1.9.2']['aus2_base_upload_dir'] = '/opt/aus2/build/0/{a23983c0-fd0e-11dc-95ff-0800200c9a66}/mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['download_base_url'] = 'http://dev-stage01.build.sjc1.mozilla.com/pub/mozilla.org/mobile'
MOBILE_BRANCHES['mobile-1.9.2']['stage_base_path'] = '/home/ftp/pub/mobile'
MOBILE_BRANCHES['mobile-1.9.2']['platforms'] = {
    'maemo4': {},
    'maemo5-gtk': {},
    'linux-i686': {},
    'macosx-i686': {},
    'win32-i686': {},
}
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['DISABLED'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['DISABLED'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['DISABLED'] = True
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms'] = {}
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['mozconfig'] = 'mobile/maemo4/mobile-1.1/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['sb_target'] = 'CHINOOK-ARMEL-2007'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['mozconfig'] = 'mobile/maemo5-gtk/mobile-1.1/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['sb_target'] = 'FREMANTLE_ARMEL'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['mozconfig'] = 'mobile/linux-i686/mobile-1.1/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['mozconfig'] = 'mobile/macosx-i686/mobile-1.1/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['mozconfig'] = 'mobile/win32-i686/mobile-1.1/nightly'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['generate_symbols'] = True
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['base_upload_dir'] = 'mozilla-1.9.2-maemo4'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['base_upload_dir'] = 'mozilla-1.9.2-maemo5-gtk'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_upload_dir'] = 'mozilla-1.9.2-linux'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_upload_dir'] = 'mozilla-1.9.2-macosx'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_upload_dir'] = 'mozilla-1.9.2-win32'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['base_name'] = 'Maemo mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['base_name'] = 'Maemo 5 GTK mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_name'] = 'Linux Fennec Desktop mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_name'] = 'OS X Fennec Desktop mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_name'] = 'Win32 Fennec Desktop mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['builds_before_reboot'] = 5
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['base_workdir'] = '%s/build/maemo-1.9.2' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['base_builddir'] = 'maemo-1.9.2'
# This base directory is for the individual locales repackaging; it is not for the multi-locale build
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['base_l10n_workdir'] = '%s/build/maemo-1.9.2-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['base_workdir'] = '%s/build/mobile-1.9.2-maemo5-gtk' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['base_builddir'] = 'mobile-1.9.2-maemo5-gtk'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['base_l10n_workdir'] = '%s/build/mobile-1.9.2-maemo5-gtk-l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_builddir'] = 'linux-fennec-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['base_l10n_workdir'] = 'build/linux-fennec-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_workdir'] = 'build'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_builddir'] = 'macosx-fennec-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['base_l10n_workdir'] = 'build/macosx-fennec-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_builddir'] = 'w32mob-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['base_l10n_workdir'] = 'w32mob-1.9.2-l10n'
MOBILE_BRANCHES['mobile-1.9.2']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-1.9.2']['enable_l10n_onchange'] = True
MOBILE_BRANCHES['mobile-1.9.2']['enable_multi_locale'] = True
MOBILE_BRANCHES['mobile-1.9.2']['l10n_tree'] = 'fennec11x'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['maemo4'] = 'linux'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['maemo5-gtk'] = 'linux'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['linux-i686'] = 'linux'
#MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['macosx-i686'] = 'macosx'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_platforms']['win32-i686'] = 'win32'
MOBILE_BRANCHES['mobile-1.9.2']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-1.9.2']['multiLocalesFile'] = "locales/maemo-locales"
MOBILE_BRANCHES['mobile-1.9.2']['tinderbox_tree'] = 'MozillaTest'
MOBILE_BRANCHES['mobile-1.9.2']['l10n_tinderbox_tree'] = 'MozillaStaging'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-1.9.2']['download_base_url'] + '/nightly/latest-mozilla-1.9.2-maemo4'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-1.9.2']['download_base_url'] + '/nightly/latest-mozilla-1.9.2-maemo5-gtk'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-1.9.2']['download_base_url'] + '/nightly/latest-mozilla-1.9.2-linux'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-1.9.2']['download_base_url'] + '/nightly/latest-mozilla-1.9.2-macosx'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['enUS_binaryURL'] = \
    MOBILE_BRANCHES['mobile-1.9.2']['download_base_url'] + '/nightly/latest-mozilla-1.9.2-win32'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['slaves'] = MOBILE_SLAVES['maemo4']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['slaves'] = MOBILE_SLAVES['maemo5-gtk']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['slaves'] = MOBILE_SLAVES['linux-i686']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['slaves'] = MOBILE_SLAVES['macosx-i686']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['slaves'] = MOBILE_SLAVES['win32-i686']
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo4']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-1.9.2-maemo4'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['maemo5-gtk']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-1.9.2-maemo5-gtk'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['env'] = DEFAULT_LINUX_ENV.copy()
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['linux-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['env'] = DEFAULT_MACOSX_ENV.copy()
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['macosx-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-1.9.2'
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['env'] = DEFAULT_WIN32_ENV.copy()
MOBILE_BRANCHES['mobile-1.9.2']['platforms']['win32-i686']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-1.9.2'

#This is needed because we don't use the real branch name as the branch name.
hacktionary = {'mobile-trunk': 'mozilla-central',
               'mobile-2.0': 'mozilla-2.1',
               'mozilla-mobile-5.0': 'mozilla-mobile-5.0',
               'mobile-1.9.2': 'mozilla-1.9.2',
              }

# Create configs for Maemo5 QT that are identical to Maemo5 GTK in all
# respects.
#  -naming
#  -workdirs
#  -upload location
#  -qt builds use qt mozconfigs
for branch in MOBILE_BRANCHES.keys():
    if '1.9.2' in branch:
        continue
    maemo5 = deepcopy(MOBILE_BRANCHES[branch]['platforms']['maemo5-gtk'])
    maemo5['base_name'] = "Maemo 5 QT %s" % hacktionary.get(branch, branch)
    if 'l10n_platforms' in MOBILE_BRANCHES[branch]:
        MOBILE_BRANCHES[branch]['l10n_platforms']['maemo5-qt'] = 'linux'
    maemo5['enUS_binaryURL'] = maemo5['enUS_binaryURL'].replace('gtk', 'qt')
    maemo5['mozconfig'] = maemo5['mozconfig'].replace('gtk', 'qt')
    maemo5['base_workdir'] = '%s/build/%s-maemo5-qt' % (SBOX_HOME,
                                                        branch)
    maemo5['base_builddir'] = '%s-maemo5-qt' % (branch)
    maemo5['base_upload_dir'] = '%s-maemo5-qt' % (hacktionary[branch])
    maemo5['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = '%s-maemo5-qt' % hacktionary.get(branch, branch)
    maemo5['base_l10n_workdir'] = '%s/build/%s-maemo5-qt-l10n' % (SBOX_HOME,
                                                                  branch)
    MOBILE_BRANCHES[branch]['platforms']['maemo5-qt'] = maemo5

if __name__=="__main__":
    import pprint
    pprint.pprint(MOBILE_BRANCHES)
