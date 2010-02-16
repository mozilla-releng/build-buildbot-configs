from copy import deepcopy

import buildbotcustom.env
reload(buildbotcustom.env)
from buildbotcustom.env import MozillaEnvironments

# This is only used within this file so it doesn't need to be part of the
# big dict
MAC_MINIS = ['moz2-darwin9-slave%02i' % x for x in range(1,38)]
XSERVES   = ['bm-xserve%02i' % x for x in [7,9,11,12,16,17,18,19,21,22]]
WIN32_VMS = ['win32-slave%02i' % x for x in range(1,60)]
WIN32_IXS = ['mw32-ix-slave%02i' % x for x in range(1,26)]
LINUX_VMS = ['moz2-linux-slave%02i' % x for x in range(1,51)]
LINUX_IXS = ['mv-moz2-linux-ix-slave%02i' % x for x in range(1,26)]
SLAVES = {
    'linux': LINUX_VMS + LINUX_IXS,
    'linux64': ['moz2-linux64-slave%02i' % x for x in range(1,13)],
    'win32':  WIN32_VMS + WIN32_IXS,
    'macosx': MAC_MINIS + XSERVES,
}

GLOBAL_VARS = {
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'hgurl': 'http://hg.mozilla.org/',
    'hghost': 'hg.mozilla.org',
    'config_repo_path': 'build/buildbot-configs',
    'config_subdir': 'mozilla2-staging',
    'objdir': 'obj-firefox',
    'objdir_unittests': 'objdir',
    'stage_username': 'ffxbld',
    'stage_username_xulrunner': 'xrbld',
    'stage_server': 'staging-stage.build.mozilla.org',
    'stage_base_path': '/home/ftp/pub/firefox',
    'stage_base_path_xulrunner': '/home/ftp/pub/xulrunner',
    'stage_group': None,
    'stage_ssh_key': 'ffxbld_dsa',
    'stage_ssh_xulrunner_key': 'xrbld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_ffx/',
    'symbol_server_xulrunner_path': '/mnt/netapp/breakpad/symbols_xr/',
    'aus2_user': 'cltbld',
    'aus2_host': 'staging-stage.build.mozilla.org',
    'download_base_url': 'http://staging-stage.build.mozilla.org/pub/mozilla.org/firefox',
    'graph_server': 'graphs-stage.mozilla.org',
    'graph_selector': '/server/collect.cgi',
    'build_tools_repo_path': 'users/stage-ffxbld/tools',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'default_build_space': 5,
    'base_clobber_url': 'http://build.mozilla.org/stage-clobberer/index.php',
    'default_clobber_time': 24*7, # 1 week
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning
    'talos_masters': [
        ('talos-staging-master02.build.mozilla.org:9010', False),
        ('talos-staging-master.mozilla.org:9010', False),
        ('talos-master02.build.mozilla.org:9010', False),
    ],
    # List of unittest masters to notify of new builds to test,
    # and if a failure to notify the master should result in a warning
    'unittest_masters': [('localhost:9010', True, 0),
                         ('localhost:9011', True, 0)],
    'unittest_suites': [
        ('mochitests', ['mochitest-plain']),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
            'mochitest-a11y']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
    ],
    'geriatric_masters': [],
    'geriatric_branches': {},
    'xulrunner_tinderbox_tree': 'MozillaTest',
    'weekly_tinderbox_tree': 'MozillaTest',
    'l10n_tinderbox_tree': 'MozillaStaging',
    'packaged_unittest_tinderbox_tree': 'MozillaTest',
    'platforms': {
        'linux': {},
        'linux64': {},
        'win32': {},
        'macosx': {},
        'linux-debug': {},
        'linux64-debug': {},
        'macosx-debug': {},
        'win32-debug': {},
    },
    'product_name': 'firefox',
    'app_name': 'browser',
    'brand_name': 'Minefield',
    'tinderbox_tree': 'MozillaTest',
    'enable_shark': True,
    'enable_codecoverage': False,
    'enable_nightly': True,
}

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']

