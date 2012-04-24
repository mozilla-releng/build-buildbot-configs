from copy import deepcopy

from config import GLOBAL_VARS, PLATFORM_VARS

# Note that thunderbird_localconfig.py is symlinked to one of: {production,staging,preproduction}_thunderbird_config.py
import thunderbird_localconfig
reload(thunderbird_localconfig)

# Can't reload this one because it gets reloaded in another file
from localconfig import MAC_SNOW_MINIS, MAC_MINIS, XSERVES, LINUX_VMS, \
                        LINUX_IXS, WIN32_IXS, SLAVES, \
                        TRY_SLAVES

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
PLATFORM_VARS = deepcopy(PLATFORM_VARS)

GLOBAL_VARS['objdir'] = 'obj-tb'
GLOBAL_VARS['stage_username'] = 'tbirdbld'
GLOBAL_VARS['stage_ssh_key'] = 'tbirdbld_dsa'
# etc.
GLOBAL_VARS.update(thunderbird_localconfig.GLOBAL_VARS.copy())

PLATFORM_VARS['linux']['product_name'] = 'thunderbird-test'
PLATFORM_VARS['linux']['app_name'] = 'mailnews'
# etc.
# You can probably do something like this if you really wanted to:
# for p in PLATFORM_VARS:
#     PLATFORM_VARS[p]['product_name'] = 'thunderbird'
#     # etc.


GLOBAL_VARS.update({
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'objdir': 'objdir-tb',
    'objdir_unittests': 'objdir',
    'stage_username': 'tbirdbld',
    'stage_group': None,
    'stage_ssh_key': 'tbirdbld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_tbrd-test/',
    'hg_username': 'tbirdbld',
    'hg_ssh_key': '~cltbld/.ssh/tbirdbld_dsa',
    'unittest_suites': [
        ('xpcshell', ['xpcshell']),
        ('mozmill', ['mozmill']),
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
    },
    'enable_pgo': False,
    'pgo_platforms': ('linux', 'linux64', 'win32'),
    'pgo_strategy': None,
    'periodic_pgo_interval': 6, # in hours
    'product_name': 'thunderbird-test', # Not valid for mobile builds
    'app_name': 'mail',     # Not valid for mobile builds
    'brand_name': 'Daily', # Not valid for mobile builds
    'enable_codecoverage': False,
    'enable_blocklist_update': False,
    'blocklist_update_on_closed_tree': False,
    'enable_nightly': True,
    'enabled_products': ['thunderbird-test'],
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
            'mail',
            'editor',
            'other-licenses/branding/thunderbird',
            'netwerk',
            'dom',
            'toolkit',
            'security/manager',
        ],
    'scratchbox_path': '/builds/scratchbox/moz_scratchbox',
    'scratchbox_home': '/scratchbox/users/cltbld/home/cltbld',
    'use_old_updater': False,
    'mozilla_dir': '/mozilla',
    'leak_target': 'mailbloat',
})

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']
SYMBOL_SERVER_POST_UPLOAD_CMD = GLOBAL_VARS['symbol_server_post_upload_cmd']
builder_prefix = "TB "

