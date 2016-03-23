from copy import deepcopy

from config import MOZHARNESS_REBOOT_CMD

import localconfig
reload(localconfig)
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
    # Disabled in bug 1227277
    #'alder': {},
    # Disabled in bug 1227277
    #'ash': {},
    # Not needed right now, see bug 977420
    # 'birch': {},
    # Disabled in bug 1227277
    #'cedar': {},
    # Disabled for bug 1151699
    # 'cypress': {},
    # Disabled for Bug 1150320
    # 'jamun': {},
    # disabled in bug 1215527
    # 'maple': {}
    'pine': {},
    'fx-team': {},
    'mozilla-b2g44_v2_5': {
        'gecko_version': 44,
        'b2g_version': (2, 5, 0),
    },
    'mozilla-central': {},
    'mozilla-inbound': {},
    'b2g-inbound': {},
    #'services-central': {},  # Bug 1010674
    'try': {},
}

setMainFirefoxVersions(BRANCHES)

PLATFORMS = {
    'emulator': {},
    'emulator-jb': {},
    'emulator-kk': {},
}

builder_prefix = "b2g"

PLATFORMS['emulator']['slave_platforms'] = ['ubuntu64_vm-b2g-emulator', 'ubuntu64_vm-b2g-lg-emulator']
PLATFORMS['emulator']['env_name'] = 'linux-perf'
PLATFORMS['emulator']['ubuntu64_vm-b2g-emulator'] = {'name': "b2g_emulator_vm"}
PLATFORMS['emulator']['ubuntu64_vm-b2g-lg-emulator'] = {'name': "b2g_emulator_vm_large"}
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

PLATFORMS['emulator-kk']['slave_platforms'] = ['ubuntu64_vm-b2g-emulator-kk']
PLATFORMS['emulator-kk']['env_name'] = 'linux-perf'
PLATFORMS['emulator-kk']['ubuntu64_vm-b2g-emulator-kk'] = {'name': "b2g_emulator-kk_vm"}
PLATFORMS['emulator-kk']['stage_product'] = 'b2g'
PLATFORMS['emulator-kk']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'use_mozharness': True,
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

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'emulator': {},
        'emulator-jb': {},
        'emulator-kk': {},
    },
}

SUITES = {}

