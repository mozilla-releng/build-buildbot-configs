from copy import deepcopy

from config import GLOBAL_VARS, PLATFORM_VARS, SLAVES, TRY_SLAVES

import b2g_project_branches
reload(b2g_project_branches)
from b2g_project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

# Note that b2g_localconfig.py is symlinked to one of:
# {production,staging,preproduction}_b2g_config.py
import b2g_localconfig
reload(b2g_localconfig)

import master_common
reload(master_common)
from master_common import items_before, setMainFirefoxVersions

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
PLATFORM_VARS = deepcopy(PLATFORM_VARS)

GLOBAL_VARS.update(b2g_localconfig.GLOBAL_VARS.copy())

GLOBAL_VARS.update({
    'platforms': {
        'linux32_gecko': {},
        'linux32_gecko-debug': {},
        'linux64_gecko': {},
        'linux64_gecko-debug': {},
        'macosx64_gecko': {},
        'macosx64_gecko-debug': {},
        'win32_gecko': {},
        'win32_gecko-debug': {},
        'linux32_gecko_localizer': {},
        'linux64_gecko_localizer': {},
        'macosx64_gecko_localizer': {},
        'win32_gecko_localizer': {},
        'hamachi': {},
        'hamachi_eng': {},
        'tarako': {},
        'tarako_eng': {},
        'nexus-4': {},
        'nexus-4_eng': {},
        'helix': {},
        'emulator': {},
        'emulator-debug': {},
        'emulator-jb': {},
        'emulator-jb-debug': {},
        'linux64-b2g-haz': {},
        'emulator-kk': {},
        'emulator-kk-debug': {},
        'wasabi': {},
        'flame': {},
        'flame_eng': {},
        'dolphin': {},
        'dolphin_eng': {},
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

GLOBAL_ENV = {
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_AUTOMATION': '1',
}

PLATFORM_VARS = {
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
            'TOOLTOOL_CACHE': '/builds/tooltool_cache',
            'TOOLTOOL_HOME': '/builds',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
            'WGET_OPTS': '-q -c',
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
                          'gcc472_0moz1', 'gcc473_0moz1',
                          'freetype-2.3.11-6.el6_2.9', 'freetype-devel-2.3.11-6.el6_2.9',
                          'gstreamer-devel', 'gstreamer-plugins-base-devel'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux32/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_dev.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
            ('/home/cltbld/.boto', '/builds/.boto'),
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
    'linux32_gecko-debug': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'unittest_platform': 'linux32_gecko-debug',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/debug',
        'src_mozconfig': 'b2g/config/mozconfigs/linux32_gecko/debug',
        'enable_dep': True,
        'enable_nightly': False,
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
        'stage_platform': 'linux32_gecko-debug',
        'update_platform': 'Linux_x86-gcc3',
        'enable_ccache': True,
        'enable_shared_checkouts': True,
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'TOOLTOOL_CACHE': '/builds/tooltool_cache',
            'TOOLTOOL_HOME': '/builds',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
            'WGET_OPTS': '-q -c',
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
                          'gcc472_0moz1', 'gcc473_0moz1',
                          'freetype-2.3.11-6.el6_2.9', 'freetype-devel-2.3.11-6.el6_2.9',
                          'gstreamer-devel', 'gstreamer-plugins-base-devel'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux32/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_dev.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
            ('/home/cltbld/.boto', '/builds/.boto'),
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
            'TOOLTOOL_CACHE': '/builds/tooltool_cache',
            'TOOLTOOL_HOME': '/builds',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
            'WGET_OPTS': '-q -c',
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
                          'gcc472_0moz1', 'gcc473_0moz1',
                          'freetype-2.3.11-6.el6_2.9', 'freetype-devel-2.3.11-6.el6_2.9',
                          'gstreamer-devel', 'gstreamer-plugins-base-devel'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux64/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_dev.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
            ('/home/cltbld/.boto', '/builds/.boto'),
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
    'linux64_gecko-debug': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'unittest_platform': 'linux64_gecko-debug',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/debug',
        'src_mozconfig': 'b2g/config/mozconfigs/linux64_gecko/debug',
        'enable_dep': True,
        'enable_nightly': False,
        'profiled_build': False,
        'create_snippet': False,
        'create_partial': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 16,
        'upload_symbols': False,
        'packageTests': True,
        'slaves': SLAVES['mock'],
        'platform_objdir': OBJDIR,
        'unittest_masters': GLOBAL_VARS['unittest_masters'],
        'stage_product': 'b2g',
        'stage_platform': 'linux64_gecko-debug',
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
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
            'WGET_OPTS': '-q -c',
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
                          'gcc472_0moz1', 'gcc473_0moz1',
                          'freetype-2.3.11-6.el6_2.9', 'freetype-devel-2.3.11-6.el6_2.9',
                          'gstreamer-devel', 'gstreamer-plugins-base-devel'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux64/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_dev.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
            ('/home/cltbld/.boto', '/builds/.boto'),
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
        'unittest_platform': 'macosx64_gecko-opt',
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
        'unittest_masters': GLOBAL_VARS['unittest_masters'],
        'stage_product': 'b2g',
        'stage_platform': 'macosx64_gecko',
        'update_platform': 'Darwin_x86_64-gcc3',
        'enable_shared_checkouts': True,
        'env': {
            'MOZ_OBJDIR': OBJDIR,
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'TOOLTOOL_CACHE': '/builds/tooltool_cache',
            'TOOLTOOL_HOME': '/builds',
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
            'CHOWN_ROOT': '~/bin/chown_root',
            'CHOWN_REVERT': '~/bin/chown_revert',
            'LC_ALL': 'C',
            'PATH': '/tools/python/bin:/tools/buildbot/bin:${PATH}',
            'WGET_OPTS': '-q -c',
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
    'macosx64_gecko-debug': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'unittest_platform': 'macosx64_gecko-debug',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/debug',
        'src_mozconfig': 'b2g/config/mozconfigs/macosx64_gecko/debug',
        'enable_dep': True,
        'enable_nightly': False,
        'profiled_build': False,
        'create_snippet': False,
        'create_partial': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'slaves': SLAVES['macosx64-lion'],
        'platform_objdir': OBJDIR,
        'unittest_masters': GLOBAL_VARS['unittest_masters'],
        'stage_product': 'b2g',
        'stage_platform': 'macosx64_gecko-debug',
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
            'CHOWN_ROOT': '~/bin/chown_root',
            'CHOWN_REVERT': '~/bin/chown_revert',
            'LC_ALL': 'C',
            'PATH': '/tools/python/bin:/tools/buildbot/bin:${PATH}',
            'WGET_OPTS': '-q -c',
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
        'enable_dep': True,
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'create_snippet': False,
        'create_partial': False,
        'slaves': SLAVES['win64-rev2'],
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
            'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
            'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
            'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
            'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            'WGET_OPTS': '-q -c',
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
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/win32/releng.manifest',
        'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
    },
    'win32_gecko-debug': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/debug',
        'src_mozconfig': 'b2g/config/mozconfigs/win32_gecko/debug',
        'enable_dep': True,
        'enable_nightly': False,
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'create_snippet': False,
        'create_partial': False,
        'slaves': SLAVES['win64-rev2'],
        'platform_objdir': OBJDIR,
        'unittest_masters': [],
        'stage_product': 'b2g',
        'stage_platform': 'win32_gecko-debug',
        'update_platform': 'WINNT_x86-msvc',
        'enable_shared_checkouts': True,
        'env': {
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_dsa",
            'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
            'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
            'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
            'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            'WGET_OPTS': '-q -c',
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
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/win32/releng.manifest',
        'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
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
            'TOOLTOOL_CACHE': '/builds/tooltool_cache',
            'TOOLTOOL_HOME': '/builds',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
            # Necessary to avoid conflicting with the dev-focused builds'
            # filenames
            'MOZ_PKG_SPECIAL': 'localizer',
            'WGET_OPTS': '-q -c',
        },
        'enable_opt_unittests': False,
        'enable_checktests': False,
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
                          'gstreamer-devel', 'gstreamer-plugins-base-devel',
                          'gcc472_0moz1', 'gcc473_0moz1'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux32/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_all.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
            ('/home/cltbld/.boto', '/builds/.boto'),
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
            'TOOLTOOL_CACHE': '/builds/tooltool_cache',
            'TOOLTOOL_HOME': '/builds',
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:${PATH}:/tools/buildbot/bin',
            # Necessary to avoid conflicting with the dev-focused builds'
            # filenames
            'MOZ_PKG_SPECIAL': 'localizer',
            'WGET_OPTS': '-q -c',
        },
        'enable_opt_unittests': False,
        'enable_checktests': False,
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
                          'gstreamer-devel', 'gstreamer-plugins-base-devel',
                          'gcc472_0moz1', 'gcc473_0moz1'],
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/linux64/releng.manifest',
        'gaia_repo': gaia_repo,
        'gaia_revision_file': gaia_revision_file,
        'gaia_languages_file': 'locales/languages_all.json',
        'mock_copyin_files': [
            ('/home/cltbld/.hgrc', '/builds/.hgrc'),
            ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
            ('/home/cltbld/.boto', '/builds/.boto'),
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
            'TOOLTOOL_CACHE': '/builds/tooltool_cache',
            'TOOLTOOL_HOME': '/builds',
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
            'CHOWN_ROOT': '~/bin/chown_root',
            'CHOWN_REVERT': '~/bin/chown_revert',
            'LC_ALL': 'C',
            'PATH': '/tools/python/bin:${PATH}',
            # Necessary to avoid conflicting with the dev-focused builds'
            # filenames
            'MOZ_PKG_SPECIAL': 'localizer',
            'WGET_OPTS': '-q -c',
        },
        'enable_opt_unittests': False,
        'enable_checktests': False,
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
        'slaves': SLAVES['win64-rev2'],
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
            'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
            'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
            'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
            'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            # Necessary to avoid conflicting with the dev-focused builds'
            # filenames
            'MOZ_PKG_SPECIAL': 'localizer',
            'WGET_OPTS': '-q -c',
        },
        'enable_opt_unittests': False,
        'enable_checktests': False,
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
        'tooltool_manifest_src': 'b2g/config/tooltool-manifests/win32/releng.manifest',
        'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
    },
    'hamachi': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'hamachi', '--config', 'b2g/releng-fota-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'hamachi_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'hamachi', '--config', 'b2g/releng-fota-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
    },
    'tarako': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'tarako', '--config', 'b2g/releng-fota-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
    },
    'tarako_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'tarako', '--config', 'b2g/releng-fota-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
    },
    'nexus-4': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'nexus-4', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'nexus-4_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'nexus-4', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'helix': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'helix', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'emulator': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'non_unified_extra_args': ['--non-unified'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'enable_nonunified_build': True,
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'maxTime': 6 * 3600,
    },
    'emulator-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator', '--config', 'b2g/releng-emulator.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'non_unified_extra_args': ['--non-unified'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'enable_nonunified_build': True,
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'maxTime': 6 * 3600,
    },
    'emulator-jb': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-jb', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'non_unified_extra_args': ['--non-unified'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'enable_nonunified_build': True,
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'maxTime': 6 * 3600,
    },
    'emulator-jb-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-jb', '--config', 'b2g/releng-emulator.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'non_unified_extra_args': ['--non-unified'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'enable_nonunified_build': True,
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'maxTime': 6 * 3600,
    },
    'linux64-b2g-haz': {
        'mozharness_config': {
            'script_name': 'scripts/hazard_build.py',
            'extra_args': [
                '--target', 'emulator-jb',
                '--config-file', 'b2g/releng-emulator.py',
                '--b2g-config-dir', 'emulator-jb',
                '--config-file', 'hazards/common.py',
                '--config-file', 'hazards/build_b2g.py',
            ],
        },
        'enable_nonunified_build': True,
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'maxTime': 6 * 3600,
        'try_by_default': True,
        'consider_for_nightly': False,
        'mock_target': 'mozilla-centos6-x86_64',
    },
    'emulator-kk': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-kk', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'non_unified_extra_args': ['--non-unified'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'enable_nonunified_build': True,
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
        'maxTime': 6 * 3600,
    },
    'emulator-kk-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-kk', '--config', 'b2g/releng-emulator.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'non_unified_extra_args': ['--non-unified'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'enable_nonunified_build': True,
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
        'maxTime': 6 * 3600,
    },
    'wasabi': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            # using releng-otoro since we are not doing nightlies/updates
            'extra_args': ['--target', 'wasabi', '--config', 'b2g/releng-otoro.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'flame': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'flame', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'flame_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'flame', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
    },
    'dolphin': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'dolphin', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'dolphin_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'dolphin', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
}

