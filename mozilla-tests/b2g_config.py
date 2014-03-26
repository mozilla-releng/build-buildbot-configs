from copy import deepcopy

from config import MOZHARNESS_REBOOT_CMD
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS

import b2g_localconfig
reload(b2g_localconfig)

import master_common
reload(master_common)
from master_common import setMainFirefoxVersions, items_before, items_at_least

import config_common
reload(config_common)
from config_common import nested_haskey

GLOBAL_VARS = deepcopy(GLOBAL_VARS)

GLOBAL_VARS['stage_username'] = 'ffxbld'
GLOBAL_VARS.update(b2g_localconfig.GLOBAL_VARS.copy())

BRANCHES = {
    'ash': {},
    # Not needed right now, see bug 977420
    #'birch': {},
    'cedar': {},
    'cypress': {},
    'elm': {},
    'pine': {},
    'fx-team': {},
    'graphics': {},
    'mozilla-b2g18': {
        'gecko_version': 18,
        'b2g_version': (1, 1, 0),
    },
    'mozilla-b2g18_v1_1_0_hd': {
        'gecko_version': 18,
        'b2g_version': (1, 1, 1),
    },
    'mozilla-b2g26_v1_2': {
        'gecko_version': 26,
        'b2g_version': (1, 2, 0),
    },
    'mozilla-b2g28_v1_3': {
        'gecko_version': 28,
        'b2g_version': (1, 3, 0),
    },
    'mozilla-b2g28_v1_3t': {
        'gecko_version': 28,
        'b2g_version': (1, 3, 0),
    },
    'mozilla-aurora': {
        'gecko_version': 30,
        'b2g_version': (1, 4, 0),
    },
    'mozilla-central': {},
    'mozilla-inbound': {},
    'b2g-inbound': {},
    'services-central': {},
    'ionmonkey': {},
    'try': {'coallesce_jobs': False},
}

setMainFirefoxVersions(BRANCHES)

PLATFORMS = {
    'linux32_gecko': {},
    'linux64_gecko': {},
    'macosx64_gecko': {},
    'emulator': {},
    'emulator-jb': {},
}

builder_prefix = "b2g"

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

PLATFORMS['macosx64_gecko']['slave_platforms'] = ['mountainlion-b2gdt', ]
PLATFORMS['macosx64_gecko']['env_name'] = 'linux-perf'
PLATFORMS['macosx64_gecko']['mountainlion-b2gdt'] = {'name': builder_prefix + "_macosx64"}
PLATFORMS['macosx64_gecko']['stage_product'] = 'b2g'
PLATFORMS['macosx64_gecko']['mozharness_config'] = {
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

PLATFORMS['emulator-jb']['slave_platforms'] = ['ubuntu64_vm-b2g-emulator-jb']
PLATFORMS['emulator-jb']['env_name'] = 'linux-perf'
PLATFORMS['emulator-jb']['ubuntu64_vm-b2g-emulator-jb'] = {'name': "b2g_emulator-jb_vm"}
PLATFORMS['emulator-jb']['stage_product'] = 'b2g'
PLATFORMS['emulator-jb']['mozharness_config'] = {
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
        'linux32_gecko': {},
        'linux64_gecko': {},
        'macosx64_gecko': {},
        'emulator': {},
        'emulator-jb': {},
    },
}

SUITES = {}

