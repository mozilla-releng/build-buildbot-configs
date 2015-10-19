from copy import deepcopy

import config_common
reload(config_common)
from config_common import loadDefaultValues, loadCustomTalosSuites, \
    get_talos_slave_platforms, delete_slave_platform

import master_common
reload(master_common)
from master_common import setMainFirefoxVersions, items_before, items_at_least

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS, GRAPH_CONFIG

import config_seta
reload(config_seta)
from config_seta import loadSkipConfig

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
    'mozilla-esr38': {
        'gecko_version': 38,
        'platforms': {
            'macosx64': {},
            'win32': {},
            'win64': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g37_v2_2': {
        'datazilla_url': None,
        'gecko_version': 37,
        'platforms': {
            # desktop per sicking in Bug 829513
            'macosx64': {},
            'win32': {},
            'linux': {},
            'linux64': {},
        },
        'lock_platforms': True,
    },
    'try': {
        'coallesce_jobs': False,
    },
}

TWIGS = [x for x in ACTIVE_PROJECT_BRANCHES if x not in ('mozilla-inbound', 'fx-team', 'b2g-inbound')]

setMainFirefoxVersions(BRANCHES)

# Talos
PLATFORMS = {
    'linux': {},
    'linux64': {},
    'linux64-asan': {},
    'linux64-cc': {},
    'linux64-tsan': {},
    'macosx64': {},
    'win32': {},
    'win64': {},
}

PLATFORMS['macosx64']['slave_platforms'] = ['snowleopard', 'yosemite', 'yosemite_r7']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['snowleopard'] = {'name': "Rev4 MacOSX Snow Leopard 10.6"}
PLATFORMS['macosx64']['yosemite'] = {'name': "Rev5 MacOSX Yosemite 10.10",
                                     'try_by_default': False}
PLATFORMS['macosx64']['yosemite_r7'] = {'name': "Rev5 MacOSX Yosemite 10.10.5",
                                     'try_by_default': False} 
PLATFORMS['macosx64']['stage_product'] = 'firefox'
PLATFORMS['macosx64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/mac_config.py',
}
PLATFORMS['macosx64']['talos_slave_platforms'] = ['yosemite', 'yosemite_r7']

PLATFORMS['win32']['slave_platforms'] = ['xp-ix', 'win7-ix']
PLATFORMS['win32']['talos_slave_platforms'] = ['xp-ix', 'win7-ix']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp-ix'] = {'name': "Windows XP 32-bit"}
PLATFORMS['win32']['win7-ix'] = {'name': "Windows 7 32-bit"}
PLATFORMS['win32']['stage_product'] = 'firefox'
PLATFORMS['win32']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '32',
    'config_file': 'talos/windows_config.py',
}

PLATFORMS['win64']['slave_platforms'] = ['win8_64', 'win10_64']
PLATFORMS['win64']['talos_slave_platforms'] = ['win8_64', 'win10_64']
PLATFORMS['win64']['env_name'] = 'win64-perf'
PLATFORMS['win64']['stage_product'] = 'firefox'
PLATFORMS['win64']['win8_64'] = {'name': 'Windows 8 64-bit'}
PLATFORMS['win64']['win10_64'] = {'name': 'Windows 10 64-bit',
                                  'try_by_default': False}
PLATFORMS['win64']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/windows_config.py',
}

PLATFORMS['linux']['slave_platforms'] = ['ubuntu32_vm']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['ubuntu32_vm'] = {'name': 'Ubuntu VM 12.04'}
PLATFORMS['linux']['stage_product'] = 'firefox'
PLATFORMS['linux']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '32',
    'config_file': 'talos/linux_config.py',
}


