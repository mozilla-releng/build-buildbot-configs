from copy import deepcopy

import config_common
reload(config_common)
from config_common import TALOS_CMD, loadDefaultValues, loadCustomTalosSuites, \
    loadTalosSuites, nested_haskey, get_talos_slave_platforms

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
    'mozilla-b2g18_v1_1_0_hd': {
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
    'macosx64': {},
    'win32': {},
    'linux': {},
    'linux64': {},
    'win64': {},
}

PLATFORMS['macosx64']['slave_platforms'] = ['snowleopard', 'lion', 'mountainlion']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['snowleopard'] = {'name': "Rev4 MacOSX Snow Leopard 10.6"}
PLATFORMS['macosx64']['lion'] = {'name': "Rev4 MacOSX Lion 10.7"}
PLATFORMS['macosx64']['mountainlion'] = {'name': "Rev5 MacOSX Mountain Lion 10.8"}
PLATFORMS['macosx64']['stage_product'] = 'firefox'
PLATFORMS['macosx64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/mac_config.py',
}

PLATFORMS['win32']['slave_platforms'] = ['xp', 'xp-ix', 'win7', 'win7-ix', 'win8']
PLATFORMS['win32']['talos_slave_platforms'] = ['xp', 'xp-ix', 'win7', 'win7-ix', 'win8']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "Rev3 WINNT 5.1"}
PLATFORMS['win32']['xp-ix'] = {'name': "Windows XP 32-bit"}
PLATFORMS['win32']['win7'] = {'name': "Rev3 WINNT 6.1"}
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

PLATFORMS['win64']['slave_platforms'] = ['win64_vm']
PLATFORMS['win64']['win64_vm'] = {'name': 'win64_vm'}
PLATFORMS['win64']['stage_product'] = 'firefox'
PLATFORMS['win64']['mozharness_config'] = {
    'mozharness_python': ['c:/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/windows_config.py',
}

PLATFORMS['linux']['slave_platforms'] = ['fedora', 'ubuntu32_vm']
PLATFORMS['linux']['talos_slave_platforms'] = ['fedora', 'ubuntu32_hw']
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
PLATFORMS['linux64']['talos_slave_platforms'] = ['fedora64', 'ubuntu64_hw']
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
NO_WINXP = [platform for platform in ALL_TALOS_PLATFORMS if platform != 'xp' and platform != 'xp-ix']
NO_MAC = get_talos_slave_platforms(PLATFORMS, platforms=('linux', 'linux64', 'win32'))
MAC_ONLY = get_talos_slave_platforms(PLATFORMS, platforms=('macosx64',))
WIN7_ONLY = ['win7-ix']

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
    'rafx': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscrollx:tsvgx:tcanvasmark', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'dirtypaint': {
        'enable_by_default': True,
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
}

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'linux': {},
        'linux64': {},
        'macosx64': {},
        'win32': {},
        'win64': {},
    },
}

# MERGE DAY remove this chunk when Firefox 22 is on all branches.
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
# End MERGE DAY

MOCHITEST = [
    ('mochitest-1', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain1'],
        'script_maxtime': 7200,
    }),
    ('mochitest-2', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain2'],
        'script_maxtime': 7200,
    }),
    ('mochitest-3', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain3'],
        'script_maxtime': 7200,
    }),
    ('mochitest-4', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain4'],
        'script_maxtime': 7200,
    }),
    ('mochitest-5', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain5'],
        'script_maxtime': 7200,
    }),
    ('mochitest-browser-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome'],
        'script_maxtime': 9000,
    }),
    ('mochitest-other', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'chrome,a11y,plugins'],
        'script_maxtime': 7200,
    }),
]

REFTEST_NO_IPC = [
    ('reftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest'],
        'script_maxtime': 7200,
    }),
    ('jsreftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'jsreftest'],
        'script_maxtime': 7200,
    }),
    ('crashtest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'crashtest'],
        'script_maxtime': 7200,
    }),
]
REFTEST_NOACCEL = [
    ('reftest-no-accel', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-no-accel'],
        'script_maxtime': 7200,
    }),
]
REFTEST_IPC = [
    ('reftest-ipc', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-ipc'],
        'script_maxtime': 7200,
    }),
    ('crashtest-ipc', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'crashtest-ipc'],
        'script_maxtime': 7200,
    }),
]

