from copy import deepcopy

from buildbot.steps.shell import WithProperties

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS, GRAPH_CONFIG

REMOTE_PROCESS_NAMES = { 'default':         'org.mozilla.fennec',
                         'mozilla-beta':    'org.mozilla.firefox_beta',
                         'mozilla-aurora':  'org.mozilla.fennec_aurora',
                         'mozilla-release': 'org.mozilla.firefox',
                         'mozilla-esr10':   'org.mozilla.firefox',
                       }

MOZHARNESS_REPO = "http://hg.mozilla.org/build/mozharness"

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_ADDON_CMD = ['python', 'run_tests.py', '--noisy', '--amo', WithProperties('%(configFile)s')]

TALOS_DIRTY_OPTS = {'talosAddOns': ['profiles/dirtyDBs.zip', 'profiles/dirtyMaxDBs.zip']}

TALOS_TP_OPTS = {'plugins': {'32':'zips/flash32_10_3_183_5.zip', '64': 'zips/flash64_11_0_d1_98.zip'}, 'pagesets': ['zips/tp5.zip']}
TALOS_TP_NEW_OPTS = {'plugins': {'32':'zips/flash32_10_3_183_5.zip', '64': 'zips/flash64_11_0_d1_98.zip'}, 'pagesets': ['zips/tp5n.zip']}
TALOS_TP4_OPTS = {'plugins': {'32':'zips/flash32_10_3_183_5.zip', '64': 'zips/flash64_11_0_d1_98.zip'}, 'pagesets': ['zips/tp4.zip']}

TALOS_BASELINE_ADDON_OPTS = {'releaseTester' : True}

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
ANDROID_UNITTEST_REMOTE_EXTRAS = deepcopy(UNITTEST_REMOTE_EXTRAS)
ANDROID_UNITTEST_REMOTE_EXTRAS['cmdOptions'] = ['--bootstrap']

BRANCHES = {
    'mozilla-central':     {},
    'mozilla-release':     { 'release_branch': True },
    'mozilla-beta':        { 'release_branch': True },
    'mozilla-aurora':      {},
    'mozilla-esr10':       { 'release_branch': True },
    'try':                 { 'coallesce_jobs': False},
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
    'android-xul': {},
    'linux-android': {},
}

# work around path length problem bug 599795
# leopard-o == leopard-old
PLATFORMS['macosx']['slave_platforms'] = ['leopard-o']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['leopard-o'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx']['stage_product'] = 'firefox'
PLATFORMS['macosx']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['macosx64']['slave_platforms'] = ['leopard', 'snowleopard',
                                            'lion']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['leopard'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx64']['snowleopard'] = {'name': "Rev4 MacOSX Snow Leopard 10.6"}
PLATFORMS['macosx64']['lion'] = {'name': "Rev4 MacOSX Lion 10.7"}
PLATFORMS['macosx64']['stage_product'] = 'firefox'
PLATFORMS['macosx64']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['win32']['slave_platforms'] = ['xp', 'win7']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "Rev3 WINNT 5.1"}
PLATFORMS['win32']['win7'] = {'name': "Rev3 WINNT 6.1"}
PLATFORMS['win32']['stage_product'] = 'firefox'
PLATFORMS['win32']['mozharness_python'] = ['c:/mozilla-build/python25/python', '-u']

PLATFORMS['win64']['slave_platforms'] = ['w764']
PLATFORMS['win64']['env_name'] = 'win64-perf'
PLATFORMS['win64']['w764'] = {'name': "Rev3 WINNT 6.1 x64",
                              'download_symbols': False,
                             }
PLATFORMS['win64']['stage_product'] = 'firefox'
PLATFORMS['win64']['mozharness_python'] = ['c:/mozilla-build/python25/python', '-u']

PLATFORMS['linux']['slave_platforms'] = ['fedora']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': "Rev3 Fedora 12"}
PLATFORMS['linux']['stage_product'] = 'firefox'
PLATFORMS['linux']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['linux64']['slave_platforms'] = ['fedora64']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': "Rev3 Fedora 12x64"}
PLATFORMS['linux64']['stage_product'] = 'firefox'
PLATFORMS['linux64']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['linux-android']['slave_platforms'] = ['tegra_android-o']
PLATFORMS['linux-android']['env_name'] = 'android-perf'
PLATFORMS['linux-android']['is_mobile'] = True
PLATFORMS['linux-android']['tegra_android-o'] = {'name': "Android Tegra 250"}
PLATFORMS['linux-android']['stage_platform'] = 'android'
PLATFORMS['linux-android']['stage_product'] = 'mobile'
PLATFORMS['linux-android']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['android']['slave_platforms'] = ['tegra_android']
PLATFORMS['android']['env_name'] = 'android-perf'
PLATFORMS['android']['is_mobile'] = True
PLATFORMS['android']['tegra_android'] = {'name': "Android Tegra 250"}
PLATFORMS['android']['stage_product'] = 'mobile'
PLATFORMS['android']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['android-xul']['slave_platforms'] = ['tegra_android-xul']
PLATFORMS['android-xul']['env_name'] = 'android-perf'
PLATFORMS['android-xul']['is_mobile'] = True
PLATFORMS['android-xul']['tegra_android-xul'] = {'name': "Android XUL Tegra 250"}
PLATFORMS['android-xul']['stage_product'] = 'mobile'
PLATFORMS['android-xul']['mozharness_python'] = '/tools/buildbot/bin/python'

# Lets be explicit instead of magical.  leopard-o should be a second
# entry in the SLAVE dict
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform])
        if slave_platform in TRY_SLAVES:
            platform_config[slave_platform]['try_slaves'] = sorted(TRY_SLAVES[slave_platform])
        else:
            platform_config[slave_platform]['try_slaves'] = platform_config[slave_platform]['slaves']

