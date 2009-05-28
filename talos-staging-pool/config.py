from buildbot.steps.shell import WithProperties

GRAPH_CONFIG = ['--oldresultsServer', 'graphs-stage.mozilla.org',
        '--oldresultsLink', '/server/bulk.cgi', '--resultsServer',
        'graphs-stage2.mozilla.org', '--resultsLink', '/server/collect.cgi']
TALOS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:tp:tdhtml:tsvg:twinopen:tsspider:tgfx']

TALOS_NOCHOME_CONFIG_OPTIONS = GRAPH_CONFIG + TALOS_CONFIG_OPTIONS + ['--noChrome']

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

SLAVES = {
    'linux': ["talos-rev1-linux%02i" % x for x in range(1,5)],
    'xp': ["talos-rev1-xp%02i" % x for x in range(1,5)],
    'vista': ["talos-rev1-vista%02i" % x for x in range(1,5)],
    'tiger': ["talos-rev1-tiger%02i" % x for x in range(1,5)],
    'leopard': ["talos-rev2-leopard%02i" % x for x in range(1,2)],
}

BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.1': {},
    'mozilla-1.9.0': {},
    'tracemonkey': {},
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
BRANCHES['mozilla-1.9.0']['chrome_tests'] = (1,True)
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.0']['nochrome_tests'] = (1,True)
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
BRANCHES['mozilla-central']['chrome_tests'] = (1,True)
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-central']['nochrome_tests'] = (1,True)

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['branch_name'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['build_branch'] = "1.9.1"
BRANCHES['mozilla-1.9.1']['fetch_symbols'] = True
# How many chrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.1']['chrome_tests'] = (1,True)
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['mozilla-1.9.1']['nochrome_tests'] = (1,True)

######## tracemonkey
BRANCHES['tracemonkey']['branch_name'] = "TraceMonkey"
BRANCHES['tracemonkey']['build_branch'] = "TraceMonkey"
BRANCHES['tracemonkey']['fetch_symbols'] = True
# How many chrome tests per build to run, and whether to merge build requests
BRANCHES['tracemonkey']['chrome_tests'] = (1,True)
# How many nochrome tests per build to run, and whether to merge build requests
BRANCHES['tracemonkey']['nochrome_tests'] = (1,True)
