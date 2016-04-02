from copy import deepcopy
import re

import config_common
reload(config_common)
from config_common import loadDefaultValues, loadCustomTalosSuites

import master_common
reload(master_common)
from master_common import setMainFirefoxVersions, items_before, items_at_least

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS, GRAPH_CONFIG
from config import MOZHARNESS_REBOOT_CMD

import config_seta
reload(config_seta)
from config_seta import loadSkipConfig

TALOS_REMOTE_FENNEC_OPTS = {
    'productName': 'fennec',
    'remoteTests': True,
    'remoteExtras': {
        'options': [
            '--sampleConfig', 'remote.config',
            '--output', 'local.yml',
            '--webServer', 'talos-remote.pvt.build.mozilla.org',
            '--browserWait', '60',
        ],
    },
}

ANDROID_UNITTEST_REMOTE_EXTRAS = {'cmdOptions': ['--bootstrap'], }

BRANCHES = {
    'mozilla-central':     {},
    'mozilla-aurora':      {},
    'mozilla-release':     {},
    'mozilla-beta':        {},
    'try': {'coallesce_jobs': False},
}

setMainFirefoxVersions(BRANCHES)

# Talos
PLATFORMS = {
    'android-api-9': {},
    'android-api-11': {},
    'android-api-15': {},
    'android-x86': {},
}



# bug 1073772 - split 'android' into two based on api
## this will replace 'android' as it rides trains
PLATFORMS['android-api-9']['slave_platforms'] = \
    ['ubuntu64_vm_mobile', 'ubuntu64_vm_large', ]
PLATFORMS['android-api-9']['env_name'] = 'android-perf'
PLATFORMS['android-api-9']['is_mobile'] = True
PLATFORMS['android-api-9']['ubuntu64_vm_mobile'] = {
    'name': "Android armv7 API 9",
}
PLATFORMS['android-api-9']['ubuntu64_vm_large'] = {
    'name': "Android armv7 API 9",
}
PLATFORMS['android-api-9']['stage_product'] = 'mobile'
PLATFORMS['android-api-9']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': None,
    'talos_script_maxtime': 10800,
}
PLATFORMS['android-api-11']['slave_platforms'] = ['ubuntu64_vm_armv7_mobile', 'ubuntu64_vm_armv7_large']
PLATFORMS['android-api-11']['env_name'] = 'android-perf'
PLATFORMS['android-api-11']['is_mobile'] = True
PLATFORMS['android-api-11']['ubuntu64_vm_armv7_mobile'] = {
    'name': "Android 4.3 armv7 API 11+",
    'mozharness_talos': True,
}
PLATFORMS['android-api-11']['ubuntu64_vm_armv7_large'] = {
    'name': "Android 4.3 armv7 API 11+",
    'mozharness_talos': True,
}
PLATFORMS['android-api-11']['stage_product'] = 'mobile'
PLATFORMS['android-api-11']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': None,
    'talos_script_maxtime': 10800,
}

PLATFORMS['android-api-15']['slave_platforms'] = ['ubuntu64_vm_armv7_mobile', 'ubuntu64_vm_armv7_large']
PLATFORMS['android-api-15']['env_name'] = 'android-perf'
PLATFORMS['android-api-15']['is_mobile'] = True
PLATFORMS['android-api-15']['ubuntu64_vm_armv7_mobile'] = {
    'name': "Android 4.3 armv7 API 15+",
    'mozharness_talos': True,
}
PLATFORMS['android-api-15']['ubuntu64_vm_armv7_large'] = {
    'name': "Android 4.3 armv7 API 15+",
    'mozharness_talos': True,
}
PLATFORMS['android-api-15']['stage_product'] = 'mobile'
PLATFORMS['android-api-15']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': None,
    'talos_script_maxtime': 10800,
}
PLATFORMS['android-x86']['slave_platforms'] = ['ubuntu64_hw']
PLATFORMS['android-x86']['env_name'] = 'android-perf'
PLATFORMS['android-x86']['is_mobile'] = True
PLATFORMS['android-x86']['ubuntu64_hw'] = {'name': "Android 4.2 x86 Emulator"}
PLATFORMS['android-x86']['stage_product'] = 'mobile'
PLATFORMS['android-x86']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

