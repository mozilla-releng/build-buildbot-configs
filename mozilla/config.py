from copy import deepcopy

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, TRY_SLAVES

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
    'balrog_credentials_file': 'BuildSlaves.py',
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
        'linux64': {},
        'win32': {},
        'win64': {},
        'macosx64': {},
        'linux-debug': {},
        'linux64-debug': {},
        'macosx-debug': {},
        'macosx64-debug': {},
        'win32-debug': {},
        'android': {},
        'android-armv6': {},
        'android-debug': {},
    },
    'pgo_strategy': None,
    'pgo_platforms': ('linux', 'linux64', 'win32', 'win64'),
    'periodic_pgo_interval': 6, # in hours
    'enable_shark': True,
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
            'browser',
            'dom',
            'extensions/reporter',
            'extensions/spellcheck',
            'netwerk',
            'other-licenses/branding/firefox',
            'security/manager',
            'services/sync',
            'toolkit',
            ],
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
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
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
                'PYTHON26': '/tools/python-2.6.5/bin/python',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux32/releng.manifest'
        },
        'linux64': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
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
                'PYTHON26': '/tools/python-2.6.5/bin/python',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/releng.manifest',
        },
        'macosx64': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'OS X 10.7 %(branch)s',
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
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': "%s/i386" % OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx64',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'enable_shark': False,
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
                'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'mac-dep-signing',
            'dep_signing_servers': 'mac-dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/macosx64/releng.manifest',
            'enable_ccache': True,
        },
        'win32': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/win32/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/win32/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'slaves': SLAVES['win64'],
            'l10n_slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win32',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows (x64)/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}nsis-2.46u;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'enable_pymake': True,
        },
        'win32-metro': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 6.1 metro %(branch)s',
            'mozconfig': 'win32-metro/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/win32-metro/nightly',
            'enable_xulrunner': False,
            'enable_nightly': False,
            'profiled_build': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'enable_installer': True,
            'slaves': SLAVES['win64-metro'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win32-metro',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'enable_shared_checkouts': True,
            'enable_opt_unittests': False,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
            'enable_pymake': True,
            'env': {
                "HG_SHARE_BASE_DIR": 'e:/builds/hg-shared',
                "MOZ_TOOLS": 'C:\\mozilla-build\\moztools',
                "MOZ_OBJDIR": 'obj-firefox',
                "SYMBOL_SERVER_HOST": localconfig.SYMBOL_SERVER_HOST,
                "SYMBOL_SERVER_USER": 'ffxbld',
                "SYMBOL_SERVER_PATH": SYMBOL_SERVER_PATH,
                "POST_SYMBOL_UPLOAD_CMD": SYMBOL_SERVER_POST_UPLOAD_CMD,
                "SYMBOL_SERVER_SSH_KEY": "/c/Users/cltbld/.ssh/ffxbld_dsa",
                "MOZ_CRASHREPORTER_NO_REPORT": '1',
                "PDBSTR_PATH": '/c/Program Files/Debugging Tools for Windows (x64)/srcsrv/pdbstr.exe',
                "TINDERBOX_OUTPUT": '1',
                "VS110COMNTOOLS": 'C:\\Program Files (x86)\\Microsoft Visual Studio 11.0\\Common7\\Tools\\',
                "WINDOWSSDKDIR": 'C:\\Program Files (x86)\\Windows Kits\\8.0\\',
                "PATH": \
                    'C:\\mozilla-build\\wget;' + \
                    'C:\\mozilla-build\\7zip;' + \
                    'C:\\mozilla-build\\blat261\\full;' + \
                    'C:\\mozilla-build\\python;' + \
                    'C:\\mozilla-build\\upx203w;' + \
                    'C:\\mozilla-build\\info-zip;' + \
                    'C:\\mozilla-build\\nsis-2.46u;' + \
                    'C:\\mozilla-build\\nsis-2.22;' + \
                    'C:\\mozilla-build\\nsis-2.33u;' + \
                    'C:\\mozilla-build\\hg;' + \
                    'C:\\mozilla-build\\python\\Scripts;' + \
                    'C:\\mozilla-build\\moztools\\bin;' + \
                    'C:\\mozilla-build\\yasm;' + \
                    'C:\\mozilla-build\\msys\\bin;' + \
                    'C:\\mozilla-build\\msys\\local\\bin;' + \
                    'C:\\mozilla-build\\buildbotve\\scripts;'
                    'C:\\Windows\\System32;' + \
                    'C:\\Windows;' + \
                    'C:\\Windows\\System32\\Wbem;',
            }
        },
        'win64': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 6.1 x86-64 %(branch)s',
            'src_mozconfig': 'browser/config/mozconfigs/win64/nightly',
            'mozconfig': 'win64/%(branch)s/nightly',
            # XXX we cannot build xulrunner on Win64 -- see bug 575912
            'enable_xulrunner': False,
            'profiled_build': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'enable_installer': True,
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
                'PATH': "${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
            'enable_pymake': False,
        },
        'linux-debug': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
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
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux32/releng.manifest',
        },
        'linux64-debug': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
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
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/releng.manifest',
        },
        'macosx-debug': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'OS X 10.7 32-bit %(branch)s leak test',
            'mozconfig': 'macosx/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/macosx32/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 10,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx-debug',
            'enable_shared_checkouts': True,
            'enable_shark': False,
            'enable_ccache': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'LC_ALL': 'C',
                'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'mac-dep-signing',
            'dep_signing_servers': 'mac-dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/macosx32/releng.manifest',
        },
        'macosx64-debug': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'OS X 10.7 64-bit %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'enable_leaktests': True,
            'src_mozconfig': 'browser/config/mozconfigs/macosx64/debug',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 10,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx64-debug',
            'enable_shared_checkouts': True,
            'enable_shark': False,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'LC_ALL': 'C',
                'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'mac-dep-signing',
            'dep_signing_servers': 'mac-dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/macosx64/releng.manifest',
            'enable_ccache': True,
        },
        'win32-debug': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/win32/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'build_space': 9,
            'slaves': SLAVES['win64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win32-debug',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}nsis-2.46u;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'enable_pymake': True,
        },
        'android': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Android %(branch)s',
            'mozconfig': 'android/%(branch)s/nightly',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android/nightly',
            'mobile_dir': 'mobile/android',
            'enable_xulrunner': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'enable_codesighs': False,
            'create_partial': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_arm-eabi-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'use_mock': True,
            'mock_target': 'mozilla-centos6-i386',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial', 'ccache', 'android-sdk15', 'android-sdk16', 'android-ndk5', 'zip', 'java-1.6.0-openjdk-devel', 'zlib-devel', 'glibc-static', 'openssh-clients', "mpfr"],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'JAVA_HOME': '/tools/jdk6',
                'PATH': '/tools/jdk6/bin:/opt/local/bin:/tools/python/bin:/tools/buildbot/bin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/home/',
                'PYTHON26': '/tools/python-2.6.5/bin/python',
            },
            'enable_opt_unittests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android",
            'stage_product': 'mobile',
            'android_signing': True,
            'post_upload_include_platform': True,
            'is_mobile_l10n': True,
            'l10n_chunks': 5,
            'multi_locale': True,
            'multi_locale_script': 'scripts/multil10n.py',
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android/releng.manifest',
        },
        'android-armv6': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'base_name': 'Android Armv6 %(branch)s',
            'mozconfig': 'android-armv6/%(branch)s/nightly',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android-armv6/nightly',
            'mobile_dir': 'mobile/android',
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'packageTests': True,
            'enable_codesighs': False,
            'enable_xulrunner': False,
            'profiled_build': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_arm-eabi-gcc3-armv6',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'use_mock': True,
            'mock_target': 'mozilla-centos6-i386',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial', 'ccache', 'android-sdk15', 'android-sdk16', 'android-ndk5', 'zip', 'java-1.6.0-openjdk-devel', 'zlib-devel', 'glibc-static', 'openssh-clients', "mpfr", "bc"],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'JAVA_HOME': '/tools/jdk6',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/bin:/usr/bin',
                'PYTHON26': '/tools/python-2.6.5/bin/python',
            },
            'enable_opt_unittests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android-armv6",
            'stage_product': 'mobile',
            'android_signing': True,
            'post_upload_include_platform': True,
            'is_mobile_l10n': False,
            'multi_locale': True,
            'multi_locale_script': 'scripts/multil10n.py',
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android-armv6/releng.manifest',
        },
        'android-debug': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Android Debug %(branch)s',
            'mozconfig': 'android-debug/%(branch)s/nightly',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android/debug',
            'mobile_dir': 'mobile/android',
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
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_arm-eabi-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'use_mock': True,
            'mock_target': 'mozilla-centos6-i386',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial', 'ccache', 'android-sdk15', 'android-sdk16', 'android-ndk5', 'zip', 'java-1.6.0-openjdk-devel', 'zlib-devel', 'glibc-static', 'openssh-clients', 'mpfr'],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'JAVA_HOME': '/tools/jdk6',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/bin:/usr/bin',
            },
            'enable_opt_unittests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android-debug",
            'stage_product': 'mobile',
            'android_signing': True,
            'post_upload_include_platform': True,
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android/releng.manifest',
        },
}
# Additional fixups for lion
PLATFORM_VARS["macosx64-lion"] = deepcopy(PLATFORM_VARS["macosx64"])
PLATFORM_VARS["macosx64-lion-debug"] = deepcopy(PLATFORM_VARS["macosx64-debug"])
PLATFORM_VARS["macosx64-lion"]["base_name"] = 'OS X 10.7 %(branch)s'
PLATFORM_VARS["macosx64-lion-debug"]["base_name"] = 'OS X 10.7 64-bit %(branch)s leak test'
PLATFORM_VARS["macosx64-lion"]["slaves"] = SLAVES['macosx64-lion']
PLATFORM_VARS["macosx64-lion-debug"]["slaves"] = SLAVES['macosx64-lion']
PLATFORM_VARS["macosx64-lion"]["enable_shark"] = False
PLATFORM_VARS["macosx64-lion-debug"]["enable_shark"] = False

