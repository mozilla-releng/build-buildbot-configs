from copy import deepcopy

from config import MOZHARNESS_REBOOT_CMD
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS

import b2g_localconfig
reload(b2g_localconfig)
import config_common
reload(config_common)
from config_common import nested_haskey

GLOBAL_VARS = deepcopy(GLOBAL_VARS)

GLOBAL_VARS['stage_username'] = 'ffxbld'
GLOBAL_VARS.update(b2g_localconfig.GLOBAL_VARS.copy())

BRANCHES = {
    'ash': {},
    'birch': {},
    'cedar': {},
    'cypress': {},
    'fx-team': {},
    'graphics': {},
    'mozilla-b2g18': {},
    'mozilla-b2g18_v1_0_1': {},
    'mozilla-b2g18_v1_1_0_hd': {},
    'mozilla-central': {},
    'mozilla-inbound': {},
    'b2g-inbound': {},
    'services-central': {},
    'ionmonkey': {},
    'try': {'coallesce_jobs': False},
}

PLATFORMS = {
    'ics_armv7a_gecko': {},
    'linux32_gecko': {},
    'linux64_gecko': {},
    'emulator': {},
}

builder_prefix = "b2g"

PLATFORMS['ics_armv7a_gecko']['slave_platforms'] = ['fedora-b2g', 'ubuntu64_vm-b2g', 'ubuntu64_hw-b2g']
PLATFORMS['ics_armv7a_gecko']['env_name'] = 'linux-perf'
PLATFORMS['ics_armv7a_gecko']['fedora-b2g'] = {'name': builder_prefix + "_ics_armv7a_gecko_emulator"}
PLATFORMS['ics_armv7a_gecko']['ubuntu64_vm-b2g'] = {'name': builder_prefix + "_ics_armv7a_gecko_emulator_vm"}
PLATFORMS['ics_armv7a_gecko']['ubuntu64_hw-b2g'] = {'name': builder_prefix + "_ics_armv7a_gecko_emulator_hw"}
PLATFORMS['ics_armv7a_gecko']['stage_product'] = 'b2g'
PLATFORMS['ics_armv7a_gecko']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'use_mozharness': True,
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

PLATFORMS['linux32_gecko']['slave_platforms'] = ['ubuntu32_vm-b2gdt', ]
PLATFORMS['linux32_gecko']['env_name'] = 'linux-perf'
PLATFORMS['linux32_gecko']['ubuntu32_vm-b2gdt'] = {'name': builder_prefix + "_ubuntu32_vm"}
PLATFORMS['linux32_gecko']['stage_product'] = 'b2g'
PLATFORMS['linux32_gecko']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'use_mozharness': True,
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

PLATFORMS['linux64_gecko']['slave_platforms'] = ['ubuntu64_vm-b2gdt', ]
PLATFORMS['linux64_gecko']['env_name'] = 'linux-perf'
PLATFORMS['linux64_gecko']['ubuntu64_vm-b2gdt'] = {'name': builder_prefix + "_ubuntu64_vm"}
PLATFORMS['linux64_gecko']['stage_product'] = 'b2g'
PLATFORMS['linux64_gecko']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'use_mozharness': True,
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

PLATFORMS['emulator']['slave_platforms'] = ['fedora-b2g-emulator', 'ubuntu64_vm-b2g-emulator', 'ubuntu64_hw-b2g-emulator']
PLATFORMS['emulator']['env_name'] = 'linux-perf'
PLATFORMS['emulator']['fedora-b2g-emulator'] = {'name': "b2g_emulator"}
PLATFORMS['emulator']['ubuntu64_vm-b2g-emulator'] = {'name': "b2g_emulator_vm"}
PLATFORMS['emulator']['ubuntu64_hw-b2g-emulator'] = {'name': "b2g_emulator_hw"}
PLATFORMS['emulator']['stage_product'] = 'b2g'
PLATFORMS['emulator']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'use_mozharness': True,
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

# Lets be explicit instead of magical.
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform])
        if slave_platform in TRY_SLAVES:
            platform_config[slave_platform]['try_slaves'] = sorted(TRY_SLAVES[slave_platform])
        else:
            platform_config[slave_platform]['try_slaves'] = platform_config[slave_platform]['slaves']

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'ics_armv7a_gecko': {},
        'linux32_gecko': {},
        'linux64_gecko': {},
        'emulator': {},
    },
}

SUITES = {}

