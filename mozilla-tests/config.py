from copy import deepcopy

from buildbot.steps.shell import WithProperties

import localconfig
reload(localconfig)
from localconfig import SLAVES, GLOBAL_VARS, GRAPH_CONFIG

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_ADDON_CMD = ['python', 'run_tests.py', '--screen', WithProperties('%(configFile)s')]

TALOS_DIRTY_OPTS = {'talosAddOns': ['profiles/dirtyDBs.zip', 'profiles/dirtyMaxDBs.zip']}

TALOS_TP4_OPTS = {'plugins': 'zips/plugins.zip', 'pageset': 'zips/pagesets.zip'}

TALOS_ADDON_OPTS = {'addonTester' : True, 'plugins': 'zips/plugins.zip', 'pageset': 'zips/pagesets.zip'}

TALOS_REMOTE_FENNEC_OPTS = { 'productName':  'fennec',
                             'remoteTests':  True,
                             'remoteExtras': { 'options': [ '--sampleConfig', 'remote.config',
                                                            '--output', 'local.yml',
                                                            '--webServer', 'bm-remote.build.mozilla.org',
                                                            '--browserWait', '60',
                                                          ],
                                               'exePath': 'org.mozilla.fennec',
                                             },
                           }

SUITES = {
    'chrome': GRAPH_CONFIG + ['--activeTests', 'ts:tdhtml:twinopen:tsspider'],
    'nochrome': GRAPH_CONFIG + ['--activeTests', 'tdhtml:twinopen:tsspider', '--noChrome'],
    'dirty': GRAPH_CONFIG + ['--activeTests', 'ts_places_generated_min:ts_places_generated_med:ts_places_generated_max'],
    'tp4': GRAPH_CONFIG + ['--activeTests', 'tp4'],
    'cold': GRAPH_CONFIG + ['--activeTests', 'ts_cold:ts_cold_generated_min:ts_cold_generated_med:ts_cold_generated_max'],
    'v8': GRAPH_CONFIG + ['--activeTests', 'v8'],
    'svg': GRAPH_CONFIG + ['--activeTests', 'tsvg:tsvg_opacity'],
    'scroll': GRAPH_CONFIG + ['--activeTests', 'tscroll'],
    'dromaeo': GRAPH_CONFIG + ['--activeTests', 'dromaeo_basics:dromaeo_v8:dromaeo_sunspider:dromaeo_jslib:dromaeo_css:dromaeo_dom'],
    'addon': ['--activeTests', 'ts:tp4'],
    'a11y': GRAPH_CONFIG + ['--activeTests', 'a11y'],
    'remote-ts': GRAPH_CONFIG + ['--activeTests', 'ts', '--noChrome'],
    'remote-tdhtml': GRAPH_CONFIG + ['--activeTests', 'tdhtml', '--noChrome'],
    'remote-tsvg': GRAPH_CONFIG + ['--activeTests', 'tsvg', '--noChrome'],
    'remote-tsspider': GRAPH_CONFIG + ['--activeTests', 'tsspider', '--noChrome'],
    'remote-tpan': GRAPH_CONFIG + ['--activeTests', 'tpan', '--noChrome'],
}

BRANCHES = {
    'mozilla-central': {},
    'shadow-central': {},
    'mozilla-2.0': {},
    'mozilla-1.9.2': {},
    'mozilla-1.9.1': {},
    'tracemonkey': {},
    'places': {},
    'electrolysis': {},
    'tryserver': {},
    'maple': {},
    'cedar': {},
    'birch': {},
    'jaegermonkey': {},
    'addontester': {},
}

# Talos
PLATFORMS = {
    'macosx': {},
    'macosx64': {},
    'win32': {},
    'win64': {},
    'linux': {},
    'linux64' : {},
    'android': {},
}

# work around path length problem bug 599795
# leopard-o == leopard-old
PLATFORMS['macosx']['slave_platforms'] = ['leopard-o']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['leopard-o'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}