PLATFORMS['linux64']['slave_platforms'] = ['ubuntu64_vm', 'ubuntu64_vm_lnx_large']
PLATFORMS['linux64']['talos_slave_platforms'] = ['ubuntu64_hw']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['ubuntu64_vm'] = {'name': 'Ubuntu VM 12.04 x64'}
PLATFORMS['linux64']['ubuntu64_hw'] = {'name': 'Ubuntu HW 12.04 x64'}
PLATFORMS['linux64']['ubuntu64_vm_lnx_large'] = {'name': 'Ubuntu VM large 12.04 x64'}
PLATFORMS['linux64']['stage_product'] = 'firefox'
PLATFORMS['linux64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64-asan']['slave_platforms'] = ['ubuntu64-asan_vm', 'ubuntu64-asan_vm_lnx_large']
PLATFORMS['linux64-asan']['ubuntu64-asan_vm'] = {'name': 'Ubuntu ASAN VM 12.04 x64'}
PLATFORMS['linux64-asan']['ubuntu64-asan_vm_lnx_large'] = {'name': 'Ubuntu ASAN VM large 12.04 x64'}
PLATFORMS['linux64-asan']['stage_product'] = 'firefox'
PLATFORMS['linux64-asan']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64-tsan']['slave_platforms'] = ['ubuntu64_vm', 'ubuntu64_vm_lnx_large']
PLATFORMS['linux64-tsan']['ubuntu64_vm'] = {
    'name': 'Ubuntu TSAN VM 12.04 x64',
    'build_dir_prefix': 'ubuntu64_vm_tsan',
    'scheduler_slave_platform_identifier': 'ubuntu64_vm_tsan'
}
PLATFORMS['linux64-tsan']['ubuntu64_vm_lnx_large'] = {
    'name': 'Ubuntu TSAN VM large 12.04 x64',
    'build_dir_prefix': 'ubuntu64_vm_large_tsan',
    'scheduler_slave_platform_identifier': 'ubuntu64_vm_large_tsan'
}
PLATFORMS['linux64-tsan']['stage_product'] = 'firefox'
PLATFORMS['linux64-tsan']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64-cc']['slave_platforms'] = ['ubuntu64_vm', 'ubuntu64_vm_lnx_large' ]
PLATFORMS['linux64-cc']['ubuntu64_vm'] = {
    'name': 'Ubuntu Code Coverage VM 12.04 x64',
    'build_dir_prefix': 'ubuntu64_vm_cc',
    'scheduler_slave_platform_identifier': 'ubuntu64_vm_cc'
}
PLATFORMS['linux64-cc']['ubuntu64_vm_lnx_large'] = {
    'name': 'Ubuntu Code Coverage VM large 12.04 x64',
    'build_dir_prefix': 'ubuntu64_vm_large_cc',
    'scheduler_slave_platform_identifier': 'ubuntu64_vm_large_cc'
}
PLATFORMS['linux64-cc']['stage_product'] = 'firefox'
PLATFORMS['linux64-cc']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
    'extra_args': ['--code-coverage'],
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

ALL_TALOS_PLATFORMS = get_talos_slave_platforms(PLATFORMS, platforms=('linux64', 'win32', 'macosx64', 'win64', ))
LINUX_ONLY = get_talos_slave_platforms(PLATFORMS, platforms=('linux64', ))
NO_WINXP = [platform for platform in ALL_TALOS_PLATFORMS if platform != 'xp-ix']
NO_OSX = get_talos_slave_platforms(PLATFORMS, platforms=('linux64', 'win32', 'win64'))
WIN7_ONLY = ['win7-ix']

SUITES = {
    'xperf': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5n', '--sampleConfig', 'xperf.config', '--mozAfterPaint', '--xperf_path',
                                  '"c:/Program Files/Microsoft Windows Performance Toolkit/xperf.exe"', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, WIN7_ONLY),
    },
    'xperf-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5n', '--sampleConfig', 'xperf.config', '--mozAfterPaint', '--xperf_path',
                                  '"c:/Program Files/Microsoft Windows Performance Toolkit/xperf.exe"', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, WIN7_ONLY),
    },
    'tp5o': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o', '--mozAfterPaint', '--responsiveness', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'tp5o-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o', '--mozAfterPaint', '--responsiveness', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g1': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o_scroll', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g1-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o_scroll', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g2': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'damp', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g2-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'damp', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g3': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_dom'],
        'options': ({}, LINUX_ONLY),
    },
    'g3-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_dom'],
        'options': ({}, LINUX_ONLY),
    },
    'other': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscrollr:a11yr:ts_paint:tpaint', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'other-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscrollr:a11yr:ts_paint:tpaint', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'svgr': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvgr:tsvgr_opacity', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'svgr-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvgr:tsvgr_opacity', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, NO_WINXP),
    },
    'dromaeojs': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom:kraken:v8_7'],
        'options': ({}, NO_WINXP),
    },
    'dromaeojs-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom:kraken:v8_7'],
        'options': ({}, NO_OSX),
    },
    'chromez': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tresize', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'chromez-e10s': {
        'enable_by_default': False,
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
        'linux64-asan': {},
        'linux64-cc': {},
        'linux64-tsan': {},
        'macosx64': {},
        'win32': {},
        'win64': {},
    },
}

### The below section contains definitions for all of the test suites
### available for desktop testing.

### CPP Unit Tests ###
CPPUNIT = [
    ('cppunit', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--cppunittest-suite', 'cppunittest'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

GTEST = [
    ('gtest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--gtest-suite', 'gtest'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

### Jit Tests ###
JITTEST = [
    ('jittest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--jittest-suite', 'jittest'],
        'script_maxtime': 7200,
    }),
]

JITTEST_CHUNKED = [
    ('jittest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--jittest-suite', 'jittest-chunked'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 2,
    }),
]

### Luciddream ###
LUCIDDREAM = [
    ('luciddream', {
        'use_mozharness': True,
        'script_path': 'scripts/luciddream_unittest.py',
        'script_maxtime': 7200,
        'blob_upload': True,
    }),
]

### Marionette ###
MARIONETTE = [
    ('marionette', {
        'use_mozharness': True,
        'script_path': 'scripts/marionette.py',
        'download_symbols': False,
        'blob_upload': True,
    }),
]

MARIONETTE_E10S = [
    ('marionette-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/marionette.py',
        'extra_args': ['--e10s'],
        'download_symbols': False,
        'blob_upload': True,
    }),
]

