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
    'alder': {},
    'ash': {},
    # Not needed right now, see bug 977420
    # 'birch': {},
    'cedar': {},
    'cypress': {},
    'jamun': {},
    'maple': {},
    'pine': {},
    'fx-team': {},
    'mozilla-b2g30_v1_4': {
        'gecko_version': 30,
        'b2g_version': (1, 4, 0),
    },
    'mozilla-b2g32_v2_0': {
        'gecko_version': 32,
        'b2g_version': (2, 0, 0),
    },
    'mozilla-b2g34_v2_1': {
        'gecko_version': 34,
        'b2g_version': (2, 1, 0),
    },
    'mozilla-b2g34_v2_1s': {
        'gecko_version': 34,
        'b2g_version': (2, 1, 0),
    },
    'mozilla-b2g37_v2_2': {
        'gecko_version': 37,
        'b2g_version': (2, 2, 0),
    },
    'mozilla-central': {},
    'mozilla-inbound': {},
    'b2g-inbound': {},
    #'services-central': {},  # Bug 1010674
    'try': {},
}

setMainFirefoxVersions(BRANCHES)

PLATFORMS = {
    'linux64_gecko': {},
    'macosx64_gecko': {},
    'macosx64-mulet': {},
    'emulator': {},
    'emulator-jb': {},
    'emulator-kk': {},
}

builder_prefix = "b2g"

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