PLATFORMS['macosx64']['slave_platforms'] = ['leopard', 'snowleopard']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['leopard'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx64']['snowleopard'] = {'name': "Rev3 MacOSX Snow Leopard 10.6.2"}

PLATFORMS['win32']['slave_platforms'] = ['xp', 'win7']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "Rev3 WINNT 5.1"}
PLATFORMS['win32']['win7'] = {'name': "Rev3 WINNT 6.1"}

PLATFORMS['win64']['slave_platforms'] = ['w764']
PLATFORMS['win64']['env_name'] = 'win64-perf'
PLATFORMS['win64']['w764'] = {'name': "Rev3 WINNT 6.1 x64",
                              'download_symbols': False,
                             }

PLATFORMS['linux']['slave_platforms'] = ['fedora']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': "Rev3 Fedora 12"}

PLATFORMS['linux64']['slave_platforms'] = ['fedora64']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': "Rev3 Fedora 12x64"}

PLATFORMS['android']['slave_platforms'] = ['tegra_android']
PLATFORMS['android']['env_name'] = 'android-perf'
PLATFORMS['android']['is_mobile'] = True
PLATFORMS['android']['tegra_android'] = {'name': "Android Tegra 250",
                                         'download_symbols': False,
                                        }


# Copy the slave names into PLATFORMS[platform][slave_platform], trimming off
# the -o suffix if necessary
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = SLAVES[slave_platform.split('-')[0]]

MOBILE_PLATFORMS = PLATFORMS['android']['slave_platforms']

ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['linux64']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['win64']['slave_platforms'] + \
                PLATFORMS['macosx64']['slave_platforms']

NO_WIN = PLATFORMS['macosx64']['slave_platforms'] + PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms']

NO_MAC = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms'] + PLATFORMS['win32']['slave_platforms'] + PLATFORMS['win64']['slave_platforms']

ANDROID = PLATFORMS['android']['slave_platforms']

# these three are for mozilla-1.9.1 and mozilla-1.9.2
OLD_BRANCH_ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['macosx']['slave_platforms']

OLD_BRANCH_NO_WIN = PLATFORMS['macosx']['slave_platforms'] + PLATFORMS['linux']['slave_platforms']

OLD_BRANCH_NO_MAC = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['win32']['slave_platforms']

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'linux': {},
        'linux64': {},
        'macosx': {},
        'macosx64': {},
        'win32': {},
        'win64': {},
        'android': {},
    },
}

# Default set of unit tests
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
        ('mozmill-all', ['mozmill']),
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
        ('mozmill-all', ['mozmill']),
    ],
    'mobile_unittest_suites': [
        # The disabled test suites are only disabled until we can get
        # to 100% green
        #('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        #('mochitest-other', ['mochitest-chrome', 'mochitest-a11y',
        #                     'mochitest-ipcplugins']),
        ('mobile-mochitest-browser-chrome', ['mobile-mochitest-browser-chrome']),
        #('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        #('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
    ],

}

def removeSuite(suiteName, suiteList):
    '''It removes 'suite' from 'suiteList' and returns it.

    Keyword arguments:
    suiteName -- it is the name of the suite that we want to remove
    suiteList -- it is the list of suites from where we want to remove
                 suiteList is a list of tuples. The tuples is formed
                 of a string and a list of suites.
    '''
    # Let's iterate over each tuple
    for i, info in enumerate(suiteList):
        name, suites = info
        # Let's see if suiteName is on this list of suites
        if suiteName in suites:
            suites = suites[:]
            suites.remove(suiteName)
            suiteList[i] = (name, suites)
    return suiteList

