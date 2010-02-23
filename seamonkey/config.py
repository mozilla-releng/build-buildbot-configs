from copy import deepcopy

import buildbotcustom.env
reload(buildbotcustom.env)
from buildbotcustom.env import MozillaEnvironments

SLAVES = {
    'linux': ['cb-seamonkey-linux-%02i' % x for x in [1,2]] +
             ['cb-seamonkey-linuxdebug-%02i' % x for x in [1]] +
             ['cn-sea-qm-centos5-%02i' % x for x in [1]] +
             ['cb-sea-linux-tbox'],
    'linux64': ['cb-seamonkey-linux64-%02i' % x for x in [1]],
    'win32': ['cb-seamonkey-win32-%02i' % x for x in [1,2]] +
             ['cn-sea-qm-win2k3-%02i' % x for x in [1]] +
             ['cb-sea-win32-tbox'],
    'macosx': ['cb-sea-miniosx%02i' % x for x in [1,2,3,4,5]],
}


# Everything in this list will be set in the branch dict at the end of this file
# For example,
#  BRANCHES['mozilla-central']['hgurl'] = HGURL
#  BRANCHES['mozilla-central']['hghost'] = HGHOST
#  ...
BRANCH_LEVEL_VARS = {
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
        ('mochitests', ['mochitest-plain']),
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
}

# shorthand, because these are used often
OBJDIR = BRANCH_LEVEL_VARS['objdir']
SYMBOL_SERVER_PATH = BRANCH_LEVEL_VARS['symbol_server_path']

# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-central-trunk': {},
    'comm-1.9.1': {},
    'comm-1.9.2': {},
}

# We copy the global vars in first, so branches can override them if they want to
for branch in BRANCHES.keys():
    for attr in BRANCH_LEVEL_VARS.keys():
        BRANCHES[branch][attr] = deepcopy(BRANCH_LEVEL_VARS[attr])

