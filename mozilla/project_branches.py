# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    'build-system': {},
    'devtools':{
        'enable_nightly': True,
        # need both of these to turn off mobile completely because of key in generic config.py
        'enable_mobile': False,
        'mobile_platforms': {},
        'platforms': {
            'macosx-debug': {
                'dont_build': True,
            },
            'macosx': {
                'slave_platforms': [],
            },
            'macosx64': {
                'slave_platforms': ['snowleopard'],
            },
            'android': {
                'tegra_android': {},
            },
        },
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
    'graphics':{
        'enable_unittests': False,
        'enable_talos': False,
    },
    'jaegermonkey': {
        'enable_talos': False,
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
    },
    'mozilla-aurora': {
        'repo_path': 'mozilla-aurora',
        'mozconfig_dir': 'mozilla-aurora',
        'aus2_base_upload_dir': '/opt/aus2/incoming/2/Firefox/mozilla-aurora-bug648066',
        'aus2_base_upload_dir_l10n': '/opt/aus2/incoming/2/Firefox/mozilla-aurora-bug648066',
        'aus2_mobile_base_upload_dir': '/opt/aus2/incoming/2/Fennec/mozilla-aurora-bug648066',
        'aus2_mobile_base_upload_dir_l10n': '/opt/aus2/incoming/2/Fennec/mozilla-aurora-bug648066',
        'create_snippet': True,
        'create_partial': True,
        'create_partial_l10n': True,
        'create_mobile_snippet': True,
        'start_hour': [3],
        'start_minute': [32],
        'enable_nightly': True,
        'enable_mobile_nightly': True,
        'enable_shark': True,
        'enUS_binaryURL':  '/nightly/latest-mozilla-aurora',
        'talos_suites': {
            'remote-ts': 1,
            'remote-tdhtml': 1,
            'remote-tsvg': 1,
            'remote-tsspider': 1,
            'remote-twinopen': 1,
        },
    },
    'places': {
        'platforms': {
            'linux64': {
                'build_space': 6,
            },
            'linux': {
                'build_space': 6,
            },
            'linuxqt': { 
                'build_space': 6,
            },
        },
        'talos_suites': {
            'remote-ts': 1,
            'remote-tdhtml': 1,
            'remote-tsvg': 1,
            'remote-tsspider': 1,
            'remote-twinopen': 1,
        }
    },
    'services-central': {
        'repo_path': 'services/services-central',
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
    #####  TWIGS aka RENTABLE BRANCHES
    'alder': {},
    'birch': {},
    'cedar': {
        'talos_suites': {
            'remote-ts': 1,
            'remote-tdhtml': 1,
            'remote-tsvg': 1,
            'remote-tsspider': 1,
            'remote-twinopen': 1,
        }
    },
    'holly': {},
    'larch': {},
    'maple': {},
}

# We want all for now, but can turn them off in here if necessary
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = branch.title()
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = branch.title()
    PROJECT_BRANCHES[branch]['packaged_unittest_tinderbox_tree'] = branch.title()
