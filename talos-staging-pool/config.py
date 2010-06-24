from copy import deepcopy
from twisted.python import log

from buildbot.steps.shell import WithProperties

GRAPH_CONFIG = ['--resultsServer', 'graphs-stage.mozilla.org',
    '--resultsLink', '/server/collect.cgi']

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_DIRTY_OPTS = {'talosAddOns': ['profiles/dirtyDBs.zip', 'profiles/dirtyMaxDBs.zip']}

TALOS_TP4_OPTS = {'plugins': 'zips/plugins.zip', 'pageset': 'zips/pagesets.zip'}

SUITES = {
    'chrome': GRAPH_CONFIG + ['--activeTests', 'tdhtml:twinopen:tsspider:tgfx'],
    'nochrome': GRAPH_CONFIG + ['--activeTests', 'tdhtml:twinopen:tsspider:tgfx', '--noChrome'],
    'dirty': GRAPH_CONFIG + ['--activeTests', 'ts:ts_places_generated_min:ts_places_generated_med:ts_places_generated_max:ts_cold_generated_min:ts_cold_generated_med:ts_cold_generated_max'],
    'tp4': GRAPH_CONFIG + ['--activeTests', 'tp4'],
    'cold': GRAPH_CONFIG + ['--activeTests', 'ts:ts_cold'],
    'v8': GRAPH_CONFIG + ['--activeTests', 'v8'],
    'svg': GRAPH_CONFIG + ['--activeTests', 'tsvg:tsvg_opacity'],
    'scroll': GRAPH_CONFIG + ['--activeTests', 'tscroll'],
    'dromaeo': GRAPH_CONFIG + ['--activeTests', 'dromaeo_basics:dromaeo_v8:dromaeo_sunspider:dromaeo_jslib:dromaeo_css:dromaeo_dom'],
}

SLAVES = {
    'fedora': ["talos-r3-fed-%03i" % x for x in range(1,4)],
    'fedora64' : ["talos-r3-fed64-%03i" % x for x in range (1,4)],
    'xp': ["talos-r3-xp-%03i" % x for x in range(1,4)],
    'win7': ["talos-r3-w7-%03i" % x for x in range(1,4)],
    'leopard': ["talos-r3-leopard-%03i" % x for x in range(1,4)],
    'snowleopard': ["talos-r3-snow-%03i" % x for x in range(1,4)],
}

BRANCHES = {
    'mozilla-central': {},
    'mozilla-2.0': {},
    'mozilla-1.9.2': {},
    'mozilla-1.9.1': {},
    'mozilla-1.9.0': {},
    'tracemonkey': {},
    'places': {},
    'electrolysis': {},
    'addonsmgr': {},
    'tryserver': {},
    'maple': {},
    'cedar': {},
    'birch': {},
    'jaegermonkey': {},
}

PLATFORMS = {
    'macosx': {},
    'macosx64': {},
    'win32': {},
    'linux': {},
    'linux64' : {},
}

PLATFORMS['macosx']['slave_platforms'] = ['leopard']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['leopard'] = {'name': "MacOSX Leopard 10.5.8"}

PLATFORMS['macosx64']['slave_platforms'] = ['snowleopard']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['snowleopard'] = {'name': "MacOSX Snow Leopard 10.6.2"}

PLATFORMS['win32']['slave_platforms'] = ['xp', 'win7']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "WINNT 5.1"}
PLATFORMS['win32']['win7'] = {'name': "WINNT 6.1"}

PLATFORMS['linux']['slave_platforms'] = ['fedora']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': "Fedora 12"}

PLATFORMS['linux64']['slave_platforms'] = ['fedora64']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': "Fedora 12x64"}


# Copy the slave names into PLATFORMS[platform][slave_platform]
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = SLAVES[slave_platform]

ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['linux64']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['macosx64']['slave_platforms'] + \
                PLATFORMS['macosx']['slave_platforms']

NO_WIN = PLATFORMS['macosx']['slave_platforms'] + PLATFORMS['macosx64']['slave_platforms'] + PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms']

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    'build_tools_repo_path': 'users/stage-ffxbld/tools',
    # turn on platforms as we get them running
    'platforms': {
        'linux': {},
        'linux64': {},
        'macosx': {},
        'macosx64': {},
        'win32': {},
    },
}

