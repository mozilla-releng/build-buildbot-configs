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
    }
}

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = branch.title()
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = branch.title()
    PROJECT_BRANCHES[branch]['packaged_unittest_tinderbox_tree'] = branch.title()
