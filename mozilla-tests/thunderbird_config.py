from copy import deepcopy

from config import BRANCH_UNITTEST_VARS, MOZHARNESS_REBOOT_CMD
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS

import thunderbird_localconfig
reload(thunderbird_localconfig)

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
BRANCH_UNITTEST_VARS = deepcopy(BRANCH_UNITTEST_VARS)

GLOBAL_VARS['stage_username'] = 'tbirdbld'
GLOBAL_VARS.update(thunderbird_localconfig.GLOBAL_VARS.copy())

BRANCHES = {
    'comm-central': {
    },
    'comm-release': {
    },
    'comm-beta': {
    },
    'comm-aurora': {
    },
    'comm-esr17': {
    },
    'try-comm-central': {
        'coallesce_jobs': False
    },
}

PLATFORMS = {
    'macosx64': {},
    'win32': {},
    'linux': {},
    'linux64': {},
}

builder_prefix = "TB "

PLATFORMS['macosx64']['slave_platforms'] = ['snowleopard', 'lion', 'mountainlion']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['snowleopard'] = {'name': builder_prefix + "Rev4 MacOSX Snow Leopard 10.6"}
PLATFORMS['macosx64']['lion'] = {'name': builder_prefix + "Rev4 MacOSX Lion 10.7"}
PLATFORMS['macosx64']['mountainlion'] = {'name': builder_prefix + "Rev5 MacOSX Mountain Lion 10.8"}
PLATFORMS['macosx64']['stage_product'] = 'thunderbird'
PLATFORMS['macosx64']['mozharness_python'] = '/tools/buildbot/bin/python'

PLATFORMS['win32']['slave_platforms'] = ['xp', 'xp-ix', 'win7', 'win7-ix']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': builder_prefix + "Rev3 WINNT 5.1"}
PLATFORMS['win32']['xp-ix'] = {'name': builder_prefix + "Windows XP 32-bit"}
PLATFORMS['win32']['win7'] = {'name': builder_prefix + "Rev3 WINNT 6.1"}
PLATFORMS['win32']['win7-ix'] = {'name': builder_prefix + "Windows 7 32-bit"}
PLATFORMS['win32']['stage_product'] = 'thunderbird'
PLATFORMS['win32']['mozharness_python'] = ['c:/mozilla-build/python25/python', '-u']

PLATFORMS['linux']['slave_platforms'] = ['fedora', 'ubuntu32_vm']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': builder_prefix + "Rev3 Fedora 12"}
PLATFORMS['linux']['ubuntu32_vm'] = {'name': 'Ubuntu VM 12.04'}
PLATFORMS['linux']['stage_product'] = 'thunderbird'
PLATFORMS['linux']['mozharness_python'] = '/tools/buildbot/bin/python'
PLATFORMS['linux']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '32',
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64']['slave_platforms'] = ['fedora64', 'ubuntu64_vm']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': builder_prefix + "Rev3 Fedora 12x64"}
PLATFORMS['linux64']['ubuntu64_vm'] = {'name': 'Ubuntu VM 12.04 x64'}
PLATFORMS['linux64']['stage_product'] = 'thunderbird'
PLATFORMS['linux64']['mozharness_python'] = '/tools/buildbot/bin/python'
PLATFORMS['linux64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/linux_config.py',
}

# Lets be explicit instead of magical.
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

SUITES = {}

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'linux': {},
        'linux64': {},
        'macosx64': {},
        'win32': {},
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


# You must define opt_unittest_suites when enable_opt_unittests is True for a
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
    'linux': {
        'product_name': 'thunderbird',
        'app_name': 'mail',
        'brand_name': 'Daily',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'fedora': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'ubuntu32_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
    },
    'linux64': {
        'product_name': 'thunderbird',
        'app_name': 'mail',
        'brand_name': 'Daily',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'fedora64': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'ubuntu64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
    },
    'win32': {
        'product_name': 'thunderbird',
        'app_name': 'mail',
        'brand_name': 'Daily',
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
        'xp-ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'win7': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'win7-ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
    },
    'macosx64': {
        'product_name': 'thunderbird',
        'app_name': 'mail',
        'brand_name': 'Daily',
        'builds_before_reboot': 1,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'snowleopard': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'lion': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
        },
        'mountainlion': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
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