MOCHITEST = [
    ('mochitest-1', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('mochitest-2', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('mochitest-3', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('mochitest-4', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('mochitest-5', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('mochitest-6', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('mochitest-7', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('mochitest-8', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('mochitest-9', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
]

MOCHITEST_EMULATOR_JB = [
    ('mochitest-1', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
]

MOCHITEST_EMULATOR_DEBUG = [
    ('mochitest-debug-1', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-2', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-3', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-4', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-5', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-6', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-7', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-8', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-9', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           },
     ),
    ('mochitest-debug-10', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-11', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-12', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-13', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-14', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-15', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
]

MOCHITEST_DESKTOP = [
    ('mochitest-1', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_desktop_unittest.py',
                     'blob_upload': True,
                     },
     ),
]

REFTEST = [
    ('reftest-1', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-2', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-3', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-4', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-5', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-6', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-7', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-8', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-9', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_emulator_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-10', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
]

REFTEST_15=REFTEST[:]
REFTEST_15+=[ \
    ('reftest-11', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('reftest-12', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('reftest-13', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('reftest-14', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('reftest-15', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
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

REFTEST_DESKTOP = [
    ('reftest-1', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-2', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-3', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-4', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-5', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-6', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-7', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-8', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-9', {'suite': 'reftest',
                   'use_mozharness': True,
                   'script_path': 'scripts/b2g_desktop_unittest.py',
                   'blob_upload': True,
                   },
     ),
    ('reftest-10', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_desktop_unittest.py',
                    'blob_upload': True,
                    },
     ),
]

REFTEST_DESKTOP_SANITY = [
    ('reftest', {'suite': 'reftest',
                 'use_mozharness': True,
                 'script_path': 'scripts/b2g_desktop_unittest.py',
                 'blob_upload': True,
                 },
     ),
]

JSREFTEST = [
    ('jsreftest-1', {'suite': 'jsreftest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('jsreftest-2', {'suite': 'jsreftest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('jsreftest-3', {'suite': 'jsreftest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
]

CRASHTEST = [
    ('crashtest-1', {'suite': 'crashtest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('crashtest-2', {'suite': 'crashtest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
    ('crashtest-3', {'suite': 'crashtest',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     },
     ),
]

MARIONETTE = [
    ('marionette-webapi', {'suite': 'marionette-webapi',
                           'use_mozharness': True,
                           'script_path': 'scripts/marionette.py',
                           'blob_upload': True,
                           },
     ),
]

XPCSHELL = [
    ('xpcshell', {'suite': 'xpcshell',
                  'use_mozharness': True,
                  'script_path': 'scripts/b2g_emulator_unittest.py',
                  'blob_upload': True,
                  },
     ),
]

GAIA_INTEGRATION = [(
    'gaia-integration', {
        'suite': 'gaia-integration',
        'use_mozharness': True,
        'script_path': 'scripts/gaia_integration.py',
        'timeout': 1800,
    },
)]

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
        'blob_upload': True,
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
    'linux32_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu32_vm-b2gdt': {
            'opt_unittest_suites': MOCHITEST_DESKTOP[:] + GAIA_INTEGRATION[:] + REFTEST_DESKTOP_SANITY[:],
            'debug_unittest_suites': [],
            'suite_config': {
                'gaia-integration': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_unit_production_config.py',
                    ],
                },
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
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', 1, '--total-chunks', 1,
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 1, '--total-chunks', 10,
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 2, '--total-chunks', 10,
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 3, '--total-chunks', 10,
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 4, '--total-chunks', 10,
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 5, '--total-chunks', 10,
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 6, '--total-chunks', 10,
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 7, '--total-chunks', 10,
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 8, '--total-chunks', 10,
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 9, '--total-chunks', 10,
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 10, '--total-chunks', 10,
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
            'opt_unittest_suites': GAIA_UI[:] + MOCHITEST_DESKTOP[:] + GAIA_INTEGRATION[:] + REFTEST_DESKTOP_SANITY[:] + GAIA_UNITTESTS[:],
            'debug_unittest_suites': [],
            'suite_config': {
                'gaia-integration': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_unit_production_config.py',
                    ],
                },
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
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', 1, '--total-chunks', 1,
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 1, '--total-chunks', 10,
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 2, '--total-chunks', 10,
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 3, '--total-chunks', 10,
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 4, '--total-chunks', 10,
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 5, '--total-chunks', 10,
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 6, '--total-chunks', 10,
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 7, '--total-chunks', 10,
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 8, '--total-chunks', 10,
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 9, '--total-chunks', 10,
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 10, '--total-chunks', 10,
                    ],
                },
            },
        },
    },
    'macosx64_gecko': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {
            "MOZ_NO_REMOTE": '1',
            "NO_EM_RESTART": '1',
            "XPCOM_DEBUG_BREAK": 'warn',
            "MOZ_CRASHREPORTER_NO_REPORT": '1',
            # for extracting dmg's
            "PAGER": '/bin/cat',
        },
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'mountainlion-b2gdt': {
            'opt_unittest_suites': GAIA_UI[:],
            'debug_unittest_suites': [],
            'suite_config': {
                'gaia-integration': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_unit_production_config.py',
                    ],
                },
                'gaia-ui-test': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                    ],
                },
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', 1, '--total-chunks', 1,
                    ],
                },
                'reftest': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                    ],
                },
                'reftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 1, '--total-chunks', 10,
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 2, '--total-chunks', 10,
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 3, '--total-chunks', 10,
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 4, '--total-chunks', 10,
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 5, '--total-chunks', 10,
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 6, '--total-chunks', 10,
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 7, '--total-chunks', 10,
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 8, '--total-chunks', 10,
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 9, '--total-chunks', 10,
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', 10, '--total-chunks', 10,
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
        'enable_debug_unittests': True,
        'fedora-b2g-emulator': {
            'opt_unittest_suites': REFTEST + MARIONETTE,
            'debug_unittest_suites': [],
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
                        "--cfg", "marionette/automation_emulator_config.py",
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
                'jsreftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '1', '--total-chunks', '3',
                    ],
                },
                'jsreftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '2', '--total-chunks', '3',
                    ],
                },
                'jsreftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '3', '--total-chunks', '3',
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
        'ubuntu64_vm-b2g-emulator': {
            'opt_unittest_suites': MOCHITEST + CRASHTEST + XPCSHELL + MARIONETTE,
            'debug_unittest_suites': MOCHITEST_EMULATOR_DEBUG + XPCSHELL[:],
            'suite_config': {
                'marionette-webapi': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py",
                    ],
                },
                'gaia-ui-test': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--cfg', 'marionette/gaia_ui_test_emu_config.py',
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
                'mochitest-debug-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '1', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '2', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '3', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '4', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '5', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '6', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '7', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '8', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '9', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '10', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-11': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '11', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-12': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '12', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-13': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '13', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-14': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '14', '--total-chunks', '15',
                    ],
                },
                'mochitest-debug-15': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '15', '--total-chunks', '15',
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
                        '--this-chunk', '1', '--total-chunks', '15',
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '2', '--total-chunks', '15',
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '3', '--total-chunks', '15',
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '4', '--total-chunks', '15',
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '5', '--total-chunks', '15',
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '6', '--total-chunks', '15',
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '7', '--total-chunks', '15',
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '8', '--total-chunks', '15',
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '9', '--total-chunks', '15',
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '10', '--total-chunks', '15',
                    ],
                },
                'reftest-11': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '11', '--total-chunks', '15',
                    ],
                },
                'reftest-12': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '12', '--total-chunks', '15',
                    ],
                },
                'reftest-13': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '13', '--total-chunks', '15',
                    ],
                },
                'reftest-14': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '14', '--total-chunks', '15',
                    ],
                },
                'reftest-15': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '15', '--total-chunks', '15',
                    ],
                },
                'jsreftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '1', '--total-chunks', '3',
                    ],
                },
                'jsreftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '2', '--total-chunks', '3',
                    ],
                },
                'jsreftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '3', '--total-chunks', '3',
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
                'jsreftest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '1', '--total-chunks', '3',
                    ],
                },
                'jsreftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '2', '--total-chunks', '3',
                    ],
                },
                'jsreftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'jsreftest',
                        '--this-chunk', '3', '--total-chunks', '3',
                    ],
                },
            },
        },
    },
    'emulator-jb': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu64_vm-b2g-emulator-jb': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
            'suite_config': {
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '1', '--total-chunks', '1',
                        '--test-manifest', 'manifests/emulator-jb.ini',
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
BRANCHES['ash']['mozharness_repo'] = "https://hg.mozilla.org/users/asasaki_mozilla.com/ash-mozharness"
BRANCHES['ash']['mozharness_tag'] = "default"
BRANCHES['cedar']['branch_name'] = "Cedar"
BRANCHES['cedar']['repo_path'] = "projects/cedar"
BRANCHES['cedar']['mozharness_tag'] = "default"
BRANCHES['cedar']['platforms']['emulator']['fedora-b2g-emulator']['opt_unittest_suites'] += JSREFTEST
BRANCHES['cedar']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] = \
    MOCHITEST + CRASHTEST + XPCSHELL + MARIONETTE + JSREFTEST + GAIA_UI