# You must define opt_unittest_suites when enable_opt_unittests is True for a 
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
        'linux': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'fedora': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
                'mobile_unittest_suites' : UNITTEST_SUITES['mobile_unittest_suites'][:],
            },
        },
        'linux64': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'fedora64': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            },
        },
        'win32': {
            'builds_before_reboot': 1,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'env_name' : 'win32-perf-unittest',
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'xp': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites': [],
            },
            'win7': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            }
        },
        'win64': {
            'builds_before_reboot': 1,
            'download_symbols': False,
            'enable_opt_unittests': True,
            # We can't yet run unit tests on debug builds - see bug 562459
            'enable_debug_unittests': False,
            'w764': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            },
        },
        'macosx': {
            'builds_before_reboot': 1,
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'leopard-o': {
                'opt_unittest_suites' : [],
                'debug_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
            },
        },
        'macosx64': {
            'builds_before_reboot': 1,
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'leopard': {
                'opt_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
                'debug_unittest_suites' : [],
            },
            'snowleopard': {
                'opt_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
                'debug_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
            },
        },
        'android': {
            'builds_before_reboot':  1,
            'enable_opt_unittests': False,
            'enable_debug_unittests': False,
            'download_symbols': False,
            'tegra_android': {
                'opt_unittest_suites': [],
                'debug_unittest_suites': [],
            },
        },
}

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

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

    # Copy in local config
    if branch in localconfig.BRANCHES:
        for key, value in localconfig.BRANCHES[branch].items():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.items():
                    for key, value in platform_config.items():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

