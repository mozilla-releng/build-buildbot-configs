HGURL = 'http://hg.mozilla.org/'
ADD_POLL_BRANCH = 'mozilla-central'
CONFIG_REPO_URL = 'http://hg.mozilla.org/build/buildbot-configs'
CONFIG_SUBDIR = 'thunderbird'
LOCALE_REPO_URL = 'http://hg.mozilla.org/l10n-central/index.cgi/%(locale)s'
OBJDIR = 'objdir-tb'
STAGE_USERNAME = 'tbirdbld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_BASE_PATH = '/home/ftp/pub/thunderbird'
STAGE_GROUP = 'thunderbird'
STAGE_SSH_KEY = 'tbirdbld_dsa'
AUS2_USER = 'tbirdbld'
AUS2_HOST = 'aus2-staging.mozilla.org'
DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/thunderbird'
PRODUCT = 'mail'
MOZ_APP_NAME = 'thunderbird'
BRAND_NAME = 'Shredder'

# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-central': {},
    'comm-central-bloat': {},
    'comm-central-calendar': {},
    'comm-central-sunbird': {},
}

######## thunderbird-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}

BRANCHES['comm-central']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-central']['cvsroot'] = ':ext:tbirdbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-central']['mozconfig'] = 'mozconfig'
BRANCHES['comm-central']['package'] = True
BRANCHES['comm-central']['upload_stage'] = True
BRANCHES['comm-central']['codesighs'] = True
BRANCHES['comm-central']['l10n'] = True
BRANCHES['comm-central']['irc_nick'] = 'thunderbuild'
BRANCHES['comm-central']['irc_channels'] = [ 'maildev' ]
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
BRANCHES['comm-central']['create_l10n_snippets'] = False
BRANCHES['comm-central']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Thunderbird/trunk'
BRANCHES['comm-central']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central']['tinderbox_tree'] = 'Thunderbird'
BRANCHES['comm-central']['platforms']['linux']['slaves'] = [
    'tb-linux-tbox',
]
BRANCHES['comm-central']['platforms']['win32']['slaves'] = [
    'tbnewref-win32-tbox'
]
BRANCHES['comm-central']['platforms']['macosx']['slaves'] = [
    'bm-xserve07'
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
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## lightning-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-calendar']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}

BRANCHES['comm-central-calendar']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-central-calendar']['cvsroot'] = ':ext:calbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-central-calendar']['mozconfig'] = 'mozconfig-calendar'
BRANCHES['comm-central-calendar']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-calendar']['period'] = 60 * 60 * 6
BRANCHES['comm-central-calendar']['package'] = True
BRANCHES['comm-central-calendar']['upload_stage'] = True
BRANCHES['comm-central-calendar']['upload_complete_mar'] = False
#Might be better off per-platform instead of per-branch here.
BRANCHES['comm-central-calendar']['upload_glob'] = "mozilla/dist/xpi-stage/{lightning,gdata-provider}.xpi"
BRANCHES['comm-central-calendar']['stage_username'] = 'calbld'
BRANCHES['comm-central-calendar']['stage_base_path'] = '/home/ftp/pub/calendar/lightning'
BRANCHES['comm-central-calendar']['stage_group'] = 'calendar'
BRANCHES['comm-central-calendar']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-central-calendar']['codesighs'] = False
BRANCHES['comm-central-calendar']['l10n'] = False
BRANCHES['comm-central-calendar']['irc_nick'] = 'calbuild'
BRANCHES['comm-central-calendar']['irc_channels'] = [ 'maildev', 'calendar' ]
BRANCHES['comm-central-calendar']['platforms']['linux']['base_name'] = 'Linux comm-central-calendar ltn'
BRANCHES['comm-central-calendar']['platforms']['win32']['base_name'] = 'Win2k3 comm-central-calendar ltn'
BRANCHES['comm-central-calendar']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-central-calendar ltn'
BRANCHES['comm-central-calendar']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-calendar']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-calendar']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central-calendar']['platforms']['linux']['milestone'] = "comm-central/linux-xpi"
BRANCHES['comm-central-calendar']['platforms']['win32']['milestone'] = "comm-central/win32-xpi"
BRANCHES['comm-central-calendar']['platforms']['macosx']['milestone'] = "comm-central/macosx-xpi"
BRANCHES['comm-central-calendar']['platforms']['macosx']['upload_glob'] = "mozilla/dist/universal/xpi-stage/{lightning,gdata-provider}.xpi"

# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-calendar']['create_snippet'] = False
BRANCHES['comm-central-calendar']['create_l10n_snippets'] = False
BRANCHES['comm-central-calendar']['aus2_base_upload_dir'] = False
BRANCHES['comm-central-calendar']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-calendar']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-calendar']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-calendar']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-calendar']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-calendar']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-calendar']['tinderbox_tree'] = 'Sunbird'
BRANCHES['comm-central-calendar']['platforms']['linux']['slaves'] = [
    'cb-sb-linux-tbox',
]
BRANCHES['comm-central-calendar']['platforms']['win32']['slaves'] = [
    'cb-sb-win32-tbox',
]
BRANCHES['comm-central-calendar']['platforms']['macosx']['slaves'] = [
    'cb-xserve03',
]
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-calendar']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-calendar']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-calendar']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-calendar']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-calendar']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-calendar']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## sunbird-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-sunbird']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}