PLATFORMS['macosx64-mulet']['slave_platforms'] = ['snowleopard']
PLATFORMS['macosx64-mulet']['env_name'] = 'mac-perf'
PLATFORMS['macosx64-mulet']['snowleopard'] = {
    'name': 'Rev4 MacOSX Mulet Snow Leopard 10.6',
    'build_dir_prefix': 'snowleopard_mulet',
    'scheduler_slave_platform_identifier': 'snowleopard_mulet'
}
PLATFORMS['macosx64-mulet']['stage_product'] = 'b2g'
PLATFORMS['macosx64-mulet']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'use_mozharness': True,
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
}

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
        'linux64_gecko': {},
        'macosx64_gecko': {},
        'macosx64-mulet': {},
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
MOCHITEST_CHROME = [
    ('mochitest-chrome', {'suite': 'mochitest-chrome',
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

MOCHITEST_MULET_PLAIN = [
    ('mochitest-1', {'suite': 'mochitest-plain',
                                 'use_mozharness': True,
                                 'script_path': 'scripts/desktop_unittest.py',
                                 'blob_upload': True,
                                }
    ),
    ('mochitest-2', {'suite': 'mochitest-plain',
                                 'use_mozharness': True,
                                 'script_path': 'scripts/desktop_unittest.py',
                                 'blob_upload': True,
                                }
    ),
    ('mochitest-3', {'suite': 'mochitest-plain',
                                 'use_mozharness': True,
                                 'script_path': 'scripts/desktop_unittest.py',
                                 'blob_upload': True,
                                }
    ),
    ('mochitest-4', {'suite': 'mochitest-plain',
                                 'use_mozharness': True,
                                 'script_path': 'scripts/desktop_unittest.py',
                                 'blob_upload': True,
                                }
    ),
    ('mochitest-5', {'suite': 'mochitest-plain',
                                 'use_mozharness': True,
                                 'script_path': 'scripts/desktop_unittest.py',
                                 'blob_upload': True,
                                }
    ),
]

REFTEST_MULET = [
    ('reftest-1', {
        'suite': 'reftest',
        'use_mozharness': True,
        'script_path': 'scripts/mulet_unittest.py',
        'blob_upload': True,
    }),
    ('reftest-2', {
        'suite': 'reftest',
        'use_mozharness': True,
        'script_path': 'scripts/mulet_unittest.py',
        'blob_upload': True,
    }),
    ('reftest-3', {
        'suite': 'reftest',
        'use_mozharness': True,
        'script_path': 'scripts/mulet_unittest.py',
        'blob_upload': True,
    }),
    ('reftest-4', {
        'suite': 'reftest',
        'use_mozharness': True,
        'script_path': 'scripts/mulet_unittest.py',
        'blob_upload': True,
    }),
    ('reftest-5', {
        'suite': 'reftest',
        'use_mozharness': True,
        'script_path': 'scripts/mulet_unittest.py',
        'blob_upload': True,
    }),
    ('reftest-6', {
        'suite': 'reftest',
        'use_mozharness': True,
        'script_path': 'scripts/mulet_unittest.py',
        'blob_upload': True,
    }),
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
    ('mochitest-debug-16', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-17', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-18', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-19', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
    ('mochitest-debug-20', {'suite': 'mochitest-plain',
                            'use_mozharness': True,
                            'script_path': 'scripts/b2g_emulator_unittest.py',
                            'blob_upload': True,
                            },
     ),
]

MOCHITEST_MEDIA = [
    ('mochitest-media', {'suite': 'mochitest-plain',
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

MOCHITEST_OOP_DESKTOP = [('mochitest-oop-1', MOCHITEST_DESKTOP[0][1])]

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

REFTEST_SANITY = [
    ('reftest-sanity', {'suite': 'reftest',
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
    ('reftest-sanity', {'suite': 'reftest',
                        'use_mozharness': True,
                        'script_path': 'scripts/b2g_desktop_unittest.py',
                        'blob_upload': True,
                       },
     ),
]

REFTEST_DESKTOP_OOP_SANITY = [('reftest-sanity-oop', REFTEST_DESKTOP_SANITY[0][1])]

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

MARIONETTE_UNIT = [
    ('marionette', {'suite': 'marionette',
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

GAIA_UNITTESTS_OOP = [('gaia-unit-oop', GAIA_UNITTESTS[0][1])]

GAIA_UI = [(
    'gaia-ui-test', {
        'suite': 'gaia-ui-test',
        'use_mozharness': True,
        'script_path': 'scripts/marionette.py',
        'blob_upload': True,
    },
)]

#Gaia Python Integration Tests
# will replae GAIA_UI, Bug 1046694
GIP = [
    ('gaia-ui-test-functional-1', {
                                    'suite': 'gip',
                                    'use_mozharness': True,
                                    'script_path': 'scripts/marionette.py',
                                    'blob_upload': True,
                                   },
    ),
    ('gaia-ui-test-functional-2', {
                                    'suite': 'gip',
                                    'use_mozharness': True,
                                    'script_path': 'scripts/marionette.py',
                                    'blob_upload': True,
                                   },
    ),
    ('gaia-ui-test-functional-3', {
                                    'suite': 'gip',
                                    'use_mozharness': True,
                                    'script_path': 'scripts/marionette.py',
                                    'blob_upload': True,
                                   },
    ),
    ('gaia-ui-test-unit', {
                            'suite': 'gip',
                            'use_mozharness': True,
                            'script_path': 'scripts/marionette.py',
                            'blob_upload': True,
                           },
    ),
    ('gaia-ui-test-accessibility', {
                                     'suite': 'gip',
                                     'use_mozharness': True,
                                     'script_path': 'scripts/marionette.py',
                                     'blob_upload': True,
                                   },
    )
]

GAIA_UI_OOP = [('gaia-ui-test-oop', GAIA_UI[0][1])]

CPPUNIT = [(
    'cppunit', {
        'suite': 'cppunit',
        'use_mozharness': True,
        'script_path': 'scripts/b2g_emulator_unittest.py',
        'blob_upload': True,
    },
)]

ALL_UNITTESTS = MOCHITEST + REFTEST + CRASHTEST + MARIONETTE + MARIONETTE_UNIT + XPCSHELL

# Default set of unit tests
UNITTEST_SUITES = {
    'opt_unittest_suites': ALL_UNITTESTS[:],
    'debug_unittest_suites': [],
}

# You must define opt_unittest_suites when enable_opt_unittests is True for a
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
    'macosx64-mulet': {
        'product_name': 'b2g',
        'app_name': 'firefox',
        'brand_name': 'Mulet',
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
        'snowleopard': {
            'opt_unittest_suites': MOCHITEST_MULET_PLAIN[:],
            'debug_unittest_suites': [],
            'suite_config': {
                'mochitest-1': {
                    'extra_args': [
                      '--cfg', 'unittests/mac_unittest.py',
                      '--total-chunks', 5, '--this-chunk', 1,
                      '--mochitest-suite', 'plain-chunked',
                    ]
                },
                'mochitest-2': {
                    'extra_args': [
                      '--cfg', 'unittests/mac_unittest.py',
                      '--total-chunks', 5, '--this-chunk', 2,
                      '--mochitest-suite', 'plain-chunked',
                    ]
                },
                'mochitest-3': {
                    'extra_args': [
                      '--cfg', 'unittests/mac_unittest.py',
                      '--total-chunks', 5, '--this-chunk', 3,
                      '--mochitest-suite', 'plain-chunked',
                    ]
                },
                'mochitest-4': {
                    'extra_args': [
                      '--cfg', 'unittests/mac_unittest.py',
                      '--total-chunks', 5, '--this-chunk', 4,
                      '--mochitest-suite', 'plain-chunked',
                    ]
                },
                'mochitest-5': {
                    'extra_args': [
                      '--cfg', 'unittests/mac_unittest.py',
                      '--total-chunks', 5, '--this-chunk', 5,
                      '--mochitest-suite', 'plain-chunked',
                    ]
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
        'enable_debug_unittests': True,
        'ubuntu64_vm-b2gdt': {
            'opt_unittest_suites': MOCHITEST_DESKTOP[:] + \
                    REFTEST_DESKTOP_SANITY[:] + GAIA_UNITTESTS[:] + GAIA_LINTER[:],
            'debug_unittest_suites': [],
            'suite_config': {
                'gaia-integration': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_integration_config.py',
                    ],
                },
                'gaia-js-integration-1': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 1, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-2': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 2, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-3': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 3, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-4': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 4, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-5': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 5, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-6': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 6, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-7': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 7, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-8': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 8, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-9': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 9, '--total-chunks', 10,
                        ],
                },
                'gaia-js-integration-10': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 10, '--total-chunks', 10,
                        ],
                },
                'gaia-build': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_integration_config.py',
                    ],
                },
                'gaia-build-unit': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_integration_config.py',
                    ],
                },
                'gaia-linter': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_integration_config.py',
                    ],
                },
                'gaia-unit': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_unit_production_config.py',
                    ],
                },
                'gaia-unit-oop': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_unit_production_config.py',
                        '--browser-arg', '-oop',
                    ],
                },
                'gaia-ui-test': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                    ],
                },
                'gaia-ui-test-functional-1': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                        '--this-chunk', '1', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-functional-2': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                       '--this-chunk', '2', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-functional-3': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                        '--this-chunk', '3', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-unit': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'unit',
                    ],
                },
                'gaia-ui-test-accessibility': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'accessibility',
                    ],
                },
                'gaia-ui-test-oop': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--app-arg', '-oop',
                    ],
                },
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', 1, '--total-chunks', 1,
                    ],
                },
                'mochitest-oop-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', 1, '--total-chunks', 1,
                        '--browser-arg', '-oop',
                    ],
                },
                'reftest-sanity': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                    ],
                },
                'reftest-sanity-oop': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
                        '--browser-arg', '-oop',
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
        'enable_opt_unittests': False,
        'enable_debug_unittests': False,
        'mountainlion-b2gdt': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
            'suite_config': {
                'gaia-integration': {
                    'extra_args': [
                        '--cfg', 'b2g/gaia_integration_config.py',
                    ],
                },
                'gaia-js-integration-1': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 1, '--total-chunks', 4,
                        ],
                },
                'gaia-js-integration-2': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 2, '--total-chunks', 4,
                        ],
                },
                'gaia-js-integration-3': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 3, '--total-chunks', 4,
                        ],
                },
                'gaia-js-integration-4': {
                        'extra_args': [
                            '--cfg', 'b2g/gaia_integration_config.py',
                            '--this-chunk', 4, '--total-chunks', 4,
                        ],
                },
                'gaia-ui-test': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                    ],
                },
                'gaia-ui-test-functional-1': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                        '--this-chunk', '1', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-functional-2': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                       '--this-chunk', '2', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-functional-3': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                        '--this-chunk', '3', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-unit': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'unit',
                    ],
                },
                'gaia-ui-test-accessibility': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'accessibility',
                    ],
                },
                'mochitest-1': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', 1, '--total-chunks', 1,
                    ],
                },
                'reftest-sanity': {
                    'extra_args': [
                        '--cfg', 'b2g/desktop_automation_config.py',
                        '--test-suite', 'reftest',
                        '--test-manifest', 'tests/layout/reftests/reftest-sanity/reftest.list',
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
        'ubuntu64_vm-b2g-emulator': {
            'opt_unittest_suites': MOCHITEST + CRASHTEST + XPCSHELL + MARIONETTE + MARIONETTE_UNIT + CPPUNIT + REFTEST_20,
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
                'gaia-ui-test': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--cfg', 'marionette/gaia_ui_test_emu_config.py',
                    ],
                },
                'gaia-ui-test-functional-1': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                        '--this-chunk', '1', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-functional-2': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                       '--this-chunk', '2', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-functional-3': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                        '--this-chunk', '3', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-unit': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'unit',
                    ],
                },
                'gaia-ui-test-accessibility': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'accessibility',
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
                        '--this-chunk', '1', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '2', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '3', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '4', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '5', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '6', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '7', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '8', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '9', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '10', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-11': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '11', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-12': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '12', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-13': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '13', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-14': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '14', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-15': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '15', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-16': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '16', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-17': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '17', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-18': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '18', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-19': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '19', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-20': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '20', '--total-chunks', '20',
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
                        '--this-chunk', '1', '--total-chunks', '2'
                    ],
                },
                'xpcshell-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                        '--this-chunk', '2', '--total-chunks', '2'
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
        'ubuntu64_vm-b2g-lg-emulator': {
           'opt_unittest_suites': [],
           'debug_unittest_suites': [],
           'suite_config': {
               'gaia-ui-test': {
                   'extra_args': [
                       '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                       '--cfg', 'marionette/gaia_ui_test_emu_config.py',
                   ],
               },
               'gaia-ui-test-functional-1': {
                   'extra_args': [
                       '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                       '--gip-suite', 'functional',
                       '--this-chunk', '1', '--total-chunks', 3,
                   ],
               },
               'gaia-ui-test-functional-2': {
                   'extra_args': [
                       '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                       '--gip-suite', 'functional',
                      '--this-chunk', '2', '--total-chunks', 3,
                   ],
               },
               'gaia-ui-test-functional-3': {
                   'extra_args': [
                       '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                       '--gip-suite', 'functional',
                       '--this-chunk', '3', '--total-chunks', 3,
                   ],
               },
               'gaia-ui-test-unit': {
                   'extra_args': [
                       '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                       '--gip-suite', 'unit',
                   ],
               },
               'gaia-ui-test-accessibility': {
                   'extra_args': [
                       '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                       '--gip-suite', 'accessibility',
                   ],
               },
                'mochitest-media': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--test-path', 'dom/media/tests/',
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
                'marionette': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py",
                    ],
                },
                'marionette-webapi': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py",
                        "--test-manifest", "webapi-tests.ini",
                    ],
                },
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
    'emulator-kk': {
        'product_name': 'b2g',
        'app_name': 'b2g',
        'brand_name': 'Gecko',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu64_vm-b2g-emulator-kk': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
            'suite_config': {
                'marionette': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py",
                    ],
                },
                'marionette-webapi': {
                    'extra_args': [
                        "--cfg", "marionette/automation_emulator_config.py",
                        "--test-manifest", "webapi-tests.ini",
                    ],
                },
                'gaia-ui-test': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--cfg', 'marionette/gaia_ui_test_emu_config.py',
                    ],
                },
                'gaia-ui-test-functional-1': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                        '--this-chunk', '1', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-functional-2': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                       '--this-chunk', '2', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-functional-3': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'functional',
                        '--this-chunk', '3', '--total-chunks', 3,
                    ],
                },
                'gaia-ui-test-unit': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'unit',
                    ],
                },
                'gaia-ui-test-accessibility': {
                    'extra_args': [
                        '--cfg', 'marionette/gaia_ui_test_prod_config.py',
                        '--gip-suite', 'accessibility',
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
                        '--this-chunk', '1', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '2', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-3': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '3', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-4': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '4', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-5': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '5', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-6': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '6', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-7': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '7', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-8': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '8', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-9': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '9', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-10': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '10', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-11': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '11', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-12': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '12', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-13': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '13', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-14': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '14', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-15': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '15', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-16': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '16', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-17': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '17', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-18': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '18', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-19': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '19', '--total-chunks', '20',
                    ],
                },
                'mochitest-debug-20': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'mochitest',
                        '--this-chunk', '20', '--total-chunks', '20',
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
                        '--this-chunk', '1', '--total-chunks', '2'
                    ],
                },
                'xpcshell-2': {
                    'extra_args': [
                        '--cfg', 'b2g/emulator_automation_config.py',
                        '--test-suite', 'xpcshell',
                        '--this-chunk', '2', '--total-chunks', '2'
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

BRANCHES['alder']['branch_name'] = "Alder"
BRANCHES['alder']['repo_path'] = "projects/alder"
BRANCHES['ash']['branch_name'] = "Ash"
BRANCHES['ash']['repo_path'] = "projects/ash"
BRANCHES['cedar']['branch_name'] = "Cedar"
BRANCHES['cedar']['repo_path'] = "projects/cedar"
BRANCHES['cedar']['mozharness_tag'] = "default"
BRANCHES['cedar']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] = \
    MOCHITEST + REFTEST_20 + CRASHTEST + XPCSHELL + MARIONETTE + MARIONETTE_UNIT + JSREFTEST + CPPUNIT
BRANCHES['cedar']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['debug_unittest_suites'] = \
    MOCHITEST_EMULATOR_DEBUG[:] + REFTEST + CRASHTEST + MARIONETTE + MARIONETTE_UNIT + XPCSHELL_CHUNKED + CPPUNIT
BRANCHES['cedar']['platforms']['emulator']['ubuntu64_vm-b2g-lg-emulator']['opt_unittest_suites'] = MOCHITEST_MEDIA
BRANCHES['cedar']['platforms']['emulator-jb']['ubuntu64_vm-b2g-emulator-jb']['opt_unittest_suites'] = MOCHITEST_EMULATOR_JB[:]
BRANCHES['cedar']['platforms']['emulator-kk']['ubuntu64_vm-b2g-emulator-kk']['opt_unittest_suites'] = \
    MOCHITEST + REFTEST_20 + CRASHTEST + XPCSHELL + MARIONETTE + MARIONETTE_UNIT + JSREFTEST + CPPUNIT + MOCHITEST_CHROME
BRANCHES['cedar']['platforms']['emulator-kk']['ubuntu64_vm-b2g-emulator-kk']['debug_unittest_suites'] = \
    MOCHITEST_EMULATOR_DEBUG[:] + REFTEST + CRASHTEST + MARIONETTE + MARIONETTE_UNIT + XPCSHELL_CHUNKED + CPPUNIT
BRANCHES['cedar']['platforms']['linux64_gecko']['ubuntu64_vm-b2gdt']['opt_unittest_suites'] += \
  REFTEST_DESKTOP + GAIA_UI_OOP + GAIA_UNITTESTS_OOP
BRANCHES['cedar']['platforms']['linux64_gecko']['ubuntu64_vm-b2gdt']['debug_unittest_suites'] += GAIA_JS_INTEGRATION[:]
BRANCHES['cedar']['platforms']['macosx64_gecko']['mountainlion-b2gdt']['opt_unittest_suites'] += MOCHITEST_DESKTOP + REFTEST_DESKTOP_SANITY
BRANCHES['maple']['branch_name'] = "Maple"
BRANCHES['maple']['repo_path'] = "projects/maple"
BRANCHES['pine']['branch_name'] = "Pine"
BRANCHES['pine']['repo_path'] = "projects/pine"
BRANCHES['pine']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] = \
    MOCHITEST + CRASHTEST + XPCSHELL + MARIONETTE + JSREFTEST + REFTEST_20