PLATFORM_VARS = {
        'linux': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/linux32/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/linux32/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'leak_target': 'mailbloat',
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'linux',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbirdbld_dsa",
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
            'talos_masters': None,
            'test_pretty_names': True,
            'l10n_check_test': False,
        },
        'linuxqt': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux QT %(branch)s',
            'mozconfig': 'linux/%(branch)s/qt',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/linux32/qt',
            'xr_mozconfig': 'linux/%(branch)s/xulrunner-qt',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/linux32/xulrunner-qt',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'leak_target': 'mailbloat',
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'linuxqt',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'enable_nightly': False,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbirdbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
        },
        'linux-rpm': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux RPM %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly-rpm',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/linux32/rpm',
            'enable_nightly': False, # We will explicitly enable for m-c
            'enable_dep': False,
            'enable_xulrunner': False,
            'stage_platform': 'linux-rpm',
            'leak_target': 'mailbloat',
            'mc_patches': [],
            'create_snippet': False,
            'create_partial': False,
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': False,
            'download_symbols': False,
            'packageTests': False, #Done in rpm spec file
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbirdbld_dsa",
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
            'talos_masters': None,
            'unittest_masters': [],
            'test_pretty_names': False,
        },
        'linux64': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/linux64/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/linux64/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'leak_target': 'mailbloat',
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'linux64',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbirdbld_dsa",
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
            'talos_masters': None,
            'test_pretty_names': True,
            'l10n_check_test': False,
        },
        'linux64-rpm': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux RPM x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly-rpm',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/linux64/rpm',
            'enable_nightly': False, # We will explicitly enable for m-c
            'enable_dep': False,
            'enable_xulrunner': False,
            'stage_platform': 'linux64-rpm',
            'leak_target': 'mailbloat',
            'mc_patches': [],
            'create_snippet': False,
            'create_partial': False,
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': False,
            'download_symbols': False,
            'packageTests': False, #Done in rpm spec file
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbirdbld_dsa",
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
            'talos_masters': None,
            'unittest_masters': [],
            'test_pretty_names': False,
        },
        'macosx': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'OS X 10.5.2 %(branch)s',
            'mozconfig': 'macosx/%(branch)s/nightly',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/macosx-universal/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/macosx-universal/xulrunner',
            'src_shark_mozconfig': 'mail/config/mozconfigs/macosx-universal/shark',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'leak_target': 'mailbloat',
            'build_space': 10,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['macosx'],
            'platform_objdir': "%s/ppc" % OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'macosx',
            'update_platform': 'Darwin_Universal-gcc3',
            'enable_shared_checkouts': True,
            'enable_shark': False,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/tbirdbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
        },
        'macosx64': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'OS X 10.6.2 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/macosx-universal/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/macosx-universal/xulrunner',
            'src_shark_mozconfig': 'mail/config/mozconfigs/macosx-universal/shark',
            'packageTests': True,
            'profiled_build': False,
            'leak_target': 'mailbloat',
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx64'],
            'platform_objdir': "%s/i386" % OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'macosx64',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'enable_shark': False,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/tbirdbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'macosx64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'LC_ALL': 'C',
                'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'test_pretty_names': True,
        },
        'win32': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/win32/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/win32/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'leak_target': 'mailbloat',
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'win32',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/tbirdbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                # Source server support, bug 506702
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'test_pretty_names': True,
            'l10n_check_test': False,
        },
        'win64': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'WINNT 6.1 x86-64 %(branch)s',
            'src_mozconfig': 'mail/config/mozconfigs/win64/nightly',
            'mozconfig': 'win64/%(branch)s/nightly',
            'run_alive_tests': False,
            # XXX we cannot build xulrunner on Win64 -- see bug 575912
            'enable_xulrunner': False,
            'profiled_build': True,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'leak_target': 'mailbloat',
            'upload_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['win64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'win64',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86_64-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': thunderbird_localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'tbirdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/tbirdbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'win64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows (x64)/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'test_pretty_names': True,
            'l10n_check_test': False,
        },
        'linux-debug': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/linux32/debug',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'leak_target': 'mailbloat',
            'build_space': 7,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'linux-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
        },
        'linux64-debug': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/linux64/debug',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': False,
            'packageTests': True,
            'leak_target': 'mailbloat',
            'build_space': 7,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'linux64-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
        },
        'macosx-debug': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'OS X 10.5.2 %(branch)s leak test',
            'mozconfig': 'macosx/%(branch)s/debug',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/macosx32/debug',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'leak_target': 'mailbloat',
            'build_space': 10,
            'slaves': SLAVES['macosx'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
            'stage_platform': 'macosx-debug',
            'enable_shared_checkouts': True,
            'enable_shark': False,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
        },
        'macosx64-debug': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'OS X 10.6.2 %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/macosx64/debug',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'leak_target': 'mailbloat',
            'build_space': 10,
            'slaves': SLAVES['macosx64'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
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
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
        },
        'win32-debug': {
            'product_name': 'thunderbird-test',
            'app_name': 'mail',
            'base_name': builder_prefix + 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'run_alive_tests': False,
            'src_mozconfig': 'mail/config/mozconfigs/win32/debug',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'leak_target': 'mailbloat',
            'build_space': 9,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird-test',
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
            'talos_masters': None,
        },
}


# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'comm-central': {
    },
    'comm-aurora': {
    },
    'comm-beta': {
    },
    'comm-release': {
    },
    'comm-esr10': {
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
    'try-comm-central': {
    },
}

for branch in BRANCHES:
    BRANCHES[branch]['l10n_slaves'] = SLAVES

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
                # put default platform set in all branches
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                else:
                    value = deepcopy(value)
                BRANCHES[branch]['platforms'][platform][key] = value

    # Copy in local config
    if branch in thunderbird_localconfig.BRANCHES:
        for key, value in thunderbird_localconfig.BRANCHES[branch].items():
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

    for platform, platform_config in thunderbird_localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value


######## comm-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-central']['moz_repo_path'] = 'mozilla-central'
BRANCHES['comm-central']['mozilla_dir'] = 'mozilla'
BRANCHES['comm-central']['skip_blank_repos'] = True
BRANCHES['comm-central']['call_client_py'] = True
BRANCHES['comm-central']['repo_path'] = 'comm-central'
BRANCHES['comm-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['comm-central']['enable_weekly_bundle'] = True
BRANCHES['comm-central']['start_hour'] = [3]
BRANCHES['comm-central']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['comm-central']['enable_xulrunner'] = False
# Enable PGO Builds on this branch
BRANCHES['comm-central']['enable_pgo'] = True
# Enable unit tests
BRANCHES['comm-central']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['comm-central']['enable_mac_a11y'] = True
BRANCHES['comm-central']['unittest_build_space'] = 6
# And code coverage
BRANCHES['comm-central']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-central']['enable_l10n'] = True
BRANCHES['comm-central']['enable_l10n_onchange'] = True
BRANCHES['comm-central']['l10nNightlyUpdate'] = True
BRANCHES['comm-central']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['comm-central']['l10nDatedDirs'] = True
BRANCHES['comm-central']['l10n_tree'] = 'fx37x'
#make sure it has an ending slash
BRANCHES['comm-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/thunderbird-test/nightly/latest-comm-central-l10n/'
BRANCHES['comm-central']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-central'
BRANCHES['comm-central']['allLocalesFile'] = 'mail/locales/all-locales'
BRANCHES['comm-central']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/thunderbird/l10n/all-locales.comm-central' % (GLOBAL_VARS['hgurl'])
BRANCHES['comm-central']['enable_multi_locale'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central']['create_snippet'] = True
BRANCHES['comm-central']['update_channel'] = 'nightly'
BRANCHES['comm-central']['create_partial'] = True
BRANCHES['comm-central']['create_partial_l10n'] = True
BRANCHES['comm-central']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Thunderbird/comm-central-test'
BRANCHES['comm-central']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Thunderbird/comm-central-test'
BRANCHES['comm-central']['enable_blocklist_update'] = True
BRANCHES['comm-central']['blocklist_update_on_closed_tree'] = False

######## comm-release
BRANCHES['comm-release']['repo_path'] = 'releases/comm-release'
BRANCHES['comm-release']['update_channel'] = 'release'
BRANCHES['comm-release']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['comm-release']['enable_weekly_bundle'] = True
BRANCHES['comm-release']['start_hour'] = [3]
BRANCHES['comm-release']['start_minute'] = [2]
BRANCHES['comm-release']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['comm-release']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['comm-release']['enable_mac_a11y'] = True
# And code coverage
BRANCHES['comm-release']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-release']['enable_l10n'] = False
BRANCHES['comm-release']['enable_l10n_onchange'] = True
BRANCHES['comm-release']['l10nNightlyUpdate'] = False
BRANCHES['comm-release']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['comm-release']['l10nDatedDirs'] = True
BRANCHES['comm-release']['l10n_tree'] = 'fxrel'
BRANCHES['comm-release']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-release'
BRANCHES['comm-release']['allLocalesFile'] = 'mail/locales/all-locales'
BRANCHES['comm-release']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/thunderbird/l10n/all-locales.comm-release' % (GLOBAL_VARS['hgurl'])
BRANCHES['comm-release']['enable_multi_locale'] = True
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['comm-release']['enable_nightly'] = False
BRANCHES['comm-release']['enable_blocklist_update'] = False
BRANCHES['comm-release']['blocklist_update_on_closed_tree'] = False
del BRANCHES['comm-release']['platforms']['win64']
BRANCHES['comm-release']['enable_valgrind'] = False

######## comm-esr10
BRANCHES['comm-esr10']['repo_path'] = 'releases/comm-esr10'
BRANCHES['comm-esr10']['update_channel'] = 'nightly-esr10'
BRANCHES['comm-esr10']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['comm-esr10']['enable_weekly_bundle'] = True
BRANCHES['comm-esr10']['start_hour'] = [3]
BRANCHES['comm-esr10']['start_minute'] = [45]
BRANCHES['comm-esr10']['enable_xulrunner'] = False
BRANCHES['comm-esr10']['enable_mac_a11y'] = True
BRANCHES['comm-esr10']['pgo_strategy'] = 'per-checkin'
# L10n configuration
BRANCHES['comm-esr10']['enable_l10n'] = False
BRANCHES['comm-esr10']['enable_l10n_onchange'] = False
BRANCHES['comm-esr10']['l10nNightlyUpdate'] = False
BRANCHES['comm-esr10']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['comm-esr10']['l10nDatedDirs'] = True
BRANCHES['comm-esr10']['l10n_tree'] = 'fxesr10'
BRANCHES['comm-esr10']['enable_multi_locale'] = True
BRANCHES['comm-esr10']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-esr10'
BRANCHES['comm-esr10']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['comm-esr10']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.comm-esr10' % (GLOBAL_VARS['hgurl'])
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['comm-esr10']['enable_nightly'] = True
BRANCHES['comm-esr10']['create_snippet'] = True
BRANCHES['comm-esr10']['create_partial'] = True
BRANCHES['comm-esr10']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Thunderbird/comm-esr10'
BRANCHES['comm-esr10']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Thunderbird/comm-esr10'
BRANCHES['comm-esr10']['enable_blocklist_update'] = False
BRANCHES['comm-esr10']['blocklist_update_on_closed_tree'] = False
BRANCHES['comm-esr10']['enable_valgrind'] = False

######## comm-beta
BRANCHES['comm-beta']['moz_repo_path'] = 'releases/mozilla-beta'
BRANCHES['comm-beta']['mozilla_dir'] = 'mozilla'
BRANCHES['comm-beta']['skip_blank_repos'] = True
BRANCHES['comm-beta']['call_client_py'] = True
BRANCHES['comm-beta']['repo_path'] = 'releases/comm-beta'
BRANCHES['comm-beta']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['comm-beta']['enable_weekly_bundle'] = True
BRANCHES['comm-beta']['update_channel'] = 'beta'
BRANCHES['comm-beta']['start_hour'] = [3]
BRANCHES['comm-beta']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['comm-beta']['enable_xulrunner'] = False
# Enable PGO Builds on this branch
BRANCHES['comm-beta']['enable_pgo'] = True
# Enable unit tests
BRANCHES['comm-beta']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['comm-beta']['enable_mac_a11y'] = True
BRANCHES['comm-beta']['unittest_build_space'] = 6
# And code coverage
BRANCHES['comm-beta']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-beta']['enable_l10n'] = False
BRANCHES['comm-beta']['enable_l10n_onchange'] = True
BRANCHES['comm-beta']['l10nNightlyUpdate'] = False
BRANCHES['comm-beta']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['comm-beta']['l10nDatedDirs'] = True
BRANCHES['comm-beta']['l10n_tree'] = 'fxbeta'
#make sure it has an ending slash
BRANCHES['comm-beta']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/thunderbird-test/nightly/latest-comm-beta-l10n/'
BRANCHES['comm-beta']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-beta'
BRANCHES['comm-beta']['allLocalesFile'] = 'mail/locales/all-locales'
BRANCHES['comm-beta']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/thunderbird/l10n/all-locales.comm-beta' % (GLOBAL_VARS['hgurl'])
BRANCHES['comm-beta']['enable_multi_locale'] = True
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['comm-beta']['enable_nightly'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-beta']['enable_blocklist_update'] = True
BRANCHES['comm-beta']['blocklist_update_on_closed_tree'] = False
del BRANCHES['comm-beta']['platforms']['win64']
BRANCHES['comm-beta']['enable_valgrind'] = False

######## comm-aurora
BRANCHES['comm-aurora']['moz_repo_path'] = 'releases/mozilla-aurora'
BRANCHES['comm-aurora']['mozilla_dir'] = 'mozilla'
BRANCHES['comm-aurora']['skip_blank_repos'] = True
BRANCHES['comm-aurora']['call_client_py'] = True
BRANCHES['comm-aurora']['repo_path'] = 'releases/comm-aurora'
BRANCHES['comm-aurora']['l10n_repo_path'] = 'releases/l10n/mozilla-aurora'
BRANCHES['comm-aurora']['enable_weekly_bundle'] = True
BRANCHES['comm-aurora']['start_hour'] = [4]
BRANCHES['comm-aurora']['start_minute'] = [20]
# Enable XULRunner / SDK builds
BRANCHES['comm-aurora']['enable_xulrunner'] = False
# Enable PGO Builds on this branch
BRANCHES['comm-aurora']['enable_pgo'] = True
# Enable unit tests
BRANCHES['comm-aurora']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['comm-aurora']['enable_mac_a11y'] = True
BRANCHES['comm-aurora']['unittest_build_space'] = 6
# And code coverage
BRANCHES['comm-aurora']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-aurora']['enable_l10n'] = True
BRANCHES['comm-aurora']['enable_l10n_onchange'] = True
BRANCHES['comm-aurora']['l10nNightlyUpdate'] = True
BRANCHES['comm-aurora']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['comm-aurora']['l10nDatedDirs'] = True
BRANCHES['comm-aurora']['l10n_tree'] = 'fxaurora'
#make sure it has an ending slash
BRANCHES['comm-aurora']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/thunderbird-test/nightly/latest-comm-aurora-l10n/'
BRANCHES['comm-aurora']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-aurora'
BRANCHES['comm-aurora']['allLocalesFile'] = 'mail/locales/all-locales'
BRANCHES['comm-aurora']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/thunderbird/l10n/all-locales.comm-aurora' % (GLOBAL_VARS['hgurl'])
BRANCHES['comm-aurora']['enable_multi_locale'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-aurora']['create_snippet'] = True
BRANCHES['comm-aurora']['update_channel'] = 'aurora'
BRANCHES['comm-aurora']['create_partial'] = True
BRANCHES['comm-aurora']['create_partial_l10n'] = True
# use comm-aurora-test when disabling updates for merges
BRANCHES['comm-aurora']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Thunderbird/comm-aurora'
BRANCHES['comm-aurora']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Thunderbird/comm-aurora'
BRANCHES['comm-aurora']['enable_blocklist_update'] = True
BRANCHES['comm-aurora']['blocklist_update_on_closed_tree'] = False
del BRANCHES['comm-aurora']['platforms']['win64']
BRANCHES['comm-aurora']['enable_valgrind'] = False

######## try
# Try-specific configs
BRANCHES['try-comm-central']['stage_username'] = 'tbirdtry'
BRANCHES['try-comm-central']['stage_ssh_key'] = 'trybld_dsa'
BRANCHES['try-comm-central']['stage_base_path'] = '/home/ftp/pub/thunderbird-test/try-builds'
BRANCHES['try-comm-central']['enable_merging'] = False
BRANCHES['try-comm-central']['enable_try'] = True
BRANCHES['try-comm-central']['package_dir'] ='%(who)s-%(got_revision)s'
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try-comm-central']['repo_path'] = 'try-comm-central'
BRANCHES['try-comm-central']['start_hour'] = [3]
BRANCHES['try-comm-central']['start_minute'] = [2]
# Disable Nightly builds
BRANCHES['try-comm-central']['enable_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['try-comm-central']['enable_xulrunner'] = False
BRANCHES['try-comm-central']['enable_mac_a11y'] = True
# only do unittests locally until they are switched over to talos-r3
BRANCHES['try-comm-central']['enable_l10n'] = False
BRANCHES['try-comm-central']['enable_l10n_onchange'] = False
BRANCHES['try-comm-central']['l10nNightlyUpdate'] = False
BRANCHES['try-comm-central']['l10nDatedDirs'] = False
BRANCHES['try-comm-central']['enable_codecoverage'] = False
BRANCHES['try-comm-central']['enable_shark'] = False
BRANCHES['try-comm-central']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['try-comm-central']['aus2_base_upload_dir'] = 'fake'
BRANCHES['try-comm-central']['platforms']['linux']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try-comm-central']['platforms']['linux64']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['try-comm-central']['platforms']['win32']['slaves'] = TRY_SLAVES['win32']
BRANCHES['try-comm-central']['platforms']['win64']['slaves'] = TRY_SLAVES['win64']
BRANCHES['try-comm-central']['platforms']['macosx64']['slaves'] = TRY_SLAVES['macosx64']
BRANCHES['try-comm-central']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['linux']
BRANCHES['try-comm-central']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['try-comm-central']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win32']
BRANCHES['try-comm-central']['platforms']['macosx-debug']['slaves'] = TRY_SLAVES['macosx']
BRANCHES['try-comm-central']['platforms']['macosx64-debug']['slaves'] = TRY_SLAVES['macosx64']
BRANCHES['try-comm-central']['platforms']['linux']['upload_symbols'] = False
BRANCHES['try-comm-central']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['try-comm-central']['platforms']['macosx64']['upload_symbols'] = False
BRANCHES['try-comm-central']['platforms']['win32']['upload_symbols'] = True
BRANCHES['try-comm-central']['platforms']['win32']['env']['SYMBOL_SERVER_USER'] = 'trybld'
BRANCHES['try-comm-central']['platforms']['win32']['env']['SYMBOL_SERVER_PATH'] = '/symbols/windows'
BRANCHES['try-comm-central']['platforms']['win32']['env']['SYMBOL_SERVER_SSH_KEY'] = '/c/Documents and Settings/cltbld/.ssh/trybld_dsa'
BRANCHES['try-comm-central']['platforms']['win64']['upload_symbols'] = False
for platform in BRANCHES['try-comm-central']['platforms'].keys():
    BRANCHES['try-comm-central']['platforms'][platform]['stage_product'] = 'thunderbird-test'

# Bug 578880, remove the following block after gcc-4.5 switch
branches = BRANCHES.keys()
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
        BRANCHES[branch]['platforms']['linux-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib:%s/mozilla/dist/bin' % OBJDIR
        BRANCHES[branch]['platforms']['linux-debug']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if BRANCHES[branch]['platforms'].has_key('linux64-debug'):
        BRANCHES[branch]['platforms']['linux64-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib64:%s/mozilla/dist/bin' % OBJDIR
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

# need to do things to copy platform/global stuff into BRANCHES here, like config.py does
