from copy import deepcopy

import buildbotcustom.env
reload(buildbotcustom.env)
from buildbotcustom.env import MozillaEnvironments

MAC_MINIS = ['moz2-darwin9-slave%02i' % x for x in [2,5,6,7] + range(9,27)]
XSERVES   = ['bm-xserve%02i' % x for x in [7,11,12,16,17,18,19,21,22]]
SLAVES = {
    'linux': ['moz2-linux-slave%02i' % x for x in [1,2] +
              range(5,17) + range(18,51)],
    'linux64': ['moz2-linux64-slave%02i' % x for x in [1,2]],
    'win32': ['moz2-win32-slave%02i' % x for x in [1,2] +
              range(5,21) + range(22,60)],
    'macosx': MAC_MINIS + XSERVES,
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
        ('talos-master.mozilla.org:9010', False),
        ('talos-staging-master.mozilla.org:9010', False),
    ],
    # List of unittest masters to notify of new builds to test,
    # and if a failure to notify the master should result in a warning
    'unittest_masters': [('localhost:9010', True)],
    'unittest_suites': [
        ('mochitests', ['mochitest-plain']),
        ('everythingelse', ['reftest', 'crashtest', 'mochitest-chrome',
                            'mochitest-browser-chrome', 'mochitest-a11y',
                            'xpcshell'])
    ],
    'xulrunner_tinderbox_tree': 'XULRunner',
    'weekly_tinderbox_tree': 'Testing',
    'l10n_tinderbox_tree': 'Mozilla-l10n',
}

# shorthand, because these are used often
OBJDIR = BRANCH_LEVEL_VARS['objdir']
SYMBOL_SERVER_PATH = BRANCH_LEVEL_VARS['symbol_server_path']

# All branches that are to be built MUST be listed here.
BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.1': {},
    'mozilla-1.9.2': {},
    'tracemonkey': {},
    'places': {},
    'electrolysis': {},
}

# We copy the global vars in first, so branches can override them if they want to
for branch in BRANCHES.keys():
    for attr in BRANCH_LEVEL_VARS.keys():
        BRANCHES[branch][attr] = deepcopy(BRANCH_LEVEL_VARS[attr])

