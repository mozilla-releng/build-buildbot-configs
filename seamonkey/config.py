# It's a little unfortunate to have both of these but some things (HgPoller)
# require an URL while other things (BuildSteps) require only the host.
# Since they're both right here it shouldn't be a problem to keep them in sync.
HGURL = 'http://hg.mozilla.org/'
HGHOST = 'hg.mozilla.org'
# for chatzilla/venkman
CVSROOT = ':ext:seabld@cvs.mozilla.org:/cvsroot'
CONFIG_REPO_PATH = 'build/buildbot-configs'
CONFIG_SUBDIR = 'seamonkey'
IRC_BOT_NAME = 'sea2-build-bot'
IRC_BOT_CHANNELS = ['mozbot']
OBJDIR = 'objdir'
OBJDIR_UNITTESTS = 'objdir'
STAGE_USERNAME = 'seabld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_BASE_PATH = '/home/ftp/pub/seamonkey'
STAGE_GROUP = 'seamonkey'
STAGE_SSH_KEY = 'seabld_dsa'
AUS2_USER = 'seabld'
AUS2_HOST = 'aus2-community.mozilla.org'
DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/seamonkey'
#GRAPH_SERVER = 'graphs.mozilla.org'
GRAPH_SERVER = None
GRAPH_SELECTOR = '/server/collect.cgi'
BUILD_TOOLS_REPO_PATH = 'build/tools'
COMPARE_LOCALES_REPO_PATH = 'build/compare-locales'
COMPARE_LOCALES_TAG = 'RELEASE_AUTOMATION'
DEFAULT_BUILD_SPACE = 6
#BASE_CLOBBER_URL = 'http://build.mozilla.org/clobberer/index.php'
BASE_CLOBBER_URL = None # deactivates clobberer support for now
DEFAULT_CLOBBER_TIME = 24*7 # 1 week
# List of talos masters to notify of new builds, and if a failure to notify the
# talos master should result in a warning
TALOS_MASTERS = []

SLAVES = {
    'linux': ['cb-seamonkey-linux-%02i' % x for x in [1,2]] +
             ['cb-seamonkey-linuxdebug-%02i' % x for x in [1]] +
             ['cn-sea-qm-centos5-%02i' % x for x in [1]] +
             ['cb-sea-linux-tbox'],
    'linux64': ['cb-seamonkey-linux64-%02i' % x for x in [1]],
    'win32': ['cb-seamonkey-win32-%02i' % x for x in [1,2]] +
             ['cn-sea-qm-win2k3-%02i' % x for x in [1]] +
             ['cb-sea-win32-tbox'],
    'macosx': ['cb-seamonkey-osx-%02i' % x for x in [1,2,3,4]],
}

L10N_SLAVES = {
    'linux': SLAVES['linux'],
    'win32': SLAVES['win32'],
    'macosx': SLAVES['macosx'],
}

# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-1.9.1': {},
    'comm-central-trunk': {},
}

