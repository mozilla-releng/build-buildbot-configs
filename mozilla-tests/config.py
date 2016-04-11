from copy import deepcopy

import config_common
reload(config_common)
from config_common import loadDefaultValues, loadCustomTalosSuites, \
    get_talos_slave_platforms, delete_slave_platform, nested_haskey

import master_common
reload(master_common)
from master_common import setMainFirefoxVersions, items_at_least, items_before

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

TALOS_TP_NEW_OPTS = {'plugins': {'32': 'zips/flash32_10_3_183_5.zip', '64':
                                 'zips/flash64_11_0_d1_98.zip'}, 'pagesets':
                     ['zips/tp5n.zip']}

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
    'mozilla-esr45': {
        'gecko_version': 45,
        'platforms': {
            'macosx64': {},
            'win32': {},
            'win64': {},
            'linux': {},
            'linux64': {},
            'linux64-asan': {},
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
PLATFORMS['macosx64']['snowleopard'] = {'name': "Rev4 MacOSX Snow Leopard 10.6",
                                        'try_by_default': False}
PLATFORMS['macosx64']['yosemite'] = {'name': "Rev5 MacOSX Yosemite 10.10",
                                     'try_by_default': False}
PLATFORMS['macosx64']['yosemite_r7'] = {'name': "Rev7 MacOSX Yosemite 10.10.5"}
PLATFORMS['macosx64']['stage_product'] = 'firefox'
PLATFORMS['macosx64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'config_file': 'talos/mac_config.py',
}
PLATFORMS['macosx64']['talos_slave_platforms'] = ['yosemite', 'yosemite_r7']

PLATFORMS['win32']['slave_platforms'] = ['xp-ix', 'win7-ix', 'win7-all']
PLATFORMS['win32']['talos_slave_platforms'] = ['xp-ix', 'win7-ix']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp-ix'] = {'name': "Windows XP 32-bit",
                               'try_by_default': False}
PLATFORMS['win32']['win7-ix'] = {'name': "Windows 7 32-bit"}
PLATFORMS['win32']['win7-all'] = {'name': "Windows 7 32-bit"}
PLATFORMS['win32']['stage_product'] = 'firefox'
PLATFORMS['win32']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
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
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64-cc']['slave_platforms'] = ['ubuntu64_vm', 'ubuntu64_vm_lnx_large']
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
for platform, platform_config in PLATFORMS.iteritems():
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
WIN7_ONLY = ['win7-ix']

SUITES = {
    'xperf': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5n', '--sampleConfig', 'xperf.config', '--mozAfterPaint', '--xperf_path',
                                  '"c:/Program Files/Microsoft Windows Performance Toolkit/xperf.exe"', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, WIN7_ONLY),
    },
    'xperf-e10s': {
        'enable_by_default': True,
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
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o', '--mozAfterPaint', '--responsiveness', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g1': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o_scroll', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g1-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o_scroll', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g2': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'damp', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g2-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'damp', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g3': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_dom'],
        'options': ({}, LINUX_ONLY),
    },
    'g3-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_dom'],
        'options': ({}, LINUX_ONLY),
    },
    'other': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscrollr:a11yr:ts_paint:tpaint', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'other-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscrollr:a11yr:ts_paint:tpaint', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'svgr': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvgr:tsvgr_opacity', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'svgr-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvgr:tsvgr_opacity', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'dromaeojs': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom:kraken:v8_7'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'dromaeojs-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom:kraken:v8_7'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'chromez': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tresize', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'chromez-e10s': {
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

### Mochitests (Browser-Chrome-Screenshots) ###
MOCHITEST_BC_SCREENSHOTS = [
    ('mochitest-browser-screenshots', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'browser-chrome-screenshots'],
        'blob_upload': True,
        'script_maxtime': 1200,
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

MOCHITEST_DT_8_E10S = [
    ('mochitest-e10s-devtools-chrome', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-devtools-chrome', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 4800,
        'totalChunks': 8,
    }),
]

### Mochitests (Plain) ###
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

MOCHITEST_E10S_8 = [
    ('mochitest-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain-chunked', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 8,
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

MOCHITEST_WO_BC_8 = [
    ('mochitest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain-chunked'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 8,
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

MOCHITEST_MEDIA = [
    ('mochitest-media', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-media'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

MOCHITEST_MEDIA_E10S = [
    ('mochitest-media-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-media', '--e10s'],
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

MOCHITEST_WEBGL_E10S = [
    ('mochitest-gl-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-gl', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 1800,
    }),
]

### Mochitest Combinations ###
MOCHITEST = MOCHITEST_WO_BC + MOCHITEST_OTHER

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

JSREFTEST_E10S = [
    ('jsreftest-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'jsreftest', '--e10s'],
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

REFTEST_NOACCEL_E10S = [
    ('reftest-no-accel-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-no-accel', '--e10s'],
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

REFTEST_NOACCEL_E10S_TWO_CHUNKS = [
    ('reftest-no-accel-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-no-accel', '--e10s'],
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

WEB_PLATFORM_TESTS_CHUNKED = [
    ('web-platform-tests', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness"],
        'totalChunks': 5,
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_TESTS_CHUNKED_MORE = [
    ('web-platform-tests', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness"],
        'totalChunks': 10,
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

WEB_PLATFORM_TESTS_CHUNKED_E10S = [
    ('web-platform-tests-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness", "--e10s"],
        'totalChunks': 5,
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S = [
    ('web-platform-tests-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/web_platform_tests.py',
        'extra_args': ["--test-type=testharness", "--e10s"],
        'totalChunks': 10,
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

XPCSHELL_FOUR_CHUNKS = [
    ('xpcshell', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--xpcshell-suite', 'xpcshell'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 4,
    }),
]


### Default Test Suites For All Platforms ###
# The below test suites will run across all platforms and trees. Many platforms
# will additionally require other various suites to be run, which are set in the
# sections below.
UNITTEST_SUITES = {
    'opt_unittest_suites': CPPUNIT + MOCHITEST + OTHER_REFTESTS + MOCHITEST_WEBGL,
    'debug_unittest_suites': CPPUNIT + MARIONETTE + MOCHITEST + MOCHITEST_WEBGL + \
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST_CHUNKED + \
                                   MARIONETTE + REFTEST_NOACCEL_TWO_CHUNKS + REFTEST_TWO_CHUNKS + \
                                   WEB_PLATFORM_REFTESTS + WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST_CHUNKED + \
                                     REFTEST_FOUR_CHUNKS,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
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
        'ubuntu64_hw': {},
        'ubuntu64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST_CHUNKED + \
                                   MARIONETTE + REFTEST_NOACCEL_TWO_CHUNKS + REFTEST_TWO_CHUNKS + \
                                   WEB_PLATFORM_REFTESTS + WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST_CHUNKED + \
                                    REFTEST_FOUR_CHUNKS,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'luciddream': {
                    'config_files': ["luciddream/linux_config.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
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
    'linux64-asan': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'ubuntu64-asan_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST_CHUNKED + \
                                   REFTEST_TWO_CHUNKS,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST_CHUNKED + \
                                     REFTEST_FOUR_CHUNKS,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST_CHUNKED + \
                                   REFTEST_TWO_CHUNKS,
            'debug_unittest_suites': [],
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST_CHUNKED + \
                                   REFTEST_TWO_CHUNKS,
            'debug_unittest_suites': [],
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'xpcshell': {
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + \
                                   MARIONETTE + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     REFTEST_ONE_CHUNK,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        },
        'win7-ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     REFTEST_ONE_CHUNK,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        },
        'win7-all': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     REFTEST_ONE_CHUNK,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     REFTEST_ONE_CHUNK,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        },
        'win10_64': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     REFTEST_ONE_CHUNK,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/windows_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_windows_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-browser-screenshots': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config_windows.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + REFTEST_ONE_CHUNK,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     REFTEST_ONE_CHUNK,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
        'yosemite': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_ONE_CHUNK,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + REFTEST_ONE_CHUNK,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
        'yosemite_r7': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + REFTEST_ONE_CHUNK,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + REFTEST_ONE_CHUNK,
            'suite_config': {
                'cppunit': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'gtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jittest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'marionette': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'marionette-e10s': {
                    'config_files': ["marionette/prod_config.py"],
                },
                'media-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'media-youtube-tests': {
                    'config_files': ["mediatests/buildbot_posix_config.py"],
                },
                'mochitest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-a11y': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-e10s-browser-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-browser-screenshots': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-chrome': {
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
                'mochitest-gl-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-jetpack': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-media': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-media-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-other': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mozbase': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'crashtest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'jsreftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'reftest-no-accel-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'web-platform-tests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'web-platform-tests-reftests-e10s': {
                    'config_files': ["web_platform_tests/prod_config.py"],
                },
                'webapprt-chrome': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'xpcshell': {
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
    if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch]:
        for platform, platform_config in PROJECT_BRANCHES[branch]['platforms'].iteritems():
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

### PROJECTS ###
PROJECTS = {

}
for k, v in localconfig.PROJECTS.iteritems():
    if k not in PROJECTS:
        PROJECTS[k] = {}
    for k1, v1 in v.iteritems():
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

######### b2g-inbound
BRANCHES['b2g-inbound']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['b2g-inbound']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['b2g-inbound']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['b2g-inbound']['platforms']['linux64']['talos_slave_platforms'] = []
BRANCHES['b2g-inbound']['platforms']['win64']['talos_slave_platforms'] = []

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

######### mozilla-esr45
BRANCHES['mozilla-esr45']['repo_path'] = "releases/mozilla-esr45"
BRANCHES['mozilla-esr45']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr45']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr45']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr45']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr45']['platforms']['linux64']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr45']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr45']['platforms']['win64']['talos_slave_platforms'] = []

######## try
BRANCHES['try']['repo_path'] = "try"
BRANCHES['try']['pgo_strategy'] = None
BRANCHES['try']['enable_try'] = True


######### elm
#BRANCHES['elm']['platforms']['win32']['talos_slave_platforms'] = []
#BRANCHES['elm']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['elm']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['elm']['platforms']['linux64']['talos_slave_platforms'] = []
#BRANCHES['elm']['platforms']['win64']['talos_slave_platforms'] = []

######### jamun
BRANCHES['jamun']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['jamun']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['jamun']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['jamun']['platforms']['linux64']['talos_slave_platforms'] = []
BRANCHES['jamun']['platforms']['win64']['talos_slave_platforms'] = []

loadSkipConfig(BRANCHES, "desktop")


### Tests Enabled In Gecko 39+ ###

# Luciddream on Linux64 opt only
for platform in PLATFORMS.keys():
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in ['ubuntu64_vm']:
                continue
            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += LUCIDDREAM

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
            branch['platforms'][pf][slave_pf]['opt_unittest_suites'] += MOCHITEST_JP
            branch['platforms'][pf][slave_pf]['debug_unittest_suites'] += MOCHITEST_JP

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
                        WEB_PLATFORM_TESTS_CHUNKED + WEB_PLATFORM_REFTESTS


### Tests Enabled in Gecko 48+ ###

# Bug 1242682 - Split out mochitest-media in 48+
for platform in PLATFORMS.keys():
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 48):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_MEDIA
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites']+= MOCHITEST_MEDIA
                    if platform not in ('win64') and slave_platform not in ('snowleopard', 'xp-ix'):
                        BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_MEDIA_E10S

            if platform in ('linux', 'linux64') and platform in BRANCHES[name]['platforms']:
                BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_MEDIA_E10S


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
                        WEB_PLATFORM_TESTS_CHUNKED_MORE + WEB_PLATFORM_REFTESTS

### Tests Enabled in Gecko 44+ ###
# mochitest a11y/chrome instead of other
for platform in PLATFORMS.keys():
    if platform not in ['linux']:
        continue

    for name, branch in items_at_least(BRANCHES, 'gecko_version', 44):
        for test_platform in PLATFORMS[platform]['slave_platforms']:

            platforms = BRANCHES[name]['platforms']
            if platform in platforms:
                if test_platform in platforms[platform]:
                    platforms[platform][test_platform]['debug_unittest_suites'] += MOCHITEST_A11Y
                    platforms[platform][test_platform]['debug_unittest_suites'] += MOCHITEST_CHROME
                    for item in platforms[platform][test_platform]['debug_unittest_suites']:
                        if item[0] == 'mochitest-other':
                            platforms[platform][test_platform]['debug_unittest_suites'].remove(item)

### Tests Enabled in Gecko 43+ ###

# Starting in Firefox 46:
#   Enable e10s Linux mochitests
#   Enable e10s browser-chrome mochitests, opt builds only for all platforms (not ready for Xp).
#   Enable e10s devtools tests for Linux opt
#   Enable e10s reftests/crashtests for Linux opt
#   Enable e10s marionette tests for Linux32 opt
#   Enable e10s web-platform-tests
# Bug 1200437 - Use 7 chunks for m-e10-bc on branches > trunk, excluding twigs, 3 chunks elsewhere
trunk_gecko_version = BRANCHES['mozilla-central']['gecko_version']
for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
    for platform in PLATFORMS.keys():
        if platform not in branch['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if platform in branch['platforms'] and slave_platform in branch['platforms'][platform] and \
                    not slave_platform == 'xp-ix':
                if name in TWIGS or ('gecko_version' in branch and branch['gecko_version'] != trunk_gecko_version):
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_BC_3_E10S
                else:
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_BC_7_E10S
            # asan is a special snowflake, so treat it as such
            if platform in ['linux64-asan']:
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += CRASHTEST_E10S + \
                    JSREFTEST_E10S + MOCHITEST_E10S + MOCHITEST_WEBGL_E10S
            if platform in ('linux', 'linux64'):
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += CRASHTEST_E10S + \
                    JSREFTEST_E10S + MARIONETTE_E10S + MOCHITEST_E10S + MOCHITEST_WEBGL_E10S + \
                    REFTEST_E10S
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += CRASHTEST_E10S + \
                    JSREFTEST_E10S + MARIONETTE_E10S + MOCHITEST_E10S_8 + MOCHITEST_WEBGL_E10S + \
                    REFTEST_E10S_TWO_CHUNKS
                # we want mochitests to be 8 chunks for debug on gecko version 46+
                for test, config in branch['platforms'][platform][slave_platform]['debug_unittest_suites']:
                    if test == 'mochitest':
                        branch['platforms'][platform][slave_platform]['debug_unittest_suites'].remove((test,config))
                        branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_WO_BC_8
                if name in TWIGS or ('gecko_version' in branch and branch['gecko_version'] != trunk_gecko_version):
                    branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_BC_3_E10S
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_DT_2_E10S
                else:
                    branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_BC_7_E10S
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_DT_8_E10S
            # wpt-10s
            if (platform in ('linux64', 'linux') or
                (platform == "macosx64" and slave_platform != "snowleopard")):

                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S + WEB_PLATFORM_REFTESTS_E10S
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_E10S + WEB_PLATFORM_REFTESTS_E10S

# Bug 1215233 - Enable more e10s tests on Windows 7 only
#   Turn on mochitest-gl-e10s - bug 1221102
#   Turn on mochitest-e10s-devtools-chrome - bug 1221499
#   Turn on mochitest-e10s - bug 1232780
#   Turn on reftest-e10s - bug 1239025
#   Turn on crashtest-e10s - bug 1240825
#   Turn on jsreftest-e10s - bug 1246627
#   Turn on web platform tests for e10s - bug 1245559
# Bug 1194533 - Enable tests on OSX 10.10
#   Turn on e10s tests for opt builds - bug 1253710
#   Turn on Mn-e10s and mochitest-e10s-browser-chrome - bug 1253714
for name, branch in items_at_least(BRANCHES, 'gecko_version', 47):
    for platform in PLATFORMS.keys():
        if platform not in branch['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform in branch['platforms'][platform] and slave_platform in ('win7-ix', 'win7-all', 'win10_64'):
                if name not in TWIGS:
                    branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += \
                        MOCHITEST_WEBGL_E10S + MOCHITEST_DT_8_E10S + REFTEST_E10S + CRASHTEST_E10S + \
                        JSREFTEST_E10S + WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S + \
                        WEB_PLATFORM_REFTESTS_E10S + MARIONETTE_E10S
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += \
                        MOCHITEST_WEBGL_E10S + MOCHITEST_DT_8_E10S + MOCHITEST_E10S + REFTEST_E10S + \
                        CRASHTEST_E10S + JSREFTEST_E10S + WEB_PLATFORM_TESTS_CHUNKED_E10S + \
                        WEB_PLATFORM_REFTESTS_E10S + MARIONETTE_E10S
            if slave_platform in branch['platforms'][platform] and slave_platform in ('yosemite_r7'):
                if name not in TWIGS:
                    branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += \
                        MARIONETTE_E10S + MOCHITEST_BC_7_E10S
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += \
                        CRASHTEST_E10S + JSREFTEST_E10S + MARIONETTE_E10S + MOCHITEST_DT_8_E10S + \
                        MOCHITEST_E10S + MOCHITEST_WEBGL_E10S + REFTEST_E10S

# Bug 1200437
# Use 7 chunks for m-bc on branches > trunk, excluding twigs, 3 chunks elsewhere
# Bug 1203227
# Use 9 chunks for m-dt on branches > trunk, excluding twigs, 2 or 4 chunks elsewhere
for branch in BRANCHES.keys():
    for platform in PLATFORMS.keys():
        if platform not in BRANCHES[branch]['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in BRANCHES[branch]['platforms'][platform]:
                continue
            if branch.startswith('mozilla-b2g'):
                continue
            bc_suite = MOCHITEST_BC_3[:]
            dt_opt_suite = MOCHITEST_DT_2[:]
            dt_debug_suite = MOCHITEST_DT_4[:]
            gecko_version = BRANCHES[branch].get('gecko_version')
            if branch in TWIGS:
                pass
            elif gecko_version and gecko_version != trunk_gecko_version:
                if gecko_version > 38:
                    # gecko_version <= 38 is a no-op for this entire if statement
                    if slave_platform in ('ubuntu64_vm', 'ubuntu32_vm'):
                        dt_debug_suite = MOCHITEST_DT_8[:]
                    if slave_platform in ('ubuntu64-asan_vm',):
                        dt_opt_suite = MOCHITEST_DT_8[:]
            else:
                dt_opt_suite = MOCHITEST_DT_8[:]
                dt_debug_suite = MOCHITEST_DT_8[:]
                bc_suite = MOCHITEST_BC_7[:]
            BRANCHES[branch]['platforms'][platform][slave_platform]['opt_unittest_suites'] += bc_suite + dt_opt_suite
            BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] += bc_suite + dt_debug_suite

# Use 4 xpcshell chunks on linux debug/asan builds and 1 everywhere else
for branch in BRANCHES.keys():
    for platform in PLATFORMS.keys():
        if platform not in BRANCHES[branch]['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in BRANCHES[branch]['platforms'][platform]:
                continue
            xpc_opt_suite = XPCSHELL[:]
            xpc_debug_suite = XPCSHELL[:]
            if slave_platform in ('ubuntu64_vm', 'ubuntu32_vm', 'ubuntu64-asan_vm'):
                xpc_debug_suite = XPCSHELL_FOUR_CHUNKS[:]
            if slave_platform in ('ubuntu64-asan_vm'):
                xpc_opt_suite = XPCSHELL_FOUR_CHUNKS[:]
            BRANCHES[branch]['platforms'][platform][slave_platform]['opt_unittest_suites'] += xpc_opt_suite
            BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] += xpc_debug_suite

# Enable mediatests on gecko >= 44 (bug 1209258)
for name, branch in items_at_least(BRANCHES, 'gecko_version', 44):
    for platform in PLATFORMS.keys():
        if platform not in branch['platforms']:
            continue
        for slave_platform in ('ubuntu64_vm', 'ubuntu64-asan_vm', 'win7-ix', 'win7-all', 'win8_64', 'yosemite'):
            if slave_platform in branch['platforms'][platform]:
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MEDIATESTS
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MEDIATESTS

# Enable mediatest-youtube-tests on gecko >= 46 (bug 1221963)
for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
    for platform in PLATFORMS.keys():
        if platform not in branch['platforms']:
            continue
        for slave_platform in ('win7-ix', 'win7-all', 'yosemite_r7'):
            if slave_platform in branch['platforms'][platform]:
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MEDIA_YOUTUBE_TESTS
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MEDIA_YOUTUBE_TESTS


# Bug 1223072 - disable media-tests on linux asan, debug (on development and release-stabilization branches)

for slave_platform in ('ubuntu64_vm', 'ubuntu64-asan_vm'):
    for platform in ('linux64', 'linux64-asan'):
        for branch in BRANCHES.keys():
            if platform not in BRANCHES[branch]['platforms']:
                continue
            if slave_platform in BRANCHES[branch]['platforms'][platform]:
                if platform == 'linux64':
                    BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] = [item for item in BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] if item not in MEDIATESTS]
                elif platform == 'linux64-asan':
                    BRANCHES[branch]['platforms'][platform][slave_platform]['opt_unittest_suites'] = [item for item in BRANCHES[branch]['platforms'][platform][slave_platform]['opt_unittest_suites'] if item not in MEDIATESTS]
                    BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] = [item for item in BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] if item not in MEDIATESTS]


# Enable browser chrome screenshots on try and m-c
for branch_name in ('try', 'mozilla-central'):
    branch = BRANCHES[branch_name]
    for platform in PLATFORMS.keys():
        if platform not in branch['platforms']:
            continue
        if platform == 'linux64-asan':
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform in ('ubuntu64_vm', 'ubuntu64-asan_vm'):
                continue
            if slave_platform in branch['platforms'][platform]:
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOCHITEST_BC_SCREENSHOTS


### Test suites that only run on Cedar ###
# Turn off most suites on cedar (bug 1198400)
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms']:
        continue
    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform in BRANCHES['cedar']['platforms'][platform]:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] = []
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] = []

BRANCHES['cedar']['platforms']['linux64-asan']['ubuntu64-asan_vm']['opt_unittest_suites'] += MARIONETTE

# Enable mozbase unit tests (bug 971687)
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms']:
        continue
    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform in BRANCHES['cedar']['platforms'][platform]:
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += MOZBASE
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOZBASE

# Enable web-platform-tests on cedar
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['cedar']['platforms']:
        continue

    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform not in BRANCHES['cedar']['platforms'][platform]:
            continue

        if platform in ('linux64-asan',):
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_REFTESTS
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_MORE + WEB_PLATFORM_REFTESTS
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_REFTESTS_E10S
            BRANCHES['cedar']['platforms'][platform][slave_platform]['opt_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_E10S
            BRANCHES['cedar']['platforms'][platform][slave_platform]['debug_unittest_suites'] += WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S + WEB_PLATFORM_REFTESTS_E10S


### Test suites that only run on Try ###

# Enable linux64-cc, linux64-tsan, and win10 on Try only
delete_slave_platform(BRANCHES, PLATFORMS, {'win64': 'win10_64'}, branch_exclusions=["try"])


ride_trains_branches = []
for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
    ride_trains_branches.append(name)

r7_active_branches = []
for name, branch in items_at_least(BRANCHES, 'gecko_version', 43):
    r7_active_branches.append(name)

r7_inactive_branches = []
for name, branch in items_before(BRANCHES, 'gecko_version', 43):
    r7_inactive_branches.append(name)

# Bug 1203128 - enable r7 on trunk and disable r5 on trunk
delete_slave_platform(BRANCHES, PLATFORMS, {'macosx64': 'yosemite_r7'}, branch_exclusions=r7_active_branches)
delete_slave_platform(BRANCHES, PLATFORMS, {'macosx64': 'yosemite'}, branch_exclusions=r7_inactive_branches)

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

    for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:

            # Not stable on windows XP
            if slave_platform in ['xp-ix', 'win10_64', 'yosemite', 'yosemite_r7']:
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

delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-cc': 'ubuntu64_vm'}, branch_exclusions=["try"])
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-cc': 'ubuntu64_vm_lnx_large'}, branch_exclusions=["try"])
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-tsan': 'ubuntu64_vm' }, branch_exclusions=["try"])
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-tsan': 'ubuntu64_vm_lnx_large'}, branch_exclusions=["try"])
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-asan': 'ubuntu64_vm'}, branch_exclusions=ride_trains_branches)
delete_slave_platform(BRANCHES, PLATFORMS, {'linux64-asan': 'ubuntu64-asan_vm_lnx_large'}, branch_exclusions=ride_trains_branches)

# bug 1217534 delete_slave_platform deletes talos too so we need to delete the ubuntu64_vm_lnx_large
# slave platform a different way otherwise it deletes all talos jobs on linux64 for the non-excluded branches
for name in BRANCHES.keys():
    if name in ride_trains_branches:
        continue
    if 'linux64' not in BRANCHES[name]['platforms']:
        continue
    if 'ubuntu64_vm_lnx_large' not in BRANCHES[name]['platforms']['linux64']:
        continue
    del BRANCHES[name]['platforms']['linux64']['ubuntu64_vm_lnx_large']

# Run only e10s tests on Ash
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['ash']['platforms']:
        continue

    base_tests = CRASHTEST_E10S + JSREFTEST_E10S + MARIONETTE_E10S + MOCHITEST_BC_7_E10S + \
                 MOCHITEST_DT_8_E10S + MOCHITEST_E10S + MOCHITEST_MEDIA_E10S + \
                 MOCHITEST_WEBGL_E10S + WEB_PLATFORM_REFTESTS_E10S

    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform not in BRANCHES['ash']['platforms'][platform]:
            continue

        if slave_platform in BRANCHES['ash']['platforms'][platform] and platform in ['linux64-asan']:
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                base_tests + REFTEST_E10S_TWO_CHUNKS + REFTEST_NOACCEL_E10S_TWO_CHUNKS + \
                WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
        if slave_platform in BRANCHES['ash']['platforms'][platform] and platform in ('linux', 'linux64'):
            BRANCHES['ash']['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                base_tests + REFTEST_E10S_TWO_CHUNKS + REFTEST_NOACCEL_E10S_TWO_CHUNKS + \
                WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                base_tests + REFTEST_E10S_TWO_CHUNKS + REFTEST_NOACCEL_E10S_TWO_CHUNKS + \
                WEB_PLATFORM_TESTS_CHUNKED_E10S
        if slave_platform in BRANCHES['ash']['platforms'][platform] and slave_platform in ('xp-ix', 'yosemite_r7'):
            BRANCHES['ash']['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                base_tests + REFTEST_E10S + WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                base_tests + REFTEST_E10S + WEB_PLATFORM_TESTS_CHUNKED_E10S
        if slave_platform in BRANCHES['ash']['platforms'][platform] and slave_platform in ('win7-ix', 'win7-all', 'win8_64'):
            BRANCHES['ash']['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                base_tests + REFTEST_E10S + REFTEST_NOACCEL_E10S + WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                base_tests + REFTEST_E10S + REFTEST_NOACCEL_E10S + WEB_PLATFORM_TESTS_CHUNKED_E10S


# Bug 1229790 - enable win7 virtual instances (ec2/spot) on try
win7_vm_active_branches = ['try']
win7_vm_inactive_branches = []
for branch in BRANCHES.keys():
    if branch not in win7_vm_active_branches:
        win7_vm_inactive_branches.append(branch)
delete_slave_platform(BRANCHES, PLATFORMS, {'win32': 'win7-all'}, branch_exclusions=win7_vm_active_branches)
# Explicitly don't remove win7-ix from talos
for branch in set(BRANCHES.keys()) - set(win7_vm_inactive_branches):
    for platform in ('win32', 'win64'):
        if platform not in BRANCHES[branch]['platforms']:
            continue
        if nested_haskey(BRANCHES[branch]['platforms'], platform, 'win7-ix'):
            del BRANCHES[branch]['platforms'][platform]['win7-ix']

# Bug 1253341 - run talos jobs on AWS
for branch in ():
    BRANCHES[branch]['platforms']['linux64']['talos_slave_platforms'] = ['ubuntu64_hw', 'ubuntu64_vm']
    # Add ubuntu64_vm to the talos suites
    for test, test_config in BRANCHES[branch].items():
        if not test.endswith('_tests'):
            continue
        tests, merge, extra, platforms = test_config
        if 'ubuntu64_hw' in platforms and 'ubuntu64_vm' not in platforms:
            platforms = platforms + ['ubuntu64_vm']
            BRANCHES[branch][test] = (tests, merge, extra, platforms)

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
