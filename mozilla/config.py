from copy import deepcopy

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import MAC_SNOW_MINIS, MAC_MINIS, XSERVES, LINUX_VMS, \
                        LINUX_IXS, WIN32_IXS, SLAVES, \
                        TRY_SLAVES

GLOBAL_VARS = {
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'hgurl': 'http://hg.mozilla.org/',
    'hghost': 'hg.mozilla.org',
    'config_subdir': 'mozilla2',
    'objdir': 'obj-firefox',
    'objdir_unittests': 'objdir',
    'stage_username': 'ffxbld',
    'stage_username_xulrunner': 'xrbld',
    'stage_base_path': '/home/ftp/pub',
    'stage_group': None,
    'stage_ssh_key': 'ffxbld_dsa',
    'stage_ssh_xulrunner_key': 'xrbld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_ffx/',
    'symbol_server_post_upload_cmd': '/usr/local/bin/post-symbol-upload.py',
    'symbol_server_mobile_path': '/mnt/netapp/breakpad/symbols_mob/',
    'symbol_server_xulrunner_path': '/mnt/netapp/breakpad/symbols_xr/',
    'aus2_user': 'cltbld',
    'aus2_ssh_key': 'cltbld_dsa',
    'hg_username': 'ffxbld',
    'hg_ssh_key': '~cltbld/.ssh/ffxbld_dsa',
    'graph_selector': '/server/collect.cgi',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'mozharness_repo_path': 'build/mozharness',
    'mozharness_tag': 'default',
    'multi_locale_merge': True,
    'default_build_space': 5,
    'default_l10n_space': 3,
    'default_clobber_time': 24*7, # 1 week
    'unittest_suites': [
        ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
            'mochitest-a11y', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
    ],
    'geriatric_masters': [],
    'platforms': {
        'linux': {},
        'linuxqt': {},
        'linux-rpm': {},
        'linux64': {},
        'linux64-rpm': {},
        'win32': {},
        'win64': {},
        'macosx64': {},
        'linux-debug': {},
        'linux64-debug': {},
        'macosx-debug': {},
        'macosx64-debug': {},
        'win32-debug': {},
        'linux-android': {},
        'linux-android-debug': {},
        'linux-maemo5-gtk': {},
        'linux-maemo5-qt': {},
        'linux-mobile': {},
        'win32-mobile': {},
        'macosx-mobile': {},
    },
    'enable_pgo': False,
    'pgo_platforms': ('linux', 'linux64', 'win32'),
    'periodic_pgo_interval': 6, # in hours
    'product_name': 'firefox', # Not valid for mobile builds
    'app_name': 'browser',     # Not valid for mobile builds
    'brand_name': 'Minefield', # Not valid for mobile builds
    'enable_shark': True,
    'enable_codecoverage': False,
    'enable_blocklist_update': False,
    'blocklist_update_on_closed_tree': False,
    'enable_nightly': True,
    'enabled_products': ['firefox', 'mobile'],
    'enable_valgrind': True,
    'valgrind_platforms': ('linux', 'linux64'),

    # if true, this branch will get bundled and uploaded to ftp.m.o for users
    # to download and thereby accelerate their cloning
    'enable_weekly_bundle': False,

    'hash_type': 'sha512',
    'create_snippet': False,
    'create_partial': False,
    'create_partial_l10n': False,
    'l10n_modules': [
            'browser', 'extensions/reporter',
            'other-licenses/branding/firefox', 'netwerk', 'dom', 'toolkit',
            'security/manager',
            'sync/services',
            ],
    'scratchbox_path': '/builds/scratchbox/moz_scratchbox',
    'scratchbox_home': '/scratchbox/users/cltbld/home/cltbld',
    'use_old_updater': False,
}
GLOBAL_VARS.update(localconfig.GLOBAL_VARS.copy())

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']
SYMBOL_SERVER_POST_UPLOAD_CMD = GLOBAL_VARS['symbol_server_post_upload_cmd']
SYMBOL_SERVER_MOBILE_PATH = GLOBAL_VARS['symbol_server_mobile_path']