XPCSHELL = [
    ('xpcshell', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--xpcshell-suite', 'xpcshell'],
        'script_maxtime': 7200,
    }),
]
MARIONETTE = [
    ('marionette', {
        'use_mozharness': True,
        'script_path': 'scripts/marionette.py',
        'download_symbols': False,
    }),
]
METRO = [
    ('mochitest-metro-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-metro-chrome'],
        'script_maxtime': 7200,
    }),
]

UNITTEST_SUITES = {
    'opt_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL,
    'debug_unittest_suites': MOCHITEST + REFTEST_NO_IPC + XPCSHELL + MARIONETTE,
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
        'xp': {
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
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
            },
        },
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
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
            },
        },
        'win7': {
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
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
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
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
            },
        },
        'win8': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + REFTEST_NOACCEL[:],
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
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
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
        'win64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + REFTEST_NOACCEL[:],
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
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
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
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
            },
        },
        'lion': {
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
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
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
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
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
        'branches': ['mozilla-central'],
        'platforms': {
            'ubuntu64_vm': {'ext': 'linux-x86_64.tar.bz2', 'debug': True},
            'ubuntu32_vm': {'ext': 'linux-i686.tar.bz2', 'debug': True},
            'snowleopard': {'ext': '(mac|mac64).dmg', 'debug': True},
            'lion': {'ext': '(mac|mac64).dmg', 'debug': True},
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
    BRANCHES[branch]['support_url_base'] = 'http://talos-bundles.pvt.build.mozilla.org'
    loadTalosSuites(BRANCHES, SUITES, branch)
    BRANCHES[branch]['pgo_strategy'] = None
    BRANCHES[branch]['pgo_platforms'] = ['linux', 'linux64', 'win32']
    BRANCHES[branch]['mozharness_talos'] = True

# The following are exceptions to the defaults

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'
BRANCHES['mozilla-central']['rafx_tests'] = (1, True, {}, ALL_TALOS_PLATFORMS)

######### mozilla-release
BRANCHES['mozilla-release']['release_tests'] = 1
BRANCHES['mozilla-release']['repo_path'] = "releases/mozilla-release"
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'

# MERGE DAY remove the below when Firefox 25 merges in
BRANCHES['mozilla-release']['mozharness_talos'] = False
BRANCHES['mozilla-release']['xperf_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
# END MERGE DAY remove the below when Firefox 25 merges in

######### mozilla-beta
BRANCHES['mozilla-beta']['release_tests'] = 1
BRANCHES['mozilla-beta']['repo_path'] = "releases/mozilla-beta"
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'

# MERGE DAY remove the below when Firefox 25 merges in
BRANCHES['mozilla-beta']['mozharness_talos'] = False
BRANCHES['mozilla-beta']['xperf_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
# END MERGE DAY remove the below when Firefox 25 merges in

######### mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = "releases/mozilla-aurora"
BRANCHES['mozilla-aurora']['pgo_strategy'] = 'per-checkin'

######### mozilla-esr17
BRANCHES['mozilla-esr17']['release_tests'] = 1
BRANCHES['mozilla-esr17']['repo_path'] = "releases/mozilla-esr17"
BRANCHES['mozilla-esr17']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr17']['mozharness_talos'] = False
BRANCHES['mozilla-esr17']['platforms']['linux']['fedora']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_with_ipc'][:]
BRANCHES['mozilla-esr17']['platforms']['linux']['fedora']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-esr17']['platforms']['linux64']['fedora64']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-esr17']['platforms']['linux64']['fedora64']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-esr17']['platforms']['win32']['xp']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-esr17']['platforms']['win32']['xp']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-esr17']['platforms']['win32']['win7']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_with_no-d2d-d3d'][:]
BRANCHES['mozilla-esr17']['platforms']['win32']['win7']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-esr17']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-esr17']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'][:]
BRANCHES['mozilla-esr17']['platforms']['macosx64']['lion']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-esr17']['platforms']['macosx64']['lion']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'][:]
BRANCHES['mozilla-esr17']['platforms']['macosx64']['mountainlion']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-esr17']['platforms']['macosx64']['mountainlion']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'][:]
BRANCHES['mozilla-esr17']['tpn_tests'] = (1, True, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-esr17']['tp5o_tests'] = (0, True, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
del BRANCHES['mozilla-esr17']['platforms']['win32']['win8']
del BRANCHES['mozilla-esr17']['platforms']['win32']['win7-ix']
del BRANCHES['mozilla-esr17']['platforms']['win32']['xp-ix']
BRANCHES['mozilla-esr17']['platforms']['win32']['talos_slave_platforms'] = ['xp', 'win7']


######### mozilla-b2g18
BRANCHES['mozilla-b2g18']['release_tests'] = 1
BRANCHES['mozilla-b2g18']['repo_path'] = "releases/mozilla-b2g18"
BRANCHES['mozilla-b2g18']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g18']['mozharness_talos'] = False
BRANCHES['mozilla-b2g18']['platforms']['linux']['fedora']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_with_ipc'][:]
BRANCHES['mozilla-b2g18']['platforms']['linux']['fedora']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'] + MARIONETTE
BRANCHES['mozilla-b2g18']['platforms']['linux64']['fedora64']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-b2g18']['platforms']['linux64']['fedora64']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'] + MARIONETTE
BRANCHES['mozilla-b2g18']['platforms']['win32']['xp']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-b2g18']['platforms']['win32']['xp']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-b2g18']['platforms']['win32']['win7']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_with_no-d2d-d3d'][:]
BRANCHES['mozilla-b2g18']['platforms']['win32']['win7']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-b2g18']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18']['platforms']['macosx64']['lion']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18']['platforms']['macosx64']['lion']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18']['platforms']['macosx64']['mountainlion']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18']['platforms']['macosx64']['mountainlion']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18']['tpn_tests'] = (1, True, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-b2g18']['tp5o_tests'] = (0, True, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
del BRANCHES['mozilla-b2g18']['platforms']['win32']['win8']
del BRANCHES['mozilla-b2g18']['platforms']['win32']['win7-ix']
del BRANCHES['mozilla-b2g18']['platforms']['win32']['xp-ix']
BRANCHES['mozilla-b2g18']['platforms']['win32']['talos_slave_platforms'] = ['xp', 'win7']
BRANCHES['mozilla-b2g18']['xperf_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)

######### mozilla-b2g18_v1_0_1
BRANCHES['mozilla-b2g18_v1_0_1']['release_tests'] = 1
BRANCHES['mozilla-b2g18_v1_0_1']['repo_path'] = "releases/mozilla-b2g18_v1_0_1"
BRANCHES['mozilla-b2g18_v1_0_1']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g18_v1_0_1']['mozharness_talos'] = False
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux']['fedora']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_with_ipc'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux']['fedora']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux64']['fedora64']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['linux64']['fedora64']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32']['xp']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32']['xp']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32']['win7']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_with_no-d2d-d3d'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32']['win7']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64']['lion']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64']['lion']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64']['mountainlion']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['macosx64']['mountainlion']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_0_1']['tpn_tests'] = (1, True, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-b2g18_v1_0_1']['tp5o_tests'] = (0, True, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
del BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32']['win8']
del BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32']['win7-ix']
del BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32']['xp-ix']
BRANCHES['mozilla-b2g18_v1_0_1']['platforms']['win32']['talos_slave_platforms'] = ['xp', 'win7']
BRANCHES['mozilla-b2g18_v1_0_1']['xperf_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)

######### mozilla-b2g18_v1_1_0_hd
BRANCHES['mozilla-b2g18_v1_1_0_hd']['release_tests'] = 1
BRANCHES['mozilla-b2g18_v1_1_0_hd']['repo_path'] = "releases/mozilla-b2g18_v1_1_0_hd"
BRANCHES['mozilla-b2g18_v1_1_0_hd']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g18_v1_1_0_hd']['mozharness_talos'] = False
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux']['fedora']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_with_ipc'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux']['fedora']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64']['fedora64']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['linux64']['fedora64']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32']['xp']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32']['xp']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32']['win7']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_with_no-d2d-d3d'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32']['win7']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64']['snowleopard']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64']['lion']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64']['lion']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64']['mountainlion']['opt_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['opt_no_a11y'][:]
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['macosx64']['mountainlion']['debug_unittest_suites'] = BUILDBOT_UNITTEST_SUITES['debug_no_a11y'] + MARIONETTE
BRANCHES['mozilla-b2g18_v1_1_0_hd']['tpn_tests'] = (1, True, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-b2g18_v1_1_0_hd']['tp5o_tests'] = (0, True, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
del BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32']['win8']
del BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32']['win7-ix']
del BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32']['xp-ix']
BRANCHES['mozilla-b2g18_v1_1_0_hd']['platforms']['win32']['talos_slave_platforms'] = ['xp', 'win7']
BRANCHES['mozilla-b2g18_v1_1_0_hd']['xperf_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)

######## try
BRANCHES['try']['xperf_tests'] = (1, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
BRANCHES['try']['tp5o_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['try']['pgo_strategy'] = 'try'
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['platforms']['macosx64']['snowleopard']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_IPC
BRANCHES['try']['platforms']['macosx64']['lion']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_IPC
BRANCHES['try']['platforms']['macosx64']['mountainlion']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_IPC
BRANCHES['try']['platforms']['win32']['xp']['debug_unittest_suites'] = MOCHITEST + REFTEST_NO_IPC + XPCSHELL + MARIONETTE
BRANCHES['try']['platforms']['win32']['xp-ix']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites']
BRANCHES['try']['platforms']['win32']['xp-ix']['debug_unittest_suites'] = MOCHITEST + REFTEST_NO_IPC + XPCSHELL + MARIONETTE
BRANCHES['try']['platforms']['win32']['win7']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_NOACCEL
BRANCHES['try']['platforms']['win32']['win7']['debug_unittest_suites'] = MOCHITEST + REFTEST_NO_IPC + XPCSHELL + MARIONETTE
BRANCHES['try']['platforms']['win32']['win7-ix']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_NOACCEL
BRANCHES['try']['platforms']['win32']['win7-ix']['debug_unittest_suites'] = MOCHITEST + REFTEST_NO_IPC + XPCSHELL + MARIONETTE

# Let's load jetpack for the following branches:
# MERGE DAY once FF21 merges into a branch remove it from this list
for branch in BRANCHES.keys():
    if branch not in ('mozilla-esr17', 'mozilla-b2g18', 'mozilla-b2g18_v1_0_1',
                      'mozilla-b2g18_v1_1_0_hd'):
        for pf in PLATFORMS:
            if pf not in BRANCHES[branch]['platforms'].keys():
                continue
            for slave_pf in BRANCHES[branch]['platforms'][pf].get(
                    'slave_platforms', PLATFORMS[pf]['slave_platforms']):
                if slave_pf not in BRANCHES[branch]['platforms'][pf]:
                    continue
                BRANCHES[branch]['platforms'][pf][slave_pf]['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
                BRANCHES[branch]['platforms'][pf][slave_pf]['debug_unittest_suites'] += [('jetpack', ['jetpack'])]


######## generic branch variables for project branches
for projectBranch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[projectBranch]
    loadDefaultValues(BRANCHES, projectBranch, branchConfig)
    loadCustomTalosSuites(BRANCHES, SUITES, projectBranch, branchConfig)

# Enable metro jobs for now
# MERGE DAY: This may need to follow the trains: see bug 847442
BRANCHES['cedar']['platforms']['win32']['win8']['debug_unittest_suites'] += METRO[:]
for branch in BRANCHES.keys():
    if branch not in ('mozilla-aurora', 'mozilla-beta', 'mozilla-release',
                      'mozilla-esr17', 'mozilla-b2g18', 'mozilla-b2g18_v1_0_0',
                      'mozilla-b2g18_v1_0_1', 'mozilla-b2g18_v1_1_0_hd'):
        if 'win32' in BRANCHES[branch]['platforms'] and \
                'win8' in BRANCHES[branch]['platforms']['win32']:
            BRANCHES[branch]['platforms']['win32']['win8']['opt_unittest_suites'] += METRO[:]

# MERGE DAY NOTE: remove v21 based branches from the list below
NON_UBUNTU_BRANCHES = ("mozilla-esr17", "mozilla-b2g18",
                       "mozilla-b2g18_v1_0_1", "mozilla-b2g18_v1_1_0_hd")


# Green tests, including mozharness based ones
# Tests listed as Ubuntu tests won't be enabled on Fedora
def get_ubuntu_unittests(branch, test_type):
    UBUNTU_TESTS = {"opt_unittest_suites":
                    ["crashtest", "jsreftest", "jetpack", "crashtest-ipc",
                     "reftest-ipc", "xpcshell", "reftest", "reftest-no-accel",
                     "mochitest-1", "mochitest-2", "mochitest-3",
                     "mochitest-4", "mochitest-5", "mochitest"],
                    "debug_unittest_suites":
                    ["crashtest", "jsreftest", "jetpack", "marionette",
                     "xpcshell", "reftest", "reftest-no-accel", "mochitest-1",
                     "mochitest-2", "mochitest-3", "mochitest-4",
                     "mochitest-5", "mochitest"]}
    # MERGE DAY: uplift when Firefox 24 merges in
    FF24_TESTS = {"opt_unittest_suites":
                  ["mochitest-browser-chrome", "mochitest-other"],
                  "debug_unittest_suites": ["mochitest-other"]}
    if branch not in ("mozilla-release"):
        return UBUNTU_TESTS[test_type] + FF24_TESTS[test_type]
    else:
        return list(UBUNTU_TESTS[test_type])


# Remove Ubuntu platform from the release trains,
# use either Fedora or Ubuntu for other branches
for branch in BRANCHES:
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

# MERGE DAY: remove branches when Firefox 23 merges in
NON_UBUNTU_TALOS_BRANCHES = ("mozilla-esr17", "mozilla-b2g18")
for branch in set(BRANCHES.keys()) - set(NON_UBUNTU_TALOS_BRANCHES):
    for s in SUITES.iterkeys():
        if nested_haskey(BRANCHES[branch], 'suites', s, 'options'):
            options = list(BRANCHES[branch]['suites'][s]['options'])
            # filter out fedora
            options[1] = [x for x in options[1] if x not in ('fedora', 'fedora64')]
            BRANCHES[branch]['suites'][s]['options'] = tuple(options)
        tests_key = '%s_tests' % s
        if tests_key in BRANCHES[branch]:
            tests = list(BRANCHES[branch]['%s_tests' % s])
            tests[3] = [x for x in tests[3] if x not in ('fedora', 'fedora64')]
            BRANCHES[branch]['%s_tests' % s] = tuple(tests)

# MERGE DAY: remove branches when Firefox 23 merges in
WIN32_REV3_BRANCHES = ("mozilla-esr17", "mozilla-b2g18", "mozilla-b2g18_v1_0_1")
# Disable Rev3 winxp and win7 machines for FF23+
for branch in set(BRANCHES.keys()) - set(WIN32_REV3_BRANCHES):
    if 'win32' not in BRANCHES[branch]['platforms']:
        continue
    del BRANCHES[branch]['platforms']['win32']['xp']
    del BRANCHES[branch]['platforms']['win32']['win7']
    if 'talos_slave_platforms' not in BRANCHES[branch]['platforms']['win32']:
        BRANCHES[branch]['platforms']['win32']['talos_slave_platforms'] = ['xp-ix', 'win7-ix', 'win8']

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
WIN64_TESTING_BRANCHES = ('date', 'try')
for branch in set(BRANCHES.keys()) - set(WIN64_TESTING_BRANCHES):
    if 'win64' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['win64']

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
