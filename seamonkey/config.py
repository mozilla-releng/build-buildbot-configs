from copy import deepcopy

import buildbotcustom.env
reload(buildbotcustom.env)
from buildbotcustom.env import MozillaEnvironments

SLAVES = {
    'linux': ['cb-seamonkey-linux-%02i' % x for x in [1,2,3]] +
             ['cn-sea-qm-centos5-%02i' % x for x in [1]] +
             ['cb-sea-linux-tbox'],
    'linux64': ['cb-seamonkey-linux64-%02i' % x for x in [1]],
    'win32': ['cb-seamonkey-win32-%02i' % x for x in [1,2,3]] +
             ['cn-sea-qm-win2k3-%02i' % x for x in [1]] +
             ['cb-sea-win32-tbox'],
    'macosx': ['cb-sea-miniosx%02i' % x for x in [1,2,3,4,5]],
}


GLOBAL_VARS = {
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'hgurl': 'http://hg.mozilla.org/',
    'hghost': 'hg.mozilla.org',
    'cvsroot': ':ext:seabld@cvs.mozilla.org:/cvsroot', #?
    'config_repo_path': 'build/buildbot-configs',
    'config_subdir': 'seamonkey',
    'irc_bot_name': 'sea-build-bot', #?
    'irc_bot_channels': ['mozbot'], #?
    'objdir': 'objdir',
    'objdir_unittests': 'objdir',
    'stage_username': 'seabld',
    'stage_server': 'stage.mozilla.org',
    'stage_base_path': '/home/ftp/pub/seamonkey',
    'stage_group': 'seamonkey',
    'stage_ssh_key': 'seabld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_sea/',
    'aus2_user': 'seabld',
    'aus2_ssh_key': 'seabld_dsa',
    'aus2_host': 'aus2-community.mozilla.org',
    'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/seamonkey',
    'graph_server': 'graphs.mozilla.org',
    'graph_selector': '/server/collect.cgi',
    'build_tools_repo_path': 'build/tools',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'default_build_space': 5,
    'base_clobber_url': None, # 'http://build.mozilla.org/clobberer/index.php',
    'default_clobber_time': 24*7, # 1 week
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning
    'talos_masters': [],
    # List of unittest masters to notify of new builds to test,
    # and if a failure to notify the master should result in a warning
    'unittest_masters': [('localhost:9010', False, 0)],
    'unittest_suites': [
        ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
            'mochitest-a11y']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
    ],
    # Unittest suites to run directly in the unittest build cycle
    'unittest_exec_xpcshell_suites': False,
    'unittest_exec_reftest_suites': False,
    'unittest_exec_mochi_suites': False,
    'unittest_exec_mozmill_suites': False,
    'geriatric_masters': [],
    'geriatric_branches': {},
    'weekly_tinderbox_tree': 'Testing',
    'l10n_tinderbox_tree': 'Mozilla-l10n',
    'platforms': {
        'linux': {},
        'linux64': {},
        'win32': {},
        'macosx': {},
        'linux-debug': {},
        'macosx-debug': {},
        'win32-debug': {},
    },
    'product_name': 'seamonkey',
    'app_name': 'suite',
    'brand_name': 'SeaMonkey',
    'tinderbox_tree': 'MozillaTest',
    'enable_shark': False,
    'enable_codecoverage': False,
    'enable_nightly': True,
    'hash_type': 'sha512',
    'create_snippet': False,
    'create_partial': False,
    'create_partial_l10n': False,
    'idle_timeout': 60*60*12,     # 12 hours
}

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']

