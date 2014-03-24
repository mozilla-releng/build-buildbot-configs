from copy import deepcopy

import config_common
reload(config_common)
from config_common import loadDefaultValues, loadCustomTalosSuites, \
    nested_haskey, get_talos_slave_platforms, delete_slave_platform

import master_common
reload(master_common)
from master_common import setMainFirefoxVersions, items_before, items_at_least

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

TALOS_TP_NEW_OPTS = {'plugins': {'32': 'zips/flash32_10_3_183_5.zip', '64': 'zips/flash64_11_0_d1_98.zip'}, 'pagesets': ['zips/tp5n.zip']}

BRANCHES = {
    'mozilla-central':     {},
    'mozilla-aurora':      {},
    'mozilla-release':     {},
    'mozilla-beta':        {},
    'mozilla-esr24': {
        'gecko_version': 24,
        'platforms': {
            'macosx64': {},
            'win32': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g26_v1_2': {
        'datazilla_url': None,
        'gecko_version': 26,
        'platforms': {
            # desktop per sicking in Bug 829513
            'macosx64': {},
            'win32': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g28_v1_3': {
        'datazilla_url': None,
        'gecko_version': 28,
        'platforms': {
            # desktop per sicking in Bug 829513
            'macosx64': {},
            'win32': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g18': {
        'datazilla_url': None,
        'gecko_version': 18,
        'platforms': {
            # desktop per sicking in Bug 829513
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g18_v1_1_0_hd': {
        'datazilla_url': None,
        'gecko_version': 18,
        'platforms': {
            # desktop per sicking in Bug 829513
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'try': {
        'coallesce_jobs': False,
    },
}

setMainFirefoxVersions(BRANCHES)

# Talos
PLATFORMS = {
    'macosx64': {},
    'win32': {},
    'linux': {},
    'linux64': {},
    'linux64-asan': {},
    'win64': {},
}

PLATFORMS['macosx64']['slave_platforms'] = ['snowleopard', 'mountainlion', 'mavericks']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['snowleopard'] = {'name': "Rev4 MacOSX Snow Leopard 10.6"}
PLATFORMS['macosx64']['mountainlion'] = {'name': "Rev5 MacOSX Mountain Lion 10.8"}
PLATFORMS['macosx64']['mavericks'] = {'name': "Rev5 MacOSX Mavericks 10.9"}
PLATFORMS['macosx64']['stage_product'] = 'firefox'
PLATFORMS['macosx64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/mac_config.py',
}

PLATFORMS['win32']['slave_platforms'] = ['xp-ix', 'win7-ix', 'win8']
PLATFORMS['win32']['talos_slave_platforms'] = ['xp-ix', 'win7-ix', 'win8']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp-ix'] = {'name': "Windows XP 32-bit"}
PLATFORMS['win32']['win7-ix'] = {'name': "Windows 7 32-bit"}
PLATFORMS['win32']['win8'] = {'name': "WINNT 6.2"}
PLATFORMS['win32']['stage_product'] = 'firefox'
PLATFORMS['win32']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '32',
    'config_file': 'talos/windows_config.py',
}

PLATFORMS['win64']['slave_platforms'] = ['win64_vm', 'win8_64']
PLATFORMS['win64']['win64_vm'] = {'name': 'win64_vm'}
PLATFORMS['win64']['win8_64'] = {'name': 'win8_64'}
PLATFORMS['win64']['stage_product'] = 'firefox'
PLATFORMS['win64']['win8_64']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
}
PLATFORMS['win64']['mozharness_config'] = {
    'mozharness_python': ['c:/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/windows_config.py',
}

PLATFORMS['linux']['slave_platforms'] = ['fedora', 'ubuntu32_vm']
PLATFORMS['linux']['talos_slave_platforms'] = ['ubuntu32_hw']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': "Rev3 Fedora 12"}
PLATFORMS['linux']['ubuntu32_vm'] = {'name': 'Ubuntu VM 12.04'}
PLATFORMS['linux']['ubuntu32_hw'] = {'name': 'Ubuntu HW 12.04'}
PLATFORMS['linux']['stage_product'] = 'firefox'
PLATFORMS['linux']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '32',
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64']['slave_platforms'] = ['fedora64', 'ubuntu64_vm']
PLATFORMS['linux64']['talos_slave_platforms'] = ['ubuntu64_hw']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': "Rev3 Fedora 12x64"}
PLATFORMS['linux64']['ubuntu64_vm'] = {'name': 'Ubuntu VM 12.04 x64'}
PLATFORMS['linux64']['ubuntu64_hw'] = {'name': 'Ubuntu HW 12.04 x64'}
PLATFORMS['linux64']['stage_product'] = 'firefox'
PLATFORMS['linux64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64-asan']['slave_platforms'] = ['ubuntu64-asan_vm']
PLATFORMS['linux64-asan']['ubuntu64-asan_vm'] = {'name': 'Ubuntu ASAN VM 12.04 x64'}
PLATFORMS['linux64-asan']['stage_product'] = 'firefox'
PLATFORMS['linux64-asan']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/linux_config.py',
}

# Lets be explicit instead of magical.
for platform, platform_config in PLATFORMS.items():
    all_slave_platforms = set(platform_config['slave_platforms'] +
                              platform_config.get('talos_slave_platforms', []))
    for slave_platform in all_slave_platforms:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform])
        if slave_platform in TRY_SLAVES:
            platform_config[slave_platform]['try_slaves'] = sorted(TRY_SLAVES[slave_platform])
        else:
            platform_config[slave_platform]['try_slaves'] = platform_config[slave_platform]['slaves']

ALL_TALOS_PLATFORMS = get_talos_slave_platforms(PLATFORMS, platforms=('linux', 'linux64', 'win32', 'macosx64'))
NO_WIN = get_talos_slave_platforms(PLATFORMS, platforms=('linux', 'linux64', 'macosx64'))
NO_WINXP = [platform for platform in ALL_TALOS_PLATFORMS if platform != 'xp-ix']
NO_MAC = get_talos_slave_platforms(PLATFORMS, platforms=('linux', 'linux64', 'win32'))
MAC_ONLY = get_talos_slave_platforms(PLATFORMS, platforms=('macosx64',))
WIN7_ONLY = ['win7-ix']
WIN8_ONLY = ['win8']
LINUX64_ONLY = ['ubuntu64_hw']

SUITES = {
    'xperf': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5n', '--sampleConfig', 'xperf.config', '--mozAfterPaint', '--xperf_path', '"c:/Program Files/Microsoft Windows Performance Toolkit/xperf.exe"', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, WIN7_ONLY),
    },
    'tpn': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5n', '--mozAfterPaint', '--responsiveness', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'tp5o': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o', '--mozAfterPaint', '--responsiveness', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'other': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscrollr:a11yr:ts_paint:tpaint', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'svgr': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvgr:tsvgr_opacity', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'dirtypaint': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tspaint_places_generated_med:tspaint_places_generated_max', '--setPref', 'hangmonitor.timeout=0', '--mozAfterPaint'],
        'options': (TALOS_DIRTY_OPTS, ALL_TALOS_PLATFORMS),
    },
    'dromaeojs': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom:kraken:v8_7'],
        'options': ({}, NO_WINXP),
    },
    'chromez': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tresize', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    # now let's add the metro talos suites
    'tp5o-metro': {
        'enable_by_default': False,
        'suites': [],  # suite + args are governed by talos.json
        'options': ({}, WIN8_ONLY),
    },
    'other-metro': {
        'enable_by_default': False,
        'suites': [],  # suite + args are governed by talos.json
        'options': ({}, WIN8_ONLY),
    },
    'svgr-metro': {
        'enable_by_default': False,
        'suites': [],  # suite + args are governed by talos.json
        'options': ({}, WIN8_ONLY),
    },
    'dromaeojs-metro': {
        'enable_by_default': False,
        'suites': [],  # suite + args are governed by talos.json
        'options': ({}, WIN8_ONLY),
    },
}

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'linux': {},
        'linux64': {},
        'linux64-asan': {},
        'macosx64': {},
        'win32': {},
        'win64': {},
    },
}