MOCHITEST = [
    ('mochitest-1', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
    ('mochitest-2', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
    ('mochitest-3', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
    ('mochitest-4', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
    ('mochitest-5', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
    ('mochitest-6', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
    ('mochitest-7', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
    ('mochitest-8', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
    ('mochitest-9', {'suite': 'mochitest-plain',
                     'use_mozharness': True,
                     'script_path': 'scripts/b2g_emulator_unittest.py',
                     'blob_upload': True,
                     'script_maxtime': 14400,
                     },
     ),
]
MOCHITEST_CHROME = [
    ('mochitest-chrome', {'suite': 'mochitest-chrome',
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
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-2', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-3', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-4', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-5', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-6', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-7', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-8', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-9', {'suite': 'mochitest-plain',
                           'use_mozharness': True,
                           'script_path': 'scripts/b2g_emulator_unittest.py',
                           'blob_upload': True,
                           'script_maxtime': 14400,
                           },
     ),
    ('mochitest-debug-10', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-11', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-12', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-13', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-14', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-15', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-16', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-17', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-18', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-19', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-20', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-21', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-22', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-23', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-24', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
    ('mochitest-debug-25', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            'script_maxtime': 14400,
                            },
     ),
]

MOCHITEST_OOP_DESKTOP = [
    ('mochitest-oop-1', {'suite': 'mochitest-plain',
                         'use_mozharness': True,
                         'script_path': 'scripts/b2g_desktop_unittest.py',
                         'blob_upload': True,
                        },
     ),
]

GAIA_JS_INTEGRATION = [
    ('gaia-js-integration-1', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-2', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-3', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-4', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-5', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-6', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-7', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-8', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-9', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
                           },
    ),
    ('gaia-js-integration-10', {'suite': 'gaia-js-integration',
                           'use_mozharness': True,
                           'script_path': 'scripts/gaia_integration.py',
                           'timeout': 1800,
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

REFTEST_20 = REFTEST[:]
REFTEST_20 += [
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
    ('reftest-16', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('reftest-17', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('reftest-18', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('reftest-19', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('reftest-20', {'suite': 'reftest',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
]

REFTEST_DESKTOP_OOP_SANITY = [
    ('reftest-sanity-oop', {'suite': 'reftest',
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

XPCSHELL_CHUNKED = [
    ('xpcshell-1', {'suite': 'xpcshell',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('xpcshell-2', {'suite': 'xpcshell',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('xpcshell-3', {'suite': 'xpcshell',
                    'use_mozharness': True,
                    'script_path': 'scripts/b2g_emulator_unittest.py',
                    'blob_upload': True,
                    },
     ),
    ('xpcshell-4', {'suite': 'xpcshell',
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

GAIA_BUILD = [(
    'gaia-build', {
        'suite': 'gaia-build',
        'use_mozharness': True,
        'script_path': 'scripts/gaia_build_integration.py',
        'timeout': 1800,
    },
)]

GAIA_BUILD_UNIT = [(
    'gaia-build-unit', {
        'suite': 'gaia-build-unit',
        'use_mozharness': True,
        'script_path': 'scripts/gaia_build_unit.py',
        'timeout': 1800,
    },
)]

GAIA_LINTER = [(
    'gaia-linter', {
        'suite': 'gaia-linter',
        'use_mozharness': True,
        'script_path': 'scripts/gaia_linter.py',
        'timeout': 1800,
    },
)]

GAIA_UNITTESTS = [(
    'gaia-unit', {
        'suite': 'gaia-unit',
        'use_mozharness': True,
        'script_path': 'scripts/gaia_unit.py',
        'blob_upload': True,
    },
)]

CPPUNIT = [(
    'cppunit', {
        'suite': 'cppunit',
        'use_mozharness': True,
        'script_path': 'scripts/b2g_emulator_unittest.py',
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
    'emulator': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'ubuntu64_vm-b2g-emulator': {
            'opt_unittest_suites': MOCHITEST + CRASHTEST + XPCSHELL + MARIONETTE + CPPUNIT + REFTEST_20,
            'debug_unittest_suites': MOCHITEST_EMULATOR_DEBUG + XPCSHELL_CHUNKED + CPPUNIT,
            'suite_config': {
                'marionette': {
                  'extra_args': [
                      "--cfg", "marionette/automation_emulator_config.py",
                  ],
                },
                'marionette-webapi': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py",
                        "--test-manifest", "webapi-tests.ini"
                    ],
                },
                'mochitest-media': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--test-path', 'dom/media/tests/',
                    ],
                },
                'mochitest-chrome': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest-chrome',
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
                        '--this-chunk', '1', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '2', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '3', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '4', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '5', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '6', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '7', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '8', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '9', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '10', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-11': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '11', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-12': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '12', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-13': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '13', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-14': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '14', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-15': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '15', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-16': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '16', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-17': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '17', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-18': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '18', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-19': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '19', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-20': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '20', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-21': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '21', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-22': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '22', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-23': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '23', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-24': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '24', '--total-chunks', '25',
                    ],
                },
                'mochitest-debug-25': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '25', '--total-chunks', '25',
                    ],
                },
                'xpcshell': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                    ],
                },
                'xpcshell-1': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                        '--this-chunk', '1', '--total-chunks', '4'
                    ],
                },
                'xpcshell-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                        '--this-chunk', '2', '--total-chunks', '4'
                    ],
                },
                'xpcshell-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                        '--this-chunk', '3', '--total-chunks', '4'
                    ],
                },
                'xpcshell-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                        '--this-chunk', '4', '--total-chunks', '4'
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
                'reftest-sanity': {
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
                        '--this-chunk', '1', '--total-chunks', '20',
                    ],
                },
                'reftest-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '2', '--total-chunks', '20',
                    ],
                },
                'reftest-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '3', '--total-chunks', '20',
                    ],
                },
                'reftest-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '4', '--total-chunks', '20',
                    ],
                },
                'reftest-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '5', '--total-chunks', '20',
                    ],
                },
                'reftest-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '6', '--total-chunks', '20',
                    ],
                },
                'reftest-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '7', '--total-chunks', '20',
                    ],
                },
                'reftest-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '8', '--total-chunks', '20',
                    ],
                },
                'reftest-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '9', '--total-chunks', '20',
                    ],
                },
                'reftest-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '10', '--total-chunks', '20',
                    ],
                },
                'reftest-11': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '11', '--total-chunks', '20',
                    ],
                },
                'reftest-12': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '12', '--total-chunks', '20',
                    ],
                },
                'reftest-13': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '13', '--total-chunks', '20',
                    ],
                },
                'reftest-14': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '14', '--total-chunks', '20',
                    ],
                },
                'reftest-15': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '15', '--total-chunks', '20',
                    ],
                },
                'reftest-16': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '16', '--total-chunks', '20',
                    ],
                },
                'reftest-17': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '17', '--total-chunks', '20',
                    ],
                },
                'reftest-18': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '18', '--total-chunks', '20',
                    ],
                },
                'reftest-19': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '19', '--total-chunks', '20',
                    ],
                },
                'reftest-20': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'reftest',
                        '--this-chunk', '20', '--total-chunks', '20',
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
                'cppunit': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'cppunittest',
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
        'enable_opt_unittests': False,
        'enable_debug_unittests': False,
        'ubuntu64_vm-b2g-emulator-jb': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
            'suite_config': {},
        },
    },
    'emulator-kk': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': False,
        'enable_debug_unittests': False,
        'ubuntu64_vm-b2g-emulator-kk': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
            'suite_config': {},
        },
    },
}

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.iteritems():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
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
    if branch in b2g_localconfig.BRANCHES:
        for key, value in b2g_localconfig.BRANCHES[branch].iteritems():
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

    for platform, platform_config in b2g_localconfig.PLATFORM_VARS.iteritems():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.iteritems():
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
    BRANCHES[branch]['script_repo_manifest'] = "https://hg.mozilla.org/%(repo_path)s/raw-file/%(revision)s/" + \
                                               "testing/mozharness/mozharness.json"
    # mozharness_archiver_repo_path tells the factory to use a copy of mozharness from within the
    #  gecko tree and also allows us to overwrite which gecko repo to use. Useful for platforms
    # like Thunderbird
    BRANCHES[branch]['mozharness_archiver_repo_path'] = '%(repo_path)s'