######## comm-1.9.1
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-1.9.1']['repo_path'] = 'releases/comm-1.9.1'
BRANCHES['comm-1.9.1']['mozilla_repo_path'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-1.9.1']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['comm-1.9.1']['extension_revision'] = 'SEAMONKEY_2_0_RELEASE'
BRANCHES['comm-1.9.1']['major_version'] = '1.9.1'
BRANCHES['comm-1.9.1']['product_name'] = 'seamonkey'
BRANCHES['comm-1.9.1']['app_name'] = 'suite'
BRANCHES['comm-1.9.1']['brand_name'] = 'SeaMonkey'
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
# Enable unit tests
BRANCHES['comm-1.9.1']['enable_unittests'] = True
BRANCHES['comm-1.9.1']['enable_mac_a11y'] = False
BRANCHES['comm-1.9.1']['unittest_build_space'] = 6
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
# And code coverage
BRANCHES['comm-1.9.1']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-1.9.1']['enable_l10n'] = True
BRANCHES['comm-1.9.1']['l10n_tree'] = 'sea20x'
#make sure it has an ending slash
BRANCHES['comm-1.9.1']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-1.9.1-l10n/'
BRANCHES['comm-1.9.1']['enUS_binaryURL'] = \
    DOWNLOAD_BASE_URL + '/nightly/latest-comm-1.9.1'
BRANCHES['comm-1.9.1']['allLocalesFile'] = 'suite/locales/all-locales'
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-1.9.1']['create_snippet'] = True
BRANCHES['comm-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/build/0/SeaMonkey/comm-1.9.1'
BRANCHES['comm-1.9.1']['idle_timeout'] = 60*60*4   # 4 hours
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
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
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

######## comm-central-trunk
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-central-trunk']['repo_path'] = 'comm-central'
BRANCHES['comm-central-trunk']['mozilla_repo_path'] = 'mozilla-central'
BRANCHES['comm-central-trunk']['l10n_repo_path'] = 'l10n-central'
BRANCHES['comm-central-trunk']['extension_revision'] = None
BRANCHES['comm-central-trunk']['major_version'] = '1.9.3'
BRANCHES['comm-central-trunk']['product_name'] = 'seamonkey'
BRANCHES['comm-central-trunk']['app_name'] = 'suite'
BRANCHES['comm-central-trunk']['brand_name'] = 'SeaMonkey'
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-trunk']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx': {},
    'linux-debug': {},
}
# The mozconfig file to use, relative to CONFIG_REPO_URL/CONFIG_SUBDIR
BRANCHES['comm-central-trunk']['platforms']['linux']['mozconfig_dep'] = 'linux/comm-central-trunk/dep'
BRANCHES['comm-central-trunk']['platforms']['linux64']['mozconfig_dep'] = 'linux64/comm-central-trunk/dep'
BRANCHES['comm-central-trunk']['platforms']['macosx']['mozconfig_dep'] = 'macosx/comm-central-trunk/dep'
BRANCHES['comm-central-trunk']['platforms']['win32']['mozconfig_dep'] = 'win32/comm-central-trunk/dep'
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['mozconfig_dep'] = 'linux/comm-central-trunk/debug'
# nightly mozconfig (not for debug builds)
BRANCHES['comm-central-trunk']['platforms']['linux']['mozconfig'] = 'linux/comm-central-trunk/nightly'
BRANCHES['comm-central-trunk']['platforms']['linux64']['mozconfig'] = 'linux64/comm-central-trunk/nightly'
BRANCHES['comm-central-trunk']['platforms']['macosx']['mozconfig'] = 'macosx/comm-central-trunk/nightly'
BRANCHES['comm-central-trunk']['platforms']['win32']['mozconfig'] = 'win32/comm-central-trunk/nightly'
BRANCHES['comm-central-trunk']['platforms']['linux']['base_name'] = 'Linux comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['linux64']['base_name'] = 'Linux x86-64 comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['macosx']['base_name'] = 'OS X 10.5 comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['base_name'] = 'Linux comm-central-trunk leak test'
BRANCHES['comm-central-trunk']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['linux64']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['linux']['build_space'] = 5
BRANCHES['comm-central-trunk']['platforms']['linux64']['build_space'] = 5
BRANCHES['comm-central-trunk']['platforms']['win32']['build_space'] = 7
BRANCHES['comm-central-trunk']['platforms']['macosx']['build_space'] = 5
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['comm-central-trunk']['platforms']['linux']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['linux64']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['win32']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['macosx']['builds_before_reboot'] = None
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['builds_before_reboot'] = None
# Enable unit tests
BRANCHES['comm-central-trunk']['enable_unittests'] = False
BRANCHES['comm-central-trunk']['enable_mac_a11y'] = True
BRANCHES['comm-central-trunk']['unittest_build_space'] = 5
BRANCHES['comm-central-trunk']['platforms']['linux']['crashtest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['win32']['crashtest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['macosx']['crashtest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['linux']['mochitest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['win32']['mochitest_leak_threshold'] = 200
BRANCHES['comm-central-trunk']['platforms']['macosx']['mochitest_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['linux']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['win32']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['macosx']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['linux']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['win32']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-central-trunk']['platforms']['macosx']['mochibrowser_leak_threshold'] = 0
# And code coverage
BRANCHES['comm-central-trunk']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-central-trunk']['enable_l10n'] = True
BRANCHES['comm-central-trunk']['l10n_tree'] = 'sea21x'
#make sure it has an ending slash
BRANCHES['comm-central-trunk']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-central-trunk-l10n/'
BRANCHES['comm-central-trunk']['enUS_binaryURL'] = \
    DOWNLOAD_BASE_URL + '/nightly/latest-comm-central-trunk'
BRANCHES['comm-central-trunk']['allLocalesFile'] = 'suite/locales/all-locales'
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-trunk']['create_snippet'] = True
BRANCHES['comm-central-trunk']['aus2_base_upload_dir'] = '/opt/aus2/build/0/SeaMonkey/comm-central-trunk'
BRANCHES['comm-central-trunk']['idle_timeout'] = 60*60*4   # 4 hours
# We're actually using gcc4, but the platform hardcodes gcc3
BRANCHES['comm-central-trunk']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-trunk']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['comm-central-trunk']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-trunk']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-trunk']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['tinderbox_tree'] = 'SeaMonkey'
BRANCHES['comm-central-trunk']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['comm-central-trunk']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['comm-central-trunk']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['comm-central-trunk']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['slaves'] = SLAVES['linux']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-trunk']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'CHOWN_ROOT': '~/bin/chown_root',
    'CHOWN_REVERT': '~/bin/chown_revert',
}
BRANCHES['comm-central-trunk']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':2',
    'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