PLATFORM_VARS = {
        'linux': {
            'base_name': 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/linux32/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/linux32/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
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
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
        },
        'linuxqt': {
            'base_name': 'Linux QT %(branch)s',
            'mozconfig': 'linux/%(branch)s/qt',
            'src_mozconfig': 'browser/config/mozconfigs/linux32/qt',
            'xr_mozconfig': 'linux/%(branch)s/xulrunner-qt',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/linux32/xulrunner-qt',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linuxqt',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'enable_nightly': False,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None #GLOBAL_VARS['talos_masters'],
        },
        'linux-rpm': {
            'base_name': 'Linux RPM %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly-rpm',
            'src_mozconfig': 'browser/config/mozconfigs/linux32/rpm',
            'enable_nightly': False, # We will explicitly enable for m-c
            'enable_dep': False,
            'enable_xulrunner': False,
            'stage_platform': 'linux-rpm',
            'mc_patches': [],
            'create_snippet': False,
            'create_partial': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': False,
            'download_symbols': False,
            'packageTests': False, #Done in rpm spec file
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux-rpm',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': [],
            'unittest_masters': [],
            'test_pretty_names': False,
        },
        'linux64': {
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/linux64/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
        },
        'linux64-rpm': {
            'base_name': 'Linux RPM x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly-rpm',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/rpm',
            'enable_nightly': False, # We will explicitly enable for m-c
            'enable_dep': False,
            'enable_xulrunner': False,
            'stage_platform': 'linux64-rpm',
            'mc_patches': [],
            'create_snippet': False,
            'create_partial': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': False,
            'download_symbols': False,
            'packageTests': False, #Done in rpm spec file
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64-rpm',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': [],
            'unittest_masters': [],
            'test_pretty_names': False,
        },
        'macosx': {
            'base_name': 'OS X 10.5.2 %(branch)s',
            'mozconfig': 'macosx/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/macosx-universal/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/macosx-universal/xulrunner',
            'src_shark_mozconfig': 'browser/config/mozconfigs/macosx-universal/shark',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 10,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['macosx'],
            'platform_objdir': "%s/ppc" % OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx',
            'update_platform': 'Darwin_Universal-gcc3',
            'enable_shared_checkouts': True,
            'enable_shark': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx64': {
            'base_name': 'OS X 10.6.2 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/macosx-universal/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/macosx-universal/xulrunner',
            'src_shark_mozconfig': 'browser/config/mozconfigs/macosx-universal/shark',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx64'],
            'platform_objdir': "%s/i386" % OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx64',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'enable_shark': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'macosx64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
        },
        'win32': {
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/win32/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/win32/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win32',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                # Source server support, bug 506702
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
        },
        'win64': {
            'base_name': 'WINNT 6.1 x86-64 %(branch)s',
            'src_mozconfig': 'browser/config/mozconfigs/win64/nightly',
            'mozconfig': 'win64/%(branch)s/nightly',
            # XXX we cannot build xulrunner on Win64 -- see bug 575912
            'enable_xulrunner': False,
            'profiled_build': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['win64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win64',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86_64-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'win64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows (x64)/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
        },
        'linux-debug': {
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/linux32/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 7,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64-debug': {
            'base_name': 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': False,
            'packageTests': True,
            'build_space': 7,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx-debug': {
            'base_name': 'OS X 10.5.2 %(branch)s leak test',
            'mozconfig': 'macosx/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/macosx32/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 10,
            'slaves': SLAVES['macosx'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx-debug',
            'enable_shared_checkouts': True,
            'enable_shark': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx64-debug': {
            'base_name': 'OS X 10.6.2 %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'enable_leaktests': False,
            'src_mozconfig': 'browser/config/mozconfigs/macosx64/debug',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 10,
            'slaves': SLAVES['macosx64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx64-debug',
            'enable_shared_checkouts': True,
            'enable_shark': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32-debug': {
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/win32/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 9,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win32-debug',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux-android': {
            'base_name': 'Android %(branch)s',
            'mozconfig': 'linux-android/%(branch)s/nightly',
            'src_mozconfig': 'mobile/config/mozconfigs/android/nightly',
            'enable_xulrunner': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'enable_codesighs': False,
            'create_partial': False,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_arm-eabi-gcc3',
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'JAVA_HOME': '/tools/jdk6',
                'PATH': '/tools/jdk6/bin:/opt/local/bin:/tools/python/bin:/tools/buildbot/bin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/home/',
            },
            'enable_opt_unittests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android",
            'stage_product': 'mobile',
            'android_signing': True,
            'post_upload_include_platform': True,
            'multi_locale': True,
            'multi_locale_script': 'scripts/multil10n.py',
        },
        'linux-android-debug': {
            'base_name': 'Android Debug %(branch)s',
            'mozconfig': 'linux-android-debug/%(branch)s/nightly',
            'src_mozconfig': 'mobile/config/mozconfigs/android/debug',
            'enable_xulrunner': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'enable_codesighs': False,
            'enable_leaktests': False,
            'create_snippet': False,
            'create_partial': False,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_arm-eabi-gcc3',
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'JAVA_HOME': '/tools/jdk6',
                'PATH': '/tools/jdk6/bin:/opt/local/bin:/tools/python/bin:/tools/buildbot/bin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/home/',
            },
            'enable_opt_unittests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android-debug",
            'stage_product': 'mobile',
            'android_signing': True,
            'post_upload_include_platform': True,
        },
        'linux-maemo5-gtk': {
            'base_name': 'Maemo 5 GTK %(branch)s',
            'mozconfig': 'linux-maemo5-gtk/%(branch)s/nightly',
            'profiled_build': False,
            'enable_xulrunner': False,
            'use_scratchbox': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'packageTests': True,
            'upload_symbols': True,
            'update_platform': 'Linux_x86-gcc3',
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'enable_codesighs': False,
            'create_snippet': False,
            'create_partial': False,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                #for some reason, broken CC and CXX are in env
                'CC': '/scratchbox/compilers/bin/gcc',
                'CXX': '/scratchbox/compilers/bin/g++',
            },
            'enable_opt_unittests': False,
            'enable_checktests': False,
            'talos_masters': [],#GLOBAL_VARS['talos_masters'],
            'stage_platform': "maemo5-gtk",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
            'multi_locale': True,
            'multi_locale_script': 'scripts/maemo_multi_locale_build.py',
        },
        'linux-maemo5-qt': {
            'base_name': 'Maemo 5 QT %(branch)s',
            'mozconfig': 'linux-maemo5-qt/%(branch)s/nightly',
            'profiled_build': False,
            'enable_xulrunner': False,
            'enable_nightly': False,
            'use_scratchbox': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'packageTests': True,
            'upload_symbols': True,
            'update_platform': 'Linux_x86-gcc3',
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'enable_codesighs': False,
            'create_snippet': False,
            'create_partial': False,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                #for some reason, broken CC and CXX are in env
                'CC': '/scratchbox/compilers/bin/gcc',
                'CXX': '/scratchbox/compilers/bin/g++',
            },
            'enable_opt_unittests': False,
            'enable_checktests': False,
            'talos_masters': [],#GLOBAL_VARS['talos_masters'],
            'stage_platform': "maemo5-qt",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
        },
        'linux-mobile': {
            'base_name': 'Linux Mobile Desktop %(branch)s',
            'mozconfig': 'linux-mobile/%(branch)s/nightly',
            'src_mozconfig': 'mobile/config/mozconfigs/linux-desktop/nightly',
            'profiled_build': False,
            'enable_xulrunner': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'packageTests': True,
            'upload_symbols': True,
            'update_platform': 'Linux_x86-gcc3',
            'create_partial': False,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'enable_codesighs': False,
            'create_snippet': False,
            'create_partial': False,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'is_mobile_l10n': True,
            'l10n_chunks': 5,
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': [],#GLOBAL_VARS['talos_masters'],
            'stage_platform': "linux",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
        },
        'win32-mobile': {
            'base_name': 'WINNT 5.2 Mobile Desktop %(branch)s',
            'mozconfig': 'win32-mobile/%(branch)s/nightly',
            'src_mozconfig': 'mobile/config/mozconfigs/win32-desktop/nightly',
            'profiled_build': False,
            'enable_xulrunner': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'packageTests': True,
            'upload_symbols': True,
            'update_platform': 'WINNT_x86-msvc',
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'enable_ccache': False,
            'enable_codesighs': False,
            'create_snippet': False,
            'create_partial': False,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'is_mobile_l10n': True,
            'l10n_chunks': 5,
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': [],#GLOBAL_VARS['talos_masters'],
            'stage_platform': "win32",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
        },
        'macosx-mobile': {
            'base_name': 'OS X 10.5.2 Mobile Desktop %(branch)s',
            'mozconfig': 'macosx-mobile/%(branch)s/nightly',
            'src_mozconfig': 'mobile/config/mozconfigs/macosx-desktop/nightly',
            'profiled_build': False,
            'enable_xulrunner': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'packageTests': True,
            'upload_symbols': True,
            'update_platform': 'Darwin_x86_64-gcc3',
            'platform_objdir': "%s/i386" % OBJDIR, #needed?
            'slaves': SLAVES['macosx'],
            'platform_objdir': OBJDIR,
            'enable_ccache': False,
            'enable_codesighs': False,
            'create_snippet': False,
            'create_partial': False,
            'enable_shark': False,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'is_mobile_l10n': True,
            'l10n_chunks': 5,
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': [],#GLOBAL_VARS['talos_masters'],
            'stage_platform': "macosx",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
        },
}