for platform in PLATFORM_VARS.values():
    if 'env' not in platform:
        platform['env'] = deepcopy(GLOBAL_ENV)
    else:
        platform['env'].update((k, v) for k, v in GLOBAL_ENV.items() if k not in platform['env'])


# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {
    },
#    'mozilla-aurora': {
#        'gecko_version': 34,
#        'b2g_version': (2, 1, 0),
#    },
    'mozilla-b2g28_v1_3': {
        'gecko_version': 28,
        'b2g_version': (1, 3, 0),
    },
    'mozilla-b2g28_v1_3t': {
        'gecko_version': 28,
        'b2g_version': (1, 3, 0),
        'platforms': {
            'emulator': {},
            'emulator-debug': {},
            'tarako': {},
            'tarako_eng': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g30_v1_4': {
        'gecko_version': 30,
        'b2g_version': (1, 4, 0),
    },
    'mozilla-b2g32_v2_0': {
        'gecko_version': 32,
        'b2g_version': (2, 0, 0),
    },
    'try': {
        'lock_platforms': True,
        'platforms': {
            'linux32_gecko': {},
            'linux64_gecko': {},
            'linux64-b2g-haz': {},
            'macosx64_gecko': {},
            'win32_gecko': {},
            'emulator': {},
            'emulator-debug': {},
            'emulator-jb': {},
            'emulator-jb-debug': {},
            'emulator-kk': {},
            'emulator-kk-debug': {},
        },
    },
}