MOCHITEST = [
    ('mochitest-1', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('mochitest-2', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('mochitest-3', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('mochitest-4', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('mochitest-5', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('mochitest-6', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('mochitest-7', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('mochitest-8', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('mochitest-9', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
]
REFTEST = [
    ('reftest-1', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-2', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-3', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-4', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-5', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-6', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-7', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-8', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-9', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   },
     ),
    ('reftest-10', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    },
     ),
]

REFTEST_SANITY = [
    ('reftest', {'suite': 'reftest',
                 'use_mozharness': True,
                 'script_path': 'scripts/b2g_emulator_unittest.py',
                 },
     ),
]

CRASHTEST = [
    ('crashtest-1', {'suite': 'crashtest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('crashtest-2', {'suite': 'crashtest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
    ('crashtest-3', {'suite': 'crashtest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     },
     ),
]

MARIONETTE = [
    ('marionette-webapi', {'suite': 'marionette-webapi',
                           'use_mozharness': True,
                           'script_path': 'scripts/marionette.py',
                           },
     ),
]

XPCSHELL = [
    ('xpcshell', {'suite': 'xpcshell',
                  'use_mozharness': True,
                  'script_path': 'scripts/b2g_emulator_unittest.py',
                  },
     ),
]

GAIA_UNITTESTS = [(
    'gaia-unit', {
        'suite': 'gaia-unit',
        'use_mozharness': True,
        'script_path': 'scripts/gaia_unit.py',
    },
)]

GAIA_UI = [(
    'gaia-ui-test', {
        'suite': 'gaia-ui-test',
        'use_mozharness': True,
        'script_path': 'scripts/marionette.py',
    },
)]

ALL_UNITTESTS = MOCHITEST + REFTEST + CRASHTEST + MARIONETTE + XPCSHELL

# Default set of unit tests
UNITTEST_SUITES = {
    'opt_unittest_suites': ALL_UNITTESTS[:],
    'debug_unittest_suites': [],
}

# You must define opt_unittest_suites when enable_opt_unittests is True for a
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
    'ics_armv7a_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'fedora-b2g': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'crashtest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '1', '--total-chunks', '3',
                    ],
                },
                'crashtest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '2', '--total-chunks', '3',
                    ],
                },
                'crashtest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '3', '--total-chunks', '3',
                    ],
                },
                'marionette-webapi': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py"
                    ],
                },
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '1', '--total-chunks', '9',
                    ],
                },
                'mochitest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '2', '--total-chunks', '9',
                    ],
                },
                'mochitest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '3', '--total-chunks', '9',
                    ],
                },
                'mochitest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '4', '--total-chunks', '9',
                    ],
                },
                'mochitest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '5', '--total-chunks', '9',
                    ],
                },
                'mochitest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '6', '--total-chunks', '9',
                    ],
                },
                'mochitest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '7', '--total-chunks', '9',
                    ],
                },
                'mochitest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '8', '--total-chunks', '9',
                    ],
                },
                'mochitest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '9', '--total-chunks', '9',
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '1', '--total-chunks', '10',
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '2', '--total-chunks', '10',
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '3', '--total-chunks', '10',
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '4', '--total-chunks', '10',
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '5', '--total-chunks', '10',
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '6', '--total-chunks', '10',
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '7', '--total-chunks', '10',
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '8', '--total-chunks', '10',
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '9', '--total-chunks', '10',
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '10', '--total-chunks', '10',
                    ],
                },
                'xpcshell': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                    ],
                },
            },
        },
        'ubuntu64_vm-b2g': {
            'opt_unittest_suites': MOCHITEST + MARIONETTE + XPCSHELL + CRASHTEST,
            'debug_unittest_suites': MOCHITEST + MARIONETTE + XPCSHELL + CRASHTEST,
            'suite_config': {
                'marionette-webapi': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py"
                    ],
                },
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '1', '--total-chunks', '9',
                    ],
                },
                'mochitest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '2', '--total-chunks', '9',
                    ],
                },
                'mochitest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '3', '--total-chunks', '9',
                    ],
                },
                'mochitest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '4', '--total-chunks', '9',
                    ],
                },
                'mochitest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '5', '--total-chunks', '9',
                    ],
                },
                'mochitest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '6', '--total-chunks', '9',
                    ],
                },
                'mochitest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '7', '--total-chunks', '9',
                    ],
                },
                'mochitest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '8', '--total-chunks', '9',
                    ],
                },
                'mochitest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '9', '--total-chunks', '9',
                    ],
                },
                'xpcshell': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                    ],
                },
                'crashtest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '1', '--total-chunks', '3',
                    ],
                },
                'crashtest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '2', '--total-chunks', '3',
                    ],
                },
                'crashtest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '3', '--total-chunks', '3',
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '1', '--total-chunks', '10',
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '2', '--total-chunks', '10',
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '3', '--total-chunks', '10',
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '4', '--total-chunks', '10',
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '5', '--total-chunks', '10',
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '6', '--total-chunks', '10',
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '7', '--total-chunks', '10',
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '8', '--total-chunks', '10',
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '9', '--total-chunks', '10',
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '10', '--total-chunks', '10',
                    ],
                },
            },
        },
        'ubuntu64_hw-b2g': {
            'opt_unittest_suites': REFTEST,
            'debug_unittest_suites': REFTEST,
            'suite_config': {
                'crashtest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '1', '--total-chunks', '3',
                    ],
                },
                'crashtest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '2', '--total-chunks', '3',
                    ],
                },
                'crashtest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '3', '--total-chunks', '3',
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '1', '--total-chunks', '10',
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '2', '--total-chunks', '10',
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '3', '--total-chunks', '10',
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '4', '--total-chunks', '10',
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '5', '--total-chunks', '10',
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '6', '--total-chunks', '10',
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '7', '--total-chunks', '10',
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '8', '--total-chunks', '10',
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '9', '--total-chunks', '10',
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '10', '--total-chunks', '10',
                    ],
                },
            },
        },
    },  # end of ics_armv7a_gecko configs
    'linux32_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu32_vm-b2gdt': {
            'opt_unittest_suites': GAIA_UI[:],
            'debug_unittest_suites': [],
            'suite_config': {
                'gaia-unit': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_unit_production_config.py',
                    ],
                },
                'gaia-ui-test': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                    ],
                },
            },
        },
    },
    'linux64_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu64_vm-b2gdt': {
            'opt_unittest_suites': GAIA_UNITTESTS[:],
            'debug_unittest_suites': [],
            'suite_config': {
                'gaia-unit': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_unit_production_config.py',
                    ],
                },
                'gaia-ui-test': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                    ],
                },
            },
        },
    },
    'emulator': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'fedora-b2g-emulator': {
            'opt_unittest_suites': REFTEST + MARIONETTE,
            'debug_unittest_suites': [],
            'suite_config': {
                'crashtest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '1', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'crashtest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '2', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'crashtest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '3', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'marionette-webapi': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py",
                        '--no-update',
                    ],
                },
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '1', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '2', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '3', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '4', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '5', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '6', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '7', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '8', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '9', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                        '--no-update',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '1', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '2', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '3', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '4', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '5', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '6', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '7', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '8', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '9', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '10', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'xpcshell': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                        '--no-update',
                    ],
                },
            },
        },
        'ubuntu64_vm-b2g-emulator': {
            'opt_unittest_suites': MOCHITEST + CRASHTEST + XPCSHELL,
            'debug_unittest_suites': [],
            'suite_config': {
                'marionette-webapi': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py",
                        '--no-update',
                    ],
                },
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '1', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '2', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '3', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '4', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '5', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '6', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '7', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '8', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'mochitest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '9', '--total-chunks', '9',
                        '--no-update',
                    ],
                },
                'xpcshell': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                        '--no-update',
                    ],
                },
                'crashtest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '1', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'crashtest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '2', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'crashtest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '3', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                        '--no-update',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '1', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '2', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '3', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '4', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '5', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '6', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '7', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '8', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '9', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '10', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
            },
        },
        'ubuntu64_hw-b2g-dt': {
            'opt_unittest_suites': REFTEST,
            'debug_unittest_suites': REFTEST,
            'suite_config': {
                'crashtest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '1', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'crashtest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '2', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'crashtest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'crashtest',
                        '--this-chunk', '3', '--total-chunks', '3',
                        '--no-update',
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                        '--no-update',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '1', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '2', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '3', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '4', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '5', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '6', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '7', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '8', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '9', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '10', '--total-chunks', '10',
                        '--no-update',
                    ],
                },
            },
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
    if branch in b2g_localconfig.BRANCHES:
        for key, value in b2g_localconfig.BRANCHES[branch].items():
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

    for platform, platform_config in b2g_localconfig.PLATFORM_VARS.items():
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

