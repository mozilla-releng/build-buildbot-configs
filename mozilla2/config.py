# It's a little unfortunate to have both of these but some things (HgPoller)
# require an URL while other things (BuildSteps) require only the host.
# Since they're both right here it shouldn't be a problem to keep them in sync.
HGURL = 'http://hg.mozilla.org/'
HGHOST = 'hg.mozilla.org'
# for nss/nspr
CVSROOT = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
CONFIG_REPO_PATH = 'build/buildbot-configs'
CONFIG_SUBDIR = 'mozilla2'
OBJDIR = 'obj-firefox'
OBJDIR_UNITTESTS = 'objdir'
STAGE_USERNAME = 'ffxbld'
STAGE_USERNAME_XULRUNNER = 'xrbld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_BASE_PATH = '/home/ftp/pub/firefox'
STAGE_BASE_PATH_XULRUNNER = '/home/ftp/pub/xulrunner'
STAGE_GROUP = None
STAGE_SSH_KEY = 'ffxbld_dsa'
STAGE_SSH_XULRUNNER_KEY = 'xrbld_dsa'
AUS2_USER = 'cltbld'
AUS2_HOST = 'aus2-staging.mozilla.org'
DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/firefox'
GRAPH_SERVER = 'graphs.mozilla.org'
GRAPH_SELECTOR = 'server'
BUILD_TOOLS_REPO_PATH = 'build/tools'
DEFAULT_BUILD_SPACE = 5
BASE_CLOBBER_URL = 'http://build.mozilla.org/clobberer/index.php'
DEFAULT_CLOBBER_TIME = 24*7 # 1 week
# List of talos masters to notify of new builds, and if a failure to notify the
# talos master should result in a warning
TALOS_MASTERS = [
    ('qm-rhel02.mozilla.org:9988', True),
    ('qm-buildbot01.mozilla.org:9987', False),
    ('qm-buildbot01.mozilla.org:9989', False),
    ]

SLAVES = {
    'linux': ['moz2-linux-slave%02i' % x for x in [
        1,2,5,6,7,8,9,
        10,11,12,13,14,15,16,18,19,
        20,21,22,23,24,25]],
    'linux64': ['moz2-linux64-slave%02i' % x for x in [1]],
    'win32': ['moz2-win32-slave%02i' % x for x in [
        1,2,5,6,7,8,9,
        10,11,12,13,14,15,16,17,18,19,
        20,22,23,24,25,26,27,28,29]],
    'macosx': ['moz2-darwin9-slave%02i' % x for x in [2,5,6,7]] + [
               'bm-xserve%02i' for x in [12,16,17,18,19,22]],
}

L10N_SLAVES = {
    'linux': SLAVES['linux'][:8],
    'win32': SLAVES['win32'][:8],
    'macosx': SLAVES['macosx'][:8],
}

# All branches that are to be built MUST be listed here.
BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.1': {},
    'tracemonkey': {}
}

