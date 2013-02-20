from copy import deepcopy

import config_common
reload(config_common)
from config_common import TALOS_CMD, loadDefaultValues, loadCustomTalosSuites, loadTalosSuites

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS, GRAPH_CONFIG

MOZHARNESS_REBOOT_CMD = ['scripts/external_tools/count_and_reboot.py',
                         '-f', '../reboot_count.txt',
                         '-n', '1', '-z']

TALOS_DIRTY_OPTS = {'talosAddOns': ['profiles/dirtyDBs.zip', 'profiles/dirtyMaxDBs.zip']}

TALOS_TP_OPTS = {'plugins': {'32': 'zips/flash32_10_3_183_5.zip', '64': 'zips/flash64_11_0_d1_98.zip'}, 'pagesets': ['zips/tp5.zip']}
TALOS_TP_NEW_OPTS = {'plugins': {'32': 'zips/flash32_10_3_183_5.zip', '64': 'zips/flash64_11_0_d1_98.zip'}, 'pagesets': ['zips/tp5n.zip']}

BRANCHES = {
    'mozilla-central':     {},
    'mozilla-aurora':      {},
    'mozilla-release':     {},
    'mozilla-beta':        {},
    'mozilla-esr17':       {
        'datazilla_url': None,
        'platforms': {
            'macosx': {},
            'macosx64': {},
            'win32': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g18': {
        'datazilla_url': None,
        'platforms': {
            # desktop per sicking in Bug 829513
            'macosx64': {},
            'win32': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g18_v1_0_0': {
        'datazilla_url': None,
        'platforms': {
            # desktop per sicking in Bug 829513
            'macosx64': {},
            'win32': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g18_v1_0_1': {
        'datazilla_url': None,
        'platforms': {
            # desktop per sicking in Bug 829513
            'macosx64': {},
            'win32': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'try': {'coallesce_jobs': False},
}

# Talos
PLATFORMS = {
    'macosx': {},
    'macosx64': {},
    'win32': {},
    'linux': {},
    'linux64': {},
}

# work around path length problem bug 599795
# leopard-o == leopard-old
PLATFORMS['macosx']['slave_platforms'] = ['leopard-o']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['leopard-o'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx']['stage_product'] = 'firefox'
PLATFORMS['macosx']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD}

PLATFORMS['macosx64']['slave_platforms'] = ['leopard', 'snowleopard',
                                            'lion', 'mountainlion']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['leopard'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx64']['snowleopard'] = {'name': "Rev4 MacOSX Snow Leopard 10.6"}
PLATFORMS['macosx64']['lion'] = {'name': "Rev4 MacOSX Lion 10.7"}
PLATFORMS['macosx64']['mountainlion'] = {'name': "Rev5 MacOSX Mountain Lion 10.8"}
PLATFORMS['macosx64']['stage_product'] = 'firefox'
PLATFORMS['macosx64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

PLATFORMS['win32']['slave_platforms'] = ['xp', 'win7']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "Rev3 WINNT 5.1"}
PLATFORMS['win32']['win7'] = {'name': "Rev3 WINNT 6.1"}
PLATFORMS['win32']['stage_product'] = 'firefox'
PLATFORMS['win32']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
}

PLATFORMS['linux']['slave_platforms'] = ['fedora', 'ubuntu32']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': "Rev3 Fedora 12"}
PLATFORMS['linux']['ubuntu32'] = {'name': 'Ubuntu 12.04'}
PLATFORMS['linux']['stage_product'] = 'firefox'
PLATFORMS['linux']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

PLATFORMS['linux64']['slave_platforms'] = ['fedora64', 'ubuntu64']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': "Rev3 Fedora 12x64"}
PLATFORMS['linux64']['ubuntu64'] = {'name': 'Ubuntu 12.04 x64'}
PLATFORMS['linux64']['stage_product'] = 'firefox'
PLATFORMS['linux64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

# Lets be explicit instead of magical.  leopard-o should be a second
# entry in the SLAVE dict
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform])
        if slave_platform in TRY_SLAVES:
            platform_config[slave_platform]['try_slaves'] = sorted(TRY_SLAVES[slave_platform])
        else:
            platform_config[slave_platform]['try_slaves'] = platform_config[slave_platform]['slaves']

ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
    PLATFORMS['linux64']['slave_platforms'] + \
    PLATFORMS['win32']['slave_platforms'] + \
    PLATFORMS['macosx64']['slave_platforms']
# Don't use ubuntu{32,64} for talos for now
ALL_PLATFORMS.remove('ubuntu32')
ALL_PLATFORMS.remove('ubuntu64')

WIN7_ONLY = ['win7']

NO_WIN = PLATFORMS['macosx64']['slave_platforms'] + PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms']
# Don't use ubuntu{,3264} for talos for now
NO_WIN.remove('ubuntu32')
NO_WIN.remove('ubuntu64')

NO_MAC = PLATFORMS['linux']['slave_platforms'] + \
    PLATFORMS['linux64']['slave_platforms'] + \
    PLATFORMS['win32']['slave_platforms']
# Don't use ubuntu{32,64} for talos for now
NO_MAC.remove('ubuntu32')
NO_MAC.remove('ubuntu64')

MAC_ONLY = PLATFORMS['macosx64']['slave_platforms']

SUITES = {
    'chrome': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll:a11y:ts_paint:tpaint:tsspider', '--mozAfterPaint'],
        'options': ({}, NO_MAC),
    },
    # chrome_mac compared to chrome is that it does not contain a11y and only run on Mac
    'chrome_mac': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll:ts_paint:tpaint:tsspider', '--mozAfterPaint'],
        'options': ({}, MAC_ONLY),
    },
    'nochrome': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsspider', '--noChrome', '--mozAfterPaint'],
        'options': ({}, ALL_PLATFORMS),
    },
    'dirty': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts_places_generated_med:ts_places_generated_max', '--setPref', 'hangmonitor.timeout=0'],
        'options': (TALOS_DIRTY_OPTS, ALL_PLATFORMS),
    },
    'tp': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5', '--mozAfterPaint'],
        'options': (TALOS_TP_OPTS, ALL_PLATFORMS),
    },
    'cold': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts_cold:ts_cold_generated_min:ts_cold_generated_med:ts_cold_generated_max'],
        'options': (TALOS_DIRTY_OPTS, NO_WIN),
    },
    'svg': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvg:tsvg_opacity'],
        'options': ({}, ALL_PLATFORMS),
    },
    'dromaeo': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom'],
        'options': ({}, ALL_PLATFORMS),
    },
    'chrome.2': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll.2:a11y.2:ts_paint:tpaint:tsspider.2', '--mozAfterPaint', '--ignoreFirst', '--sampleConfig', 'sample.2.config'],
        'options': ({}, NO_MAC),
    },
    # chrome_mac compared to chrome is that it does not contain a11y and only run on Mac
    'chrome_mac.2': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll.2:ts_paint:tpaint:tsspider.2', '--mozAfterPaint', '--ignoreFirst', '--sampleConfig', 'sample.2.config'],
        'options': ({}, MAC_ONLY),
    },
    'nochrome.2': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsspider.2', '--noChrome', '--mozAfterPaint', '--ignoreFirst', '--sampleConfig', 'sample.2.config'],
        'options': ({}, ALL_PLATFORMS),
    },
    'xperf': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5n', '--sampleConfig', 'xperf.config', '--mozAfterPaint', '--xperf_path', '"c:/Program Files/Microsoft Windows Performance Toolkit/xperf.exe"', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, WIN7_ONLY),
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
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tspaint_places_generated_med:tspaint_places_generated_max', '--setPref', 'hangmonitor.timeout=0', '--mozAfterPaint'],
        'options': (TALOS_DIRTY_OPTS, ALL_PLATFORMS),
    },
    'dromaeojs': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom:kraken:v8_7'],
        'options': ({}, ALL_PLATFORMS),
    },
    'chromez': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tresize', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_PLATFORMS),
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
    },
}