PROJECTS = {
    'fuzzing': {
        'platforms': ['linux', 'linux64', 'macosx', 'macosx64', 'win32'],
    },
    'nanojit': {
        'platforms': ['linux', 'linux64', 'macosx', 'macosx64', 'win32', 'arm'],
        'hgurl': 'http://hg.mozilla.org',
        'repo_path': 'projects/nanojit-central',
    },
    'spidermonkey_mozilla-inbound': {
        'platforms': {
            'linux':          ['warnaserr'],
            'linux-debug':    ['nomethodjit', 'notracejit', 'warnaserrdebug'],
            'linux64':        ['warnaserr'],
            'linux64-debug':  ['nomethodjit', 'notracejit', 'warnaserrdebug'],
            'win32':          ['warnaserr'],
            'win32-debug':    ['nomethodjit', 'notracejit', 'warnaserrdebug'],
            'macosx64':       ['warnaserr'],
            'macosx64-debug': ['nomethodjit', 'notracejit', 'dtrace', 'shark', 'warnaserrdebug'],
            'macosx':         ['warnaserr'],
            'macosx-debug':   ['nomethodjit', 'notracejit', 'dtrace', 'shark', 'warnaserrdebug'],
        },
        'env': {
            'linux': PLATFORM_VARS['linux']['env'],
            'linux-debug': PLATFORM_VARS['linux-debug']['env'],
            'linux64': PLATFORM_VARS['linux64']['env'],
            'linux64-debug': PLATFORM_VARS['linux64-debug']['env'],
            'win32': PLATFORM_VARS['win32']['env'],
            'win32-debug': PLATFORM_VARS['win32-debug']['env'],
            'macosx64': PLATFORM_VARS['macosx64']['env'],
            'macosx64-debug': PLATFORM_VARS['macosx64-debug']['env'],
            'macosx': PLATFORM_VARS['macosx']['env'],
            'macosx-debug': PLATFORM_VARS['macosx-debug']['env'],
        },
        'hgurl': 'http://hg.mozilla.org/',
        'repo_path': 'integration/mozilla-inbound',
    },
    'spidermonkey_ionmonkey': {
        'platforms': {
            'linux':          ['warnaserr'],
            'linux-debug':    ['nomethodjit', 'notracejit', 'warnaserrdebug'],
            'linux64':        ['warnaserr'],
            'linux64-debug':  ['nomethodjit', 'notracejit', 'warnaserrdebug'],
            'win32':          ['warnaserr'],
            'win32-debug':    ['nomethodjit', 'notracejit', 'warnaserrdebug'],
            'macosx64':       ['warnaserr'],
            'macosx64-debug': ['nomethodjit', 'notracejit', 'dtrace', 'shark', 'warnaserrdebug'],
            'macosx':         ['warnaserr'],
            'macosx-debug':   ['nomethodjit', 'notracejit', 'dtrace', 'shark', 'warnaserrdebug'],
        },
        'env': {
            'linux': PLATFORM_VARS['linux']['env'],
            'linux-debug': PLATFORM_VARS['linux-debug']['env'],
            'linux64': PLATFORM_VARS['linux64']['env'],
            'linux64-debug': PLATFORM_VARS['linux64-debug']['env'],
            'win32': PLATFORM_VARS['win32']['env'],
            'win32-debug': PLATFORM_VARS['win32-debug']['env'],
            'macosx64': PLATFORM_VARS['macosx64']['env'],
            'macosx64-debug': PLATFORM_VARS['macosx64-debug']['env'],
            'macosx': PLATFORM_VARS['macosx']['env'],
            'macosx-debug': PLATFORM_VARS['macosx-debug']['env'],
        },
        'hgurl': 'http://hg.mozilla.org/',
        'repo_path': 'projects/ionmonkey',
    },
}

