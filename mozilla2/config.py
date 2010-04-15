from copy import deepcopy

import buildbotcustom.env
reload(buildbotcustom.env)
from buildbotcustom.env import MozillaEnvironments

MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in range(1,51)]
MAC_MINIS      = ['moz2-darwin9-slave%02i' % x for x in [2,5,6,7] + range(9,27) + range(29,68)]
XSERVES        = ['bm-xserve%02i' % x for x in [6,7,9,11,12,16,17,18,19,21,22]]
LINUX_VMS      = ['moz2-linux-slave%02i' % x for x in [1,2] + range(5,17) + range(18,51)]
LINUX_IXS      = ['mv-moz2-linux-ix-slave%02i' % x for x in range(2,25)]
WIN32_VMS      = ['win32-slave%02i' % x for x in [1,2] + range(5,21) + range(22,60)]
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in range(2,26)]
SLAVES = {
    'linux':       LINUX_VMS + LINUX_IXS,
    'linux64':     ['moz2-linux64-slave%02i' % x for x in range(1,13)],
    'win32':       WIN32_VMS + WIN32_IXS,
    'macosx':      MAC_MINIS + XSERVES,
    'macosx-snow': MAC_SNOW_MINIS,
}

GLOBAL_VARS = {
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'hgurl': 'http://hg.mozilla.org/',
    'hghost': 'hg.mozilla.org',
    'config_repo_path': 'build/buildbot-configs',
    'config_subdir': 'mozilla2',
    'objdir': 'obj-firefox',
    'objdir_unittests': 'objdir',
    'stage_username': 'ffxbld',
    'stage_username_xulrunner': 'xrbld',
    'stage_server': 'stage.mozilla.org',
    'stage_base_path': '/home/ftp/pub/firefox',
    'stage_base_path_xulrunner': '/home/ftp/pub/xulrunner',
    'stage_group': None,
    'stage_ssh_key': 'ffxbld_dsa',
    'stage_ssh_xulrunner_key': 'xrbld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_ffx/',
    'symbol_server_xulrunner_path': '/mnt/netapp/breakpad/symbols_xr/',
    'aus2_user': 'cltbld',
    'aus2_ssh_key': 'cltbld_dsa',
    'aus2_host': 'aus2-staging.mozilla.org',
    'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox',
    'graph_server': 'graphs.mozilla.org',
    'graph_selector': '/server/collect.cgi',
    'build_tools_repo_path': 'build/tools',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'default_build_space': 5,
    'base_clobber_url': 'http://build.mozilla.org/clobberer/index.php',
    'default_clobber_time': 24*7, # 1 week
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning
    'talos_masters': [
        ('talos-master.mozilla.org:9010', True),
        ('talos-master.mozilla.org:9012', False),
        ('talos-master02.build.mozilla.org:9010', False),
        ('talos-staging-master02.build.mozilla.org:9010', False),
        ('talos-staging-master02.build.mozilla.org:9012', False),
    ],
    # List of unittest masters to notify of new builds to test,
    # and if a failure to notify the master should result in a warning
    'unittest_masters': [('localhost:9010', False, 0),
                         ('talos-master.mozilla.org:9012', False, 0),
                         ('talos-staging-master02.build.mozilla.org:9010', False, 0),
                         ('talos-staging-master02.build.mozilla.org:9012', False, 0),
                        ],
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
    'geriatric_branches': {},
    'xulrunner_tinderbox_tree': 'XULRunner',
    'weekly_tinderbox_tree': 'Testing',
    'l10n_tinderbox_tree': 'Mozilla-l10n',
    'platforms': {
        'linux': {},
        'linux64': {},
        'win32': {},
        'macosx': {},
        'macosx64': {},
        'linux-debug': {},
        'linux64-debug': {},
        'macosx-debug': {},
        'macosx64-debug': {},
        'win32-debug': {},
    },
    'product_name': 'firefox',
    'app_name': 'browser',
    'brand_name': 'Minefield',
    'tinderbox_tree': 'MozillaTest',
    'enable_shark': True,
    'enable_codecoverage': False,
    'enable_nightly': True,
    'hash_type': 'sha512',
    'create_snippet': False,
    'create_partial': False,
    'create_partial_l10n': False,
}

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']