MOBILE_PLATFORMS = PLATFORMS['android']['slave_platforms'] + \
                   PLATFORMS['android-xul']['slave_platforms'] + \
                   PLATFORMS['linux-android']['slave_platforms']

ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['linux64']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['macosx64']['slave_platforms']

WIN7_ONLY = ['win7']

NO_WIN = PLATFORMS['macosx64']['slave_platforms'] + PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms']

NO_MAC = PLATFORMS['linux']['slave_platforms'] + \
         PLATFORMS['linux64']['slave_platforms'] + \
         PLATFORMS['win32']['slave_platforms']

MAC_ONLY = PLATFORMS['macosx64']['slave_platforms']

ANDROID = PLATFORMS['android']['slave_platforms'] + \
          PLATFORMS['linux-android']['slave_platforms']

ANDROID_NATIVE = PLATFORMS['android']['slave_platforms']

ANDROID_XUL = PLATFORMS['linux-android']['slave_platforms']

ADDON_TESTER_PLATFORMS = ['win7', 'fedora', 'snowleopard']

SUITES = {
    'chrome': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll:a11y:ts_paint:tpaint:tdhtml:tsspider', '--mozAfterPaint'],
        'options': ({}, NO_MAC),
    },
    # chrome_mac compared to chrome is that it does not contain a11y and only run on Mac
    'chrome_mac': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll:ts_paint:tpaint:tdhtml:tsspider', '--mozAfterPaint'],
        'options': ({}, MAC_ONLY),
    },
    'nochrome': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tdhtml:tsspider', '--noChrome', '--mozAfterPaint'],
        'options': ({}, ALL_PLATFORMS),
    },
    'dirty': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts_places_generated_med:ts_places_generated_max', '--setPref', 'hangmonitor.timeout=0'],
        'options': (TALOS_DIRTY_OPTS, ALL_PLATFORMS),
    },
    'tp': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5', '--mozAfterPaint'],
        'options': (TALOS_TP_OPTS, ALL_PLATFORMS),
    },
    'tp4': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp4'],
        'options': (TALOS_TP4_OPTS, ALL_PLATFORMS),
    },
    'cold': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts_cold:ts_cold_generated_min:ts_cold_generated_med:ts_cold_generated_max'],
        'options': (TALOS_DIRTY_OPTS, NO_WIN),
    },
    'v8': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'v8'],
        'options': ({}, ALL_PLATFORMS),
    },
    'svg': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvg:tsvg_opacity'],
        'options': ({}, ALL_PLATFORMS),
    },
    'dromaeo': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom'],
        'options': ({}, ALL_PLATFORMS),
    },
    # New set of test that report numbers differently (https://wiki.mozilla.org/Auto-tools/Projects/Signal_From_Noise)
    # tp5 -> tpr instead of tp5.2.  This is osx only and we will consider switching linux and windows ot this as well.
    # all these tests should be default on m-c/m-i/m-a and project branches.
    'tpr_responsiveness': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5r', '--mozAfterPaint', '--responsiveness', '--ignoreFirst', '--sampleConfig', 'sample.2.config'],
        'options': (TALOS_TP_OPTS, ALL_PLATFORMS),
    },
    'v8.2': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'v8.2', '--ignoreFirst', '--sampleConfig', 'sample.2.config'],
        'options': ({}, ALL_PLATFORMS),
    },
    'chrome.2': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll.2:a11y.2:ts_paint:tpaint:tdhtml.2:tsspider.2', '--mozAfterPaint', '--ignoreFirst', '--sampleConfig', 'sample.2.config'],
        'options': ({}, NO_MAC),
    },
    # chrome_mac compared to chrome is that it does not contain a11y and only run on Mac
    'chrome_mac.2': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll.2:ts_paint:tpaint:tdhtml.2:tsspider.2', '--mozAfterPaint', '--ignoreFirst', '--sampleConfig', 'sample.2.config'],
        'options': ({}, MAC_ONLY),
    },
    'nochrome.2': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tdhtml.2:tsspider.2', '--noChrome', '--mozAfterPaint', '--ignoreFirst', '--sampleConfig', 'sample.2.config'],
        'options': ({}, ALL_PLATFORMS),
    },
    'xperf': {
        'enable_by_default': False,
        'suites': ['--activeTests', 'ts_paint:tpaint', '--sampleConfig', 'xperf.config', '--setPref', 'dom.send_after_paint_to_content=true', '--xperf_path', '"c:/Program Files/Microsoft Windows Performance Toolkit/xperf.exe"'],
        'options': ({}, WIN7_ONLY),
    },
    'tprow': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5row', '--mozAfterPaint', '--responsiveness', '--filter', 'ignore_first:5', '--filter', 'median', '--sampleConfig', 'sample.2.config'],
        'options': (TALOS_TP_OPTS, ALL_PLATFORMS),
    },
    'tpn': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5n', '--mozAfterPaint', '--responsiveness', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_PLATFORMS),
    },
    'chromer': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tdhtmlr', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_PLATFORMS),
    },
    'nochromer': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tdhtmlr', '--noChrome', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_PLATFORMS),
    },
    'other': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscrollr:a11yr:ts_paint:tpaint', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_PLATFORMS),
    },
    'svgr': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvgr:tsvgr_opacity', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_PLATFORMS),
    },
    'dirtypaint': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tspaint_places_generated_med:tspaint_places_generated_max', '--setPref', 'hangmonitor.timeout=0', '--mozAfterPaint'],
        'options': (TALOS_DIRTY_OPTS, ALL_PLATFORMS),
    },
    #run in staging for a week to get a baseline of numbers, then merge in with the dromaeo suite
    'jstests': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'sunspider:kraken:v8_7', '--mozAfterPaint'],
        'options': ({}, ALL_PLATFORMS),
    },

    # Mobile specific talos tests
    'remote-ts': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts', '--mozAfterPaint', '--noChrome'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tdhtml': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tdhtml', '--noChrome'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tsvg': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvg', '--noChrome'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tsspider': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsspider', '--noChrome'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tpan': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tpan', '--noChrome'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_XUL),
    },
    'remote-trobopan': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'trobopan', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_NATIVE),
    },
    'remote-trobocheck': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tcheckerboard', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_NATIVE),
    },
    'remote-troboprovider': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tprovider', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_NATIVE),
    },
    'remote-trobocheck2': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tcheck2', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_NATIVE),
    },
    'remote-trobocheck3': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tcheck3', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_NATIVE),
    },
    'remote-tp4m': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp4m', '--rss'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_XUL),
    },
    'remote-tp4m_nochrome': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp4m', '--noChrome', '--rss'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-twinopen': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'twinopen'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_XUL),
    },
    'remote-tzoom': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tzoom'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID_XUL),
    },
}

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
        'android-xul': {},
        'linux-android': {},
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

