from copy import deepcopy

import buildbotcustom.env
reload(buildbotcustom.env)
from buildbotcustom.env import MozillaEnvironments

# This is only used within this file so it doesn't need to be part of the
# big dict
TRY_LINUX      = ['momo-vm-linux-%02i' % x for x in [1,10,17,18]]
TRY_LINUX64    = ['momo-vm-linux64-%02i' % x for x in [1,11]]
TRY_MAC64      = ['tb2-darwin10-slave%02i'  % x for x in [71]]
TRY_MAC        = ['tb2-darwin9-slave%02i'  % x for x in [72]]
TRY_WIN32      = ['momo-vm-win2k3-03', 'momo-vm-win2k3-16']


TRY_SLAVES = {
    'linux':       TRY_LINUX,
#    'linux-debug':       TRY_LINUX,
    'linux64':     TRY_LINUX64,
    'win32':       TRY_WIN32,
    'macosx':      TRY_MAC,
    'macosx64':    TRY_MAC64,
}

SLAVES = {
    'linux': [],
}

GLOBAL_VARS = {
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'hgurl': 'http://hg.mozilla.org/',
    'hghost': 'hg.mozilla.org',
    'config_repo_path': 'build/buildbot-configs',
    'config_subdir': 'thunderbird',
    'objdir': 'objdir',
    'objdir_unittests': 'objdir',
    'stage_server': 'stage.mozilla.org',
    'stage_group': None,
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_tbrd/',
    'graph_server': None,
    'graph_selector': None,
    'build_tools_repo_path': 'build/tools',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'default_build_space': 5,
    'default_l10n_space': 3,
    'base_clobber_url': 'http://build.mozillamessaging.com/clobberer',
    'default_clobber_time': 24*7, # 1 week
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning
    'talos_masters': [ ],
    # List of unittest masters to notify of new builds to test,
    # and if a failure to notify the master should result in a warning
    'unittest_masters': [
                          ('momo-vm-03.sj.mozillamessaging.com:9015', False, 3),
                          ('momo-vm-03.sj.mozillamessaging.com:9920', False, 3),
                        ],
    'unittest_suites': [
        ('mozmill', ['mozmill']),
        ('xpcshell', ['xpcshell']),
    ],
    'geriatric_masters': [],
    'platforms': {
        'linux': {},
        'linux64': {},
        'win32': {},
        'macosx': {},
        'macosx64': {},
    },
    'product_name': 'thunderbird',
    'app_name': 'mail',
    'brand_name': 'Shredder',
    'tinderbox_tree': 'ThunderbirdTry',
    'enable_codecoverage': False,
#    'hash_type': 'sha512',
}

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']

PLATFORM_VARS = {
        'linux': {
            'base_name': 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/lib',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'tbrdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbrdbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_UMASK': '002',
                'DISPLAY': ':0',
            },
            'unittest-env': {
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/lib',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64': {
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/lib64',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'tbrdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbrdbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_UMASK': '002',
                'DISPLAY': ':0',
            },
            'unittest-env': {
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/lib64',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx': {
            'base_name': 'OS X 10.5.2 %(branch)s',
            'mozconfig': 'macosx/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 8,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'platform_objdir': OBJDIR,
            'update_platform': 'Darwin_Universal-gcc3',
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'tbrdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/tbrdbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'MOZ_PKG_PLATFORM': 'mac',
            },
            'enable_opt_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx64': {
            'base_name': 'OS X 10.6 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 8,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'platform_objdir': "%s/i386" % OBJDIR,
            'update_platform': 'Darwin_x86_64-gcc3',
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'tbrdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/tbrdbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
            },
            'enable_opt_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32': {
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'build_space': 9,
            'upload_symbols': True,
            'download_symbols': True,
            'platform_objdir': OBJDIR,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
                'SYMBOL_SERVER_USER': 'tbrdbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/tbrdbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                # Source server support, bug 506702
            #    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe'
            },
            'enable_opt_unittests': True,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux-debug': {
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 7,
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/lib',
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':0',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_UMASK': '002',
            },
            'unittest-env': {
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/lib',
            },
            'enable_unittests': False,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64-debug': {
            'base_name': 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': False,
            'packageTests': True,
            'build_space': 7,
            'platform_objdir': OBJDIR,
            'enable_ccache': False,
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/lib64',
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':0',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_UMASK': '002',
            },
            'unittest-env': {
                'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/lib64',
            },
            'enable_unittests': False,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx-debug': {
            'base_name': 'OS X 10.5.2 %(branch)s leak test',
            'mozconfig': 'macosx/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 5,
            'platform_objdir': OBJDIR,
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
            'enable_unittests': True,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx64-debug': {
            'base_name': 'OS X 10.6 %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 5,
            'platform_objdir': OBJDIR,
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
            'enable_unittests': True,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32-debug': {
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 1,
            'download_symbols': True,
            'build_space': 7,
            'platform_objdir': OBJDIR,
            'env': {
                'DISABLE_LIGHTNING_INSTALL': '1',
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
            },
            'enable_unittests': True,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
}