setMainFirefoxVersions(BRANCHES)

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
BRANCHES['mozilla-central']['start_hour'] = [4, 16]
BRANCHES['mozilla-central']['start_minute'] = [2]
BRANCHES['mozilla-central']['periodic_start_hours'] = range(1, 24, 3)
BRANCHES['mozilla-central']['periodic_start_minute'] = 30
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-central']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-central']['platforms']['hamachi']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['hamachi_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['hamachi_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-central']['platforms']['nexus-4']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-4_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-4_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-central']['platforms']['helix']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['wasabi']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['flame']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['flame_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-debug']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['linux64-b2g-haz']['enable_nightly'] = False
BRANCHES['mozilla-central']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-kk-debug']['enable_nightly'] = True

######### mozilla-aurora
## This is a path, relative to HGURL, where the repository is located
## HGURL + repo_path should be a valid repository
#BRANCHES['mozilla-aurora']['repo_path'] = 'releases/mozilla-aurora'
#BRANCHES['mozilla-aurora']['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
#BRANCHES['mozilla-aurora']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-aurora'
#BRANCHES['mozilla-aurora']['start_hour'] = [0, 16]
#BRANCHES['mozilla-aurora']['start_minute'] = [2]
#BRANCHES['mozilla-aurora']['periodic_start_minute'] = 30
#BRANCHES['mozilla-aurora']['aus2_base_upload_dir'] = 'fake'
#BRANCHES['mozilla-aurora']['aus2_base_upload_dir_l10n'] = 'fake'
#BRANCHES['mozilla-aurora']['platforms']['hamachi']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['hamachi_eng']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['hamachi_eng']['consider_for_nightly'] = False
#BRANCHES['mozilla-aurora']['platforms']['nexus-4']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['helix']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['wasabi']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['flame']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['flame_eng']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['emulator']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['emulator-debug']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['emulator-jb']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['emulator-jb-debug']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['emulator-kk']['enable_nightly'] = True
#BRANCHES['mozilla-aurora']['platforms']['emulator-kk-debug']['enable_nightly'] = True

