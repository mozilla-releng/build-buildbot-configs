from buildbot.steps.shell import WithProperties

GRAPH_CONFIG = ['--resultsServer', 'graphs-stage.mozilla.org',
    '--resultsLink', '/server/collect.cgi']

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_DIRTY_OPTS = {'talosAddOns': ['/builds/buildbot/profiles/dirtyDBs.zip', '/builds/buildbot/profiles/dirtyMaxDBs.zip']}

TALOS_TP4_OPTS = {'plugins': 'zips/plugins.zip', 'pageset': 'zips/pagesets.zip'} 

SUITES = {
    'chrome': GRAPH_CONFIG + ['--activeTests', 'tdhtml:twinopen:tsspider:tgfx'],
    'nochrome': GRAPH_CONFIG + ['--activeTests', 'tdhtml:twinopen:tsspider:tgfx', '--noChrome'],
    'jss': GRAPH_CONFIG + ['--activeTests', 'tjss'],
    'dirty': GRAPH_CONFIG + ['--activeTests', 'ts:ts_places_generated_min:ts_places_generated_med:ts_places_generated_max:ts_cold_generated_min:ts_cold_generated_med:ts_cold_generated_max'],
    'tp4': GRAPH_CONFIG + ['--activeTests', 'tp4'],
    'cold': GRAPH_CONFIG + ['--activeTests', 'ts:ts_cold'],
    'v8': GRAPH_CONFIG + ['--activeTests', 'v8'],
    'svg': GRAPH_CONFIG + ['--activeTests', 'tsvg:tsvg_opacity'],
}

SLAVES = {
    'linux': ["talos-rev1-linux%02i" % x for x in range(1,6)],
    'linux64' : ["talos-rev2-x64%02i" % x for x in range (1,2)],
    'xp': ["talos-rev1-xp%02i" % x for x in range(1,5)],
    'vista': ["talos-rev1-vista%02i" % x for x in range(1,5)],
    'tiger': ["talos-rev1-tiger%02i" % x for x in range(1,5)],
    'leopard': ["talos-rev1-leopard%02i" % x for x in range(1,5)],
}

BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.2': {},
    'mozilla-1.9.1': {},
    'mozilla-1.9.0': {},
    'tracemonkey': {},
    'places': {},
    'electrolysis': {},
    'firefox-lorentz': {},
    'addonsmgr': {},
}