MEDIATESTS = [
    ('media-tests', {
        'use_mozharness': True,
        'script_path': 'scripts/firefox_media_tests_buildbot.py',
        'blob_upload': True,
    }),
]

MEDIA_YOUTUBE_TESTS = [
    ('media-youtube-tests', {
        'use_mozharness': True,
        'script_path': 'scripts/firefox_media_tests_buildbot.py',
        'extra_args': ['--suite', 'media-youtube-tests'],
        'blob_upload': True,
    }),
]

### Mochitests (Browser-Chrome) ###
MOCHITEST_BC = [
    ('mochitest-browser-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome'],
        'blob_upload': True,
        'script_maxtime': 12000,
    }),
]

MOCHITEST_BC_3 = [
    ('mochitest-browser-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome-chunked'],
        'blob_upload': True,
        'script_maxtime': 12000,
        'totalChunks': 3,
    }),
]

MOCHITEST_BC_7 = [
    ('mochitest-browser-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome-chunked'],
        'blob_upload': True,
        'script_maxtime': 12000,
        'totalChunks': 7,
    }),
]

MOCHITEST_BC_3_E10S = [
    ('mochitest-e10s-browser-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome-chunked', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 12000,
        'totalChunks': 3,
    }),
]

MOCHITEST_BC_7_E10S = [
    ('mochitest-e10s-browser-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome-chunked', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 12000,
        'totalChunks': 7,
    }),
]

### Mochitests (Devtools) ###
MOCHITEST_DT_2 = [
    ('mochitest-devtools-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-devtools-chrome'],
        'blob_upload': True,
        'script_maxtime': 4800,
        'totalChunks': 2,
    }),
]

MOCHITEST_DT_2_E10S = [
    ('mochitest-e10s-devtools-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-devtools-chrome', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 4800,
        'totalChunks': 2,
    }),
]

MOCHITEST_DT_4 = [
    ('mochitest-devtools-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-devtools-chrome-chunked'],
        'blob_upload': True,
        'script_maxtime': 4800,
        'totalChunks': 4,
    }),
]

MOCHITEST_DT_8 = [
    ('mochitest-devtools-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-devtools-chrome-chunked'],
        'blob_upload': True,
        'script_maxtime': 4800,
        'totalChunks': 8,
    }),
]

### Mochitests (Plain) ###
MOCHITEST_CSB = [
    ('mochitest-csb', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain-chunked', '--strict-content-sandbox'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 5,
    }),
]

MOCHITEST_E10S = [
    ('mochitest-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain-chunked', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 5,
    }),
]

MOCHITEST_WO_BC = [
    ('mochitest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain-chunked'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 5,
    }),
]

### Mochitest (Other Miscellaneous Suites) ###
MOCHITEST_JP = [
    ('mochitest-jetpack', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'jetpack-package', '--mochitest-suite', 'jetpack-addon'],
        'blob_upload': True,
        'script_maxtime': 12000,
    }),
]

MOCHITEST_OTHER = [
    ('mochitest-other', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'chrome,a11y'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

MOCHITEST_A11Y   = [
    ('mochitest-a11y', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'a11y'],
        'blob_upload': True,
        'script_maxtime': 1800,
    }),
]

MOCHITEST_CHROME = [
    ('mochitest-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'chrome-chunked'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 3,
    }),
]

MOCHITEST_PUSH = [
    ('mochitest-push', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-push'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

MOCHITEST_WEBGL = [
    ('mochitest-gl', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-gl'],
        'blob_upload': True,
        'script_maxtime': 12000,
    }),
]

### Mochitest Combinations ###
MOCHITEST_PLAIN = MOCHITEST_WO_BC[:]
MOCHITEST = MOCHITEST_WO_BC[:] + MOCHITEST_OTHER
MOCHITEST_WO_BC += MOCHITEST_OTHER

### Mozbase ###
MOZBASE = [
    ('mozbase', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mozbase-suite', 'mozbase'],
        'script_maxtime': 7200,
    }),
]

