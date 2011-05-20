from copy import deepcopy

from buildbot.steps.shell import WithProperties

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, GLOBAL_VARS, GRAPH_CONFIG

REMOTE_PROCESS_NAMES = { 'default':         'org.mozilla.fennec',
                         'mozilla-beta':    'org.mozilla.firefox_beta',
                         'mozilla-aurora':  'org.mozilla.fennec_aurora',
                         'mozilla-release': 'org.mozilla.firefox',
                       }

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_ADDON_CMD = ['python', 'run_tests.py', '--noisy', '--amo', WithProperties('%(configFile)s')]

TALOS_DIRTY_OPTS = {'talosAddOns': ['profiles/dirtyDBs.zip', 'profiles/dirtyMaxDBs.zip']}

TALOS_TP4_OPTS = {'plugins': 'zips/plugins.zip', 'pageset': 'zips/pagesets.zip'}

TALOS_ADDON_OPTS = {'addonTester' : True, 'releaseTester' : True, 'plugins': 'zips/plugins.zip', 'pageset': 'zips/pagesets.zip'}
TALOS_BASELINE_ADDON_OPTS = {'releaseTester' : True, 'plugins': 'zips/plugins.zip', 'pageset': 'zips/pagesets.zip'}

TALOS_REMOTE_FENNEC_OPTS = { 'productName':  'fennec',
                             'remoteTests':  True,
                             'remoteExtras': { 'options': [ '--sampleConfig', 'remote.config',
                                                            '--output', 'local.yml',
                                                            '--webServer', 'bm-remote.build.mozilla.org',
                                                            '--browserWait', '60',
                                                          ],
                                               'processName': REMOTE_PROCESS_NAMES,
                                             },
                           }

UNITTEST_REMOTE_EXTRAS = { 'processName': REMOTE_PROCESS_NAMES,
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
    'addon': GRAPH_CONFIG + ['--activeTests', 'ts', '--noShutdown', '--sampleConfig', 'addon.config'],
    'addon-baseline': GRAPH_CONFIG + ['--activeTests', 'ts', '--noShutdown', '--sampleConfig', 'addon.config'],
    'a11y': GRAPH_CONFIG + ['--activeTests', 'a11y'],
    'paint': GRAPH_CONFIG + ['--activeTests', 'ts_paint:tpaint', '--setPref', 'dom.send_after_paint_to_content=true'],
    'remote-ts': GRAPH_CONFIG + ['--activeTests', 'ts', '--noChrome'],
    'remote-tdhtml': GRAPH_CONFIG + ['--activeTests', 'tdhtml', '--noChrome'],
    'remote-tsvg': GRAPH_CONFIG + ['--activeTests', 'tsvg', '--noChrome'],
    'remote-tsspider': GRAPH_CONFIG + ['--activeTests', 'tsspider', '--noChrome'],
    'remote-tpan': GRAPH_CONFIG + ['--activeTests', 'tpan', '--noChrome'],
    'remote-tp4m': GRAPH_CONFIG + ['--activeTests', 'tp4m'],
    'remote-tp4m_nochrome': GRAPH_CONFIG + ['--activeTests', 'tp4m', '--noChrome'],
    'remote-twinopen': GRAPH_CONFIG + ['--activeTests', 'twinopen'],
    'remote-tzoom': GRAPH_CONFIG + ['--activeTests', 'tzoom'],
}