######## comm-release
BRANCHES['comm-release']['pgo_strategy'] = None
BRANCHES['comm-release']['repo_path'] = "releases/comm-release"
# MERGE DAY: remove when Thunderbird 24 merges in
del BRANCHES['comm-release']['platforms']['win32']['xp-ix']
del BRANCHES['comm-release']['platforms']['win32']['win7-ix']
del BRANCHES['comm-release']['platforms']['linux']['ubuntu32_vm']
del BRANCHES['comm-release']['platforms']['linux64']['ubuntu64_vm']
BRANCHES['comm-release']['platforms']['win32']['slave_platforms'] = ['xp', 'win7']
BRANCHES['comm-release']['platforms']['linux']['slave_platforms'] = ['fedora']
BRANCHES['comm-release']['platforms']['linux64']['slave_platforms'] = ['fedora64']

######## comm-beta
BRANCHES['comm-beta']['pgo_strategy'] = None
BRANCHES['comm-beta']['repo_path'] = "releases/comm-beta"
BRANCHES['comm-beta']['platforms']['linux']['slave_platforms'] = ['fedora']
BRANCHES['comm-beta']['platforms']['linux64']['slave_platforms'] = ['fedora64']

######## comm-aurora
BRANCHES['comm-aurora']['pgo_strategy'] = None
BRANCHES['comm-aurora']['repo_path'] = "releases/comm-aurora"
BRANCHES['comm-aurora']['platforms']['linux']['slave_platforms'] = ['fedora']
BRANCHES['comm-aurora']['platforms']['linux64']['slave_platforms'] = ['fedora64']

######## comm-esr17
BRANCHES['comm-esr17']['pgo_strategy'] = None
BRANCHES['comm-esr17']['repo_path'] = "releases/comm-esr17"
del BRANCHES['comm-esr17']['platforms']['win32']['xp-ix']
del BRANCHES['comm-esr17']['platforms']['win32']['win7-ix']
del BRANCHES['comm-esr17']['platforms']['linux']['ubuntu32_vm']
del BRANCHES['comm-esr17']['platforms']['linux64']['ubuntu64_vm']
BRANCHES['comm-esr17']['platforms']['win32']['slave_platforms'] = ['xp', 'win7']
BRANCHES['comm-esr17']['platforms']['linux']['slave_platforms'] = ['fedora']
BRANCHES['comm-esr17']['platforms']['linux64']['slave_platforms'] = ['fedora64']

######## try
BRANCHES['try-comm-central']['enable_try'] = True

# MERGE DAY: Remove comm-release when TB 24 merges in.
WIN32_REV3_BRANCHES = ("comm-release", "comm-esr17")
FEDORA_REV3_BRANCHES = WIN32_REV3_BRANCHES

# Disable Rev3 winxp and win7 machines for all branches apart from try and comm-central
# for now.
for branch in set(BRANCHES.keys()) - set(WIN32_REV3_BRANCHES):
    if 'win32' not in BRANCHES[branch]['platforms']:
        continue
    del BRANCHES[branch]['platforms']['win32']['xp']
    del BRANCHES[branch]['platforms']['win32']['win7']
    BRANCHES[branch]['platforms']['win32']['slave_platforms'] = ['xp-ix', 'win7-ix']

for branch in set(BRANCHES.keys()) - set(FEDORA_REV3_BRANCHES):
    if 'linux' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['linux']['fedora']
        BRANCHES[branch]['platforms']['linux']['slave_platforms'] = ['ubuntu32_vm']
    if 'linux64' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['linux64']['fedora64']
        BRANCHES[branch]['platforms']['linux64']['slave_platforms'] = ['ubuntu64_vm']

if __name__ == "__main__":
    import sys
    import pprint

    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = dict(BRANCHES.items())

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)

    for suite in sorted(SUITES):
        out = pprint.pformat(SUITES[suite])
        for l in out.splitlines():
            print '%s: %s' % (suite, l)