# Lets be explicit instead of magical.
for platform, platform_config in PLATFORMS.iteritems():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform])
        if slave_platform in TRY_SLAVES:
            platform_config[slave_platform]['try_slaves'] = sorted(TRY_SLAVES[slave_platform])
        else:
            platform_config[slave_platform]['try_slaves'] = platform_config[slave_platform]['slaves']

# List of Android platforms that have talos enabled
ANDROID = ["panda_android"]
ANDROID_NOT_PANDA = [slave_plat for slave_plat in ANDROID if 'panda' not in slave_plat]

SUITES = {
    'remote-tsvgx': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvgx', '--noChrome', '--tppagecycles', '10'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tp4m_nochrome': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp4m', '--noChrome', '--rss'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
}

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'android-debug': {},
        'android-api-9': {},
        'android-api-11': {},
        'android-api-15': {},
        'android-x86': {},
    },
}

EMPTY_UNITTEST_DICT = {'opt_unittest_suites': [], 'debug_unittest_suites': []}

ANDROID_2_3_C3_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}

ANDROID_2_3_AWS_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}

ANDROID_4_3_C3_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}

ANDROID_4_3_C3_TRUNK_DICT = {
    'debug_unittest_suites': [],
}

ANDROID_4_3_AWS_TRUNK_DICT = {
    'debug_unittest_suites': [],
}

ANDROID_4_3_AWS_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}

ANDROID_2_3_ARMV6_AWS_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}

ANDROID_2_3_ARMV6_C3_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}