BRANCHES['ash']['branch_name'] = "Ash"
BRANCHES['ash']['repo_path'] = "projects/ash"
BRANCHES['ash']['mozharness_repo'] = "http://hg.mozilla.org/users/asasaki_mozilla.com/ash-mozharness"
BRANCHES['ash']['mozharness_tag'] = "default"
BRANCHES['ash']['platforms']['ics_armv7a_gecko']['fedora-b2g']['debug_unittest_suites'] = ALL_UNITTESTS[:]
BRANCHES['ash']['platforms']['ics_armv7a_gecko']['enable_debug_unittests'] = True
BRANCHES['birch']['branch_name'] = "Birch"
BRANCHES['birch']['repo_path'] = "projects/birch"
BRANCHES['cedar']['branch_name'] = "Cedar"
BRANCHES['cedar']['repo_path'] = "projects/cedar"
BRANCHES['cedar']['mozharness_tag'] = "default"
BRANCHES['cedar']['platforms']['ics_armv7a_gecko']['fedora-b2g']['debug_unittest_suites'] = ALL_UNITTESTS[:]
BRANCHES['cedar']['platforms']['ics_armv7a_gecko']['ubuntu64_vm-b2g']['debug_unittest_suites'] = ALL_UNITTESTS[:]
BRANCHES['cedar']['platforms']['ics_armv7a_gecko']['enable_debug_unittests'] = True
BRANCHES['cedar']['platforms']['ics_armv7a_gecko']['slave_platforms'] = ['fedora-b2g', 'ubuntu64_vm-b2g', 'ubuntu64_hw-b2g']
BRANCHES['cedar']['platforms']['emulator']['fedora-b2g-emulator']['opt_unittest_suites'] = ALL_UNITTESTS[:]
BRANCHES['cedar']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] = MOCHITEST + CRASHTEST + MARIONETTE + XPCSHELL
BRANCHES['cedar']['platforms']['emulator']['fedora-b2g-emulator']['debug_unittest_suites'] = ALL_UNITTESTS[:]
BRANCHES['cedar']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['debug_unittest_suites'] = ALL_UNITTESTS[:]
BRANCHES['cedar']['platforms']['emulator']['enable_debug_unittests'] = True
BRANCHES['cedar']['platforms']['linux64_gecko']['ubuntu64_vm-b2gdt']['opt_unittest_suites'] = GAIA_UNITTESTS[:] + GAIA_UI[:]
BRANCHES['cypress']['branch_name'] = "Cypress"
BRANCHES['cypress']['repo_path'] = "projects/cypress"
BRANCHES['fx-team']['repo_path'] = "integration/fx-team"
BRANCHES['graphics']['repo_path'] = "projects/graphics"
BRANCHES['ionmonkey']['repo_path'] = "projects/ionmonkey"
BRANCHES['mozilla-b2g18']['repo_path'] = "releases/mozilla-b2g18"
BRANCHES['mozilla-b2g18']['platforms']['ics_armv7a_gecko']['fedora-b2g']['opt_unittest_suites'] = [x for x in ALL_UNITTESTS if x not in REFTEST] + REFTEST_SANITY
BRANCHES['mozilla-b2g18']['platforms']['ics_armv7a_gecko']['fedora-b2g']['debug_unittest_suites'] = MOCHITEST + XPCSHELL
BRANCHES['mozilla-b2g18']['platforms']['ics_armv7a_gecko']['enable_debug_unittests'] = True
BRANCHES['mozilla-b2g18_v1_0_1']['repo_path'] = "releases/mozilla-b2g18_v1_0_1"
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['ics_armv7a_gecko']['fedora-b2g']['opt_unittest_suites'] = [x for x in ALL_UNITTESTS if x not in CRASHTEST + REFTEST] + REFTEST_SANITY
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['ics_armv7a_gecko']['fedora-b2g']['debug_unittest_suites'] = MOCHITEST + XPCSHELL
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['ics_armv7a_gecko']['enable_debug_unittests'] = True
BRANCHES['mozilla-b2g18_v1_1_0_hd']['repo_path'] = "releases/mozilla-b2g18_v1_1_0_hd"
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['ics_armv7a_gecko']['fedora-b2g']['opt_unittest_suites'] = [x for x in ALL_UNITTESTS if x not in REFTEST] + REFTEST_SANITY
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['ics_armv7a_gecko']['fedora-b2g']['debug_unittest_suites'] = MOCHITEST + XPCSHELL
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['ics_armv7a_gecko']['enable_debug_unittests'] = True
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-inbound']['repo_path'] = "integration/mozilla-inbound"
BRANCHES['b2g-inbound']['repo_path'] = "integration/b2g-inbound"
BRANCHES['services-central']['repo_path'] = "services/services-central"
BRANCHES['try']['pgo_strategy'] = "try"
BRANCHES['try']['enable_try'] = True