def addSuite(suiteGroupName, newSuiteName, suiteList):
    # In UNITTEST_SUITES we have opt, debug and mobile unit tests keys.
    # Each one of these have a list of tuples of test suites.
    #     e.g. suiteGroup = ('reftest', ['reftest])
    newSuiteList = []
    added = False
    for tuple in suiteList:
        name, suites = tuple
        if suiteGroupName == name:
            suites.append(newSuiteName)
            added = True
        newSuiteList.append((name, suites))

    if not added:
        newSuiteList.append((name, suites))

    return newSuiteList

def loadDefaultValues(BRANCHES, branch, branchConfig):
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch) 
    BRANCHES[branch]['branch_name'] = branchConfig.get('branch_name', branch.title())
    BRANCHES[branch]['mobile_branch_name'] = branchConfig.get('mobile_branch_name', branch.title())
    BRANCHES[branch]['build_branch'] = branchConfig.get('build_branch', branch.title())
    BRANCHES[branch]['talos_command'] = branchConfig.get('talos_cmd', TALOS_CMD)
    BRANCHES[branch]['fetch_symbols'] = branchConfig.get('fetch_symbols', True)
    BRANCHES[branch]['talos_from_source_code'] = branchConfig.get('talos_from_source_code', True)
    BRANCHES[branch]['support_url_base'] = branchConfig.get('support_url_base', 'http://build.mozilla.org/talos')
    BRANCHES[branch]['enable_unittests'] = branchConfig.get('enable_unittests', True)
    BRANCHES[branch]['pgo_strategy'] = branchConfig.get('pgo_strategy', None)

