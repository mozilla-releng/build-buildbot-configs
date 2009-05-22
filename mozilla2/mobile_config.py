# -*- python -*-
# ex: set syntax=python:

import config
reload(config)

OBJDIR = 'objdir'
SBOX_HOME = '/scratchbox/users/cltbld/home/cltbld'

mobile_slaves = {
    'linux-arm': config.SLAVES['linux'],
    'wince-arm': config.SLAVES['win32'],
}

wince_arm_env = {
    "DEVENVDIR": 'd:\\msvs9\\Common7\\IDE',
    "FRAMEWORK35VERSION": 'v3.5',
    "FRAMEWORKDIR": 'C:\\WINDOWS\\Microsoft.NET\\Framework',
    "FRAMEWORKVERSION": 'v2.0.50727',
    "INCLUDE": 'd:\\msvs9\\VC\\ATLMFC\\INCLUDE;' + \
               'd:\\msvs9\\VC\\INCLUDE;' + \
               'C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\include;',
    "LIB": 'd:\\msvs9\\VC\\ATLMFC\\LIB;' + \
           'd:\\msvs9\\VC\\LIB;C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\lib;',
    "LIBPATH": 'C:\\WINDOWS\\Microsoft.NET\\Framework\\v3.5;' + \
               'C:\\WINDOWS\\Microsoft.NET\\Framework\\v2.0.50727;' + \
               'd:\\msvs9\\VC\\ATLMFC\\LIB;d:\\msvs9\\VC\\LIB;',
    "MOZILLABUILD": 'D:\\mozilla-build\\',
    "MOZILLABUILDDRIVE": 'D:',
    "MOZILLABUILDPATH": '\\mozilla-build\\',
    "MOZ_MSVCVERSION": '9',
    "MOZ_NO_RESET_PATH": '1',
    "MOZ_TOOLS": 'D:\\mozilla-build\\moztools',
    "PATH": 'D:\\mozilla-build\\msys\\local\\bin;' + \
            'd:\\mozilla-build\\wget;' + \
            'd:\\mozilla-build\\7zip;' + \
            'd:\\mozilla-build\\blat261\\full;' + \
            'd:\\mozilla-build\\python25;' + \
            'd:\\mozilla-build\\svn-win32-1.4.2\\bin;' + \
            'd:\\mozilla-build\\upx203w;' + \
            'd:\\mozilla-build\\xemacs\\XEmacs-21.4.19\\i586-pc-win32;' + \
            'd:\\mozilla-build\\info-zip;' + \
            'd:\\mozilla-build\\nsis-2.22;' + \
            'd:\\mozilla-build\\nsis-2.33u;' + \
            '.;' + \
            'D:\\mozilla-build\\msys\\local\\bin;' + \
            'D:\\mozilla-build\\msys\\mingw\\bin;' + \
            'D:\\mozilla-build\\msys\\bin;' + \
            'd:\\msvs9\\Common7\\IDE;' + \
            'd:\\msvs9\\VC\\BIN;' + \
            'd:\\msvs9\\Common7\\Tools;' + \
            'c:\\WINDOWS\\Microsoft.NET\\Framework\\v3.5;' + \
            'c:\\WINDOWS\\Microsoft.NET\\Framework\\v2.0.50727;' + \
            'd:\\msvs9\\VC\\VCPackages;' + \
            'c:\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\bin;' + \
            'c:\\WINDOWS\\system32;' + \
            'c:\\WINDOWS;' + \
            'c:\\WINDOWS\\System32\\Wbem;' + \
            'd:\\mozilla-build\\python25;' + \
            'd:\\mercurial;' + \
            'c:\\Program Files\\Microsoft SQL Server\\90\\Tools\\binn\\;' + \
            'd:\\mozilla-build\\moztools\\bin',
    "SDKDIR": 'D:\\sdks\\v6.0\\',
    "SDKVER": '6',
    "VC8DIR": 'D:\\msvs8\\VC\\',
    "VC9DIR": 'd:\\msvs9\\VC\\',
    "VCINSTALLDIR": 'd:\\msvs9\\VC',
    "VS80COMNTOOLS": 'D:\\msvs8\\Common7\\Tools\\',
    "VS90COMNTOOLS": 'd:\\msvs9\\Common7\\Tools\\',
    "VSINSTALLDIR": 'd:\\msvs9',
}

MOBILE_BRANCHES = {
    'mobile-trunk': {},
    'mobile-1.9.1': {},
}



