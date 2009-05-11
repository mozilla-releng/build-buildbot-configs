# It's a little unfortunate to have both of these but some things (HgPoller)
# require an URL while other things (BuildSteps) require only the host.
# Since they're both right here it shouldn't be a problem to keep them in sync.
HGURL = 'http://hg.mozilla.org/'
HGHOST = 'hg.mozilla.org'
# for chatzilla/venkman
CVSROOT = ':ext:seabld@cvs.mozilla.org:/cvsroot'
CONFIG_REPO_PATH = 'build/buildbot-configs'
CONFIG_SUBDIR = 'seamonkey-unittest'
IRC_BOT_NAME = 'sea-unit-bot'
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
GRAPH_SERVER = 'graphs.mozilla.org'
GRAPH_SELECTOR = 'server'
BUILD_TOOLS_REPO_PATH = 'build/tools'
DEFAULT_BUILD_SPACE = 5
#BASE_CLOBBER_URL = 'http://build.mozilla.org/clobberer/index.php'
BASE_CLOBBER_URL = None # deactivates clobberer support for now
DEFAULT_CLOBBER_TIME = 24*7 # 1 week
# List of talos masters to notify of new builds, and if a failure to notify the
# talos master should result in a warning
TALOS_MASTERS = []


# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-central': {},
}

######## comm-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-central']['repo_path'] = 'comm-central'
BRANCHES['comm-central']['mozilla_repo_path'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-central']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['comm-central']['major_version'] = '1.9.1'
BRANCHES['comm-central']['product_name'] = 'seamonkey'
BRANCHES['comm-central']['app_name'] = 'suite'
BRANCHES['comm-central']['brand_name'] = 'SeaMonkey'
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
}
# The mozconfig file to use, relative to CONFIG_REPO_URL/CONFIG_SUBDIR
BRANCHES['comm-central']['platforms']['linux']['mozconfig'] = 'linux/comm-central/nightly'
BRANCHES['comm-central']['platforms']['macosx']['mozconfig'] = 'macosx/comm-central/nightly'
BRANCHES['comm-central']['platforms']['win32']['mozconfig'] = 'win32/comm-central/nightly'
BRANCHES['comm-central']['platforms']['linux']['base_name'] = 'Linux comm-central'
BRANCHES['comm-central']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-central'
BRANCHES['comm-central']['platforms']['macosx']['base_name'] = 'OS X 10.4 comm-central'
BRANCHES['comm-central']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['linux']['build_space'] = 5
BRANCHES['comm-central']['platforms']['win32']['build_space'] = 7
BRANCHES['comm-central']['platforms']['macosx']['build_space'] = 5
BRANCHES['comm-central']['platforms']['linux']['builds_before_reboot'] = None
BRANCHES['comm-central']['platforms']['win32']['builds_before_reboot'] = None
BRANCHES['comm-central']['platforms']['macosx']['builds_before_reboot'] = None
# Enable unit tests
BRANCHES['comm-central']['enable_unittests'] = True
BRANCHES['comm-central']['enable_mac_a11y'] = False
BRANCHES['comm-central']['unittest_build_space'] = 5
BRANCHES['comm-central']['platforms']['linux']['mochitest_leak_threshold'] = 0
BRANCHES['comm-central']['platforms']['win32']['mochitest_leak_threshold'] = 200
BRANCHES['comm-central']['platforms']['macosx']['mochitest_leak_threshold'] = 0
BRANCHES['comm-central']['platforms']['linux']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central']['platforms']['win32']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central']['platforms']['macosx']['mochichrome_leak_threshold'] = 0
BRANCHES['comm-central']['platforms']['linux']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-central']['platforms']['win32']['mochibrowser_leak_threshold'] = 0
BRANCHES['comm-central']['platforms']['macosx']['mochibrowser_leak_threshold'] = 0
# And code coverage
BRANCHES['comm-central']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-central']['enable_l10n'] = False
#make sure it has an ending slash
BRANCHES['comm-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-central-l10n/'
BRANCHES['comm-central']['enUS_binaryURL'] = \
    DOWNLOAD_BASE_URL + '/nightly/latest-comm-central'
BRANCHES['comm-central']['allLocalesFile'] = 'suite/locales/all-locales'
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central']['create_snippet'] = True
BRANCHES['comm-central']['aus2_base_upload_dir'] = '/opt/aus2/build/0/SeaMonkey/trunk'
BRANCHES['comm-central']['idle_timeout'] = 60*60*2   # 2 hours
BRANCHES['comm-central']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central']['tinderbox_tree'] = 'SeaMonkey'
BRANCHES['comm-central']['platforms']['linux']['slaves'] = [
#    'cb-sea-linux-tbox',
    'cn-sea-qm-centos5-01'
]
BRANCHES['comm-central']['platforms']['win32']['slaves'] = [
#    'cb-sea-win32-tbox',
    'cn-sea-qm-win2k3-01'
]
BRANCHES['comm-central']['platforms']['macosx']['slaves'] = [
#    'cb-xserve02',
    'cb-sea-miniosx01'
]
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'BUILD_PALMSYNC': '1',
    'PALM_CDK_DIR': 'C:\PALMCDK403',
}
BRANCHES['comm-central']['platforms']['macosx']['env'] = {
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