def loadCustomTalosSuites(BRANCHES, SUITES, branch, branchConfig):
    coallesceJobs = branchConfig.get('coallesce_jobs', True)
    BRANCHES[branch]['suites'] = deepcopy(SUITES)
    # Check if Talos is enabled, if False, set 0 runs for all suites
    if branchConfig.get('enable_talos') == False:
        branchConfig['talos_suites'] = {}
        for suite in SUITES.keys():
            branchConfig['talos_suites'][suite]  = 0

    # Want to turn on/off a talos suite? Set it in the PROJECT_BRANCHES[branch]['talos_suites'] 
    # This is the default and will make all talosConfig.get(key,0) calls
    # to default to 0 a.k.a. disabled suite
    talosConfig = {}
    if branchConfig.get('talos_suites'):
        for suite, settings in branchConfig['talos_suites'].items():
            # Normally the setting is just 0 or 1 for talosConfig to enable/disable a test
            # If there's a list, value[0] is the enabling flag and [1] is a dict of customization
            if isinstance(settings, list):
                talosConfig[suite] = settings[0]
                # append anything new in 'suites' for a talos_suite
                for key, value in settings[1].items():
                    if suite in SUITES.keys():
                        BRANCHES[branch]['suites'][suite][key] += value
            else:
                talosConfig[suite] = settings

    for suite in SUITES.keys():
        if not SUITES[suite]['enable_by_default']:
            # Suites that are turned off by default
            BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 0), coallesceJobs) + SUITES[suite]['options']
        else:
            # Suites that are turned on by default
            BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 1), coallesceJobs) + SUITES[suite]['options']

def loadTalosSuites(BRANCHES, SUITES, branch):
    '''
    This is very similar to loadCustomTalosSuites and is to deal with branches that are not in project_branches.py
    but in config.py. Both functions could be unified later on when we do further refactoring.
    '''
    coallesceJobs = BRANCHES[branch].get('coallesce_jobs', True)
    for suite in SUITES.keys():
        if not SUITES[suite]['enable_by_default']:
            # Suites that are turned off by default
            BRANCHES[branch][suite + '_tests'] = (0, coallesceJobs) + SUITES[suite]['options']
        else:
            # Suites that are turned on by default
            BRANCHES[branch][suite + '_tests'] = (1, coallesceJobs) + SUITES[suite]['options']

def loadCustomUnittestSuites(BRANCHES, branch, branchConfig):
    # If you want a project branch to have a different set of unit tests you can
    # do the following:
    #  - add a key called "add_test_suites"
    #  - add a tuple for each test suite with the following format:
    #      ('OS_nick', 'platform', 'opt|debug', 'new or existing group', 'suite name')
    #      e.g. ('macosx64', 'snowleopard', 'debug', 'mochitest-other', 'a11y')
    #
    # Old way of adding suites but still the same format
    #    BRANCHES['mozilla-central']['platforms']['win32']['win7']['debug_unittest_suites'] \
    #        += [('jetpack', ['jetpack'])]
    #
    for suiteToAdd in branchConfig.get('add_test_suites', []):
        type = 'opt_unittest_suites' if suiteToAdd[2] == 'opt' else 'debug_unittest_suites'
        # 'debug_unittest_suites' or 'opt_unittest_suites' is a list of tuple
        # addSuite() modifies that list and returns a new one with the added suite
        BRANCHES[branch]['platforms'][suiteToAdd[0]][suiteToAdd[1]][type] = \
            addSuite( suiteGroupName=suiteToAdd[3], newSuiteName=suiteToAdd[4],
                      suiteList=BRANCHES[branch]['platforms'][suiteToAdd[0]][suiteToAdd[1]][type])