BRANCHES = {
    'mozilla-central': {},
    'shadow-central': {},
    'mozilla-beta': {},
    'mozilla-aurora': {},
    'mozilla-2.0': {},
    'mozilla-2.1': {},
    'mozilla-1.9.2': {},
    'mozilla-1.9.1': {},
    'try': {},
    'addontester': {},
    'addonbaselinetester': {},
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
PLATFORMS['android']['branch_extra'] = 'mobile-browser'
PLATFORMS['android']['tegra_android'] = {'name': "Android Tegra 250",
                                         'download_symbols': False,
                                        }


# Copy the slave names into PLATFORMS[platform][slave_platform], trimming off
# the -o suffix if necessary
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform.split('-')[0]])

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
        # Disabled in bug 630551
        #('mozmill-all', ['mozmill']),
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
        # Disabled in bug 630551
        #('mozmill-all', ['mozmill']),
    ],
    'mobile_unittest_suites': [
        # The disabled test suites are only disabled until we can get
        # to 100% green
        #('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        #('mochitest-other', ['mochitest-chrome', 'mochitest-a11y',
        #                     'mochitest-ipcplugins']),
        ('mobile-mochitest-browser-chrome', ['mobile-mochitest-browser-chrome']),
        #('reftest', ['reftest']),
        #('crashtest', ['crashtest']),
        #('xpcshell', ['xpcshell']),
        #('jsreftest', ['jsreftest']),
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

PLATFORM_UNITTEST_JSREFTEST = [ ('jsreftest-1', (
                                  {'suite': 'jsreftest',
                                            'totalChunks': 2,
                                            'thisChunk': 1,
                                  },
                                 )),
                                ('jsreftest-2', (
                                  {'suite': 'jsreftest',
                                            'totalChunks': 2,
                                            'thisChunk': 2,
                                  },
                                 )),
                              ]

# You must define opt_unittest_suites when enable_opt_unittests is True for a 
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
        'linux': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'fedora': {
                'opt_unittest_suites' : \
                    UNITTEST_SUITES['opt_unittest_suites'][:] + \
                    [('reftest-ipc', ['reftest-ipc'])] + \
                    [('crashtest-ipc', ['crashtest-ipc'])],
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
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
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
            'is_remote': True,
            'branch_extra': 'mobile-browser',
            'host_utils_url': 'http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.zip',
            'remote_extras': UNITTEST_REMOTE_EXTRAS,
            'tegra_android': {
                'opt_unittest_suites': [
                    ('mochitest-1', (
                        {'suite': 'mochitest-plain',
                         'testPaths': [
                             'content/smil/test', 'content/xml/document/test',
                             'content/xul/document/test', 'content/xul/templates/tests',
                             'content/xslt/tests/mochitest'
                         ]
                        },
                    )),
                    ('mochitest-2', (
                        {'suite': 'mochitest-plain',
                         'testPaths': [
                             'dom/src/json/test', 'dom/src/jsurl/test',
                             'dom/tests/mochitest/dom-level0', 'js/jsd/test',
                             'js/src/xpconnect/tests/mochitest'
                         ]
                        },
                    )),
                    ('mochitest-3', (
                        {'suite': 'mochitest-plain',
                         'testPaths': ['dom/tests/mochitest/dom-level1-core']
                        },
                    )),
                    ('mochitest-4', (
                        {'suite': 'mochitest-plain',
                         'testPaths': ['dom/tests/mochitest/dom-level2-core']
                        },
                    )),
                    ('browser-chrome', (
                        {'suite': 'mochitest-browser-chrome',
                         'testPaths': ['mobile']
                        },
                    )),
                    ('reftest-1', (
                        {'suite': 'reftest',
                         'totalChunks': 2,
                         'thisChunk': 1,
                        },
                    )),
                    ('reftest-2', (
                        {'suite': 'reftest',
                         'totalChunks': 2,
                         'thisChunk': 2,
                        },
                    )),
                    ('crashtest', (
                        {'suite': 'crashtest'},
                    )),
                ]
            },
        },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for key, value in BRANCH_UNITTEST_VARS.items():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
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
 
    # Merge in any project branch config for platforms
    if branch in ACTIVE_PROJECT_BRANCHES and PROJECT_BRANCHES[branch].has_key('platforms'):
        for platform, platform_config in PROJECT_BRANCHES[branch]['platforms'].items():
            if platform in PLATFORMS:
                for key, value in platform_config.items():
                    value = deepcopy(value)
                    if isinstance(value, str):
                        value = value % locals()
                    BRANCHES[branch]['platforms'][platform][key] = value

    for platform, platform_config in localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

### PROJECTS ###
PROJECTS = {
    'jetpack': {
        'platforms': {
            'w764': {'ext':'win64-x86_64.zip',}, 
            'fedora64': {'ext':'linux-x86_64.tar.bz2',}, 
            'fedora':{'ext':'linux-i686.tar.bz2'}, 
            'leopard':{'ext':'.mac.dmg'}, 
            'snowleopard':{'ext':'.mac.dmg'},   
            'xp':{
                'ext':'win32.zip',
                'env':PLATFORM_UNITTEST_VARS['win32']['env_name'],
                }, 
            'win7':{
                'ext':'win32.zip',
                'env':PLATFORM_UNITTEST_VARS['win32']['env_name'],
                }, 

            },
        'hgurl': 'http://hg.mozilla.org',
        'repo_path': 'projects/addon-sdk',
        'jetpack_tarball': 'archive/tip.tar.bz2',
        'ftp_url': 'ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/',
    },
}
for k, v in localconfig.PROJECTS.items():
    if k not in PROJECTS:
        PROJECTS[k] = {}
    for k1, v1 in v.items():
        PROJECTS[k][k1] = v1

########
# Entries in BRANCHES for tests should be a tuple of:
# - Number of tests to run per build
# - Whether queue merging is on
# - TalosFactory options
# - Which platforms to run on

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['mobile_branch_name'] = "Mobile"
BRANCHES['mozilla-central']['mobile_talos_branch'] = "mobile"
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
BRANCHES['mozilla-central']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-central']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-central']['paint_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-central']['remote-ts_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tdhtml_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tsvg_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tsspider_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tpan_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tp4m_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tp4m_nochrome_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-twinopen_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['remote-tzoom_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['platforms']['win32']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['enable_mobile_unittests'] = True
BRANCHES['mozilla-central']['platforms']['win64']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['android']['enable_opt_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('reftest-no-accel', ['opengl-no-accel'])]
BRANCHES['mozilla-central']['platforms']['linux']['fedora']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['linux64']['fedora64']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['linux64']['fedora64']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['macosx']['leopard-o']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['macosx64']['leopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['win32']['xp']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['win32']['xp']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['win32']['win7']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['win32']['win7']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-central']['platforms']['android']['tegra_android']['opt_unittest_suites'] += PLATFORM_UNITTEST_JSREFTEST

######## mozilla-beta
BRANCHES['mozilla-beta']['branch_name'] = "Mozilla-Beta"
BRANCHES['mozilla-beta']['mobile_branch_name'] = "Mozilla-Beta"
BRANCHES['mozilla-beta']['build_branch'] = "Mozilla-Beta"
BRANCHES['mozilla-beta']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-beta']['fetch_symbols'] = True
BRANCHES['mozilla-beta']['fetch_release_symbols'] = False
BRANCHES['mozilla-beta']['release_tests'] = 5
BRANCHES['mozilla-beta']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-beta']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['mozilla-beta']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-beta']['paint_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['remote-ts_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['remote-tdhtml_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['remote-tsvg_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['remote-tsspider_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['remote-tpan_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['remote-tp4m_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['remote-tp4m_nochrome_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['remote-twinopen_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['remote-tzoom_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-beta']['repo_path'] = "releases/mozilla-beta"
BRANCHES['mozilla-beta']['platforms']['win32']['enable_opt_unittests'] = True
BRANCHES['mozilla-beta']['platforms']['linux']['enable_mobile_unittests'] = True
BRANCHES['mozilla-beta']['platforms']['win64']['enable_opt_unittests'] = True
BRANCHES['mozilla-beta']['platforms']['android']['enable_opt_unittests'] = True

######## mozilla-aurora
BRANCHES['mozilla-aurora']['branch_name'] = "Mozilla-Aurora"
BRANCHES['mozilla-aurora']['mobile_branch_name'] = "Mozilla-Aurora"
BRANCHES['mozilla-aurora']['build_branch'] = "Mozilla-Aurora"
BRANCHES['mozilla-aurora']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-aurora']['fetch_symbols'] = True
BRANCHES['mozilla-aurora']['fetch_release_symbols'] = False
BRANCHES['mozilla-aurora']['release_tests'] = 5
BRANCHES['mozilla-aurora']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-aurora']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['mozilla-aurora']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-aurora']['paint_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-aurora']['remote-ts_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['remote-tdhtml_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['remote-tsvg_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['remote-tsspider_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['remote-tpan_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['remote-tp4m_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['remote-tp4m_nochrome_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['remote-twinopen_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['remote-tzoom_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-aurora']['repo_path'] = "releases/mozilla-aurora"
BRANCHES['mozilla-aurora']['platforms']['win32']['enable_opt_unittests'] = True
BRANCHES['mozilla-aurora']['platforms']['linux']['enable_mobile_unittests'] = True
BRANCHES['mozilla-aurora']['platforms']['win64']['enable_opt_unittests'] = True
BRANCHES['mozilla-aurora']['platforms']['android']['enable_opt_unittests'] = True
BRANCHES['mozilla-aurora']['platforms']['linux']['fedora']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['linux64']['fedora64']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['linux64']['fedora64']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['macosx']['leopard-o']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['macosx64']['leopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['win32']['xp']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['win32']['xp']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['win32']['win7']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['mozilla-aurora']['platforms']['win32']['win7']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]

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
BRANCHES['shadow-central']['remote-tp4m_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['remote-tp4m_nochrome_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['remote-twinopen_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['remote-tzoom_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['shadow-central']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['shadow-central']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['shadow-central']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['shadow-central']['paint_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['shadow-central']['repo_path'] = "shadow-central"

######## mozilla-2.0
BRANCHES['mozilla-2.0']['branch_name'] = "Firefox4.0"
BRANCHES['mozilla-2.0']['mobile_branch_name'] = "Firefox4.0"
BRANCHES['mozilla-2.0']['build_branch'] = "2.0"
BRANCHES['mozilla-2.0']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-2.0']['fetch_symbols'] = True
BRANCHES['mozilla-2.0']['release_tests'] = 5
BRANCHES['mozilla-2.0']['fetch_release_symbols'] = False
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
BRANCHES['mozilla-2.0']['remote-tp4m_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['remote-tp4m_nochrome_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['remote-twinopen_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['remote-tzoom_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.0']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-2.0']['paint_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.0']['repo_path'] = "mozilla-2.0"

######## mozilla-2.1
BRANCHES['mozilla-2.1']['branch_name'] = "Mobile2.0"
BRANCHES['mozilla-2.1']['mobile_branch_name'] = "Mobile2.0"
BRANCHES['mozilla-2.1']['mobile_talos_branch'] = "mobile-2.0"
BRANCHES['mozilla-2.1']['build_branch'] = "2.1"
BRANCHES['mozilla-2.1']['talos_command'] = TALOS_CMD
BRANCHES['mozilla-2.1']['fetch_symbols'] = True
BRANCHES['mozilla-2.1']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['mozilla-2.1']['chrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['dromaeo_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['dirty_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['mozilla-2.1']['remote-ts_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['remote-tdhtml_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['remote-tsvg_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['remote-tsspider_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['remote-tpan_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['remote-tp4m_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['remote-tp4m_nochrome_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['remote-twinopen_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['remote-tzoom_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-2.1']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['v8_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['scroll_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['a11y_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-2.1']['paint_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-2.1']['repo_path'] = "mozilla-2.1"

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
BRANCHES['mozilla-1.9.1']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['mozilla-1.9.1']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tp4m_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tp4m_nochrome_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-twinopen_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['remote-tzoom_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.1']['svg_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['scroll_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.1']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['mozilla-1.9.1']['paint_tests'] = (0, True, {}, ALL_PLATFORMS)
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
BRANCHES['mozilla-1.9.2']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['mozilla-1.9.2']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tp4m_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tp4m_nochrome_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-twinopen_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['remote-tzoom_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['mozilla-1.9.2']['svg_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['scroll_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['mozilla-1.9.2']['paint_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['enable_unittests'] = False

######## addontester 
BRANCHES['addontester']['branch_name'] = "AddonTester"
BRANCHES['addontester']['mobile_branch_name'] = "AddonTester"
BRANCHES['addontester']['build_branch'] = "N/A"
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
BRANCHES['addontester']['remote-tp4m_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tp4m_nochrome_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-twinopen_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tzoom_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['svg_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['scroll_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['addon_tests'] = (1, False, TALOS_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['addontester']['paint_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addontester']['enable_unittests'] = False
######## addonbaselinetester - tests against 1.9.2
BRANCHES['addonbaselinetester']['branch_name'] = "AddonTester"
BRANCHES['addonbaselinetester']['mobile_branch_name'] = "AddonTester"
BRANCHES['addonbaselinetester']['build_branch'] = "N/A"
BRANCHES['addonbaselinetester']['talos_command'] = TALOS_ADDON_CMD
BRANCHES['addonbaselinetester']['fetch_symbols'] = False
BRANCHES['addonbaselinetester']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['addonbaselinetester']['fetch_release_symbols'] = False
BRANCHES['addonbaselinetester']['chrome_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['nochrome_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['dromaeo_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['addonbaselinetester']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tp4m_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tp4m_nochrome_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-twinopen_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tzoom_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['svg_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['scroll_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['addon-baseline_tests'] = (1, False, TALOS_BASELINE_ADDON_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['addonbaselinetester']['paint_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['enable_unittests'] = False

######## try
BRANCHES['try']['branch_name'] = "Try"
BRANCHES['try']['mobile_branch_name'] = "Try"
BRANCHES['try']['build_branch'] = "Try"
BRANCHES['try']['talos_command'] = TALOS_CMD
BRANCHES['try']['fetch_symbols'] = True
BRANCHES['try']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['try']['chrome_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['nochrome_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['dromaeo_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['dirty_tests'] = (1, False, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['try']['tp4_tests'] = (1, False, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['try']['cold_tests'] = (0, False, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['try']['remote-ts_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tdhtml_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tsvg_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tsspider_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tpan_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tp4m_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tp4m_nochrome_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-twinopen_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tzoom_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['svg_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['v8_tests'] = (0, False, {}, ALL_PLATFORMS)
BRANCHES['try']['scroll_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['try']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['try']['a11y_tests'] = (1, False, {}, NO_MAC)
BRANCHES['try']['paint_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['try']['repo_path'] = "try"
BRANCHES['try']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('reftest-no-accel', ['opengl-no-accel'])]
BRANCHES['try']['platforms']['win32']['win7']['opt_unittest_suites'] += [('reftest-no-accel', ['reftest-no-d2d-d3d'])]
BRANCHES['try']['platforms']['linux']['fedora']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['linux64']['fedora64']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['linux64']['fedora64']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['macosx']['leopard-o']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['macosx64']['leopard']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['win32']['xp']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['win32']['xp']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['win32']['win7']['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['win32']['win7']['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
BRANCHES['try']['platforms']['android']['enable_opt_unittests'] = True

######## generic branch variables for project branches
for branch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[branch]
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch) 
    BRANCHES[branch]['branch_name'] = branchConfig.get('branch_name', branch.title())
    BRANCHES[branch]['mobile_branch_name'] = branchConfig.get('mobile_branch_name', branch.title())
    BRANCHES[branch]['build_branch'] = branchConfig.get('build_branch', branch.title())
    BRANCHES[branch]['talos_command'] = branchConfig.get('talos_cmd', TALOS_CMD)
    BRANCHES[branch]['fetch_symbols'] = branchConfig.get('fetch_symbols', True)
    BRANCHES[branch]['support_url_base'] = branchConfig.get('support_url_base', 'http://build.mozilla.org/talos')
    BRANCHES[branch]['enable_unittests'] = branchConfig.get('enable_unittests', True)
    # Check if Talos is enabled, if False, set 0 runs for all suites
    if branchConfig.get('enable_talos') == False:
        branchConfig['talos_suites'] = {}
        for suite in SUITES.keys():
            branchConfig['talos_suites'][suite]  = 0
    # Want to turn on/off a talos suite? Set it in the PROJECT_BRANCHES[branch]['talos_suites'] otherwise, defaults below
    if branchConfig.get('talos_suites'):
        talosConfig = branchConfig['talos_suites']
    else:
        talosConfig = {}
    for suite in SUITES.keys():
        if suite.startswith('remote-'):
            BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 0), True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
        else:
            # 0 runs by default
            if suite in ('v8', 'addon', 'addon-baseline', 'cold'):
                if suite == 'cold':
                    BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 0), True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
                elif suite == 'addon':
                    BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 0), False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
                elif suite == 'addon-baseline':
                     BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 0), False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
                else:
                    BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 0), True, {}, ALL_PLATFORMS)
            else:
                # default is 1 run
                if suite == 'dirty':
                    BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 1), True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
                elif suite == 'tp4':
                    BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 1), True, TALOS_TP4_OPTS, ALL_PLATFORMS)
                elif suite == 'a11y':
                    BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 1), True, {}, NO_MAC)
                else:
                    BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 1), True, {}, ALL_PLATFORMS)

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
