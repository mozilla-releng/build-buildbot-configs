from buildbot.steps.shell import WithProperties

GRAPH_CONFIG = ['--resultsServer', 'graphs-stage.mozilla.org', '--resultsLink', '/server/collect.cgi']

TALOS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:tdhtml:tsvg:twinopen:tsspider:tgfx']

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_JSS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tjss']

TALOS_DIRTY_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:ts_places_generated_min:ts_places_generated_med:ts_places_generated_max']
TALOS_DIRTY_ADDONS = ['/builds/buildbot/profiles/dirtyDBs.zip', '/builds/buildbot/profiles/dirtyMaxDBs.zip']

TALOS_TP4_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tp4']

TALOS_COLD_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:ts_cold']

SLAVES = {
    'linux': ["talos-rev1-linux%02i" % x for x in range(1,10)],
    'xp': ["talos-rev1-xp%02i" % x for x in range(1,10)],
    'vista': ["talos-rev1-vista%02i" % x for x in range(1,10)],
    'tiger': ["talos-rev1-tiger%02i" % x for x in range(1,10)],
    'leopard': ["talos-rev1-leopard%02i" % x for x in range(1,10)],
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

NO_WIN = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['macosx']['slave_platforms']
