from copy import deepcopy

from config import GLOBAL_VARS, PLATFORM_VARS, SLAVES, TRY_SLAVES

import b2g_project_branches
reload(b2g_project_branches)
from b2g_project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

# Note that b2g_localconfig.py is symlinked to one of: {production,staging,preproduction}_b2g_config.py
import b2g_localconfig
reload(b2g_localconfig)

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
PLATFORM_VARS = deepcopy(PLATFORM_VARS)

GLOBAL_VARS.update(b2g_localconfig.GLOBAL_VARS.copy())

GLOBAL_VARS.update({
    'platforms': {
        'ics_armv7a_gecko': {},
        'ics_armv7a_gecko-debug': {},
        'linux32_gecko': {},
        'linux64_gecko': {},
        'macosx64_gecko': {},
        'win32_gecko': {},
        'linux32_gecko_localizer': {},
        'linux64_gecko_localizer': {},
        'macosx64_gecko_localizer': {},
        'win32_gecko_localizer': {},
        'panda': {},
        'unagi': {},
        'unagi_eng': {},
        'otoro': {},
        'inari': {},
        'inari_eng': {},
        'leo': {},
        'leo_eng': {},
        'hamachi': {},
        'hamachi_eng': {},
        'emulator': {},
        'emulator_debug': {},
    },
    'enable_nightly': True,
    'enable_l10n': False,
    'enable_xulrunner': False,
    'enabled_products': ['b2g'],
    'product_prefix': 'b2g',
    'unittest_suites': [],
    # XXX: this seems like it should be at the platform level
    'enable_multi_locale': True,
})

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']
SYMBOL_SERVER_POST_UPLOAD_CMD = GLOBAL_VARS['symbol_server_post_upload_cmd']
builder_prefix = "b2g"
gaia_repo = 'integration/gaia-central'
gaia_revision_file = 'b2g/config/gaia.json'

