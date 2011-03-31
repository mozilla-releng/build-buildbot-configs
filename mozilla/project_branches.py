# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    'graphics':{
        'enable_unittests': False,
        'enable_talos': False,
        },
    'build-system': {},
    'services-central': {
        'repo_path': 'services/services-central',
    },
    'maple': {},
    'cedar': {},
    'birch': {},
    'devtools':{
        'enable_nightly': True,
        # need both of these to turn off mobile completely because of key in generic config.py
        'enable_mobile': False,
        'mobile_platforms': {},
        'platforms': {
            'linux': {},  'linuxqt': {},'linux-debug': {}, 'linux64': {}, 'linux64-debug': {},
            'win32': {}, 'win32-debug': {},
            'macosx64-debug': {
                'slave_platforms': ['snowleopard'],
            },
            'macosx64': {
                'slave_platforms': ['snowleopard'],
            },
            'android': {
                    'test_only_platform': True,
                    'tegra_android': {},
                },
            'win64': {
                    'test_only_platform': True,
                },
        },
    },
    'places': {
        'platforms': {
            'win32': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'linux64': {
                'build_space': 6,
            },
            'linux': {
                'build_space': 6,
            },
            'linuxqt': { 
                'build_space': 6,
            },
            'android': {
                'test_only_platform': True,
            },
            'win64': {
                'test_only_platform': True,
            },
            'macosx': {
                'test_only_platform': True,
            },
        },
    },
    'tracemonkey': {
        'repo_path': 'tracemonkey',
        'mozconfig_dir': 'tracemonkey',
        'branch_name': 'TraceMonkey',
        'mobile_branch_name': 'TraceMonkey',
        'build_branch': 'TraceMonkey',
        'start_hour': [3],
        'start_minute': [32],
        'enable_nightly': True,
        'enable_mobile_nightly': True,
        'enable_shark': True,
        'platforms': {
            'win32': {},
            'macosx64': {},
            'macosx-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'linux64': {
                'build_space': 7,
            },
            'linux': {
                'build_space': 7,
            },
            'linuxqt': { 
                'build_space': 7,
            },
            'linux-debug': {
                'enable_valgrind_checktests': True,
            },
            'linux64-debug': {
                'enable_valgrind_checktests': True,
            },
            'android': {
                'test_only_platform': True,
            },
            'win64': {
                'test_only_platform': True,
            },
            'macosx': {
                'test_only_platform': True,
            },
        }, 
        'create_snippet': True,
        'create_partial': True,
        'talos_suites': {
            'remote-ts': 1,
            'remote-tdhtml': 1,
            'remote-tsvg': 1,
            'remote-tsspider': 1,
            'remote-tpan': 1,
            'v8': 1,
        }
    },
    'electrolysis': {
        'mozconfig_dir': 'electrolysis',
        'mobile_platforms': {
            'maemo5-gtk': {
                'mozconfig': 'mobile/maemo5-gtk/mobile-e10s/nightly',
            },
            'maemo5-qt': {
                'mozconfig': 'mobile/maemo5-qt/mobile-e10s/nightly',
            },
            'linux': {
                'mozconfig': 'mobile/linux-i686/mobile-e10s/nightly',
            },
            'win32': {
                'mozconfig': 'mobile/win32-i686/mobile-e10s/nightly',
            },
            'macosx': {
                'mozconfig': 'mobile/macosx-i686/mobile-e10s/nightly',
            },
            'android-r7': {},
        },
        'enable_talos': False,
    },
    'jaegermonkey': {
        'enable_talos': False,
    },
}

# We want all for now, but can turn them off in here if necessary
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = branch.title()
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = branch.title()
    PROJECT_BRANCHES[branch]['packaged_unittest_tinderbox_tree'] = branch.title()
