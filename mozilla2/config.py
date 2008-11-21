HGURL = 'http://hg.mozilla.org/'
# for nss/nspr
CVSROOT = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
CONFIG_REPO_URL = 'http://hg.mozilla.org/build/buildbot-configs'
CONFIG_SUBDIR = 'mozilla2'
OBJDIR = 'obj-firefox'
STAGE_USERNAME = 'ffxbld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_BASE_PATH = '/home/ftp/pub/firefox'
STAGE_GROUP = None
STAGE_SSH_KEY = 'ffxbld_dsa'
AUS2_USER = 'cltbld'
AUS2_HOST = 'aus2-staging.mozilla.org'
DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/firefox'
GRAPH_SERVER = 'graphs.mozilla.org'
GRAPH_SELECTOR = 'server'


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
BRANCHES['mozilla-central']['major_version'] = '1.9.2'
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
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-central']['create_snippet'] = True
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-central'
BRANCHES['mozilla-central']['periodic_scheduler_period'] = 60*60*2   # 2 hours
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
BRANCHES['mozilla-central']['platforms']['linux']['slaves'] = [
    'moz2-linux-slave1',
    'moz2-linux-slave02',
    'moz2-linux-slave03',
    'moz2-linux-slave05',
    'moz2-linux-slave06',
    'moz2-linux-slave11',
    'moz2-linux-slave12',
    'moz2-linux-slave13',
    'moz2-linux-slave14',
    'moz2-linux-slave15',
    'moz2-linux-slave16',
]
BRANCHES['mozilla-central']['platforms']['linux64']['slaves'] = [
    'moz2-linux64-slave01'
]
BRANCHES['mozilla-central']['platforms']['win32']['slaves'] = [
    'moz2-win32-slave1',
    'moz2-win32-slave02',
    'moz2-win32-slave03',
    'moz2-win32-slave05',
    'moz2-win32-slave06',
    'moz2-win32-slave11',
    'moz2-win32-slave12',
    'moz2-win32-slave13',
    'moz2-win32-slave15',
    'moz2-win32-slave16',
    'moz2-win32-slave17',
    'moz2-win32-slave18'
]
BRANCHES['mozilla-central']['platforms']['macosx']['slaves'] = [
    'bm-xserve16',
    'bm-xserve17',
    'bm-xserve18',
    'bm-xserve19',
    'moz2-darwin9-slave02'
]
BRANCHES['mozilla-central']['platforms']['linux-debug']['slaves'] = [
    'moz2-linux-slave02',
    'moz2-linux-slave05',
    'moz2-linux-slave06',
    'moz2-linux-slave11',
    'moz2-linux-slave12',
    'moz2-linux-slave14',
    'moz2-linux-slave15',
    'moz2-linux-slave16',
]
BRANCHES['mozilla-central']['platforms']['win32-debug']['slaves'] = [
    'moz2-win32-slave1',
    'moz2-win32-slave02',
    'moz2-win32-slave05',
    'moz2-win32-slave06',
    'moz2-win32-slave11',
    'moz2-win32-slave12',
    'moz2-win32-slave13',
    'moz2-win32-slave15',
    'moz2-win32-slave16',
    'moz2-win32-slave17',
    'moz2-win32-slave18'
]
BRANCHES['mozilla-central']['platforms']['macosx-debug']['slaves'] = [
    'bm-xserve16',
    'bm-xserve17',
    'bm-xserve18',
    'bm-xserve19',
    'moz2-darwin9-slave02',
]
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
}
BRANCHES['mozilla-central']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':0',
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
BRANCHES['mozilla-1.9.1']['major_version'] = '1.9.1'
BRANCHES['mozilla-1.9.1']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx': {},
    'linux-debug': {},
    'macosx-debug': {},
    'win32-debug': {}
}
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
BRANCHES['mozilla-1.9.1']['create_snippet'] = True
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['periodic_scheduler_period'] = 60*60*2   # 2 hours
BRANCHES['mozilla-1.9.1']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['mozilla-1.9.1']['platforms']['linux']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['mozilla-1.9.1']['tinderbox_tree'] = 'Firefox3.1'
BRANCHES['mozilla-1.9.1']['platforms']['linux']['slaves'] = [
    'moz2-linux-slave1',
    'moz2-linux-slave02',
    'moz2-linux-slave03',
    'moz2-linux-slave05',
    'moz2-linux-slave06',
    'moz2-linux-slave11',
    'moz2-linux-slave12',
    'moz2-linux-slave13',
    'moz2-linux-slave14',
    'moz2-linux-slave15',
    'moz2-linux-slave16',
]
BRANCHES['mozilla-1.9.1']['platforms']['linux64']['slaves'] = [
    'moz2-linux64-slave01'
]
BRANCHES['mozilla-1.9.1']['platforms']['win32']['slaves'] = [
    'moz2-win32-slave1',
    'moz2-win32-slave02',
    'moz2-win32-slave03',
    'moz2-win32-slave05',
    'moz2-win32-slave06',
    'moz2-win32-slave11',
    'moz2-win32-slave12',
    'moz2-win32-slave13',
    'moz2-win32-slave15',
    'moz2-win32-slave16',
    'moz2-win32-slave17',
    'moz2-win32-slave18'
]
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['slaves'] = [
    'bm-xserve16',
    'bm-xserve17',
    'bm-xserve18',
    'bm-xserve19',
    'moz2-darwin9-slave02'
]
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['slaves'] = [
    'moz2-linux-slave02',
    'moz2-linux-slave05',
    'moz2-linux-slave06',
    'moz2-linux-slave11',
    'moz2-linux-slave12',
    'moz2-linux-slave14',
    'moz2-linux-slave15',
    'moz2-linux-slave16',
]
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['slaves'] = [
    'moz2-win32-slave1',
    'moz2-win32-slave02',
    'moz2-win32-slave05',
    'moz2-win32-slave06',
    'moz2-win32-slave11',
    'moz2-win32-slave12',
    'moz2-win32-slave13',
    'moz2-win32-slave15',
    'moz2-win32-slave16',
    'moz2-win32-slave17',
    'moz2-win32-slave18'
]
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['slaves'] = [
    'bm-xserve16',
    'bm-xserve17',
    'bm-xserve18',
    'bm-xserve19',
    'moz2-darwin9-slave02',
]
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
}
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'DISPLAY': ':0',
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
BRANCHES['tracemonkey']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}
BRANCHES['tracemonkey']['platforms']['linux']['base_name'] = 'Linux tracemonkey'
BRANCHES['tracemonkey']['platforms']['win32']['base_name'] = 'WINNT 5.2 tracemonkey'
BRANCHES['tracemonkey']['platforms']['macosx']['base_name'] = 'OS X 10.5.2 tracemonkey'
BRANCHES['tracemonkey']['platforms']['linux']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['win32']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['macosx']['profiled_build'] = False
BRANCHES['tracemonkey']['platforms']['linux']['upload_symbols'] = True
BRANCHES['tracemonkey']['platforms']['win32']['upload_symbols'] = True
BRANCHES['tracemonkey']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['tracemonkey']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['tracemonkey']['aus2_base_upload_dir'] = 'fake'
BRANCHES['tracemonkey']['periodic_scheduler_period'] = 60*60*10   # 10 hours
BRANCHES['tracemonkey']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['platforms']['macosx']['update_platform'] = 'fake'
BRANCHES['tracemonkey']['tinderbox_tree'] = 'TraceMonkey'
BRANCHES['tracemonkey']['platforms']['linux']['slaves'] = [
    'moz2-linux-slave02',
    'moz2-linux-slave05',
    'moz2-linux-slave06',
    'moz2-linux-slave11',
    'moz2-linux-slave12',
    'moz2-linux-slave14',
    'moz2-linux-slave15',
    'moz2-linux-slave16',
]
BRANCHES['tracemonkey']['platforms']['win32']['slaves'] = [
    'moz2-win32-slave1',
    'moz2-win32-slave02',
    'moz2-win32-slave05',
    'moz2-win32-slave06',
    'moz2-win32-slave11',
    'moz2-win32-slave12',
    'moz2-win32-slave13',
    'moz2-win32-slave15',
    'moz2-win32-slave16',
    'moz2-win32-slave17',
    'moz2-win32-slave18'
]
BRANCHES['tracemonkey']['platforms']['macosx']['slaves'] = [
    'bm-xserve16',
    'bm-xserve17',
    'bm-xserve18',
    'bm-xserve19',
    'moz2-darwin9-slave02',
]
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