PLATFORM_VARS = {
    'ics_armv7a_gecko': {
        'product_name': 'b2g',
        'unittest_platform': 'ics_armv7a_gecko-opt',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/ics_armv7a_gecko/nightly',
        'src_xulrunner_mozconfig': 'NO-B2G-XULRUNNER',
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'update_platform': None,
        'upload_symbols': True,
        'create_snippet': False,
        'create_partial': False,
        'enable_xulrunner': False,
        'slaves': SLAVES['mock'],
        'platform_objdir': 'obj-b2g',
        'stage_product': 'b2g',
        'enable_packaging': True,
        'uploadPackages': True,
        'packageTests': True,
        'disable_symbols': False,
        'unittest_masters': GLOBAL_VARS['unittest_masters'],
        'stage_platform': 'ics_armv7a_gecko',
        'enable_ccache': True,
        'enable_shared_checkouts': True,
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'GONK_PRODUCT': 'generic',
            'TOOLCHAIN_HOST': 'linux-x86',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
        },
        'enable_opt_unittests': False,
        'enable_checktests': False,
        'enable_build_analysis': False,
        'test_pretty_names': False,
        'l10n_check_test': False,
        # MOCK SPECIFIC OPTIONS BELOW
        'use_mock': True,
        'mock_target': 'mozilla-centos6-i386',
        'mock_packages': ['autoconf213', 'mozilla-python27', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                          'glibc-static', 'libstdc++-static'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/ics.manifest',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
        ],
    },
    'ics_armv7a_gecko-debug': {
        'enable_nightly': False,
        'product_name': 'b2g',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/ics_armv7a_gecko/debug',
        'src_xulrunner_mozconfig': 'NO-B2G-XULRUNNER',
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'update_platform': None,
        'upload_symbols': True,
        'create_snippet': False,
        'create_partial': False,
        'enable_xulrunner': False,
        'enable_leaktests': False,
        'slaves': SLAVES['mock'],
        'platform_objdir': 'obj-b2g',
        'disable_symbols': False,
        'unittest_masters': GLOBAL_VARS['unittest_masters'],
        'stage_product': 'b2g',
        'enable_packaging': True,
        'uploadPackages': True,
        'packageTests': True,
        'stage_platform': 'ics_armv7a_gecko-debug',
        'enable_ccache': True,
        'enable_shared_checkouts': True,
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'GONK_PRODUCT': 'generic',
            'TOOLCHAIN_HOST': 'linux-x86',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
        },
        'enable_opt_unittests': False,
        'enable_checktests': False,
        'enable_build_analysis': False,
        'test_pretty_names': False,
        'l10n_check_test': False,
        # MOCK SPECIFIC OPTIONS BELOW
        'use_mock': True,
        'mock_target': 'mozilla-centos6-i386',
        'mock_packages': ['autoconf213', 'mozilla-python27', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                          'glibc-static', 'libstdc++-static'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/ics.manifest',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
        ],
    },
    'linux32_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'unittest_platform': 'linux32_gecko-opt',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/linux32_gecko/nightly',
        'enable_dep': True,
        'profiled_build': False,
        'create_snippet': False,
        'create_partial': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'slaves': SLAVES['mock'],
        'platform_objdir': OBJDIR,
        'unittest_masters': GLOBAL_VARS['unittest_masters'],
        'stage_product': 'b2g',
        'stage_platform': 'linux32_gecko',
        'update_platform': 'Linux_x86-gcc3',
        'enable_ccache': True,
        'enable_shared_checkouts': True,
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'TINDERBOX_OUTPUT': '1',
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'enable_build_analysis': True,
        'test_pretty_names': False,
        'l10n_check_test': False,
        'use_mock': True,
        'mock_target': 'mozilla-centos6-i386',
        'mock_packages': ['autoconf213', 'mozilla-python27', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                          'glibc-static', 'libstdc++-static', 'perl-Test-Simple',
                          'perl-Config-General', 'gtk2-devel', 'libnotify-devel',
                          'yasm', 'alsa-lib-devel', 'libcurl-devel', 'wireless-tools-devel',
                          'libX11-devel', 'libXt-devel', 'mesa-libGL-devel',
                          'gnome-vfs2-devel', 'mpfr', 'xorg-x11-font',
                          'imake', 'ccache', 'wget',
                          'freetype-2.3.11-6.el6_2.9', 'freetype-devel-2.3.11-6.el6_2.9',
                          'gstreamer-devel', 'gstreamer-plugins-base-devel'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux32/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_dev.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
        ],
        'multi_locale': True,
        'multi_config_name': 'multi_locale/b2g_linux32.py',
        'mozharness_multi_options': [
            '--build',
            '--summary',
            '--gecko-languages-file', 'build/b2g/locales/all-locales',
        ],
        'gecko_languages_file': 'build/b2g/locales/all-locales',
    },
    'linux64_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'unittest_platform': 'linux64_gecko-opt',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/linux64_gecko/nightly',
        'enable_dep': True,
        'profiled_build': False,
        'create_snippet': False,
        'create_partial': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'slaves': SLAVES['mock'],
        'platform_objdir': OBJDIR,
        'unittest_masters': GLOBAL_VARS['unittest_masters'],
        'stage_product': 'b2g',
        'stage_platform': 'linux64_gecko',
        'update_platform': 'Linux_x86_64-gcc3',
        'enable_ccache': True,
        'enable_shared_checkouts': True,
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'TINDERBOX_OUTPUT': '1',
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'enable_build_analysis': True,
        'test_pretty_names': False,
        'l10n_check_test': False,
        'use_mock': True,
        'mock_target': 'mozilla-centos6-x86_64',
        'mock_packages': ['autoconf213', 'mozilla-python27', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                          'glibc-static', 'libstdc++-static', 'perl-Test-Simple',
                          'perl-Config-General', 'gtk2-devel', 'libnotify-devel',
                          'yasm', 'alsa-lib-devel', 'libcurl-devel', 'wireless-tools-devel',
                          'libX11-devel', 'libXt-devel', 'mesa-libGL-devel',
                          'gnome-vfs2-devel', 'mpfr', 'xorg-x11-font',
                          'imake', 'ccache', 'wget',
                          'freetype-2.3.11-6.el6_2.9', 'freetype-devel-2.3.11-6.el6_2.9',
                          'gstreamer-devel', 'gstreamer-plugins-base-devel'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux64/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_dev.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
        ],
        'multi_locale': True,
        'multi_config_name': 'multi_locale/b2g_linux64.py',
        'mozharness_multi_options': [
            '--build',
            '--summary',
            '--gecko-languages-file', 'build/b2g/locales/all-locales',
        ],
        'gecko_languages_file': 'build/b2g/locales/all-locales',
    },
    'macosx64_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/macosx64_gecko/nightly',
        'enable_dep': True,
        'profiled_build': False,
        'create_snippet': False,
        'create_partial': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'slaves': SLAVES['macosx64-lion'],
        'platform_objdir': OBJDIR,
        'unittest_masters': [],
        'stage_product': 'b2g',
        'stage_platform': 'macosx64_gecko',
        'update_platform': 'Darwin_x86_64-gcc3',
        'enable_shared_checkouts': True,
        'env': {
            'MOZ_OBJDIR': OBJDIR,
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
            'TINDERBOX_OUTPUT': '1',
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'CHOWN_ROOT': '~/bin/chown_root',
            'CHOWN_REVERT': '~/bin/chown_revert',
            'LC_ALL': 'C',
            'PATH': '/tools/python/bin:${PATH}',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'test_pretty_names': False,
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/macosx64/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_dev.json',
        'multi_locale': True,
        'multi_config_name': 'multi_locale/b2g_macosx64.py',
        'mozharness_multi_options': [
            '--build',
            '--summary',
            '--gecko-languages-file', 'build/b2g/locales/all-locales',
        ],
        'gecko_languages_file': 'build/b2g/locales/all-locales',
    },
    'win32_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/win32_gecko/nightly',
        'enable_dep': False,
        'enable_nightly': True,
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'create_snippet': False,
        'create_partial': False,
        'slaves': SLAVES['win64'],
        'platform_objdir': OBJDIR,
        'unittest_masters': [],
        'stage_product': 'b2g',
        'stage_platform': 'win32_gecko',
        'update_platform': 'WINNT_x86-msvc',
        'enable_shared_checkouts': True,
        'env': {
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_dsa",
            'TINDERBOX_OUTPUT': '1',
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows (x64)/srcsrv/pdbstr.exe',
            'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
            'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'talos_masters': GLOBAL_VARS['talos_masters'],
        'test_pretty_names': False,
        'l10n_check_test': False,
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_dev.json',
        'multi_locale': True,
        'multi_config_name': 'multi_locale/b2g_win32.py',
        'mozharness_multi_options': [
            '--build',
            '--summary',
            '--gecko-languages-file', 'build/b2g/locales/all-locales',
        ],
        'gecko_languages_file': 'build/b2g/locales/all-locales',
    },
    'linux32_gecko_localizer': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/linux32_gecko/nightly',
        'enable_dep': False,
        'profiled_build': False,
        'create_snippet': False,
        'create_partial': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': False,
        'slaves': SLAVES['mock'],
        'platform_objdir': OBJDIR,
        'unittest_masters': [],
        'stage_product': 'b2g',
        'stage_platform': 'linux32_gecko_localizer',
        'update_platform': 'Linux_x86-gcc3',
        'enable_ccache': True,
        'enable_shared_checkouts': True,
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'TINDERBOX_OUTPUT': '1',
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
            # Necessary to avoid conflicting with the dev-focused builds'
            # filenames
            'MOZ_PKG_SPECIAL': 'localizer',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'enable_build_analysis': True,
        'test_pretty_names': False,
        'l10n_check_test': False,
        'use_mock': True,
        'mock_target': 'mozilla-centos6-i386',
        'mock_packages': ['autoconf213', 'mozilla-python27', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                          'glibc-static', 'libstdc++-static', 'gtk2-devel',
                          'libnotify-devel', 'yasm', 'alsa-lib-devel',
                          'libcurl-devel', 'wireless-tools-devel',
                          'libX11-devel', 'libXt-devel', 'mesa-libGL-devel',
                          'gnome-vfs2-devel', 'mpfr', 'xorg-x11-font',
                          'imake', 'ccache', 'wget',
                          'freetype-2.3.11-6.el6_2.9', 'freetype-devel-2.3.11-6.el6_2.9',
                          'gstreamer-devel', 'gstreamer-plugins-base-devel'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux32/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_all.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
        ],
        'multi_locale': True,
        'multi_config_name': 'multi_locale/b2g_linux32.py',
        'mozharness_multi_options': [
            '--build',
            '--summary',
            '--gecko-languages-file', 'build/b2g/locales/all-locales',
        ],
        'gecko_languages_file': 'build/b2g/locales/all-locales',
    },
    'linux64_gecko_localizer': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/linux64_gecko/nightly',
        'enable_dep': False,
        'profiled_build': False,
        'create_snippet': False,
        'create_partial': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': False,
        'slaves': SLAVES['mock'],
        'platform_objdir': OBJDIR,
        'unittest_masters': [],
        'stage_product': 'b2g',
        'stage_platform': 'linux64_gecko_localizer',
        'update_platform': 'Linux_x86_64-gcc3',
        'enable_ccache': True,
        'enable_shared_checkouts': True,
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'TINDERBOX_OUTPUT': '1',
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
            # Necessary to avoid conflicting with the dev-focused builds'
            # filenames
            'MOZ_PKG_SPECIAL': 'localizer',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'enable_build_analysis': True,
        'test_pretty_names': False,
        'l10n_check_test': False,
        'use_mock': True,
        'mock_target': 'mozilla-centos6-x86_64',
        'mock_packages': ['autoconf213', 'mozilla-python27', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                          'glibc-static', 'libstdc++-static', 'gtk2-devel',
                          'libnotify-devel', 'yasm', 'alsa-lib-devel',
                          'libcurl-devel', 'wireless-tools-devel',
                          'libX11-devel', 'libXt-devel', 'mesa-libGL-devel',
                          'gnome-vfs2-devel', 'mpfr', 'xorg-x11-font',
                          'imake', 'ccache', 'wget',
                          'freetype-2.3.11-6.el6_2.9', 'freetype-devel-2.3.11-6.el6_2.9',
                          'gstreamer-devel', 'gstreamer-plugins-base-devel'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux64/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_all.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
        ],
        'multi_locale': True,
        'multi_config_name': 'multi_locale/b2g_linux64.py',
        'mozharness_multi_options': [
            '--build',
            '--summary',
            '--gecko-languages-file', 'build/b2g/locales/all-locales',
        ],
        'gecko_languages_file': 'build/b2g/locales/all-locales',
    },
    'macosx64_gecko_localizer': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/macosx64_gecko/nightly',
        'enable_dep': False,
        'profiled_build': False,
        'create_snippet': False,
        'create_partial': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': True,
        'packageTests': False,
        'slaves': SLAVES['macosx64-lion'],
        'platform_objdir': OBJDIR,
        'unittest_masters': [],
        'stage_product': 'b2g',
        'stage_platform': 'macosx64_gecko_localizer',
        'update_platform': 'Darwin_x86_64-gcc3',
        'enable_shared_checkouts': True,
        'env': {
            'MOZ_OBJDIR': OBJDIR,
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
            'TINDERBOX_OUTPUT': '1',
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'CHOWN_ROOT': '~/bin/chown_root',
            'CHOWN_REVERT': '~/bin/chown_revert',
            'LC_ALL': 'C',
            'PATH': '/tools/python/bin:${PATH}',
            # Necessary to avoid conflicting with the dev-focused builds'
            # filenames
            'MOZ_PKG_SPECIAL': 'localizer',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'test_pretty_names': False,
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/macosx64/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_all.json',
        'multi_locale': True,
        'multi_config_name': 'multi_locale/b2g_macosx64.py',
        'mozharness_multi_options': [
            '--build',
            '--summary',
            '--gecko-languages-file', 'build/b2g/locales/all-locales',
        ],
        'gecko_languages_file': 'build/b2g/locales/all-locales',
    },
    'win32_gecko_localizer': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/win32_gecko/nightly',
        'enable_dep': False,
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'create_snippet': False,
        'create_partial': False,
        'slaves': SLAVES['win64'],
        'platform_objdir': OBJDIR,
        'unittest_masters': [],
        'stage_product': 'b2g',
        'stage_platform': 'win32_gecko_localizer',
        'update_platform': 'WINNT_x86-msvc',
        'enable_shared_checkouts': True,
        'env': {
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_dsa",
            'TINDERBOX_OUTPUT': '1',
            'MOZ_CRASHREPORTER_NO_REPORT': '1',
            'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows (x64)/srcsrv/pdbstr.exe',
            'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
            'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            # Necessary to avoid conflicting with the dev-focused builds'
            # filenames
            'MOZ_PKG_SPECIAL': 'localizer',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'talos_masters': GLOBAL_VARS['talos_masters'],
        'test_pretty_names': False,
        'l10n_check_test': False,
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_all.json',
        'multi_locale': True,
        'multi_config_name': 'multi_locale/b2g_win32.py',
        'mozharness_multi_options': [
            '--build',
            '--summary',
            '--gecko-languages-file', 'build/b2g/locales/all-locales',
        ],
        'gecko_languages_file': 'build/b2g/locales/all-locales',
    },
    'panda': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'panda', '--config', 'b2g/releng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--additional-source-tarballs', 'download-panda.tar.bz2'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'unagi': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'unagi', '--config', 'b2g/releng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'unagi_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'unagi', '--config', 'b2g/releng-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           ],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'otoro': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'otoro', '--config', 'b2g/releng-otoro.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'inari': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'inari', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'inari_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'inari', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'leo': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'leo', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'leo_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'leo', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'hamachi': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'hamachi', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'hamachi_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'hamachi', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'emulator': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'generic', '--config', 'b2g/releng.py',
                           '--b2g-config-dir', 'emulator',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
    'emulator_debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'generic', '--config', 'b2g/releng.py',
                           '--b2g-config-dir', 'emulator', '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
    },
}


# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {
    },
    'mozilla-b2g18': {
        # b2g explicitly
        'ics_armv7a_gecko': {},
        'ics_armv7a_gecko-debug': {},
        'linux32_gecko': {},
        'linux64_gecko': {},
        'macosx64_gecko': {},
        'win32_gecko': {},
        'linux32_gecko_localizer': {},
        'linux64_gecko_localizer': {},
        'macosx64_gecko_localizer': {},
        'win32_gecko_localizer': {},
        'panda': {},
        'unagi': {},
        'unagi_eng': {},
        'otoro': {},
        'inari': {},
        'leo': {},
        'leo_eng': {},
        'hamachi': {},
    },
    'mozilla-b2g18_v1_0_1': {
        # b2g explicitly
        'ics_armv7a_gecko': {},
        'ics_armv7a_gecko-debug': {},
        'linux32_gecko': {},
        'linux64_gecko': {},
        'macosx64_gecko': {},
        'win32_gecko': {},
        'linux32_gecko_localizer': {},
        'linux64_gecko_localizer': {},
        'macosx64_gecko_localizer': {},
        'win32_gecko_localizer': {},
        'panda': {},
        'unagi': {},
        'unagi_eng': {},
        'otoro': {},
        'inari': {},
        'inari_eng': {},
        'leo': {},
        'hamachi_eng': {},
    },
    'mozilla-b2g18_v1_1_0_hd': {
        # b2g explicitly
        'ics_armv7a_gecko': {},
        'ics_armv7a_gecko-debug': {},
        'linux32_gecko': {},
        'linux64_gecko': {},
        'macosx64_gecko': {},
        'win32_gecko': {},
        'linux32_gecko_localizer': {},
        'linux64_gecko_localizer': {},
        'macosx64_gecko_localizer': {},
        'win32_gecko_localizer': {},
        'panda': {},
        'unagi': {},
        'unagi_eng': {},
        'otoro': {},
        'inari': {},
        'leo': {},
        'leo_eng': {},
        'hamachi': {},
    },
    'try': {
    },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        # Don't override something that's set
        elif key in ('enable_weekly_bundle',) and key in BRANCHES[branch]:
            continue
        else:
            BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                # put default platform set in all branches, but grab any
                # project_branches.py overrides/additional keys
                if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch]:
                    if platform in PROJECT_BRANCHES[branch]['platforms'].keys():
                        if key in PROJECT_BRANCHES[branch]['platforms'][platform].keys():
                            value = deepcopy(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                else:
                    value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                else:
                    value = deepcopy(value)
                BRANCHES[branch]['platforms'][platform][key] = value

            if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch] and \
                    platform in PROJECT_BRANCHES[branch]['platforms']:
                for key, value in PROJECT_BRANCHES[branch]['platforms'][platform].items():
                    if key == 'env':
                        value = deepcopy(PLATFORM_VARS[platform]['env'])
                        value.update(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                    else:
                        value = deepcopy(value)
                    BRANCHES[branch]['platforms'][platform][key] = value
    # Copy in local config
    if branch in b2g_localconfig.BRANCHES:
        for key, value in b2g_localconfig.BRANCHES[branch].items():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.items():
                    for key, value in platform_config.items():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in b2g_localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Check for project branch removing a platform from default platforms
    if branch in ACTIVE_PROJECT_BRANCHES:
        for key, value in PROJECT_BRANCHES[branch].items():
            if key == 'platforms':
                for platform, platform_config in value.items():
                    if platform_config.get('dont_build'):
                        del BRANCHES[branch]['platforms'][platform]


######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
BRANCHES['mozilla-central']['gecko_l10n_root'] = 'https://hg.mozilla.org/l10n-central'
BRANCHES['mozilla-central']['start_hour'] = [3]
BRANCHES['mozilla-central']['start_minute'] = [2]
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-central']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-central']['platforms']['unagi']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['unagi_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['unagi_eng']['enable_dep'] = False
BRANCHES['mozilla-central']['platforms']['inari']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['inari_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['inari_eng']['enable_dep'] = False
BRANCHES['mozilla-central']['platforms']['leo']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['leo_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['hamachi']['enable_nightly'] = True

######## mozilla-b2g18
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g18']['repo_path'] = 'releases/mozilla-b2g18'
BRANCHES['mozilla-b2g18']['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
BRANCHES['mozilla-b2g18']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
# Build every night since we have external dependencies like gaia which need
# building
BRANCHES['mozilla-b2g18']['enable_nightly_lastgood'] = False
BRANCHES['mozilla-b2g18']['enable_perproduct_builds'] = True
BRANCHES['mozilla-b2g18']['start_hour'] = [7, 23]
BRANCHES['mozilla-b2g18']['start_minute'] = [2]
BRANCHES['mozilla-b2g18']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-b2g18']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-b2g18']['platforms']['unagi']['enable_nightly'] = True
BRANCHES['mozilla-b2g18']['platforms']['unagi']['mozharness_config']['extra_args'] = ['--target', 'unagi', '--config', 'b2g/releng-beta.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['mozilla-b2g18']['platforms']['unagi_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g18']['platforms']['linux32_gecko']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18']['platforms']['linux64_gecko']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18']['platforms']['macosx64_gecko']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18']['platforms']['win32_gecko']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18']['platforms']['linux32_gecko_localizer']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18']['platforms']['linux64_gecko_localizer']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18']['platforms']['macosx64_gecko_localizer']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18']['platforms']['win32_gecko_localizer']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18']['platforms']['otoro']['enable_nightly'] = True
BRANCHES['mozilla-b2g18']['platforms']['inari']['enable_nightly'] = True
BRANCHES['mozilla-b2g18']['platforms']['leo']['enable_nightly'] = True
BRANCHES['mozilla-b2g18']['platforms']['leo_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g18']['platforms']['hamachi']['enable_nightly'] = True
# Disable desktop B2G checktests on the b2g18 branch
BRANCHES['mozilla-b2g18']['platforms']['linux32_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18']['platforms']['linux32_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18']['platforms']['linux64_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18']['platforms']['linux64_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18']['platforms']['macosx64_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18']['platforms']['macosx64_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18']['platforms']['win32_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18']['platforms']['win32_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18']['platforms']['linux32_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18']['platforms']['linux32_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18']['platforms']['linux64_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18']['platforms']['linux64_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18']['platforms']['macosx64_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18']['platforms']['macosx64_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18']['platforms']['win32_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18']['platforms']['win32_gecko_localizer']['gaia_revision_file'] = None