PLATFORMS = {
    'macosx': {},
    'win32': {},
    'linux': {},
    'linux64' : {},
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

PLATFORMS['linux64']['slave_platforms'] = ['linux64']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['linux64'] = {'name': "Linux64"}

# Copy the slave names into PLATFORMS[platform][slave_platform]
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = SLAVES[slave_platform]

ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['linux64']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['macosx']['slave_platforms'] 
NO_TIGER = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms'] + PLATFORMS['win32']['slave_platforms'] + ['leopard']
NO_WIN = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms'] + PLATFORMS['macosx']['slave_platforms']
NO_TIGER_NO_WIN = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms'] + ['leopard']

########
# Entries in BRANCHES for tests should be a tuple of:
# - Number of tests to run per build
# - Whether queue merging is on
# - TalosFactory options
# - Which platforms to run on

######## mozilla-1.9.0
BRANCHES['mozilla-1.9.0']['branch_name'] = "Firefox3.0"
BRANCHES['mozilla-1.9.0']['build_branch'] = "1.9.0"
BRANCHES['mozilla-1.9.0']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-1.9.0']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.0']['fetch_symbols'] = False
BRANCHES['mozilla-1.9.0']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['jss_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['cold_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['ftp_urls'] = {
    'win32': [
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/FX-WIN32-TBOX-mozilla1.9.0/",
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla1.9.0/",
        ],
    'linux': [
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/fx-linux-tbox-mozilla1.9.0/",
        "http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla1.9.0/",
        ],
    'linux64': [
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
    'linux64': "en-US.linux-x86_64.tar.bz2",
    'macosx': "en-US.mac.dmg",
}

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-central']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-central']['fetch_symbols'] = True
BRANCHES['mozilla-central']['chrome_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['mozilla-central']['nochrome_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['mozilla-central']['jss_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['mozilla-central']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, NO_TIGER)
BRANCHES['mozilla-central']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, NO_TIGER)
BRANCHES['mozilla-central']['cold_tests'] = (1, True, {}, NO_TIGER_NO_WIN)
BRANCHES['mozilla-central']['svg_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['mozilla-central']['v8_tests'] = (0, True, {}, NO_TIGER)

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['branch_name'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['build_branch'] = "1.9.1"
BRANCHES['mozilla-1.9.1']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-1.9.1']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.1']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.1']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['mozilla-1.9.1']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['branch_name'] = "Firefox3.6"
BRANCHES['mozilla-1.9.2']['build_branch'] = "1.9.2"
BRANCHES['mozilla-1.9.2']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-1.9.2']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.2']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.2']['release_tests'] = 5
BRANCHES['mozilla-1.9.2']['fetch_release_symbols'] = False
BRANCHES['mozilla-1.9.2']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['mozilla-1.9.2']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)

######## tracemonkey
BRANCHES['tracemonkey']['branch_name'] = "TraceMonkey"
BRANCHES['tracemonkey']['build_branch'] = "TraceMonkey"
BRANCHES['tracemonkey']['tinderbox_tree'] = "MozillaTest"
BRANCHES['tracemonkey']['talos_command'] = TALOS_CMD
BRANCHES['tracemonkey']['fetch_symbols'] = True
BRANCHES['tracemonkey']['chrome_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['tracemonkey']['nochrome_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['tracemonkey']['jss_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['tracemonkey']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, NO_TIGER)
BRANCHES['tracemonkey']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, NO_TIGER)
BRANCHES['tracemonkey']['cold_tests'] = (1, True, {}, NO_TIGER_NO_WIN)
BRANCHES['tracemonkey']['svg_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['tracemonkey']['v8_tests'] = (1, True, {}, NO_TIGER)

######## places
BRANCHES['places']['branch_name'] = "Places"
BRANCHES['places']['build_branch'] = "Places"
BRANCHES['places']['tinderbox_tree'] = "MozillaTest"
BRANCHES['places']['talos_command'] = TALOS_CMD
BRANCHES['places']['fetch_symbols'] = True
BRANCHES['places']['chrome_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['places']['nochrome_tests'] = (0, True, {}, NO_TIGER)
BRANCHES['places']['jss_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['places']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, NO_TIGER)
BRANCHES['places']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, NO_TIGER)
BRANCHES['places']['cold_tests'] = (1, True, {}, NO_TIGER_NO_WIN)
BRANCHES['places']['svg_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['places']['v8_tests'] = (0, True, {}, NO_TIGER)

######## electrolysis
BRANCHES['electrolysis']['branch_name'] = "Electrolysis"
BRANCHES['electrolysis']['build_branch'] = "Electrolysis"
BRANCHES['electrolysis']['tinderbox_tree'] = "MozillaTest"
BRANCHES['electrolysis']['talos_command'] = TALOS_CMD
BRANCHES['electrolysis']['fetch_symbols'] = True
BRANCHES['electrolysis']['chrome_tests'] = (1,True, {}, NO_TIGER)
BRANCHES['electrolysis']['nochrome_tests'] = (0,True, {}, NO_TIGER)
BRANCHES['electrolysis']['jss_tests'] = (1,True, {}, NO_TIGER)
BRANCHES['electrolysis']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, NO_TIGER)
BRANCHES['electrolysis']['tp4_tests'] = (1,True, TALOS_TP4_OPTS, NO_TIGER)
BRANCHES['electrolysis']['cold_tests'] = (1, True, {}, NO_TIGER_NO_WIN)
BRANCHES['electrolysis']['svg_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['electrolysis']['v8_tests'] = (0, True, {}, NO_TIGER)

######## firefox-lorentz
BRANCHES['firefox-lorentz']['branch_name'] = "Firefox-Lorentz"
BRANCHES['firefox-lorentz']['build_branch'] = "Firefox-Lorentz"
BRANCHES['firefox-lorentz']['tinderbox_tree'] = "MozillaTest"
BRANCHES['firefox-lorentz']['talos_command'] = TALOS_CMD
BRANCHES['firefox-lorentz']['fetch_symbols'] = True
BRANCHES['firefox-lorentz']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['firefox-lorentz']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)

######## addonsmgr
BRANCHES['addonsmgr']['branch_name'] = "Addonsmgr"
BRANCHES['addonsmgr']['build_branch'] = "Addonsmgr"
BRANCHES['addonsmgr']['tinderbox_tree'] = "MozillaTest"
BRANCHES['addonsmgr']['talos_command'] = TALOS_CMD
BRANCHES['addonsmgr']['fetch_symbols'] = True
BRANCHES['addonsmgr']['chrome_tests'] = (0, True, {}, NO_TIGER)
BRANCHES['addonsmgr']['nochrome_tests'] = (0, True, {}, NO_TIGER)
BRANCHES['addonsmgr']['jss_tests'] = (1, True, {}, NO_TIGER)
BRANCHES['addonsmgr']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, NO_TIGER)
BRANCHES['addonsmgr']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, NO_TIGER)
BRANCHES['addonsmgr']['cold_tests'] = (1, True, {}, NO_TIGER_NO_WIN)
BRANCHES['addonsmgr']['svg_tests'] = (0, True, {}, NO_TIGER)
BRANCHES['addonsmgr']['v8_tests'] = (0, True, {}, NO_TIGER)