PLATFORM_UNITTEST_VARS = {
        'linux': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'fedora': {},
        },
        'linux64': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'fedora64': {},
        },
        'win32': {
            'builds_before_reboot': 1,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'env_name' : 'win32-perf-unittest',
            # We can't yet run unit tests for WinXP - see bug 563036
            'xp': {
                'opt_unittest_suites': [],
                'debug_unittest_suites': [],
            },
            # We want to add reftests-d2d for Win7
            'win7': {
                'opt_unittest_suites': [
                    # Turn on chunks for mochitests
                    ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
                    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
                        'mochitest-a11y', 'mochitest-ipcplugins']),
                    ('reftest', ['reftest']),
                    ('reftest-d2d', ['reftest-d2d']),
                    ('crashtest', ['crashtest']),
                    ('xpcshell', ['xpcshell']),
                    ('jsreftest', ['jsreftest']),
                ],
            }
        },
        'macosx': {
            'builds_before_reboot': 1,
            # We don't have a11y on mochitest-other for Mac
            'leopard': {
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
        },
        'macosx64': {
            'builds_before_reboot': 1,
            'download_symbols': False,
            # We don't have a11y on mochitest-other for Mac
            'snowleopard': {
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
            }
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

# Copy unittest vars in first, then platform vars, then add unittest suites to each active platform
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
        # If we want to test for a certain architeture for multiple operating systems.
        # An example is that win32 packages can be tested on 'xp' and 'win7'
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            for key, value in UNITTEST_SUITES.items():
                # don't override platform specified unittests
                if key in BRANCHES[branch]['platforms'][platform][slave_platform]:
                    continue
                BRANCHES[branch]['platforms'][platform][slave_platform][key] = deepcopy(value)

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
BRANCHES['mozilla-1.9.0']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-1.9.0']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.0']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
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
    'macosx64': [],
}
BRANCHES['mozilla-1.9.0']['ftp_searchstrings'] = {
    'win32': "en-US.win32.zip",
    'linux': "en-US.linux-i686.tar.bz2",
    'linux64': "en-US.linux-x86_64.tar.bz2",
    'macosx': "en-US.mac.dmg",
    'macosx64': "en-US.mac.dmg",
}

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-central']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-central']['fetch_symbols'] = True
BRANCHES['mozilla-central']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-central']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
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
BRANCHES['mozilla-central']['platforms']['macosx64']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['macosx64']['enable_debug_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['enable_debug_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux64']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux64']['enable_debug_unittests'] = True
BRANCHES['mozilla-central']['platforms']['win32']['enable_opt_unittests'] = True
# We can't yet run unit tests on debug builds - see bug 562459
BRANCHES['mozilla-central']['platforms']['win32']['enable_debug_unittests'] = False 