######## mozilla-b2g18_v1_0_1
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g18_v1_0_1']['repo_path'] = 'releases/mozilla-b2g18_v1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
# Build every night since we have external dependencies like gaia which need
# building
BRANCHES['mozilla-b2g18_v1_0_1']['enable_nightly_lastgood'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['enable_perproduct_builds'] = True
BRANCHES['mozilla-b2g18_v1_0_1']['start_hour'] = [7, 23]
BRANCHES['mozilla-b2g18_v1_0_1']['start_minute'] = [2]
BRANCHES['mozilla-b2g18_v1_0_1']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-b2g18_v1_0_1']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['unagi']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['unagi_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux32_gecko']['gaia_repo'] = 'integration/gaia-1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux64_gecko']['gaia_repo'] = 'integration/gaia-1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64_gecko']['gaia_repo'] = 'integration/gaia-1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32_gecko']['gaia_repo'] = 'integration/gaia-1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux32_gecko_localizer']['gaia_repo'] = 'integration/gaia-1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux64_gecko_localizer']['gaia_repo'] = 'integration/gaia-1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64_gecko_localizer']['gaia_repo'] = 'integration/gaia-1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32_gecko_localizer']['gaia_repo'] = 'integration/gaia-1_0_1'
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['otoro']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['inari']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['inari_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['hamachi']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['hamachi_eng']['enable_nightly'] = True
# Disable desktop B2G checktests on the b2g18_v1_0_1 branch
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux32_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux32_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux64_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux64_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux32_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux32_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux64_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux64_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32_gecko_localizer']['gaia_revision_file'] = None

######## mozilla-b2g18_v1_1_0_hd
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g18_v1_1_0_hd']['repo_path'] = 'releases/mozilla-b2g18_v1_1_0_hd'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
# Build every night since we have external dependencies like gaia which need
# building
BRANCHES['mozilla-b2g18_v1_1_0_hd']['enable_nightly_lastgood'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['enable_perproduct_builds'] = True
BRANCHES['mozilla-b2g18_v1_1_0_hd']['start_hour'] = [7, 23]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['start_minute'] = [2]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['unagi']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['unagi_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux32_gecko']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64_gecko']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64_gecko']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32_gecko']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux32_gecko_localizer']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64_gecko_localizer']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64_gecko_localizer']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32_gecko_localizer']['gaia_repo'] = 'integration/gaia-v1-train'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['otoro']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['inari']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['leo']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['leo_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['hamachi']['enable_nightly'] = True
# Disable desktop B2G checktests on the b2g18 branch
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux32_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux32_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32_gecko']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32_gecko']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux32_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux32_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64_gecko_localizer']['gaia_revision_file'] = None
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32_gecko_localizer']['enable_checktests'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32_gecko_localizer']['gaia_revision_file'] = None