# explicitly set slave platforms per branch
for branch in BRANCHES.keys():
    for platform in BRANCHES[branch]['platforms']:
        if 'slave_platforms' not in BRANCHES[branch]['platforms'][platform]:
            BRANCHES[branch]['platforms'][platform]['slave_platforms'] = list(PLATFORMS[platform]['slave_platforms'])

# MERGE DAY NOTE: remove v22 based branches from the list below
NON_UBUNTU_BRANCHES = ("mozilla-b2g18", "mozilla-b2g18_v1_0_1", "mozilla-b2g18_v1_1_0_hd")

# use either Fedora or Ubuntu for other branches,
# don't touch cedar
for branch in set(BRANCHES.keys()) - set(['cedar']):
    if branch in NON_UBUNTU_BRANCHES:
        # Remove Ubuntu completely
        for platform in BRANCHES[branch]['platforms']:
            if 'ubuntu64_vm-b2g' in BRANCHES[branch]['platforms'][platform]['slave_platforms']:
                BRANCHES[branch]['platforms'][platform]['slave_platforms'].remove('ubuntu64_vm-b2g')
            if 'ubuntu64_vm-b2g' in BRANCHES[branch]['platforms'][platform]:
                del BRANCHES[branch]['platforms'][platform]['ubuntu64_vm-b2g']
        continue

    for suite_type in ('opt_unittest_suites', 'debug_unittest_suites'):
        if nested_haskey(BRANCHES[branch]['platforms'], 'ics_armv7a_gecko',
                         'ubuntu64_vm-b2g', suite_type) and \
            nested_haskey(BRANCHES[branch]['platforms'], 'ics_armv7a_gecko',
                          'fedora-b2g', suite_type):
            # Don't run tests on Fedora if they listed in Ubuntu
            for suite in BRANCHES[branch]['platforms']['ics_armv7a_gecko']['ubuntu64_vm-b2g'][suite_type]:
                BRANCHES[branch]['platforms']['ics_armv7a_gecko']['fedora-b2g'][suite_type] = \
                    [s for s in deepcopy(BRANCHES[branch]['platforms']['ics_armv7a_gecko']['fedora-b2g'][suite_type]) if s[0] != suite[0]]

