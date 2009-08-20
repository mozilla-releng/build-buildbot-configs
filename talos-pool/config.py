from buildbot.steps.shell import WithProperties

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org', '--resultsLink',
        '/server/collect.cgi']
TALOS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:tdhtml:tsvg:twinopen:tsspider:tgfx']

TALOS_NOCHROME_CONFIG_OPTIONS = GRAPH_CONFIG + TALOS_CONFIG_OPTIONS + ['--noChrome']

TALOS_JSS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tjss']

TALOS_DIRTY_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:ts_places_generated_min:ts_places_generated_med']
TALOS_DIRTY_ADDONS = ['/builds/buildbot/profiles/dirtyDBs.zip']

TALOS_TP4_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tp4']

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

SLAVES = {
    'linux': ["talos-rev2-linux%02i" % x for x in range(1,21)],
    'xp': ["talos-rev2-xp%02i" % x for x in range(1,21)],
    'vista': ["talos-rev2-vista%02i" % x for x in range(1,21)],
    'tiger': ["talos-rev2-tiger%02i" % x for x in range(1,21)],
    'leopard': ["talos-rev2-leopard%02i" % x for x in range(1,21)],
}

BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.2': {},
    'mozilla-1.9.1': {},
    'mozilla-1.9.0': {},
    'tracemonkey': {},
    'places': {},
}

PLATFORMS = {
    'macosx': {},
    'win32': {},
    'linux': {},
}

PLATFORMS['macosx']['slave_platforms'] = ['tiger', 'leopard']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['tiger'] = {'name': "MacOSX Darwin 8.8.1"}
PLATFORMS['macosx']['leopard'] = {'name': "MacOSX Darwin 9.0.0"}

PLATFORMS['win32']['slave_platforms'] = ['xp', 'vista']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "WINNT 5.1"}
PLATFORMS['win32']['vista'] = {'name': "WINNT 6.0"}

PLATFORMS['linux']['slave_platforms'] = ['linux']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['linux'] = {'name': "Linux"}

######## mozilla-1.9.0
BRANCHES['mozilla-1.9.0']['branch_name'] = "Firefox3.0"
BRANCHES['mozilla-1.9.0']['build_branch'] = "1.9.0"
BRANCHES['mozilla-1.9.0']['fetch_symbols'] = False
# How many chrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.0']['chrome_tests'] = (1,True, [])
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.0']['nochrome_tests'] = (1,True, [])
BRANCHES['mozilla-1.9.0']['jss_tests'] = (0,True, [])
BRANCHES['mozilla-1.9.0']['tp4_tests'] = (0,True, [])
BRANCHES['mozilla-1.9.0']['ftp_urls'] = {
    'win32': [
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/FX-WIN32-TBOX-mozilla1.9.0/",
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla1.9.0/",
        ],
    'linux': [
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/fx-linux-tbox-mozilla1.9.0/",
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla1.9.0/",
        ],
    'macosx': [
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/bm-xserve08-mozilla1.9.0/",
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla1.9.0/",
        ],
}
BRANCHES['mozilla-1.9.0']['ftp_searchstrings'] = {
    'win32': "en-US.win32.zip",
    'linux': "en-US.linux-i686.tar.bz2",
    'macosx': "en-US.mac.dmg",
}

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['fetch_symbols'] = True
# How many chrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-central']['chrome_tests'] = (1,True, [])
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-central']['nochrome_tests'] = (1,True, [])
# How many jss tests per build to run, and whether to merge build requests
BRANCHES['mozilla-central']['jss_tests'] = (1,True, [])
# How many dirty ts tests per build to run, and whether to merge build requests
BRANCHES['mozilla-central']['dirty_tests'] = (1, True, TALOS_DIRTY_ADDONS)
# How many tp4 tests per build to run, and whether to merge build requests
BRANCHES['mozilla-central']['tp4_tests'] = (1,True, [])

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['branch_name'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['build_branch'] = "1.9.1"
BRANCHES['mozilla-1.9.1']['fetch_symbols'] = True
# How many chrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.1']['chrome_tests'] = (1,True, [])
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.1']['nochrome_tests'] = (1,True, [])
# How many jss tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.1']['jss_tests'] = (1,True, [])
# How many dirty ts tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.1']['dirty_tests'] = (1, True, TALOS_DIRTY_ADDONS)
# How many tp4 tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.1']['tp4_tests'] = (1,True, [])

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['branch_name'] = "Firefox3.6"
BRANCHES['mozilla-1.9.2']['build_branch'] = "1.9.2"
BRANCHES['mozilla-1.9.2']['fetch_symbols'] = True
# How many chrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.2']['chrome_tests'] = (1,True, [])
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.2']['nochrome_tests'] = (1,True, [])
# How many jss tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.2']['jss_tests'] = (1,True, [])
# How many dirty ts tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.2']['dirty_tests'] = (1, True, TALOS_DIRTY_ADDONS)
# How many tp4 tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.2']['tp4_tests'] = (1,True, [])

######## tracemonkey
BRANCHES['tracemonkey']['branch_name'] = "TraceMonkey"
BRANCHES['tracemonkey']['build_branch'] = "TraceMonkey"
BRANCHES['tracemonkey']['fetch_symbols'] = True
# How many chrome tests per build to run, and whether to merge build requests
BRANCHES['tracemonkey']['chrome_tests'] = (1,True, [])
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['tracemonkey']['nochrome_tests'] = (1,True, [])
# How many jss tests per build to run, and whether to merge build requests
BRANCHES['tracemonkey']['jss_tests'] = (1,True, [])
# How many dirty ts tests per build to run, and whether to merge build requests
BRANCHES['tracemonkey']['dirty_tests'] = (1, True, TALOS_DIRTY_ADDONS)
# How many tp4 tests per build to run, and whether to merge build requests
BRANCHES['tracemonkey']['tp4_tests'] = (1,True, [])

######## places
BRANCHES['places']['branch_name'] = "Places"
BRANCHES['places']['build_branch'] = "Places"
BRANCHES['places']['fetch_symbols'] = True
# How many chrome tests per build to run, and whether to merge build requests
BRANCHES['places']['chrome_tests'] = (1,True, [])
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['places']['nochrome_tests'] = (0,True, [])
# How many jss tests per build to run, and whether to merge build requests
BRANCHES['places']['jss_tests'] = (1,True, [])
# How many dirty ts tests per build to run, and whether to merge build requests
BRANCHES['places']['dirty_tests'] = (1, True, TALOS_DIRTY_ADDONS)
# How many tp4 tests per build to run, and whether to merge build requests
BRANCHES['places']['tp4_tests'] = (1,True, [])
