all_tests = ('xpcshell', 'crashtest', 'reftest', 'mochitest-plain')

p3_linux_slaves = ['p3-linux01', 'p3-linux02']
p3_win_slaves = ['p3-win01', 'p3-win02']
g4_leopard_slaves = ['g4-leopard01']
g4_tiger_slaves = ['g4-tiger01', 'g4-tiger02']

platforms = {
    'p3-linux':
   	{'platform': 'linux',
         'tests': all_tests,
         'slaves': p3_linux_slaves,
        },
    'p3-win':
   	{'platform': 'win32',
         'tests': all_tests,
         'slaves': p3_win_slaves,
        },
    'g4-leopard':
   	{'platform': 'macosx',
         'tests': all_tests,
         'slaves': g4_leopard_slaves,
        },
    'g4-tiger':
   	{'platform': 'macosx',
         'tests': all_tests,
         'slaves': g4_tiger_slaves,
        },
}

