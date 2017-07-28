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

MOZHARNESS_REBOOT_CMD = ['scripts/external_tools/count_and_reboot.py',
                         '-f', '../reboot_count.txt',
                         '-n', '1', '-z']

TALOS_TP_NEW_OPTS = {'plugins': {'32': 'zips/flash32_10_3_183_5.zip', '64':
                                 'zips/flash64_11_0_d1_98.zip'}, 'pagesets':
                     ['zips/tp5n.zip']}

BRANCHES = {
    'mozilla-central':     {},
    'mozilla-release':     {},
    'mozilla-beta':        {},
    'mozilla-esr52': {
        'gecko_version': 52,
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

setMainFirefoxVersions(BRANCHES)

# Talos
PLATFORMS = {
    'linux': {},
    'linux64': {},
    'linux64-asan': {},
    'linux64-stylo': {},
    'linux64-stylosequential': {},
    'linux64-devedition': {},
    'macosx64': {},
    'macosx64-devedition':{},
    'win32': {},
    'win32-devedition': {},
    'win64': {},
    'win64-devedition':{},

}

PLATFORMS['macosx64']['slave_platforms'] = ['yosemite_r7']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['yosemite_r7'] = {'name': "Rev7 MacOSX Yosemite 10.10.5"}
PLATFORMS['macosx64']['stage_product'] = 'firefox'
PLATFORMS['macosx64']['mozharness_config'] = {
    'mozharness_python': ['/tools/buildbot/bin/python', '-u'],
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'config_file': 'talos/mac_config.py',
}
PLATFORMS['macosx64']['talos_slave_platforms'] = ['yosemite_r7']

PLATFORMS['macosx64-devedition']['slave_platforms'] = ['yosemite_r7_devedition']
PLATFORMS['macosx64-devedition']['env_name'] = 'mac-perf'
PLATFORMS['macosx64-devedition']['yosemite_r7_devedition'] = {'name': "Rev7 MacOSX Yosemite 10.10.5 DevEdition",
							      'try_by_default': False}
PLATFORMS['macosx64-devedition']['stage_product'] = 'firefox'
PLATFORMS['macosx64-devedition']['mozharness_config'] = {
    'mozharness_python': ['/tools/buildbot/bin/python', '-u'],
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'config_file': 'talos/mac_config.py',
}

PLATFORMS['win32']['slave_platforms'] = ['xp_ix', 'win7_ix', 'win7_vm', 'win7_vm_gfx']
PLATFORMS['win32']['talos_slave_platforms'] = ['win7_ix']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp_ix'] = {'name': "Windows XP 32-bit",
                               'try_by_default': False}
PLATFORMS['win32']['win7_ix'] = {'name': "Windows 7 32-bit"}
PLATFORMS['win32']['win7_vm'] = {'name': "Windows 7 VM 32-bit"}
PLATFORMS['win32']['win7_vm_gfx'] = {'name': "Windows 7 VM-GFX 32-bit",
                                     'try_by_default': True}
PLATFORMS['win32']['stage_product'] = 'firefox'
PLATFORMS['win32']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'config_file': 'talos/windows_config.py',
}

PLATFORMS['win32-devedition']['slave_platforms'] = ['win7_ix_devedition', 'win7_vm_devedition', 'win7_vm_gfx_devedition']
PLATFORMS['win32-devedition']['env_name'] = 'win32-perf'
PLATFORMS['win32-devedition']['win7_ix_devedition'] = {'name': "Windows 7 32-bit DevEdition",
                                                      'try_by_default': False}
PLATFORMS['win32-devedition']['win7_vm_devedition'] = {'name': "Windows 7 VM 32-bit DevEdition",
                                                       'try_by_default': False}
PLATFORMS['win32-devedition']['win7_vm_gfx_devedition'] = {'name': "Windows 7 VM-GFX 32-bit DevEdition",
                                                           'try_by_default': False}
PLATFORMS['win32-devedition']['stage_product'] = 'firefox'
PLATFORMS['win32-devedition']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'config_file': 'talos/windows_config.py',
}

PLATFORMS['win64']['slave_platforms'] = ['win8_64']
PLATFORMS['win64']['talos_slave_platforms'] = ['win10_64']
PLATFORMS['win64']['env_name'] = 'win64-perf'
PLATFORMS['win64']['stage_product'] = 'firefox'
PLATFORMS['win64']['win8_64'] = {'name': 'Windows 8 64-bit',
                                 'try_by_default': False}
PLATFORMS['win64']['win10_64'] = {'name': 'Windows 10 64-bit',
                                  'try_by_default': True}
PLATFORMS['win64']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'config_file': 'talos/windows_config.py',
}

PLATFORMS['win64-devedition']['slave_platforms'] = ['win8_64_devedition']
PLATFORMS['win64-devedition']['env_name'] = 'win64-perf'
PLATFORMS['win64-devedition']['stage_product'] = 'firefox'
PLATFORMS['win64-devedition']['win8_64_devedition'] = {'name': 'Windows 8 64-bit DevEdition',
                                                       'try_by_default': False}
PLATFORMS['win64-devedition']['win10_64_devedition'] = {'name': 'Windows 10 64-bit DevEdition',
                                                       'try_by_default': False}
PLATFORMS['win64-devedition']['mozharness_config'] = {
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
    'mozharness_python': ['/tools/buildbot/bin/python', '-u'],
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

PLATFORMS['linux64-stylo']['slave_platforms'] = []
PLATFORMS['linux64-stylo']['talos_slave_platforms'] = ['ubuntu64_hw_stylo']
PLATFORMS['linux64-stylo']['env_name'] = 'linux-perf'
PLATFORMS['linux64-stylo']['ubuntu64_hw_stylo'] = {'name': 'Ubuntu HW 12.04 x64 stylo'}
PLATFORMS['linux64-stylo']['stage_product'] = 'firefox'
PLATFORMS['linux64-stylo']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64-stylosequential']['slave_platforms'] = []
PLATFORMS['linux64-stylosequential']['talos_slave_platforms'] = ['ubuntu64_hw_styloseq']
PLATFORMS['linux64-stylosequential']['env_name'] = 'linux-perf'
PLATFORMS['linux64-stylosequential']['ubuntu64_hw_styloseq'] = {'name': 'Ubuntu HW 12.04 x64 stylo-sequential'}
PLATFORMS['linux64-stylosequential']['stage_product'] = 'firefox'
PLATFORMS['linux64-stylosequential']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'config_file': 'talos/linux_config.py',
}

