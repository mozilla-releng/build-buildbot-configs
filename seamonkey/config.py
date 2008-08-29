HGURL = 'http://hg.mozilla.org/'
# for chatzilla/venkman
CVSROOT = ':ext:seabld@cvs.mozilla.org:/cvsroot'
ADD_POLL_BRANCH = 'mozilla-central'
CONFIG_REPO_URL = 'http://hg.mozilla.org/build/buildbot-configs'
CONFIG_SUBDIR = 'seamonkey'
LOCALE_REPO_URL = 'http://hg.mozilla.org/l10n-central/index.cgi/%(locale)s'
OBJDIR = 'objdir'
STAGE_USERNAME = 'seabld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_BASE_PATH = '/home/ftp/pub/seamonkey'
STAGE_GROUP = 'seamonkey'
STAGE_SSH_KEY = 'seabld_dsa'
AUS2_USER = 'seabld'
AUS2_HOST = 'aus2-community.mozilla.org'
DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/seamonkey'
PRODUCT = 'suite'
MOZ_APP_NAME = 'seamonkey'


# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-central': {}
}

######## seamonkey-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}
BRANCHES['comm-central']['platforms']['linux']['base_name'] = 'Linux comm-central'
BRANCHES['comm-central']['platforms']['win32']['base_name'] = 'Win2k3 comm-central'
BRANCHES['comm-central']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-central'
BRANCHES['comm-central']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['macosx']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central']['create_snippet'] = True
BRANCHES['comm-central']['aus2_base_upload_dir'] = '/opt/aus2/build/0/SeaMonkey/trunk'
BRANCHES['comm-central']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central']['tinderbox_tree'] = 'MozillaTest'
BRANCHES['comm-central']['platforms']['linux']['slaves'] = [
    'cb-sea-linux-tbox'
]
BRANCHES['comm-central']['platforms']['win32']['slaves'] = [
    'cb-sea-win32-tbox'
]
BRANCHES['comm-central']['platforms']['macosx']['slaves'] = [
    'cb-xserve02'
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
}
BRANCHES['comm-central']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'seabld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sea/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/seabld/.ssh/seabld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