# All branches that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'try': { 'platforms': { 'linux': {}, #'linux-debug': {},
                                  'win32': {}, #'win32-debug': {},
                                  'macosx': {},# 'macosx-debug': {},
                                  'macosx64': {},# 'macosx64-debug': {},
                                  'linux64': {},# 'linux64-debug': {}, 
                                 }},
}

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

######## try
# Try-specific configs 
BRANCHES['try']['stage_username'] = 'tbirdbld'
BRANCHES['try']['stage_ssh_key'] = 'tbirdbld_dsa'
BRANCHES['try']['stage_base_path'] = '/home/ftp/pub/thunderbird/try-builds'
BRANCHES['try']['enable_merging'] = False
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['repo_path'] = 'try-comm-central'
BRANCHES['try']['cc_try_factory' ] = True
BRANCHES['try']['run_client_py'] = True
BRANCHES['try']['alive_step'] = 'mailbloat'
BRANCHES['try']['enable_mail_notifier'] = True
BRANCHES['try']['notify_real_author'] = True
BRANCHES['try']['package_url'] ='http://ftp.mozilla.org/pub/mozilla.org/thunderbird/try-builds'
BRANCHES['try']['package_dir'] ='%(who)s-%(got_revision)s'
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try']['repo_path'] = 'try-comm-central'
BRANCHES['try']['start_hour'] = [3]
BRANCHES['try']['start_minute'] = [2]
# Disable Nightly builds
BRANCHES['try']['enable_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['try']['enable_xulrunner'] = False
BRANCHES['try']['enable_mac_a11y'] = True
# only do unittests locally until they are switched over to talos-r3
#BRANCHES['try']['unittest_masters'] = []
BRANCHES['try']['tinderbox_tree'] = 'ThunderbirdTry'
BRANCHES['try']['packaged_unittest_tinderbox_tree'] = 'ThunderbirdTry'
BRANCHES['try']['download_base_url'] ='http://ftp.mozilla.org/pub/mozilla.org/thunderbird/try-builds'
BRANCHES['try']['enable_l10n'] = False
BRANCHES['try']['enable_l10n_onchange'] = False
BRANCHES['try']['l10nNightlyUpdate'] = False
BRANCHES['try']['l10nDatedDirs'] = False
BRANCHES['try']['enable_codecoverage'] = False
BRANCHES['try']['enable_weekly_bundle'] = False
BRANCHES['try']['enable_shark'] = False
BRANCHES['try']['create_snippet'] = False
BRANCHES['try']['mozconfig_branch'] = 'default'
# need this or the master.cfg will bail
BRANCHES['try']['aus2_base_upload_dir'] = 'fake'
for platform in ['linux', 'linux64', 'win32', 'macosx', 'macosx64']:
    BRANCHES['try']['platforms'][platform]['slaves'] = TRY_SLAVES[platform]
    BRANCHES['try']['platforms'][platform]['upload_symbols'] = False

#BRANCHES['try']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['linux']
#BRANCHES['try']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['linux64']
#BRANCHES['try']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win32']
#BRANCHES['try']['platforms']['macosx-debug']['slaves'] = TRY_SLAVES['macosx']
#BRANCHES['try']['platforms']['linux-debug']['upload_symbols'] = False
#BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_HOST'] = 'build.mozilla.org'
#BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_USER'] = 'trybld'
#BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_PATH'] = '/symbols/windows'
#BRANCHES['try']['platforms']['win32']['env']['SYMBOL_SERVER_SSH_KEY'] = '/c/Documents and Settings/cltbld/.ssh/trybld_dsa'

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
