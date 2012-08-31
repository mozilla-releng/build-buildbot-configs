from copy import deepcopy

from config import BRANCH_UNITTEST_VARS, MOZHARNESS_REPO
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS, GRAPH_CONFIG, \
                        PLATFORM_VARS

import thunderbird_localconfig
reload(thunderbird_localconfig)

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
BRANCH_UNITTEST_VARS = deepcopy(BRANCH_UNITTEST_VARS)

GLOBAL_VARS['stage_username'] = 'tbirdbld'
GLOBAL_VARS.update(thunderbird_localconfig.GLOBAL_VARS.copy())

BRANCH_UNITTEST_VARS

BRANCHES = {
    'comm-central': {
    },
    'comm-release': {
    },
    'comm-beta': {
    },
    'comm-aurora': {
    },
    'comm-esr10': {
    },
    'try-comm-central': {
      'coallesce_jobs': False
    },
}

PLATFORMS = {
    'macosx': {},
    'macosx64': {},
    'win32': {},
    'win64': {},
    'linux': {},
    'linux64' : {},
}

builder_prefix = "TB "

# work around path length problem bug 599795
# leopard-o == leopard-old
PLATFORMS['macosx']['slave_platforms'] = ['leopard-o']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['leopard-o'] = {'name': builder_prefix + "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx']['stage_product'] = 'thunderbird'
PLATFORMS['macosx']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['macosx64']['slave_platforms'] = ['leopard', 'snowleopard',
                                            'lion']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['leopard'] = {'name': builder_prefix + "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx64']['snowleopard'] = {'name': builder_prefix + "Rev4 MacOSX Snow Leopard 10.6"}
PLATFORMS['macosx64']['lion'] = {'name': builder_prefix + "Rev4 MacOSX Lion 10.7"}
PLATFORMS['macosx64']['stage_product'] = 'thunderbird'
PLATFORMS['macosx64']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['win32']['slave_platforms'] = ['xp', 'win7']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': builder_prefix + "Rev3 WINNT 5.1"}
PLATFORMS['win32']['win7'] = {'name': builder_prefix + "Rev3 WINNT 6.1"}
PLATFORMS['win32']['stage_product'] = 'thunderbird'
PLATFORMS['win32']['mozharness_python'] = ['c:/mozilla-build/python25/python', '-u']

PLATFORMS['win64']['slave_platforms'] = ['w764']
PLATFORMS['win64']['env_name'] = 'win64-perf'
PLATFORMS['win64']['w764'] = {'name': builder_prefix + "Rev3 WINNT 6.1 x64",
                              'download_symbols': False,
                             }
PLATFORMS['win64']['stage_product'] = 'thunderbird'
PLATFORMS['win64']['mozharness_python'] = ['c:/mozilla-build/python25/python', '-u']

PLATFORMS['linux']['slave_platforms'] = ['fedora']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': builder_prefix + "Rev3 Fedora 12"}
PLATFORMS['linux']['stage_product'] = 'thunderbird'
PLATFORMS['linux']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['linux64']['slave_platforms'] = ['fedora64']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': builder_prefix + "Rev3 Fedora 12x64"}
PLATFORMS['linux64']['stage_product'] = 'thunderbird'
PLATFORMS['linux64']['mozharness_python'] = '/tools/buildbot/bin/python'

# Lets be explicit instead of magical.  leopard-o should be a second
# entry in the SLAVE dict
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform])
        if slave_platform in TRY_SLAVES:
            platform_config[slave_platform]['try_slaves'] = sorted(TRY_SLAVES[slave_platform])
        else:
            platform_config[slave_platform]['try_slaves'] = platform_config[slave_platform]['slaves']

MOBILE_PLATFORMS = []

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

ANDROID = []

ANDROID_NATIVE = []

ANDROID_XUL = []

ADDON_TESTER_PLATFORMS = ['win7', 'fedora', 'snowleopard']

SUITES = {}

# these three are for mozilla-1.9.2
OLD_BRANCH_ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['macosx']['slave_platforms']

OLD_BRANCH_NO_WIN = PLATFORMS['macosx']['slave_platforms'] + PLATFORMS['linux']['slave_platforms']

OLD_BRANCH_NO_MAC = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['win32']['slave_platforms']

OLD_BRANCH_MAC_ONLY = PLATFORMS['macosx']['slave_platforms']

OLD_BRANCH_ADDON_TESTER_PLATFORMS = ['win7'] + ['fedora'] + ['snowleopard']

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
    },
}