# Beginning Androidx86 configurations
ANDROID_X86_MOZHARNESS_DICT = [
    ('androidx86-set-4', {
        'use_mozharness': True,
        'script_path': 'scripts/androidx86_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidx86.py',
            '--test-suite', 'xpcshell',
        ],
        'trychooser_suites': ['xpcshell'],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
]

ANDROID_X86_NOT_GREEN_DICT = [
    ('androidx86-set-1', {
        'use_mozharness': True,
        'script_path': 'scripts/androidx86_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidx86.py',
            '--test-suite', 'jsreftest',
            '--test-suite', 'mochitest-1',
        ],
        'trychooser_suites': ['mochitest-1', 'jsreftest'],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('androidx86-set-2', {
        'use_mozharness': True,
        'script_path': 'scripts/androidx86_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidx86.py',
            '--test-suite', 'mochitest-2',
            '--test-suite', 'mochitest-gl',
        ],
        'trychooser_suites': ['mochitest-2', 'mochitest-gl'],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('androidx86-set-3', {
        'use_mozharness': True,
        'script_path': 'scripts/androidx86_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidx86.py',
            '--test-suite', 'reftest-1',
            '--test-suite', 'reftest-2',
            '--test-suite', 'reftest-3',
            '--test-suite', 'crashtest',
        ],
        'trychooser_suites': ['plain-reftest-1', 'plain-reftest-2', 'plain-reftest-3', 'crashtest'],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
]

# Funky DICT naming
ANDROID_X86_MOZHARNESS_UNITTEST_DICT = {
    'opt_unittest_suites': ANDROID_X86_MOZHARNESS_DICT,
    'debug_unittest_suites': [],
}
# End of Androidx86 configurations

# Beginning Android 2.3 configurations
ANDROID_2_3_MOZHARNESS_DICT = [
    ('mochitest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-7', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-7',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-8', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-8',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-9', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-9',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-10', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-10',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-11', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-11',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-12', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-12',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-13', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-13',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-14', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-14',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-15', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-15',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-16', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-16',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-chrome',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('robocop-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'robocop-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('robocop-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'robocop-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('robocop-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'robocop-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('robocop-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'robocop-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('xpcshell-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'xpcshell-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('xpcshell-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'xpcshell-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('xpcshell-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'xpcshell-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-gl-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-gl-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-gl-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-gl-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'jsreftest-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'jsreftest-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'jsreftest-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'jsreftest-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'jsreftest-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'jsreftest-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-7', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-7',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-8', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-8',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-9', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-9',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-10', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-10',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-11', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-11',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-12', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-12',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-13', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-13',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-14', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-14',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-15', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-15',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-16', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'reftest-16',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'crashtest-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'crashtest-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
]
# End of Android 2.3 configurations

# Beginning Android 4.3 configurations
ANDROID_4_3_MOZHARNESS_DICT = [
    ('mochitest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-7', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-7',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-8', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-8',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-9', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-9',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-10', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-10',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-11', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-11',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-12', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-12',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-13', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-13',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-14', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-14',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-15', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-15',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-16', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-16',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-17', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-17',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-18', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-18',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-19', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-19',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-20', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-20',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-chrome',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('robocop-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'robocop-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('robocop-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'robocop-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('robocop-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'robocop-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('robocop-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'robocop-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('xpcshell-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'xpcshell-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('xpcshell-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'xpcshell-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('xpcshell-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'xpcshell-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-7', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-7',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-8', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-8',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-9', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-9',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('mochitest-gl-10', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-gl-10',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-7', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-7',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-8', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-8',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-9', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-9',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-10', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-10',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-11', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-11',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-12', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-12',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-13', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-13',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-14', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-14',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-15', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-15',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-16', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-16',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('cppunit', {
      'use_mozharness': True,
      'script_path': 'scripts/android_emulator_unittest.py',
      'extra_args': [
          '--cfg', 'android/androidarm_4_3.py',
          '--test-suite', 'cppunittest',
      ],
      'blob_upload': True,
      'timeout': 2400,
      'script_maxtime': 14400,
      },
     ),
]

ANDROID_4_3_MOZHARNESS_DEBUG_JSREFTEST_TRUNK = [
    ('jsreftest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
   ),
    ('jsreftest-4', {
        'use_mozharness': True,
       'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-5', {
        'use_mozharness': True,
       'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-7', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-7',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-8', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-8',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-9', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-9',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-10', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-10',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-11', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-11',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-12', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-12',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-13', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-13',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-14', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-14',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-15', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-15',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-16', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-16',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-17', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-17',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-18', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-18',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-19', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-19',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('jsreftest-20', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'jsreftest-debug-20',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
]

ANDROID_4_3_MOZHARNESS_DEBUG_REFTEST_TRUNK = [
     ('plain-reftest-1', {
         'use_mozharness': True,
         'script_path': 'scripts/android_emulator_unittest.py',
         'extra_args': [
             '--cfg', 'android/androidarm_4_3.py',
             '--test-suite', 'reftest-debug-1',
         ],
         'blob_upload': True,
         'timeout': 2400,
         'script_maxtime': 14400,
     },
     ),
    ('plain-reftest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
   },
    ),
    ('plain-reftest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-7', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-7',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-8', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-8',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-9', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-9',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-10', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-10',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-11', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-11',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-12', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-12',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-13', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-13',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-14', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-14',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-15', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-15',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-16', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-16',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-17', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
           '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-17',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-18', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-18',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-19', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-19',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-20', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-20',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-21', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-21',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-22', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-22',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-23', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-23',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-24', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-24',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-25', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-25',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-26', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-26',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-27', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-27',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-28', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-28',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-29', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-29',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-30', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-30',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-31', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-31',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-32', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-32',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-33', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-33',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-34', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-34',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-35', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-35',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-36', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-36',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-37', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-37',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-38', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-38',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-39', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-39',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-40', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-40',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-41', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-41',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-42', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-42',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-43', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-43',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-44', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-44',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-45', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-45',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-46', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-46',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-47', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-47',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('plain-reftest-48', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'reftest-debug-48',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
]

ANDROID_4_3_MOZHARNESS_DEBUG_CRASHTEST_TRUNK = [
    ('crashtest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-3',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-4',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-5',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-6', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-6',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-7', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-7',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-8', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-8',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-9', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-9',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
    ('crashtest-10', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'crashtest-debug-10',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
    },
    ),
]

ANDROID_4_3_MOZHARNESS_DEBUG_TRUNK = ANDROID_4_3_MOZHARNESS_DEBUG_JSREFTEST_TRUNK + ANDROID_4_3_MOZHARNESS_DEBUG_REFTEST_TRUNK + ANDROID_4_3_MOZHARNESS_DEBUG_CRASHTEST_TRUNK

# End of Android 4.3 configurations

# bug 1242682 - Enable DOM media Mochitests on Android Fennec
ANDROID_4_3_MOCHITEST_MEDIA = [
    ('mochitest-media-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-media-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
        },
    ),
    ('mochitest-media-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm_4_3.py',
            '--test-suite', 'mochitest-media-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
        },
    ),
]
ANDROID_2_3_MOCHITEST_MEDIA = [
    ('mochitest-media-1', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-media-1',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
        },
    ),
    ('mochitest-media-2', {
        'use_mozharness': True,
        'script_path': 'scripts/android_emulator_unittest.py',
        'extra_args': [
            '--cfg', 'android/androidarm.py',
            '--test-suite', 'mochitest-media-2',
        ],
        'blob_upload': True,
        'timeout': 2400,
        'script_maxtime': 14400,
        },
    ),
]

for suite in ANDROID_2_3_MOZHARNESS_DICT:
    if suite[0].startswith('mochitest-gl'):
        continue
    elif suite[0].startswith('plain-reftest'):
        ANDROID_2_3_ARMV6_C3_DICT['opt_unittest_suites'].append(suite)
    elif suite[0].startswith('crashtest'):
        ANDROID_2_3_ARMV6_C3_DICT['opt_unittest_suites'].append(suite)
    elif suite[0].startswith('jsreftest'):
        ANDROID_2_3_ARMV6_C3_DICT['opt_unittest_suites'].append(suite)
    else:
        ANDROID_2_3_ARMV6_AWS_DICT['opt_unittest_suites'].append(suite)


# You must define opt_unittest_suites when enable_opt_unittests is True for a
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
    'android-api-9': {
        'product_name': 'fennec',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'is_remote': True,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'remote_extras': ANDROID_UNITTEST_REMOTE_EXTRAS,
    },
    'android-api-11': {
        'product_name': 'fennec',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'is_remote': True,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'remote_extras': ANDROID_UNITTEST_REMOTE_EXTRAS,
    },
    'android-api-15': {
        'product_name': 'fennec',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'is_remote': True,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'remote_extras': ANDROID_UNITTEST_REMOTE_EXTRAS,
    },
    'android-x86': {
        'product_name': 'fennec',
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu64_hw': deepcopy(ANDROID_X86_MOZHARNESS_UNITTEST_DICT),
    },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])
    if BRANCHES[branch].get('mobile_platforms'):
        BRANCHES[branch]['platforms'] = deepcopy(BRANCHES[branch]['mobile_platforms'])

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.iteritems():
        # In order to have things ride the trains we need to be able to
        # override "global" things. Therefore, we shouldn't override anything
        # that's already been set.
        if key in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for key, value in BRANCH_UNITTEST_VARS.iteritems():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_UNITTEST_VARS.iteritems():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.iteritems():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Copy in local config
    if branch in localconfig.BRANCHES:
        for key, value in localconfig.BRANCHES[branch].iteritems():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.iteritems():
                    for key, value in platform_config.iteritems():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    # Merge in any project branch config for platforms
    if branch in ACTIVE_PROJECT_BRANCHES and 'mobile_platforms' in PROJECT_BRANCHES[branch]:
        for platform, platform_config in PROJECT_BRANCHES[branch]['mobile_platforms'].iteritems():
            if platform in PLATFORMS:
                for key, value in platform_config.iteritems():
                    value = deepcopy(value)
                    if isinstance(value, str):
                        value = value % locals()
                    BRANCHES[branch]['platforms'][platform][key] = value

    for platform, platform_config in localconfig.PLATFORM_VARS.iteritems():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.iteritems():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value


#
# Entries in BRANCHES for tests should be a tuple of:
# - Number of tests to run per build
# - Whether queue merging is on
# - TalosFactory options
# - Which platforms to run on

BRANCHES['mozilla-release']['enable_talos'] = False

# Let's load the defaults
for branch in BRANCHES.keys():
    loadDefaultValues(BRANCHES, branch, BRANCHES[branch])
    loadCustomTalosSuites(BRANCHES, SUITES, branch, BRANCHES[branch])

# The following are exceptions to the defaults

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['mobile_branch_name'] = "Mobile"
BRANCHES['mozilla-central']['mobile_talos_branch'] = "mobile"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'
BRANCHES['mozilla-central']['pgo_platforms'] = []
BRANCHES['mozilla-central']['platforms']['android-api-15']['enable_debug_unittests'] = True

######### mozilla-release
BRANCHES['mozilla-release']['repo_path'] = "releases/mozilla-release"
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-release']['pgo_platforms'] = []

######### mozilla-beta
BRANCHES['mozilla-beta']['repo_path'] = "releases/mozilla-beta"
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-beta']['pgo_platforms'] = []

######### mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = "releases/mozilla-aurora"
BRANCHES['mozilla-aurora']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-aurora']['pgo_platforms'] = []

######## try
BRANCHES['try']['repo_path'] = "try"
BRANCHES['try']['platforms']['android-api-15']['enable_debug_unittests'] = True
BRANCHES['try']['pgo_strategy'] = 'try'
BRANCHES['try']['pgo_platforms'] = []
BRANCHES['try']['enable_try'] = True

######## cedar
# Until we green out these Android x86 tests
BRANCHES['cedar']['platforms']['android-x86']['ubuntu64_hw']['opt_unittest_suites'] = ANDROID_X86_NOT_GREEN_DICT[:]

#split 2.3 tests to ones that can run on ix and AWS
for suite in ANDROID_2_3_MOZHARNESS_DICT:
    if suite[0].startswith('plain-reftest'):
        ANDROID_2_3_C3_DICT['opt_unittest_suites'].append(suite)
    elif suite[0].startswith('crashtest'):
        ANDROID_2_3_C3_DICT['opt_unittest_suites'].append(suite)
    elif suite[0].startswith('jsreftest'):
        ANDROID_2_3_C3_DICT['opt_unittest_suites'].append(suite)
    else:
        ANDROID_2_3_AWS_DICT['opt_unittest_suites'].append(suite)

#split 4.3 opt and debug tests to ones that can run on C3 vs less powerful instances
for suite in ANDROID_4_3_MOZHARNESS_DICT:
    if suite[0].startswith('plain-reftest'):
        ANDROID_4_3_C3_DICT['opt_unittest_suites'].append(suite)
        ANDROID_4_3_C3_DICT['debug_unittest_suites'].append(suite)
    elif re.match(r"^mochitest-\d", suite[0]):
        ANDROID_4_3_C3_DICT['opt_unittest_suites'].append(suite)
        ANDROID_4_3_C3_DICT['debug_unittest_suites'].append(suite)
        ANDROID_4_3_C3_TRUNK_DICT['debug_unittest_suites'].append(suite)
    elif suite[0].startswith('mochitest'):
        ANDROID_4_3_AWS_DICT['opt_unittest_suites'].append(suite)
        ANDROID_4_3_C3_DICT['debug_unittest_suites'].append(suite)
        ANDROID_4_3_C3_TRUNK_DICT['debug_unittest_suites'].append(suite)
    elif suite[0].startswith('xpcshell'):
        ANDROID_4_3_AWS_DICT['opt_unittest_suites'].append(suite)
        ANDROID_4_3_C3_DICT['debug_unittest_suites'].append(suite)
        ANDROID_4_3_C3_TRUNK_DICT['debug_unittest_suites'].append(suite)
    elif suite[0].startswith('crashtest'):
        ANDROID_4_3_C3_DICT['opt_unittest_suites'].append(suite)
        ANDROID_4_3_C3_DICT['debug_unittest_suites'].append(suite)
    elif suite[0].startswith('jsreftest'):
        ANDROID_4_3_C3_DICT['opt_unittest_suites'].append(suite)
        ANDROID_4_3_C3_DICT['debug_unittest_suites'].append(suite)
    else:
        ANDROID_4_3_AWS_DICT['opt_unittest_suites'].append(suite)
        if suite[0].startswith('robocop'):
            continue
        else:
            ANDROID_4_3_AWS_DICT['debug_unittest_suites'].append(suite)
        if suite[0].startswith('cppunit'):
            ANDROID_4_3_AWS_TRUNK_DICT['debug_unittest_suites'].append(suite)

# Bug 1219094 - releng work for dropping honeycomb support
for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
    # remove the soon to be replaced android builds
    if 'android-api-11' in branch['platforms']:
        del branch['platforms']['android-api-11']
for name, branch in items_before(BRANCHES, 'gecko_version', 46):
    if 'android-api-15' in branch['platforms']:
        del branch['platforms']['android-api-15']

# enable android 2.3 tests to ride the trains bug 1004791
for name, branch in items_at_least(BRANCHES, 'gecko_version', 32):
    # Loop removes it from any branch that gets beyond here
    for platform in branch['platforms']:
        if not platform in PLATFORMS:
            continue
        if platform not in ('android-api-9'):
            continue
        BRANCHES[name]['platforms'][platform]['ubuntu64_vm_large'] = {
            'opt_unittest_suites': deepcopy(ANDROID_2_3_C3_DICT['opt_unittest_suites']),
            'debug_unittest_suites': []
        }
        BRANCHES[name]['platforms'][platform]['ubuntu64_vm_mobile'] = {
            'opt_unittest_suites': deepcopy(ANDROID_2_3_AWS_DICT['opt_unittest_suites']),
            'debug_unittest_suites': []
        }

# enable android 2.3 mochitest media to ride the trains (bug 1242682)
for name, branch in items_at_least(BRANCHES, 'gecko_version', 48):
    # Loop removes it from any branch that gets beyond here
    for platform in branch['platforms']:
        if not platform in PLATFORMS:
            continue
        if platform not in ('android-api-9'):
            continue
        BRANCHES[name]['platforms'][platform]['ubuntu64_vm_large'] = {
            'opt_unittest_suites': deepcopy(ANDROID_2_3_C3_DICT['opt_unittest_suites']),
            'debug_unittest_suites': []
        }
        BRANCHES[name]['platforms'][platform]['ubuntu64_vm_mobile'] = {
            'opt_unittest_suites': deepcopy(ANDROID_2_3_AWS_DICT['opt_unittest_suites']),
            'debug_unittest_suites': []
        }
        BRANCHES[name]['platforms'][platform]['ubuntu64_vm_mobile']['opt_unittest_suites'] += ANDROID_2_3_MOCHITEST_MEDIA


# bug 1133833 enable Android 4.3 on trunk for opt only
# while disabling corresponding 4.0 tests
for name, branch in items_at_least(BRANCHES, 'gecko_version', 40):
    # Loop removes it from any branch that gets beyond here
    for platform in branch['platforms']:
        if not platform in PLATFORMS:
            continue
        if platform not in ('android-api-11', 'android-api-15'):
            continue
        for slave_plat in PLATFORMS[platform]['slave_platforms']:
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_mobile'] = {
            'opt_unittest_suites': deepcopy(ANDROID_4_3_AWS_DICT['opt_unittest_suites']),
            'debug_unittest_suites': [],}
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_large'] = {
            'opt_unittest_suites': deepcopy(ANDROID_4_3_C3_DICT['opt_unittest_suites']),
            'debug_unittest_suites': [],}

for name, branch in items_at_least(BRANCHES, 'gecko_version', 41):
    if name in ('cedar' ):
       continue
    for platform in branch['platforms']:
        if not platform in PLATFORMS:
            continue
        if platform not in ('android-api-11', 'android-api-15'):
            continue
        for slave_plat in PLATFORMS[platform]['slave_platforms']:
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_large'] = {
            'opt_unittest_suites': deepcopy(ANDROID_4_3_C3_DICT['opt_unittest_suites']),
            'debug_unittest_suites': deepcopy(ANDROID_4_3_C3_TRUNK_DICT['debug_unittest_suites']),}
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_mobile'] = {
                'opt_unittest_suites': deepcopy(ANDROID_4_3_AWS_DICT['opt_unittest_suites']),
                'debug_unittest_suites': deepcopy(ANDROID_4_3_AWS_TRUNK_DICT['debug_unittest_suites']),
            }

# bug 1183877 Increase total-chunks for Android 4.3 Debug crashtests, js-reftests, and reftests
for name, branch in items_at_least(BRANCHES, 'gecko_version', 44):
    for platform in branch['platforms']:
        if not platform in PLATFORMS:
            continue
        if platform not in ('android-api-11', 'android-api-15'):
            continue
        for slave_plat in PLATFORMS[platform]['slave_platforms']:
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_large'] = {
            'opt_unittest_suites': deepcopy(ANDROID_4_3_C3_DICT['opt_unittest_suites']),
            'debug_unittest_suites': deepcopy(ANDROID_4_3_C3_TRUNK_DICT['debug_unittest_suites'] + ANDROID_4_3_MOZHARNESS_DEBUG_TRUNK),}
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_mobile'] = {
                'opt_unittest_suites': deepcopy(ANDROID_4_3_AWS_DICT['opt_unittest_suites']),
                'debug_unittest_suites': deepcopy(ANDROID_4_3_AWS_TRUNK_DICT['debug_unittest_suites']),
            }

# bug 1242682 add mochitest-media
for name, branch in items_at_least(BRANCHES, 'gecko_version', 48):
    for platform in branch['platforms']:
        if not platform in PLATFORMS:
            continue
        if platform not in ('android-api-11', 'android-api-15'):
            continue
        for slave_plat in PLATFORMS[platform]['slave_platforms']:
            if not slave_plat in branch['platforms'][platform]:
                continue
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_large'] = {
            'opt_unittest_suites': deepcopy(ANDROID_4_3_C3_DICT['opt_unittest_suites']),
            'debug_unittest_suites': deepcopy(ANDROID_4_3_C3_TRUNK_DICT['debug_unittest_suites'] + ANDROID_4_3_MOZHARNESS_DEBUG_TRUNK),}
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_mobile'] = {
                'opt_unittest_suites': deepcopy(ANDROID_4_3_AWS_DICT['opt_unittest_suites']),
                'debug_unittest_suites': deepcopy(ANDROID_4_3_AWS_TRUNK_DICT['debug_unittest_suites']),
            }
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_large']['opt_unittest_suites'] += ANDROID_4_3_MOCHITEST_MEDIA
            BRANCHES[name]['platforms'][platform]['ubuntu64_vm_armv7_large']['debug_unittest_suites'] += ANDROID_4_3_MOCHITEST_MEDIA

# Bug 1250999 - releng - releng work for dropping api 9-10
# disable api-9-10 mobile builds on >= 48 based branches
for name, branch in items_at_least(BRANCHES, 'gecko_version', 48):
    if 'android-api-9' in branch['platforms']:
        del branch['platforms']['android-api-9']

def remove_suite_from_slave_platform(BRANCHES, PLATFORMS, suite_to_remove, slave_platform, branches_to_keep=[]):
    """Remove suites named like |suite_to_remove| from all branches on slave platforms named like |slave_platform|.

Updates BRANCHES in place.  Consumes PLATFORMS without side
effects. Does not remove any suites from the specified
|branches_to_keep|."""

    for branch in BRANCHES:
        # Loop removes it from any branch that gets beyond here.
        if branch in branches_to_keep:
            continue
        for platform in BRANCHES[branch]['platforms']:
            if not platform in PLATFORMS:
                continue
            if not platform.startswith('android'):
                continue
            if platform.endswith('-debug'):
                continue  # no slave_platform for debug
            for slave_plat in PLATFORMS[platform]['slave_platforms']:
                if not slave_plat in BRANCHES[branch]['platforms'][platform]:
                    continue
                if not slave_plat == slave_platform:
                    continue
                for unittest_suite_type, unittest_suites in BRANCHES[branch]['platforms'][platform][slave_plat].iteritems():
                    # This replaces the contents of the unittest_suites list in place with the filtered list.
                    unittest_suites[:] = [ suite for suite in unittest_suites if not suite_to_remove in suite[0] ]

# Bug 1182691 - Run Android 2.3 and Android 4.3 mochitest-chrome on trunk
trunk_branches = []
for name, branch in items_at_least(BRANCHES, 'gecko_version', 42):
    trunk_branches.append(name)

remove_suite_from_slave_platform(BRANCHES, PLATFORMS, 'mochitest-chrome', 'ubuntu64_vm_armv7_mobile', branches_to_keep=trunk_branches)
remove_suite_from_slave_platform(BRANCHES, PLATFORMS, 'mochitest-chrome', 'ubuntu64_vm_armv7_large', branches_to_keep=trunk_branches)
remove_suite_from_slave_platform(BRANCHES, PLATFORMS, 'mochitest-chrome', 'ubuntu64_vm_mobile', branches_to_keep=trunk_branches)
remove_suite_from_slave_platform(BRANCHES, PLATFORMS, 'mochitest-chrome', 'ubuntu64_vm_large', branches_to_keep=trunk_branches)

loadSkipConfig(BRANCHES, "mobile")

if __name__ == "__main__":
    import sys
    import pprint

    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = dict(BRANCHES.iteritems())

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)

    for suite in sorted(SUITES):
        out = pprint.pformat(SUITES[suite])
        for l in out.splitlines():
            print '%s: %s' % (suite, l)