for k, v in localconfig.PROJECTS.items():
    if k not in PROJECTS:
        PROJECTS[k] = {}
    for k1, v1 in v.items():
        PROJECTS[k][k1] = v1


# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {
    },
    'shadow-central': {
    },
    'mozilla-release': {
    },
    'mozilla-beta': {
    },
    'mozilla-aurora': {
    },
    'mozilla-1.9.1': {
        'lock_platforms': True,
        'platforms': {
            'linux': {}, 'linux-debug': {}, 'linux64': {}, 'linux64-debug': {},
            'macosx': {}, 'macosx-debug': {}, 'win32': {}, 'win32-debug': {},
        },
    },
    'mozilla-1.9.2': {
        'lock_platforms': True,
        'platforms': {
            'linux': {}, 'linux-debug': {}, 'linux64': {}, 'linux64-debug': {},
            'macosx': {}, 'macosx-debug': {}, 'win32': {}, 'win32-debug': {},
        },
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
        elif key == 'mobile_platforms' and 'mobile_platforms' in BRANCHES[branch]:
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
                if branch in ACTIVE_PROJECT_BRANCHES and PROJECT_BRANCHES[branch].has_key('platforms'):
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
                    PROJECT_BRANCHES[branch]['platforms'].has_key(platform):
                for key, value in PROJECT_BRANCHES[branch]['platforms'][platform].items():
                    BRANCHES[branch]['platforms'][platform][key] = deepcopy(value)

    # Copy in local config
    if branch in localconfig.BRANCHES:
        for key, value in localconfig.BRANCHES[branch].items():
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

    for platform, platform_config in localconfig.PLATFORM_VARS.items():
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
BRANCHES['mozilla-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['mozilla-central']['enable_weekly_bundle'] = True
BRANCHES['mozilla-central']['start_hour'] = [3]
BRANCHES['mozilla-central']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-central']['enable_xulrunner'] = True
# Enable PGO Builds on this branch
BRANCHES['mozilla-central']['enable_pgo'] = True
# Enable unit tests
BRANCHES['mozilla-central']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['mozilla-central']['enable_mac_a11y'] = True
BRANCHES['mozilla-central']['unittest_build_space'] = 6
# And code coverage
BRANCHES['mozilla-central']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
BRANCHES['mozilla-central']['enable_l10n_onchange'] = True
BRANCHES['mozilla-central']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-central']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-central']['l10nDatedDirs'] = True
BRANCHES['mozilla-central']['l10n_tree'] = 'fx37x'
#make sure it has an ending slash
BRANCHES['mozilla-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-central-l10n/'
BRANCHES['mozilla-central']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-central'
BRANCHES['mozilla-central']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-central']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-central' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-central']['enable_multi_locale'] = True
BRANCHES['mozilla-central']['upload_mobile_symbols'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-central']['create_snippet'] = True
BRANCHES['mozilla-central']['update_channel'] = 'nightly'
BRANCHES['mozilla-central']['create_mobile_snippet'] = True
BRANCHES['mozilla-central']['create_partial'] = True
BRANCHES['mozilla-central']['create_partial_l10n'] = True
BRANCHES['mozilla-central']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-central']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_mobile_base_upload_dir'] = '/opt/aus2/incoming/2/Fennec/mozilla-central'
BRANCHES['mozilla-central']['aus2_mobile_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Fennec/mozilla-central'
BRANCHES['mozilla-central']['enable_blocklist_update'] = True
BRANCHES['mozilla-central']['blocklist_update_on_closed_tree'] = False
BRANCHES['mozilla-central']['platforms']['linux-rpm']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['linux64-rpm']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['linux-android-debug']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['linux-android']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-central'
BRANCHES['mozilla-central']['platforms']['macosx64-debug']['enable_leaktests'] = True

######## shadow-central
# custom settings for shadow-central repo
BRANCHES['shadow-central']['hgurl'] = 'https://hgpvt.mozilla.org/'
# have to use complete config repo path so it doesn't look to https://hgpvt.mozilla.org
BRANCHES['shadow-central']['config_repo_path'] = 'http://hg.mozilla.org/build/buildbot-configs'
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['shadow-central']['repo_path'] = 'shadow-central'
BRANCHES['shadow-central']['start_hour'] = [3]
BRANCHES['shadow-central']['start_minute'] = [2]
BRANCHES['shadow-central']['create_snippet'] = False
BRANCHES['shadow-central']['enable_nightly'] = False
# Enable XULRunner / SDK builds
BRANCHES['shadow-central']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['shadow-central']['enable_mac_a11y'] = True
BRANCHES['shadow-central']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['shadow-central']['enable_l10n'] = False
BRANCHES['shadow-central']['l10nNightlyUpdate'] = False
BRANCHES['shadow-central']['l10nDatedDirs'] = False
# need this or master.cfg will bail
BRANCHES['shadow-central']['aus2_base_upload_dir'] = 'fake'
BRANCHES['shadow-central']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'shadow-central'
BRANCHES['shadow-central']['platforms']['linuxqt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'shadow-central'
BRANCHES['shadow-central']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-shadow-central'
BRANCHES['shadow-central']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'shadow-central'
BRANCHES['shadow-central']['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-shadow-central'
BRANCHES['shadow-central']['platforms']['win64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'win64-shadow-central'
BRANCHES['shadow-central']['enable_valgrind'] = False

######## mozilla-release
BRANCHES['mozilla-release']['repo_path'] = 'releases/mozilla-release'
BRANCHES['mozilla-release']['update_channel'] = 'release'
BRANCHES['mozilla-release']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['mozilla-release']['enable_weekly_bundle'] = True
BRANCHES['mozilla-release']['start_hour'] = [3]
BRANCHES['mozilla-release']['start_minute'] = [2]
BRANCHES['mozilla-release']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['mozilla-release']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['mozilla-release']['enable_mac_a11y'] = True
# And code coverage
BRANCHES['mozilla-release']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-release']['enable_l10n'] = False
BRANCHES['mozilla-release']['enable_l10n_onchange'] = True
BRANCHES['mozilla-release']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-release']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-release']['l10nDatedDirs'] = True
BRANCHES['mozilla-release']['l10n_tree'] = 'fxrel'
BRANCHES['mozilla-release']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-release'
BRANCHES['mozilla-release']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-release']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-release' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-release']['enable_multi_locale'] = True
BRANCHES['mozilla-release']['upload_mobile_symbols'] = True
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['mozilla-release']['enable_nightly'] = False
BRANCHES['mozilla-release']['enable_blocklist_update'] = False
BRANCHES['mozilla-release']['blocklist_update_on_closed_tree'] = False
BRANCHES['mozilla-release']['platforms']['linux-android']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-release'
del BRANCHES['mozilla-release']['platforms']['win64']
BRANCHES['mozilla-release']['enable_valgrind'] = False

######## mozilla-beta
BRANCHES['mozilla-beta']['repo_path'] = 'releases/mozilla-beta'
BRANCHES['mozilla-beta']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['mozilla-beta']['enable_weekly_bundle'] = True
BRANCHES['mozilla-beta']['update_channel'] = 'beta'
BRANCHES['mozilla-beta']['start_hour'] = [3]
BRANCHES['mozilla-beta']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-beta']['enable_xulrunner'] = True
# Enable PGO Builds on this branch
BRANCHES['mozilla-beta']['enable_pgo'] = True
# Enable unit tests
BRANCHES['mozilla-beta']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['mozilla-beta']['enable_mac_a11y'] = True
BRANCHES['mozilla-beta']['unittest_build_space'] = 6
# And code coverage
BRANCHES['mozilla-beta']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-beta']['enable_l10n'] = False
BRANCHES['mozilla-beta']['enable_l10n_onchange'] = True
BRANCHES['mozilla-beta']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-beta']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-beta']['l10nDatedDirs'] = True
BRANCHES['mozilla-beta']['l10n_tree'] = 'fxbeta'
#make sure it has an ending slash
BRANCHES['mozilla-beta']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-beta-l10n/'
BRANCHES['mozilla-beta']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-beta'
BRANCHES['mozilla-beta']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-beta']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-beta' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-beta']['enable_multi_locale'] = True
BRANCHES['mozilla-beta']['upload_mobile_symbols'] = True
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['mozilla-beta']['enable_nightly'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-beta']['enable_blocklist_update'] = True
BRANCHES['mozilla-beta']['blocklist_update_on_closed_tree'] = False
BRANCHES['mozilla-beta']['platforms']['linux-android']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-beta'
del BRANCHES['mozilla-beta']['platforms']['win64']
BRANCHES['mozilla-beta']['enable_valgrind'] = False

######## mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = 'releases/mozilla-aurora'
BRANCHES['mozilla-aurora']['l10n_repo_path'] = 'releases/l10n/mozilla-aurora'
BRANCHES['mozilla-aurora']['enable_weekly_bundle'] = True
BRANCHES['mozilla-aurora']['start_hour'] = [4]
BRANCHES['mozilla-aurora']['start_minute'] = [20]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-aurora']['enable_xulrunner'] = True
# Enable PGO Builds on this branch
BRANCHES['mozilla-aurora']['enable_pgo'] = True
# Enable unit tests
BRANCHES['mozilla-aurora']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['mozilla-aurora']['enable_mac_a11y'] = True
BRANCHES['mozilla-aurora']['unittest_build_space'] = 6
# And code coverage
BRANCHES['mozilla-aurora']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-aurora']['enable_l10n'] = True
BRANCHES['mozilla-aurora']['enable_l10n_onchange'] = True
BRANCHES['mozilla-aurora']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-aurora']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-aurora']['l10nDatedDirs'] = True
BRANCHES['mozilla-aurora']['l10n_tree'] = 'fxaurora'
#make sure it has an ending slash
BRANCHES['mozilla-aurora']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-aurora-l10n/'
BRANCHES['mozilla-aurora']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-aurora'
BRANCHES['mozilla-aurora']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-aurora']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-aurora' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-aurora']['enable_multi_locale'] = True
BRANCHES['mozilla-aurora']['upload_mobile_symbols'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-aurora']['create_snippet'] = True
BRANCHES['mozilla-aurora']['update_channel'] = 'aurora'
BRANCHES['mozilla-aurora']['create_mobile_snippet'] = True
BRANCHES['mozilla-aurora']['create_partial'] = True
BRANCHES['mozilla-aurora']['create_partial_l10n'] = True
BRANCHES['mozilla-aurora']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-aurora']['aus2_ssh_key'] = 'ffxbld_dsa'
# use mozilla-aurora-test when disabling updates for merges
BRANCHES['mozilla-aurora']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_mobile_base_upload_dir'] = '/opt/aus2/incoming/2/Fennec/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_mobile_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Fennec/mozilla-aurora'
BRANCHES['mozilla-aurora']['platforms']['linux-android']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-aurora'
BRANCHES['mozilla-aurora']['enable_blocklist_update'] = True
BRANCHES['mozilla-aurora']['blocklist_update_on_closed_tree'] = False
del BRANCHES['mozilla-aurora']['platforms']['win64']
BRANCHES['mozilla-aurora']['enable_valgrind'] = False

######## mozilla-1.9.1
# mozilla-1.9.1 can be removed once we're no longer refreshing MUs from 3.5.18,
# or bug 662298 is fixed.
BRANCHES['mozilla-1.9.1']['repo_path'] = 'releases/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['enable_weekly_bundle'] = True
BRANCHES['mozilla-1.9.1']['brand_name'] = 'Shiretoko'
BRANCHES['mozilla-1.9.1']['start_hour'] = [3]
BRANCHES['mozilla-1.9.1']['start_minute'] = [2]
BRANCHES['mozilla-1.9.1']['use_old_updater'] = True
BRANCHES['mozilla-1.9.1']['platforms']['win32']['build_space'] = 7
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['build_space'] = 7
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.1']['platforms']['linux64-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['build_space'] = 3
# Enable XULRunner / SDK builds
BRANCHES['mozilla-1.9.1']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-1.9.1']['unittest_suites'] = [
    ('mochitests', ['mochitest-plain']),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y']),
    ('reftest', ['reftest']),
    ('crashtest', ['crashtest']),
    ('xpcshell', ['xpcshell']),
]
BRANCHES['mozilla-1.9.1']['platforms']['linux']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['linux']['enable_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['packageTests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux64-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux64-debug']['packageTests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['packageTests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['packageTests'] = False
BRANCHES['mozilla-1.9.1']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.1']['unittest_build_space'] = 5
# L10n configuration
BRANCHES['mozilla-1.9.1']['enable_l10n'] = True
BRANCHES['mozilla-1.9.1']['enable_l10n_onchange'] = True
BRANCHES['mozilla-1.9.1']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['mozilla-1.9.1']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-1.9.1']['l10nDatedDirs'] = False
BRANCHES['mozilla-1.9.1']['l10n_tree'] = 'fx35x'
BRANCHES['mozilla-1.9.1']['l10n_modules'] =  [
    'browser', 'extensions/reporter',
    'other-licenses/branding/firefox', 'netwerk', 'dom', 'toolkit',
    'security/manager',
    ]
#make sure it has an ending slash
BRANCHES['mozilla-1.9.1']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.1-l10n/'
BRANCHES['mozilla-1.9.1']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-1.9.1']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-1.9.1' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-1.9.1']['create_snippet'] = True
BRANCHES['mozilla-1.9.1']['create_partial'] = True
BRANCHES['mozilla-1.9.1']['create_partial_l10n'] = False
BRANCHES['mozilla-1.9.1']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-1.9.1']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['enable_blocklist_update'] = True
BRANCHES['mozilla-1.9.1']['blocklist_update_on_closed_tree'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux']['l10n_check_test'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['l10n_check_test'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['l10n_check_test'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['l10n_check_test'] = False
BRANCHES['mozilla-1.9.1']['enable_valgrind'] = False

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['repo_path'] = 'releases/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['mobile_repo_path'] = 'releases/mobile-1.1'
BRANCHES['mozilla-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['enable_weekly_bundle'] = True
BRANCHES['mozilla-1.9.2']['brand_name'] = 'Namoroka'
BRANCHES['mozilla-1.9.2']['start_hour'] = [3]
BRANCHES['mozilla-1.9.2']['start_minute'] = [32]
BRANCHES['mozilla-1.9.2']['use_old_updater'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux']['build_space'] = 8
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['build_space'] = 8
BRANCHES['mozilla-1.9.2']['platforms']['win32']['build_space'] = 8
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['build_space'] = 7
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['linux64-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['build_space'] = 3
# Enable XULRunner / SDK builds
BRANCHES['mozilla-1.9.2']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-1.9.2']['unittest_suites'] = [
    ('mochitests', ['mochitest-plain']),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y']),
    ('reftest', ['reftest']),
    ('crashtest', ['crashtest']),
    ('xpcshell', ['xpcshell']),
]
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux64-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['win32']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.2']['unittest_build_space'] = 5
# L10n configuration
BRANCHES['mozilla-1.9.2']['enable_l10n'] = True
BRANCHES['mozilla-1.9.2']['enable_l10n_onchange'] = True
BRANCHES['mozilla-1.9.2']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['mozilla-1.9.2']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-1.9.2']['l10nDatedDirs'] = True
BRANCHES['mozilla-1.9.2']['l10n_tree'] = 'fx36x'
BRANCHES['mozilla-1.9.2']['l10n_modules'] =  [
    'browser', 'extensions/reporter',
    'other-licenses/branding/firefox', 'netwerk', 'dom', 'toolkit',
    'security/manager',
    ]
#make sure it has an ending slash
BRANCHES['mozilla-1.9.2']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.2-l10n/'
BRANCHES['mozilla-1.9.2']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-1.9.2']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-1.9.2' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-1.9.2']['create_snippet'] = True
BRANCHES['mozilla-1.9.2']['update_channel'] = 'nightly'
BRANCHES['mozilla-1.9.2']['create_partial'] = True
BRANCHES['mozilla-1.9.2']['create_partial_l10n'] = True
BRANCHES['mozilla-1.9.2']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-1.9.2']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-1.9.2']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['enable_blocklist_update'] = True
BRANCHES['mozilla-1.9.2']['blocklist_update_on_closed_tree'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux']['l10n_check_test'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['l10n_check_test'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['l10n_check_test'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32']['l10n_check_test'] = False
BRANCHES['mozilla-1.9.2']['enable_valgrind'] = False

######## try
# Try-specific configs
BRANCHES['try']['stage_username'] = 'trybld'
BRANCHES['try']['stage_username_mobile'] = 'trybld'
BRANCHES['try']['stage_ssh_key'] = 'trybld_dsa'
BRANCHES['try']['stage_ssh_mobile_key'] = 'trybld_dsa'
BRANCHES['try']['stage_base_path'] = '/home/ftp/pub/firefox/try-builds'
BRANCHES['try']['stage_base_path_mobile'] = '/home/ftp/pub/firefox/try-builds'
BRANCHES['try']['enable_merging'] = False
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['package_dir'] ='%(who)s-%(got_revision)s'
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try']['repo_path'] = 'try'
BRANCHES['try']['start_hour'] = [3]
BRANCHES['try']['start_minute'] = [2]
# Disable Nightly builds
BRANCHES['try']['enable_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['try']['enable_xulrunner'] = False
BRANCHES['try']['enable_mac_a11y'] = True
# only do unittests locally until they are switched over to talos-r3
BRANCHES['try']['enable_l10n'] = False
BRANCHES['try']['enable_l10n_onchange'] = False
BRANCHES['try']['l10nNightlyUpdate'] = False
BRANCHES['try']['l10nDatedDirs'] = False
BRANCHES['try']['enable_codecoverage'] = False
BRANCHES['try']['enable_shark'] = False
BRANCHES['try']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['try']['aus2_base_upload_dir'] = 'fake'
BRANCHES['try']['platforms']['linux']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux64']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['try']['platforms']['linux-rpm']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux64-rpm']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['try']['platforms']['linuxqt']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['win32']['slaves'] = TRY_SLAVES['win32']
BRANCHES['try']['platforms']['win64']['slaves'] = TRY_SLAVES['win64']
BRANCHES['try']['platforms']['macosx64']['slaves'] = TRY_SLAVES['macosx64']
BRANCHES['try']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['try']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win32']
BRANCHES['try']['platforms']['macosx-debug']['slaves'] = TRY_SLAVES['macosx']
BRANCHES['try']['platforms']['macosx64-debug']['slaves'] = TRY_SLAVES['macosx64']
BRANCHES['try']['platforms']['linux-android']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux-android-debug']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux-maemo5-gtk']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux-maemo5-qt']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux-mobile']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['win32-mobile']['slaves'] = TRY_SLAVES['win32']
BRANCHES['try']['platforms']['macosx-mobile']['slaves'] = TRY_SLAVES['macosx']
BRANCHES['try']['platforms']['linux']['upload_symbols'] = False
BRANCHES['try']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['try']['platforms']['linuxqt']['upload_symbols'] = False
BRANCHES['try']['platforms']['macosx64']['upload_symbols'] = False
BRANCHES['try']['platforms']['linux-android']['upload_symbols'] = False
BRANCHES['try']['platforms']['linux-android-debug']['upload_symbols'] = False
BRANCHES['try']['platforms']['linux-maemo5-gtk']['upload_symbols'] = False
BRANCHES['try']['platforms']['linux-maemo5-qt']['upload_symbols'] = False
BRANCHES['try']['platforms']['linux-mobile']['upload_symbols'] = False
BRANCHES['try']['platforms']['win32-mobile']['upload_symbols'] = False
BRANCHES['try']['platforms']['macosx-mobile']['upload_symbols'] = False
BRANCHES['try']['platforms']['win32']['upload_symbols'] = True
BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_USER'] = 'trybld'
BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_PATH'] = '/symbols/windows'
BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_SSH_KEY'] = '/c/Documents and Settings/cltbld/.ssh/trybld_dsa'
BRANCHES['try']['platforms']['win64']['upload_symbols'] = False
for platform in BRANCHES['try']['platforms'].keys():
    # Sadly, the rule that mobile builds go to /mobile/
    # isn't true for try :(
    BRANCHES['try']['platforms'][platform]['stage_product'] = 'firefox'


######## generic branch configs
for branch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[branch]
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['enabled_products'] = branchConfig.get('enabled_products',
                                                            GLOBAL_VARS['enabled_products'])
    BRANCHES[branch]['enable_nightly'] =  branchConfig.get('enable_nightly', False)
    BRANCHES[branch]['enable_mobile'] = branchConfig.get('enable_mobile', True)
    BRANCHES[branch]['enable_pgo'] = branchConfig.get('enable_pgo', False)
    if BRANCHES[branch]['enable_mobile']:
        if branchConfig.get('mobile_platforms'):
            for platform, platform_config in branchConfig['mobile_platforms'].items():
                if platform in ('maemo5-gtk', 'maemo5-qt'):
                    BRANCHES[branch]['mobile_platforms'][platform]['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch + '-' + platform
                else:
                    BRANCHES[branch]['mobile_platforms'][platform]['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
                for key, value in platform_config.items():
                    BRANCHES[branch]['mobile_platforms'][platform][key] = deepcopy(value)
    BRANCHES[branch]['start_hour'] = branchConfig.get('start_hour', [4])
    BRANCHES[branch]['start_minute'] = branchConfig.get('start_minute', [2])
    # Disable XULRunner / SDK builds
    BRANCHES[branch]['enable_xulrunner'] = branchConfig.get('enable_xulrunner', False)
    # Enable unit tests
    BRANCHES[branch]['enable_mac_a11y'] = branchConfig.get('enable_mac_a11y', True)
    BRANCHES[branch]['unittest_build_space'] = branchConfig.get('unittest_build_space', 6)
    BRANCHES[branch]['enable_shark'] = branchConfig.get('enable_shark', False)
    # L10n configuration is not set up for project_branches
    BRANCHES[branch]['enable_l10n'] = branchConfig.get('enable_l10n', False)
    BRANCHES[branch]['l10nNightlyUpdate'] = branchConfig.get('l10nNightlyUpdate', False)
    BRANCHES[branch]['l10nDatedDirs'] = branchConfig.get('l10nDatedDirs', False)
    # nightly updates
    BRANCHES[branch]['create_snippet'] = branchConfig.get('create_snippet', False)
    BRANCHES[branch]['update_channel'] = branchConfig.get('update_channel', 'nightly-%s' % branch)
    BRANCHES[branch]['create_partial'] = branchConfig.get('create_partial', False)
    BRANCHES[branch]['create_partial_l10n'] = branchConfig.get('create_partial_l10n', False)
    BRANCHES[branch]['create_mobile_snippet'] = branchConfig.get('create_mobile_snippet', False)
    BRANCHES[branch]['aus2_user'] = branchConfig.get('aus2_user', 'ffxbld')
    BRANCHES[branch]['aus2_ssh_key'] = branchConfig.get('aus2_ssh_key', 'ffxbld_dsa')
    BRANCHES[branch]['aus2_base_upload_dir'] = branchConfig.get('aus2_base_upload_dir', '/opt/aus2/incoming/2/Firefox/' + branch)
    BRANCHES[branch]['aus2_base_upload_dir_l10n'] = branchConfig.get('aus2_base_upload_dir_l10n', '/opt/aus2/incoming/2/Firefox/' + branch)
    BRANCHES[branch]['aus2_mobile_base_upload_dir'] = branchConfig.get('aus2_mobile_base_upload_dir', '/opt/aus2/incoming/2/Fennec/' + branch)
    BRANCHES[branch]['aus2_mobile_base_upload_dir_l10n'] = branchConfig.get('aus2_mobile_base_upload_dir_l10n', '/opt/aus2/incoming/2/Fennec/' + branch)
    #make sure it has an ending slash
    BRANCHES[branch]['l10nUploadPath'] = \
        '/home/ftp/pub/mozilla.org/firefox/nightly/latest-' + branch + '-l10n/' 
    BRANCHES[branch]['enUS_binaryURL'] = GLOBAL_VARS['download_base_url'] + branchConfig.get('enUS_binaryURL', '')
    if BRANCHES[branch]['platforms'].has_key('linux'):
        BRANCHES[branch]['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
    if BRANCHES[branch]['platforms'].has_key('linux-mobile'):
        BRANCHES[branch]['platforms']['linux-mobile']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux-mobile-' + branch
    if BRANCHES[branch]['platforms'].has_key('linux-android'):
        BRANCHES[branch]['platforms']['linux-android']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-' + branch
    if BRANCHES[branch]['platforms'].has_key('linuxqt'):
        BRANCHES[branch]['platforms']['linuxqt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linuxqt-' + branch
    if BRANCHES[branch]['platforms'].has_key('linux64'):
        BRANCHES[branch]['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-' + branch
    if BRANCHES[branch]['platforms'].has_key('win32'):
        BRANCHES[branch]['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
    if BRANCHES[branch]['platforms'].has_key('win64'):
        BRANCHES[branch]['platforms']['win64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'win64-' + branch
    if BRANCHES[branch]['platforms'].has_key('macosx64'):
        BRANCHES[branch]['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-' + branch
    # point to the mozconfigs, default is generic
    for platform in BRANCHES[branch]['platforms']:
        if platform.endswith('debug') and 'linux-android' not in platform:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform.split('-')[0] + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/debug'
        elif platform.endswith('qt') and 'maemo' not in platform:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = 'linux/' + branchConfig.get('mozconfig_dir', 'generic') + '/qt'
        else:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/nightly'
    BRANCHES[branch]['enable_valgrind'] = False

# Bug 578880, remove the following block after gcc-4.5 switch
branches = BRANCHES.keys()
branches.extend(ACTIVE_PROJECT_BRANCHES)
for branch in ('mozilla-1.9.1', 'mozilla-1.9.2',):
    branches.remove(branch)
for branch in branches:
    if BRANCHES[branch]['platforms'].has_key('linux'):
        BRANCHES[branch]['platforms']['linux']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
        BRANCHES[branch]['platforms']['linux']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if BRANCHES[branch]['platforms'].has_key('linux-mobile'):
        BRANCHES[branch]['platforms']['linux-mobile']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
        BRANCHES[branch]['platforms']['linux-mobile']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if BRANCHES[branch]['platforms'].has_key('linuxqt'):
        BRANCHES[branch]['platforms']['linuxqt']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
        BRANCHES[branch]['platforms']['linuxqt']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if BRANCHES[branch]['platforms'].has_key('linux64'):
        BRANCHES[branch]['platforms']['linux64']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib64'
        BRANCHES[branch]['platforms']['linux64']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
        }
    if BRANCHES[branch]['platforms'].has_key('linux-debug'):
        BRANCHES[branch]['platforms']['linux-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib:%s/dist/bin' % OBJDIR
        BRANCHES[branch]['platforms']['linux-debug']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if BRANCHES[branch]['platforms'].has_key('linux64-debug'):
        BRANCHES[branch]['platforms']['linux64-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib64:%s/dist/bin' % OBJDIR
        BRANCHES[branch]['platforms']['linux64-debug']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
        }

if __name__ == "__main__":
    import sys, pprint
    args = sys.argv[1:]

    if len(args) > 0:
        branches = args
    else:
        branches = BRANCHES.keys()

    for branch in branches:
        print branch
        pprint.pprint(BRANCHES[branch])

    pprint.pprint(PROJECTS)