BRANCHES['cedar']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['debug_unittest_suites'] = MOCHITEST_EMULATOR_DEBUG[:] + REFTEST + CRASHTEST + MARIONETTE + XPCSHELL
BRANCHES['cedar']['platforms']['emulator-jb']['ubuntu64_vm-b2g-emulator-jb']['opt_unittest_suites'] = MOCHITEST_EMULATOR_JB[:]
BRANCHES['cedar']['platforms']['linux32_gecko']['ubuntu32_vm-b2gdt']['opt_unittest_suites'] += GAIA_UI + REFTEST_DESKTOP
BRANCHES['cedar']['platforms']['linux64_gecko']['ubuntu64_vm-b2gdt']['opt_unittest_suites'] += REFTEST_DESKTOP
BRANCHES['cedar']['platforms']['macosx64_gecko']['mountainlion-b2gdt']['opt_unittest_suites'] += MOCHITEST_DESKTOP + REFTEST_DESKTOP_SANITY + GAIA_INTEGRATION
BRANCHES['pine']['branch_name'] = "Pine"
BRANCHES['pine']['repo_path'] = "projects/pine"
BRANCHES['pine']['platforms']['emulator']['fedora-b2g-emulator']['opt_unittest_suites'] += JSREFTEST
BRANCHES['pine']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] = \
    MOCHITEST + CRASHTEST + XPCSHELL + MARIONETTE + JSREFTEST