BRANCHES['pine']['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['debug_unittest_suites'] = \
    MOCHITEST_EMULATOR_DEBUG[:] + REFTEST + CRASHTEST + MARIONETTE + XPCSHELL_CHUNKED
BRANCHES['cypress']['branch_name'] = "Cypress"
BRANCHES['cypress']['repo_path'] = "projects/cypress"
BRANCHES['jamun']['repo_path'] = "projects/jamun"
BRANCHES['fx-team']['repo_path'] = "integration/fx-team"
BRANCHES['mozilla-b2g30_v1_4']['repo_path'] = "releases/mozilla-b2g30_v1_4"
BRANCHES['mozilla-b2g32_v2_0']['repo_path'] = "releases/mozilla-b2g32_v2_0"
BRANCHES['mozilla-b2g34_v2_1']['repo_path'] = "releases/mozilla-b2g34_v2_1"
BRANCHES['mozilla-b2g34_v2_1s']['repo_path'] = "releases/mozilla-b2g34_v2_1s"
BRANCHES['mozilla-b2g37_v2_2']['repo_path'] = "releases/mozilla-b2g37_v2_2"
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-inbound']['repo_path'] = "integration/mozilla-inbound"
BRANCHES['b2g-inbound']['branch_name'] = "B2g-Inbound"
BRANCHES['b2g-inbound']['repo_path'] = "integration/b2g-inbound"
BRANCHES['try']['pgo_strategy'] = "try"
BRANCHES['try']['enable_try'] = True

# Enable mozharness pinning
for _, branch in items_at_least(BRANCHES, 'gecko_version', 30):
    branch['script_repo_manifest'] = \
        "https://hg.mozilla.org/%(repo_path)s/raw-file/%(revision)s/" + \
        "testing/mozharness/mozharness.json"

BRANCHES['mozilla-b2g30_v1_4']['script_repo_manifest'] = \
    "https://hg.mozilla.org/%(repo_path)s/raw-file/%(revision)s/" + \
    "testing/mozharness/mozharness.json"

def exclude_suites(slave_platform, branch, suites_to_be_excluded, from_opt_unittests, from_debug_unittests):
    #slave_platform is a tuple, e.g.:
    #('linux64_gecko', 'ubuntu64_vm-b2gdt')
    if nested_haskey(BRANCHES[branch]['platforms'], slave_platform[0], slave_platform[1]):
        slave_p = BRANCHES[branch]['platforms'][slave_platform[0]][slave_platform[1]]
        if from_opt_unittests:
            slave_p['opt_unittest_suites'] = [x for x in slave_p['opt_unittest_suites']
                                              if x[0] if x[0] not in suites_to_be_excluded]
        if from_debug_unittests:
            slave_p['debug_unittest_suites'] = [x for x in slave_p['debug_unittest_suites']
                                            if x[0] if x[0] not in suites_to_be_excluded]

exclude_suites(('linux64_gecko', 'ubuntu64_vm-b2gdt'), 'cedar', ('gaia-ui-test',), True, True)
exclude_suites(('macosx64_gecko', 'mountainlion-b2gdt'), 'cedar', ('gaia-ui-test',), True, True)

# new linux64_gecko tests as of gecko 32; OOP replaces their non-OOP variants
for name, branch in items_at_least(BRANCHES, 'gecko_version', 32):
    BRANCHES[name]['platforms']['linux64_gecko']['ubuntu64_vm-b2gdt']['opt_unittest_suites'] += \
      GAIA_BUILD + REFTEST_DESKTOP_OOP_SANITY + MOCHITEST_OOP_DESKTOP
    for suite_to_remove in ('mochitest-1', 'reftest-sanity'):
        for s in BRANCHES[name]['platforms']['linux64_gecko']['ubuntu64_vm-b2gdt']['opt_unittest_suites']:
            if s[0] == suite_to_remove:
                BRANCHES[name]['platforms']['linux64_gecko']['ubuntu64_vm-b2gdt']['opt_unittest_suites'].remove(s)

# new linux64_gecko tests as of gecko 34
for name, branch in items_at_least(BRANCHES, 'gecko_version', 34):
    BRANCHES[name]['platforms']['linux64_gecko']['ubuntu64_vm-b2gdt']['opt_unittest_suites'] += \
      GAIA_BUILD_UNIT

# add mochitest-chrome on B2G emulators as of gecko 38
for name, branch in items_at_least(BRANCHES, 'gecko_version', 38):
    if nested_haskey(BRANCHES[name]['platforms'], 'emulator', 'ubuntu64_vm-b2g-emulator'):
        BRANCHES[name]['platforms']['emulator']['ubuntu64_vm-b2g-emulator']['opt_unittest_suites'] += \
            MOCHITEST_CHROME

# Use chunked Gip, Gij in 36+ (bug 1081246)
for name, branch in items_at_least(BRANCHES, 'gecko_version', 36):
    for slave_platform in (('linux64_gecko', 'ubuntu64_vm-b2gdt'),
                           ('macosx64_gecko', 'mountainlion-b2gdt')):
        if slave_platform[0] in BRANCHES[name]['platforms']:
            BRANCHES[name]['platforms'][slave_platform[0]][slave_platform[1]]['opt_unittest_suites'] += GIP[:]
            if slave_platform[0] == 'linux64_gecko':
                BRANCHES[name]['platforms'][slave_platform[0]][slave_platform[1]]['debug_unittest_suites'] += GIP[:]
                BRANCHES[name]['platforms'][slave_platform[0]][slave_platform[1]]['opt_unittest_suites'] += GAIA_JS_INTEGRATION[:]
# ...and non-chunked Gip in earlier branches
for name, branch in items_before(BRANCHES, 'gecko_version', 36):
    for slave_platform in (('linux64_gecko', 'ubuntu64_vm-b2gdt'),
                           ('macosx64_gecko', 'mountainlion-b2gdt')):
        if slave_platform[0] in BRANCHES[name]['platforms']:
            BRANCHES[name]['platforms'][slave_platform[0]][slave_platform[1]]['opt_unittest_suites'] += GAIA_UI[:]
            if slave_platform[0] == 'linux64_gecko':
                BRANCHES[name]['platforms'][slave_platform[0]][slave_platform[1]]['debug_unittest_suites'] += GAIA_UI[:]
                BRANCHES[name]['platforms'][slave_platform[0]][slave_platform[1]]['opt_unittest_suites'] += GAIA_INTEGRATION[:]

# explicitly set slave platforms per branch
for branch in BRANCHES.keys():
    for platform in BRANCHES[branch]['platforms']:
        if 'slave_platforms' not in BRANCHES[branch]['platforms'][platform]:
            BRANCHES[branch]['platforms'][platform]['slave_platforms'] = list(PLATFORMS[platform]['slave_platforms'])

# Disable linter tests on branches older than gecko 31
OLD_BRANCHES = set([name for name, branch in items_before(BRANCHES, 'gecko_version', 31)])
excluded_tests = ['gaia-linter']
for b in BRANCHES.keys():
    branch = BRANCHES[b]
    if b in OLD_BRANCHES:
        for slave_platform in (('linux64_gecko', 'ubuntu64_vm-b2gdt'),):
            if nested_haskey(branch['platforms'], slave_platform[0], slave_platform[1]):
                slave_p = branch['platforms'][slave_platform[0]][slave_platform[1]]
                slave_p['opt_unittest_suites'] = [x for x in slave_p['opt_unittest_suites']
                                                  if x[0] not in excluded_tests]

# Disable debug emulator mochitests on older branches
OLD_BRANCHES = set([name for name, branch in items_before(BRANCHES, 'gecko_version', 29)])
for b in BRANCHES.keys():
    branch = BRANCHES[b]
    if b in OLD_BRANCHES:
        if nested_haskey(branch['platforms'], 'emulator', 'ubuntu64_vm-b2g-emulator'):
            slave_p = branch['platforms']['emulator']['ubuntu64_vm-b2g-emulator']
            slave_p['debug_unittest_suites'] = [x for x in slave_p['debug_unittest_suites']
                                                if not x[0].startswith('mochitest-debug')]

# Disable emulator cppunit tests on older branches
OLD_BRANCHES = set([name for name, branch in items_before(BRANCHES, 'gecko_version', 34)])
for b in BRANCHES.keys():
    branch = BRANCHES[b]
    if b in OLD_BRANCHES:
        if nested_haskey(branch['platforms'], 'emulator', 'ubuntu64_vm-b2g-emulator'):
            slave_p = branch['platforms']['emulator']['ubuntu64_vm-b2g-emulator']
            for suites in ['opt_unittest_suites', 'debug_unittest_suites']:
                slave_p[suites] = [x for x in slave_p[suites]
                                   if not x[0].startswith('cppunit')]

# Disable OSX Mulet in every branch except cedar
for name in BRANCHES.keys():
    if name in ('cedar', ):
        continue
    for platform in ('macosx64-mulet', ):
        if platform in BRANCHES[name]['platforms']:
            del BRANCHES[name]['platforms'][platform]

# Disable tests jobs of builds that have been moved to TC
for _, branch in items_at_least(BRANCHES, 'gecko_version', 39):
    for p in ('emulator-jb', 'emulator-kk', 'linux64_gecko'):
        if branch['platforms'].get(p):
            del branch['platforms'][p]


PROJECTS = {}

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
