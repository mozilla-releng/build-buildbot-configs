from copy import deepcopy

from config import GLOBAL_VARS, PLATFORM_VARS

import b2g_project_branches
reload(b2g_project_branches)
from b2g_project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

# Note that b2g_localconfig.py is symlinked to one of: {production,staging,preproduction}_b2g_config.py
import b2g_localconfig
reload(b2g_localconfig)

from b2g_localconfig import SLAVES, TRY_SLAVES

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
PLATFORM_VARS = deepcopy(PLATFORM_VARS)

GLOBAL_VARS.update(b2g_localconfig.GLOBAL_VARS.copy())

GLOBAL_VARS.update({
    'platforms': {
        'gb_armv7a_gecko': {},
        'gb_armv7a_gecko-debug': {},
    },
    'enable_nightly': True,
    'enable_l10n': False,
    'enable_xulrunner': False,
    'enabled_products': ['b2g'],
    'product_prefix': 'b2g',
})

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']
SYMBOL_SERVER_POST_UPLOAD_CMD = GLOBAL_VARS['symbol_server_post_upload_cmd']
builder_prefix = "B2G "

PLATFORM_VARS = {
        'gb_armv7a_gecko': {
            'product_name': 'b2g',
            'app_name': 'b2g',
            'brand_name': 'b2g',
            'base_name': builder_prefix + '%(platform)s %(branch)s',
            'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
            'src_mozconfig': 'b2g/config/mozconfigs/gb_armv7a_gecko/nightly',
            'src_xulrunner_mozconfig': 'NO-B2G-XULRUNNER',
            'profiled_build': False,
            'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 10,
            'update_platform': None,
            'upload_symbols': False,
            'create_snippet': False,
            'create_partial': False,
            'enable_xulrunner': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': 'obj-b2g',
            'stage_product': 'b2g',
            'enable_codesighs': False,
            'enable_packaging': True,
            'uploadPackages': False,
            'packageTests': False,
            'stage_platform': 'gb_armv7a_gecko',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'GONK_PRODUCT': 'generic',
                'TOOLCHAIN_HOST': 'linux-x86',
            },
            'enable_opt_unittests': False,
            'enable_checktests': False,
            'enable_build_analysis': False,
            'test_pretty_names': False,
            'l10n_check_test': False,
            # MOCK SPECIFIC OPTIONS BELOW
            'use_mock': True,
            'mock_target': 'mozilla-f16-i386',
            'mock_packages': ['autoconf213', 'python', 'zip', 'mercurial', 'git', 'ccache',
                              'glibc-static', 'libstdc++-static'],
            'tooltool_manifest_src': 'b2g/config/tooltool-manifests/releng.manifest',
        },
        'gb_armv7a_gecko-debug': {
            'product_name': 'b2g',
            'app_name': 'b2g',
            'brand_name': 'b2g',
            'base_name': builder_prefix + '%(platform)s %(branch)s',
            'mozconfig': 'NOT-IN-BB-CONF/%(branch)s/nightly',
            'src_mozconfig': 'b2g/config/mozconfigs/gb_armv7a_gecko/debug',
            'src_xulrunner_mozconfig': 'NO-B2G-XULRUNNER',
            'profiled_build': False,
            'builds_before_reboot': b2g_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 10,
            'update_platform': None,
            'upload_symbols': False,
            'create_snippet': False,
            'create_partial': False,
            'enable_xulrunner': False,
            'enable_leaktests': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': 'obj-b2g',
            'stage_product': 'b2g',
            'enable_codesighs': False,
            'enable_packaging': True,
            'uploadPackages': False,
            'packageTests': False,
            'stage_platform': 'gb_armv7a_gecko-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'GONK_PRODUCT': 'generic',
                'TOOLCHAIN_HOST': 'linux-x86',
            },
            'enable_opt_unittests': False,
            'enable_checktests': False,
            'enable_build_analysis': False,
            'test_pretty_names': False,
            'l10n_check_test': False,
            # MOCK SPECIFIC OPTIONS BELOW
            'use_mock': True,
            'mock_target': 'mozilla-f16-i386',
            'mock_packages': ['autoconf213', 'python', 'zip', 'mercurial', 'git', 'ccache',
                              'glibc-static', 'libstdc++-static'],
            'tooltool_manifest_src': 'b2g/config/tooltool-manifests/releng.manifest',
        },
}


# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {
    },
    'try': {
    },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        elif key == 'mobile_platforms' and 'mobile_platforms' in BRANCHES[branch]:
            continue
        # Don't override something that's set
        elif key in ('enable_weekly_bundle',) and key in BRANCHES[branch]:
            continue
        else:
            BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                # put default platform set in all branches, but grab any
                # project_branches.py overrides/additional keys
                if branch in ACTIVE_PROJECT_BRANCHES and PROJECT_BRANCHES[branch].has_key('platforms'):
                    if platform in PROJECT_BRANCHES[branch]['platforms'].keys():
                        if key in PROJECT_BRANCHES[branch]['platforms'][platform].keys():
                            value = deepcopy(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                else:
                    value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                else:
                    value = deepcopy(value)
                BRANCHES[branch]['platforms'][platform][key] = value

            if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch] and \
                    PROJECT_BRANCHES[branch]['platforms'].has_key(platform):
                for key, value in PROJECT_BRANCHES[branch]['platforms'][platform].items():
                    if key == 'env':
                        value = deepcopy(PLATFORM_VARS[platform]['env'])
                        value.update(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                    else:
                        value = deepcopy(value)
                    BRANCHES[branch]['platforms'][platform][key] = value
    # Copy in local config
    if branch in b2g_localconfig.BRANCHES:
        for key, value in b2g_localconfig.BRANCHES[branch].items():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.items():
                    for key, value in platform_config.items():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in b2g_localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Check for project branch removing a platform from default platforms
    if branch in ACTIVE_PROJECT_BRANCHES:
        for key, value in PROJECT_BRANCHES[branch].items():
            if key == 'platforms':
                for platform, platform_config in value.items():
                    if platform_config.get('dont_build'):
                        del BRANCHES[branch]['platforms'][platform]

######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['start_hour'] = [3]
BRANCHES['mozilla-central']['start_minute'] = [2]
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = 'fake'
BRANCHES['mozilla-central']['aus2_base_upload_dir_l10n'] = 'fake'

######## try
# Try-specific configs
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try']['repo_path'] = 'try'
BRANCHES['try']['enable_merging'] = False
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['package_dir'] ='%(who)s-%(got_revision)s'
# Disable Nightly builds
BRANCHES['try']['enable_nightly'] = False
BRANCHES['try']['platforms']['gb_armv7a_gecko']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['gb_armv7a_gecko-debug']['slaves'] = TRY_SLAVES['mock']

######## generic branch configs
for branch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[branch]
    BRANCHES[branch]['product_name'] = branchConfig.get('product_name', None)
    BRANCHES[branch]['app_name']     = branchConfig.get('app_name', None)
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['enabled_products'] = branchConfig.get('enabled_products',
                                                            GLOBAL_VARS['enabled_products'])
    BRANCHES[branch]['enable_nightly'] =  branchConfig.get('enable_nightly', False)
    BRANCHES[branch]['start_hour'] = branchConfig.get('start_hour', [4])
    BRANCHES[branch]['start_minute'] = branchConfig.get('start_minute', [2])
    # nightly updates
    BRANCHES[branch]['create_snippet'] = branchConfig.get('create_snippet', False)
    BRANCHES[branch]['update_channel'] = branchConfig.get('update_channel', 'nightly-%s' % branch)
    BRANCHES[branch]['create_partial'] = branchConfig.get('create_partial', False)
    BRANCHES[branch]['create_partial_l10n'] = branchConfig.get('create_partial_l10n', False)
    BRANCHES[branch]['aus2_user'] = branchConfig.get('aus2_user', GLOBAL_VARS['aus2_user'])
    BRANCHES[branch]['aus2_ssh_key'] = branchConfig.get('aus2_ssh_key', GLOBAL_VARS['aus2_ssh_key'])
    BRANCHES[branch]['aus2_base_upload_dir'] = branchConfig.get('aus2_base_upload_dir', '/opt/aus2/incoming/2/B2G/' + branch)
    BRANCHES[branch]['enUS_binaryURL'] = GLOBAL_VARS['download_base_url'] + branchConfig.get('enUS_binaryURL', '')
    # Platform-specific defaults/interpretation
    for platform in BRANCHES[branch]['platforms']:
        # point to the mozconfigs, default is generic
        if platform.endswith('debug'):
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform.split('-')[0] + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/debug'
        else:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/nightly'

if __name__ == "__main__":
    import sys, pprint
    args = sys.argv[1:]

    if len(args) > 0:
        branches = args
    else:
        branches = BRANCHES.keys()

    for branch in branches:
        print branch
        pprint.pprint(BRANCHES[branch])