### Reftests ###
CRASHTEST_E10S = [
    ('crashtest-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'crashtest', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

OTHER_REFTESTS = [
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

REFTEST_E10S = [
    ('reftest-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

REFTEST_E10S_TWO_CHUNKS = [
    ('reftest-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 2,
    }),
]

REFTEST_ONE_CHUNK = [
    ('reftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

REFTEST_TWO_CHUNKS = [
    ('reftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 2,
    }),
]

REFTEST_FOUR_CHUNKS = [
    ('reftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 4,
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

REFTEST_NOACCEL_TWO_CHUNKS = [
    ('reftest-no-accel', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-no-accel'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 2,
    }),
]

### Web Platform Tests ###
WEB_PLATFORM_REFTESTS = [
    ('web-platform-tests-reftests', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=reftest"],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_TESTS = [
    ('web-platform-tests', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness"],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_TESTS_CHUNKED = [
    ('web-platform-tests', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness"],
        'totalChunks': 4,
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_TESTS_CHUNKED_MORE = [
    ('web-platform-tests', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness"],
        'totalChunks': 8,
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_REFTESTS_E10S = [
    ('web-platform-tests-reftests-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=reftest", "--e10s"],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_TESTS_E10S = [
    ('web-platform-tests-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness", "--e10s"],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_TESTS_CHUNKED_E10S = [
    ('web-platform-tests-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness", "--e10s"],
        'totalChunks': 4,
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S = [
    ('web-platform-tests-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness", "--e10s"],
        'totalChunks': 8,
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

### XPCShell ###
XPCSHELL = [
    ('xpcshell', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--xpcshell-suite', 'xpcshell'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

XPCSHELL_TWO_CHUNKS = [
    ('xpcshell', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--xpcshell-suite', 'xpcshell'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 2,
    }),
]


### Default Test Suites For All Platforms ###
# The below test suites will run across all platforms and trees. Many platforms
# will additionally require other various suites to be run, which are set in the
# sections below.
UNITTEST_SUITES = {
    'opt_unittest_suites': CPPUNIT + MOCHITEST + MOCHITEST_DT_2 + OTHER_REFTESTS + MOCHITEST_WEBGL + \
                           XPCSHELL,
    'debug_unittest_suites': CPPUNIT + MARIONETTE + MOCHITEST + MOCHITEST_DT_4 + MOCHITEST_WEBGL + \
                             OTHER_REFTESTS,
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
        'ubuntu32_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST_CHUNKED + \
                                   MARIONETTE + REFTEST_NOACCEL_TWO_CHUNKS + REFTEST_TWO_CHUNKS + \
                                   WEB_PLATFORM_REFTESTS + WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + JITTEST_CHUNKED + \
                                     REFTEST_FOUR_CHUNKS + XPCSHELL_TWO_CHUNKS,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
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
                'gtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
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
        'ubuntu64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST_CHUNKED + \
                                   MARIONETTE + REFTEST_NOACCEL_TWO_CHUNKS + REFTEST_TWO_CHUNKS + \
                                   WEB_PLATFORM_REFTESTS + WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + JITTEST_CHUNKED + \
                                    REFTEST_FOUR_CHUNKS + XPCSHELL_TWO_CHUNKS,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
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
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'luciddream': {
                    'config_files': ["luciddream/linux_config.py"],
                },
            },
        },
        'ubuntu64_vm_lnx_large': {
           'opt_unittest_suites': [], 
           'debug_unittest_suites': [], 
           'suite_config': {
               'gtest': {
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST_CHUNKED + \
                                   REFTEST_TWO_CHUNKS,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + JITTEST_CHUNKED + \
                                     REFTEST_FOUR_CHUNKS + XPCSHELL_TWO_CHUNKS,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
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
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
        },
        'ubuntu64-asan_vm_lnx_large': {
           'opt_unittest_suites': [],
           'debug_unittest_suites': [],
           'suite_config': {
               'gtest': {
                   'config_files': ["unittests/linux_unittest.py"],
               },
           },
        },
    },
    'linux64-tsan': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST_CHUNKED + \
                                   REFTEST_TWO_CHUNKS,
            'debug_unittest_suites': [],
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
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
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
        },
        'ubuntu64_vm_lnx_large': {
           'opt_unittest_suites': [],
           'debug_unittest_suites': [],
           'suite_config': {
               'gtest': {
                   'config_files': ["unittests/linux_unittest.py"],
               },
           },
        },
    },
    'linux64-cc': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST_CHUNKED + \
                                   REFTEST_TWO_CHUNKS,
            'debug_unittest_suites': [],
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
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
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
        },
        'ubuntu64_vm_lnx_large': {
           'opt_unittest_suites': [],
           'debug_unittest_suites': [],
           'suite_config': {
               'gtest': {
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST + \
                                   MARIONETTE + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + JITTEST + \
                                     REFTEST_ONE_CHUNK + XPCSHELL,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-csb': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-omtc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
            },
        },
        'win7-ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + JITTEST + \
                                     REFTEST_ONE_CHUNK + XPCSHELL,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-csb': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-omtc': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + JITTEST + \
                                     REFTEST_ONE_CHUNK + XPCSHELL,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-csb': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
            },
        },
        'win10_64': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + JITTEST + \
                                     REFTEST_ONE_CHUNK + XPCSHELL,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-csb': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
            },
        },
    },
    'macosx64': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'snowleopard': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + JITTEST + REFTEST_ONE_CHUNK,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + JITTEST + \
                                     REFTEST_ONE_CHUNK + XPCSHELL,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
        'yosemite': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + REFTEST_ONE_CHUNK,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + REFTEST_ONE_CHUNK + \
                                     XPCSHELL,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
        'yosemite_r7': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:] + REFTEST_ONE_CHUNK,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:] + REFTEST_ONE_CHUNK + \
                                     XPCSHELL,
            'suite_config': {
                'mochitest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-push': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-devtools-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-devtools-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-gl': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
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
            'ubuntu64_vm': {
                'ext': 'linux-x86_64.tar.bz2',
                'env': 'linux-perf',
                'debug': True
            },
            'ubuntu64-asan_vm': {
                'ext': 'linux-x86_64-asan.tar.bz2',
                'env': 'linux-perf',
                'debug': False
            },
            'ubuntu32_vm': {
                'ext': 'linux-i686.tar.bz2',
                'env': 'linux-perf',
                'debug': True
            },
            'snowleopard': {'ext': '(mac|mac64).dmg', 'debug': True},
            'yosemite': {'ext': '(mac|mac64).dmg', 'debug': True},
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
BRANCHES['mozilla-central']['xperf-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
BRANCHES['mozilla-central']['tp5o-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-central']['g1-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, NO_OSX)
#BRANCHES['mozilla-central']['g1-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-central']['g2-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-central']['g3_tests'] = (1, False, {}, LINUX_ONLY)
BRANCHES['mozilla-central']['g3-e10s_tests'] = (1, False, {}, LINUX_ONLY)
BRANCHES['mozilla-central']['other-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-central']['svgr-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-central']['dromaeojs-e10s_tests'] = (1, False, {}, NO_OSX)
#BRANCHES['mozilla-central']['dromaeojs-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-central']['chromez-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)


######### mozilla-inbound
# no xperf here since it fails all the time
BRANCHES['mozilla-inbound']['xperf-e10s_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
BRANCHES['mozilla-inbound']['tp5o-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-inbound']['g1-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, NO_OSX)
#BRANCHES['mozilla-inbound']['g1-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-inbound']['g2-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-inbound']['g3_tests'] = (1, False, {}, LINUX_ONLY)
BRANCHES['mozilla-inbound']['g3-e10s_tests'] = (1, False, {}, LINUX_ONLY)
BRANCHES['mozilla-inbound']['other-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-inbound']['svgr-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-inbound']['dromaeojs-e10s_tests'] = (1, False, {}, NO_OSX)
#BRANCHES['mozilla-inbound']['dromaeojs-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['mozilla-inbound']['chromez-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)


######### fx-team
# no xperf here since it fails all the time
BRANCHES['fx-team']['xperf-e10s_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
BRANCHES['fx-team']['tp5o-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['fx-team']['g1-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, NO_OSX)
#BRANCHES['fx-team']['g1-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['fx-team']['g2-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['fx-team']['other-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['fx-team']['g3_tests'] = (1, False, {}, LINUX_ONLY)
BRANCHES['fx-team']['g3-e10s_tests'] = (1, False, {}, LINUX_ONLY)
BRANCHES['fx-team']['svgr-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['fx-team']['dromaeojs-e10s_tests'] = (1, False, {}, NO_OSX)
#BRANCHES['fx-team']['dromaeojs-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['fx-team']['chromez-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)


######### mozilla-release
BRANCHES['mozilla-release']['repo_path'] = "releases/mozilla-release"
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-release']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-release']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['mozilla-release']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['mozilla-release']['platforms']['linux64']['talos_slave_platforms'] = []
BRANCHES['mozilla-release']['platforms']['win64']['talos_slave_platforms'] = []

######### mozilla-beta
BRANCHES['mozilla-beta']['repo_path'] = "releases/mozilla-beta"
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'

######### mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = "releases/mozilla-aurora"
BRANCHES['mozilla-aurora']['pgo_strategy'] = 'per-checkin'

######### mozilla-esr38
BRANCHES['mozilla-esr38']['repo_path'] = "releases/mozilla-esr38"
BRANCHES['mozilla-esr38']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr38']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr38']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr38']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr38']['platforms']['linux64']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr38']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr38']['platforms']['win64']['talos_slave_platforms'] = []

######### mozilla-b2g37_v2_2
BRANCHES['mozilla-b2g37_v2_2']['repo_path'] = "releases/mozilla-b2g37_v2_2"
BRANCHES['mozilla-b2g37_v2_2']['pgo_strategy'] = None
BRANCHES['mozilla-b2g37_v2_2']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-b2g37_v2_2']['platforms']['macosx64']['slave_platforms'] = ['snowleopard']
BRANCHES['mozilla-b2g37_v2_2']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['mozilla-b2g37_v2_2']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['mozilla-b2g37_v2_2']['platforms']['linux64']['talos_slave_platforms'] = []


######## try
BRANCHES['try']['repo_path'] = "try"
BRANCHES['try']['xperf_tests'] = (1, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
BRANCHES['try']['tp5o_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['try']['other_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['try']['g1_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['try']['g2_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['try']['g3_tests'] = (1, False, {}, LINUX_ONLY)
BRANCHES['try']['pgo_strategy'] = None
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['platforms']['macosx64']['yosemite_r7']['opt_unittest_suites'] = UNITTEST_SUITES['opt_unittest_suites'][:]
BRANCHES['try']['platforms']['macosx64']['yosemite_r7']['debug_unittest_suites'] = UNITTEST_SUITES['debug_unittest_suites'][:]

# now for e10s tests
# no xperf here since it fails all the time
BRANCHES['try']['xperf-e10s_tests'] = (0, False, TALOS_TP_NEW_OPTS, WIN7_ONLY)
BRANCHES['try']['tp5o-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['try']['g1-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, NO_OSX)
#BRANCHES['try']['g1-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['try']['g2-e10s_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)
BRANCHES['try']['g3-e10s_tests'] = (1, False, {}, LINUX_ONLY)
BRANCHES['try']['other-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['try']['svgr-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['try']['dromaeojs-e10s_tests'] = (1, False, {}, NO_OSX)
#BRANCHES['try']['dromaeojs-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
BRANCHES['try']['chromez-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)


loadSkipConfig(BRANCHES,"desktop")


### Tests Enabled In Gecko 39+ ###

# Luciddream on Linux64 opt only
for platform in PLATFORMS.keys():
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in ['ubuntu64_vm']:
                continue
            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += LUCIDDREAM[:]

# mochitest-jetpack everywhere except on versioned B2G branches
for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
    if name.startswith('mozilla-b2g'):
        continue
    for pf in PLATFORMS:
        if pf not in branch['platforms']:
            continue
        for slave_pf in branch['platforms'][pf].get(
                'slave_platforms', PLATFORMS[pf]['slave_platforms']):
            if slave_pf not in branch['platforms'][pf]:
                continue
            branch['platforms'][pf][slave_pf]['opt_unittest_suites'] += MOCHITEST_JP[:]
            branch['platforms'][pf][slave_pf]['debug_unittest_suites'] += MOCHITEST_JP[:]

# web-platform-tests on OS X 10.10
for platform in PLATFORMS.keys():
    if platform not in ['macosx64']:
        continue
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:

            # These are not stable enough on OS X 10.6
            if slave_platform == "snowleopard":
                continue

            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += \
                        WEB_PLATFORM_TESTS_CHUNKED[:] + WEB_PLATFORM_REFTESTS[:]


### Tests Enabled in Gecko 40+ ###

# Bug 1165962 - Use more chunks for mochitest-dt on linux32 debug
# Bug 1214853 - Use more chunks for mochitest-dt on linux64 debug
for platform in PLATFORMS.keys():
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 40):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in ('ubuntu32_vm', 'ubuntu64_vm'):
                continue
            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    debug_suites = BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites']
                    debug_suites = [x for x in debug_suites if x[0] and x[0] != 'mochitest-devtools-chrome']
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] = debug_suites + MOCHITEST_DT_8[:]

# Bug 1156421 - Use more chunks for mochitest-dt on ASAN
for platform in PLATFORMS.keys():
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 40):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in ('ubuntu64-asan_vm',):
                continue
            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    opt_suites = BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites']
                    opt_suites = [x for x in opt_suites if x[0] and x[0] != 'mochitest-devtools-chrome']
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] = opt_suites + MOCHITEST_DT_4[:]

# Bug 1156357 - Enable mochitest-push to ride the trains
for platform in PLATFORMS.keys():
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 40):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_PUSH
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites']+= MOCHITEST_PUSH

# Talos g2 for all talos platforms
for name, branch in items_at_least(BRANCHES, 'gecko_version', 40):
    if name.startswith('mozilla-b2g'):
        continue
    branch['g2_tests'] = (1, False, TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS)


### Tests Enabled in Gecko 42+ ###

# Debug web-platform-tests
for platform in PLATFORMS.keys():
    if platform not in ['linux', 'linux64', 'macosx64', 'win32', 'win64']:
        continue
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 42):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:

            # These are not stable enough on OS X 10.6
            if slave_platform == "snowleopard":
                continue

            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] += \
                        WEB_PLATFORM_TESTS_CHUNKED_MORE[:] + WEB_PLATFORM_REFTESTS

### Tests Enabled in Gecko 44+ ###
# mochitest a11y/chrome instead of other
for platform in PLATFORMS.keys():
    if platform not in ['linux', 'linux64', 'linux64-asan', 'linux64-tsan', 'linux64-cc',
                        'macosx64', 'win32', 'win64']:
        continue

    for name, branch in items_at_least(BRANCHES, 'gecko_version', 44):
        for test_platform in PLATFORMS[platform]['slave_platforms']:

            platforms = BRANCHES[name]['platforms']
            if platform in platforms:
                if test_platform in platforms[platform]:
                    platforms[platform][test_platform]['debug_unittest_suites'] += MOCHITEST_A11Y
                    platforms[platform][test_platform]['debug_unittest_suites'] += MOCHITEST_CHROME
                    platforms[platform][test_platform]['opt_unittest_suites'] += MOCHITEST_CHROME
                    platforms[platform][test_platform]['opt_unittest_suites'] += MOCHITEST_A11Y
                    for item in platforms[platform][test_platform]['debug_unittest_suites']:
                        if item[0] == 'mochitest-other':
                            platforms[platform][test_platform]['debug_unittest_suites'].remove(item)

                    for item in platforms[platform][test_platform]['opt_unittest_suites']:
                        if item[0] == 'mochitest-other':
                            platforms[platform][test_platform]['opt_unittest_suites'].remove(item)

### Tests Enabled in Gecko 43+ ###

# On trunk and Aurora:
#   Enable e10s Linux mochitests
#   Enable e10s browser-chrome mochitests, opt builds only for all platforms (not ready for Xp).
#   Enable e10s devtools tests for Linux opt
#   Enable e10s reftests/crashtests for Linux opt
#   Enable e10s marionette tests for Linux32 opt
#   Enable e10s web-platform-tests
# Fix this to a certain gecko version once e10s starts riding the trains
# Bug 1200437 - Use 7 chunks for m-e10-bc on branches > trunk, excluding twigs, 3 chunks elsewhere
aurora_gecko_version = BRANCHES['mozilla-aurora']['gecko_version']
trunk_gecko_version = BRANCHES['mozilla-central']['gecko_version']
for name, branch in items_at_least(BRANCHES, 'gecko_version', aurora_gecko_version):
    for platform in PLATFORMS.keys():
        if platform not in branch['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if platform in branch['platforms'] and slave_platform in branch['platforms'][platform] and \
                    not slave_platform == 'xp-ix':
                if name in TWIGS or ('gecko_version' in branch and branch['gecko_version'] != trunk_gecko_version):
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_BC_3_E10S[:]
                else:
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_BC_7_E10S[:]
            if platform in ('linux', 'linux64', 'linux64-asan'):
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_E10S[:]
            if platform in ('linux', 'linux64'):
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_E10S[:]
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += CRASHTEST_E10S + \
                    REFTEST_E10S_TWO_CHUNKS
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += CRASHTEST_E10S + \
                    MOCHITEST_DT_2_E10S + REFTEST_E10S
                if name in TWIGS or ('gecko_version' in branch and branch['gecko_version'] != trunk_gecko_version):
                    branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_BC_3_E10S
                else:
                    branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_BC_7_E10S
            if platform == 'linux':
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MARIONETTE_E10S[:]
            # wpt-10s
            if (platform in ('linux64', 'linux') or
                (platform == "macosx64" and slave_platform != "snowleopard")):

                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S[:] + WEB_PLATFORM_REFTESTS_E10S
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_E10S[:] + WEB_PLATFORM_REFTESTS_E10S[:]

# Bug 1200437
# Use 7 chunks for m-bc on branches > trunk, excluding twigs, 3 chunks elsewhere
for branch in BRANCHES.keys():
    for platform in PLATFORMS.keys():
        if platform not in BRANCHES[branch]['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in BRANCHES[branch]['platforms'][platform]:
                continue
            if branch in TWIGS or ('gecko_version' in BRANCHES[branch] and BRANCHES[branch]['gecko_version'] != trunk_gecko_version):
                BRANCHES[branch]['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_BC_3
                BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_BC_3
            else:
                BRANCHES[branch]['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_BC_7
                BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_BC_7

# Remove mochitest-browser-chrome and mochitest-devtools-chrome
# from versioned b2g branches - bug 1045398
for name in [x for x in BRANCHES.keys() if x.startswith('mozilla-b2g')]:
    branch = BRANCHES[name]
    for platform in branch['platforms']:
        for item in branch['platforms'][platform].keys():
            try:
                if 'debug_unittest_suites' in branch['platforms'][platform][item]:
                    unit_tests = branch['platforms'][platform][item]
                    for element in unit_tests:
                        for component in unit_tests[element]:
                            if (component[0] == 'mochitest-browser-chrome' or
                                component[0] == 'mochitest-devtools-chrome'):
                                unit_tests[element].remove(component)
            except TypeError:
                # not an iterable,
                pass

# Enable mediatests on gecko >= 44 (bug 1209258)
for name, branch in items_at_least(BRANCHES, 'gecko_version', 44):
    for platform in PLATFORMS.keys():
        if platform not in branch['platforms']:
            continue
        for slave_platform in ('ubuntu64_vm', 'ubuntu64-asan_vm', 'win7-ix', 'win8_64', 'yosemite'):
            if slave_platform in branch['platforms'][platform]:
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MEDIATESTS[:]
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MEDIATESTS[:]

### Test suites that only run on Cedar ###
# Turn off most suites on cedar (bug 1198400)
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms']:
        continue
    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform in BRANCHES['cedar']['platforms'][platform]:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] = []
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] = []

BRANCHES['cedar']['platforms']['linux64-asan']['ubuntu64-asan_vm']['opt_unittest_suites'] += MARIONETTE[:]

# Enable media-youtube-tests (bug 1209327)
for slave_platform in ('ubuntu64_vm', 'ubuntu64-asan_vm', 'win7-ix', 'win8_64', 'yosemite'):
    for platform in PLATFORMS.keys():
        if platform not in BRANCHES['cedar']['platforms']:
            continue
        if slave_platform in BRANCHES['cedar']['platforms'][platform]:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += MEDIA_YOUTUBE_TESTS[:]
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += MEDIA_YOUTUBE_TESTS[:]

# Enable mozbase unit tests (bug 971687)
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms']:
        continue
    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform in BRANCHES['cedar']['platforms'][platform]:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOZBASE[:]
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOZBASE[:]

# Enable web-platform-tests on cedar
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms']:
        continue

    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform not in BRANCHES['cedar']['platforms'][platform]:
            continue

        if platform in ('linux64-asan',):
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_REFTESTS[:]
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED[:]
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_MORE[:] + WEB_PLATFORM_REFTESTS
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_REFTESTS_E10S[:]
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_E10S[:]
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S[:] + WEB_PLATFORM_REFTESTS_E10S


### Test suites that only run on Try ###

# Enable linux64-cc, linux64-tsan, and win10 on Try only
delete_slave_platform(BRANCHES, PLATFORMS, {'win64': 'win10_64'}, branch_exclusions=["try"])
# Enable Yosemite testing on select branches only
delete_slave_platform(BRANCHES, PLATFORMS, {'macosx64': 'yosemite_r7'}, branch_exclusions=["try"])

# Enable web-platform-tests-e10s on windows 7 try opt
BRANCHES['try']['platforms']['win32']['win7-ix']['opt_unittest_suites'] += WEB_PLATFORM_REFTESTS_E10S[:]
BRANCHES['try']['platforms']['win32']['win7-ix']['opt_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_E10S[:]


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


# Gtests run from the test package
for platform in PLATFORMS.keys():
    if platform not in ['linux', 'linux64', 'linux64-asan', 'linux64-tsan', 'linux64-cc',
                        'macosx64', 'win32', 'win64']:
        continue

    for name, branch in items_at_least(BRANCHES, 'gecko_version', 44):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:

            # Not stable on windows XP
            if slave_platform in ['xp-ix', 'win10_64', 'yosemite_r7']:
                continue
      
            if platform in BRANCHES[name]['platforms']:
                if (platform in ['linux64', 'linux64-tsan', 'linux64-cc'] and slave_platform in ['ubuntu64_vm']) or (platform in ['linux64-asan'] and slave_platform in ['ubuntu64-asan_vm']):                    
                    continue
                elif (platform in ['linux64', 'linux64-tsan', 'linux64-cc'] and slave_platform in ['ubuntu64_vm_lnx_large']) or (platform in ['linux64-asan'] and slave_platform in ['ubuntu64-asan_vm_lnx_large']):
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] = GTEST
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] = GTEST
                else:               
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] += GTEST
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += GTEST

ride_trains_branches = []
for name, branch in items_at_least(BRANCHES, 'gecko_version', 44):
    ride_trains_branches.append(name)

delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-cc': 'ubuntu64_vm'}, branch_exclusions=["try"])
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-cc': 'ubuntu64_vm_lnx_large'}, branch_exclusions=["try"])
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-tsan': 'ubuntu64_vm' }, branch_exclusions=["try"])
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-tsan': 'ubuntu64_vm_lnx_large'}, branch_exclusions=["try"])
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-asan': 'ubuntu64_vm'}, branch_exclusions=ride_trains_branches)
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-asan': 'ubuntu64-asan_vm_lnx_large'}, branch_exclusions=ride_trains_branches)
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64': 'ubuntu64_vm_lnx_large'}, branch_exclusions=ride_trains_branches)


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