########
# Entries in BRANCHES for tests should be a tuple of:
# - Number of tests to run per build
# - Whether queue merging is on
# - TalosFactory options
# - Which platforms to run on

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['mobile_branch_name'] = "Mobile"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-central']['fetch_symbols'] = True
BRANCHES['mozilla-central']['fetch_release_symbols'] = False
BRANCHES['mozilla-central']['release_tests'] = 5
BRANCHES['mozilla-central']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-central']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-central']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-central']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['mozilla-central']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-central']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-central']['remote-ts_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tdhtml_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tsvg_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tsspider_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tpan_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['platforms']['win32']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['enable_mobile_unittests'] = True
BRANCHES['mozilla-central']['platforms']['win64']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['android']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['fedora']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['linux64']['fedora64']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['linux64']['fedora64']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['macosx']['leopard-o']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['macosx64']['leopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['win32']['xp']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
# Disabling win7 until hung slave issue is fixed
#BRANCHES['mozilla-central']['platforms']['win32']['win7']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]

######## shadow-central
BRANCHES['shadow-central']['branch_name'] = "Shadow-Central"
BRANCHES['shadow-central']['mobile_branch_name'] = "Shadow-Central"
BRANCHES['shadow-central']['build_branch'] = "Shadow-Central"
BRANCHES['shadow-central']['talos_command'] = TALOS_CMD
BRANCHES['shadow-central']['fetch_symbols'] = True
BRANCHES['shadow-central']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['shadow-central']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['shadow-central']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['shadow-central']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['shadow-central']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['shadow-central']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['shadow-central']['repo_path'] = "shadow-central"

######## mozilla-2.0
BRANCHES['mozilla-2.0']['branch_name'] = "Firefox4.0"
BRANCHES['mozilla-2.0']['mobile_branch_name'] = "Mobile4.0"
BRANCHES['mozilla-2.0']['build_branch'] = "2.0"
BRANCHES['mozilla-2.0']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-2.0']['fetch_symbols'] = True
BRANCHES['mozilla-2.0']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-2.0']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['mozilla-2.0']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-2.0']['repo_path'] = "mozilla-2.0"

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['branch_name'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['mobile_branch_name'] = "Firefox3.5"
BRANCHES['mozilla-1.9.1']['build_branch'] = "1.9.1"
BRANCHES['mozilla-1.9.1']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.1']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.1']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-1.9.1']['chrome_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['nochrome_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['dromaeo_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['mozilla-1.9.1']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['svg_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['scroll_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['mozilla-1.9.1']['enable_unittests'] = False

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['branch_name'] = "Firefox3.6"
BRANCHES['mozilla-1.9.2']['mobile_branch_name'] = "Mobile1.1"
BRANCHES['mozilla-1.9.2']['build_branch'] = "1.9.2"
BRANCHES['mozilla-1.9.2']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-1.9.2']['fetch_symbols'] = True
BRANCHES['mozilla-1.9.2']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-1.9.2']['release_tests'] = 5
BRANCHES['mozilla-1.9.2']['fetch_release_symbols'] = False
BRANCHES['mozilla-1.9.2']['chrome_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['nochrome_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dromaeo_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['mozilla-1.9.2']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['svg_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['scroll_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['mozilla-1.9.2']['enable_unittests'] = False

######## addontester - tests against 1.9.2
BRANCHES['addontester']['branch_name'] = "Firefox3.6"
BRANCHES['addontester']['mobile_branch_name'] = "Firefox3.6"
BRANCHES['addontester']['build_branch'] = "1.9.2"
BRANCHES['addontester']['talos_command'] = TALOS_ADDON_CMD
BRANCHES['addontester']['fetch_symbols'] = False
BRANCHES['addontester']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['addontester']['fetch_release_symbols'] = False
BRANCHES['addontester']['chrome_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['nochrome_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['dromaeo_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['addontester']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['svg_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['scroll_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['addon_tests'] = (1, False, TALOS_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['addontester']['enable_unittests'] = False

######## tracemonkey
BRANCHES['tracemonkey']['branch_name'] = "TraceMonkey"
BRANCHES['tracemonkey']['mobile_branch_name'] = "TraceMonkey"
BRANCHES['tracemonkey']['build_branch'] = "TraceMonkey"
BRANCHES['tracemonkey']['talos_command'] = TALOS_CMD
BRANCHES['tracemonkey']['fetch_symbols'] = True
BRANCHES['tracemonkey']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['tracemonkey']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['tracemonkey']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['tracemonkey']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['tracemonkey']['remote-ts_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tracemonkey']['remote-tdhtml_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tracemonkey']['remote-tsvg_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tracemonkey']['remote-tsspider_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tracemonkey']['remote-tpan_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tracemonkey']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['v8_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['tracemonkey']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['tracemonkey']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['tracemonkey']['repo_path'] = "tracemonkey"

######## places
BRANCHES['places']['branch_name'] = "Places"
BRANCHES['places']['mobile_branch_name'] = "Places"
BRANCHES['places']['build_branch'] = "Places"
BRANCHES['places']['talos_command'] = TALOS_CMD
BRANCHES['places']['fetch_symbols'] = True
BRANCHES['places']['repo_path'] = "projects/places"
BRANCHES['places']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['places']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['places']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['places']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['places']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['places']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['places']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['places']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['places']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['places']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['places']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['places']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['places']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)

######## electrolysis
BRANCHES['electrolysis']['branch_name'] = "Electrolysis"
BRANCHES['electrolysis']['mobile_branch_name'] = "Electrolysis"
BRANCHES['electrolysis']['build_branch'] = "Electrolysis"
BRANCHES['electrolysis']['talos_command'] = TALOS_CMD
BRANCHES['electrolysis']['repo_path'] = "projects/electrolysis"
BRANCHES['electrolysis']['fetch_symbols'] = True
BRANCHES['electrolysis']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['electrolysis']['chrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['nochrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['dromaeo_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['electrolysis']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['electrolysis']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['electrolysis']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['electrolysis']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['electrolysis']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['electrolysis']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['electrolysis']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['electrolysis']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['scroll_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['electrolysis']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['electrolysis']['a11y_tests'] = (0, True, {}, NO_MAC)

######## maple
BRANCHES['maple']['branch_name'] = "Maple"
BRANCHES['maple']['mobile_branch_name'] = "Maple"
BRANCHES['maple']['build_branch'] = "Maple"
BRANCHES['maple']['repo_path'] = "projects/maple"
BRANCHES['maple']['talos_command'] = TALOS_CMD
BRANCHES['maple']['fetch_symbols'] = True
BRANCHES['maple']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['maple']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['maple']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['maple']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['maple']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['maple']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['maple']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['maple']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['maple']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['maple']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['maple']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['maple']['a11y_tests'] = (1, True, {}, NO_MAC)

######## cedar
BRANCHES['cedar']['branch_name'] = "Cedar"
BRANCHES['cedar']['mobile_branch_name'] = "Cedar"
BRANCHES['cedar']['build_branch'] = "Cedar"
BRANCHES['cedar']['repo_path'] = "projects/cedar"
BRANCHES['cedar']['talos_command'] = TALOS_CMD
BRANCHES['cedar']['fetch_symbols'] = True
BRANCHES['cedar']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['cedar']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['cedar']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['cedar']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['cedar']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['cedar']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['cedar']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['cedar']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['cedar']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['cedar']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['cedar']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['cedar']['a11y_tests'] = (1, True, {}, NO_MAC)

######## birch
BRANCHES['birch']['branch_name'] = "Birch"
BRANCHES['birch']['mobile_branch_name'] = "Birch"
BRANCHES['birch']['build_branch'] = "Birch"
BRANCHES['birch']['repo_path'] = "projects/birch"
BRANCHES['birch']['talos_command'] = TALOS_CMD
BRANCHES['birch']['fetch_symbols'] = True
BRANCHES['birch']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['birch']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['birch']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['birch']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['birch']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['birch']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['birch']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['birch']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['birch']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['birch']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['birch']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['birch']['a11y_tests'] = (1, True, {}, NO_MAC)

######## jaegermonkey
BRANCHES['jaegermonkey']['branch_name'] = "Jaegermonkey"
BRANCHES['jaegermonkey']['mobile_branch_name'] = "Jaegermonkey"
BRANCHES['jaegermonkey']['build_branch'] = "Jaegermonkey"
BRANCHES['jaegermonkey']['repo_path'] = "projects/jaegermonkey"
BRANCHES['jaegermonkey']['talos_command'] = TALOS_CMD
BRANCHES['jaegermonkey']['fetch_symbols'] = True
BRANCHES['jaegermonkey']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['jaegermonkey']['chrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['nochrome_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['dromaeo_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['jaegermonkey']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['jaegermonkey']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['jaegermonkey']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['jaegermonkey']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['jaegermonkey']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['jaegermonkey']['svg_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['scroll_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['jaegermonkey']['a11y_tests'] = (0, True, {}, NO_MAC)

######## tryserver
BRANCHES['tryserver']['branch_name'] = "Tryserver"
BRANCHES['tryserver']['mobile_branch_name'] = "Tryserver"
BRANCHES['tryserver']['build_branch'] = "Tryserver"
BRANCHES['tryserver']['talos_command'] = TALOS_CMD
BRANCHES['tryserver']['fetch_symbols'] = True
BRANCHES['tryserver']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['tryserver']['chrome_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['nochrome_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['dromaeo_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['dirty_tests'] = (1, False, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['tryserver']['tp4_tests'] = (1, False, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['tryserver']['cold_tests'] = (0, False, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['tryserver']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tryserver']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tryserver']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tryserver']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tryserver']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['tryserver']['svg_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['v8_tests'] = (0, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['scroll_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['tryserver']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['tryserver']['a11y_tests'] = (1, False, {}, NO_MAC)
BRANCHES['tryserver']['repo_path'] = "try"
BRANCHES['tryserver']['platforms']['win32']['win7']['opt_unittest_suites'] += [('reftest-no-accel', ['reftest-no-d2d-d3d'])]
BRANCHES['tryserver']['platforms']['linux']['fedora']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['tryserver']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['tryserver']['platforms']['linux64']['fedora64']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['tryserver']['platforms']['linux64']['fedora64']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['tryserver']['platforms']['macosx']['leopard-o']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['tryserver']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['tryserver']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['tryserver']['platforms']['macosx64']['leopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['tryserver']['platforms']['win32']['xp']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
# Disabling win7 until hung slave issue is fixed
#BRANCHES['tryserver']['platforms']['win32']['win7']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]

if __name__ == "__main__":
    import sys, pprint, re

    class BBPrettyPrinter(pprint.PrettyPrinter):
        def format(self, object, context, maxlevels, level):
            if isinstance(object, WithProperties):
                return pprint.PrettyPrinter.format(self, object.fmtstring, context, maxlevels, level)
            return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)

    args = sys.argv[1:]

    if len(args) > 0:
        branches = args
    else:
        branches = BRANCHES.keys()

    pp = BBPrettyPrinter()
    for branch in branches:
        print branch
        pp.pprint(BRANCHES[branch])

    for suite in SUITES:
        print suite
        pp.pprint(SUITES[suite])