######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['mozilla-central']['major_version'] = '1.9.2'
BRANCHES['mozilla-central']['product_name'] = 'firefox'
BRANCHES['mozilla-central']['app_name'] = 'browser'
BRANCHES['mozilla-central']['brand_name'] = 'Minefield'
BRANCHES['mozilla-central']['start_hour'] = [3] 
BRANCHES['mozilla-central']['start_minute'] = [2] 
# All platforms being built for this branch MUST be listed here.
BRANCHES['mozilla-central']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'wince': {},
    'macosx': {},
    'linux-debug': {},
    'macosx-debug': {},
    'win32-debug': {}
}
# The mozconfig file to use, relative to CONFIG_REPO_URL/CONFIG_SUBDIR
BRANCHES['mozilla-central']['platforms']['linux']['mozconfig'] = 'linux/mozilla-central/nightly'
BRANCHES['mozilla-central']['platforms']['linux64']['mozconfig'] = 'linux64/mozilla-central/nightly'
BRANCHES['mozilla-central']['platforms']['macosx']['mozconfig'] = 'macosx/mozilla-central/nightly'
BRANCHES['mozilla-central']['platforms']['win32']['mozconfig'] = 'win32/mozilla-central/nightly'
BRANCHES['mozilla-central']['platforms']['wince']['mozconfig'] = 'wince/mozilla-central/nightly'
BRANCHES['mozilla-central']['platforms']['linux-debug']['mozconfig'] = 'linux/mozilla-central/debug'
BRANCHES['mozilla-central']['platforms']['macosx-debug']['mozconfig'] = 'macosx/mozilla-central/debug'
BRANCHES['mozilla-central']['platforms']['win32-debug']['mozconfig'] = 'win32/mozilla-central/debug'
BRANCHES['mozilla-central']['platforms']['linux']['base_name'] = 'Linux mozilla-central'
BRANCHES['mozilla-central']['platforms']['linux64']['base_name'] = 'Linux x86-64 mozilla-central'
BRANCHES['mozilla-central']['platforms']['win32']['base_name'] = 'WINNT 5.2 mozilla-central'
BRANCHES['mozilla-central']['platforms']['wince']['base_name'] = 'WINCE 5.0 mozilla-central'
BRANCHES['mozilla-central']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 mozilla-central'
BRANCHES['mozilla-central']['platforms']['linux-debug']['base_name'] = 'Linux mozilla-central leak test'
BRANCHES['mozilla-central']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 mozilla-central leak test'
BRANCHES['mozilla-central']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 mozilla-central leak test'
BRANCHES['mozilla-central']['platforms']['linux']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['linux64']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['win32']['profiled_build'] = True
BRANCHES['mozilla-central']['platforms']['wince']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['macosx']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['win32-debug']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['macosx-debug']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['linux']['build_space'] = 6
BRANCHES['mozilla-central']['platforms']['linux64']['build_space'] = 6
BRANCHES['mozilla-central']['platforms']['win32']['build_space'] = 8
BRANCHES['mozilla-central']['platforms']['wince']['build_space'] = 4
BRANCHES['mozilla-central']['platforms']['macosx']['build_space'] = 6
BRANCHES['mozilla-central']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-central']['platforms']['win32-debug']['build_space'] = 5
BRANCHES['mozilla-central']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['mozilla-central']['platforms']['linux']['builds_before_reboot'] = 1
BRANCHES['mozilla-central']['platforms']['linux64']['builds_before_reboot'] = 1
BRANCHES['mozilla-central']['platforms']['win32']['builds_before_reboot'] = 1
BRANCHES['mozilla-central']['platforms']['wince']['builds_before_reboot'] = 1
BRANCHES['mozilla-central']['platforms']['macosx']['builds_before_reboot'] = 1
BRANCHES['mozilla-central']['platforms']['linux-debug']['builds_before_reboot'] = 1
BRANCHES['mozilla-central']['platforms']['win32-debug']['builds_before_reboot'] = 1
BRANCHES['mozilla-central']['platforms']['macosx-debug']['builds_before_reboot'] = 1
# Enable XULRunner / SDK builds
BRANCHES['mozilla-central']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-central']['enable_unittests'] = True
BRANCHES['mozilla-central']['unittest_suites'] = [
    # Turn on chunks for mochitests
    ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
    ('everythingelse', ['reftest', 'crashtest', 'mochitest-chrome',
                        'mochitest-browser-chrome', 'mochitest-a11y',
                        'xpcshell'])
]
BRANCHES['mozilla-central']['enable_packaged_debug_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['enable_packaged_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux64']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-central']['platforms']['macosx']['enable_packaged_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['win32']['enable_packaged_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['wince']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-central']['platforms']['wince']['packageTests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['macosx']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['win32']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['linux-debug']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['macosx-debug']['enable_checktests'] = True
BRANCHES['mozilla-central']['platforms']['win32-debug']['enable_checktests'] = True
BRANCHES['mozilla-central']['enable_mac_a11y'] = True
BRANCHES['mozilla-central']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['mozilla-central']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['mozilla-central']['unittest_build_space'] = 6
# And code coverage
BRANCHES['mozilla-central']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
BRANCHES['mozilla-central']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-central']['l10nDatedDirs'] = True
BRANCHES['mozilla-central']['l10n_tree'] = 'fx37x'
#make sure it has an ending slash
BRANCHES['mozilla-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-central-l10n/'
BRANCHES['mozilla-central']['enUS_binaryURL'] = \
    BRANCH_LEVEL_VARS['download_base_url'] + '/nightly/latest-mozilla-central'
BRANCHES['mozilla-central']['allLocalesFile'] = 'browser/locales/all-locales'
# nightly shark build for profiling
BRANCHES['mozilla-central']['enable_shark'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-central']['create_snippet'] = True
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-central'
BRANCHES['mozilla-central']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
# We're actually using gcc4, but Firefox hardcodes gcc3
BRANCHES['mozilla-central']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['mozilla-central']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['mozilla-central']['platforms']['wince']['update_platform'] = 'WINCE_arm-msvc'
BRANCHES['mozilla-central']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['mozilla-central']['platforms']['linux']['upload_symbols'] = True
BRANCHES['mozilla-central']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['mozilla-central']['platforms']['win32']['upload_symbols'] = True
BRANCHES['mozilla-central']['platforms']['wince']['upload_symbols'] = False
BRANCHES['mozilla-central']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['mozilla-central']['tinderbox_tree'] = 'Firefox'
BRANCHES['mozilla-central']['packaged_unittest_tinderbox_tree'] = 'Firefox-Unittest'
BRANCHES['mozilla-central']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['mozilla-central']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['mozilla-central']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-central']['platforms']['wince']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-central']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['mozilla-central']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
BRANCHES['mozilla-central']['platforms']['win32-debug']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-central']['platforms']['macosx-debug']['slaves'] = SLAVES['macosx']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['mozilla-central']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['wince']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['mozilla-central']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['macosx-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['win32-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-central']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-central']['platforms']['win32']['env'] = {
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
}
BRANCHES['mozilla-central']['platforms']['wince']['env'] = MozillaEnvironments['winmo-arm'].copy()
BRANCHES['mozilla-central']['platforms']['wince']['env'].update(
    BRANCHES['mozilla-central']['platforms']['win32']['env'])
BRANCHES['mozilla-central']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
BRANCHES['mozilla-central']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-central']['platforms']['macosx-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-central']['platforms']['win32-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['repo_path'] = 'releases/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['major_version'] = '1.9.1'
BRANCHES['mozilla-1.9.1']['product_name'] = 'firefox'
BRANCHES['mozilla-1.9.1']['app_name'] = 'browser'
BRANCHES['mozilla-1.9.1']['brand_name'] = 'Shiretoko'
BRANCHES['mozilla-1.9.1']['start_hour'] = [3] 
BRANCHES['mozilla-1.9.1']['start_minute'] = [2] 
BRANCHES['mozilla-1.9.1']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx': {},
    'linux-debug': {},
    'macosx-debug': {},
    'win32-debug': {}
}
BRANCHES['mozilla-1.9.1']['platforms']['linux']['mozconfig'] = 'linux/mozilla-1.9.1/nightly'
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['mozconfig'] = 'linux64/mozilla-1.9.1/nightly'
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['mozconfig'] = 'macosx/mozilla-1.9.1/nightly'
BRANCHES['mozilla-1.9.1']['platforms']['win32']['mozconfig'] = 'win32/mozilla-1.9.1/nightly'
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['mozconfig'] = 'linux/mozilla-1.9.1/debug'
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['mozconfig'] = 'macosx/mozilla-1.9.1/debug'
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['mozconfig'] = 'win32/mozilla-1.9.1/debug'
BRANCHES['mozilla-1.9.1']['platforms']['linux']['base_name'] = 'Linux mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['base_name'] = 'Linux x86-64 mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['platforms']['win32']['base_name'] = 'WINNT 5.2 mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['base_name'] = 'Linux mozilla-1.9.1 leak test'
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 mozilla-1.9.1 leak test'
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 mozilla-1.9.1 leak test'
BRANCHES['mozilla-1.9.1']['platforms']['linux']['profiled_build'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['profiled_build'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['profiled_build'] = True
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['profiled_build'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['profiled_build'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['profiled_build'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux']['build_space'] = 5
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['build_space'] = 5
BRANCHES['mozilla-1.9.1']['platforms']['win32']['build_space'] = 7
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['build_space'] = 5
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.1']['platforms']['linux']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.1']['platforms']['win32']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['builds_before_reboot'] = 1
# Enable XULRunner / SDK builds
BRANCHES['mozilla-1.9.1']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-1.9.1']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['enable_packaged_debug_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['mozilla-1.9.1']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['mozilla-1.9.1']['unittest_build_space'] = 5
BRANCHES['mozilla-1.9.1']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['mozilla-1.9.1']['enable_l10n'] = True
BRANCHES['mozilla-1.9.1']['l10nNightlyUpdate'] = False 
BRANCHES['mozilla-1.9.1']['l10nDatedDirs'] = False 
BRANCHES['mozilla-1.9.1']['l10n_tree'] = 'fx35x'
#make sure it has an ending slash
BRANCHES['mozilla-1.9.1']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.1-l10n/'
BRANCHES['mozilla-1.9.1']['enUS_binaryURL'] = \
    BRANCH_LEVEL_VARS['download_base_url'] + '/nightly/latest-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['allLocalesFile'] = 'browser/locales/all-locales'
# nightly shark build for profiling
BRANCHES['mozilla-1.9.1']['enable_shark'] = True
BRANCHES['mozilla-1.9.1']['create_snippet'] = True
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['linux']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['tinderbox_tree'] = 'Firefox3.5'
BRANCHES['mozilla-1.9.1']['packaged_unittest_tinderbox_tree'] = 'Firefox3.5-Unittest'
BRANCHES['mozilla-1.9.1']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['mozilla-1.9.1']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['slaves'] = SLAVES['macosx']
BRANCHES['mozilla-1.9.1']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.1']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.1']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.1']['platforms']['win32']['env'] = {
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
}
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['repo_path'] = 'releases/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['major_version'] = '1.9.2'
BRANCHES['mozilla-1.9.2']['product_name'] = 'firefox'
BRANCHES['mozilla-1.9.2']['app_name'] = 'browser'
BRANCHES['mozilla-1.9.2']['brand_name'] = 'Namoroka'
BRANCHES['mozilla-1.9.2']['start_hour'] = [3] 
BRANCHES['mozilla-1.9.2']['start_minute'] = [32] 
BRANCHES['mozilla-1.9.2']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'wince': {},
    'macosx': {},
    'linux-debug': {},
    'macosx-debug': {},
    'win32-debug': {}
}
BRANCHES['mozilla-1.9.2']['platforms']['linux']['mozconfig'] = 'linux/mozilla-1.9.2/nightly'
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['mozconfig'] = 'linux64/mozilla-1.9.2/nightly'
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['mozconfig'] = 'macosx/mozilla-1.9.2/nightly'
BRANCHES['mozilla-1.9.2']['platforms']['win32']['mozconfig'] = 'win32/mozilla-1.9.2/nightly'
BRANCHES['mozilla-1.9.2']['platforms']['wince']['mozconfig'] = 'wince/mozilla-1.9.2/nightly'
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['mozconfig'] = 'linux/mozilla-1.9.2/debug'
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['mozconfig'] = 'macosx/mozilla-1.9.2/debug'
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['mozconfig'] = 'win32/mozilla-1.9.2/debug'
BRANCHES['mozilla-1.9.2']['platforms']['linux']['base_name'] = 'Linux mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['base_name'] = 'Linux x86-64 mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['win32']['base_name'] = 'WINNT 5.2 mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['wince']['base_name'] = 'WINCE 5.0 mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['base_name'] = 'Linux mozilla-1.9.2 leak test'
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 mozilla-1.9.2 leak test'
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 mozilla-1.9.2 leak test'
BRANCHES['mozilla-1.9.2']['platforms']['linux']['profiled_build'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['profiled_build'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32']['profiled_build'] = True
BRANCHES['mozilla-1.9.2']['platforms']['wince']['profiled_build'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['profiled_build'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['profiled_build'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['profiled_build'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux']['build_space'] = 5
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['build_space'] = 5
BRANCHES['mozilla-1.9.2']['platforms']['win32']['build_space'] = 7
BRANCHES['mozilla-1.9.2']['platforms']['wince']['build_space'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['build_space'] = 5
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['linux']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.2']['platforms']['win32']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.2']['platforms']['wince']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['builds_before_reboot'] = 1
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['builds_before_reboot'] = 1
# Enable XULRunner / SDK builds
BRANCHES['mozilla-1.9.2']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-1.9.2']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['enable_packaged_debug_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['wince']['enable_packaged_opt_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['wince']['packageTests'] = True
BRANCHES['mozilla-1.9.2']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['mozilla-1.9.2']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['mozilla-1.9.2']['unittest_build_space'] = 5
BRANCHES['mozilla-1.9.2']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['mozilla-1.9.2']['enable_l10n'] = True
BRANCHES['mozilla-1.9.2']['l10nNightlyUpdate'] = True 
BRANCHES['mozilla-1.9.2']['l10nDatedDirs'] = True 
BRANCHES['mozilla-1.9.2']['l10n_tree'] = 'fx36x'
#make sure it has an ending slash
BRANCHES['mozilla-1.9.2']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.2-l10n/'
BRANCHES['mozilla-1.9.2']['enUS_binaryURL'] = \
    BRANCH_LEVEL_VARS['download_base_url'] + '/nightly/latest-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['allLocalesFile'] = 'browser/locales/all-locales'
# nightly shark build for profiling
BRANCHES['mozilla-1.9.2']['enable_shark'] = True
BRANCHES['mozilla-1.9.2']['create_snippet'] = True
BRANCHES['mozilla-1.9.2']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['mozilla-1.9.2']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['mozilla-1.9.2']['platforms']['wince']['update_platform'] = 'WINCE_arm-msvc'
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['mozilla-1.9.2']['platforms']['linux']['upload_symbols'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32']['upload_symbols'] = True
BRANCHES['mozilla-1.9.2']['platforms']['wince']['upload_symbols'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['mozilla-1.9.2']['tinderbox_tree'] = 'Firefox3.6'
BRANCHES['mozilla-1.9.2']['packaged_unittest_tinderbox_tree'] = 'Firefox3.6-Unittest'
BRANCHES['mozilla-1.9.2']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['mozilla-1.9.2']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-1.9.2']['platforms']['wince']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['slaves'] = SLAVES['win32']
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['slaves'] = SLAVES['macosx']
BRANCHES['mozilla-1.9.2']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.2']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.2']['platforms']['wince']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-1.9.2']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.2']['platforms']['win32']['env'] = {
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
}
BRANCHES['mozilla-1.9.2']['platforms']['wince']['env'] = MozillaEnvironments['winmo-arm'].copy()
BRANCHES['mozilla-1.9.2']['platforms']['wince']['env'].update(
    BRANCHES['mozilla-1.9.2']['platforms']['win32']['env'])
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## tracemonkey
BRANCHES['tracemonkey']['repo_path'] = 'tracemonkey'
BRANCHES['tracemonkey']['major_version'] = '1.9.2'
BRANCHES['tracemonkey']['product_name'] = 'firefox'
BRANCHES['tracemonkey']['app_name'] = 'browser'
BRANCHES['tracemonkey']['brand_name'] = 'Minefield'
BRANCHES['tracemonkey']['start_hour'] = [3] 
BRANCHES['tracemonkey']['start_minute'] = [32] 
BRANCHES['tracemonkey']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx': {},
    'linux-debug': {},
    'macosx-debug': {},
    'win32-debug': {},
}
BRANCHES['tracemonkey']['platforms']['linux']['mozconfig'] = 'linux/tracemonkey/nightly'
BRANCHES['tracemonkey']['platforms']['linux64']['mozconfig'] = 'linux64/tracemonkey/nightly'
BRANCHES['tracemonkey']['platforms']['macosx']['mozconfig'] = 'macosx/tracemonkey/nightly'
BRANCHES['tracemonkey']['platforms']['win32']['mozconfig'] = 'win32/tracemonkey/nightly'
BRANCHES['tracemonkey']['platforms']['linux-debug']['mozconfig'] = 'linux/tracemonkey/debug'
BRANCHES['tracemonkey']['platforms']['macosx-debug']['mozconfig'] = 'macosx/tracemonkey/debug'
BRANCHES['tracemonkey']['platforms']['win32-debug']['mozconfig'] = 'win32/tracemonkey/debug'
BRANCHES['tracemonkey']['platforms']['linux']['base_name'] = 'Linux tracemonkey'
BRANCHES['tracemonkey']['platforms']['linux64']['base_name'] = 'Linux x86-64 tracemonkey'
BRANCHES['tracemonkey']['platforms']['win32']['base_name'] = 'WINNT 5.2 tracemonkey'
BRANCHES['tracemonkey']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 tracemonkey'
BRANCHES['tracemonkey']['platforms']['linux-debug']['base_name'] = 'Linux tracemonkey leak test'
BRANCHES['tracemonkey']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 tracemonkey leak test'
BRANCHES['tracemonkey']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 tracemonkey leak test'
BRANCHES['tracemonkey']['platforms']['linux']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['linux64']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['win32']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['macosx']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['win32-debug']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['macosx-debug']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['linux']['build_space'] = 5
BRANCHES['tracemonkey']['platforms']['linux64']['build_space'] = 5
BRANCHES['tracemonkey']['platforms']['win32']['build_space'] = 5
BRANCHES['tracemonkey']['platforms']['macosx']['build_space'] = 5
BRANCHES['tracemonkey']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['tracemonkey']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['tracemonkey']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['tracemonkey']['platforms']['linux']['builds_before_reboot'] = 1
BRANCHES['tracemonkey']['platforms']['linux64']['builds_before_reboot'] = 1
BRANCHES['tracemonkey']['platforms']['win32']['builds_before_reboot'] = 1
BRANCHES['tracemonkey']['platforms']['macosx']['builds_before_reboot'] = 1
BRANCHES['tracemonkey']['platforms']['linux-debug']['builds_before_reboot'] = 1
BRANCHES['tracemonkey']['platforms']['win32-debug']['builds_before_reboot'] = 1
BRANCHES['tracemonkey']['platforms']['macosx-debug']['builds_before_reboot'] = 1
BRANCHES['tracemonkey']['platforms']['linux']['upload_symbols'] = True
BRANCHES['tracemonkey']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['tracemonkey']['platforms']['win32']['upload_symbols'] = True
BRANCHES['tracemonkey']['platforms']['macosx']['upload_symbols'] = True
# Disable XULRunner / SDK builds
BRANCHES['tracemonkey']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['tracemonkey']['enable_unittests'] = True
BRANCHES['tracemonkey']['enable_packaged_debug_unittests'] = False
BRANCHES['tracemonkey']['platforms']['linux']['enable_packaged_opt_unittests'] = False
BRANCHES['tracemonkey']['platforms']['macosx']['enable_packaged_opt_unittests'] = False
BRANCHES['tracemonkey']['platforms']['win32']['enable_packaged_opt_unittests'] = False
BRANCHES['tracemonkey']['platforms']['linux']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['macosx']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['win32']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux-debug']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['macosx-debug']['enable_checktests'] = True
BRANCHES['tracemonkey']['platforms']['win32-debug']['enable_checktests'] = True
BRANCHES['tracemonkey']['enable_mac_a11y'] = True
BRANCHES['tracemonkey']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['tracemonkey']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['tracemonkey']['unittest_build_space'] = 5
BRANCHES['tracemonkey']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['tracemonkey']['enable_l10n'] = False
BRANCHES['tracemonkey']['l10nNightlyUpdate'] = False 
BRANCHES['tracemonkey']['l10nDatedDirs'] = False 
# nightly shark build for profiling
BRANCHES['tracemonkey']['enable_shark'] = True
BRANCHES['tracemonkey']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['tracemonkey']['aus2_base_upload_dir'] = 'fake'
BRANCHES['tracemonkey']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['linux64']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['macosx']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['tinderbox_tree'] = 'TraceMonkey'
BRANCHES['tracemonkey']['packaged_unittest_tinderbox_tree'] = 'TraceMonkey-Unittest'
BRANCHES['tracemonkey']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['tracemonkey']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['tracemonkey']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['tracemonkey']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['tracemonkey']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
BRANCHES['tracemonkey']['platforms']['win32-debug']['slaves'] = SLAVES['win32']
BRANCHES['tracemonkey']['platforms']['macosx-debug']['slaves'] = SLAVES['macosx']
BRANCHES['tracemonkey']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['tracemonkey']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['tracemonkey']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['tracemonkey']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['tracemonkey']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['tracemonkey']['platforms']['linux-debug']['enable_valgrind_checktests'] = True
BRANCHES['tracemonkey']['platforms']['macosx-debug']['platform_objdir'] = OBJDIR
BRANCHES['tracemonkey']['platforms']['win32-debug']['platform_objdir'] = OBJDIR
BRANCHES['tracemonkey']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'tracemonkey',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['tracemonkey']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64-tracemonkey',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['tracemonkey']['platforms']['win32']['env'] = {
    'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'tracemonkey',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    # Source server support, bug 506702
    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
}
BRANCHES['tracemonkey']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'tracemonkey',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['tracemonkey']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['tracemonkey']['platforms']['macosx-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['tracemonkey']['platforms']['win32-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## places
BRANCHES['places']['repo_path'] = 'projects/places'
BRANCHES['places']['major_version'] = '1.9.2'
BRANCHES['places']['product_name'] = 'firefox'
BRANCHES['places']['app_name'] = 'browser'
BRANCHES['places']['brand_name'] = 'Minefield'
BRANCHES['places']['start_hour'] = [4] 
BRANCHES['places']['start_minute'] = [2] 
BRANCHES['places']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
    'linux-debug': {},
    'macosx-debug': {},
    'win32-debug': {},
}
BRANCHES['places']['platforms']['linux']['mozconfig'] = 'linux/places/nightly'
BRANCHES['places']['platforms']['macosx']['mozconfig'] = 'macosx/places/nightly'
BRANCHES['places']['platforms']['win32']['mozconfig'] = 'win32/places/nightly'
BRANCHES['places']['platforms']['linux-debug']['mozconfig'] = 'linux/places/debug'
BRANCHES['places']['platforms']['macosx-debug']['mozconfig'] = 'macosx/places/debug'
BRANCHES['places']['platforms']['win32-debug']['mozconfig'] = 'win32/places/debug'
BRANCHES['places']['platforms']['linux']['base_name'] = 'Linux places'
BRANCHES['places']['platforms']['win32']['base_name'] = 'WINNT 5.2 places'
BRANCHES['places']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 places'
BRANCHES['places']['platforms']['linux-debug']['base_name'] = 'Linux places leak test'
BRANCHES['places']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 places leak test'
BRANCHES['places']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 places leak test'
BRANCHES['places']['platforms']['linux']['profiled_build'] = False
BRANCHES['places']['platforms']['win32']['profiled_build'] = False
BRANCHES['places']['platforms']['macosx']['profiled_build'] = False
BRANCHES['places']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['places']['platforms']['win32-debug']['profiled_build'] = False
BRANCHES['places']['platforms']['macosx-debug']['profiled_build'] = False
BRANCHES['places']['platforms']['linux']['build_space'] = 5
BRANCHES['places']['platforms']['win32']['build_space'] = 5
BRANCHES['places']['platforms']['macosx']['build_space'] = 5
BRANCHES['places']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['places']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['places']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['places']['platforms']['linux']['builds_before_reboot'] = 1
BRANCHES['places']['platforms']['win32']['builds_before_reboot'] = 1
BRANCHES['places']['platforms']['macosx']['builds_before_reboot'] = 1
BRANCHES['places']['platforms']['linux-debug']['builds_before_reboot'] = 1
BRANCHES['places']['platforms']['win32-debug']['builds_before_reboot'] = 1
BRANCHES['places']['platforms']['macosx-debug']['builds_before_reboot'] = 1
BRANCHES['places']['platforms']['linux']['upload_symbols'] = True
BRANCHES['places']['platforms']['win32']['upload_symbols'] = True
BRANCHES['places']['platforms']['macosx']['upload_symbols'] = True
# Disable XULRunner / SDK builds
BRANCHES['places']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['places']['enable_unittests'] = True
BRANCHES['places']['enable_packaged_debug_unittests'] = False
BRANCHES['places']['platforms']['linux']['enable_packaged_opt_unittests'] = False
BRANCHES['places']['platforms']['macosx']['enable_packaged_opt_unittests'] = False
BRANCHES['places']['platforms']['win32']['enable_packaged_opt_unittests'] = False
BRANCHES['places']['platforms']['linux']['enable_checktests'] = True
BRANCHES['places']['platforms']['macosx']['enable_checktests'] = True
BRANCHES['places']['platforms']['win32']['enable_checktests'] = True
BRANCHES['places']['platforms']['linux-debug']['enable_checktests'] = True
BRANCHES['places']['platforms']['macosx-debug']['enable_checktests'] = True
BRANCHES['places']['platforms']['win32-debug']['enable_checktests'] = True
BRANCHES['places']['enable_mac_a11y'] = True
BRANCHES['places']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['places']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['places']['unittest_build_space'] = 5
BRANCHES['places']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['places']['enable_l10n'] = False
# nightly shark build for profiling
BRANCHES['places']['enable_shark'] = True
BRANCHES['places']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['places']['aus2_base_upload_dir'] = 'fake'
BRANCHES['places']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['macosx']['update_platform'] = 'fake'
BRANCHES['places']['tinderbox_tree'] = 'Places'
BRANCHES['places']['packaged_unittest_tinderbox_tree'] = 'Places-Unittest'
BRANCHES['places']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['places']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['places']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['places']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
BRANCHES['places']['platforms']['win32-debug']['slaves'] = SLAVES['win32']
BRANCHES['places']['platforms']['macosx-debug']['slaves'] = SLAVES['macosx']
BRANCHES['places']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['places']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['places']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['places']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['places']['platforms']['macosx-debug']['platform_objdir'] = OBJDIR
BRANCHES['places']['platforms']['win32-debug']['platform_objdir'] = OBJDIR
BRANCHES['places']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'places',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['places']['platforms']['win32']['env'] = {
    'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'places',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    # Source server support, bug 506702
    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
}
BRANCHES['places']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'places',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['places']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['places']['platforms']['macosx-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['places']['platforms']['win32-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## electrolysis
BRANCHES['electrolysis']['repo_path'] = 'projects/electrolysis'
BRANCHES['electrolysis']['major_version'] = '1.9.2'
BRANCHES['electrolysis']['product_name'] = 'firefox'
BRANCHES['electrolysis']['app_name'] = 'browser'
BRANCHES['electrolysis']['brand_name'] = 'Minefield'
BRANCHES['electrolysis']['start_hour'] = [4] 
BRANCHES['electrolysis']['start_minute'] = [2] 
BRANCHES['electrolysis']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
    'linux-debug': {},
    'macosx-debug': {},
    'win32-debug': {},
}
BRANCHES['electrolysis']['platforms']['linux']['mozconfig'] = 'linux/electrolysis/nightly'
BRANCHES['electrolysis']['platforms']['macosx']['mozconfig'] = 'macosx/electrolysis/nightly'
BRANCHES['electrolysis']['platforms']['win32']['mozconfig'] = 'win32/electrolysis/nightly'
BRANCHES['electrolysis']['platforms']['linux-debug']['mozconfig'] = 'linux/electrolysis/debug'
BRANCHES['electrolysis']['platforms']['macosx-debug']['mozconfig'] = 'macosx/electrolysis/debug'
BRANCHES['electrolysis']['platforms']['win32-debug']['mozconfig'] = 'win32/electrolysis/debug'
BRANCHES['electrolysis']['platforms']['linux']['base_name'] = 'Linux electrolysis'
BRANCHES['electrolysis']['platforms']['win32']['base_name'] = 'WINNT 5.2 electrolysis'
BRANCHES['electrolysis']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 electrolysis'
BRANCHES['electrolysis']['platforms']['linux-debug']['base_name'] = 'Linux electrolysis leak test'
BRANCHES['electrolysis']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 electrolysis leak test'
BRANCHES['electrolysis']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 electrolysis leak test'
BRANCHES['electrolysis']['platforms']['linux']['profiled_build'] = False
BRANCHES['electrolysis']['platforms']['win32']['profiled_build'] = False
BRANCHES['electrolysis']['platforms']['macosx']['profiled_build'] = False
BRANCHES['electrolysis']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['electrolysis']['platforms']['win32-debug']['profiled_build'] = False
BRANCHES['electrolysis']['platforms']['macosx-debug']['profiled_build'] = False
BRANCHES['electrolysis']['platforms']['linux']['build_space'] = 6
BRANCHES['electrolysis']['platforms']['win32']['build_space'] = 6
BRANCHES['electrolysis']['platforms']['macosx']['build_space'] = 6
BRANCHES['electrolysis']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['electrolysis']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['electrolysis']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['electrolysis']['platforms']['linux']['builds_before_reboot'] = 1
BRANCHES['electrolysis']['platforms']['win32']['builds_before_reboot'] = 1
BRANCHES['electrolysis']['platforms']['macosx']['builds_before_reboot'] = 1
BRANCHES['electrolysis']['platforms']['linux-debug']['builds_before_reboot'] = 1
BRANCHES['electrolysis']['platforms']['win32-debug']['builds_before_reboot'] = 1
BRANCHES['electrolysis']['platforms']['macosx-debug']['builds_before_reboot'] = 1
BRANCHES['electrolysis']['platforms']['linux']['upload_symbols'] = True
BRANCHES['electrolysis']['platforms']['win32']['upload_symbols'] = True
BRANCHES['electrolysis']['platforms']['macosx']['upload_symbols'] = True
# Disable XULRunner / SDK builds
BRANCHES['electrolysis']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['electrolysis']['enable_unittests'] = True
BRANCHES['electrolysis']['enable_packaged_debug_unittests'] = False
BRANCHES['electrolysis']['platforms']['linux']['enable_packaged_opt_unittests'] = False
BRANCHES['electrolysis']['platforms']['win32']['enable_packaged_opt_unittests'] = False
BRANCHES['electrolysis']['platforms']['linux']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['macosx']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['win32']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['linux-debug']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['macosx-debug']['enable_checktests'] = True
BRANCHES['electrolysis']['platforms']['win32-debug']['enable_checktests'] = True
BRANCHES['electrolysis']['enable_mac_a11y'] = True
BRANCHES['electrolysis']['platforms']['win32']['mochitest_leak_threshold'] = 484
BRANCHES['electrolysis']['platforms']['win32']['crashtest_leak_threshold'] = 484
BRANCHES['electrolysis']['unittest_build_space'] = 5
BRANCHES['electrolysis']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['electrolysis']['enable_l10n'] = False
BRANCHES['electrolysis']['l10nNightlyUpdate'] = False 
BRANCHES['electrolysis']['l10nDatedDirs'] = False 
# nightly shark build for profiling
BRANCHES['electrolysis']['enable_shark'] = True
BRANCHES['electrolysis']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['electrolysis']['aus2_base_upload_dir'] = 'fake'
BRANCHES['electrolysis']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['electrolysis']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['electrolysis']['platforms']['macosx']['update_platform'] = 'fake'
BRANCHES['electrolysis']['tinderbox_tree'] = 'Electrolysis'
BRANCHES['electrolysis']['packaged_unittest_tinderbox_tree'] = 'Electrolysis'
BRANCHES['electrolysis']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['electrolysis']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['electrolysis']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['electrolysis']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
BRANCHES['electrolysis']['platforms']['win32-debug']['slaves'] = SLAVES['win32']
BRANCHES['electrolysis']['platforms']['macosx-debug']['slaves'] = SLAVES['macosx']
BRANCHES['electrolysis']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['electrolysis']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['electrolysis']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['electrolysis']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['electrolysis']['platforms']['macosx-debug']['platform_objdir'] = OBJDIR
BRANCHES['electrolysis']['platforms']['win32-debug']['platform_objdir'] = OBJDIR
BRANCHES['electrolysis']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'electrolysis',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['electrolysis']['platforms']['win32']['env'] = {
    'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'electrolysis',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    # Source server support, bug 506702
    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
}
BRANCHES['electrolysis']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'electrolysis',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['electrolysis']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib:%s/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['electrolysis']['platforms']['macosx-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['electrolysis']['platforms']['win32-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