ANDROID_XUL_UNITTEST_DICT = {
    'opt_unittest_suites': [
        ('mochitest-1', (
            {'suite': 'mochitest-plain',
             'testPaths': [
                 'content/smil/test', 'content/xml/document/test',
                 'content/xslt/tests/mochitest'
             ]
            },
        )),
        ('mochitest-2', (
            {'suite': 'mochitest-plain',
             'testPaths': [
                 'dom/src/json/test', 'dom/src/jsurl/test',
                 'dom/tests/mochitest/dom-level0', 'js'
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
        ('mochitest-5', (
            {'suite': 'mochitest-plain',
             'testPaths': ['dom/tests/mochitest/ajax/mochikit',
                           'dom/tests/mochitest/ajax/scriptaculous',
                           'dom/tests/mochitest/ajax/jquery'],
            },
        )),
        ('mochitest-6', (
            {'suite': 'mochitest-plain',
             'testPaths': ['dom/tests/mochitest/dom-level2-html'],
            },
        )),
        ('mochitest-7', (
            {'suite': 'mochitest-plain',
             'testPaths': ['Harness_sanity',
                           'editor/composer/test',
                           'intl/uconv/tests',
                           'dom/tests/mochitest/orientation',
                           'dom/tests/mochitest/storageevent'],
            },
        )),
        ('mochitest-8', (
            {'suite': 'mochitest-plain',
             'testPaths': ['layout/xul/test',
                           'modules/libjar/test/mochitest',
                           'layout/inspector/tests',
                           'toolkit/xre/test',
                           'toolkit/components/microformats/tests',
                           'MochiKit-1.4.2/tests',
                           'parser/htmlparser/tests/mochitest'],
           },
        )),
# Disable browser-chrome for android-xul; bug 771421
#        ('browser-chrome', (
#            {'suite': 'mochitest-browser-chrome',
#             'testPaths': ['mobile']
#            },
#        )),
        ('reftest-1', (
            {'suite': 'reftest',
             'totalChunks': 3,
             'thisChunk': 1,
            },
        )),
        ('reftest-2', (
            {'suite': 'reftest',
             'totalChunks': 3,
             'thisChunk': 2,
            },
        )),
        ('reftest-3', (
            {'suite': 'reftest',
             'totalChunks': 3,
             'thisChunk': 3,
            },
        )),
        # disabled for constant timeouts, bug 728119
        # ('crashtest-1', (
        #     {'suite': 'crashtest',
        #      'totalChunks': 3,
        #      'thisChunk': 1,
        #     },
        # )),
        ('crashtest-2', (
            {'suite': 'crashtest',
             'totalChunks': 3,
             'thisChunk': 2,
            },
        )),
        ('crashtest-3', (
            {'suite': 'crashtest',
             'totalChunks': 3,
             'thisChunk': 3,
            },
        )),
        ('jsreftest-1', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 1,
            },
        )),
        ('jsreftest-2', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 2,
            },
        )),
        ('jsreftest-3', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 3,
            },
        )),
    ],
    'debug_unittest_suites': [],
}
ANDROID_UNITTEST_DICT = {
    'opt_unittest_suites': [
        ('mochitest-1', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 1,
            },
        )),
        ('mochitest-2', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 2,
            },
        )),
        ('mochitest-3', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 3,
            },
        )),
        ('mochitest-4', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 4,
            },
        )),
        ('mochitest-5', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 5,
            },
        )),
        ('mochitest-6', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 6,
            },
        )),
        ('mochitest-7', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 7,
            },
        )),
        ('mochitest-8', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 8,
           },
        )),
        ('reftest-1', (
            {'suite': 'reftest',
             'totalChunks': 3,
             'thisChunk': 1,
            },
        )),
        ('reftest-2', (
            {'suite': 'reftest',
             'totalChunks': 3,
             'thisChunk': 2,
            },
        )),
        ('reftest-3', (
            {'suite': 'reftest',
             'totalChunks': 3,
             'thisChunk': 3,
            },
        )),
        # disabled for constant timeouts, bug 728119
        # ('crashtest-1', (
        #     {'suite': 'crashtest',
        #      'totalChunks': 3,
        #      'thisChunk': 1,
        #     },
        # )),
        ('crashtest-2', (
            {'suite': 'crashtest',
             'totalChunks': 3,
             'thisChunk': 2,
            },
        )),
        ('crashtest-3', (
            {'suite': 'crashtest',
             'totalChunks': 3,
             'thisChunk': 3,
            },
        )),
        ('jsreftest-1', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 1,
            },
        )),
        ('jsreftest-2', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 2,
            },
        )),
        ('jsreftest-3', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 3,
            },
        )),
        ('robocop', (
            {'suite': 'mochitest-robocop',
            },
        )),
    ],
    'debug_unittest_suites': [],
}