PLATFORM_VARS = {
        'linux': {
            'base_name': 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 5,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'staging-stage.build.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_UMASK': '002',
            },
        },
        'linux64': {
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 5,
            'build_space': 6,
            'upload_symbols': False,
            'download_symbols': False,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86_64-gcc3',
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'staging-stage.build.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_UMASK': '002',
            }
        },
        'macosx': {
            'base_name': 'OS X 10.5.2 %(branch)s',
            'mozconfig': 'macosx/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 5,
            'build_space': 8,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx'],
            'platform_objdir': "%s/ppc" % OBJDIR,
            'update_platform': 'Darwin_Universal-gcc3',
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'staging-stage.build.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
            },
        },
        'win32': {
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'profiled_build': True,
            'builds_before_reboot': 5,
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
                'SYMBOL_SERVER_HOST': 'staging-stage.build.mozilla.org',
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                # Source server support, bug 506702
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
            },
        },
        'linux-debug': {
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 5,
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
        },
        'linux64-debug': {
            'base_name': 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 5,
            'download_symbols': False,
            'build_space': 7,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
        },
        'macosx-debug': {
            'base_name': 'OS X 10.5.2 %(branch)s leak test',
            'mozconfig': 'macosx/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 5,
            'download_symbols': True,
            'build_space': 5,
            'slaves': SLAVES['macosx'],
            'platform_objdir': OBJDIR,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
        },
        'win32-debug': {
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 5,
            'download_symbols': True,
            'build_space': 7,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
        },
}

