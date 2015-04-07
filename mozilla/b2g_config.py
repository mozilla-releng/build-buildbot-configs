from copy import deepcopy

from config import GLOBAL_VARS, PLATFORM_VARS, SLAVES, TRY_SLAVES

import b2g_project_branches
reload(b2g_project_branches)
from b2g_project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

# Note that b2g_localconfig.py is symlinked to one of:
# {production,staging}_b2g_config.py
import b2g_localconfig
reload(b2g_localconfig)

import master_common
reload(master_common)
from master_common import items_before, setMainFirefoxVersions, items_at_least

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
PLATFORM_VARS = deepcopy(PLATFORM_VARS)

GLOBAL_VARS.update(b2g_localconfig.GLOBAL_VARS.copy())

GLOBAL_VARS.update({
    'platforms': {
        'linux64_gecko': {},
        'linux64_gecko-debug': {},
        'macosx64_gecko': {},
        'macosx64_gecko-debug': {},
        'macosx64-mulet': {},
        'win32_gecko': {},
        'win32_gecko-debug': {},
        'win32-mulet': {},
        'nexus-4': {},
        'nexus-4_eng': {},
        'nexus-5-l': {},
        'nexus-5-l_eng': {},
        'emulator': {},
        'emulator-debug': {},
        'emulator-jb': {},
        'emulator-jb-debug': {},
        'emulator-kk': {},
        'emulator-kk-debug': {},
        'emulator-l': {},
        'emulator-l-debug': {},
        'linux64-b2g-haz': {},
        'flame': {},
        'flame_eng': {},
        'flame-kk': {},
        'flame-kk_eng': {},
        'flame-kk_eng-debug': {},
        'dolphin': {},
        'dolphin_eng': {},
        'dolphin-512': {},
        'dolphin-512_eng': {},

        # Graphene builds. These are a different app (ie, not B2G) and would
        # have their own config files in an ideal world, but it's not worth
        # the effort at this point.
        'linux64_graphene': {},
        'macosx64_graphene': {},
        'win64_graphene': {},
    },
    'enable_nightly': True,
    'enable_l10n': False,
    'enable_xulrunner': False,
    'enabled_products': ['b2g', 'graphene'],
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
    'linux64_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'unittest_platform': 'linux64_gecko-opt',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/linux64_gecko/nightly',
        'enable_dep': True,
        'profiled_build': False,
        'updates_enabled': False,
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
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_rsa",
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
            ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
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
        'enable_dep': False,
        'enable_periodic': True,
        'enable_nightly': False,
        'profiled_build': False,
        'updates_enabled': False,
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
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_rsa",
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
            ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
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
        'mozharness_desktop_build': {
                'script_name': 'scripts/b2g_desktop_build.py',
                'extra_args': ['--config', 'b2g/desktop_macosx64.py'],
        },
        'app_name': 'b2g',
        'unittest_platform': 'macosx64_gecko-opt',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/macosx64_gecko/nightly',
        'enable_dep': False,
        'enable_periodic': True,
        'profiled_build': False,
        'updates_enabled': False,
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
            'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_rsa",
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
        'mozharness_desktop_build': {
                'script_name': 'scripts/b2g_desktop_build.py',
                'extra_args': [
                    '--config', 'b2g/desktop_macosx64.py',
                    '--custom-build-variant-cfg', 'b2g-debug',
                ],
        },
        'app_name': 'b2g',
        'unittest_platform': 'macosx64_gecko-debug',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/debug',
        'src_mozconfig': 'b2g/config/mozconfigs/macosx64_gecko/debug',
        'enable_dep': False,
        'enable_periodic': True,
        'enable_nightly': False,
        'profiled_build': False,
        'updates_enabled': False,
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
            'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_rsa",
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
    'macosx64-mulet': {
        'product_name': 'firefox',
        'mozharness_desktop_build': {
            'script_name': 'scripts/fx_desktop_build.py',
            'extra_args': [
                '--config', 'builds/releng_base_mac_64_builds.py',
                '--custom-build-variant-cfg', 'mulet',
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            'script_timeout': 3 * 3600,
            'script_maxtime': int(5.5 * 3600),
        },
        'multi_locale': False,
        'unittest_platform': 'macosx64-mulet-opt',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'base_name': 'OS X Mulet %(branch)s',
        'mozconfig': 'in_tree',
        'src_mozconfig': 'b2g/dev/config/mozconfigs/macosx64/mulet',
        'packageTests': False,
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 12,
        'upload_symbols': False,
        'download_symbols': False,
        'slaves': SLAVES['macosx64-lion'],
        'platform_objdir': OBJDIR,
        'stage_product': 'b2g',
        'stage_platform': 'macosx64-mulet',
        'update_platform': 'Darwin_x86_64-gcc3',
        'enable_shared_checkouts': True,
        'enable_nightly': True,
        'env': {
            'MOZ_OBJDIR': OBJDIR,
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'TOOLTOOL_CACHE': '/builds/tooltool_cache',
            'TOOLTOOL_HOME': '/builds',
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_rsa",
            'MOZ_SYMBOLS_EXTRA_BUILDID': 'macosx64-mulet',
            'CHOWN_ROOT': '~/bin/chown_root',
            'CHOWN_REVERT': '~/bin/chown_revert',
            'LC_ALL': 'C',
            'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
            'CCACHE_DIR': '/builds/ccache',
            'CCACHE_COMPRESS': '1',
            'CCACHE_UMASK': '002',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'talos_masters': None,
        'test_pretty_names': False,
        'tooltool_manifest_src': 'b2g/dev/config/tooltool-manifests/macosx64/releng.manifest',
        'tooltool_l10n_manifest_src': 'browser/config/tooltool-manifests/macosx64/l10n.manifest',
        'enable_ccache': True,
    },
    'win32_gecko': {
        'product_name': 'b2g',
        'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
        'mozharness_desktop_build': {
                'script_name': 'scripts/b2g_desktop_build.py',
                'extra_args': ['--config', 'b2g/desktop_windows32.py'],
        },
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
        'src_mozconfig': 'b2g/config/mozconfigs/win32_gecko/nightly',
        'enable_dep': False,
        'enable_periodic': True,
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'updates_enabled': False,
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
            'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_rsa",
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
        'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
        'mozharness_desktop_build': {
                'script_name': 'scripts/b2g_desktop_build.py',
                'extra_args': [
                    '--config', 'b2g/desktop_windows32.py',
                    '--custom-build-variant-cfg', 'b2g-debug',
                ],
        },
        'app_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/debug',
        'src_mozconfig': 'b2g/config/mozconfigs/win32_gecko/debug',
        'enable_dep': False,
        'enable_periodic': True,
        'enable_nightly': False,
        'profiled_build': False,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'updates_enabled': False,
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
            'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_rsa",
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
    'win32-mulet': {
        'product_name': 'firefox',
        'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
        'mozharness_desktop_build': {
            'script_name': 'scripts/fx_desktop_build.py',
            'extra_args': [
                '--config', 'builds/releng_base_windows_32_builds.py',
                '--custom-build-variant-cfg', 'mulet',
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            'script_timeout': 3 * 3600,
            'script_maxtime': int(5.5 * 3600),
        },
        'app_name': 'browser',
        'base_name': 'Win32 Mulet %(branch)s',
        'mozconfig': 'in_tree',
        'src_mozconfig': 'b2g/dev/config/mozconfigs/win32/mulet',
        'enable_dep': True,
        'profiled_build': False,
        'enable_nightly': True,
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 13,
        'upload_symbols': False,
        'packageTests': True,
        'updates_enabled': False,
        'create_partial': False,
        'slaves': SLAVES['win64-rev2'],
        'platform_objdir': OBJDIR,
        'unittest_masters': [],
        'unittest_platform': 'win32-mulet-opt',
        'stage_product': 'b2g',
        'stage_platform': 'win32-mulet',
        'update_platform': 'WINNT_x86-msvc',
        'enable_shared_checkouts': True,
        'env': {
            'MOZ_OBJDIR': OBJDIR,
            'SYMBOL_SERVER_HOST': b2g_localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_rsa",
            'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
            'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
            'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
            'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            'WGET_OPTS': '-q -c',
        },
        'enable_opt_unittests': False,
        'enable_checktests': True,
        'talos_masters': None,
        'test_pretty_names': False,
        'l10n_check_test': False,
        'multi_locale': False,
        'tooltool_manifest_src': 'b2g/dev/config/tooltool-manifests/win32/releng.manifest',
        'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
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
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
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
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'nexus-5-l': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'nexus-5-l', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'nexus-5-l_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'nexus-5-l', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
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
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
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
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
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
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
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
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
        'maxTime': 6 * 3600,
    },
    'emulator-kk': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-kk', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
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
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
        'maxTime': 6 * 3600,
    },
    'emulator-l': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-l', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
        'maxTime': 6 * 3600,
    },
    'emulator-l-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-l', '--config', 'b2g/releng-emulator.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
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
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'maxTime': 6 * 3600,
        'try_by_default': True,
        'consider_for_nightly': False,
        'mock_target': 'mozilla-centos6-x86_64',
        'reboot_command': [
            '/tools/checkouts/mozharness/external_tools/count_and_reboot.py',
            '-f', '../reboot_count.txt', '-n', '1', '-z'
        ],
        'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
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
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
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
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
    },
    'flame-kk': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'flame-kk', '--config', 'b2g/releng-private-updates.py',
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
    'flame-kk_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'flame-kk', '--config', 'b2g/releng-otoro-eng.py',
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
    'flame-kk_eng-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'flame-kk', '--config', 'b2g/releng-otoro-eng.py',
                           '--debug',
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
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
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
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'dolphin-512': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'dolphin-512', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'dolphin-512_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'dolphin-512', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },


    "linux64_graphene": {
        "mozharness_python": "/tools/buildbot/bin/python",
        "reboot_command": [
            "/tools/checkouts/mozharness/external_tools/count_and_reboot.py",
            "-f", "../reboot_count.txt", "-n", "1", "-z"
        ],
        "mozharness_repo_cache": "/tools/checkouts/mozharness",
        "tools_repo_cache": "/tools/checkouts/build-tools",
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_linux_64_builds.py",
                "--custom-build-variant-cfg", "graphene",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "graphene_%(branch)s_linux64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["mock"],
        "try_by_default": False,
    },
    "macosx64_graphene": {
        "mozharness_python": "/tools/buildbot/bin/python",
        "reboot_command": ["scripts/external_tools/count_and_reboot.py",
                           "-f", "../reboot_count.txt", "-n", "1", "-z"],
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_mac_64_builds.py",
                "--custom-build-variant-cfg", "graphene",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "graphene_%(branch)s_macosx64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["macosx64-lion"],
        "try_by_default": False,
    },
    "win64_graphene": {
        "mozharness_python": ["c:/mozilla-build/python27/python", "-u"],
        "reboot_command": [
            "c:/mozilla-build/python27/python", "-u",
            "scripts/external_tools/count_and_reboot.py",
            "-f", "../reboot_count.txt","-n", "1", "-z"
        ],
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_windows_64_builds.py",
                "--custom-build-variant-cfg", "graphene",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "graphene_%(branch)s_win64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["win64-rev2"],
        "try_by_default": False,
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
    'mozilla-b2g30_v1_4': {
        'gecko_version': 30,
        'b2g_version': (1, 4, 0),
    },
    'mozilla-b2g32_v2_0': {
        'gecko_version': 32,
        'b2g_version': (2, 0, 0),
    },
    'mozilla-b2g34_v2_1': {
        'gecko_version': 34,
        'b2g_version': (2, 1, 0),
    },
    'mozilla-b2g34_v2_1s': {
        'gecko_version': 34,
        'b2g_version': (2, 1, 0),
    },
    'mozilla-b2g37_v2_2': {
        'gecko_version': 37,
        'b2g_version': (2, 2, 0),
    },
    'try': {
        'lock_platforms': True,
        'platforms': {
            'linux64-b2g-haz': {},
            'macosx64_gecko': {},
            'macosx64_gecko-debug': {},
            'macosx64-mulet': {},
            'win32_gecko': {},
            'win32_gecko-debug': {},
            'win32-mulet': {},
            'linux64_graphene': {},
            'macosx64_graphene': {},
            'win64_graphene': {},
            'emulator': {},
            'emulator-debug': {},
            'emulator-jb': {},
            'emulator-jb-debug': {},
            'emulator-kk': {},
            'emulator-kk-debug': {},
            'emulator-l': {},
            'emulator-l-debug': {},
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
BRANCHES['mozilla-central']['start_hour'] = [1, 16]
BRANCHES['mozilla-central']['start_minute'] = [2]
BRANCHES['mozilla-central']['periodic_start_hours'] = range(1, 24, 3)
BRANCHES['mozilla-central']['periodic_start_minute'] = 30
BRANCHES['mozilla-central']['platforms']['linux64-b2g-haz']['enable_nightly'] = False
BRANCHES['mozilla-central']['platforms']['nexus-4']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-4_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-4_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-central']['platforms']['nexus-5-l']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-5-l_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-5-l_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-central']['platforms']['flame-kk']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['flame-kk_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-debug']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-kk-debug']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-l']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['emulator-l-debug']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['dolphin']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['dolphin_eng']['enable_nightly'] = True

######## mozilla-b2g37_v2_2
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g37_v2_2']['repo_path'] = 'releases/mozilla-b2g37_v2_2'
BRANCHES['mozilla-b2g37_v2_2']['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
BRANCHES['mozilla-b2g37_v2_2']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-aurora'
BRANCHES['mozilla-b2g37_v2_2']['start_hour'] = [0, 16]
BRANCHES['mozilla-b2g37_v2_2']['start_minute'] = [25]
BRANCHES['mozilla-b2g37_v2_2']['periodic_start_minute'] = 30
BRANCHES['mozilla-b2g37_v2_2']['platforms']['linux64-b2g-haz']['enable_nightly'] = False
BRANCHES['mozilla-b2g37_v2_2']['platforms']['nexus-4']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['nexus-4_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['nexus-4_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-b2g37_v2_2']['platforms']['nexus-5-l']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['nexus-5-l_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['nexus-5-l_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-b2g37_v2_2']['platforms']['flame-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['flame-kk_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['emulator']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['emulator-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['emulator-kk-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['emulator-l']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['emulator-l-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['dolphin']['enable_nightly'] = True
BRANCHES['mozilla-b2g37_v2_2']['platforms']['dolphin_eng']['enable_nightly'] = True

######## mozilla-b2g34_v2_1
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g34_v2_1']['repo_path'] = 'releases/mozilla-b2g34_v2_1'
BRANCHES['mozilla-b2g34_v2_1']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v2_1/'
BRANCHES['mozilla-b2g34_v2_1']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g34_v2_1']['start_hour'] = [0, 16]
BRANCHES['mozilla-b2g34_v2_1']['start_minute'] = [12]
BRANCHES['mozilla-b2g34_v2_1']['periodic_start_minute'] = 30
BRANCHES['mozilla-b2g34_v2_1']['platforms']['nexus-4']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['nexus-4_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['nexus-4_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-b2g34_v2_1']['platforms']['nexus-5-l']['enable_periodic'] = False
BRANCHES['mozilla-b2g34_v2_1']['platforms']['nexus-5-l_eng']['enable_periodic'] = False
BRANCHES['mozilla-b2g34_v2_1']['platforms']['flame']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['flame_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['flame-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['flame-kk_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['emulator']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['emulator-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['emulator-kk-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1']['platforms']['dolphin']['enable_nightly'] = False
BRANCHES['mozilla-b2g34_v2_1']['platforms']['dolphin_eng']['enable_nightly'] = False

######## mozilla-b2g34_v2_1s
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g34_v2_1s']['repo_path'] = 'releases/mozilla-b2g34_v2_1s'
BRANCHES['mozilla-b2g34_v2_1s']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v2_1/'
BRANCHES['mozilla-b2g34_v2_1s']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g34_v2_1s']['start_hour'] = [0, 16]
BRANCHES['mozilla-b2g34_v2_1s']['start_minute'] = [12]
BRANCHES['mozilla-b2g34_v2_1s']['periodic_start_minute'] = 30
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['emulator-kk-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['dolphin']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['dolphin_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['dolphin-512']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['dolphin-512_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['dolphin-512_eng']['enable_dep'] = True
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['flame-kk']['enable_periodic'] = False
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['flame-kk_eng']['enable_periodic'] = False
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['flame-kk_eng']['enable_dep'] = False
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['flame-kk_eng-debug']['enable_periodic'] = False
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['nexus-4']['enable_periodic'] = False
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['nexus-4_eng']['enable_periodic'] = False
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['nexus-5-l']['enable_periodic'] = False
BRANCHES['mozilla-b2g34_v2_1s']['platforms']['nexus-5-l_eng']['enable_periodic'] = False

######## mozilla-b2g32_v2_0
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g32_v2_0']['repo_path'] = 'releases/mozilla-b2g32_v2_0'
BRANCHES['mozilla-b2g32_v2_0']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v2_0/'
BRANCHES['mozilla-b2g32_v2_0']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g32_v2_0']['start_hour'] = [0, 16]
BRANCHES['mozilla-b2g32_v2_0']['start_minute'] = [2]
BRANCHES['mozilla-b2g32_v2_0']['periodic_start_minute'] = 30
BRANCHES['mozilla-b2g32_v2_0']['platforms']['nexus-4']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['flame-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['flame-kk_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-jb']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-jb-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['emulator-kk-debug']['enable_nightly'] = True
BRANCHES['mozilla-b2g32_v2_0']['platforms']['nexus-5-l']['enable_periodic'] = False
BRANCHES['mozilla-b2g32_v2_0']['platforms']['nexus-5-l_eng']['enable_periodic'] = False

######## mozilla-b2g30_v1_4
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g30_v1_4']['repo_path'] = 'releases/mozilla-b2g30_v1_4'
BRANCHES['mozilla-b2g30_v1_4']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v1_4/'
BRANCHES['mozilla-b2g30_v1_4']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g30_v1_4']['start_hour'] = [0, 16]
BRANCHES['mozilla-b2g30_v1_4']['start_minute'] = [2]
BRANCHES['mozilla-b2g30_v1_4']['periodic_start_minute'] = 30
BRANCHES['mozilla-b2g30_v1_4']['platforms']['nexus-4']['enable_nightly'] = True
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
BRANCHES['mozilla-b2g30_v1_4']['platforms']['nexus-5-l']['enable_periodic'] = False
BRANCHES['mozilla-b2g30_v1_4']['platforms']['nexus-5-l_eng']['enable_periodic'] = False

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
BRANCHES['try']['platforms']['linux64-b2g-haz']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['macosx64_gecko']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['macosx64_gecko-debug']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['macosx64-mulet']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['win32_gecko']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['win32_gecko-debug']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['win32-mulet']['slaves'] = TRY_SLAVES['win64-rev2']
# Bug 1127482 - Make Windows opt and debug, linux debug, and osx debug B2G Desktop builds periodic
## we can't have 1127482 builders be periodic on try so let's revert them back to dep builds
BRANCHES['try']['platforms']['macosx64_gecko']['enable_dep'] = True
BRANCHES['try']['platforms']['macosx64_gecko']['enable_periodic'] = False
BRANCHES['try']['platforms']['macosx64_gecko-debug']['enable_dep'] = True
BRANCHES['try']['platforms']['macosx64_gecko-debug']['enable_periodic'] = False
BRANCHES['try']['platforms']['win32_gecko']['enable_dep'] = True
BRANCHES['try']['platforms']['win32_gecko']['enable_periodic'] = False
BRANCHES['try']['platforms']['win32_gecko-debug']['enable_dep'] = True
BRANCHES['try']['platforms']['win32_gecko-debug']['enable_periodic'] = False
BRANCHES['try']['platforms']['linux64_graphene']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['macosx64_graphene']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['win64_graphene']['slaves'] = TRY_SLAVES['win64-rev2']

BRANCHES['try']['platforms']['emulator']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator']['mozharness_config']['extra_args'] = ['--target', 'emulator', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-debug']['mozharness_config']['extra_args'] = ['--target', 'emulator', '--config', 'b2g/releng-try.py', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-jb']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-jb']['mozharness_config']['extra_args'] = ['--target', 'emulator-jb', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-jb-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-jb-debug']['mozharness_config']['extra_args'] = ['--target', 'emulator-jb', '--config', 'b2g/releng-try.py', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-jb-debug']['enable_dep'] = True
BRANCHES['try']['platforms']['emulator-jb-debug']['enable_periodic'] = False
BRANCHES['try']['platforms']['emulator-kk']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-kk']['mozharness_config']['extra_args'] = ['--target', 'emulator-kk', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-kk']['enable_dep'] = True
BRANCHES['try']['platforms']['emulator-kk']['enable_periodic'] = False
BRANCHES['try']['platforms']['emulator-kk-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-kk-debug']['mozharness_config']['extra_args'] = ['--target', 'emulator-kk', '--config', 'b2g/releng-try.py', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-kk-debug']['enable_dep'] = True
BRANCHES['try']['platforms']['emulator-kk-debug']['enable_periodic'] = False
BRANCHES['try']['platforms']['emulator-l']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-l']['mozharness_config']['extra_args'] = ['--target', 'emulator-l', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-l-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-l-debug']['mozharness_config']['extra_args'] = ['--target', 'emulator-l', '--config', 'b2g/releng-try.py', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-l-debug']['enable_dep'] = True
BRANCHES['try']['platforms']['emulator-l-debug']['enable_periodic'] = False

# Graphene is only enabled on Larch and Try for now.
for name, branch in BRANCHES.iteritems():
    if name not in ("larch", "try"):
        if "linux64_graphene" in branch["platforms"]:
            del branch["platforms"]["linux64_graphene"]
        if "macosx64_graphene" in branch["platforms"]:
            del branch["platforms"]["macosx64_graphene"]
        if "win64_graphene" in branch["platforms"]:
            del branch["platforms"]["win64_graphene"]

# Enable win32/macosx64 mulet in gecko 36+
for name, branch in items_before(BRANCHES, 'gecko_version', 36):
    if 'win32-mulet' in branch['platforms']:
        del branch['platforms']['win32-mulet']
    if 'macosx64-mulet' in branch['platforms']:
        del branch['platforms']['macosx64-mulet']

# dolphin is for selected branches only
for branch in BRANCHES:
    if branch not in ('mozilla-b2g30_v1_4', 'mozilla-b2g34_v2_1s',
                      'mozilla-aurora', 'mozilla-central',
                      'mozilla-inbound', 'b2g-inbound', 'fx-team'):
        if 'dolphin' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['dolphin']
        if 'dolphin_eng' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['dolphin_eng']

# dolphin-512 is for selected branches only
for branch in BRANCHES:
    if branch not in ('mozilla-b2g34_v2_1s',):
        if 'dolphin-512' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['dolphin-512']
        if 'dolphin-512_eng' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['dolphin-512_eng']

# flame (JB) is for b2g30_v1_4 only, superceded by flame-kk
for branch in BRANCHES:
    if branch not in ('mozilla-b2g30_v1_4',):
        if 'flame' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['flame']
        if 'flame_eng' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['flame_eng']

# b2g 1.4+
for name, branch in items_before(BRANCHES, 'gecko_version', 30):
    for p in ('linux64_gecko-debug', 'macosx64_gecko-debug',
              'win32_gecko-debug',
              'emulator-kk', 'emulator-kk-debug'):
        if p in branch['platforms']:
            del branch['platforms'][p]

# exact rooting was enabled in gecko 32
for name, branch in items_before(BRANCHES, 'gecko_version', 32):
    if 'linux64-b2g-haz' in branch['platforms']:
        del branch['platforms']['linux64-b2g-haz']

# b2g 2.0+
for name, branch in items_before(BRANCHES, 'gecko_version', 32):
    for p in ('flame-kk', 'flame-kk_eng', 'flame-kk_eng-debug'):
        if p in branch['platforms']:
            del branch['platforms'][p]

# b2g 2.2+
for name, branch in items_before(BRANCHES, 'gecko_version', 37):
    for p in ('emulator-l', 'emulator-l-debug'):
        if p in branch['platforms']:
            del branch['platforms'][p]

# Disable emulators for gecko 39 and higher, they're now in TC
# See bug 1143766
for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
    for p in ('emulator-l', 'emulator-kk', 'emulator-jb',
              'emulator-l-debug', 'emulator-kk-debug', 'emulator-jb-debug'):
        if p in branch['platforms']:
            del branch['platforms'][p]

# Disable linux b2g desktop builds for gecko 39 and higher, they're now in TC
# See bug 1146604
for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
    for p in ('linux64_gecko', 'linux64_gecko-debug'):
        if p in branch['platforms']:
            del branch['platforms'][p]

# Enable mozharness pinning
for name, branch in items_at_least(BRANCHES, 'gecko_version', 38):
    if name in ('ash', 'try', 'fx-team', 'mozilla-central', 'b2g-inbound'):
        branch['script_repo_manifest'] = \
            "https://hg.mozilla.org/%(repo_path)s/raw-file/%(revision)s/" + \
            "testing/mozharness/mozharness.json"

# Enable mozharness desktop builds
for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
    # if true, any platform with mozharness_desktop_build in its config
    # will use mozharness instead of MozillaBuildFactory
    branch['desktop_mozharness_builds_enabled'] = True

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
    BRANCHES[branch]['updates_enabled'] = branchConfig.get('updates_enabled', False)
    BRANCHES[branch]['update_channel'] = branchConfig.get('update_channel', 'nightly-%s' % branch)
    BRANCHES[branch]['create_partial'] = branchConfig.get('create_partial', False)
    BRANCHES[branch]['create_partial_l10n'] = branchConfig.get('create_partial_l10n', False)
    BRANCHES[branch]['enUS_binaryURL'] = GLOBAL_VARS['download_base_url'] + branchConfig.get('enUS_binaryURL', '')
    # Platform-specific defaults/interpretation
    for platform in BRANCHES[branch]['platforms']:
        # point to the mozconfigs, default is generic
        if platform.endswith('debug'):
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform.split('-')[0] + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/debug'
        else:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/nightly'

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