######## try
# Try-specific configs
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try']['repo_path'] = 'try'
BRANCHES['try']['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
BRANCHES['try']['gecko_l10n_root'] = 'https://hg.mozilla.org/l10n-central'
BRANCHES['try']['enable_merging'] = False
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['package_dir'] = '%(who)s-%(got_revision)s'
BRANCHES['try']['stage_username'] = 'trybld'
BRANCHES['try']['stage_ssh_key'] = 'trybld_dsa'
# Disable Nightly builds
BRANCHES['try']['enable_nightly'] = False
BRANCHES['try']['platforms']['ics_armv7a_gecko']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['ics_armv7a_gecko']['upload_symbols'] = False
BRANCHES['try']['platforms']['ics_armv7a_gecko-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['ics_armv7a_gecko-debug']['upload_symbols'] = False
BRANCHES['try']['platforms']['linux32_gecko']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64_gecko']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['macosx64_gecko']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['win32_gecko']['slaves'] = TRY_SLAVES['win64']
BRANCHES['try']['platforms']['panda']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['panda']['mozharness_config']['extra_args'] = ['--target', 'panda', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales', '--additional-source-tarballs', 'download-panda.tar.bz2']
BRANCHES['try']['platforms']['unagi']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['unagi']['mozharness_config']['extra_args'] = ['--target', 'unagi', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator']['mozharness_config']['extra_args'] = ['--target', 'generic', '--config', 'b2g/releng-try.py', '--b2g-config-dir', 'emulator', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator_debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator_debug']['mozharness_config']['extra_args'] = ['--target', 'generic', '--config', 'b2g/releng-try.py', '--b2g-config-dir', 'emulator', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']


# TODO: move the MERGE DAY items below to above the BRANCHES['mozilla-central']
# chunk above, once the whole v1_0_1/kill_b2g18 stuff has calmed down

# MERGE DAY: otoro is only for b2g18 + b2g18_v1_0_1
for branch in BRANCHES:
    if branch not in ('mozilla-b2g18', 'mozilla-b2g18_v1_0_1') and \
            'otoro' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['otoro']

# MERGE DAY: inari is only for central + birch + b2g18 + b2g18_v1_0_1
for branch in BRANCHES:
    if branch not in ('mozilla-central', 'birch', 'mozilla-b2g18', 'mozilla-b2g18_v1_0_1') and \
            'inari' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['inari']

# MERGE DAY: inari_eng is only for central + birch + b2g18_v1_0_1
for branch in BRANCHES:
    if branch not in ('mozilla-central', 'birch', 'mozilla-b2g18_v1_0_1',) and \
            'inari_eng' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['inari_eng']

# MERGE DAY: leo/leo_eng is only for birch, m-c, b2g18
for branch in BRANCHES:
    if branch not in ('mozilla-central', 'birch', 'mozilla-b2g18',) and \
            'leo' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['leo']
for branch in BRANCHES:
    if branch not in ('mozilla-central', 'birch', 'mozilla-b2g18',) and \
            'leo_eng' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['leo_eng']

# MERGE DAY: hamachi is only for m-c, birch, b2g18, b2g18_v1_0_1
for branch in BRANCHES:
    if branch not in ('mozilla-central', 'birch', 'mozilla-b2g18', 'mozilla-b2g18_v1_0_1') and \
            'hamachi' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['hamachi']

# MERGE DAY: hamachi_eng is only for b2g18_v1_0_1
for branch in BRANCHES:
    if branch not in ('mozilla-b2g18_v1_0_1',) and \
            'hamachi_eng' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['hamachi_eng']

# MERGE DAY: unagi_eng is only for b2g18 + b2g18_v1_0_1
for branch in BRANCHES:
    if branch not in ('mozilla-b2g18', 'mozilla-b2g18_v1_0_1', 'mozilla-central',) and \
            'unagi_eng' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['unagi_eng']

# MERGE DAY - gstreamer-devel packages ride the trains (bug 881589)
# MERGE DAY - remove branches from this list if gecko 24 merges into them
for b in ("mozilla-b2g18", "mozilla-b2g18_v1_0_1", "mozilla-b2g18_v1_1_0_hd"):
    for p, pc in BRANCHES[b]['platforms'].items():
        if 'mock_packages' in pc:
            BRANCHES[b]['platforms'][p]['mock_packages'] = \
                [x for x in BRANCHES[b]['platforms'][p]['mock_packages'] if x not in (
                    'gstreamer-devel', 'gstreamer-plugins-base-devel',
                    'gstreamer-devel.i686', 'gstreamer-plugins-base-devel.i686',
                )]

######## generic branch configs
for branch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[branch]
    BRANCHES[branch]['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
    BRANCHES[branch]['gecko_l10n_root'] = 'https://hg.mozilla.org/l10n-central'
    BRANCHES[branch]['product_name'] = branchConfig.get('product_name', None)
    BRANCHES[branch]['app_name'] = branchConfig.get('app_name', None)
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['mozharness_repo_path'] = branchConfig.get('mozharness_repo_path', GLOBAL_VARS['mozharness_repo_path'])
    BRANCHES[branch]['mozharness_tag'] = branchConfig.get('mozharness_tag', GLOBAL_VARS['mozharness_tag'])
    BRANCHES[branch]['enabled_products'] = branchConfig.get('enabled_products',
                                                            GLOBAL_VARS['enabled_products'])
    BRANCHES[branch]['enable_nightly'] = branchConfig.get('enable_nightly', False)
    BRANCHES[branch]['start_hour'] = branchConfig.get('start_hour', [4])
    BRANCHES[branch]['start_minute'] = branchConfig.get('start_minute', [2])
    # nightly updates
    BRANCHES[branch]['create_snippet'] = branchConfig.get('create_snippet', False)
    BRANCHES[branch]['update_channel'] = branchConfig.get('update_channel', 'nightly-%s' % branch)
    BRANCHES[branch]['create_partial'] = branchConfig.get('create_partial', False)
    BRANCHES[branch]['create_partial_l10n'] = branchConfig.get('create_partial_l10n', False)
    BRANCHES[branch]['aus2_user'] = branchConfig.get('aus2_user', GLOBAL_VARS['aus2_user'])
    BRANCHES[branch]['aus2_ssh_key'] = branchConfig.get('aus2_ssh_key', GLOBAL_VARS['aus2_ssh_key'])
    BRANCHES[branch]['aus2_base_upload_dir'] = branchConfig.get('aus2_base_upload_dir', '/opt/aus2/incoming/2/B2G/' + branch)
    BRANCHES[branch]['enUS_binaryURL'] = GLOBAL_VARS['download_base_url'] + branchConfig.get('enUS_binaryURL', '')
    # Platform-specific defaults/interpretation
    for platform in BRANCHES[branch]['platforms']:
        # point to the mozconfigs, default is generic
        if platform.endswith('debug'):
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform.split('-')[0] + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/debug'
        else:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/nightly'

# B2G WORK WEEK
for b in ('birch',):
    BRANCHES[b]['platforms']['linux32_gecko']['enable_checktests'] = False
    BRANCHES[b]['platforms']['linux64_gecko']['enable_checktests'] = False
    BRANCHES[b]['platforms']['linux32_gecko_localizer']['enable_checktests'] = False
    BRANCHES[b]['platforms']['linux64_gecko_localizer']['enable_checktests'] = False
    del BRANCHES[b]['platforms']['ics_armv7a_gecko-debug']
# END B2G WORK WEEK


if __name__ == "__main__":
    import sys
    import pprint

    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = BRANCHES

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)
