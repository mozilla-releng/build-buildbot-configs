slaves = {
    'fedora12-p3': ['p3-linux03'],
    'xp-p3': ['p3-win03'],
    '10.5-g4': ['g4-leopard01'],
    '10.5-g5': ['bm-xserve%02d' % x for x in range(1,6)],
}

all_tests = ('xpcshell', 'crashtest', 'reftest', 'mochitest-plain')

branches = {
    'mozilla-1.9.2': {
        'tinderbox_tree': 'GeriatricMachines',
        'repo_path': 'releases/mozilla-1.9.2',
        'platforms': {
            'linux': {
                'variants': ['fedora12-p3'],
                'tests': all_tests,
            },
            'win32': {
                'variants': ['xp-p3'],
                'tests': all_tests,
            },
            'macosx': {
                'variants': ['10.5-g4', '10.5-g5'],
                'tests': all_tests,
            },
        },
    },
    'mozilla-1.9.1': {
        'tinderbox_tree': 'GeriatricMachines',
        'repo_path': 'releases/mozilla-1.9.1',
        'platforms': {
            'linux': {
                'variants': ['fedora12-p3'],
                'tests': all_tests,
            },
            'win32': {
                'variants': ['xp-p3'],
                'tests': all_tests,
            },
            'macosx': {
                'variants': ['10.5-g4', '10.5-g5'],
                'tests': all_tests,
            },
        },
    },
    'mozilla-2.0': {
        'tinderbox_tree': 'GeriatricMachines',
        'repo_path': 'releases/mozilla-2.0',
        'platforms': {
            'linux': {
                'variants': ['fedora12-p3'],
                'tests': all_tests,
            },
            'win32': {
                'variants': ['xp-p3'],
                'tests': all_tests,
            },
        },
    },
    'mozilla-central': {
        'tinderbox_tree': 'GeriatricMachines',
        'repo_path': 'releases/mozilla-1.9.2',
        'platforms': {
            'linux': {
                'variants': ['fedora12-p3'],
                'tests': all_tests,
            },
            'win32': {
                'variants': ['xp-p3'],
                'tests': all_tests,
            },
        },
    },
}