# You must define opt_unittest_suites when enable_opt_unittests is True for a 
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
        'linux': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'fedora': {
                'opt_unittest_suites' : \
                    UNITTEST_SUITES['opt_unittest_suites'][:] + \
                    [('reftest-ipc', ['reftest-ipc'])] + \
                    [('reftest-no-accel', ['opengl-no-accel'])] + \
                    [('crashtest-ipc', ['crashtest-ipc'])],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
                'mobile_unittest_suites' : UNITTEST_SUITES['mobile_unittest_suites'][:],
            },
        },
        'linux64': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
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
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
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
                'opt_unittest_suites' : \
                    UNITTEST_SUITES['opt_unittest_suites'][:] + \
                    [('reftest-no-accel', ['reftest-no-d2d-d3d'])],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            }
        },
        'win64': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'builds_before_reboot': 1,
            'download_symbols': False,
            'enable_opt_unittests': False,
            # We can't yet run unit tests on debug builds - see bug 562459
            'enable_debug_unittests': False,
            'w764': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            },
        },
        'macosx': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'builds_before_reboot': 1,
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'leopard-o': {
                'opt_unittest_suites' : [],
                'debug_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
            },
        },
        'macosx64': {
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
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
            'lion': {
                'opt_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
                'debug_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
            },
        },
        'android': {
            'product_name': 'fennec',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'is_remote': True,
            'host_utils_url': 'http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.742597.zip',
            'enable_opt_unittests': True,
            'enable_debug_unittests': False,
            'remote_extras': ANDROID_UNITTEST_REMOTE_EXTRAS,
            'tegra_android': deepcopy(ANDROID_UNITTEST_DICT),
        },
        'android-xul': {
            'product_name': 'fennec',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'is_remote': True,
            'host_utils_url': 'http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.742597.zip',
            'enable_opt_unittests': True,
            'enable_debug_unittests': False,
            'remote_extras': UNITTEST_REMOTE_EXTRAS,
            'tegra_android-xul': deepcopy(ANDROID_XUL_UNITTEST_DICT),
        },
        'linux-android': {
            'product_name': 'fennec',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'is_remote': True,
            'host_utils_url': 'http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.742597.zip',
            'enable_opt_unittests': True,
            'enable_debug_unittests': False,
            'remote_extras': UNITTEST_REMOTE_EXTRAS,
            'tegra_android-o': deepcopy(ANDROID_XUL_UNITTEST_DICT),
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
        'branches': ['mozilla-central', 'mozilla-aurora', 'mozilla-beta', 'mozilla-release'],
        'platforms': {
            'w764': {'ext':'win64-x86_64.zip', 'debug':True}, 
            'fedora64': {'ext':'linux-x86_64.tar.bz2', 'debug':True}, 
            'fedora':{'ext':'linux-i686.tar.bz2', 'debug':True}, 
            'leopard':{'ext':'(mac|mac64).dmg', 'debug':True}, 
            'snowleopard':{'ext':'(mac|mac64).dmg', 'debug':True},
            'lion':{'ext':'(mac|mac64).dmg', 'debug':True},
            'xp':{
                'ext':'win32.zip',
                'env':PLATFORM_UNITTEST_VARS['win32']['env_name'],
                'debug':True,
                }, 
            'win7':{
                'ext':'win32.zip',
                'env':PLATFORM_UNITTEST_VARS['win32']['env_name'],
                'debug':True,
                },
            },
        'hgurl': 'http://hg.mozilla.org',
        'repo_path': 'projects/addon-sdk',
        'jetpack_tarball': 'archive/tip.tar.bz2',
        'ftp_url': 'ftp://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/%(branch)s-%(platform)s',
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

# Let's load the defaults
for branch in BRANCHES.keys():
    BRANCHES[branch]['repo_path'] = branch
    BRANCHES[branch]['branch_name'] = branch.title()
    BRANCHES[branch]['mobile_branch_name'] = branch.title()
    BRANCHES[branch]['build_branch'] = branch.title()
    BRANCHES[branch]['enable_unittests'] = True
    BRANCHES[branch]['talos_command'] = TALOS_CMD
    BRANCHES[branch]['fetch_symbols'] = True
    BRANCHES[branch]['fetch_release_symbols'] = False
    BRANCHES[branch]['talos_from_source_code'] = True
    if BRANCHES[branch].has_key('release_branch'):
        BRANCHES[branch]['release_tests'] = 5
        BRANCHES[branch]['repo_path'] = "releases/%s" % branch
        BRANCHES[branch]['platforms']['linux']['enable_mobile_unittests'] = True
    BRANCHES[branch]['support_url_base'] = 'http://build.mozilla.org/talos'
    loadTalosSuites(BRANCHES, SUITES, branch)
    BRANCHES[branch]['pgo_strategy'] = None
    BRANCHES[branch]['pgo_platforms'] = ['linux', 'linux64', 'win32']

# The following are exceptions to the defaults

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['mobile_branch_name'] = "Mobile"
BRANCHES['mozilla-central']['mobile_talos_branch'] = "mobile"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'
# Let's add win64 tests only for mozilla-central until we have enough capacity - see bug 667024
# XXX hacking warning - this code could get out of date easily
BRANCHES['mozilla-central']['platforms']['win64']['enable_opt_unittests'] = True
for suite in SUITES.keys():
    options = SUITES[suite]['options']
    if options[1] == ALL_PLATFORMS:
        options = (options[0], ALL_PLATFORMS + PLATFORMS['win64']['slave_platforms'])
    if options[1] == NO_MAC:
        options = (options[0], NO_MAC + PLATFORMS['win64']['slave_platforms'])
    if not SUITES[suite]['enable_by_default']:
        # Suites that are turned off by default
        BRANCHES['mozilla-central'][suite + '_tests'] = (0, True) + options
    else:
        # Suites that are turned on by default
        BRANCHES['mozilla-central'][suite + '_tests'] = (1, True) + options
BRANCHES['mozilla-central']['platforms']['android']['enable_debug_unittests'] = True
BRANCHES['mozilla-central']['xperf_tests'] = (1, True, {}, WIN7_ONLY)

# Side by side staging on m-c only
BRANCHES['mozilla-central']['dirtypaint_tests'] = (1, True, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-central']['jstests_tests'] = (1, True, {}, ALL_PLATFORMS)

# pgo-strategy
BRANCHES['mozilla-aurora']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'

#### MERGE DAY - EXCEPTIONS
# When Firefox 16 is on mozilla-beta we can remove these
# Firefox 16/beta
BRANCHES['mozilla-beta']['chrome.2_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-beta']['chrome_mac.2_tests'] = (1, True, {}, MAC_ONLY)
BRANCHES['mozilla-beta']['nochrome.2_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['tprow_tests'] = (1, True, TALOS_TP_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['chromer_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['other_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['nochromer_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['svgr_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-beta']['tpn_tests'] = (0, True, TALOS_TP_NEW_OPTS, ALL_PLATFORMS)
# end Firefox 16/beta

# Firefox 16/release
BRANCHES['mozilla-release']['chrome.2_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-release']['chrome_mac.2_tests'] = (1, True, {}, MAC_ONLY)
BRANCHES['mozilla-release']['nochrome.2_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-release']['tprow_tests'] = (1, True, TALOS_TP_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-release']['svg_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-release']['chromer_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-release']['other_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-release']['nochromer_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-release']['svgr_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-release']['tpn_tests'] = (0, True, TALOS_TP_NEW_OPTS, ALL_PLATFORMS)
# end Firefox 16/release
#### END OF MERGE DAY - EXCEPTIONS

######## mozilla-esr10
BRANCHES['mozilla-esr10']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr10']['talos_from_source_code'] = False
BRANCHES['mozilla-esr10']['tpn_tests'] = (0, True, TALOS_TP_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-esr10']['svgr_tests'] = (0, True, TALOS_TP_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-esr10']['other_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-esr10']['nochromer_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-esr10']['chromer_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-esr10']['tp_tests'] = (1, True, TALOS_TP_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-esr10']['svg_tests'] = (1, True, TALOS_TP_OPTS, ALL_PLATFORMS)
BRANCHES['mozilla-esr10']['chrome_tests'] = (1, True, {}, NO_MAC)
BRANCHES['mozilla-esr10']['chrome_mac_tests'] = (1, True, {}, MAC_ONLY)
BRANCHES['mozilla-esr10']['nochrome_tests'] = (1, True, {}, ALL_PLATFORMS)

######## try
BRANCHES['try']['tp4_tests'] = (1, False, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['try']['tpr_responsiveness_tests'] = (1, False, TALOS_TP_OPTS, ALL_PLATFORMS)
BRANCHES['try']['xperf_tests'] = (1, False, {}, WIN7_ONLY)
BRANCHES['try']['remote-trobocheck3_tests'] = (1, False, TALOS_REMOTE_FENNEC_OPTS, ANDROID_NATIVE)
BRANCHES['try']['platforms']['android']['enable_debug_unittests'] = True
BRANCHES['try']['pgo_strategy'] = 'try'

# Let's load jetpack for the following branches:
for branch in ('mozilla-central', 'mozilla-aurora', 'try', 'mozilla-inbound', ):
    for pf in PLATFORMS:
        if 'android' in pf:
            continue
        for slave_pf in PLATFORMS[pf]['slave_platforms']:
            # These two mac exceptions are because we have been adding debug jetpack to macosx/leopard-o
            # and opt jetpack to macosx64/leopard. This probably was not correct but that's how it came about
            # XXX clean this mess in the next refactoring patch
            if pf == "macosx" and slave_pf == "leopard-o":
                BRANCHES[branch]['platforms'][pf][slave_pf]['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
                continue
            if pf == "macosx64" and slave_pf == "leopard":
                BRANCHES[branch]['platforms'][pf][slave_pf]['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
                continue
            BRANCHES[branch]['platforms'][pf][slave_pf]['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
            BRANCHES[branch]['platforms'][pf][slave_pf]['debug_unittest_suites'] += [('jetpack', ['jetpack'])]

# Let's load peptest for the following branches:
for branch in ('mozilla-central', 'mozilla-inbound', 'try', ):
    for pf in PLATFORMS:
        if 'android' in pf:
            continue
        hg_bin = 'hg'
        if pf.startswith("win"):
            hg_bin = 'c:\\mozilla-build\\hg\\hg'
        if isinstance(PLATFORMS[pf]['mozharness_python'], list):
            reboot_command = PLATFORMS[pf]['mozharness_python'][:]
        else:
            reboot_command = [PLATFORMS[pf]['mozharness_python']]
        reboot_command.extend(['build/tools/buildfarm/maintenance/count_and_reboot.py',
                               '-f', '../reboot_count.txt',
                               '-n', '1', '-z'])
        for slave_pf in PLATFORMS[pf]['slave_platforms']:
            config_file = "peptest/prod_config.py"
            if pf == "macosx" and slave_pf == "leopard-o":
                continue
            if pf.startswith("win"):
                config_file = "peptest/windows_config.py"
            BRANCHES[branch]['platforms'][pf][slave_pf]['opt_unittest_suites'] += [('peptest', {'suite': 'peptest',
                'mozharness_repo': MOZHARNESS_REPO,
                'script_path': 'scripts/peptest.py',
                'extra_args': [
                    "--cfg", config_file
                ],
                'reboot_command': reboot_command,
                'hg_bin': hg_bin,
            })]

######## generic branch variables for project branches
for projectBranch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[projectBranch]
    loadDefaultValues(BRANCHES, projectBranch, branchConfig)
    loadCustomTalosSuites(BRANCHES, SUITES, projectBranch, branchConfig)
    loadCustomUnittestSuites(BRANCHES, projectBranch, branchConfig)

#-------------------------------------------------------------------------
# Delete all references to linux-android when mozilla-esr10 is retired.
#-------------------------------------------------------------------------
LINUX_ANDROID_BRANCHES = ('mozilla-esr10',)
for branch in BRANCHES.keys():
    if branch in LINUX_ANDROID_BRANCHES:
        for p in ('android', 'android-xul'):
            if p in BRANCHES[branch]['platforms']:
                del BRANCHES[branch]['platforms'][p]
    else:
        if 'linux-android' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['linux-android']
#-------------------------------------------------------------------------
# End Android native hacks.
#-------------------------------------------------------------------------

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