PLATFORMS['linux64-devedition']['slave_platforms'] = []
PLATFORMS['linux64-devedition']['env_name'] = 'linux-perf'
PLATFORMS['linux64-devedition']['ubuntu64_hw_devedition'] = {'name': 'Ubuntu HW 12.04 x64 devedition'}
PLATFORMS['linux64-devedition']['stage_product'] = 'firefox'
PLATFORMS['linux64-devedition']['mozharness_config'] = {
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

ALL_TALOS_PLATFORMS = get_talos_slave_platforms(PLATFORMS, platforms=('linux64', 'win32', 'macosx64', 'win64', 'linux64-stylo', 'linux64-stylosequential'))
LINUX_ONLY = get_talos_slave_platforms(PLATFORMS, platforms=('linux64', 'linux64-stylo', 'linux64-stylosequential'))
WIN_ONLY = get_talos_slave_platforms(PLATFORMS, platforms=('win32', 'win64'))
WIN7_ONLY = ['win7_ix']

SUITES = {
    'xperf-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5n', '--sampleConfig', 'xperf.config', '--mozAfterPaint', '--xperf_path',
                                  '"c:/Program Files/Microsoft Windows Performance Toolkit/xperf.exe"', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, WIN7_ONLY),
    },
    'tp5o-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o', '--mozAfterPaint', '--responsiveness', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g1-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5o_scroll', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g2-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'damp', '--filter', 'ignore_first:1', '--filter', 'median'],
        'options': (TALOS_TP_NEW_OPTS, ALL_TALOS_PLATFORMS),
    },
    'g3-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_dom'],
        'options': ({}, LINUX_ONLY),
    },
    'g4-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'basic_compositor_video'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'g5-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts_paint'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'other-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscrollr:a11yr:ts_paint:tpaint', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'svgr-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvgr:tsvgr_opacity', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'dromaeojs-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_css:dromaeo_dom:kraken:v8_7'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'chromez-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tresize', '--mozAfterPaint', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'perf-reftest-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'bloom_basic:bloom_basic_ref', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
    'quantum-pageload-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'Quantum_1', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, WIN_ONLY),
    },
    'quantum-pageload-stylo-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'Quantum_1', '--filter', 'ignore_first:5', '--filter', 'median', '--stylo'],
        'options': ({}, WIN_ONLY),
    },
    'tp6-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'Quantum_1', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, WIN_ONLY),
    },
    'tp6-stylo-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'Quantum_1', '--filter', 'ignore_first:5', '--filter', 'median', '--stylo'],
        'options': ({}, WIN_ONLY),
    },
    'tp6-stylo-threads-e10s': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'Quantum_1', '--filter', 'ignore_first:5', '--filter', 'median', '--stylo-threads'],
        'options': ({}, WIN_ONLY),
    },
    'perf-reftest-singletons-e10s': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'bloom_basic_singleton', '--filter', 'ignore_first:5', '--filter', 'median'],
        'options': ({}, ALL_TALOS_PLATFORMS),
    },
}

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'linux': {},
        'linux64': {},
        'linux64-stylo': {},
        'linux64-stylosequential': {},
        'linux64-devedition': {},
        'linux64-asan': {},
        'macosx64': {},
        'macosx64-devedition':{},
        'win32': {},
        'win32-devedition':{},
        'win64':{},
        'win64-devedition': {},
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


### Mochitests (Browser-Chrome) ###
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
        'script_maxtime': 1800,
    }),
]

### Mochitests (Devtools) ###
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

MOCHITEST_E10S_10 = [
    ('mochitest-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain-chunked', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 10,
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

MOCHITEST_WO_BC_10 = [
    ('mochitest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'plain-chunked'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 10,
    }),
]

### Mochitest (Other Miscellaneous Suites) ###
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

MOCHITEST_JP = [
    ('mochitest-jetpack', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'jetpack-package', '--mochitest-suite', 'jetpack-addon'],
        'blob_upload': True,
        'script_maxtime': 12000,
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

MOCHITEST_WEBGL_CHUNKED = [
    ('mochitest-gl', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-gl'],
        'blob_upload': True,
        'script_maxtime': 5400,
        'totalChunks': 3,
    }),
]

MOCHITEST_WEBGL_CHUNKED_E10S = [
    ('mochitest-gl-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite', 'mochitest-gl', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 5400,
        'totalChunks': 3,
    }),
]

