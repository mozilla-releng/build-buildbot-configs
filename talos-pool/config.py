from buildbot.steps.shell import WithProperties

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org',
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
    'tiger': ["talos-rev2-tiger%02i" % x for x in range(1,21)],
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
}

PLATFORMS = {
    'macosx': {},
}

PLATFORMS['macosx']['slave_platforms'] = ['tiger']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['tiger'] = {'name': "MacOSX Darwin 8.8.1"}

# Copy the slave names into PLATFORMS[platform][slave_platform]
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = SLAVES[slave_platform]

ALL_PLATFORMS = PLATFORMS['macosx']['slave_platforms']

########
# Entries in BRANCHES for tests should be a tuple of:
# - Number of tests to run per build
# - Whether queue merging is on
# - TalosFactory options
# - Which platforms to run on

######## mozilla-1.9.0
BRANCHES['mozilla-1.9.0']['branch_name'] = "Firefox3.0"
BRANCHES['mozilla-1.9.0']['build_branch'] = "1.9.0"
BRANCHES['mozilla-1.9.0']['tinderbox_tree'] = "Firefox3.0"
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

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['branch_name'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['build_branch'] = "1.9.1"
BRANCHES['mozilla-1.9.1']['tinderbox_tree'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.1']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.1']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['cold_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['branch_name'] = "Firefox3.6"
BRANCHES['mozilla-1.9.2']['build_branch'] = "1.9.2"
BRANCHES['mozilla-1.9.2']['tinderbox_tree'] = "Firefox3.6"
BRANCHES['mozilla-1.9.2']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.2']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.2']['release_tests'] = 5
BRANCHES['mozilla-1.9.2']['fetch_release_symbols'] = False
BRANCHES['mozilla-1.9.2']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['cold_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)

######## firefox-lorentz
BRANCHES['firefox-lorentz']['branch_name'] = "Firefox-Lorentz"
BRANCHES['firefox-lorentz']['build_branch'] = "Firefox-Lorentz"
BRANCHES['firefox-lorentz']['tinderbox_tree'] = "Firefox-Lorentz"
BRANCHES['firefox-lorentz']['talos_command'] = TALOS_CMD
BRANCHES['firefox-lorentz']['fetch_symbols'] = True
BRANCHES['firefox-lorentz']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['cold_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