BRANCHES['pine']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['debug_unittest_suites'] = \
    MOCHITEST_EMULATOR_DEBUG[:] + REFTEST + CRASHTEST + MARIONETTE + XPCSHELL
BRANCHES['pine']['platforms']['linux32_gecko']['ubuntu32_vm-b2gdt']['opt_unittest_suites'] += GAIA_UI
BRANCHES['cypress']['branch_name'] = "Cypress"
BRANCHES['cypress']['repo_path'] = "projects/cypress"
BRANCHES['cypress']['mozharness_tag'] = "default"
BRANCHES['fx-team']['repo_path'] = "integration/fx-team"
BRANCHES['graphics']['repo_path'] = "projects/graphics"
BRANCHES['ionmonkey']['repo_path'] = "projects/ionmonkey"
BRANCHES['mozilla-b2g18']['repo_path'] = "releases/mozilla-b2g18"
BRANCHES['mozilla-b2g18']['platforms']['emulator']['enable_debug_unittests'] = False
BRANCHES['mozilla-b2g18']['platforms']['emulator']['fedora-b2g-emulator']['opt_unittest_suites'] = MARIONETTE + REFTEST_SANITY
BRANCHES['mozilla-b2g18_v1_1_0_hd']['repo_path'] = "releases/mozilla-b2g18_v1_1_0_hd"
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['emulator']['fedora-b2g-emulator']['opt_unittest_suites'] = MARIONETTE + REFTEST_SANITY
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['emulator']['enable_debug_unittests'] = False
BRANCHES['mozilla-b2g26_v1_2']['repo_path'] = "releases/mozilla-b2g26_v1_2"
BRANCHES['mozilla-b2g26_v1_2']['platforms']['emulator']['enable_debug_unittests'] = False
BRANCHES['mozilla-b2g28_v1_3']['repo_path'] = "releases/mozilla-b2g28_v1_3"
BRANCHES['mozilla-b2g28_v1_3t']['repo_path'] = "releases/mozilla-b2g28_v1_3t"
BRANCHES['mozilla-aurora']['branch_name'] = "Mozilla-Aurora"
BRANCHES['mozilla-aurora']['repo_path'] = "releases/mozilla-aurora"
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-inbound']['repo_path'] = "integration/mozilla-inbound"
BRANCHES['b2g-inbound']['branch_name'] = "B2g-Inbound"
BRANCHES['b2g-inbound']['repo_path'] = "integration/b2g-inbound"
BRANCHES['services-central']['repo_path'] = "services/services-central"
BRANCHES['try']['pgo_strategy'] = "try"
BRANCHES['try']['enable_try'] = True