# Default set of unit tests
UNITTEST_SUITES = {
    'opt_unittest_suites': [
        # Turn on chunks for mochitest
        ('mochitest', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-browser-chrome', ['mochitest-browser-chrome']),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-a11y', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
        # Disabled in bug 630551
        #('mozmill-all', ['mozmill']),
    ],
    'debug_unittest_suites': [
        # Turn on chunks for mochitest
        ('mochitest', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-browser-chrome', ['mochitest-browser-chrome']),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-a11y', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
        # Disabled in bug 630551
        #('mozmill-all', ['mozmill']),
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


def nested_haskey(dictionary, *keys):
    if len(keys) == 1:
        return keys[0] in dictionary
    else:
        #recurse
        key, keys = keys[0], keys[1:]
        if key in dictionary:
            return nested_haskey(dictionary[key], *keys)
        else:
            return False

# You must define opt_unittest_suites when enable_opt_unittests is True for a
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
    'linux': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'fedora': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + [
                ('reftest-ipc', ['reftest-ipc']),
                ('reftest-no-accel', ['opengl-no-accel']),
                ('crashtest-ipc', ['crashtest-ipc'])
            ],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'ubuntu32': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + [
                ('reftest-ipc', ['reftest-ipc']),
                ('reftest-no-accel', ['opengl-no-accel']),
                ('crashtest-ipc', ['crashtest-ipc'])
            ],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
    },
    'linux64': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'fedora64': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'ubuntu64': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
    },
    'win32': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'mochitest_leak_threshold': 484,
        'crashtest_leak_threshold': 484,
        'env_name': 'win32-perf-unittest',
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'xp': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'win7': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] +
            [('reftest-no-accel', ['reftest-no-d2d-d3d'])],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        }
    },
    'macosx': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'leopard-o': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
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
            'opt_unittest_suites': removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
            'debug_unittest_suites': [],
        },
        'snowleopard': {
            'opt_unittest_suites': removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
            'debug_unittest_suites': removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
        },
        'lion': {
            'opt_unittest_suites': removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
            'debug_unittest_suites': removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
        },
        'mountainlion': {
            'opt_unittest_suites': removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
            'debug_unittest_suites': removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
        },
    },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # In order to have things ride the trains we need to be able to
        # override "global" things. Therefore, we shouldn't override anything
        # that's already been set.
        if key in BRANCHES[branch]:
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
    if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch]:
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
            'ubuntu64': {'ext': 'linux-x86_64.tar.bz2', 'debug': True},
            'ubuntu32': {'ext': 'linux-i686.tar.bz2', 'debug': True},
            'snowleopard': {'ext': '(mac|mac64).dmg', 'debug': True},
            'lion': {'ext': '(mac|mac64).dmg', 'debug': True},
            'mountainlion': {'ext': '(mac|mac64).dmg', 'debug': True},
            'xp': {
                'ext': 'win32.zip',
                'env': PLATFORM_UNITTEST_VARS['win32']['env_name'],
                'debug': True,
            },
            'win7': {
                'ext': 'win32.zip',
                'env': PLATFORM_UNITTEST_VARS['win32']['env_name'],
                'debug': True,
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
    BRANCHES[branch]['build_branch'] = branch.title()
    BRANCHES[branch]['enable_unittests'] = True
    BRANCHES[branch]['talos_command'] = TALOS_CMD
    BRANCHES[branch]['fetch_symbols'] = True
    BRANCHES[branch]['fetch_release_symbols'] = False
    BRANCHES[branch]['talos_from_source_code'] = True
    BRANCHES[branch]['support_url_base'] = 'http://build.mozilla.org/talos'
    loadTalosSuites(BRANCHES, SUITES, branch)
    BRANCHES[branch]['pgo_strategy'] = None
    BRANCHES[branch]['pgo_platforms'] = ['linux', 'linux64', 'win32']

# The following are exceptions to the defaults

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'
BRANCHES['mozilla-central']['xperf_tests'] = (1, True, TALOS_TP_NEW_OPTS, WIN7_ONLY)

######### mozilla-release
BRANCHES['mozilla-release']['release_tests'] = 1
BRANCHES['mozilla-release']['repo_path'] = "releases/mozilla-release"
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'

######### mozilla-beta
BRANCHES['mozilla-beta']['release_tests'] = 1
BRANCHES['mozilla-beta']['repo_path'] = "releases/mozilla-beta"
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'

######### mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = "releases/mozilla-aurora"
BRANCHES['mozilla-aurora']['pgo_strategy'] = 'per-checkin'

######### mozilla-esr17
BRANCHES['mozilla-esr17']['release_tests'] = 1
BRANCHES['mozilla-esr17']['repo_path'] = "releases/mozilla-esr17"
BRANCHES['mozilla-esr17']['pgo_strategy'] = 'per-checkin'

######### mozilla-b2g18
BRANCHES['mozilla-b2g18']['release_tests'] = 1
BRANCHES['mozilla-b2g18']['repo_path'] = "releases/mozilla-b2g18"
BRANCHES['mozilla-b2g18']['pgo_strategy'] = 'per-checkin'

######### mozilla-b2g18_v1_0_0
BRANCHES['mozilla-b2g18_v1_0_0']['release_tests'] = 1
BRANCHES['mozilla-b2g18_v1_0_0']['repo_path'] = "releases/mozilla-b2g18_v1_0_0"
BRANCHES['mozilla-b2g18_v1_0_0']['pgo_strategy'] = 'per-checkin'

######### mozilla-b2g18_v1_0_1
BRANCHES['mozilla-b2g18_v1_0_1']['release_tests'] = 1
BRANCHES['mozilla-b2g18_v1_0_1']['repo_path'] = "releases/mozilla-b2g18_v1_0_1"
BRANCHES['mozilla-b2g18_v1_0_1']['pgo_strategy'] = 'per-checkin'

######## try
BRANCHES['try']['xperf_tests'] = (1, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
BRANCHES['try']['pgo_strategy'] = 'try'
BRANCHES['try']['enable_try'] = True

# Let's load jetpack for the following branches:
for branch in ('mozilla-central', 'mozilla-aurora', 'try', 'mozilla-inbound', 'ionmonkey', ):
    for pf in PLATFORMS:
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


# Let's load Marionette for the following branches:
for branch in ('mozilla-central', 'mozilla-inbound', 'try', 'fx-team', 'services-central', ):
    for pf in PLATFORMS:
        config_file = "marionette/prod_config.py"
        if pf.startswith('win'):
            if branch != 'try':
                # for now, only run windows tests on try because of bug 795513
                continue
            config_file = "marionette/windows_config.py"
        for slave_pf in PLATFORMS[pf]['slave_platforms']:
            if pf == "macosx" and slave_pf in ("leopard-o", "leopard"):
                # we don't run on OSX 10.5
                continue
            # Marionette is only enabled on debug builds
            BRANCHES[branch]['platforms'][pf][slave_pf]['debug_unittest_suites'] += [(
                'marionette',
                {'suite': 'marionette',
                 'script_path': 'scripts/marionette.py',
                 'use_mozharness': True,
                 'extra_args': [
                     "--cfg", config_file
                 ],
                 'reboot_command': PLATFORMS[pf]['mozharness_config']['reboot_command'],
                 'hg_bin': PLATFORMS[pf]['mozharness_config']['hg_bin'],
                 })]

### start of mozharness desktop unittests
mozharness_unittest_suites = [
    {'suite_name': 'mochitest-1', 'suite_category': 'mochitest', 'sub_categories': ['plain1']},
    {'suite_name': 'mochitest-2', 'suite_category': 'mochitest', 'sub_categories': ['plain2']},
    {'suite_name': 'mochitest-3', 'suite_category': 'mochitest', 'sub_categories': ['plain3']},
    {'suite_name': 'mochitest-4', 'suite_category': 'mochitest', 'sub_categories': ['plain4']},
    {'suite_name': 'mochitest-5', 'suite_category': 'mochitest', 'sub_categories': ['plain5']},
    {'suite_name': 'mochitest-browser-chrome', 'suite_category': 'mochitest', 'sub_categories':
        ['browser-chrome']},
    {'suite_name': 'mochitest-other', 'suite_category': 'mochitest', 'sub_categories':
        ['chrome', 'a11y', 'plugins']},
    {'suite_name': 'reftest', 'suite_category': 'reftest', 'sub_categories': ['reftest']},
    {'suite_name': 'jsreftest', 'suite_category': 'reftest', 'sub_categories': ['jsreftest']},
    {'suite_name': 'crashtest', 'suite_category': 'reftest', 'sub_categories': ['crashtest']},
    {'suite_name': 'reftest-ipc', 'suite_category': 'reftest', 'sub_categories': ['reftest-ipc'], 'platforms': ['linux'], 'test_types': ['opt']},
    {'suite_name': 'reftest-no-accel', 'suite_category': 'reftest', 'sub_categories': ['reftest-no-accel'],
     'platforms': ['linux', 'win32'], 'slave_platforms': ['fedora', 'ubuntu32', 'win7'], 'test_types': ['opt']},
    {'suite_name': 'crashtest-ipc', 'suite_category': 'reftest', 'sub_categories': ['crashtest-ipc'], 'platforms': ['linux'], 'test_types': ['opt']},
    {'suite_name': 'xpcshell', 'suite_category': 'xpcshell', 'sub_categories': ['xpcshell']},
]
for branch in BRANCHES:
    if BRANCHES[branch].get('mozharness_unittests'):
        for pf in PLATFORMS:
            hg_bin = 'hg'
            if pf.startswith("win"):
                config_file = "unittests/win_unittest.py"
            elif pf.startswith("mac"):
                config_file = "unittests/mac_unittest.py"
            else:
                config_file = "unittests/linux_unittest.py"
            for slave_pf in PLATFORMS[pf]['slave_platforms']:
                if pf == "macosx" and slave_pf == "leopard-o":
                    continue
                for testtype in ("opt", "debug"):
                    if not BRANCHES[branch]['platforms'][pf][slave_pf]['%s_unittest_suites' % testtype]:
                        continue
                    BRANCHES[branch]['platforms'][pf][slave_pf]['%s_unittest_suites' % testtype] = []
                    for suite in mozharness_unittest_suites:
                        if 'platforms' in suite and pf not in suite['platforms']:
                            continue
                        if 'test_types' in suite and testtype not in suite['test_types']:
                            continue
                        if 'slave_platforms' in suite and slave_pf not in suite['slave_platforms']:
                            continue
                        extra_args = ["--cfg", config_file]
                        for sub_category in suite['sub_categories']:
                            extra_args += ["--%s-suite" % suite['suite_category'], sub_category]
                        if BRANCHES[branch]['fetch_symbols'] and BRANCHES[branch]['platforms'][pf][slave_pf].get('download_symbols', True):
                            if testtype == "debug":
                                extra_args += ["--download-symbols", "true"]
                            else:
                                extra_args += ["--download-symbols", "ondemand"]
                        BRANCHES[branch]['platforms'][pf][slave_pf]['%s_unittest_suites' % testtype] += [
                            (suite['suite_name'], {
                                'use_mozharness': True,
                                'script_path': 'scripts/desktop_unittest.py',
                                'extra_args': extra_args,
                                'reboot_command': PLATFORMS[pf]['mozharness_config']['reboot_command'],
                                'hg_bin': PLATFORMS[pf]['mozharness_config']['hg_bin'],
                                'script_maxtime': 7200,
                            })]
###################### END OF MOZHARNESS UNITTEST CONFIGS

######## generic branch variables for project branches
for projectBranch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[projectBranch]
    loadDefaultValues(BRANCHES, projectBranch, branchConfig)
    loadCustomTalosSuites(BRANCHES, SUITES, projectBranch, branchConfig)

#-------------------------------------------------------------------------
# Remove leopard when esr10 goes away
#-------------------------------------------------------------------------
for branch in BRANCHES.keys():
    if 'macosx' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['macosx']
    if 'macosx64' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['macosx64']['leopard']
        BRANCHES[branch]['platforms']['macosx64']['slave_platforms'] = ['snowleopard', 'lion', 'mountainlion']
#-------------------------------------------------------------------------
# End disable leopard tests for FF17 onwards
#-------------------------------------------------------------------------

# MERGE DAY NOTE: remove v21 based branches from the list below
NON_UBUNTU_BRANCHES = ("mozilla-beta", "mozilla-release", "mozilla-esr17",
                       "mozilla-b2g18", "mozilla-b2g18_v1_0_0", "mozilla-b2g18_v1_0_1")
# Green tests, including mozharness based ones
# Tests listed as Ubuntu tests won't be enabled on Fedora
UBUNTU_OPT_UNITTEST = ["crashtest", "jsreftest", "jetpack", "crashtest-ipc",
                       "reftest-ipc"]
UBUNTU_DEBUG_UNITTEST = ["crashtest", "jsreftest", "jetpack", "marionette"]

# Remove Ubuntu platform from the release trains,
# use either Fedora or Ubuntu for other branches,
# don't touch cedar
for branch in set(BRANCHES.keys()) - set(['cedar', 'build-system']):
    if branch in NON_UBUNTU_BRANCHES:
        # Remove Ubuntu completely
        if 'linux64' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['linux64']['ubuntu64']
            BRANCHES[branch]['platforms']['linux64']['slave_platforms'] = ['fedora64']
        if 'linux' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['linux']['ubuntu32']
            BRANCHES[branch]['platforms']['linux']['slave_platforms'] = ['fedora']
        continue

    for p, ubuntu, fedora in [('linux', 'ubuntu32', 'fedora'),
                              ('linux64', 'ubuntu64', 'fedora64')]:
        for suite_type, ubuntu_tests in [('opt_unittest_suites',
                                         UBUNTU_OPT_UNITTEST),
                                         ('debug_unittest_suites',
                                         UBUNTU_DEBUG_UNITTEST)]:
            if nested_haskey(BRANCHES[branch]['platforms'], p, ubuntu,
                             suite_type):
                for suite in list(BRANCHES[branch]['platforms'][p][ubuntu][suite_type]):
                    if suite[0] not in ubuntu_tests:
                        BRANCHES[branch]['platforms'][p][ubuntu][suite_type].remove(suite)
                    else:
                        try:
                            BRANCHES[branch]['platforms'][p][fedora][suite_type].remove(suite)
                        except KeyError:
                            pass


if __name__ == "__main__":
    import sys
    import pprint

    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = dict(BRANCHES.items() + PROJECTS.items())

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)

    for suite in sorted(SUITES):
        out = pprint.pformat(SUITES[suite])
        for l in out.splitlines():
            print '%s: %s' % (suite, l)