# Disable ubuntu64_hw-b2g on all branches but cedar
for branch in set(BRANCHES.keys()) - set(['cedar']):
    for platform in BRANCHES[branch]['platforms']:
        if 'ubuntu64_hw-b2g' in BRANCHES[branch]['platforms'][platform]['slave_platforms']:
            BRANCHES[branch]['platforms'][platform]['slave_platforms'].remove('ubuntu64_hw-b2g')
        if 'ubuntu64_hw-b2g' in BRANCHES[branch]['platforms'][platform]:
            del BRANCHES[branch]['platforms'][platform]['ubuntu64_hw-b2g']

# Disable linux32_gecko on all branches but cedar
for branch in set(BRANCHES.keys()) - set(['cedar']):
    for platform in ('linux32_gecko',):
        if platform not in BRANCHES[branch]['platforms']:
            continue
        del BRANCHES[branch]['platforms'][platform]

# emulator hacks.  See bug 885456
# MERGE DAY This will someday ride trains...
for branch in BRANCHES.keys():
    if branch in ('mozilla-aurora', 'mozilla-beta', 'mozilla-release',
                  'mozilla-esr17', 'mozilla-b2g18_v1_0_0',
                  'mozilla-b2g18_v1_0_1', 'mozilla-b2g18_v1_1_0_hd'):
        if 'emulator' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['emulator']
    elif branch not in ('mozilla-b2g18', ):
        if 'ics_armv7a_gecko' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['ics_armv7a_gecko']

# linux64_gecko hacks.  See bug 891973
# MERGE DAY This will someday ride trains...
for branch in BRANCHES.keys():
    if branch in ('mozilla-aurora', 'mozilla-beta', 'mozilla-release',
                  'mozilla-esr17', 'mozilla-b2g18', 'mozilla-b2g18_v1_0_0',
                  'mozilla-b2g18_v1_0_1', 'mozilla-b2g18_v1_1_0_hd'):
        if 'linux64_gecko' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['linux64_gecko']


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