######## comm-central-trunk
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-central-trunk']['repo_path'] = 'comm-central'
BRANCHES['comm-central-trunk']['mozilla_repo_path'] = 'mozilla-central'
BRANCHES['comm-central-trunk']['l10n_repo_path'] = 'l10n-central'
BRANCHES['comm-central-trunk']['major_version'] = '1.9.3'
BRANCHES['comm-central-trunk']['product_name'] = 'seamonkey'
BRANCHES['comm-central-trunk']['app_name'] = 'suite'
BRANCHES['comm-central-trunk']['brand_name'] = 'SeaMonkey'
BRANCHES['comm-central-trunk']['start_hour'] = [0]
BRANCHES['comm-central-trunk']['start_minute'] = [30]
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-trunk']['platforms'] = {
    'linux': {},
    'linux64': {},
    'macosx': {},
    'win32': {},
    'linux-debug': {},
    'macosx-debug': {},
    'win32-debug': {},
}
# The mozconfig file to use, relative to CONFIG_REPO_URL/CONFIG_SUBDIR
BRANCHES['comm-central-trunk']['platforms']['linux']['mozconfig_dep'] = 'linux/comm-central-trunk/dep'
BRANCHES['comm-central-trunk']['platforms']['linux64']['mozconfig_dep'] = 'linux64/comm-central-trunk/dep'
BRANCHES['comm-central-trunk']['platforms']['macosx']['mozconfig_dep'] = 'macosx/comm-central-trunk/dep'
BRANCHES['comm-central-trunk']['platforms']['win32']['mozconfig_dep'] = 'win32/comm-central-trunk/dep'
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['mozconfig_dep'] = 'linux/comm-central-trunk/debug'
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['mozconfig_dep'] = 'macosx/comm-central-trunk/debug'
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['mozconfig_dep'] = 'win32/comm-central-trunk/debug'
# nightly mozconfig (not for debug builds)
BRANCHES['comm-central-trunk']['platforms']['linux']['mozconfig'] = 'linux/comm-central-trunk/nightly'
BRANCHES['comm-central-trunk']['platforms']['linux64']['mozconfig'] = 'linux64/comm-central-trunk/nightly'
BRANCHES['comm-central-trunk']['platforms']['macosx']['mozconfig'] = 'macosx/comm-central-trunk/nightly'
BRANCHES['comm-central-trunk']['platforms']['win32']['mozconfig'] = 'win32/comm-central-trunk/nightly'
BRANCHES['comm-central-trunk']['platforms']['linux']['base_name'] = 'Linux comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['linux64']['base_name'] = 'Linux x86-64 comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['macosx']['base_name'] = 'OS X 10.5 comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['base_name'] = 'Linux comm-central-trunk leak test'
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5 comm-central-trunk leak test'
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 comm-central-trunk leak test'
BRANCHES['comm-central-trunk']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['linux64']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['linux']['build_space'] = 7
BRANCHES['comm-central-trunk']['platforms']['linux64']['build_space'] = 5
BRANCHES['comm-central-trunk']['platforms']['macosx']['build_space'] = 5
BRANCHES['comm-central-trunk']['platforms']['win32']['build_space'] = 8
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['build_space'] = 3
BRANCHES['comm-central-trunk']['platforms']['linux']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['linux64']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['macosx']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['win32']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['builds_before_reboot'] = None
# Enable Nightly builds
BRANCHES['comm-central-trunk']['enable_nightly'] = True
# Enable unit tests
BRANCHES['comm-central-trunk']['unittest_suites'] = [
#    ('mochitests', ['mochitest-plain']),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y']),
    ('xpcshell', ['xpcshell']),
]
BRANCHES['comm-central-trunk']['platforms']['linux']['enable_unittests'] = False
BRANCHES['comm-central-trunk']['platforms']['macosx']['enable_unittests'] = False
BRANCHES['comm-central-trunk']['platforms']['win32']['enable_unittests'] = False
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['enable_unittests'] = True
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['enable_unittests'] = True
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['enable_unittests'] = False
BRANCHES['comm-central-trunk']['enable_mac_a11y'] = True
BRANCHES['comm-central-trunk']['platforms']['linux']['crashtest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['macosx']['crashtest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['comm-central-trunk']['platforms']['linux']['mochitest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['macosx']['mochitest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['comm-central-trunk']['platforms']['linux']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['macosx']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['win32']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['linux']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['macosx']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['win32']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['unittest_build_space'] = 6
# And code coverage
BRANCHES['comm-central-trunk']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-central-trunk']['enable_l10n'] = True
BRANCHES['comm-central-trunk']['l10nNightlyUpdate'] = True
BRANCHES['comm-central-trunk']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['comm-central-trunk']['l10nDatedDirs'] = True
BRANCHES['comm-central-trunk']['l10n_tree'] = 'sea21x'
#make sure it has an ending slash
BRANCHES['comm-central-trunk']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-central-trunk-l10n/'
BRANCHES['comm-central-trunk']['enUS_binaryURL'] = \
    BRANCH_LEVEL_VARS['download_base_url'] + '/nightly/latest-comm-central-trunk'
BRANCHES['comm-central-trunk']['allLocalesFile'] = 'suite/locales/all-locales'
# nightly shark build for profiling
BRANCHES['comm-central-trunk']['enable_shark'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-trunk']['create_snippet'] = True
BRANCHES['comm-central-trunk']['aus2_base_upload_dir'] = '/opt/aus2/build/0/SeaMonkey/comm-central-trunk'
BRANCHES['comm-central-trunk']['idle_timeout'] = 60*60*6   # 6 hours
# We're actually using gcc4, but the platform hardcodes gcc3
BRANCHES['comm-central-trunk']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-trunk']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['comm-central-trunk']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['comm-central-trunk']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-trunk']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['tinderbox_tree'] = 'SeaMonkey'
BRANCHES['comm-central-trunk']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey'
BRANCHES['comm-central-trunk']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['comm-central-trunk']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['comm-central-trunk']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['comm-central-trunk']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['slaves'] = SLAVES['macosx']
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['slaves'] = SLAVES['win32']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-trunk']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-trunk']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/Users/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
BRANCHES['comm-central-trunk']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    # Source server support, bug 506702
    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
}
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['macosx-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['win32-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## comm-1.9.1
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-1.9.1']['repo_path'] = 'releases/comm-1.9.1'
BRANCHES['comm-1.9.1']['mozilla_repo_path'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-1.9.1']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['comm-1.9.1']['major_version'] = '1.9.1'
BRANCHES['comm-1.9.1']['product_name'] = 'seamonkey'
BRANCHES['comm-1.9.1']['app_name'] = 'suite'
BRANCHES['comm-1.9.1']['brand_name'] = 'SeaMonkey'
BRANCHES['comm-1.9.1']['start_hour'] = [0]
BRANCHES['comm-1.9.1']['start_minute'] = [0]
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-1.9.1']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx': {},
    'linux-debug': {},
}
# The mozconfig file to use, relative to CONFIG_REPO_URL/CONFIG_SUBDIR
BRANCHES['comm-1.9.1']['platforms']['linux']['mozconfig_dep'] = 'linux/comm-1.9.1/dep'
BRANCHES['comm-1.9.1']['platforms']['linux64']['mozconfig_dep'] = 'linux64/comm-1.9.1/dep'
BRANCHES['comm-1.9.1']['platforms']['macosx']['mozconfig_dep'] = 'macosx/comm-1.9.1/dep'
BRANCHES['comm-1.9.1']['platforms']['win32']['mozconfig_dep'] = 'win32/comm-1.9.1/dep'
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['mozconfig_dep'] = 'linux/comm-1.9.1/debug'
# nightly mozconfig (not for debug builds)
BRANCHES['comm-1.9.1']['platforms']['linux']['mozconfig'] = 'linux/comm-1.9.1/nightly'
BRANCHES['comm-1.9.1']['platforms']['linux64']['mozconfig'] = 'linux64/comm-1.9.1/nightly'
BRANCHES['comm-1.9.1']['platforms']['macosx']['mozconfig'] = 'macosx/comm-1.9.1/nightly'
BRANCHES['comm-1.9.1']['platforms']['win32']['mozconfig'] = 'win32/comm-1.9.1/nightly'
BRANCHES['comm-1.9.1']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1'
BRANCHES['comm-1.9.1']['platforms']['linux64']['base_name'] = 'Linux x86-64 comm-1.9.1'
BRANCHES['comm-1.9.1']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-1.9.1'
BRANCHES['comm-1.9.1']['platforms']['macosx']['base_name'] = 'OS X 10.5 comm-1.9.1'
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['base_name'] = 'Linux comm-1.9.1 leak test'
BRANCHES['comm-1.9.1']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-1.9.1']['platforms']['linux64']['profiled_build'] = False
BRANCHES['comm-1.9.1']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-1.9.1']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['comm-1.9.1']['platforms']['linux']['build_space'] = 6
BRANCHES['comm-1.9.1']['platforms']['linux64']['build_space'] = 6
BRANCHES['comm-1.9.1']['platforms']['win32']['build_space'] = 7
BRANCHES['comm-1.9.1']['platforms']['macosx']['build_space'] = 5
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['build_space'] = 4
BRANCHES['comm-1.9.1']['platforms']['linux']['builds_before_reboot'] = None
BRANCHES['comm-1.9.1']['platforms']['linux64']['builds_before_reboot'] = None
BRANCHES['comm-1.9.1']['platforms']['win32']['builds_before_reboot'] = None
BRANCHES['comm-1.9.1']['platforms']['macosx']['builds_before_reboot'] = None
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['builds_before_reboot'] = None
# Enable Nightly builds
BRANCHES['comm-1.9.1']['enable_nightly'] = True
# Enable unit tests
BRANCHES['comm-1.9.1']['platforms']['linux']['enable_unittests'] = True
BRANCHES['comm-1.9.1']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['comm-1.9.1']['platforms']['win32']['enable_unittests'] = True
BRANCHES['comm-1.9.1']['unittest_exec_xpcshell_suites'] = True
BRANCHES['comm-1.9.1']['enable_mac_a11y'] = False
BRANCHES['comm-1.9.1']['platforms']['linux']['crashtest_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['comm-1.9.1']['platforms']['macosx']['crashtest_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['linux']['mochitest_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['comm-1.9.1']['platforms']['macosx']['mochitest_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['linux']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['win32']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['macosx']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['linux']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['win32']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-1.9.1']['platforms']['macosx']['mochibrowser_leak_threshold'] = 0
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
    BRANCH_LEVEL_VARS['download_base_url'] + '/nightly/latest-comm-1.9.1'
BRANCHES['comm-1.9.1']['allLocalesFile'] = 'suite/locales/all-locales'
# nightly shark build for profiling
BRANCHES['comm-1.9.1']['enable_shark'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-1.9.1']['create_snippet'] = True
BRANCHES['comm-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/build/0/SeaMonkey/comm-1.9.1'
BRANCHES['comm-1.9.1']['idle_timeout'] = 60*60*6   # 6 hours
# We're actually using gcc4, but the platform hardcodes gcc3
BRANCHES['comm-1.9.1']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-1.9.1']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['comm-1.9.1']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-1.9.1']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-1.9.1']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-1.9.1']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-1.9.1']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-1.9.1']['tinderbox_tree'] = 'SeaMonkey2.0'
BRANCHES['comm-1.9.1']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey2.0'
BRANCHES['comm-1.9.1']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['comm-1.9.1']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['comm-1.9.1']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['comm-1.9.1']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-1.9.1']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.1']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.1']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.1']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.1']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    # Source server support, bug 506702
    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
}
BRANCHES['comm-1.9.1']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/Users/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
BRANCHES['comm-1.9.1']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## comm-1.9.2
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-1.9.2']['repo_path'] = 'comm-central'
BRANCHES['comm-1.9.2']['mozilla_repo_path'] = 'releases/mozilla-1.9.2'
BRANCHES['comm-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
BRANCHES['comm-1.9.2']['major_version'] = '1.9.2'
BRANCHES['comm-1.9.2']['product_name'] = 'seamonkey'
BRANCHES['comm-1.9.2']['app_name'] = 'suite'
BRANCHES['comm-1.9.2']['brand_name'] = 'SeaMonkey'
BRANCHES['comm-1.9.2']['start_hour'] = [0]
BRANCHES['comm-1.9.2']['start_minute'] = [15]
# Force graphs off for now, this branch is still experimental
BRANCHES['comm-1.9.2']['graph_server'] = None
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-1.9.2']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx': {},
}
# The mozconfig file to use, relative to CONFIG_REPO_URL/CONFIG_SUBDIR
BRANCHES['comm-1.9.2']['platforms']['linux']['mozconfig_dep'] = 'linux/comm-1.9.2/dep'
BRANCHES['comm-1.9.2']['platforms']['linux64']['mozconfig_dep'] = 'linux64/comm-1.9.2/dep'
BRANCHES['comm-1.9.2']['platforms']['macosx']['mozconfig_dep'] = 'macosx/comm-1.9.2/dep'
BRANCHES['comm-1.9.2']['platforms']['win32']['mozconfig_dep'] = 'win32/comm-1.9.2/dep'
# nightly mozconfig (not for debug builds)
BRANCHES['comm-1.9.2']['platforms']['linux']['mozconfig'] = 'linux/comm-1.9.2/nightly'
BRANCHES['comm-1.9.2']['platforms']['linux64']['mozconfig'] = 'linux64/comm-1.9.2/nightly'
BRANCHES['comm-1.9.2']['platforms']['macosx']['mozconfig'] = 'macosx/comm-1.9.2/nightly'
BRANCHES['comm-1.9.2']['platforms']['win32']['mozconfig'] = 'win32/comm-1.9.2/nightly'
BRANCHES['comm-1.9.2']['platforms']['linux']['base_name'] = 'Linux comm-1.9.2'
BRANCHES['comm-1.9.2']['platforms']['linux64']['base_name'] = 'Linux x86-64 comm-1.9.2'
BRANCHES['comm-1.9.2']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-1.9.2'
BRANCHES['comm-1.9.2']['platforms']['macosx']['base_name'] = 'OS X 10.5 comm-1.9.2'
BRANCHES['comm-1.9.2']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-1.9.2']['platforms']['linux64']['profiled_build'] = False
BRANCHES['comm-1.9.2']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-1.9.2']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-1.9.2']['platforms']['linux']['build_space'] = 6
BRANCHES['comm-1.9.2']['platforms']['linux64']['build_space'] = 6
BRANCHES['comm-1.9.2']['platforms']['win32']['build_space'] = 7
BRANCHES['comm-1.9.2']['platforms']['macosx']['build_space'] = 5
BRANCHES['comm-1.9.2']['platforms']['linux']['builds_before_reboot'] = None
BRANCHES['comm-1.9.2']['platforms']['linux64']['builds_before_reboot'] = None
BRANCHES['comm-1.9.2']['platforms']['win32']['builds_before_reboot'] = None
BRANCHES['comm-1.9.2']['platforms']['macosx']['builds_before_reboot'] = None
# Enable Nightly builds
BRANCHES['comm-1.9.2']['enable_nightly'] = False
# Enable unit tests
BRANCHES['comm-1.9.2']['unittest_suites'] = []
BRANCHES['comm-1.9.2']['platforms']['linux']['enable_unittests'] = False
BRANCHES['comm-1.9.2']['platforms']['macosx']['enable_unittests'] = False
BRANCHES['comm-1.9.2']['platforms']['win32']['enable_unittests'] = False
BRANCHES['comm-1.9.2']['enable_mac_a11y'] = True
BRANCHES['comm-1.9.2']['platforms']['linux']['crashtest_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['comm-1.9.2']['platforms']['macosx']['crashtest_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['linux']['mochitest_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['comm-1.9.2']['platforms']['macosx']['mochitest_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['linux']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['win32']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['macosx']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['linux']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['win32']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['platforms']['macosx']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-1.9.2']['unittest_build_space'] = 6
# And code coverage
BRANCHES['comm-1.9.2']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-1.9.2']['enable_l10n'] = False
BRANCHES['comm-1.9.2']['l10nNightlyUpdate'] = False
BRANCHES['comm-1.9.2']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['comm-1.9.2']['l10nDatedDirs'] = False
BRANCHES['comm-1.9.2']['l10n_tree'] = 'sea20x'
#make sure it has an ending slash
BRANCHES['comm-1.9.2']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-1.9.2-l10n/'
BRANCHES['comm-1.9.2']['enUS_binaryURL'] = \
    BRANCH_LEVEL_VARS['download_base_url'] + '/nightly/latest-comm-1.9.2'
BRANCHES['comm-1.9.2']['allLocalesFile'] = 'suite/locales/all-locales'
# nightly shark build for profiling
BRANCHES['comm-1.9.2']['enable_shark'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-1.9.2']['create_snippet'] = True
BRANCHES['comm-1.9.2']['aus2_base_upload_dir'] = '/opt/aus2/build/0/SeaMonkey/comm-1.9.2'
BRANCHES['comm-1.9.2']['idle_timeout'] = 60*60*12   # 12 hours
# We're actually using gcc4, but the platform hardcodes gcc3
BRANCHES['comm-1.9.2']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-1.9.2']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['comm-1.9.2']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-1.9.2']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-1.9.2']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-1.9.2']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-1.9.2']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-1.9.2']['tinderbox_tree'] = 'SeaMonkey2.1'
BRANCHES['comm-1.9.2']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey2.1'
BRANCHES['comm-1.9.2']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['comm-1.9.2']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['comm-1.9.2']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['comm-1.9.2']['platforms']['macosx']['slaves'] = SLAVES['macosx']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-1.9.2']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.2']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.2']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.2']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-1.9.2']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.2']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.2']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    # Source server support, bug 506702
    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
}
BRANCHES['comm-1.9.2']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/Users/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
