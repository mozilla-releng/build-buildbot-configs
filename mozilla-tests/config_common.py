from copy import deepcopy

TALOS_CMD = ['python', '-u', 'run_tests.py', '--noisy']


def loadDefaultValues(BRANCHES, branch, branchConfig):
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['branch_name'] = branchConfig.get('branch_name', branch.title())
    BRANCHES[branch]['build_branch'] = branchConfig.get('build_branch', branch.title())
    BRANCHES[branch]['mobile_branch_name'] = branch.title()
    BRANCHES[branch]['talos_command'] = branchConfig.get('talos_cmd', TALOS_CMD)
    BRANCHES[branch]['fetch_symbols'] = branchConfig.get('fetch_symbols', True)
    BRANCHES[branch]['fetch_release_symbols'] = branchConfig.get('fetch_release_symbols', False)
    BRANCHES[branch]['talos_from_source_code'] = branchConfig.get('talos_from_source_code', True)
    BRANCHES[branch]['support_url_base'] = branchConfig.get('support_url_base', 'http://talos-bundles.pvt.build.mozilla.org')
    BRANCHES[branch]['enable_unittests'] = branchConfig.get('enable_unittests', True)
    BRANCHES[branch]['pgo_strategy'] = branchConfig.get('pgo_strategy', None)
    BRANCHES[branch]['pgo_platforms'] = branchConfig.get('pgo_platforms', ['linux', 'linux64', 'win32', 'win64'])
    BRANCHES[branch]['mozharness_talos'] = True
    BRANCHES[branch]['script_repo_manifest'] = "https://hg.mozilla.org/%(repo_path)s/raw-file/%(revision)s/" + \
                                               "testing/mozharness/mozharness.json"


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

def delete_slave_platform(BRANCHES, PLATFORMS, platforms_to_delete, branch_exclusions=[]):
    for branch in set(BRANCHES.keys()) - set(branch_exclusions):
        for platform, slave_platform in platforms_to_delete.iteritems():
            if platform not in BRANCHES[branch]['platforms']:
                continue
            if nested_haskey(BRANCHES[branch]['platforms'], platform, slave_platform):
                del BRANCHES[branch]['platforms'][platform][slave_platform]
            # Disable talos for this branch by making sure talos_slave_platforms is set.
            if 'talos_slave_platforms' not in BRANCHES[branch]['platforms'][platform]:
                # Need to copy the list from PLATFORMS, so we don't change what's in PLATFORMS.
                BRANCHES[branch]['platforms'][platform]['talos_slave_platforms'] = PLATFORMS[platform]['slave_platforms'][:]
            if slave_platform in BRANCHES[branch]['platforms'][platform]['talos_slave_platforms']:
                BRANCHES[branch]['platforms'][platform]['talos_slave_platforms'].remove(slave_platform)
