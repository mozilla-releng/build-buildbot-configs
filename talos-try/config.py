from buildbot.steps.shell import WithProperties

GRAPH_CONFIG = ['--resultsServer', 'graphs-stage.mozilla.org', '--resultsLink', '/server/collect.cgi']

TALOS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:tp:tdhtml:tsvg:twinopen:tsspider:tgfx']

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_JSS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tjss']

TALOS_TP4_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tp4']

SLAVES = {
    'linux': ["qm-pubuntu-try%02i" % x for x in range(1,7)],
    'xp': ["qm-pxp-try%02i" % x for x in range(1,7)],
    'vista': ["qm-pvista-try%02i" % x for x in range(1,7)],
    'tiger': ["qm-ptiger-try%02i" % x for x in range(1,7)],
    'leopard': ["qm-pleopard-try%02i" % x for x in range(1,7)],
}

PLATFORMS = {
    'macosx': {},
    'win32': {},
    'linux': {},
}

PLATFORMS['macosx']['slave_platforms'] = ['tiger', 'leopard']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['tiger'] = {'name': "MacOSX Darwin 8.8.1"}
PLATFORMS['macosx']['leopard'] = {'name': "MacOSX Darwin 9.0.0"}

PLATFORMS['win32']['slave_platforms'] = ['xp', 'vista']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "WINNT 5.1"}
PLATFORMS['win32']['vista'] = {'name': "WINNT 6.0"}

PLATFORMS['linux']['slave_platforms'] = ['linux']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['linux'] = {'name': "Linux"}
