from copy import deepcopy

from buildbot.steps.shell import WithProperties

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]


def loadDefaultValues(BRANCHES, branch, branchConfig):
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['branch_name'] = branchConfig.get('branch_name', branch.title())
    BRANCHES[branch]['build_branch'] = branchConfig.get('build_branch', branch.title())
    BRANCHES[branch]['talos_command'] = branchConfig.get('talos_cmd', TALOS_CMD)
    BRANCHES[branch]['fetch_symbols'] = branchConfig.get('fetch_symbols', True)
    BRANCHES[branch]['talos_from_source_code'] = branchConfig.get('talos_from_source_code', True)
    BRANCHES[branch]['support_url_base'] = branchConfig.get('support_url_base', 'http://talos-bundles.pvt.build.mozilla.org')
    BRANCHES[branch]['enable_unittests'] = branchConfig.get('enable_unittests', True)
    BRANCHES[branch]['pgo_strategy'] = branchConfig.get('pgo_strategy', None)
    BRANCHES[branch]['mozharness_talos'] = True


def loadCustomTalosSuites(BRANCHES, SUITES, branch, branchConfig):
    coallesceJobs = branchConfig.get('coallesce_jobs', True)
    BRANCHES[branch]['suites'] = deepcopy(SUITES)
    # Check if Talos is enabled, if False, set 0 runs for all suites
    if branchConfig.get('enable_talos') is False:
        branchConfig['talos_suites'] = {}
        for suite in SUITES.keys():
            branchConfig['talos_suites'][suite] = 0

    # Want to turn on/off a talos suite? Set it in the PROJECT_BRANCHES[branch]['talos_suites']
    # This is the default and will make all talosConfig.get(key,0) calls
    # to default to 0 a.k.a. disabled suite
    talosConfig = {}
    if branchConfig.get('talos_suites'):
        for suite, settings in branchConfig['talos_suites'].items():
            # Normally the setting is just 0 or 1 for talosConfig to enable/disable a test
            # If there's a list, value[0] is the enabling flag and [1] is a dict of customization
            if isinstance(settings, list):
                talosConfig[suite] = settings[0]
                # append anything new in 'suites' for a talos_suite
                for key, value in settings[1].items():
                    if suite in SUITES.keys():
                        BRANCHES[branch]['suites'][suite][key] += value
            else:
                talosConfig[suite] = settings

    for suite in SUITES.keys():
        if not SUITES[suite]['enable_by_default']:
            # Suites that are turned off by default
            BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 0), coallesceJobs) + SUITES[suite]['options']
        else:
            # Suites that are turned on by default
            BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 1), coallesceJobs) + SUITES[suite]['options']


def loadTalosSuites(BRANCHES, SUITES, branch):
    '''
    This is very similar to loadCustomTalosSuites and is to deal with branches that are not in project_branches.py
    but in config.py. Both functions could be unified later on when we do further refactoring.
    '''
    coallesceJobs = BRANCHES[branch].get('coallesce_jobs', True)
    for suite in SUITES.keys():
        if not SUITES[suite]['enable_by_default']:
            # Suites that are turned off by default
            BRANCHES[branch][suite + '_tests'] = (0, coallesceJobs) + SUITES[suite]['options']
        else:
            # Suites that are turned on by default
            BRANCHES[branch][suite + '_tests'] = (1, coallesceJobs) + SUITES[suite]['options']


def nested_haskey(dictionary, *keys):
    if len(keys) == 1:
        return keys[0] in dictionary
    else:
        #recurse
        key, keys = keys[0], keys[1:]
        if key in dictionary:
            return nested_haskey(dictionary[key], *keys)
        else:
            return False


def get_talos_slave_platforms(platforms_dict, platforms):
    """Returns talos_slave_platforms if defined or slave_platform otherwise"""
    ret = []
    for p in platforms:
        ret.extend(platforms_dict[p].get('talos_slave_platforms',
                                         platforms_dict[p]['slave_platforms']))
    return ret