# All branches that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.1': {},
    'mozilla-1.9.2': {},
    'tracemonkey': {},
    'places': {},
    'electrolysis': {'platforms': {
            'linux': {},
            'win32': {},
            'macosx': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx-debug': {},
            'win32-debug': {},
        }},
    'firefox-lorentz': {},
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
BRANCHES['mozilla-central']['unittest_suites'] = [
    # Turn on chunks for mochitests
    ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y', 'mochitest-ipcplugins']),
    ('reftest', ['reftest']),
    ('crashtest', ['crashtest']),
    ('xpcshell', ['xpcshell']),
    ('jsreftest', ['jsreftest']),
]
BRANCHES['mozilla-central']['platforms']['linux']['enable_unittests'] = False
BRANCHES['mozilla-central']['platforms']['linux64']['enable_unittests'] = False
BRANCHES['mozilla-central']['platforms']['macosx']['enable_unittests'] = False
BRANCHES['mozilla-central']['platforms']['win32']['enable_unittests'] = False
BRANCHES['mozilla-central']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux64']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['macosx']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['win32']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['linux64']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['macosx']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['win32']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['linux-debug']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['linux64-debug']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['macosx-debug']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['win32-debug']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['linux-debug']['enable_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux64-debug']['enable_unittests'] = True
BRANCHES['mozilla-central']['platforms']['macosx-debug']['enable_unittests'] = True
BRANCHES['mozilla-central']['platforms']['win32-debug']['enable_unittests'] = True
BRANCHES['mozilla-central']['enable_mac_a11y'] = True
BRANCHES['mozilla-central']['unittest_build_space'] = 6
# And code coverage
BRANCHES['mozilla-central']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
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
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-central'

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
BRANCHES['mozilla-1.9.1']['platforms']['linux']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.1']['unittest_build_space'] = 5
# L10n configuration
BRANCHES['mozilla-1.9.1']['enable_l10n'] = True
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

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['repo_path'] = 'releases/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['brand_name'] = 'Namoroka'
BRANCHES['mozilla-1.9.2']['start_hour'] = [3]
BRANCHES['mozilla-1.9.2']['start_minute'] = [32]
BRANCHES['mozilla-1.9.2']['platforms']['linux']['build_space'] = 5
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['build_space'] = 5
BRANCHES['mozilla-1.9.2']['platforms']['win32']['build_space'] = 7
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['build_space'] = 7
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['linux64-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['build_space'] = 3
# Enable XULRunner / SDK builds
BRANCHES['mozilla-1.9.2']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['win32']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['enable_opt_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['enable_opt_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['win32']['enable_opt_unittests'] = True
BRANCHES['mozilla-1.9.2']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.2']['unittest_build_space'] = 5
# L10n configuration
BRANCHES['mozilla-1.9.2']['enable_l10n'] = True
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
BRANCHES['mozilla-1.9.2']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-1.9.2'

######## tracemonkey
BRANCHES['tracemonkey']['repo_path'] = 'tracemonkey'
BRANCHES['tracemonkey']['start_hour'] = [3]
BRANCHES['tracemonkey']['start_minute'] = [32]
BRANCHES['tracemonkey']['unittest_suites'] = [
    # Turn on chunks for mochitests
    ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y', 'mochitest-ipcplugins']),
    ('reftest', ['reftest']),
    ('crashtest', ['crashtest']),
    ('xpcshell', ['xpcshell']),
    ('jsreftest', ['jsreftest']),
]
BRANCHES['tracemonkey']['platforms']['linux']['build_space'] = 7
BRANCHES['tracemonkey']['platforms']['linux64']['build_space'] = 7
BRANCHES['tracemonkey']['create_snippet'] = False
# Disable XULRunner / SDK builds
BRANCHES['tracemonkey']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['tracemonkey']['platforms']['linux']['enable_unittests'] = False
BRANCHES['tracemonkey']['platforms']['linux64']['enable_unittests'] = False
BRANCHES['tracemonkey']['platforms']['macosx']['enable_unittests'] = False
BRANCHES['tracemonkey']['platforms']['win32']['enable_unittests'] = False
BRANCHES['tracemonkey']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['tracemonkey']['platforms']['linux64']['enable_opt_unittests'] = True
BRANCHES['tracemonkey']['platforms']['macosx']['enable_opt_unittests'] = True
BRANCHES['tracemonkey']['platforms']['win32']['enable_opt_unittests'] = True
BRANCHES['tracemonkey']['platforms']['linux']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux64']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['macosx']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['win32']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux-debug']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux64-debug']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['macosx-debug']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['win32-debug']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux-debug']['enable_unittests'] = True
BRANCHES['tracemonkey']['platforms']['linux64-debug']['enable_unittests'] = True
BRANCHES['tracemonkey']['platforms']['macosx-debug']['enable_unittests'] = True
BRANCHES['tracemonkey']['platforms']['win32-debug']['enable_unittests'] = True
BRANCHES['tracemonkey']['enable_mac_a11y'] = True
BRANCHES['tracemonkey']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['tracemonkey']['enable_l10n'] = False
BRANCHES['tracemonkey']['l10nNightlyUpdate'] = False
BRANCHES['tracemonkey']['l10nDatedDirs'] = False
# need this or the master.cfg will bail
BRANCHES['tracemonkey']['aus2_base_upload_dir'] = 'fake'
BRANCHES['tracemonkey']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['linux64']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['macosx']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['linux-debug']['enable_valgrind_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux64-debug']['enable_valgrind_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-tracemonkey'
BRANCHES['tracemonkey']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'

######## places
BRANCHES['places']['repo_path'] = 'projects/places'
BRANCHES['places']['start_hour'] = [4]
BRANCHES['places']['start_minute'] = [2]
BRANCHES['places']['create_snippet'] = False
BRANCHES['places']['enable_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['places']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['places']['unittest_suites'] = [
    # Turn on chunks for mochitests
    ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y', 'mochitest-ipcplugins']),
    ('reftest', ['reftest']),
    ('crashtest', ['crashtest']),
    ('xpcshell', ['xpcshell']),
    ('jsreftest', ['jsreftest']),
]
BRANCHES['places']['platforms']['linux']['enable_unittests'] = False
BRANCHES['places']['platforms']['linux64']['enable_unittests'] = False
BRANCHES['places']['platforms']['macosx']['enable_unittests'] = False
BRANCHES['places']['platforms']['win32']['enable_unittests'] = False
BRANCHES['places']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['places']['platforms']['linux64']['enable_opt_unittests'] = True
BRANCHES['places']['platforms']['macosx']['enable_opt_unittests'] = True
BRANCHES['places']['platforms']['win32']['enable_opt_unittests'] = True
BRANCHES['places']['platforms']['linux']['enable_checktests'] = True
BRANCHES['places']['platforms']['linux64']['enable_checktests'] = True
BRANCHES['places']['platforms']['macosx']['enable_checktests'] = True
BRANCHES['places']['platforms']['win32']['enable_checktests'] = True
BRANCHES['places']['platforms']['linux-debug']['enable_checktests'] = True
BRANCHES['places']['platforms']['linux64-debug']['enable_checktests'] = True
BRANCHES['places']['platforms']['macosx-debug']['enable_checktests'] = True
BRANCHES['places']['platforms']['win32-debug']['enable_checktests'] = True
BRANCHES['places']['platforms']['linux-debug']['enable_unittests'] = True
BRANCHES['places']['platforms']['linux64-debug']['enable_unittests'] = True
BRANCHES['places']['platforms']['macosx-debug']['enable_unittests'] = True
BRANCHES['places']['platforms']['win32-debug']['enable_unittests'] = True
BRANCHES['places']['enable_mac_a11y'] = True
BRANCHES['places']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['places']['enable_l10n'] = False
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

######## electrolysis
BRANCHES['electrolysis']['repo_path'] = 'projects/electrolysis'
BRANCHES['electrolysis']['start_hour'] = [4]
BRANCHES['electrolysis']['start_minute'] = [2]
BRANCHES['electrolysis']['unittest_suites'].append( ('jsreftest', ['jsreftest']) )
for suite in BRANCHES['electrolysis']['unittest_suites']:
    if suite[0] == 'mochitest-other':
        suite[1].append('mochitest-ipcplugins')
BRANCHES['electrolysis']['create_snippet'] = False
# Disable XULRunner / SDK builds
BRANCHES['electrolysis']['enable_xulrunner'] = False
BRANCHES['electrolysis']['platforms']['win32']['profiled_build'] = False
# Enable unit tests
BRANCHES['electrolysis']['platforms']['linux']['enable_unittests'] = True
BRANCHES['electrolysis']['platforms']['linux64']['enable_unittests'] = True
BRANCHES['electrolysis']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['electrolysis']['platforms']['win32']['enable_unittests'] = True
BRANCHES['electrolysis']['platforms']['linux']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['linux64']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['macosx']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['win32']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['linux-debug']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['linux64-debug']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['macosx-debug']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['win32-debug']['enable_checktests'] = True
BRANCHES['electrolysis']['enable_mac_a11y'] = True
BRANCHES['electrolysis']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['electrolysis']['enable_l10n'] = False
BRANCHES['electrolysis']['l10nNightlyUpdate'] = False
BRANCHES['electrolysis']['l10nDatedDirs'] = False
# need this or the master.cfg will bail
BRANCHES['electrolysis']['aus2_base_upload_dir'] = 'fake'
BRANCHES['electrolysis']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['electrolysis']['platforms']['linux64']['update_platform'] = 'fake'
BRANCHES['electrolysis']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['electrolysis']['platforms']['macosx']['update_platform'] = 'fake'
BRANCHES['electrolysis']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['linux']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
BRANCHES['electrolysis']['platforms']['linux']['unittest-env'] = {
    'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
}
BRANCHES['electrolysis']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['linux64']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
BRANCHES['electrolysis']['platforms']['linux64']['unittest-env'] = {
    'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
}
BRANCHES['electrolysis']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['linux-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib:%s/dist/bin' % OBJDIR
BRANCHES['electrolysis']['platforms']['linux64-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib:%s/dist/bin' % OBJDIR

######## lorentz
BRANCHES['firefox-lorentz']['repo_path'] = 'projects/firefox-lorentz'
BRANCHES['firefox-lorentz']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
BRANCHES['firefox-lorentz']['brand_name'] = 'Lorentz'
BRANCHES['firefox-lorentz']['start_hour'] = [3]
BRANCHES['firefox-lorentz']['start_minute'] = [32]
BRANCHES['firefox-lorentz']['platforms']['linux']['base_name'] = 'Linux lorentz'
BRANCHES['firefox-lorentz']['platforms']['linux64']['base_name'] = 'Linux x86-64 lorentz'
BRANCHES['firefox-lorentz']['platforms']['win32']['base_name'] = 'WINNT 5.2 lorentz'
BRANCHES['firefox-lorentz']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 lorentz'
BRANCHES['firefox-lorentz']['platforms']['linux-debug']['base_name'] = 'Linux lorentz leak test'
BRANCHES['firefox-lorentz']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 lorentz leak test'
BRANCHES['firefox-lorentz']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 lorentz leak test'
BRANCHES['firefox-lorentz']['platforms']['linux']['build_space'] = 5
BRANCHES['firefox-lorentz']['platforms']['linux64']['build_space'] = 5
BRANCHES['firefox-lorentz']['platforms']['win32']['build_space'] = 7
BRANCHES['firefox-lorentz']['platforms']['macosx']['build_space'] = 7
BRANCHES['firefox-lorentz']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['firefox-lorentz']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['firefox-lorentz']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['firefox-lorentz']['create_snippet'] = False
# Enable XULRunner / SDK builds
BRANCHES['firefox-lorentz']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['firefox-lorentz']['platforms']['linux']['enable_unittests'] = True
BRANCHES['firefox-lorentz']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['firefox-lorentz']['platforms']['win32']['enable_unittests'] = True
BRANCHES['firefox-lorentz']['enable_mac_a11y'] = False
BRANCHES['firefox-lorentz']['unittest_build_space'] = 5
# L10n configuration
BRANCHES['firefox-lorentz']['enable_l10n'] = False
BRANCHES['firefox-lorentz']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['firefox-lorentz']['l10nNightlyUpdate'] = False
BRANCHES['firefox-lorentz']['l10nDatedDirs'] = False
BRANCHES['firefox-lorentz']['l10n_tree'] = 'lorentz'
#make sure it has an ending slash
BRANCHES['firefox-lorentz']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-firefox-lorentz'
# need this or the master.cfg will bail
BRANCHES['firefox-lorentz']['aus2_base_upload_dir'] = 'fake'
BRANCHES['firefox-lorentz']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'lorentz'
BRANCHES['firefox-lorentz']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-lorentz'
BRANCHES['firefox-lorentz']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'lorentz'
BRANCHES['firefox-lorentz']['platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'lorentz'

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