# Default set of unit tests
UNITTEST_SUITES = {
    'opt_unittest_suites': [
        ('xpcshell', ['xpcshell']),
        ('mozmill', ['mozmill']),
    ],
    'debug_unittest_suites': [
        ('xpcshell', ['xpcshell']),
        ('mozmill', ['mozmill']),
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
    BRANCHES[branch]['build_branch'] = branchConfig.get('build_branch', branch.title())
    BRANCHES[branch]['fetch_symbols'] = branchConfig.get('fetch_symbols', True)
    BRANCHES[branch]['enable_unittests'] = branchConfig.get('enable_unittests', True)
    BRANCHES[branch]['pgo_strategy'] = None

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

ANDROID_XUL_UNITTEST_DICT = {}
ANDROID_UNITTEST_DICT = {}

# You must define opt_unittest_suites when enable_opt_unittests is True for a
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
        'linux': {
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'brand_name': 'Daily',
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'fedora': {
                'opt_unittest_suites' : \
                    UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            },
        },
        'linux64': {
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'brand_name': 'Daily',
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
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'brand_name': 'Daily',
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
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'brand_name': 'Daily',
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
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'brand_name': 'Daily',
            'builds_before_reboot': 1,
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'leopard-o': {
                'opt_unittest_suites' : [],
                'debug_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
            },
        },
        'macosx64': {
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'brand_name': 'Daily',
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
}

# Copy project branches into BRANCHES keys
#for branch in ACTIVE_PROJECT_BRANCHES:
#    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

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
    if branch in thunderbird_localconfig.BRANCHES:
        for key, value in thunderbird_localconfig.BRANCHES[branch].items():
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

#    # Merge in any project branch config for platforms
#    if branch in ACTIVE_PROJECT_BRANCHES and PROJECT_BRANCHES[branch].has_key('platforms'):
#        for platform, platform_config in PROJECT_BRANCHES[branch]['platforms'].items():
#            if platform in PLATFORMS:
#                for key, value in platform_config.items():
#                    value = deepcopy(value)
#                    if isinstance(value, str):
#                        value = value % locals()
#                    BRANCHES[branch]['platforms'][platform][key] = value

    for platform, platform_config in thunderbird_localconfig.PLATFORM_VARS.items():
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

# Let's load the defaults
for branch in BRANCHES.keys():
    BRANCHES[branch]['repo_path'] = branch
    BRANCHES[branch]['branch_name'] = branch.title()
    BRANCHES[branch]['build_branch'] = branch.title()
    BRANCHES[branch]['enable_unittests'] = True
    BRANCHES[branch]['fetch_symbols'] = True
    BRANCHES[branch]['fetch_release_symbols'] = False
    BRANCHES[branch]['pgo_strategy'] = None
    BRANCHES[branch]['pgo_platforms'] = []

# The following are exceptions to the defaults

######## comm-central
BRANCHES['comm-central']['branch_name'] = "Thunderbird"
BRANCHES['comm-central']['repo_path'] = "comm-central"
#BRANCHES['comm-central']['build_branch'] = "1.9.2"
BRANCHES['comm-central']['pgo_strategy'] = None
# Let's add win64 tests only for comm-central until we have enough capacity - see bug 667024
# XXX hacking warning - this code could get out of date easily
BRANCHES['comm-central']['platforms']['win64']['enable_opt_unittests'] = True
for suite in SUITES.keys():
    options = SUITES[suite]['options']
    if options[1] == ALL_PLATFORMS:
        options = (options[0], ALL_PLATFORMS + PLATFORMS['win64']['slave_platforms'])
    if options[1] == NO_MAC:
        options = (options[0], NO_MAC + PLATFORMS['win64']['slave_platforms'])
    if not SUITES[suite]['enable_by_default']:
        # Suites that are turned off by default
        BRANCHES['comm-central'][suite + '_tests'] = (0, True) + options
    else:
        # Suites that are turned on by default
        BRANCHES['comm-central'][suite + '_tests'] = (1, True) + options

######## comm-release
BRANCHES['comm-release']['pgo_strategy'] = None
BRANCHES['comm-release']['repo_path'] = "releases/comm-release"

######## comm-beta
BRANCHES['comm-beta']['pgo_strategy'] = None
BRANCHES['comm-beta']['repo_path'] = "releases/comm-beta"

######## comm-aurora
BRANCHES['comm-aurora']['pgo_strategy'] = None
BRANCHES['comm-aurora']['repo_path'] = "releases/comm-aurora"

######## comm-esr10
BRANCHES['comm-esr10']['pgo_strategy'] = None

######## try
BRANCHES['try-comm-central']['enable_try'] = True

#-------------------------------------------------------------------------
# MERGE day - disable leopard tests for TB17 onwards
#-------------------------------------------------------------------------
for branch in ['comm-central', 'try-comm-central', 'comm-aurora']:
    if 'macosx' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['macosx']
    if 'macosx64' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['macosx64']['leopard']
        BRANCHES[branch]['platforms']['macosx64']['slave_platforms'] = ['snowleopard', 'lion']
#-------------------------------------------------------------------------
# End disable leopard tests for TB17 onwards
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