MOCHITEST_GPU = [
    ('mochitest-gpu', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite',
                       'plain-gpu,chrome-gpu,browser-chrome-gpu'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

MOCHITEST_GPU_E10S = [
    ('mochitest-gpu-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite',
                       'plain-gpu,chrome-gpu,browser-chrome-gpu',
                       '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

MOCHITEST_CLIPBOARD = [
    ('mochitest-clipboard', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite',
                       'plain-clipboard,chrome-clipboard,browser-chrome-clipboard,jetpack-package-clipboard'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

MOCHITEST_CLIPBOARD_E10S = [
    ('mochitest-clipboard-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mochitest-suite',
                       'plain-clipboard,chrome-clipboard,browser-chrome-clipboard,jetpack-package-clipboard',
                       '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

### Mochitest Combinations ###
MOCHITEST_5 = MOCHITEST_WO_BC + MOCHITEST_A11Y + MOCHITEST_CHROME
MOCHITEST_10 = MOCHITEST_WO_BC_10 + MOCHITEST_A11Y + MOCHITEST_CHROME

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

JSREFTEST = [
    ('jsreftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'jsreftest'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

JSREFTEST_TWO_CHUNKS = [
    ('jsreftest', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'jsreftest'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 2,
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

JSREFTEST_E10S_TWO_CHUNKS = [
    ('jsreftest-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'jsreftest', '--e10s'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 2,
    }),
]

OTHER_REFTESTS = [
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

REFTEST_QR_E10S = [
    ('reftest-qr-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-qr', '--e10s'],
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

REFTEST_QR_E10S_TWO_CHUNKS = [
    ('reftest-qr-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-qr', '--e10s'],
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

REFTEST_GPU_E10S = [
    ('reftest-gpu-e10s', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-gpu', '--e10s'],
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

REFTEST_NOACCEL_FOUR_CHUNKS = [
    ('reftest-no-accel', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--reftest-suite', 'reftest-no-accel'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 4,
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
    'opt_unittest_suites': CPPUNIT + MOCHITEST_5 + MOCHITEST_BC_7 + MOCHITEST_DT_8 + \
                           MOCHITEST_WEBGL_CHUNKED + OTHER_REFTESTS + JSREFTEST,
    'debug_unittest_suites': CPPUNIT + MARIONETTE + MOCHITEST_BC_7 + \
                             MOCHITEST_WEBGL_CHUNKED + OTHER_REFTESTS + JSREFTEST,
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
                                   MARIONETTE + WEB_PLATFORM_REFTESTS + WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST_CHUNKED + \
                                     MOCHITEST_10,
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
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
                                   MARIONETTE + WEB_PLATFORM_REFTESTS + WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST_CHUNKED + \
                                     MOCHITEST_10 + MOCHITEST_DT_8,
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
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
    'linux64-stylo': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'ubuntu64_hw_stylo': {},
    },
     'linux64-stylosequential': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'ubuntu64_hw_styloseq': {},
    },
    'linux64-devedition': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'ubuntu64_hw_devedition': {},
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
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST_CHUNKED,
            'debug_unittest_suites': [],
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
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
        'xp_ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + \
                                   MARIONETTE + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     MOCHITEST_5 + MOCHITEST_DT_8 + REFTEST_ONE_CHUNK,
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
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
        'win7_ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     MOCHITEST_5 + MOCHITEST_DT_8 + REFTEST_NOACCEL_TWO_CHUNKS + \
                                     REFTEST_TWO_CHUNKS,
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
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
        'win7_vm': {
            'opt_unittest_suites': CPPUNIT + JITTEST + MARIONETTE + MOCHITEST_5 + MOCHITEST_BC_7 + \
                                   MOCHITEST_DT_8 + OTHER_REFTESTS + JSREFTEST + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': CPPUNIT + JITTEST + MARIONETTE + MOCHITEST_5 + MOCHITEST_BC_7 + \
                                     MOCHITEST_DT_8 + OTHER_REFTESTS + JSREFTEST,
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
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
        'win7_vm_gfx': {
            'opt_unittest_suites': MOCHITEST_5 + MOCHITEST_BC_7 + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK,
            'debug_unittest_suites': MOCHITEST_5 + MOCHITEST_BC_7 + \
                                     REFTEST_NOACCEL_TWO_CHUNKS + REFTEST_TWO_CHUNKS,
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
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
                'reftest-gpu-e10s': {
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
    'win32-devedition': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'mochitest_leak_threshold': 484,
        'crashtest_leak_threshold': 484,
        'env_name': 'win32-perf-unittest',
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'win7_ix_devedition': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
        },
        'win7_vm_devedition': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
        },
        'win7_vm_gfx_devedition': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
        },
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
        'win10_64': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': []
        },
        'win8_64': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + MARIONETTE + \
                                   REFTEST_NOACCEL + REFTEST_ONE_CHUNK + WEB_PLATFORM_REFTESTS + \
                                   WEB_PLATFORM_TESTS_CHUNKED,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     MOCHITEST_5 + MOCHITEST_DT_8 + REFTEST_NOACCEL_TWO_CHUNKS + \
                                     REFTEST_TWO_CHUNKS,
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/win_unittest.py"],
                },
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
                'reftest-qr-e10s': {
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
    'win64-devedition': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'mochitest_leak_threshold': 484,
        'crashtest_leak_threshold': 484,
        'env_name': 'win64-perf-unittest',
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'win8_64_devedition': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
        },
        'win10_64_devedition': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
        },
    },
    'macosx64': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'yosemite_r7': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'] + JITTEST + REFTEST_ONE_CHUNK,
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'] + JITTEST + \
                                     MOCHITEST_5 + MOCHITEST_DT_8 + REFTEST_TWO_CHUNKS,
            'suite_config': {
                'mochitest-gpu': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-gpu-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-clipboard': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mochitest-clipboard-e10s': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
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
    'macosx64-devedition': {
        'product_name': 'firefox',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'builds_before_reboot': 1,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'yosemite_r7_devedition': {
            'opt_unittest_suites': [],
            'debug_unittest_suites': [],
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

######### mozilla-esr52
BRANCHES['mozilla-esr52']['repo_path'] = "releases/mozilla-esr52"
BRANCHES['mozilla-esr52']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr52']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr52']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr52']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr52']['platforms']['linux64']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr52']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['mozilla-esr52']['platforms']['win64']['talos_slave_platforms'] = []


######## try
BRANCHES['try']['repo_path'] = "try"
BRANCHES['try']['pgo_strategy'] = 'try'
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['watch_all_branches'] = True

######### jamun
BRANCHES['jamun']['platforms']['win32']['talos_slave_platforms'] = []
BRANCHES['jamun']['platforms']['macosx64']['talos_slave_platforms'] = []
BRANCHES['jamun']['platforms']['linux']['talos_slave_platforms'] = []
BRANCHES['jamun']['platforms']['linux64']['talos_slave_platforms'] = []
BRANCHES['jamun']['platforms']['win64']['talos_slave_platforms'] = []

### Tests Enabled In Gecko 39+ ###

# mochitest-jetpack everywhere
for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
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

### Tests Enabled in Gecko 42+ ###

# Debug web-platform-tests
for platform in PLATFORMS.keys():
    if platform not in ['linux', 'linux64', 'macosx64', 'win32', 'win64']:
        continue
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 42):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:

            if platform in BRANCHES[name]['platforms']:
                if slave_platform in BRANCHES[name]['platforms'][platform]:
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] += \
                        WEB_PLATFORM_TESTS_CHUNKED_MORE + WEB_PLATFORM_REFTESTS

### Tests Enabled in Gecko 43+ ###

# Enable e10s tests for Gecko 46+ on all eligible platforms
for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
    for platform in PLATFORMS.keys():
        if platform not in branch['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            # e10s tests not supported on WinXP
            if slave_platform == 'xp_ix':
                continue

            # Base set of test suites that are run across all platforms and flavors.
            base_tests = CRASHTEST_E10S + JSREFTEST_E10S + MARIONETTE_E10S + MOCHITEST_BC_7_E10S + \
                         MOCHITEST_CLIPBOARD_E10S + MOCHITEST_GPU_E10S + MOCHITEST_MEDIA_E10S + \
                         MOCHITEST_WEBGL_CHUNKED_E10S + WEB_PLATFORM_REFTESTS_E10S

            if platform in branch['platforms'] and slave_platform in branch['platforms'][platform]:
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += base_tests + \
                    WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += base_tests + \
                    MOCHITEST_DT_8_E10S + MOCHITEST_E10S + WEB_PLATFORM_TESTS_CHUNKED_E10S

            # On Linux debug, split mochitest-plain into 10 chunks.
            # Otherwise, use 5 (as set in the block below this one).
            if platform in ('linux', 'linux64'):
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += MOCHITEST_E10S_10

            # Bug 1223198 - Linux buildbot reftests are broken and not being fixed due to
            # being migrated to Taskcluster. Therefore, only schedule e10s reftests on OSX & Windows.
            # Also, don't schedule reftest-no-accel on OSX since it's not supported on there.
            # Debug devtools tests are also only scheduled on OSX & Windows since they're timeout-
            # prone on the AWS VMs.
            if platform not in ('linux', 'linux64'):
                branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += \
                    MOCHITEST_DT_8_E10S + MOCHITEST_E10S + REFTEST_E10S_TWO_CHUNKS
                branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += REFTEST_E10S
                if slave_platform != 'yosemite_r7':
                    branch['platforms'][platform][slave_platform]['debug_unittest_suites'] += \
                        REFTEST_NOACCEL_E10S_TWO_CHUNKS
                    branch['platforms'][platform][slave_platform]['opt_unittest_suites'] += \
                        REFTEST_NOACCEL_E10S

# Bug 1277885 - Enable e10s tests for all Windows platforms on Try
# Win7/Win8 already run by default on production. WinXP is opt-in platforms.
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['try']['platforms']:
        continue

    base_tests = CRASHTEST_E10S + JSREFTEST_E10S + MARIONETTE_E10S + MOCHITEST_CLIPBOARD_E10S + \
                 MOCHITEST_DT_8_E10S + MOCHITEST_E10S + MOCHITEST_GPU_E10S + MOCHITEST_MEDIA_E10S + \
                 MOCHITEST_WEBGL_CHUNKED_E10S + WEB_PLATFORM_REFTESTS_E10S

    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform not in BRANCHES['try']['platforms'][platform]:
            continue

        if slave_platform in BRANCHES['try']['platforms'][platform] and slave_platform in ('xp_ix'):
            BRANCHES['try']['platforms'][platform][slave_platform]['debug_unittest_suites'] += \
                base_tests + MOCHITEST_BC_7_E10S + REFTEST_E10S_TWO_CHUNKS + WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
            BRANCHES['try']['platforms'][platform][slave_platform]['opt_unittest_suites'] += \
                base_tests + MOCHITEST_BC_7_E10S + REFTEST_E10S + WEB_PLATFORM_TESTS_CHUNKED_E10S

# Use 4 xpcshell chunks on linux debug/asan builds and 1 everywhere else
for branch in BRANCHES.keys():
    for platform in PLATFORMS.keys():
        if platform not in BRANCHES[branch]['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in BRANCHES[branch]['platforms'][platform]:
                continue
            # Don't run xpcshell on win7_vm_gfx
            if slave_platform == 'win7_vm_gfx':
                continue
            xpc_opt_suite = XPCSHELL[:]
            xpc_debug_suite = XPCSHELL[:]
            if slave_platform in ('ubuntu64_vm', 'ubuntu32_vm', 'ubuntu64-asan_vm'):
                xpc_debug_suite = XPCSHELL_FOUR_CHUNKS[:]
            if slave_platform in ('ubuntu64-asan_vm'):
                xpc_opt_suite = XPCSHELL_FOUR_CHUNKS[:]
            BRANCHES[branch]['platforms'][platform][slave_platform]['opt_unittest_suites'] += xpc_opt_suite
            BRANCHES[branch]['platforms'][platform][slave_platform]['debug_unittest_suites'] += xpc_debug_suite


# Enable browser chrome screenshots on try, m-c and date
for branch_name in ('try', 'mozilla-central', 'date'):
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

# Enable gpu/clipboard jobs on all branches v.49+
for platform in PLATFORMS.keys():
    for name, branch in items_at_least(BRANCHES, 'gecko_version', 49):
        if platform in BRANCHES[name]['platforms']:
            for slave_platform in PLATFORMS[platform]['slave_platforms']:
                if platform in BRANCHES[name]['platforms'] and slave_platform in BRANCHES[name]['platforms'][platform]:
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += \
                        MOCHITEST_GPU + MOCHITEST_CLIPBOARD

                    # Do not add Linux x64 debug since it is running on TaskCluster
                    if slave_platform != 'ubuntu64_vm':
                        BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] += \
                            MOCHITEST_GPU + MOCHITEST_CLIPBOARD

# Enable talos perf-reftest-singeltons on 56+
for name, branch in items_at_least(BRANCHES, 'gecko_version', 56):
    if branch.get('enable_talos') is False:
        continue
    branch['perf-reftest-singletons-e10s_tests'] = (1, False, {}, ALL_TALOS_PLATFORMS)
    branch['quantum-pageload-stylo-e10s_tests'] = (1, False, {}, WIN_ONLY)
    branch['tp6-stylo-threads-e10s_tests'] = (1, False, {}, WIN_ONLY)

    if name in ['try']:
        branch['tp6-stylo-e10s_tests'] = (1, False, {}, WIN_ONLY)
        branch['tp6-e10s_tests'] = (1, False, {}, WIN_ONLY)

### Test suites that only run on Try ###

ride_trains_branches = []
for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
    ride_trains_branches.append(name)

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
    if platform not in ['linux', 'linux64', 'linux64-asan', 'macosx64', 'win32', 'win64']:
        continue

    for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
        for slave_platform in PLATFORMS[platform]['slave_platforms']:

            # Not stable on windows XP
            if slave_platform in ['xp_ix']:
                continue
            # Don't run on win7_vm_gfx
            if slave_platform == 'win7_vm_gfx':
                continue

            if platform in BRANCHES[name]['platforms']:
                if (platform in ['linux64'] and slave_platform in ['ubuntu64_vm']) or (platform in ['linux64-asan'] and slave_platform in ['ubuntu64-asan_vm']):
                    continue
                elif (platform in ['linux64'] and slave_platform in ['ubuntu64_vm_lnx_large']) or (platform in ['linux64-asan'] and slave_platform in ['ubuntu64-asan_vm_lnx_large']):
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] = GTEST
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] = GTEST
                else:
                    BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] += GTEST
                    BRANCHES[name]['platforms'][platform][slave_platform]['opt_unittest_suites'] += GTEST

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

###
# Bug 1271355 - Run Windows tests in AWS
# Remove the new AWS platforms from older branches where they won't be running
for name, branch in items_before(BRANCHES, 'gecko_version', 49):
    if nested_haskey(BRANCHES[name]['platforms'], 'win32', 'win7_vm'):
        del BRANCHES[name]['platforms']['win32']['win7_vm']
    if nested_haskey(BRANCHES[name]['platforms'], 'win32', 'win7_vm_gfx'):
        del BRANCHES[name]['platforms']['win32']['win7_vm_gfx']

# Only enable suites in AWS that are working
WORKING_WIN7_AWS_OPT_SUITES = WEB_PLATFORM_TESTS_CHUNKED + WEB_PLATFORM_REFTESTS + GTEST + CPPUNIT + JITTEST + OTHER_REFTESTS + JSREFTEST + MARIONETTE + XPCSHELL + MOCHITEST_DT_8 + MOCHITEST_DT_8_E10S + MOCHITEST_JP + MARIONETTE_E10S + MOCHITEST_MEDIA + WEB_PLATFORM_TESTS_CHUNKED_E10S + WEB_PLATFORM_REFTESTS_E10S
WORKING_WIN7_AWS_DEBUG_SUITES = GTEST + CPPUNIT + JITTEST + WEB_PLATFORM_TESTS_CHUNKED_MORE + WEB_PLATFORM_REFTESTS + OTHER_REFTESTS + JSREFTEST + MARIONETTE + XPCSHELL + MOCHITEST_DT_8 + MOCHITEST_DT_8_E10S + MOCHITEST_JP + MARIONETTE_E10S + MOCHITEST_MEDIA + WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S + WEB_PLATFORM_REFTESTS_E10S + CRASHTEST_E10S + JSREFTEST_E10S
for name, branch in items_at_least(BRANCHES, 'gecko_version', 49):
    # Skip branches where win32 isn't running
    if not nested_haskey(branch, 'platforms', 'win32'):
        continue
    win32 = branch['platforms']['win32']

    # Strip out suites that we don't want on the VM/GFX instances
    if 'win7_vm' in win32:
        for test_type in ('opt_unittest_suites', 'debug_unittest_suites'):
            for t in win32['win7_vm'][test_type][:]:
                suite_name, suite_config = t
                if suite_name.startswith('reftest'):
                    win32['win7_vm'][test_type].remove(t)
                if suite_name.startswith('mochitest-gl'):
                    win32['win7_vm'][test_type].remove(t)
                if suite_name.startswith('mochitest-gpu'):
                    win32['win7_vm'][test_type].remove(t)
    if 'win7_vm_gfx' in win32:
        for test_type in ('opt_unittest_suites', 'debug_unittest_suites'):
            for t in win32['win7_vm_gfx'][test_type][:]:
                suite_name, suite_config = t
                if suite_name.startswith('crashtest'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('jsreftest'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('marionette'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('web-platform-tests'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('mochitest-devtools'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('mochitest-e10s-devtools'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('mochitest-jetpack'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('cppunit'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('gtest'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name.startswith('xpcshell'):
                    win32['win7_vm_gfx'][test_type].remove(t)
                if suite_name == 'mochitest-media':
                    win32['win7_vm_gfx'][test_type].remove(t)
    # Strip out suites that we don't want on the IX instances
    if 'win7_ix' in win32:
        for test_type in ('opt_unittest_suites', 'debug_unittest_suites'):
            for t in win32['win7_ix'][test_type][:]:
                suite_name, suite_config = t
                if suite_name.startswith('mochitest-devtools'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('mochitest-e10s-devtools'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('mochitest-jetpack'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('marionette'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name == 'mochitest-media':
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('cppunit'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('gtest'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('xpcshell'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('web-platform-tests'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('mochitest-gpu'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('crashtest-e10s'):
                    win32['win7_ix'][test_type].remove(t)
                if suite_name.startswith('jsreftest-e10s'):
                    win32['win7_ix'][test_type].remove(t)

    # Leave all the other suites running on try
    if name == 'try':
        continue

    if 'win7_vm' in win32:
        win32['win7_vm']['opt_unittest_suites'] = WORKING_WIN7_AWS_OPT_SUITES
        win32['win7_vm']['debug_unittest_suites'] = WORKING_WIN7_AWS_DEBUG_SUITES
    if 'win7_vm_gfx' in win32:
        win32['win7_vm_gfx']['opt_unittest_suites'] = REFTEST_ONE_CHUNK + REFTEST_NOACCEL + MOCHITEST_GPU + \
                                                      MOCHITEST_GPU_E10S + REFTEST_E10S
        win32['win7_vm_gfx']['debug_unittest_suites'] = REFTEST_TWO_CHUNKS + MOCHITEST_GPU + MOCHITEST_GPU_E10S + \
                                                        REFTEST_NOACCEL_TWO_CHUNKS + REFTEST_E10S_TWO_CHUNKS

    # Disable these suites from the IX machines
    if 'win7_ix' in win32:
        for test_type in ('opt_unittest_suites', 'debug_unittest_suites'):
            for t in win32['win7_vm'][test_type]:
                if t in win32['win7_ix'][test_type]:
                    win32['win7_ix'][test_type].remove(t)
            for t in win32['win7_vm_gfx'][test_type]:
                if t in win32['win7_ix'][test_type]:
                    win32['win7_ix'][test_type].remove(t)

# Bug 1291015 - Migrate mochitest (plain, bc, gl) to AWS
for name, branch in items_at_least(BRANCHES, 'gecko_version', 51):
    # Skip branches where win32 isn't running
    if not nested_haskey(branch, 'platforms', 'win32'):
        continue
    win32 = branch['platforms']['win32']

    if 'win7_vm_gfx' in win32:
        for test_type in ('opt_unittest_suites', 'debug_unittest_suites'):
            for t in win32['win7_vm_gfx'][test_type][:]:
                suite_name, suite_config = t
                if suite_name in ('mochitest', 'mochitest-e10s', 'mochitest-browser-chrome', 'mochitest-e10s-browser-chrome'):
                    win32['win7_vm_gfx'][test_type].remove(t)

    if 'win7_ix' in win32:
        for test_type in ('opt_unittest_suites', 'debug_unittest_suites'):
            for t in win32['win7_ix'][test_type][:]:
                suite_name, suite_config = t
                if suite_name in ('mochitest', 'mochitest-e10s', 'mochitest-browser-chrome', 'mochitest-e10s-browser-chrome', 'mochitest-gl', 'mochitest-gl-e10s', 'reftest-no-accel-e10s'):
                    win32['win7_ix'][test_type].remove(t)

    if name == 'try':
        continue

    if 'win7_vm' in win32:
        win32['win7_vm']['opt_unittest_suites'] = WORKING_WIN7_AWS_OPT_SUITES + MOCHITEST_WO_BC + \
                                                  MOCHITEST_E10S + MOCHITEST_BC_7_E10S + MOCHITEST_BC_7
        win32['win7_vm']['debug_unittest_suites'] = WORKING_WIN7_AWS_DEBUG_SUITES + MOCHITEST_WO_BC + \
                                                    MOCHITEST_E10S + MOCHITEST_BC_7_E10S + MOCHITEST_BC_7

    if 'win7_vm_gfx' in win32:
        win32['win7_vm_gfx']['opt_unittest_suites'] += MOCHITEST_WEBGL_CHUNKED_E10S + \
                                                       REFTEST_NOACCEL_E10S
        win32['win7_vm_gfx']['debug_unittest_suites'] += MOCHITEST_WEBGL_CHUNKED_E10S + \
                                                         REFTEST_NOACCEL_E10S_TWO_CHUNKS

# Bug 1313499 - Run reftest-gpu-e10s on AWS on Gecko 53+
for name, branch in items_at_least(BRANCHES, 'gecko_version', 53):
    # Skip branches where win32 isn't running
    if not nested_haskey(branch, 'platforms', 'win32'):
        continue
    win32 = branch['platforms']['win32']

    if 'win7_vm_gfx' in win32:
        win32['win7_vm_gfx']['opt_unittest_suites'] += REFTEST_GPU_E10S
        win32['win7_vm_gfx']['debug_unittest_suites'] += REFTEST_GPU_E10S

#Bug 1268542 - Disable Linux64 Debug builds and tests in buildbot
for name, branch in items_at_least(BRANCHES, 'gecko_version', 48):
    for platform in branch['platforms'].keys():
        if platform not in ['linux64']:
            continue
        for slave_platform in ['ubuntu64_vm', 'ubuntu64_vm_lnx_large']:
            BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] = []

#Bug 1282468 - disable buildbot asan builds on trunk
for name, branch in items_at_least(BRANCHES, 'gecko_version', 50):
    for platform in branch['platforms'].keys():
        if platform not in ['linux64-asan']:
            continue
        if 'linux64-asan' in platform:
            del branch['platforms'][platform]

# Bug 1308544 - Enable automation jobs on Cedar twig
for branch in BRANCHES.keys():
    if branch not in ['cedar']:
        continue
    for test in ['opt_unittest_suites', 'debug_unittest_suites']:
        for platform in BRANCHES[branch]['platforms'].keys():
                BRANCHES[branch]['platforms']['win64']['win8_64'][test] = [item for item in BRANCHES[branch]['platforms']['win64']['win8_64'][test] if (item[0].startswith('mochitest') or item in XPCSHELL)]
                BRANCHES[branch]['platforms']['macosx64']['yosemite_r7'][test] = [item for item in BRANCHES[branch]['platforms']['macosx64']['yosemite_r7'][test] if (item[0].startswith('mochitest') or item in XPCSHELL)]
                if test in ['opt_unittest_suites']:
                    BRANCHES[branch]['platforms']['linux64']['ubuntu64_vm'][test] = [item for item in BRANCHES[branch]['platforms']['linux64']['ubuntu64_vm'][test] if (item[0].startswith('mochitest') or item in XPCSHELL)]

# Bug 1308097 - Enable Windows 7 VM opt e10s crashtests and jsreftests on Firefox 52+
for name, branch in items_at_least(BRANCHES, 'gecko_version', 52):
    # they are already enabled on try
    if name in ['try']:
        continue
    if 'win32' not in branch['platforms']:
        continue
    if 'win7_vm' in branch['platforms']['win32']:
        branch['platforms']['win32']['win7_vm']['opt_unittest_suites'] += CRASHTEST_E10S + JSREFTEST_E10S

# Bug 1310836 - Disable XP testing in Firefox 53
for name, branch in items_at_least(BRANCHES, 'gecko_version', 53):
    for platform in branch['platforms'].keys():
        if platform not in ['win32']:
            continue
        if name in ['try']:
            continue
        if 'win32' in platform:
            if 'xp_ix' in branch['platforms'][platform]:
                del branch['platforms'][platform]['xp_ix']

# Bug 1253312 - Disable Linux32 debug builds and tests on trunk
for name, branch in items_at_least(BRANCHES, 'gecko_version', 53):
    for platform in branch['platforms'].keys():
        if platform not in ['linux']:
            continue
        if 'ubuntu32_vm' not in branch['platforms'][platform]:
            continue
        branch['platforms'][platform]['ubuntu32_vm']['debug_unittest_suites'] = []

# Bug 1330680 - patches to disable bb nightlies on linux32/linux64/android on m-c + trunk
for name, branch in items_at_least(BRANCHES, 'gecko_version', 53):
    for platform in branch['platforms'].keys():
        if platform not in ['linux', 'linux64']:
            continue
        if 'ubuntu32_vm' in branch['platforms'][platform]:
            branch['platforms'][platform]['ubuntu32_vm']['opt_unittest_suites'] = []
        if 'ubuntu64_vm' in branch['platforms'][platform]:
            branch['platforms'][platform]['ubuntu64_vm']['opt_unittest_suites'] = []

# Bug 1336553 - Bump OS X and Windows J chunks from 1 to 2
for name, branch in items_at_least(BRANCHES, 'gecko_version', 54):
    for platform in BRANCHES[name]['platforms'].keys():
        if platform not in ['macosx64', 'win64', 'win32']:
            continue
        for slave_platform in BRANCHES[name]['platforms'][platform].keys():
            if slave_platform  not in ['yosemite_r7', 'win8_64', 'win10_64'] and slave_platform.startswith('win7_') is False:
                continue
            for test in ['opt_unittest_suites', 'debug_unittest_suites']:
                for item in range(0, len(BRANCHES[name]['platforms'][platform][slave_platform][test])):
                    if BRANCHES[name]['platforms'][platform][slave_platform][test][item] == JSREFTEST[0]:
                        BRANCHES[name]['platforms'][platform][slave_platform][test][item] = JSREFTEST_TWO_CHUNKS[0]
                    if BRANCHES[name]['platforms'][platform][slave_platform][test][item] == JSREFTEST_E10S[0]:
                        BRANCHES[name]['platforms'][platform][slave_platform][test][item] = JSREFTEST_E10S_TWO_CHUNKS[0]

# Bug 1339185 - Disable non-e10s tests for OSX debug only
# non_e10s will store the tests that don't have an e-10s version
for name, branch in items_at_least(BRANCHES, 'gecko_version', 54):
    non_e10s = []
    for platform in BRANCHES[name]['platforms'].keys():
        if platform not in ['macosx64']:
            continue
        for slave_platform in BRANCHES[name]['platforms'][platform].keys():
            if slave_platform not in ['yosemite_r7']:
                continue
            for test in BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites']:
                if '-e10s' not in test[0] and test[0] not in non_e10s:
                    non_e10s.append(test[0])
                else:
                    s = test[0].replace('-e10s', '')
                    if s in non_e10s:
                        non_e10s.remove(s)
                    else:
                        non_e10s.append(s)
            BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                [item for item in BRANCHES[name]['platforms'][platform][slave_platform]['debug_unittest_suites']
                  if ('e10s' in item[0] or item[0] in non_e10s)]

# Bug 1342202 - Move Win7 mochitest-a11y to AWS
for name, branch in items_at_least(BRANCHES, 'gecko_version', 54):
    for platform in branch['platforms'].keys():
	# mochitest-a11y is already enabled on try
        if platform not in ['win32']:
            continue

        win32 = branch['platforms'][platform]

        if 'win7_vm' in win32 and 'try' not in name:
            win32['win7_vm']['opt_unittest_suites'] += MOCHITEST_A11Y
            win32['win7_vm']['debug_unittest_suites'] += MOCHITEST_A11Y
        if 'win7_ix' in win32:
            for test_type in ('opt_unittest_suites', 'debug_unittest_suites'):
                for t in win32['win7_ix'][test_type][:]:
                    suite_name, suite_config = t
                    if suite_name.startswith('mochitest-a11y'):
                        win32['win7_ix'][test_type].remove(t)


# bug 1343316 - add buildernames for linux64-stylo talos tests for mozilla-central and try branches
for branch in BRANCHES.keys():
    if branch in ['mozilla-central', 'try']:
        continue
    if 'linux64-stylo' not in BRANCHES[branch]['platforms'] and 'linux64-stylosequential' not in BRANCHES[branch]['platforms']  :
        continue
    BRANCHES[branch]['platforms']['linux64-stylo']['talos_slave_platforms'] = []
    BRANCHES[branch]['platforms']['linux64-stylosequential']['talos_slave_platforms'] = []

#Bug 1362397 - Add a new win8 R-e10s-qr job on the graphics tree
for branch in BRANCHES.keys():
    if branch not in ['graphics']:
        continue
    if 'win64' not in BRANCHES[branch]['platforms'].keys():
        continue
    BRANCHES[branch]['platforms']['win64']['win8_64']['opt_unittest_suites'] += REFTEST_QR_E10S
    BRANCHES[branch]['platforms']['win64']['win8_64']['debug_unittest_suites'] += REFTEST_QR_E10S_TWO_CHUNKS


# Bug 1359595 - enable CI tests for DevEdition on mozilla-beta and jamun
devedition_branches = ['jamun', 'mozilla-beta']
for branch in BRANCHES.keys():
    if branch in devedition_branches:
        for platform in BRANCHES['mozilla-beta']['platforms'].keys():
            if platform not in ['macosx64', 'win32', 'win64']:
                continue
            for slave_platform in PLATFORMS[platform]['slave_platforms']:
                if slave_platform not in BRANCHES['mozilla-beta']['platforms'][platform].keys():
                    continue
                # copy from beta
                BRANCHES[branch]['platforms'][str(platform + '-devedition')][str(slave_platform + '_devedition')] = deepcopy(BRANCHES['mozilla-beta']['platforms'][platform][slave_platform])
                #  we don't need debug tests for devedition
                BRANCHES[branch]['platforms'][str(platform + '-devedition')][str(slave_platform + '_devedition')]['debug_unittest_suites'] = []
    else:
        for p in BRANCHES[branch]['platforms'].keys():
            if p in ['macosx64-devedition', 'win32-devedition', 'win64-devedition']:
                del BRANCHES[branch]['platforms'][p]


# Bug 1365008 - Stop running reftests on Win7 hardware on Try
for branch in BRANCHES.keys():
    if branch not in ['try']:
        continue
    for platform in BRANCHES[branch]['platforms'].keys():
        if platform not in ['win32']:
            continue
        for slave_platform in BRANCHES[branch]['platforms'][platform].keys():
            if slave_platform  == 'win7_ix':
                for test_type in ['opt_unittest_suites', 'debug_unittest_suites']:
                    for test in BRANCHES[branch]['platforms'][platform][slave_platform][test_type][:]:
                        if 'extra_args' not in test[1].keys():
                            continue
                        if '--reftest-suite' in test[1]['extra_args']:
                            BRANCHES[branch]['platforms'][platform][slave_platform][test_type].remove(test)

# Bug 1369065 - Please enable Win32 tests for cedar twig.
for branch in BRANCHES.keys():
    if branch not in ['cedar']:
        continue
    for platform in BRANCHES[branch]['platforms'].keys():
        if platform not in ['win32']:
            continue
        for slave_platform in BRANCHES[branch]['platforms'][platform].keys():
            if slave_platform not in ['win7_ix', 'win7_vm', 'win7_vm_gfx']:
                continue
            for test in ['opt_unittest_suites', 'debug_unittest_suites']:
                BRANCHES[branch]['platforms'][platform][slave_platform][test] = \
                    [item for item in BRANCHES[branch]['platforms'][platform][slave_platform][test] if (item[0].startswith('mochitest') or item in XPCSHELL)]

# Bug 1362387 - enable Linux64 Devedition talos tests on mozilla-beta and jamun
for branch in BRANCHES.keys():
    if branch in ['mozilla-beta', 'jamun']:
        continue
    if 'linux64-devedition' not in BRANCHES[branch]['platforms']:
        continue
    BRANCHES[branch]['platforms']['linux64-devedition']['talos_slave_platforms'] = []

# Ash-specific branch config. Please add any new buildbot test scheduling changes above this block.
for platform in PLATFORMS.keys():
    if platform not in BRANCHES['ash']['platforms']:
        continue

    base_tests = CRASHTEST_E10S + JSREFTEST_E10S_TWO_CHUNKS + MARIONETTE_E10S + MOCHITEST_BC_7_E10S + \
                 MOCHITEST_CLIPBOARD_E10S + MOCHITEST_E10S + MOCHITEST_GPU_E10S + MOCHITEST_MEDIA_E10S + \
                 MOCHITEST_WEBGL_CHUNKED_E10S + WEB_PLATFORM_REFTESTS_E10S

    for slave_platform in PLATFORMS[platform]['slave_platforms']:
        if slave_platform not in BRANCHES['ash']['platforms'][platform]:
            continue

        # Linux jobs are scheduled via in-tree Taskcluster configs, so no need for anything here.
        if slave_platform == "yosemite_r7":
            BRANCHES['ash']['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                base_tests + MOCHITEST_DT_8_E10S + REFTEST_E10S_TWO_CHUNKS + WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                base_tests + MOCHITEST_DT_8_E10S + REFTEST_E10S + WEB_PLATFORM_TESTS_CHUNKED_E10S
        if slave_platform == "win8_64":
            BRANCHES['ash']['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                base_tests + MOCHITEST_DT_8_E10S + REFTEST_E10S_TWO_CHUNKS + REFTEST_NOACCEL_E10S_TWO_CHUNKS +\
                    WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                base_tests + MOCHITEST_DT_8_E10S + REFTEST_E10S + REFTEST_NOACCEL_E10S +\
                    WEB_PLATFORM_TESTS_CHUNKED_E10S
        if slave_platform == "win7_ix":
            BRANCHES['ash']['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                MOCHITEST_CLIPBOARD_E10S + MOCHITEST_MEDIA_E10S
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                MOCHITEST_CLIPBOARD_E10S + MOCHITEST_MEDIA_E10S
        if slave_platform == "win7_vm":
            BRANCHES['ash']['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                CRASHTEST_E10S + JSREFTEST_E10S_TWO_CHUNKS + MARIONETTE_E10S + MOCHITEST_BC_7_E10S + \
                MOCHITEST_DT_8_E10S + MOCHITEST_E10S + WEB_PLATFORM_REFTESTS_E10S + \
                WEB_PLATFORM_TESTS_CHUNKED_MORE_E10S
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                CRASHTEST_E10S + JSREFTEST_E10S_TWO_CHUNKS + MARIONETTE_E10S + MOCHITEST_BC_7_E10S + \
                MOCHITEST_DT_8_E10S + MOCHITEST_E10S + WEB_PLATFORM_REFTESTS_E10S + \
                WEB_PLATFORM_TESTS_CHUNKED_E10S
        if slave_platform == "win7_vm_gfx":
            BRANCHES['ash']['platforms'][platform][slave_platform]['debug_unittest_suites'] = \
                MOCHITEST_GPU_E10S + MOCHITEST_WEBGL_CHUNKED_E10S + REFTEST_E10S_TWO_CHUNKS + \
                    REFTEST_GPU_E10S + REFTEST_NOACCEL_E10S_TWO_CHUNKS
            BRANCHES['ash']['platforms'][platform][slave_platform]['opt_unittest_suites'] = \
                MOCHITEST_GPU_E10S + MOCHITEST_WEBGL_CHUNKED_E10S + REFTEST_E10S + \
                    REFTEST_FOUR_CHUNKS + REFTEST_GPU_E10S + REFTEST_NOACCEL_E10S + \
                    REFTEST_NOACCEL_FOUR_CHUNKS
# Bug 1370298 - Disable BB windows tests that are green in TC
WIN_TC_56_NONGREEN_DEBUG_SUITES = ('reftest-gpu-e10s', 'mochitest-clipboard', 'mochitest-clipboard-e10s', 'mochitest-chrome', 'xpcshell')
for name, branch in items_at_least(BRANCHES, 'gecko_version', 56):
    for platform in ('win32', 'win32-devedition'):
        if platform not in branch['platforms']:
            continue
        for slave_platform in ['win7_vm', 'win7_vm_gfx']:
            if slave_platform not in branch['platforms'][platform]:
                continue
            tests = branch['platforms'][platform][slave_platform]['debug_unittest_suites']
            tests = [(suite_name, suite_config) for (suite_name, suite_config) in tests if any(
                suite_name.startswith(s) for s in WIN_TC_56_NONGREEN_DEBUG_SUITES)]
            branch['platforms'][platform][slave_platform]['debug_unittest_suites'] = tests


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