# The following are exceptions to the defaults

BRANCHES['pine']['branch_name'] = "Pine"
BRANCHES['pine']['repo_path'] = "projects/pine"
BRANCHES['pine']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] = \
    MOCHITEST + CRASHTEST + XPCSHELL + MARIONETTE + JSREFTEST + REFTEST_20
BRANCHES['pine']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['debug_unittest_suites'] = \
    MOCHITEST_EMULATOR_DEBUG[:] + REFTEST + CRASHTEST + MARIONETTE + XPCSHELL_CHUNKED
# disabled for Bug 1150320
# BRANCHES['jamun']['repo_path'] = "projects/jamun"
BRANCHES['fx-team']['repo_path'] = "integration/fx-team"
BRANCHES['mozilla-b2g44_v2_5']['repo_path'] = "releases/mozilla-b2g44_v2_5"
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-inbound']['repo_path'] = "integration/mozilla-inbound"
BRANCHES['b2g-inbound']['branch_name'] = "B2g-Inbound"
BRANCHES['b2g-inbound']['repo_path'] = "integration/b2g-inbound"
BRANCHES['try']['pgo_strategy'] = "try"
BRANCHES['try']['enable_try'] = True

# add mochitest-chrome on B2G emulators as of gecko 38
for name, branch in items_at_least(BRANCHES, 'gecko_version', 38):
    if nested_haskey(BRANCHES[name]['platforms'], 'emulator', 'ubuntu64_vm-b2g-emulator'):
        BRANCHES[name]['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] += \
            MOCHITEST_CHROME[:]

# explicitly set slave platforms per branch
for branch in BRANCHES.keys():
    for platform in BRANCHES[branch]['platforms']:
        if 'slave_platforms' not in BRANCHES[branch]['platforms'][platform]:
            BRANCHES[branch]['platforms'][platform]['slave_platforms'] = list(PLATFORMS[platform]['slave_platforms'])


PROJECTS = {}

# Bug 1250953 - Disable ICS emulator builds/tests on trunk
for branch in BRANCHES.keys():
    for platform in BRANCHES[branch]['platforms'].keys():
        if branch in ['mozilla-b2g44_v2_5', 'try']:
            continue
        if platform in ['emulator']:
            del BRANCHES[branch]['platforms'][platform]

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