### mozilla-central
MOBILE_BRANCHES['mobile-trunk']['repo_path'] = 'mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['l10n_repo_path'] = 'l10n-central'
MOBILE_BRANCHES['mobile-trunk']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-trunk']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-trunk']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-trunk']['platforms'] = {
    'linux-arm': {},
    'wince-arm': {},
}
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms'] = {}
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['wince-arm']['mozconfig'] = 'wince/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-arm']['base_name'] = 'Maemo mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['wince-arm']['base_name'] = 'WinCE mozilla-central'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['wince-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-arm']['base_workdir'] = '%s/build' % SBOX_HOME
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-arm']['base_builddir'] = 'maemo-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-arm']['base_l10n_workdir'] = '%s/l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-trunk']['platforms']['wince-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['platforms']['wince-arm']['base_builddir'] = 'wince-trunk'
MOBILE_BRANCHES['mobile-trunk']['platforms']['wince-arm']['base_l10n_workdir'] = '.'
MOBILE_BRANCHES['mobile-trunk']['enable_l10n'] = True
MOBILE_BRANCHES['mobile-trunk']['tree'] = 'fennec10x'
MOBILE_BRANCHES['mobile-trunk']['l10n_platforms']['linux-arm'] = 'linux'
MOBILE_BRANCHES['mobile-trunk']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-trunk']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mobile-trunk-l10n'
MOBILE_BRANCHES['mobile-trunk']['enUS_binaryURL'] = \
    config.DOWNLOAD_BASE_URL + '/nightly/latest-mobile-trunk'
MOBILE_BRANCHES['mobile-trunk']['tinderbox_tree'] = 'Mobile'
MOBILE_BRANCHES['mobile-trunk']['l10n_tinderbox_tree'] = 'Mozilla-l10n'
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-arm']['slaves'] = mobile_slaves['linux-arm']
MOBILE_BRANCHES['mobile-trunk']['platforms']['wince-arm']['slaves'] = mobile_slaves['wince-arm']
MOBILE_BRANCHES['mobile-trunk']['platforms']['linux-arm']['env'] = {}
MOBILE_BRANCHES['mobile-trunk']['platforms']['wince-arm']['env'] = wince_arm_env



### mobile-1.9.1
MOBILE_BRANCHES['mobile-1.9.1']['repo_path'] = 'releases/mozilla-1.9.1'
MOBILE_BRANCHES['mobile-1.9.1']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
MOBILE_BRANCHES['mobile-1.9.1']['mobile_repo_path'] = 'mobile-browser'
MOBILE_BRANCHES['mobile-1.9.1']['product_name'] = 'fennec'
MOBILE_BRANCHES['mobile-1.9.1']['app_name'] = 'mobile'
MOBILE_BRANCHES['mobile-1.9.1']['platforms'] = {
    'linux-arm': {},
    'wince-arm': {},
}
MOBILE_BRANCHES['mobile-1.9.1']['l10n_platforms'] = {}
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['linux-arm']['mozconfig'] = 'linux/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['wince-arm']['mozconfig'] = 'wince/mobile-browser/nightly'
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['linux-arm']['base_name'] = 'Maemo mozilla-1.9.1'
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['wince-arm']['base_name'] = 'WinCE mozilla-1.9.1'
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['linux-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['wince-arm']['build_space'] = 5
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['linux-arm']['base_workdir'] = '%s/build' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['linux-arm']['base_builddir'] = 'maemo-1.9.1'
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['linux-arm']['base_l10n_workdir'] = '%s/l10n' % SBOX_HOME
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['wince-arm']['base_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['wince-arm']['base_builddir'] = 'wince-1.9.1'
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['wince-arm']['base_l10n_workdir'] = '.'
MOBILE_BRANCHES['mobile-1.9.1']['enable_l10n'] = False
MOBILE_BRANCHES['mobile-1.9.1']['l10n_platforms']['linux-arm'] = 'linux'
MOBILE_BRANCHES['mobile-1.9.1']['allLocalesFile'] = "locales/all-locales"
MOBILE_BRANCHES['mobile-1.9.1']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mobile-1.9.1-l10n'
MOBILE_BRANCHES['mobile-1.9.1']['enUS_binaryURL'] = \
    config.DOWNLOAD_BASE_URL + '/nightly/latest-mobile-1.9.1'
MOBILE_BRANCHES['mobile-1.9.1']['tinderbox_tree'] = 'Mobile'
MOBILE_BRANCHES['mobile-1.9.1']['l10n_tinderbox_tree'] = 'Mozilla-l10n'
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['linux-arm']['slaves'] = mobile_slaves['linux-arm']
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['wince-arm']['slaves'] = mobile_slaves['wince-arm']
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['linux-arm']['env'] = {}
MOBILE_BRANCHES['mobile-1.9.1']['platforms']['wince-arm']['env'] = wince_arm_env