######## mozilla-b2g32_v2_0
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g32_v2_0']['repo_path'] = 'releases/mozilla-b2g32_v2_0'
BRANCHES['mozilla-b2g32_v2_0']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v2_0/'
BRANCHES['mozilla-b2g32_v2_0']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g32_v2_0']['start_hour'] = [0, 16]
BRANCHES['mozilla-b2g32_v2_0']['start_minute'] = [2]
BRANCHES['mozilla-b2g32_v2_0']['periodic_start_minute'] = 30
BRANCHES['mozilla-b2g32_v2_0']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-b2g32_v2_0']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-b2g32_v2_0']['platforms']['hamachi']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['hamachi_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['hamachi_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-b2g32_v2_0']['platforms']['nexus-4']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['helix']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['wasabi']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['flame']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['flame_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-kk-debug']['enable_nightly'] = True

######## mozilla-b2g30_v1_4
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g30_v1_4']['repo_path'] = 'releases/mozilla-b2g30_v1_4'
BRANCHES['mozilla-b2g30_v1_4']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v1_4/'
BRANCHES['mozilla-b2g30_v1_4']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g30_v1_4']['start_hour'] = [0, 16]
BRANCHES['mozilla-b2g30_v1_4']['start_minute'] = [2]
BRANCHES['mozilla-b2g30_v1_4']['periodic_start_minute'] = 30
BRANCHES['mozilla-b2g30_v1_4']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-b2g30_v1_4']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-b2g30_v1_4']['platforms']['hamachi']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['hamachi_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['hamachi_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-b2g30_v1_4']['platforms']['nexus-4']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['helix']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['wasabi']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['flame']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['flame_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['emulator']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['emulator-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['emulator-kk-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['dolphin']['enable_nightly'] = True
BRANCHES['mozilla-b2g30_v1_4']['platforms']['dolphin_eng']['enable_nightly'] = True

######## mozilla-b2g28_v1_3t
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g28_v1_3t']['repo_path'] = 'releases/mozilla-b2g28_v1_3t'
BRANCHES['mozilla-b2g28_v1_3t']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v1_3'
BRANCHES['mozilla-b2g28_v1_3t']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
# Build every night since we have external dependencies like gaia which need
# building
BRANCHES['mozilla-b2g28_v1_3t']['start_hour'] = [1, 16]
BRANCHES['mozilla-b2g28_v1_3t']['start_minute'] = [40]
BRANCHES['mozilla-b2g28_v1_3t']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-b2g28_v1_3t']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-b2g28_v1_3t']['platforms']['tarako']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3t']['platforms']['tarako_eng']['enable_nightly'] = True

######## mozilla-b2g28_v1_3
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g28_v1_3']['repo_path'] = 'releases/mozilla-b2g28_v1_3'
BRANCHES['mozilla-b2g28_v1_3']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v1_3'
BRANCHES['mozilla-b2g28_v1_3']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
# Build every night since we have external dependencies like gaia which need
# building
BRANCHES['mozilla-b2g28_v1_3']['enable_perproduct_builds'] = True
BRANCHES['mozilla-b2g28_v1_3']['start_hour'] = [2]
BRANCHES['mozilla-b2g28_v1_3']['start_minute'] = [40]
BRANCHES['mozilla-b2g28_v1_3']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-b2g28_v1_3']['aus2_base_upload_dir_l10n'] = 'fake'
BRANCHES['mozilla-b2g28_v1_3']['platforms']['hamachi']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['hamachi']['enable_dep'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['hamachi']['enable_periodic'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['hamachi_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['hamachi_eng']['enable_dep'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['hamachi_eng']['enable_periodic'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['hamachi_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['helix']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['helix']['enable_dep'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['helix']['enable_periodic'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['wasabi']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['wasabi']['enable_dep'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['wasabi']['enable_periodic'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['nexus-4']['enable_dep'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['nexus-4']['enable_periodic'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['nexus-4_eng']['enable_dep'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['nexus-4_eng']['enable_periodic'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['linux32_gecko_localizer']['enable_nightly'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['linux64_gecko_localizer']['enable_nightly'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['macosx64_gecko_localizer']['enable_nightly'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['win32_gecko_localizer']['enable_nightly'] = False
BRANCHES['mozilla-b2g28_v1_3']['platforms']['emulator']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['emulator-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g28_v1_3']['platforms']['emulator-kk-debug']['enable_nightly'] = True

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
BRANCHES['try']['platforms']['linux32_gecko']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64_gecko']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-b2g-haz']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['macosx64_gecko']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['win32_gecko']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['emulator']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator']['mozharness_config']['extra_args'] = ['--target', 'emulator', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-debug']['mozharness_config']['extra_args'] = ['--target', 'emulator', '--config', 'b2g/releng-try.py', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-jb']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-jb']['mozharness_config']['extra_args'] = ['--target', 'emulator-jb', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-jb-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-jb-debug']['mozharness_config']['extra_args'] = ['--target', 'emulator-jb', '--config', 'b2g/releng-try.py', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-kk']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-kk']['mozharness_config']['extra_args'] = ['--target', 'emulator-kk', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-kk']['enable_dep'] = True
BRANCHES['try']['platforms']['emulator-kk']['enable_periodic'] = False
BRANCHES['try']['platforms']['emulator-kk-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-kk-debug']['mozharness_config']['extra_args'] = ['--target', 'emulator-kk', '--config', 'b2g/releng-try.py', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-kk-debug']['enable_dep'] = True
BRANCHES['try']['platforms']['emulator-kk-debug']['enable_periodic'] = False

# tarako is for B2G 1.3t only (gecko28)
for branch in BRANCHES:
    if branch not in ('mozilla-b2g28_v1_3t',):
        if 'tarako' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['tarako']
        if 'tarako_eng' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['tarako_eng']

# dolphin is for B2G 1.4 only
for branch in BRANCHES:
    if branch not in ('mozilla-b2g30_v1_4',):
        if 'dolphin' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['dolphin']
        if 'dolphin_eng' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['dolphin_eng']

# b2g 1.4+
for name, branch in items_before(BRANCHES, 'gecko_version', 30):
    for p in ('flame', 'flame_eng', 'linux64_gecko-debug',
              'macosx64_gecko-debug', 'linux32_gecko-debug', 'win32_gecko-debug',
              'emulator-kk', 'emulator-kk-debug'):
        if p in branch['platforms']:
            del branch['platforms'][p]

# exact rooting was enabled in gecko 32
for name, branch in items_before(BRANCHES, 'gecko_version', 32):
    if 'linux64-b2g-haz' in branch['platforms']:
        del branch['platforms']['linux64-b2g-haz']

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
    BRANCHES[branch]['enable_nightly_everytime'] = branchConfig.get('enable_nightly_everytime', False)
    BRANCHES[branch]['periodic_start_hours'] = branchConfig.get('periodic_start_hours', range(0, 24, 6))
    BRANCHES[branch]['periodic_start_minute'] = branchConfig.get('periodic_start_minute', 30)
    BRANCHES[branch]['start_hour'] = branchConfig.get('start_hour', [4])
    BRANCHES[branch]['start_minute'] = branchConfig.get('start_minute', [42])
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

# We don't run these tests on b2g-inbound
for b in ('b2g-inbound',):
    BRANCHES[b]['platforms']['linux32_gecko']['enable_checktests'] = False
    BRANCHES[b]['platforms']['linux64_gecko']['enable_checktests'] = False

# Only run non-unified builds on m-c and derived branches, except for try
for name, branch in BRANCHES.iteritems():
    gecko_version = branch.get('gecko_version')
    if name != 'try' and (gecko_version is None or gecko_version >= BRANCHES['mozilla-central']['gecko_version']):
        continue
    for pc in branch['platforms'].values():
        if 'enable_nonunified_build' in pc:
            pc['enable_nonunified_build'] = False

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
