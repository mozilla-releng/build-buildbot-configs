from copy import deepcopy

import buildbotcustom.env
reload(buildbotcustom.env)
from buildbotcustom.env import MozillaEnvironments

# This is only used within this file so it doesn't need to be part of the
# big dict
TRY_LINUX      = ['momo-vm-linux-%02i' % x for x in range (1,2)]
TRY_LINUX64    = ['momo-vm-linux64-%02i' % x for x in range (1,2)]
TRY_MAC        = ['mini-01','mini-10']
TRY_WIN32      = ['momo-vm-win2k3-03', 'momo-vm-win2k3-16']


TRY_SLAVES = {
    'linux':       TRY_LINUX,
#    'linux-debug':       TRY_LINUX,
    'linux64':     TRY_LINUX64,
    'win32':       TRY_WIN32,
    'macosx':      TRY_MAC,
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
            'builds_before_reboot': 0,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'env': {
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
            'enable_opt_unittests': True,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64': {
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 0,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'env': {
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
            'enable_opt_unittests': True,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx': {
            'base_name': 'OS X 10.5.2 %(branch)s',
            'mozconfig': 'macosx/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 0,
            'build_space': 8,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'platform_objdir': "%s/ppc" % OBJDIR,
            'update_platform': 'Darwin_Universal-gcc3',
            'env': {
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
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32': {
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': 0,
            'build_space': 9,
            'upload_symbols': True,
            'download_symbols': True,
            'platform_objdir': OBJDIR,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'env': {
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
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux-debug': {
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 0,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 7,
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':0',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_UMASK': '002',
            },
            'enable_unittests': True,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64-debug': {
            'base_name': 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 0,
            'download_symbols': False,
            'packageTests': True,
            'build_space': 7,
            'platform_objdir': OBJDIR,
            'enable_ccache': False,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':0',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_UMASK': '002',
            },
            'enable_unittests': False,
            'enable_checktests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx-debug': {
            'base_name': 'OS X 10.5.2 %(branch)s leak test',
            'mozconfig': 'macosx/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': 0,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 5,
            'platform_objdir': OBJDIR,
            'env': {
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
            'builds_before_reboot': 0,
            'download_symbols': True,
            'build_space': 7,
            'platform_objdir': OBJDIR,
            'env': {
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
    'tryserver': { 'platforms': { 'linux': {}, #'linux-debug': {},
                                  'win32': {}, #'win32-debug': {},
                                  'macosx': {},# 'macosx-debug': {},
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

######## tryserver
# Try-specific configs 
BRANCHES['tryserver']['stage_username'] = 'tbirdbld'
BRANCHES['tryserver']['stage_ssh_key'] = 'tbirdbld_dsa'
BRANCHES['tryserver']['stage_base_path'] = '/home/ftp/pub/thunderbird/tryserver-builds'
BRANCHES['tryserver']['enable_merging'] = False
BRANCHES['tryserver']['enable_try'] = True
BRANCHES['tryserver']['repo_path'] = 'try-comm-central'
BRANCHES['tryserver']['cc_try_factory' ] = True
BRANCHES['tryserver']['run_client_py'] = True
BRANCHES['tryserver']['alive_step'] = 'mailbloat'
BRANCHES['tryserver']['enable_mail_notifier'] = True
BRANCHES['tryserver']['notify_real_author'] = True
BRANCHES['tryserver']['package_url'] ='http://ftp.mozilla.org/pub/mozilla.org/thunderbird/tryserver-builds'
BRANCHES['tryserver']['package_dir'] ='%(who)s-%(got_revision)s'
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['tryserver']['repo_path'] = 'try-comm-central'
BRANCHES['tryserver']['start_hour'] = [3]
BRANCHES['tryserver']['start_minute'] = [2]
# Disable Nightly builds
BRANCHES['tryserver']['enable_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['tryserver']['enable_xulrunner'] = False
BRANCHES['tryserver']['enable_mac_a11y'] = True
# only do unittests locally until they are switched over to talos-r3
#BRANCHES['tryserver']['unittest_masters'] = []
BRANCHES['tryserver']['tinderbox_tree'] = 'ThunderbirdTry'
BRANCHES['tryserver']['packaged_unittest_tinderbox_tree'] = 'ThunderbirdTry'
BRANCHES['tryserver']['download_base_url'] ='http://ftp.mozilla.org/pub/mozilla.org/thunderbird/tryserver-builds'
BRANCHES['tryserver']['enable_l10n'] = False
BRANCHES['tryserver']['enable_l10n_onchange'] = False
BRANCHES['tryserver']['l10nNightlyUpdate'] = False
BRANCHES['tryserver']['l10nDatedDirs'] = False
BRANCHES['tryserver']['enable_codecoverage'] = False
BRANCHES['tryserver']['enable_shark'] = False
BRANCHES['tryserver']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['tryserver']['aus2_base_upload_dir'] = 'fake'
BRANCHES['tryserver']['platforms']['linux']['slaves'] = TRY_SLAVES['linux']
BRANCHES['tryserver']['platforms']['linux64']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['tryserver']['platforms']['win32']['slaves'] = TRY_SLAVES['win32']
BRANCHES['tryserver']['platforms']['macosx']['slaves'] = TRY_SLAVES['macosx']
#BRANCHES['tryserver']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['linux']
#BRANCHES['tryserver']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['linux64']
#BRANCHES['tryserver']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win32']
#BRANCHES['tryserver']['platforms']['macosx-debug']['slaves'] = TRY_SLAVES['macosx']
BRANCHES['tryserver']['platforms']['linux']['upload_symbols'] = False
#BRANCHES['tryserver']['platforms']['linux-debug']['upload_symbols'] = False
BRANCHES['tryserver']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['tryserver']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['tryserver']['platforms']['win32']['upload_symbols'] = False
#BRANCHES['tryserver']['platforms']['win32']['env']['SYMBOL_SERVER_HOST'] = 'build.mozilla.org'
#BRANCHES['tryserver']['platforms']['win32']['env']['SYMBOL_SERVER_USER'] = 'trybld'
#BRANCHES['tryserver']['platforms']['win32']['env']['SYMBOL_SERVER_PATH'] = '/symbols/windows'
#BRANCHES['tryserver']['platforms']['win32']['env']['SYMBOL_SERVER_SSH_KEY'] = '/c/Documents and Settings/cltbld/.ssh/trybld_dsa'
 
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