PLATFORM_VARS = {
        'linux': {
            'base_name': 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'mozconfig_dep': 'linux/%(branch)s/dep',
            'profiled_build': False,
            'builds_before_reboot': None,
            'build_space': 7,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86-gcc3',
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'DISPLAY': ':2',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64': {
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'mozconfig_dep': 'linux64/%(branch)s/dep',
            'profiled_build': False,
            'builds_before_reboot': None,
            'build_space': 6,
            'upload_symbols': False,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86_64-gcc3',
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'DISPLAY': ':2',
            },
            'enable_opt_unittests': False,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx': {
            'base_name': 'OS X 10.5 %(branch)s',
            'mozconfig': 'macosx/%(branch)s/nightly',
            'mozconfig_dep': 'macosx/%(branch)s/dep',
            'profiled_build': False,
            'builds_before_reboot': None,
            'build_space': 8,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['macosx'],
            'platform_objdir': "%s/ppc" % OBJDIR,
            'update_platform': 'Darwin_Universal-gcc3',
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/Users/seabld/.ssh/seabld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32': {
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'mozconfig_dep': 'win32/%(branch)s/dep',
            'profiled_build': False,
            'builds_before_reboot': None,
            'build_space': 9,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                # Source server support, bug 506702
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux-debug': {
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig_dep': 'linux/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': None,
            'download_symbols': True,
            'build_space': 7,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
            'enable_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx-debug': {
            'base_name': 'OS X 10.5 %(branch)s leak test',
            'mozconfig_dep': 'macosx/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': None,
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
        'win32-debug': {
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig_dep': 'win32/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': None,
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
    'comm-central-trunk': {},
    'comm-1.9.1': {'platforms': {
            'linux': {},
            'linux64': {},
            'win32': {},
            'macosx': {},
            'linux-debug': {},
        }},
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

######## comm-central-trunk
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-central-trunk']['repo_path'] = 'comm-central'
BRANCHES['comm-central-trunk']['mozilla_repo_path'] = 'mozilla-central'
BRANCHES['comm-central-trunk']['l10n_repo_path'] = 'l10n-central'
BRANCHES['comm-central-trunk']['start_hour'] = [0]
BRANCHES['comm-central-trunk']['start_minute'] = [30]
BRANCHES['comm-central-trunk']['enable_mac_a11y'] = True
BRANCHES['comm-central-trunk']['unittest_build_space'] = 6
# And code coverage
BRANCHES['comm-central-trunk']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-central-trunk']['enable_l10n'] = True
BRANCHES['comm-central-trunk']['enable_l10n_onchange'] = True
BRANCHES['comm-central-trunk']['l10nNightlyUpdate'] = True
BRANCHES['comm-central-trunk']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['comm-central-trunk']['l10nDatedDirs'] = True
BRANCHES['comm-central-trunk']['l10n_tree'] = 'sea21x'
#make sure it has an ending slash
BRANCHES['comm-central-trunk']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-central-trunk-l10n/'
BRANCHES['comm-central-trunk']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-central-trunk'
BRANCHES['comm-central-trunk']['allLocalesFile'] = 'suite/locales/all-locales'
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-trunk']['create_snippet'] = True
BRANCHES['comm-central-trunk']['create_partial'] = True
BRANCHES['comm-central-trunk']['create_partial_l10n'] = True
BRANCHES['comm-central-trunk']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/SeaMonkey/comm-central-trunk'
BRANCHES['comm-central-trunk']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/SeaMonkey/comm-central-trunk'
BRANCHES['comm-central-trunk']['tinderbox_tree'] = 'SeaMonkey'
BRANCHES['comm-central-trunk']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey'

######## comm-1.9.1
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-1.9.1']['repo_path'] = 'releases/comm-1.9.1'
BRANCHES['comm-1.9.1']['mozilla_repo_path'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-1.9.1']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['comm-1.9.1']['start_hour'] = [0]
BRANCHES['comm-1.9.1']['start_minute'] = [0]
BRANCHES['comm-1.9.1']['unittest_suites'] = [
    ('mochitests', ['mochitest-plain']),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y']),
    ('reftest', ['reftest']),
    ('crashtest', ['crashtest']),
    ('xpcshell', ['xpcshell']),
]
BRANCHES['comm-1.9.1']['platforms']['linux']['enable_unittests'] = True
BRANCHES['comm-1.9.1']['platforms']['linux']['enable_opt_unittests'] = False
BRANCHES['comm-1.9.1']['platforms']['linux']['enable_checktests'] = False
BRANCHES['comm-1.9.1']['platforms']['linux']['packageTests'] = False
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['enable_unittests'] = False
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['enable_checktests'] = False
BRANCHES['comm-1.9.1']['platforms']['linux64']['enable_opt_unittests'] = False
BRANCHES['comm-1.9.1']['platforms']['linux64']['enable_checktests'] = False
BRANCHES['comm-1.9.1']['platforms']['linux64']['packageTests'] = False
BRANCHES['comm-1.9.1']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['comm-1.9.1']['platforms']['macosx']['enable_opt_unittests'] = False
BRANCHES['comm-1.9.1']['platforms']['macosx']['enable_checktests'] = False
BRANCHES['comm-1.9.1']['platforms']['macosx']['packageTests'] = False
BRANCHES['comm-1.9.1']['platforms']['win32']['enable_unittests'] = True
BRANCHES['comm-1.9.1']['platforms']['win32']['enable_opt_unittests'] = False
BRANCHES['comm-1.9.1']['platforms']['win32']['enable_checktests'] = False
BRANCHES['comm-1.9.1']['platforms']['win32']['packageTests'] = False
BRANCHES['comm-1.9.1']['unittest_exec_xpcshell_suites'] = True
BRANCHES['comm-1.9.1']['enable_mac_a11y'] = False
BRANCHES['comm-1.9.1']['unittest_build_space'] = 6
# And code coverage
BRANCHES['comm-1.9.1']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-1.9.1']['enable_l10n'] = True
BRANCHES['comm-1.9.1']['l10nNightlyUpdate'] = False
BRANCHES['comm-1.9.1']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['comm-1.9.1']['l10nDatedDirs'] = False
BRANCHES['comm-1.9.1']['l10n_tree'] = 'sea20x'
#make sure it has an ending slash
BRANCHES['comm-1.9.1']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-1.9.1-l10n/'
BRANCHES['comm-1.9.1']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-1.9.1'
BRANCHES['comm-1.9.1']['allLocalesFile'] = 'suite/locales/all-locales'
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-1.9.1']['create_snippet'] = True
BRANCHES['comm-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/build/0/SeaMonkey/comm-1.9.1'
BRANCHES['comm-1.9.1']['aus2_base_upload_dir_l10n'] = '/opt/aus2/build/0/SeaMonkey/comm-1.9.1'
BRANCHES['comm-1.9.1']['tinderbox_tree'] = 'SeaMonkey2.0'
BRANCHES['comm-1.9.1']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey2.0'