# Remove this chunk when Firefox 22 is on all branches.
# That will happen when b2g18 EOL
# Buildbot-based unit tests.
BUILDBOT_UNITTEST_SUITES = {
    'opt': [
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
    'opt_with_ipc': [
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
        ('reftest-ipc', ['reftest-ipc']),
        ('reftest-no-accel', ['opengl-no-accel']),
        ('crashtest-ipc', ['crashtest-ipc'])
    ],
    'opt_with_no-d2d-d3d': [
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
        ('reftest-no-accel', ['reftest-no-d2d-d3d']),
    ],
    'opt_no_a11y': [
        # Turn on chunks for mochitest
        ('mochitest', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-browser-chrome', ['mochitest-browser-chrome']),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
        # Disabled in bug 630551
        #('mozmill-all', ['mozmill']),
    ],
    'debug': [
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
    'debug_no_a11y': [
        # Turn on chunks for mochitest
        ('mochitest', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-browser-chrome', ['mochitest-browser-chrome']),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
        # Disabled in bug 630551
        #('mozmill-all', ['mozmill']),
    ],
}
# End of block to be removed when b2g18 is removed

MOCHITEST = [
    ('mochitest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain1'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('mochitest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain2'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('mochitest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain3'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('mochitest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain4'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('mochitest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain5'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('mochitest-browser-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome'],
        'blob_upload': True,
        'script_maxtime': 12000,
    }),
    ('mochitest-other', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'chrome,a11y,plugins'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

MOCHITEST_BC_3 = [
    ('mochitest-browser-chrome-1', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome-1'],
        'blob_upload': True,
        'script_maxtime': 4200,
    }),
    ('mochitest-browser-chrome-2', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome-2'],
        'blob_upload': True,
        'script_maxtime': 6000,
    }),
    ('mochitest-browser-chrome-3', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome-3'],
        'blob_upload': True,
        'script_maxtime': 4200,
    }),
]

REFTEST_NO_IPC = [
    ('reftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('jsreftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'jsreftest'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('crashtest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'crashtest'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]
REFTEST_NOACCEL = [
    ('reftest-no-accel', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-no-accel'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]
REFTEST_OMTC = [
    ('reftest-omtc', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-omtc'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]
REFTEST_IPC = [
    ('reftest-ipc', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-ipc'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('crashtest-ipc', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'crashtest-ipc'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

XPCSHELL = [
    ('xpcshell', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--xpcshell-suite', 'xpcshell'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

CPPUNIT = [
    ('cppunit', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--cppunittest-suite', 'cppunittest'],
        'script_maxtime': 7200,
    }),
]
MARIONETTE = [
    ('marionette', {
        'use_mozharness': True,
        'script_path': 'scripts/marionette.py',
        'download_symbols': False,
        'blob_upload': True,
    }),
]
METRO = [
    ('mochitest-metro-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-metro-chrome'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]
JITTEST = [
    ('jittest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--jittest-suite', 'jittest'],
        'script_maxtime': 7200,
    }),
]
JITTEST_CHUNKED = [
    ('jittest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--jittest-suite', 'jittest1'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
    ('jittest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--jittest-suite', 'jittest2'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]
MOZBASE = [
    ('mozbase', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mozbase-suite', 'mozbase'],
        'script_maxtime': 7200,
    }),
]
WEB_PLATFORM_TESTS = [
    ('web-platform-tests', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': [],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]


UNITTEST_SUITES = {
    'opt_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL + CPPUNIT,
    'debug_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL + CPPUNIT + MARIONETTE,
}


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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_IPC + REFTEST_NOACCEL,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
        },
        'ubuntu32_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + REFTEST_IPC + REFTEST_NOACCEL,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
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
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
        },
        'ubuntu64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
        },
    },
    'linux64-asan': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu64-asan_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-1': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest-2': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
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
        'xp-ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL,  # No marionette except on Try
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-omtc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        },
        'win7-ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_NOACCEL,
            'debug_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL,  # No marionette except on Try
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-omtc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        },
        'win8': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + REFTEST_NOACCEL[:],
            'debug_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL + CPPUNIT,  # No marionette except on Try
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-metro-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-omtc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        }
    },
    'win64': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'mochitest_leak_threshold': 484,
        'crashtest_leak_threshold': 484,
        'env_name': 'win64-perf-unittest',
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'win8_64': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + REFTEST_NOACCEL[:],
            'debug_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL + CPPUNIT,  # No marionette except on Try
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-metro-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        },
        'win64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + REFTEST_NOACCEL[:],
            'debug_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL + CPPUNIT,  # No marionette except on Try
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'metro-immersive': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        }
    },
    'macosx64': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'snowleopard': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
        'mountainlion': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
        'mavericks': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
            'suite_config': {
                'mochitest-1': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-2': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-3': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-4': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-5': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-1': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-2': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome-3': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-ipc': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-ipc': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
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
        'branches': ['fx-team'],
        'platforms': {
            'ubuntu64_vm': {'ext': 'linux-x86_64.tar.bz2', 'debug': True},
            'ubuntu32_vm': {'ext': 'linux-i686.tar.bz2', 'debug': True},
            'snowleopard': {'ext': '(mac|mac64).dmg', 'debug': True},
            'mountainlion': {'ext': '(mac|mac64).dmg', 'debug': True},
            'xp-ix': {
                'ext': 'win32.zip',
                'env': PLATFORM_UNITTEST_VARS['win32']['env_name'],
                'debug': True,
            },
            'win7-ix': {
                'ext': 'win32.zip',
                'env': PLATFORM_UNITTEST_VARS['win32']['env_name'],
                'debug': True,
            },
            'win8': {
                'ext': 'win32.zip',
                'env': PLATFORM_UNITTEST_VARS['win32']['env_name'],
                'debug': True,
            },
        },
        'hgurl': 'https://hg.mozilla.org',
        'repo_path': 'projects/addon-sdk',
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
    loadDefaultValues(BRANCHES, branch, BRANCHES[branch])
    loadCustomTalosSuites(BRANCHES, SUITES, branch, BRANCHES[branch])

# The following are exceptions to the defaults

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'

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

######### mozilla-esr24
BRANCHES['mozilla-esr24']['release_tests'] = 1
BRANCHES['mozilla-esr24']['repo_path'] = "releases/mozilla-esr24"
BRANCHES['mozilla-esr24']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr24']['xperf_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)

######### mozilla-b2g18
BRANCHES['mozilla-b2g18']['repo_path'] = "releases/mozilla-b2g18"
BRANCHES['mozilla-b2g18']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g18']['mozharness_talos'] = False
BRANCHES['mozilla-b2g18']['platforms']['linux64']['fedora64']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-b2g18']['platforms']['linux64']['fedora64']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'] + MARIONETTE
BRANCHES['mozilla-b2g18']['tpn_tests'] = (1, True, TALOS_TP_NEW_OPTS, LINUX64_ONLY)
BRANCHES['mozilla-b2g18']['tp5o_tests'] = (0, True, TALOS_TP_NEW_OPTS, LINUX64_ONLY)

######### mozilla-b2g18_v1_1_0_hd
BRANCHES['mozilla-b2g18_v1_1_0_hd']['repo_path'] = "releases/mozilla-b2g18_v1_1_0_hd"
BRANCHES['mozilla-b2g18_v1_1_0_hd']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['mozharness_talos'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64']['fedora64']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64']['fedora64']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_1_0_hd']['tpn_tests'] = (1, True, TALOS_TP_NEW_OPTS, LINUX64_ONLY)
BRANCHES['mozilla-b2g18_v1_1_0_hd']['tp5o_tests'] = (0, True, TALOS_TP_NEW_OPTS, LINUX64_ONLY)

######### mozilla-b2g26_v1_2
BRANCHES['mozilla-b2g26_v1_2']['repo_path'] = "releases/mozilla-b2g26_v1_2"
BRANCHES['mozilla-b2g26_v1_2']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g26_v1_2']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-b2g26_v1_2']['platforms']['macosx64']['talos_slave_platforms'] = []

######### mozilla-b2g28_v1_3
BRANCHES['mozilla-b2g28_v1_3']['repo_path'] = "releases/mozilla-b2g28_v1_3"
BRANCHES['mozilla-b2g28_v1_3']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g28_v1_3']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-b2g28_v1_3']['platforms']['macosx64']['talos_slave_platforms'] = []

######## try
BRANCHES['try']['repo_path'] = "try"
BRANCHES['try']['xperf_tests'] = (1, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
BRANCHES['try']['tp5o_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['try']['pgo_strategy'] = 'try'
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['platforms']['win32']['xp-ix']['debug_unittest_suites'] = MOCHITEST + REFTEST_NO_IPC + XPCSHELL + CPPUNIT
BRANCHES['try']['platforms']['win32']['win7-ix']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_NOACCEL
BRANCHES['try']['platforms']['win32']['win7-ix']['debug_unittest_suites'] = MOCHITEST + REFTEST_NO_IPC + XPCSHELL + CPPUNIT
BRANCHES['try']['platforms']['linux']['ubuntu32_vm']['debug_unittest_suites'] += MOCHITEST_BC_3[:]
BRANCHES['try']['platforms']['linux64']['ubuntu64_vm']['debug_unittest_suites'] += MOCHITEST_BC_3[:]

######## cedar
BRANCHES['cedar']['platforms']['macosx64']['mavericks']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites'][:]
BRANCHES['cedar']['platforms']['macosx64']['mavericks']['debug_unittest_suites'] = UNITTEST_SUITES['debug_unittest_suites'][:]
BRANCHES['cedar']['platforms']['win32']['xp-ix']['opt_unittest_suites'] += REFTEST_OMTC[:]
BRANCHES['cedar']['platforms']['win32']['win7-ix']['opt_unittest_suites'] += REFTEST_OMTC[:]
BRANCHES['cedar']['platforms']['win32']['win8']['opt_unittest_suites'] += REFTEST_OMTC[:]
BRANCHES['cedar']['platforms']['win32']['xp-ix']['debug_unittest_suites'] += REFTEST_OMTC[:]
BRANCHES['cedar']['platforms']['win32']['win7-ix']['debug_unittest_suites'] += REFTEST_OMTC[:]
BRANCHES['cedar']['platforms']['win32']['win8']['debug_unittest_suites'] += REFTEST_OMTC[:]

# Filter the tests that are enabled on holly for bug 985718.
for platform in BRANCHES['holly']['platforms'].keys():
    if platform not in PLATFORMS:
        continue

    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        slave_p = BRANCHES['holly']['platforms'][platform][slave_platform]
        for suite in ['debug_unittest_suites', 'opt_unittest_suites']:
            slave_p[suite] = MOCHITEST + REFTEST_NO_IPC

# Disable mochitest-browser-chrome on mozilla-b2g branches
for branch in [x for x in BRANCHES.keys() if x.startswith('mozilla-b2g')]:
    for platform in ['linux', 'linux64']:
        if platform not in BRANCHES[branch]['platforms']:
            continue
        for slave_platform in ['fedora', 'fedora64']:
            if slave_platform not in BRANCHES[branch]['platforms'][platform]:
                continue
            slave_p = BRANCHES[branch]['platforms'][platform][slave_platform]
            slave_p['debug_unittest_suites'] = [x for x in slave_p['debug_unittest_suites']
                                                if x[0] if not x[0].startswith('mochitest-browser-chrome')]

# Enable mavericks testing on select branches only
delete_slave_platform(BRANCHES, PLATFORMS, {'macosx64': 'mavericks'}, branch_exclusions=['cedar'])

# Load jetpack for branches that have at least FF21
for name, branch in items_at_least(BRANCHES, 'gecko_version', 21):
    for pf in PLATFORMS:
        if pf not in branch['platforms']:
            continue
        for slave_pf in branch['platforms'][pf].get(
                'slave_platforms', PLATFORMS[pf]['slave_platforms']):
            if slave_pf not in branch['platforms'][pf]:
                continue
            branch['platforms'][pf][slave_pf]['opt_unittest_suites'].append(('jetpack', ['jetpack']))
            branch['platforms'][pf][slave_pf]['debug_unittest_suites'].append(('jetpack', ['jetpack']))

# cppunittest jobs ride the train with 28, so they need to be disabled
# for branches running an older version.
# https://bugzilla.mozilla.org/show_bug.cgi?id=937637
for platform in PLATFORMS.keys():
    for name, branch in items_before(BRANCHES, 'gecko_version', 28):
        if platform not in branch['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in branch['platforms'][platform]:
                continue
            for suite_type in ['opt_unittest_suites', 'debug_unittest_suites']:
                for cpp_suite in CPPUNIT:
                    try:
                        branch['platforms'][platform][slave_platform]['opt_unittest_suites'].remove(cpp_suite)
                        branch['platforms'][platform][slave_platform]['debug_unittest_suites'].remove(cpp_suite)
                    except ValueError:
                        # wasn't in the list anyways
                        pass

# Enable jittests on cedar https://bugzilla.mozilla.org/show_bug.cgi?id=912997
for platform in PLATFORMS.keys():
    # run in chunks on linux only
    if platform in ['linux', 'linux64', 'linux64-asan']:
        jittests = JITTEST_CHUNKED
    else:
        jittests = JITTEST

    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if platform in BRANCHES['cedar']['platforms']:
            if slave_platform in BRANCHES['cedar']['platforms'][platform]:
                if 'fedora' in slave_platform:
                    continue  # Don't use rev3 mini's with this stuff
                BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += jittests[:]
                BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += jittests[:]

        if platform in BRANCHES['try']['platforms']:
            if slave_platform in BRANCHES['try']['platforms'][platform]:
                BRANCHES['try']['platforms'][platform][slave_platform]['opt_unittest_suites'] += jittests[:]
                BRANCHES['try']['platforms'][platform][slave_platform]['debug_unittest_suites'] += jittests[:]

# Enable 3 chunks mochitest-bc on cedar https://bugzilla.mozilla.org/show_bug.cgi?id=819963
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms']:
        continue
    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform not in BRANCHES['cedar']['platforms'][platform]:
            continue
        if BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites']:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_BC_3[:]
        else:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] = MOCHITEST_BC_3[:]
        if BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites']:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_BC_3[:]
        else:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] = MOCHITEST_BC_3[:]

# Enable metro on cedar for now
# This may need to follow the trains: see bug 847442 (comment 73)
BRANCHES['cedar']['platforms']['win32']['win8']['opt_unittest_suites'] += METRO[:]
BRANCHES['cedar']['platforms']['win32']['win8']['debug_unittest_suites'] += METRO[:]

# Enable web-platform-tests on cedar (non-windows only for now)
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms'] or platform.startswith('win'):
        continue

    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform not in BRANCHES['cedar']['platforms'][platform] or slave_platform.startswith('fedora'):
            continue

        BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_TESTS

        BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += WEB_PLATFORM_TESTS

# Enable mozbase unit tests on cedar
# https://bugzilla.mozilla.org/show_bug.cgi?id=971687
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms']:
        continue
    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if 'fedora' in slave_platform:
            continue  # Don't use rev3 mini's with this stuff
        if slave_platform in BRANCHES['cedar']['platforms'][platform]:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOZBASE[:]
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOZBASE[:]

# MERGE DAY: Remove this on 3/17 merge day
NON_UBUNTU_BRANCHES = set([name for name, branch in items_before(BRANCHES, 'gecko_version', 21)])


# Green tests, including mozharness based ones
# Tests listed as Ubuntu tests won't be enabled on Fedora
def get_ubuntu_unittests(branch, test_type):
    UBUNTU_TESTS = {"opt_unittest_suites":
                    ["crashtest", "jsreftest", "jetpack", "crashtest-ipc",
                     "reftest-ipc", "xpcshell", "reftest", "reftest-no-accel",
                     "mochitest-1", "mochitest-2", "mochitest-3",
                     "mochitest-4", "mochitest-5", "mochitest",
                     "mochitest-browser-chrome", "mochitest-other", "cppunit"],
                    "debug_unittest_suites":
                    ["crashtest", "jsreftest", "jetpack", "marionette",
                     "xpcshell", "reftest", "reftest-no-accel", "mochitest-1",
                     "mochitest-2", "mochitest-3", "mochitest-4",
                     "mochitest-5", "mochitest", "mochitest-other", "cppunit"]}
    return list(UBUNTU_TESTS[test_type])

# Remove Ubuntu platform from the release trains,
# use either Fedora or Ubuntu for other branches
for branch in BRANCHES:
    # MERGE DAY: Remove this loop on 3/17 merge day
    if branch in NON_UBUNTU_BRANCHES:
        # Remove Ubuntu completely
        if 'linux64' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['linux64']['ubuntu64_vm']
            BRANCHES[branch]['platforms']['linux64']['slave_platforms'] = ['fedora64']
        if 'linux' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['linux']['ubuntu32_vm']
            BRANCHES[branch]['platforms']['linux']['slave_platforms'] = ['fedora']
        continue

    for p, ubuntu, fedora in [('linux', 'ubuntu32_vm', 'fedora'),
                              ('linux64', 'ubuntu64_vm', 'fedora64')]:
        for suite_type, ubuntu_tests in [('opt_unittest_suites',
                                          get_ubuntu_unittests(branch, 'opt_unittest_suites')),
                                         ('debug_unittest_suites',
                                          get_ubuntu_unittests(branch, 'debug_unittest_suites'))]:
            if nested_haskey(BRANCHES[branch]['platforms'], p, ubuntu,
                             suite_type):
                # Explicitly remove tests listed in ubuntu_tests even though
                # them are not enabled. This would remove old style tests when
                # Ubuntu runs mozharness based tests. (mochitest vs
                # mochitest-{1..5}
                for i in BRANCHES[branch]['platforms'][p][fedora][suite_type]:
                    if i[0] in ubuntu_tests:
                        BRANCHES[branch]['platforms'][p][fedora][suite_type].remove(i)

                for suite in list(BRANCHES[branch]['platforms'][p][ubuntu][suite_type]):
                    if suite[0] not in ubuntu_tests:
                        if branch == "cedar":
                            # Don't disable any Ubuntu test on Cedar
                            continue
                        BRANCHES[branch]['platforms'][p][ubuntu][suite_type].remove(suite)
                    else:
                        for i in BRANCHES[branch]['platforms'][p][fedora][suite_type]:
                            try:
                                if i[0] == suite[0]:
                                    BRANCHES[branch]['platforms'][p][fedora][suite_type].remove(i)
                            except KeyError:
                                pass

# Bug 982225 - mozilla-inbound
BRANCHES['mozilla-inbound']['platforms']['linux']['ubuntu32_vm']['debug_unittest_suites'] += MOCHITEST_BC_3[:]
BRANCHES['mozilla-inbound']['platforms']['linux64']['ubuntu64_vm']['debug_unittest_suites'] += MOCHITEST_BC_3[:]

# TALOS: If you set 'talos_slave_platforms' for a branch you will only get that subset of platforms
for branch in BRANCHES.keys():
    for os in PLATFORMS.keys():  # 'macosx64', 'win32' and on
        if os not in BRANCHES[branch]['platforms'].keys():
            continue
        if BRANCHES[branch]['platforms'][os].get('talos_slave_platforms') is None:
            continue
        platforms_for_os = get_talos_slave_platforms(PLATFORMS, platforms=(os,))
        enabled_platforms_for_os = BRANCHES[branch]['platforms'][os]['talos_slave_platforms']
        for s in SUITES.iterkeys():
            tests_key = '%s_tests' % s
            if tests_key in BRANCHES[branch]:
                tests = list(BRANCHES[branch]['%s_tests' % s])
                tests[3] = [x for x in tests[3] if x not in platforms_for_os or x in enabled_platforms_for_os]
                BRANCHES[branch]['%s_tests' % s] = tuple(tests)

# LOOOOOOOOOOOOOOOPS
# Enable win64 testing on select branches only
WIN64_TESTING_BRANCHES = ['date']
for branch in set(BRANCHES.keys()) - set(WIN64_TESTING_BRANCHES):
    if 'win64' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['win64']

# ASAN builds/tests should ride the trains for gecko 26
for name, branch in items_before(BRANCHES, 'gecko_version', 26):
    if 'linux64-asan' in branch['platforms']:
        del branch['platforms']['linux64-asan']


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
