all_tests = ('xpcshell', 'crashtest', 'reftest', 'mochitest-plain')

platforms = {
    'linux': {
        'variants': {'fedora12-p3': ['p3-linux03']},
        'tests': all_tests,
    },
    'win32': {
        'variants': {'xp-p3': ['p3-win03']},
        'tests': all_tests,
    },
    'macosx': {
        'variants': {'10.5-g4': ['g4-leopard01'],
                     '10.5-g5': ['bm-xserve03', 'bm-xserve04']},
        'tests': all_tests,
    },
}