BRANCHES['comm-central-sunbird']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-central-sunbird']['cvsroot'] = ':ext:calbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-central-sunbird']['mozconfig'] = 'mozconfig-sunbird'
BRANCHES['comm-central-sunbird']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-sunbird']['period'] = 60 * 60 * 6
BRANCHES['comm-central-sunbird']['package'] = True
BRANCHES['comm-central-sunbird']['upload_stage'] = True
BRANCHES['comm-central-sunbird']['stage_username'] = 'calbld'
BRANCHES['comm-central-sunbird']['stage_base_path'] = '/home/ftp/pub/calendar/sunbird'
BRANCHES['comm-central-sunbird']['stage_group'] = 'calendar'
BRANCHES['comm-central-sunbird']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-central-sunbird']['codesighs'] = False
BRANCHES['comm-central-sunbird']['l10n'] = True
BRANCHES['comm-central-sunbird']['l10n_mozconfig'] = 'mozconfig-sunbird-l10n'
BRANCHES['comm-central-sunbird']['product'] = 'calendar'
BRANCHES['comm-central-sunbird']['appname'] = 'sunbird'
BRANCHES['comm-central-sunbird']['brand_name'] = 'Sunbird'
BRANCHES['comm-central-sunbird']['irc_nick'] = 'sunbuild'
BRANCHES['comm-central-sunbird']['irc_channels'] = [ 'maildev','calendar' ]
BRANCHES['comm-central-sunbird']['platforms']['linux']['base_name'] = 'Linux comm-central sunbird'
BRANCHES['comm-central-sunbird']['platforms']['win32']['base_name'] = 'Win2k3 comm-central sunbird'
BRANCHES['comm-central-sunbird']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-central sunbird'
BRANCHES['comm-central-sunbird']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-sunbird']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-sunbird']['platforms']['macosx']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-sunbird']['create_snippet'] = True
BRANCHES['comm-central-sunbird']['aus2_host'] = 'aus2-community.mozilla.org'
BRANCHES['comm-central-sunbird']['aus2_user'] = 'calbld'
BRANCHES['comm-central-sunbird']['create_l10n_snippets'] = False
BRANCHES['comm-central-sunbird']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Sunbird/trunk'
BRANCHES['comm-central-sunbird']['download_base_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/calendar/sunbird'
BRANCHES['comm-central-sunbird']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-sunbird']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-sunbird']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-sunbird']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-sunbird']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-sunbird']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-sunbird']['tinderbox_tree'] = 'Sunbird'
BRANCHES['comm-central-sunbird']['platforms']['linux']['slaves'] = [
    'cb-sb-linux-tbox',
]
BRANCHES['comm-central-sunbird']['platforms']['win32']['slaves'] = [
    'cb-sb-win32-tbox',
]
BRANCHES['comm-central-sunbird']['platforms']['macosx']['slaves'] = [
    'cb-xserve03',
]

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-sunbird']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-sunbird']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-sunbird']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-sunbird']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-sunbird']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-sunbird']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}


######## thunderbird-bloat
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-bloat']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}

BRANCHES['comm-central-bloat']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-central-bloat']['cvsroot'] = ':pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot'
BRANCHES['comm-central-bloat']['mozconfig'] = 'mozconfig-bloat'
BRANCHES['comm-central-bloat']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-bloat']['period'] = 60 * 60 * 2
BRANCHES['comm-central-bloat']['nightly'] = False
BRANCHES['comm-central-bloat']['leak'] = True
BRANCHES['comm-central-bloat']['package'] = False
BRANCHES['comm-central-bloat']['upload_stage'] = False
BRANCHES['comm-central-bloat']['codesighs'] = False
BRANCHES['comm-central-bloat']['l10n'] = False
BRANCHES['comm-central-bloat']['irc_nick'] = 'thunderbloat'
BRANCHES['comm-central-bloat']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central-bloat']['platforms']['linux']['base_name'] = 'Linux comm-central bloat'
BRANCHES['comm-central-bloat']['platforms']['win32']['base_name'] = 'Win2k3 comm-central bloat'
BRANCHES['comm-central-bloat']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-central bloat'
BRANCHES['comm-central-bloat']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-bloat']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-bloat']['platforms']['macosx']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-bloat']['create_snippet'] = False
BRANCHES['comm-central-bloat']['create_l10n_snippets'] = False
BRANCHES['comm-central-bloat']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Thunderbird/trunk'
BRANCHES['comm-central-bloat']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-bloat']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-bloat']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-bloat']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['tinderbox_tree'] = 'Thunderbird'
BRANCHES['comm-central-bloat']['platforms']['linux']['leak_threshold'] = 970000
BRANCHES['comm-central-bloat']['platforms']['macosx']['leak_threshold'] = 1400000
BRANCHES['comm-central-bloat']['platforms']['win32']['leak_threshold'] =  110000
BRANCHES['comm-central-bloat']['platforms']['linux']['slaves'] = [
    'momo-vm-07'
]
BRANCHES['comm-central-bloat']['platforms']['win32']['slaves'] = [
    'momo-vm-06'
]
BRANCHES['comm-central-bloat']['platforms']['macosx']['slaves'] = [
    'momo-vm-09'
]
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-bloat']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['macosx']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
}
BRANCHES['comm-central-bloat']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-bloat']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}