# begin delete WIN32_ENV and WIN32_DEBUG_ENV for esr10 EOL
WIN32_ENV = {
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
    'BINSCOPE': 'C:\Program Files\Microsoft\SDL BinScope\Binscope.exe',
    'PATH': "${MOZILLABUILD}buildbotve\\scripts;${PATH}",
}
WIN32_DEBUG_ENV = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
    'BINSCOPE': 'C:\Program Files\Microsoft\SDL Binscope\Binscope.exe',
    'PATH': "${MOZILLABUILD}buildbotve\\scripts;${PATH}",
}
# end delete

PROJECTS = {
    'fuzzing': {
        'platforms': ['linux', 'linux64', 'macosx64-lion', 'win32'],
    },
    'nanojit': {
        'platforms': ['linux', 'linux64', 'macosx64-lion', 'win32'],
        'hgurl': 'http://hg.mozilla.org',
        'repo_path': 'projects/nanojit-central',
    },
    'spidermonkey_mozilla-inbound': {
        'platforms': {
            'linux':          ['warnaserr'],
            'linux-debug':    ['warnaserrdebug'],
            'linux64':        ['warnaserr'],
            'linux64-debug':  ['rootanalysis', 'warnaserrdebug'],
            'macosx64-lion':           ['warnaserr'],
            'macosx64-lion-debug':     ['dtrace', 'warnaserrdebug'],
        },
        'env': {
            'linux': PLATFORM_VARS['linux']['env'],
            'linux-debug': PLATFORM_VARS['linux-debug']['env'],
            'linux64': PLATFORM_VARS['linux64']['env'],
            'linux64-debug': PLATFORM_VARS['linux64-debug']['env'],
            'win32': PLATFORM_VARS['win32']['env'],
            'win32-debug': PLATFORM_VARS['win32-debug']['env'],
            'macosx64-lion': PLATFORM_VARS['macosx64-lion']['env'],
            'macosx64-lion-debug': PLATFORM_VARS['macosx64-lion-debug']['env'],
        },
        'hgurl': 'http://hg.mozilla.org/',
        'repo_path': 'integration/mozilla-inbound',
    },
    'spidermonkey_ionmonkey': {
        'platforms': {
            'linux':          ['warnaserr'],
            'linux-debug':    ['warnaserrdebug'],
            'linux64':        ['warnaserr'],
            'linux64-debug':  ['rootanalysis', 'warnaserrdebug'],
            'macosx64-lion':           ['warnaserr'],
            'macosx64-lion-debug':     ['dtrace', 'warnaserrdebug'],
        },
        'env': {
            'linux': PLATFORM_VARS['linux']['env'],
            'linux-debug': PLATFORM_VARS['linux-debug']['env'],
            'linux64': PLATFORM_VARS['linux64']['env'],
            'linux64-debug': PLATFORM_VARS['linux64-debug']['env'],
            'win32': PLATFORM_VARS['win32']['env'],
            'win32-debug': PLATFORM_VARS['win32-debug']['env'],
            'macosx64-lion': PLATFORM_VARS['macosx64-lion']['env'],
            'macosx64-lion-debug': PLATFORM_VARS['macosx64-lion-debug']['env'],
        },
        'hgurl': 'http://hg.mozilla.org/',
        'repo_path': 'projects/ionmonkey',
    },
    'dxr_mozilla-central': {
        'platform': 'mock',
        'repo_path': 'mozilla-central',
        'env': {'HG_SHARE_BASE_DIR': '/builds/hg-shared'},
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
    'mozilla-release': {
    },
    'mozilla-beta': {
    },
    'mozilla-aurora': {
    },
    'mozilla-esr10': {
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux64': {},
            'win32': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
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
                    if key == 'env':
                        value = deepcopy(PLATFORM_VARS[platform]['env'])
                        value.update(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                    else:
                        value = deepcopy(value)
                    BRANCHES[branch]['platforms'][platform][key] = value
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

    if branch in ('mozilla-central', 'mozilla-aurora', 'mozilla-beta', 'mozilla-release',):
        BRANCHES[branch]['platforms']['android']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
        BRANCHES[branch]['platforms']['android-armv6']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-armv6-%s' % branch

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
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'
# Enable unit tests
BRANCHES['mozilla-central']['enable_mac_a11y'] = True
BRANCHES['mozilla-central']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
BRANCHES['mozilla-central']['enable_l10n_onchange'] = True
BRANCHES['mozilla-central']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-central']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-central']['l10nDatedDirs'] = True
BRANCHES['mozilla-central']['l10n_tree'] = 'fxcentral'
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
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_mobile_base_upload_dir'] = '/opt/aus2/incoming/2/Fennec/mozilla-central'
BRANCHES['mozilla-central']['aus2_mobile_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Fennec/mozilla-central'
BRANCHES['mozilla-central']['enable_blocklist_update'] = True
BRANCHES['mozilla-central']['blocklist_update_on_closed_tree'] = False
BRANCHES['mozilla-central']['platforms']['linux']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['linux64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['win32']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['macosx64-debug']['nightly_signing_servers'] = 'mac-nightly-signing'
BRANCHES['mozilla-central']['platforms']['macosx64']['nightly_signing_servers'] = 'mac-nightly-signing'
BRANCHES['mozilla-central']['l10n_extra_configure_args']= ['--with-macbundlename-prefix=Firefox']

######## mozilla-release
BRANCHES['mozilla-release']['repo_path'] = 'releases/mozilla-release'
BRANCHES['mozilla-release']['update_channel'] = 'release'
BRANCHES['mozilla-release']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['mozilla-release']['enable_weekly_bundle'] = True
BRANCHES['mozilla-release']['start_hour'] = [3]
BRANCHES['mozilla-release']['start_minute'] = [2]
BRANCHES['mozilla-release']['enable_xulrunner'] = False
# Enable PGO Builds on this branch
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'
# Enable unit tests
BRANCHES['mozilla-release']['enable_mac_a11y'] = True
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
del BRANCHES['mozilla-release']['platforms']['win64']
BRANCHES['mozilla-release']['enable_valgrind'] = False
BRANCHES['mozilla-release']['enabled_products'] = ['firefox', 'mobile']

######## mozilla-beta
BRANCHES['mozilla-beta']['repo_path'] = 'releases/mozilla-beta'
BRANCHES['mozilla-beta']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['mozilla-beta']['enable_weekly_bundle'] = True
BRANCHES['mozilla-beta']['update_channel'] = 'beta'
BRANCHES['mozilla-beta']['start_hour'] = [3]
BRANCHES['mozilla-beta']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-beta']['enable_xulrunner'] = False
# Enable PGO Builds on this branch
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'
# Enable unit tests
BRANCHES['mozilla-beta']['enable_mac_a11y'] = True
BRANCHES['mozilla-beta']['unittest_build_space'] = 6
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
del BRANCHES['mozilla-beta']['platforms']['win64']
BRANCHES['mozilla-beta']['enable_valgrind'] = False
BRANCHES['mozilla-beta']['platforms']['android']['enable_dep'] = True
BRANCHES['mozilla-beta']['platforms']['android-debug']['enable_dep'] = True
BRANCHES['mozilla-beta']['enabled_products'] = ['firefox', 'mobile']

######## mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = 'releases/mozilla-aurora'
BRANCHES['mozilla-aurora']['l10n_repo_path'] = 'releases/l10n/mozilla-aurora'
BRANCHES['mozilla-aurora']['enable_weekly_bundle'] = True
BRANCHES['mozilla-aurora']['start_hour'] = [4]
BRANCHES['mozilla-aurora']['start_minute'] = [20]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-aurora']['enable_xulrunner'] = True
# Enable PGO Builds on this branch
BRANCHES['mozilla-aurora']['pgo_strategy'] = 'per-checkin'
# Enable unit tests
BRANCHES['mozilla-aurora']['enable_mac_a11y'] = True
BRANCHES['mozilla-aurora']['unittest_build_space'] = 6
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
# use mozilla-aurora-test when disabling updates for merges
BRANCHES['mozilla-aurora']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_mobile_base_upload_dir'] = '/opt/aus2/incoming/2/Fennec/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_mobile_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Fennec/mozilla-aurora'
BRANCHES['mozilla-aurora']['enable_blocklist_update'] = True
BRANCHES['mozilla-aurora']['blocklist_update_on_closed_tree'] = False
del BRANCHES['mozilla-aurora']['platforms']['win64']
BRANCHES['mozilla-aurora']['enable_valgrind'] = False
# aurora nightlies should use our nightly signing server
BRANCHES['mozilla-aurora']['platforms']['linux']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-aurora']['platforms']['linux64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-aurora']['platforms']['win32']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-aurora']['platforms']['macosx64-debug']['nightly_signing_servers'] = 'mac-nightly-signing'
BRANCHES['mozilla-aurora']['platforms']['macosx64']['nightly_signing_servers'] = 'mac-nightly-signing'
BRANCHES['mozilla-aurora']['l10n_extra_configure_args']= ['--with-macbundlename-prefix=Firefox']
BRANCHES['mozilla-aurora']['enabled_products'] = ['firefox', 'mobile']

######## mozilla-esr10
BRANCHES['mozilla-esr10']['repo_path'] = 'releases/mozilla-esr10'
BRANCHES['mozilla-esr10']['update_channel'] = 'nightly-esr10'
BRANCHES['mozilla-esr10']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['mozilla-esr10']['enable_weekly_bundle'] = True
BRANCHES['mozilla-esr10']['start_hour'] = [3]
BRANCHES['mozilla-esr10']['start_minute'] = [45]
BRANCHES['mozilla-esr10']['enable_xulrunner'] = False
BRANCHES['mozilla-esr10']['enable_mac_a11y'] = True
BRANCHES['mozilla-esr10']['pgo_strategy'] = 'per-checkin'
# L10n configuration
BRANCHES['mozilla-esr10']['enable_l10n'] = False
BRANCHES['mozilla-esr10']['enable_l10n_onchange'] = False
BRANCHES['mozilla-esr10']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-esr10']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-esr10']['l10nDatedDirs'] = True
BRANCHES['mozilla-esr10']['l10n_tree'] = 'fxesr10'
BRANCHES['mozilla-esr10']['enable_multi_locale'] = True
BRANCHES['mozilla-esr10']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-esr10'
BRANCHES['mozilla-esr10']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-esr10']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-esr10' % (GLOBAL_VARS['hgurl'])
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['mozilla-esr10']['enable_nightly'] = True
BRANCHES['mozilla-esr10']['create_snippet'] = True
BRANCHES['mozilla-esr10']['create_partial'] = True
# use mozilla-esr10-test when disabling updates for merges
BRANCHES['mozilla-esr10']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-esr10'
BRANCHES['mozilla-esr10']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-esr10'
BRANCHES['mozilla-esr10']['enable_blocklist_update'] = False
BRANCHES['mozilla-esr10']['blocklist_update_on_closed_tree'] = False
BRANCHES['mozilla-esr10']['enable_valgrind'] = False
BRANCHES['mozilla-esr10']['upload_mobile_symbols'] = True
# Delete these lines for esr17
BRANCHES['mozilla-esr10']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-esr10']['platforms']['win32']['env'] = WIN32_ENV
BRANCHES['mozilla-esr10']['platforms']['win32-debug']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-esr10']['platforms']['win32-debug']['env'] = WIN32_DEBUG_ENV
BRANCHES['mozilla-esr10']['platforms']['macosx64']['base_name'] = 'OS X 10.6.2 mozilla-esr10'
BRANCHES['mozilla-esr10']['platforms']['macosx64']['slaves'] = SLAVES['macosx64']
BRANCHES['mozilla-esr10']['platforms']['macosx64']['enable_shark'] = True
BRANCHES['mozilla-esr10']['platforms']['macosx64']['enable_ccache'] = False
BRANCHES['mozilla-esr10']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 mozilla-esr10 leak test'
BRANCHES['mozilla-esr10']['platforms']['macosx-debug']['slaves'] = SLAVES['macosx64']
BRANCHES['mozilla-esr10']['platforms']['macosx-debug']['enable_shark'] = True
BRANCHES['mozilla-esr10']['platforms']['macosx-debug']['enable_ccache'] = False
BRANCHES['mozilla-esr10']['platforms']['macosx64-debug']['base_name'] = 'OS X 10.6.2 mozilla-esr10 leak test'
BRANCHES['mozilla-esr10']['platforms']['macosx64-debug']['slaves'] = SLAVES['macosx64']
BRANCHES['mozilla-esr10']['platforms']['macosx64-debug']['enable_shark'] = True
BRANCHES['mozilla-esr10']['platforms']['macosx64-debug']['enable_ccache'] = False
# End delete

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
BRANCHES['try']['pgo_strategy'] = 'try'
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
BRANCHES['try']['enable_shark'] = False
BRANCHES['try']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['try']['aus2_base_upload_dir'] = 'fake'
BRANCHES['try']['platforms']['linux']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux64']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['try']['platforms']['win32']['slaves'] = TRY_SLAVES['win64']
BRANCHES['try']['platforms']['win64']['slaves'] = TRY_SLAVES['win64']
BRANCHES['try']['platforms']['macosx64']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['try']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win64']
BRANCHES['try']['platforms']['macosx64-debug']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['android']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['android-armv6']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['android-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux']['upload_symbols'] = False
BRANCHES['try']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['try']['platforms']['macosx64']['upload_symbols'] = False
BRANCHES['try']['platforms']['android']['upload_symbols'] = False
BRANCHES['try']['platforms']['android-armv6']['upload_symbols'] = False
BRANCHES['try']['platforms']['android-debug']['upload_symbols'] = False
BRANCHES['try']['platforms']['win32']['upload_symbols'] = True
BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_USER'] = 'trybld'
BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_PATH'] = '/symbols/windows'
BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_SSH_KEY'] = '/c/Documents and Settings/cltbld/.ssh/trybld_dsa'
BRANCHES['try']['platforms']['win64']['upload_symbols'] = False
for platform in BRANCHES['try']['platforms'].keys():
    # Sadly, the rule that mobile builds go to /mobile/
    # isn't true for try :(
    BRANCHES['try']['platforms'][platform]['stage_product'] = 'firefox'

# MERGE day - when FF17 moves into such branch remove it from the list
# MERGE day - when FF17 moves into mozilla-release remove the whole block (including 'try')
for branch in BRANCHES:
    if branch not in ('mozilla-beta', 'mozilla-release', 'mozilla-esr10',) and \
        'macosx-debug' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['macosx-debug']

######## generic branch configs
for branch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[branch]
    BRANCHES[branch]['product_name'] = branchConfig.get('product_name', None)
    BRANCHES[branch]['app_name']     = branchConfig.get('app_name', None)
    BRANCHES[branch]['brand_name']   = branchConfig.get('brand_name', None)
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['enabled_products'] = branchConfig.get('enabled_products',
                                                            GLOBAL_VARS['enabled_products'])
    BRANCHES[branch]['enable_nightly'] =  branchConfig.get('enable_nightly', False)
    BRANCHES[branch]['enable_mobile'] = branchConfig.get('enable_mobile', True)
    BRANCHES[branch]['pgo_strategy'] = branchConfig.get('pgo_strategy', None)
    BRANCHES[branch]['periodic_pgo_interval'] = branchConfig.get('periodic_pgo_interval', 6)
    if BRANCHES[branch]['enable_mobile']:
        if branchConfig.get('mobile_platforms'):
            for platform, platform_config in branchConfig['mobile_platforms'].items():
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
    BRANCHES[branch]['aus2_user'] = branchConfig.get('aus2_user', GLOBAL_VARS['aus2_user'])
    BRANCHES[branch]['aus2_ssh_key'] = branchConfig.get('aus2_ssh_key', GLOBAL_VARS['aus2_ssh_key'])
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
    if BRANCHES[branch]['platforms'].has_key('android'):
        BRANCHES[branch]['platforms']['android']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-' + branch
    if BRANCHES[branch]['platforms'].has_key('android-armv6'):
        BRANCHES[branch]['platforms']['android-armv6']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-armv6-' + branch
    if BRANCHES[branch]['platforms'].has_key('linux64'):
        BRANCHES[branch]['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-' + branch
    if BRANCHES[branch]['platforms'].has_key('win32'):
        BRANCHES[branch]['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
    if BRANCHES[branch]['platforms'].has_key('win64'):
        BRANCHES[branch]['platforms']['win64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'win64-' + branch
    if BRANCHES[branch]['platforms'].has_key('macosx64'):
        BRANCHES[branch]['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-' + branch
    # Platform-specific defaults/interpretation
    for platform in BRANCHES[branch]['platforms']:
        # point to the mozconfigs, default is generic
        if platform.endswith('debug') and 'android' not in platform:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform.split('-')[0] + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/debug'
        else:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/nightly'
        # Project branches should be allowed to override the signing servers.
        # If a branch does not set dep_signing_servers, it should be set to the global default.
        BRANCHES[branch]['platforms'][platform]['dep_signing_servers'] = branchConfig.get('platforms', {}).get(platform, {}).get('dep_signing_servers',
                                                                         PLATFORM_VARS[platform].get('dep_signing_servers'))
        # If a branch does not set nightly_signing_servers, it should be set to its dep signing server,
        # which may have already been set to the global default.
        BRANCHES[branch]['platforms'][platform]['nightly_signing_servers'] = branchConfig.get('platforms', {}).get(platform, {}).get('nightly_signing_servers',
                                                                             BRANCHES[branch]['platforms'][platform]['dep_signing_servers'])
    BRANCHES[branch]['enable_valgrind'] = False

# Bug 578880, remove the following block after gcc-4.5 switch
branches = BRANCHES.keys()
branches.extend(ACTIVE_PROJECT_BRANCHES)
for branch in branches:
    if BRANCHES[branch]['platforms'].has_key('linux'):
        BRANCHES[branch]['platforms']['linux']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
        BRANCHES[branch]['platforms']['linux']['unittest-env'] = {
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

# MERGE DAY delete a branch from this list when FF16 merges in
for b in ('mozilla-release',):
    del BRANCHES[b]['platforms']['android-armv6']

# MERGE DAY
# When Firefox 17 merges into these branches, they can be removed from the list
# NB. mozharness configs will also need updating
for b in ('mozilla-beta', 'mozilla-release', 'mozilla-esr10'):
    for p in ('android', 'android-debug', 'android-armv6'):
        if p not in BRANCHES[b]['platforms']:
            continue
        BRANCHES[b]['platforms'][p]['slaves'] = SLAVES['linux']
        BRANCHES[b]['platforms'][p]['env']['SYMBOL_SERVER_SSH_KEY'] = "/home/cltbld/.ssh/ffxbld_dsa"
        BRANCHES[b]['platforms'][p]['env']['PATH'] = "/tools/jdk6/bin:/opt/local/bin:/tools/python/bin:/tools/buildbot/bin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/home/"
        del BRANCHES[b]['platforms'][p]['use_mock']
        del BRANCHES[b]['platforms'][p]['mock_target']
        del BRANCHES[b]['platforms'][p]['mock_packages']

for b in ('mozilla-aurora', 'mozilla-beta', 'mozilla-release', 'mozilla-esr10'):
    # Disable pymake
    for p in ('win32', 'win32-debug', 'win32-metro', 'win64'):
        if p not in BRANCHES[b]['platforms']:
            continue
        BRANCHES[b]['platforms'][p]['enable_pymake'] = False        

if __name__ == "__main__":
    import sys
    import pprint
    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = dict(BRANCHES.items() + PROJECTS.items())

    for k, v in items.iteritems():
        out = pprint.pformat(v)
        for l in out.splitlines():
             print '%s: %s' % (k, l)