# explicitly set slave platforms per branch
for branch in BRANCHES.keys():
    for platform in BRANCHES[branch]['platforms']:
        if 'slave_platforms' not in BRANCHES[branch]['platforms'][platform]:
            BRANCHES[branch]['platforms'][platform]['slave_platforms'] = list(PLATFORMS[platform]['slave_platforms'])

NON_UBUNTU_BRANCHES = set([name for name, branch in items_before(BRANCHES, 'gecko_version', 22)])

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

# Disable ubuntu64_hw-b2g on all branches but cedar
for branch in set(BRANCHES.keys()) - set(['cedar']):
    for platform in BRANCHES[branch]['platforms']:
        if 'ubuntu64_hw-b2g' in BRANCHES[branch]['platforms'][platform]['slave_platforms']:
            BRANCHES[branch]['platforms'][platform]['slave_platforms'].remove('ubuntu64_hw-b2g')
        if 'ubuntu64_hw-b2g' in BRANCHES[branch]['platforms'][platform]:
            del BRANCHES[branch]['platforms'][platform]['ubuntu64_hw-b2g']

# Disable emulator debug unittests on older branches
for branch in BRANCHES.keys():
    if branch in ('mozilla-b2g26_v1_2',
                  'mozilla-esr24', 'mozilla-b2g18_v1_0_0',
                  'mozilla-b2g18_v1_0_1', 'mozilla-b2g18_v1_1_0_hd',
                  'mozilla-b2g18'):
        if 'emulator' in BRANCHES[branch]['platforms']:
            BRANCHES[branch]['platforms']['emulator']['enable_debug_unittests'] = False

# Disable b2g desktop reftest-sanity on cedar
for slave_platform in (('linux64_gecko', 'ubuntu64_vm-b2gdt'),
                       ('linux32_gecko', 'ubuntu32_vm-b2gdt')):
    if nested_haskey(BRANCHES['cedar']['platforms'], slave_platform[0], slave_platform[1]):
        slave_p = BRANCHES['cedar']['platforms'][slave_platform[0]][slave_platform[1]]
        slave_p['opt_unittest_suites'] = [x for x in slave_p['opt_unittest_suites']
                                          if x[0] if x[0] != 'reftest']
        slave_p['debug_unittest_suites'] = [x for x in slave_p['debug_unittest_suites']
                                            if x[0] if x[0] != 'reftest']

# Disable b2g desktop reftest-sanity, gaia-integration and gaia-unit tests on older branches
OLD_BRANCHES = set([name for name, branch in items_before(BRANCHES, 'gecko_version', 29)])
excluded_tests = ['gaia-integration', 'reftest', 'gaia-unit']
for b in BRANCHES.keys():
    branch = BRANCHES[b]
    if b in OLD_BRANCHES:
        for slave_platform in (('linux64_gecko', 'ubuntu64_vm-b2gdt'),
                               ('linux32_gecko', 'ubuntu32_vm-b2gdt'),
                               ('macosx64_gecko', 'mountainlion-b2gdt')):
            if nested_haskey(branch['platforms'], slave_platform[0], slave_platform[1]):
                slave_p = branch['platforms'][slave_platform[0]][slave_platform[1]]
                slave_p['opt_unittest_suites'] = [x for x in slave_p['opt_unittest_suites']
                                                  if x[0] not in excluded_tests]
                slave_p['debug_unittest_suites'] = [x for x in slave_p['debug_unittest_suites']
                                                    if x[0] not in excluded_tests]