PLATFORM_VARS = {
        'linux': {
            'base_name': 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_UMASK': '002',
            },
            'enable_opt_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64': {
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86_64-gcc3',
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_UMASK': '002',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx': {
            'base_name': 'OS X 10.5.2 %(branch)s',
            'mozconfig': 'macosx/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 8,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx'],
            'platform_objdir': "%s/ppc" % OBJDIR,
            'update_platform': 'Darwin_Universal-gcc3',
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
            },
            'enable_opt_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx64': {
            'base_name': 'OS X 10.6.2 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 8,
            'upload_symbols': False,
            'download_symbols': False,
            'slaves': SLAVES['macosx-snow'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Darwin_x86_64-gcc3',
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
            },
            'enable_opt_unittests': False,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32': {
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'profiled_build': True,
            'builds_before_reboot': 1,
            'build_space': 9,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                # Source server support, bug 506702
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
            },
            'enable_opt_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux-debug': {
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': True,
            'build_space': 7,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_UMASK': '002',
            },
            'enable_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64-debug': {
            'base_name': 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': False,
            'packageTests': True,
            'build_space': 7,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'enable_ccache': False,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_UMASK': '002',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx-debug': {
            'base_name': 'OS X 10.5.2 %(branch)s leak test',
            'mozconfig': 'macosx/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': True,
            'build_space': 5,
            'slaves': SLAVES['macosx'],
            'platform_objdir': OBJDIR,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
            'enable_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx64-debug': {
            'base_name': 'OS X 10.6.2 %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': True,
            'build_space': 5,
            'slaves': SLAVES['macosx-snow'],
            'platform_objdir': OBJDIR,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
            'enable_unittests': False,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32-debug': {
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': True,
            'build_space': 7,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
            'enable_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
}

# All branches that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.1': { 'platforms': { 'linux': {}, 'linux-debug': {}, 
                                      'linux64': {}, 'linux64-debug': {}, 
                                      'macosx': {}, 'macosx-debug': {}, 
                                      'win32': {}, 'win32-debug': {}, 
                                    },
                     },
    'mozilla-1.9.2': { 'platforms': { 'linux': {}, 'linux-debug': {}, 
                                      'linux64': {}, 'linux64-debug': {}, 
                                      'macosx': {}, 'macosx-debug': {}, 
                                      'win32': {}, 'win32-debug': {}, 
                                    },
                     },
    'tracemonkey': {},
    'places': {},
    'electrolysis': {},
    'addonsmgr': {},
}

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['mozilla-central']['start_hour'] = [3]
BRANCHES['mozilla-central']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-central']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-central']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['mozilla-central']['geriatric_branches'] = {
    'win32': ['p3-win-unit'],
    'linux': ['p3-linux-unit'],
    'macosx': ['g4-leopard-unit', 'g4-tiger-unit'],
}
BRANCHES['mozilla-central']['enable_mac_a11y'] = True
BRANCHES['mozilla-central']['unittest_build_space'] = 6
# And code coverage
BRANCHES['mozilla-central']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
BRANCHES['mozilla-central']['enable_l10n_onchange'] = True
BRANCHES['mozilla-central']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-central']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['mozilla-central']['l10nDatedDirs'] = True
BRANCHES['mozilla-central']['l10n_tree'] = 'fx37x'
#make sure it has an ending slash
BRANCHES['mozilla-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-central-l10n/'
BRANCHES['mozilla-central']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-central'
BRANCHES['mozilla-central']['allLocalesFile'] = 'browser/locales/all-locales'
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-central']['create_snippet'] = True
BRANCHES['mozilla-central']['create_partial'] = True
BRANCHES['mozilla-central']['create_partial_l10n'] = True
BRANCHES['mozilla-central']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-central']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['tinderbox_tree'] = 'Firefox'
BRANCHES['mozilla-central']['packaged_unittest_tinderbox_tree'] = 'Firefox'
BRANCHES['mozilla-central']['platforms']['macosx-debug']['enable_unittests'] = False
BRANCHES['mozilla-central']['platforms']['macosx-debug']['packageTests'] = True
BRANCHES['mozilla-central']['platforms']['macosx']['enable_opt_unittests'] = False
BRANCHES['mozilla-central']['platforms']['macosx']['packageTests'] = True

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['repo_path'] = 'releases/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['brand_name'] = 'Shiretoko'
BRANCHES['mozilla-1.9.1']['start_hour'] = [3]
BRANCHES['mozilla-1.9.1']['start_minute'] = [2]
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
BRANCHES['mozilla-1.9.1']['platforms']['linux64-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.1']['unittest_build_space'] = 5
# L10n configuration
BRANCHES['mozilla-1.9.1']['enable_l10n'] = True
BRANCHES['mozilla-1.9.1']['enable_l10n_onchange'] = True
BRANCHES['mozilla-1.9.1']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['mozilla-1.9.1']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-1.9.1']['l10nDatedDirs'] = False
BRANCHES['mozilla-1.9.1']['l10n_tree'] = 'fx35x'
#make sure it has an ending slash
BRANCHES['mozilla-1.9.1']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.1-l10n/'
BRANCHES['mozilla-1.9.1']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-1.9.1']['create_snippet'] = True
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir_l10n'] = '/opt/aus2/build/0/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['tinderbox_tree'] = 'Firefox3.5'
BRANCHES['mozilla-1.9.1']['packaged_unittest_tinderbox_tree'] = 'Firefox3.5'

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['repo_path'] = 'releases/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['brand_name'] = 'Namoroka'
BRANCHES['mozilla-1.9.2']['start_hour'] = [3]
BRANCHES['mozilla-1.9.2']['start_minute'] = [32]
BRANCHES['mozilla-1.9.2']['platforms']['linux']['build_space'] = 5
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['build_space'] = 5
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
#make sure it has an ending slash
BRANCHES['mozilla-1.9.2']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.2-l10n/'
BRANCHES['mozilla-1.9.2']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-1.9.2']['create_snippet'] = True
BRANCHES['mozilla-1.9.2']['create_partial'] = True
BRANCHES['mozilla-1.9.2']['create_partial_l10n'] = True
BRANCHES['mozilla-1.9.2']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-1.9.2']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-1.9.2']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['tinderbox_tree'] = 'Firefox3.6'
BRANCHES['mozilla-1.9.2']['packaged_unittest_tinderbox_tree'] = 'Firefox3.6'

