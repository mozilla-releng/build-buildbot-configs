from copy import deepcopy

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
    'scroll': GRAPH_CONFIG + ['--activeTests', 'tscroll'],
    'dromaeo': GRAPH_CONFIG + ['--activeTests', 'dromaeo_basics:dromaeo_v8:dromaeo_sunspider:dromaeo_jslib:dromaeo_css:dromaeo_dom'],
}

SLAVES = {
    'fedora': ["talos-r3-fed-%03i" % x for x in range(1,41)],
    'fedora64' : ["talos-r3-fed64-%03i" % x for x in range (1,21)],
    'xp': ["talos-r3-xp-%03i" % x for x in range(1,41)],
    'win7': ["talos-r3-w7-%03i" % x for x in range(1,41)],
    'leopard': ["talos-r3-leopard-%03i" % x for x in range(1,41)],
    'snowleopard': ["talos-r3-snow-%03i" % x for x in range(1,21)],
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

PLATFORMS['macosx']['slave_platforms'] = ['leopard', 'snowleopard']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['leopard'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx']['snowleopard'] = {'name': "Rev3 MacOSX Snow Leopard 10.6.2"}

PLATFORMS['win32']['slave_platforms'] = ['xp', 'win7']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "Rev3 WINNT 5.1"}
PLATFORMS['win32']['win7'] = {'name': "Rev3 WINNT 6.1"}

PLATFORMS['linux']['slave_platforms'] = ['fedora']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': "Rev3 Fedora 12"}

PLATFORMS['linux64']['slave_platforms'] = ['fedora64']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': "Rev3 Fedora 12x64"}


# Copy the slave names into PLATFORMS[platform][slave_platform]
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = SLAVES[slave_platform]

ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['linux64']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['macosx']['slave_platforms']

NO_WIN = PLATFORMS['macosx']['slave_platforms'] + PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms'] 

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    'build_tools_repo_path': 'users/stage-ffxbld/tools',
    # turn on platforms as we get them running
    'platforms': {
        'macosx': {},
    },
}

PLATFORM_UNITTEST_VARS = {
        'linux': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
        },
        'win32': {
            'builds_before_reboot': 1,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
        },
        'macosx': {
            'builds_before_reboot': 1,
            'opt_unittest_suites': [
                # Turn on chunks for mochitests
                ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
                ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
                    'mochitest-ipcplugins']),
                ('reftest', ['reftest']),
                ('crashtest', ['crashtest']),
                ('xpcshell', ['xpcshell']),
                ('jsreftest', ['jsreftest']),
            ],
            'debug_unittest_suites': [
                # Turn on chunks for mochitests
                ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
                ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
                    'mochitest-ipcplugins']),
                ('reftest', ['reftest']),
                ('crashtest', ['crashtest']),
                ('xpcshell', ['xpcshell']),
                ('jsreftest', ['jsreftest']),
            ],
        },
        'linux64': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': 0},
        },
}
UNITTEST_SUITES = {
    'opt_unittest_suites': [
            # Turn on chunks for mochitests
            ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
            ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
                'mochitest-a11y', 'mochitest-ipcplugins']),
            ('reftest', ['reftest']),
            ('crashtest', ['crashtest']),
            ('xpcshell', ['xpcshell']),
            ('jsreftest', ['jsreftest']),
        ],
    'debug_unittest_suites': [
            # Turn on chunks for mochitests
            ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
            ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
                'mochitest-a11y', 'mochitest-ipcplugins']),
            ('reftest', ['reftest']),
            ('crashtest', ['crashtest']),
            ('xpcshell', ['xpcshell']),
            ('jsreftest', ['jsreftest']),
        ],
}

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in BRANCH_UNITTEST_VARS.items():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_UNITTEST_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value
    for platform in BRANCHES[branch]['platforms']:
        for key, value in UNITTEST_SUITES.items():
            # don't override platform specified unittests
            if key in BRANCHES[branch]['platforms'][platform]:
                continue
            BRANCHES[branch]['platforms'][platform][key] = deepcopy(value)

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
BRANCHES['mozilla-1.9.0']['dromaeo_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['cold_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['scroll_tests'] = (0, True, {}, ALL_PLATFORMS)
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
BRANCHES['mozilla-central']['tinderbox_tree'] = "Firefox"
BRANCHES['mozilla-central']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-central']['fetch_symbols'] = True
BRANCHES['mozilla-central']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-central']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-central']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['mozilla-central']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['platforms']['macosx']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['macosx']['enable_debug_unittests'] = True

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['branch_name'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['build_branch'] = "1.9.1"
BRANCHES['mozilla-1.9.1']['tinderbox_tree'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.1']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.1']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['mozilla-1.9.1']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

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
BRANCHES['mozilla-1.9.2']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['mozilla-1.9.2']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## tracemonkey
BRANCHES['tracemonkey']['branch_name'] = "TraceMonkey"
BRANCHES['tracemonkey']['build_branch'] = "TraceMonkey"
BRANCHES['tracemonkey']['tinderbox_tree'] = "TraceMonkey"
BRANCHES['tracemonkey']['talos_command'] = TALOS_CMD
BRANCHES['tracemonkey']['fetch_symbols'] = True
BRANCHES['tracemonkey']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['tracemonkey']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['tracemonkey']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['tracemonkey']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['v8_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## places
BRANCHES['places']['branch_name'] = "Places"
BRANCHES['places']['build_branch'] = "Places"
BRANCHES['places']['tinderbox_tree'] = "Places"
BRANCHES['places']['talos_command'] = TALOS_CMD
BRANCHES['places']['fetch_symbols'] = True
BRANCHES['places']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['places']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['places']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['places']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['places']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## electrolysis
BRANCHES['electrolysis']['branch_name'] = "Electrolysis"
BRANCHES['electrolysis']['build_branch'] = "Electrolysis"
BRANCHES['electrolysis']['tinderbox_tree'] = "Electrolysis"
BRANCHES['electrolysis']['talos_command'] = TALOS_CMD
BRANCHES['electrolysis']['fetch_symbols'] = True
BRANCHES['electrolysis']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['electrolysis']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['electrolysis']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['electrolysis']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## firefox-lorentz
BRANCHES['firefox-lorentz']['branch_name'] = "Firefox-Lorentz"
BRANCHES['firefox-lorentz']['build_branch'] = "Firefox-Lorentz"
BRANCHES['firefox-lorentz']['tinderbox_tree'] = "Firefox-Lorentz"
BRANCHES['firefox-lorentz']['talos_command'] = TALOS_CMD
BRANCHES['firefox-lorentz']['fetch_symbols'] = True
BRANCHES['firefox-lorentz']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['firefox-lorentz']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['firefox-lorentz']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## addonsmgr
BRANCHES['addonsmgr']['branch_name'] = "Addonsmgr"
BRANCHES['addonsmgr']['build_branch'] = "Addonsmgr"
BRANCHES['addonsmgr']['tinderbox_tree'] = "AddonsMgr"
BRANCHES['addonsmgr']['talos_command'] = TALOS_CMD
BRANCHES['addonsmgr']['fetch_symbols'] = True
BRANCHES['addonsmgr']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['jss_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['addonsmgr']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['addonsmgr']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['addonsmgr']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