# Enabled b2g reftests on EC2
# For branches newer than Gecko 30 (including)
# Once we uplift the patches to esr24 and the b2g branches
# we can get enable the REFTESTS for every branch
for name, branch in items_at_least(BRANCHES, 'gecko_version', 30):
    branch['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] += REFTEST_15[:]

# Disable macosx64_gecko gaia-ui tests on older branches
for branch in BRANCHES.keys():
    if branch in ('mozilla-b2g18_v1_0_0', 'mozilla-b2g18_v1_0_1',
                  'mozilla-b2g18_v1_1_0_hd', 'mozilla-b2g18',
                  'mozilla-b2g26_v1_2', 'mozilla-b2g28_v1_3',
                  'mozilla-b2g28_v1_3t'):
        for platform in ('macosx64_gecko',):
            if platform in BRANCHES[branch]['platforms']:
                for slave_platform in ('mountainlion-b2gdt',):
                    if slave_platform in BRANCHES[branch]['platforms'][platform]:
                        del BRANCHES[branch]['platforms'][platform][slave_platform]

# Disable debug emulator mochitests on older branches
OLD_BRANCHES = set([name for name, branch in items_before(BRANCHES, 'gecko_version', 29)])
for b in BRANCHES.keys():
    branch = BRANCHES[b]
    if b in OLD_BRANCHES:
        if nested_haskey(branch['platforms'], 'emulator', 'ubuntu64_vm-b2g-emulator'):
            slave_p = branch['platforms']['emulator']['ubuntu64_vm-b2g-emulator']
            slave_p['debug_unittest_suites'] = [x for x in slave_p['debug_unittest_suites']
                                                if not x[0].startswith('mochitest-debug')]

# Disable ubuntu64_vm-b2gdt/ubuntu32_vm-b2gdt (ie gaia-ui-test) on older branches
for branch in BRANCHES.keys():
    if branch in ('mozilla-esr24', 'mozilla-b2g18_v1_1_0_hd', 'mozilla-b2g18'):
        for platform in ('linux64_gecko', 'linux32_gecko'):
            if platform in BRANCHES[branch]['platforms']:
                for slave_platform in ('ubuntu64_vm-b2gdt', 'ubuntu32_vm-b2gdt'):
                    if slave_platform in BRANCHES[branch]['platforms'][platform]:
                        del BRANCHES[branch]['platforms'][platform][slave_platform]

# linux64_gecko hacks.  See bug 891973
# MERGE DAY remove branches as gecko26 merges in
for branch in BRANCHES.keys():
    if branch in ('mozilla-b2g18', 'mozilla-b2g18_v1_1_0_hd'):
        if 'linux64_gecko' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['linux64_gecko']

# marionette-webapi Ubuntu train, see bug 932988
FEDORA_MARIONETTE_BRANCHES = set([name for name, branch in items_before(BRANCHES, 'gecko_version', 28)])
for b in BRANCHES.keys():
    slave_p = None
    branch = BRANCHES[b]
    # Figure out which slave platform to delete
    if b in FEDORA_MARIONETTE_BRANCHES:
        if nested_haskey(branch['platforms'], 'emulator', 'ubuntu64_vm-b2g-emulator'):
            slave_p = branch['platforms']['emulator']['ubuntu64_vm-b2g-emulator']
    else:
        if nested_haskey(branch['platforms'], 'emulator', 'fedora-b2g-emulator'):
            slave_p = branch['platforms']['emulator']['fedora-b2g-emulator']
    if slave_p:
        for i in slave_p['opt_unittest_suites']:
            if i[0] == "marionette-webapi":
                slave_p['opt_unittest_suites'].remove(i)
        for i in slave_p['debug_unittest_suites']:
            if i[0] == "marionette-webapi":
                slave_p['debug_unittest_suites'].remove(i)


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