######## tracemonkey
BRANCHES['tracemonkey']['repo_path'] = 'tracemonkey'
BRANCHES['tracemonkey']['start_hour'] = [3]
BRANCHES['tracemonkey']['start_minute'] = [32]
BRANCHES['tracemonkey']['platforms']['linux']['build_space'] = 7
BRANCHES['tracemonkey']['platforms']['linux64']['build_space'] = 7
# Disable XULRunner / SDK builds
BRANCHES['tracemonkey']['enable_xulrunner'] = False
BRANCHES['tracemonkey']['enable_mac_a11y'] = True
BRANCHES['tracemonkey']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['tracemonkey']['enable_l10n'] = False
BRANCHES['tracemonkey']['enable_l10n_onchange'] = False
BRANCHES['tracemonkey']['l10nNightlyUpdate'] = False
BRANCHES['tracemonkey']['l10nDatedDirs'] = False
BRANCHES['tracemonkey']['platforms']['linux-debug']['enable_valgrind_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux64-debug']['enable_valgrind_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-tracemonkey'
BRANCHES['tracemonkey']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['create_snippet'] = True
BRANCHES['tracemonkey']['create_partial'] = True
BRANCHES['tracemonkey']['create_partial_l10n'] = False
BRANCHES['tracemonkey']['aus2_user'] = 'ffxbld'
BRANCHES['tracemonkey']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['tracemonkey']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/tracemonkey'
BRANCHES['tracemonkey']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/tracemonkey'
BRANCHES['tracemonkey']['tinderbox_tree'] = 'TraceMonkey'
BRANCHES['tracemonkey']['packaged_unittest_tinderbox_tree'] = 'TraceMonkey'

######## places
BRANCHES['places']['repo_path'] = 'projects/places'
BRANCHES['places']['start_hour'] = [4]
BRANCHES['places']['start_minute'] = [2]
BRANCHES['places']['create_snippet'] = False
BRANCHES['places']['enable_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['places']['enable_xulrunner'] = False
BRANCHES['places']['enable_mac_a11y'] = True
BRANCHES['places']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['places']['enable_l10n'] = False
BRANCHES['places']['enable_l10n_onchange'] = False
# need this or the master.cfg will bail
BRANCHES['places']['aus2_base_upload_dir'] = 'fake'
BRANCHES['places']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['linux64']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['macosx']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'places'
BRANCHES['places']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-places'
BRANCHES['places']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'places'
BRANCHES['places']['platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'places'
BRANCHES['places']['platforms']['linux64']['build_space'] = 6
BRANCHES['places']['platforms']['linux']['build_space'] = 6
BRANCHES['places']['tinderbox_tree'] = 'Places'
BRANCHES['places']['packaged_unittest_tinderbox_tree'] = 'Places'

######## electrolysis
BRANCHES['electrolysis']['repo_path'] = 'projects/electrolysis'
BRANCHES['electrolysis']['start_hour'] = [4]
BRANCHES['electrolysis']['start_minute'] = [2]
# Disable XULRunner / SDK builds
BRANCHES['electrolysis']['enable_xulrunner'] = False
BRANCHES['electrolysis']['platforms']['win32']['profiled_build'] = False
BRANCHES['electrolysis']['enable_mac_a11y'] = True
BRANCHES['electrolysis']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['electrolysis']['enable_l10n'] = False
BRANCHES['electrolysis']['enable_l10n_onchange'] = False
BRANCHES['electrolysis']['l10nNightlyUpdate'] = False
BRANCHES['electrolysis']['l10nDatedDirs'] = False
BRANCHES['electrolysis']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['linux']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
BRANCHES['electrolysis']['platforms']['linux']['unittest-env'] = {
    'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
}
BRANCHES['electrolysis']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['linux-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib:%s/dist/bin' % OBJDIR
BRANCHES['electrolysis']['platforms']['linux64-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib:%s/dist/bin' % OBJDIR
BRANCHES['electrolysis']['create_snippet'] = True
BRANCHES['electrolysis']['create_partial'] = True
BRANCHES['electrolysis']['create_partial_l10n'] = False
BRANCHES['electrolysis']['aus2_user'] = 'ffxbld'
BRANCHES['electrolysis']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['electrolysis']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/electrolysis'
BRANCHES['electrolysis']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/electrolysis'
BRANCHES['electrolysis']['tinderbox_tree'] = 'Electrolysis'
BRANCHES['electrolysis']['packaged_unittest_tinderbox_tree'] = 'Electrolysis'

######## addonsmgr
BRANCHES['addonsmgr']['repo_path'] = 'projects/addonsmgr'
BRANCHES['addonsmgr']['start_hour'] = [4]
BRANCHES['addonsmgr']['start_minute'] = [2]
BRANCHES['addonsmgr']['enable_nightly'] = False
BRANCHES['addonsmgr']['create_snippet'] = False
# Disable XULRunner / SDK builds
BRANCHES['addonsmgr']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['addonsmgr']['platforms']['linux64']['enable_checktests'] = True
BRANCHES['addonsmgr']['enable_mac_a11y'] = True
BRANCHES['addonsmgr']['enable_shark'] = False
# L10n configuration
BRANCHES['addonsmgr']['enable_l10n'] = False
BRANCHES['addonsmgr']['l10nNightlyUpdate'] = False
BRANCHES['addonsmgr']['l10nDatedDirs'] = False
# need this or the master.cfg will bail
BRANCHES['addonsmgr']['aus2_base_upload_dir'] = 'fake'
BRANCHES['addonsmgr']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'addonsmgr'
BRANCHES['addonsmgr']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-addonsmgr'
BRANCHES['addonsmgr']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'addonsmgr'
BRANCHES['addonsmgr']['platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'addonsmgr'
BRANCHES['addonsmgr']['tinderbox_tree'] = 'AddonsMgr'
BRANCHES['addonsmgr']['packaged_unittest_tinderbox_tree'] = 'AddonsMgr'
 
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