######## mozilla-2.0
BRANCHES['mozilla-2.0']['branch_name'] = "Firefox4.0"
BRANCHES['mozilla-2.0']['build_branch'] = "2.0"
BRANCHES['mozilla-2.0']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-2.0']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-2.0']['fetch_symbols'] = True
BRANCHES['mozilla-2.0']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-2.0']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['mozilla-2.0']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['repo_path'] = "mozilla-2.0"
BRANCHES['mozilla-2.0']['platforms']['macosx']['enable_opt_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['macosx']['enable_debug_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['macosx64']['enable_opt_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['macosx64']['enable_debug_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['linux']['enable_debug_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['linux64']['enable_opt_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['linux64']['enable_debug_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['win64']['enable_opt_unittests'] = True
BRANCHES['mozilla-2.0']['platforms']['win64']['enable_debug_unittests'] = True

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['branch_name'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['build_branch'] = "1.9.1"
BRANCHES['mozilla-1.9.1']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-1.9.1']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.1']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.1']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-1.9.1']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
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
BRANCHES['mozilla-1.9.2']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-1.9.2']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.2']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.2']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-1.9.2']['release_tests'] = 5
BRANCHES['mozilla-1.9.2']['fetch_release_symbols'] = False
BRANCHES['mozilla-1.9.2']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['mozilla-1.9.2']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['repo_path'] = "mozilla-1.9.2"
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_debug_unittests'] = True

######## tracemonkey
BRANCHES['tracemonkey']['branch_name'] = "TraceMonkey"
BRANCHES['tracemonkey']['build_branch'] = "TraceMonkey"
BRANCHES['tracemonkey']['tinderbox_tree'] = "MozillaTest"
BRANCHES['tracemonkey']['talos_command'] = TALOS_CMD
BRANCHES['tracemonkey']['fetch_symbols'] = True
BRANCHES['tracemonkey']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['tracemonkey']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['tracemonkey']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['tracemonkey']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['tracemonkey']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['v8_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['repo_path'] = "tracemonkey"
BRANCHES['tracemonkey']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['tracemonkey']['platforms']['linux']['enable_debug_unittests'] = True
BRANCHES['tracemonkey']['platforms']['linux64']['enable_opt_unittests'] = True
BRANCHES['tracemonkey']['platforms']['linux64']['enable_debug_unittests'] = True

######## places
BRANCHES['places']['branch_name'] = "Places"
BRANCHES['places']['build_branch'] = "Places"
BRANCHES['places']['tinderbox_tree'] = "MozillaTest"
BRANCHES['places']['talos_command'] = TALOS_CMD
BRANCHES['places']['fetch_symbols'] = True
BRANCHES['places']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['places']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
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
BRANCHES['electrolysis']['tinderbox_tree'] = "MozillaTest"
BRANCHES['electrolysis']['talos_command'] = TALOS_CMD
BRANCHES['electrolysis']['fetch_symbols'] = True
BRANCHES['electrolysis']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['electrolysis']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['nochrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['electrolysis']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['electrolysis']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['electrolysis']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## addonsmgr
BRANCHES['addonsmgr']['branch_name'] = "Addonsmgr"
BRANCHES['addonsmgr']['build_branch'] = "Addonsmgr"
BRANCHES['addonsmgr']['tinderbox_tree'] = "MozillaTest"
BRANCHES['addonsmgr']['talos_command'] = TALOS_CMD
BRANCHES['addonsmgr']['fetch_symbols'] = True
BRANCHES['addonsmgr']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['addonsmgr']['chrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['nochrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['addonsmgr']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['addonsmgr']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['addonsmgr']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addonsmgr']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## maple
BRANCHES['maple']['branch_name'] = "Maple"
BRANCHES['maple']['build_branch'] = "Maple"
BRANCHES['maple']['tinderbox_tree'] = "MozillaTest"
BRANCHES['maple']['talos_command'] = TALOS_CMD
BRANCHES['maple']['fetch_symbols'] = True
BRANCHES['maple']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['maple']['chrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['nochrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['maple']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['maple']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['maple']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## cedar
BRANCHES['cedar']['branch_name'] = "Cedar"
BRANCHES['cedar']['build_branch'] = "Cedar"
BRANCHES['cedar']['tinderbox_tree'] = "MozillaTest"
BRANCHES['cedar']['talos_command'] = TALOS_CMD
BRANCHES['cedar']['fetch_symbols'] = True
BRANCHES['cedar']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['cedar']['chrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['nochrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['cedar']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['cedar']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['cedar']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## birch
BRANCHES['birch']['branch_name'] = "Birch"
BRANCHES['birch']['build_branch'] = "Birch"
BRANCHES['birch']['tinderbox_tree'] = "MozillaTest"
BRANCHES['birch']['talos_command'] = TALOS_CMD
BRANCHES['birch']['fetch_symbols'] = True
BRANCHES['birch']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['birch']['chrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['nochrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['birch']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['birch']['cold_tests'] = (1, True, {}, NO_WIN)
BRANCHES['birch']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)

######## jaegermonkey
BRANCHES['jaegermonkey']['branch_name'] = "Jaegermonkey"
BRANCHES['jaegermonkey']['build_branch'] = "Jaegermonkey"
BRANCHES['jaegermonkey']['tinderbox_tree'] = "MozillaTest"
BRANCHES['jaegermonkey']['talos_command'] = TALOS_CMD
BRANCHES['jaegermonkey']['fetch_symbols'] = True
BRANCHES['jaegermonkey']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['jaegermonkey']['chrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['nochrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['dromaeo_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['cold_tests'] = (0, True, {}, NO_WIN)
BRANCHES['jaegermonkey']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['scroll_tests'] = (0, True, {}, ALL_PLATFORMS)

######## tryserver
BRANCHES['tryserver']['branch_name'] = "Tryserver"
BRANCHES['tryserver']['build_branch'] = "Tryserver"
BRANCHES['tryserver']['tinderbox_tree'] = "MozillaTest"
BRANCHES['tryserver']['talos_command'] = TALOS_CMD
BRANCHES['tryserver']['fetch_symbols'] = True
BRANCHES['tryserver']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['tryserver']['chrome_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['nochrome_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['dromaeo_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['dirty_tests'] = (1, False, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['tryserver']['tp4_tests'] = (1, False, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['tryserver']['cold_tests'] = (1, False, {}, NO_WIN)
BRANCHES['tryserver']['svg_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['v8_tests'] = (0, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['scroll_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['repo_path'] = "try"
BRANCHES['tryserver']['platforms']['macosx']['enable_opt_unittests'] = True
BRANCHES['tryserver']['platforms']['macosx']['enable_debug_unittests'] = True
BRANCHES['tryserver']['platforms']['macosx64']['enable_opt_unittests'] = True
BRANCHES['tryserver']['platforms']['macosx64']['enable_debug_unittests'] = True
BRANCHES['tryserver']['platforms']['linux']['enable_opt_unittests'] = True
BRANCHES['tryserver']['platforms']['linux']['enable_debug_unittests'] = True
BRANCHES['tryserver']['platforms']['linux64']['enable_opt_unittests'] = True
BRANCHES['tryserver']['platforms']['linux64']['enable_debug_unittests'] = True
BRANCHES['tryserver']['platforms']['win64']['enable_opt_unittests'] = True
BRANCHES['tryserver']['platforms']['win64']['enable_debug_unittests'] = True