######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['mozilla-central']['major_version'] = '1.9.2'
BRANCHES['mozilla-central']['product_name'] = 'firefox'
BRANCHES['mozilla-central']['app_name'] = 'browser'
BRANCHES['mozilla-central']['brand_name'] = 'Minefield'
# All platforms being built for this branch MUST be listed here.
BRANCHES['mozilla-central']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
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
BRANCHES['mozilla-central']['platforms']['linux-debug']['mozconfig'] = 'linux/mozilla-central/debug'
BRANCHES['mozilla-central']['platforms']['macosx-debug']['mozconfig'] = 'macosx/mozilla-central/debug'
BRANCHES['mozilla-central']['platforms']['win32-debug']['mozconfig'] = 'win32/mozilla-central/debug'
BRANCHES['mozilla-central']['platforms']['linux']['base_name'] = 'Linux mozilla-central'
BRANCHES['mozilla-central']['platforms']['linux64']['base_name'] = 'Linux x86-64 mozilla-central'
BRANCHES['mozilla-central']['platforms']['win32']['base_name'] = 'WINNT 5.2 mozilla-central'
BRANCHES['mozilla-central']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 mozilla-central'
BRANCHES['mozilla-central']['platforms']['linux-debug']['base_name'] = 'Linux mozilla-central leak test'
BRANCHES['mozilla-central']['platforms']['win32-debug']['base_name'] = 'WINNT 5.2 mozilla-central leak test'
BRANCHES['mozilla-central']['platforms']['macosx-debug']['base_name'] = 'OS X 10.5.2 mozilla-central leak test'
BRANCHES['mozilla-central']['platforms']['linux']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['linux64']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['win32']['profiled_build'] = True
BRANCHES['mozilla-central']['platforms']['macosx']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['linux-debug']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['win32-debug']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['macosx-debug']['profiled_build'] = False
BRANCHES['mozilla-central']['platforms']['linux']['build_space'] = 5
BRANCHES['mozilla-central']['platforms']['linux64']['build_space'] = 5
BRANCHES['mozilla-central']['platforms']['win32']['build_space'] = 7
BRANCHES['mozilla-central']['platforms']['macosx']['build_space'] = 5
BRANCHES['mozilla-central']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-central']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['mozilla-central']['platforms']['macosx-debug']['build_space'] = 3
BRANCHES['mozilla-central']['platforms']['linux']['builds_before_reboot'] = None
BRANCHES['mozilla-central']['platforms']['linux64']['builds_before_reboot'] = None
BRANCHES['mozilla-central']['platforms']['win32']['builds_before_reboot'] = None
BRANCHES['mozilla-central']['platforms']['macosx']['builds_before_reboot'] = None
BRANCHES['mozilla-central']['platforms']['linux-debug']['builds_before_reboot'] = None
BRANCHES['mozilla-central']['platforms']['win32-debug']['builds_before_reboot'] = None
BRANCHES['mozilla-central']['platforms']['macosx-debug']['builds_before_reboot'] = None
# Enable XULRunner / SDK builds
BRANCHES['mozilla-central']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-central']['enable_unittests'] = True
BRANCHES['mozilla-central']['unittest_build_space'] = 5
# And code coverage
BRANCHES['mozilla-central']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
#make sure it has an ending slash
BRANCHES['mozilla-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-central-l10n/'
BRANCHES['mozilla-central']['enUS_binaryURL'] = \
    DOWNLOAD_BASE_URL + '/nightly/latest-mozilla-central'
BRANCHES['mozilla-central']['allLocalesFile'] = 'browser/locales/all-locales'
# nightly shark build for profiling
BRANCHES['mozilla-central']['enable_shark'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-central']['create_snippet'] = True
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-central'
BRANCHES['mozilla-central']['idle_timeout'] = 60*60*2   # 2 hours
BRANCHES['mozilla-central']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
# We're actually using gcc4, but Firefox hardcodes gcc3
BRANCHES['mozilla-central']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['mozilla-central']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['mozilla-central']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['mozilla-central']['platforms']['linux']['upload_symbols'] = True
BRANCHES['mozilla-central']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['mozilla-central']['platforms']['win32']['upload_symbols'] = True
BRANCHES['mozilla-central']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['mozilla-central']['tinderbox_tree'] = 'Firefox'
BRANCHES['mozilla-central']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['mozilla-central']['platforms']['linux64']['slaves'] = SLAVES['linux64']
BRANCHES['mozilla-central']['platforms']['win32']['slaves'] = SLAVES['win32']
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
BRANCHES['mozilla-central']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['mozilla-central']['platforms']['linux-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['macosx-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['win32-debug']['platform_objdir'] = OBJDIR
BRANCHES['mozilla-central']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-central']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-central']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-central']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
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
BRANCHES['mozilla-1.9.1']['platforms']['linux']['builds_before_reboot'] = None
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['builds_before_reboot'] = None
BRANCHES['mozilla-1.9.1']['platforms']['win32']['builds_before_reboot'] = None
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['builds_before_reboot'] = None
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['builds_before_reboot'] = None
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['builds_before_reboot'] = None
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['builds_before_reboot'] = None
# Enable XULRunner / SDK builds
BRANCHES['mozilla-1.9.1']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-1.9.1']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['unittest_build_space'] = 5
BRANCHES['mozilla-1.9.1']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['mozilla-1.9.1']['enable_l10n'] = True
#make sure it has an ending slash
BRANCHES['mozilla-1.9.1']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.1-l10n/'
BRANCHES['mozilla-1.9.1']['enUS_binaryURL'] = \
    DOWNLOAD_BASE_URL + '/nightly/latest-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['allLocalesFile'] = 'browser/locales/all-locales'
# nightly shark build for profiling
BRANCHES['mozilla-1.9.1']['enable_shark'] = True
BRANCHES['mozilla-1.9.1']['create_snippet'] = True
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['idle_timeout'] = 60*60*2   # 2 hours
BRANCHES['mozilla-1.9.1']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['linux']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['tinderbox_tree'] = 'Firefox3.5'
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
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.1']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
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

######## tracemonkey
BRANCHES['tracemonkey']['repo_path'] = 'tracemonkey'
BRANCHES['tracemonkey']['major_version'] = '1.9.2'
BRANCHES['tracemonkey']['product_name'] = 'firefox'
BRANCHES['tracemonkey']['app_name'] = 'browser'
BRANCHES['tracemonkey']['brand_name'] = 'Minefield'
BRANCHES['tracemonkey']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}
BRANCHES['tracemonkey']['platforms']['linux']['mozconfig'] = 'linux/tracemonkey/nightly'
BRANCHES['tracemonkey']['platforms']['macosx']['mozconfig'] = 'macosx/tracemonkey/nightly'
BRANCHES['tracemonkey']['platforms']['win32']['mozconfig'] = 'win32/tracemonkey/nightly'
BRANCHES['tracemonkey']['platforms']['linux']['base_name'] = 'Linux tracemonkey'
BRANCHES['tracemonkey']['platforms']['win32']['base_name'] = 'WINNT 5.2 tracemonkey'
BRANCHES['tracemonkey']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 tracemonkey'
BRANCHES['tracemonkey']['platforms']['linux']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['win32']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['macosx']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['linux']['build_space'] = 5
BRANCHES['tracemonkey']['platforms']['win32']['build_space'] = 5
BRANCHES['tracemonkey']['platforms']['macosx']['build_space'] = 5
BRANCHES['tracemonkey']['platforms']['linux']['builds_before_reboot'] = None
BRANCHES['tracemonkey']['platforms']['win32']['builds_before_reboot'] = None
BRANCHES['tracemonkey']['platforms']['macosx']['builds_before_reboot'] = None
BRANCHES['tracemonkey']['platforms']['linux']['upload_symbols'] = True
BRANCHES['tracemonkey']['platforms']['win32']['upload_symbols'] = True
BRANCHES['tracemonkey']['platforms']['macosx']['upload_symbols'] = True
# Disable XULRunner / SDK builds
BRANCHES['tracemonkey']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['tracemonkey']['enable_unittests'] = True
BRANCHES['tracemonkey']['unittest_build_space'] = 5
BRANCHES['tracemonkey']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['tracemonkey']['enable_l10n'] = False
# nightly shark build for profiling
BRANCHES['tracemonkey']['enable_shark'] = True
BRANCHES['tracemonkey']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['tracemonkey']['aus2_base_upload_dir'] = 'fake'
BRANCHES['tracemonkey']['idle_timeout'] = 60*60*10   # 10 hours
BRANCHES['tracemonkey']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['macosx']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['tinderbox_tree'] = 'TraceMonkey'
BRANCHES['tracemonkey']['platforms']['linux']['slaves'] = SLAVES['linux']
BRANCHES['tracemonkey']['platforms']['win32']['slaves'] = SLAVES['win32']
BRANCHES['tracemonkey']['platforms']['macosx']['slaves'] = SLAVES['macosx']
BRANCHES['tracemonkey']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['tracemonkey']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['tracemonkey']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['tracemonkey']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'tracemonkey',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['tracemonkey']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'tracemonkey',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['tracemonkey']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'ffxbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
    'MOZ_SYMBOLS_EXTRA_BUILDID': 'tracemonkey',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
