
# Buildbot configuration file


import types

# Simple copy of a dictionary tree, with the ability to ignore certain keys.
# Note: for simplicity, exceptions apply at all levels of the data structure
def key_copy(dfrom, dto, exceptions):
    for key in dfrom:
        if key in exceptions:
            continue
        if not dto.has_key(key):
            dto[key] = {}
        if type(dfrom[key]) is types.DictType:
            key_copy(dfrom[key], dto[key], exceptions)
        else:
            dto[key] = dfrom[key]


branch_configs = {
    'comm-central': {  # key is branch display name
        'branch_name': '', # actual hg branch
        'platforms': ['linux', 'linux64', 'macosx', 'macosx64', 'win32'],
    },
    'comm-1.9.2': {
        'branch_name': 'comm-1.9.2',
        'platforms': ['linux', 'linux64', 'macosx', 'win32'],
    },
}

linux_slaves            = [ 'momo-vm-linux-%02i' % x for x in [2,3,4,5,6,7,8,9,11,12,13,14,15,16]]
linux_unittest_slaves   = [ 'momo-vm-fedora12-%02i' % x for x in [2,3,4]]
linux64_slaves          = [ 'momo-vm-linux64-%02i' % x for x in [ 2,3,5,6 ]]
linux64_unittest_slaves = [ 'momo-vm-fedora12-64-%02i' % x for x in [ 2,3,4 ]]
win32_slaves            = [ 'momo-vm-win2k3-%02i' % x for x in [ 1,4,5,8,9,10,11,12,13,14,15,17 ] ]
# mini-07 needs a new drive
macosx_slaves           = [ 'mini-%02i' % x for x in [ 3,4,5,6,8,9 ] ]
macosx64_slaves         = [ 'momo-xserve-01'] + [ 'mini64-%02i' % x for x in [ 1,3,4,5,6 ] ]


platforms = {
    'linux': {
        'check_objdir': 'objdir-tb',
        'update_platform': 'Linux_x86-gcc3',
        'display_name': 'Linux',
        'platform_objdir': 'objdir-tb',
        'slaves' : linux_slaves,
	'test-slaves': linux_unittest_slaves,
        'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/tbirdbld_dsa',
    },
    'linux64': {
        'check_objdir': 'objdir-tb',
        'update_platform':  'Linux_x86_64-gcc3',
        'display_name':  'Linux x86-64',
        'platform_objdir': 'objdir-tb',
        'slaves': linux64_slaves,
        'test-slaves': linux64_unittest_slaves,
        'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/tbirdbld_dsa',
    },
    'win32': {
        'check_objdir': 'objdir-tb',
        'update_platform':  'WINNT_x86-msvc',
        'display_name':  'WINNT 5.2',
        'platform_objdir': 'objdir-tb',
        'slaves': win32_slaves,
        'test-slaves': win32_slaves,
        'SYMBOL_SERVER_SSH_KEY': '/c/Documents and Settings/cltbld/.ssh/tbirdbld_dsa',
    },
    'macosx': {
        'update_platform':  'Darwin_Universal-gcc3',
        'display_name':  'MacOSX 10.5',
        'slaves': macosx_slaves,
        'test-slaves': macosx_slaves,
        'SYMBOL_SERVER_SSH_KEY': '/Users/cltbld/.ssh/tbirdbld_dsa',
        # Override default of macosx64 for trunk builds until we switch
        # (bug 599796/bug 558837)
        'env': { 'MOZ_PKG_PLATFORM': 'mac' },
    },
    'macosx64': {
        'update_platform':  'Darwin_x86_64-gcc3',
        'display_name':  'MacOSX 10.6',
        'slaves': macosx64_slaves,
        'test-slaves': macosx64_slaves,
        'SYMBOL_SERVER_SSH_KEY': '/Users/cltbld/.ssh/tbirdbld_dsa',
    },
}


build_configs = {
    'comm-central-trunk': {
        'aus': {
            'base_upload_dir': '/opt/aus/build/0/Thunderbird/comm-central',
            'host': 'aus-staging.sj.mozillamessaging.com',
            'user': 'tbirdbld',
        },
        'branch_config': 'comm-central',
        'builder_type': 'nightly',
        'factory': 'CCNightlyBuildFactory',
        'client_py_extra_args':  ['--skip-comm', '--hg-options=--verbose --time' ],
        'env': {},
        'hg_branch': 'comm-central',
        'l10n_repo': 'l10n-central',
        'l10n_tree': 'tb',
        'leak_threshold': {
            'linux': 970000,
            'macosx': 2500000,
            'macosx64': 2500000,
            'win32': 110000,
        },
        'milestone': 'comm-central',
        'mozilla_central_branch':  'mozilla-central',
        'period': 50400,
        'tinderbox_tree': 'Thunderbird',
        'unittest_masters': [
           ('momo-vm-03.sj.mozillamessaging.com:9010',False,3),
         ],
    },
    'comm-central-trunk-bloat': {
        'branch_config':  'comm-central',
        'builder_type':  'bloat',
        'factory': 'CCNightlyBuildFactory',
        'client_py_args':  ['--skip-comm', '--mozilla-repo=http://hg.mozilla.org/mozilla-central', '--hg-options=--verbose --time' ],
        'env': {
            'XPCOM_DEBUG_BREAK': 'stack',
            'DISPLAY': ':2',
        },
        'hg_branch':  'comm-central',
        'leak_threshold': {
            'linux': 970000, #
            'linux64': 1400000, #
            'macosx': 3400000, #
            'win32': 1400000, #
        },
        'mozilla_central_branch':  'mozilla-central',
        'period': 50400,
        'tinderbox_tree': 'Thunderbird',
    },
    'comm-1.9.2': {
        'aus': {
            'base_upload_dir': '/opt/aus/build/0/Thunderbird/comm-1.9.2', #
            'host': 'aus-staging.sj.mozillamessaging.com',
            'user': 'tbirdbld',
        },
        'branch_config':  'comm-1.9.2',
        'builder_type': 'nightly',
        'factory': 'CCNightlyBuildFactory',
        'client_py_extra_args':  ['--skip-comm', '--hg-options=--verbose --time'],
        'env': {},
        'hg_branch':  'releases/comm-1.9.2', #
        'l10n_repo': 'releases/l10n-mozilla-1.9.2', #
        'l10n_tree': 'tb31x',
        'leak_threshold': {
            'linux': 970000,
            'macosx': 2500000,
            'win32': 110000,
        },
        'milestone': 'comm-1.9.2', #
        'mozilla_central_branch':  'releases/mozilla-1.9.2', #
        'nightly_hour': [0],
        'tinderbox_tree': 'Thunderbird3.1',
    },
    'comm-1.9.2-bloat': {
        'branch_config':  'comm-1.9.2',
        'builder_type':  'bloat',
        'factory': 'CCNightlyBuildFactory',
        'client_py_args':  ['--skip-comm', '--hg-options=--verbose --time', '--mozilla-repo=http://hg.mozilla.org/releases/mozilla-1.9.2' ],
        'env': {
            'XPCOM_DEBUG_BREAK': 'stack',
            'DISPLAY': ':2',
        },
        'hg_branch':  'releases/comm-1.9.2', #
        'leak_threshold': {
            'linux': 970000,
            'macosx': 2500000,
            'win32': 110000,
        },
        #'milestone': 'comm-1.9.2', #
        'mozilla_central_branch':  'releases/mozilla-1.9.2', #
        'tinderbox_tree': 'Thunderbird3.1',
    },
    'comm-1.9.2-unittest': {
        'branch_config':  'comm-1.9.2',
        'builder_type': 'check',
        'env': {},
        'factory': 'CCUnittestBuildFactory',
        'hg_branch':  'releases/comm-1.9.2', #
        'client_py_extra_args':  ['--skip-comm', '--hg-options=--verbose --time' ],
        'leak_threshold': {
            'linux': 970000,
            'macosx': 2500000,
            'win32': 110000,
        },
        'mozilla_central_branch':  'releases/mozilla-1.9.2', #
        'mozmill': True,
        'nightly': False,
        'tinderbox_tree': 'Thunderbird3.1',
    },
}

# Update all configs using constants and conditionals
for config_name in build_configs:
    # init
    config = build_configs[config_name]
    branch_config = branch_configs[config['branch_config']]
    branch = branch_config['branch_name']
    config['platforms'] = {}
    if not config.has_key('platforms'):
        config['env'] = {}

    if not config.has_key('client_py_extra_args'):
        config['client_py_extra_args'] = []
    config['client_py_extra_args'].extend(['--skip-venkman', '--skip-chatzilla'])

    if config['builder_type'] != 'check':
        config['env']['CVS_RSH'] = 'ssh'
        config['env']['MOZ_OBJDIR'] = 'objdir-tb'
        config['env']['MOZ_CRASHREPORTER_NO_REPORT'] = '1'

    #TODO - what is common about these configs?
    if config_name in ['comm-central-trunk', 'comm-central-bloat', 'comm-central', 'comm-1.9.2', 'comm-1.9.2-bloat']:
        config['env']['SYMBOL_SERVER_HOST'] = 'dm-symbolpush01.mozilla.org'
        config['env']['SYMBOL_SERVER_USER'] = 'tbirdbld'
        config['env']['SYMBOL_SERVER_PATH'] = '/mnt/netapp/breakpad/symbols_tbrd/'

    if config['builder_type'] == 'bloat':
        config['mozconfig'] = 'debug'
        config['nightly'] = False
        config['leak'] = True
        config['package'] = False
        config['upload_stage'] = False
        config['codesighs'] = False
        config['l10n'] = False
        config['create_snippet'] = False
    elif config['builder_type'] == 'nightly':
        config['mozconfig'] = 'nightly'
        config['package'] = True
        config['upload_stage'] = True
        config['codesighs'] = True
        config['l10n'] = True
        config['l10n_nightly_updates'] = True
        config['create_snippet'] = True
        if config['hg_branch'] in ['comm-central']:
            config['packageTests'] = True

    if config_name in ['comm-central', 'comm-1.9.2' ]:
        #TODO - clean this up
        if not config['platforms'].has_key('linux64'):
            config['platforms']['linux64'] = {}
            config['platforms']['linux64']['l10n'] = {}
        config['platforms']['linux64']['l10n'] = False

    if config.get('codesighs') == True:
        config['env']['TINDERBOX_OUTPUT'] = '1'

    for platform in branch_config['platforms']:
        if not config['platforms'].has_key(platform):
            config['platforms'][platform] = {}
        if not config['platforms'][platform].has_key('env'):
            config['platforms'][platform]['env'] = {}

        config['platforms'][platform]['base_name'] = '%s %s' % (platforms[platform]['display_name'], config['branch_config'])
        if not config['builder_type'] == 'check':
            config['platforms'][platform]['profiled_build']  = False

        if config_name in ['comm-central-trunk']:
            config['platforms'][platform]['enable_checktests'] = True

        if config['builder_type'] == 'bloat':
            config['platforms'][platform]['upload_symbols'] = False
            if platform.find('linux') == 0:
                config['platforms'][platform]['env']['LD_LIBRARY_PATH'] = 'objdir-tb/mozilla/dist/bin'
            # Mac OS X hack
            if platform.find('macos') == 0:
                config['platforms'][platform]['platform_objdir'] = 'objdir-tb'
                config['platforms'][platform]['check_objdir'] = 'objdir-tb'
        elif config['builder_type'] == 'nightly':
            config['platforms'][platform]['upload_symbols'] = True
            # Mac OS X hack
            if platform == 'macosx64':
                config['platforms'][platform]['platform_objdir'] = 'objdir-tb/i386'
                config['platforms'][platform]['check_objdir'] = 'objdir-tb/x86_64'
            elif platform.find('macos') == 0:
                config['platforms'][platform]['platform_objdir'] = 'objdir-tb/ppc'
                config['platforms'][platform]['check_objdir'] = 'objdir-tb/ppc'

# create final data structure
BRANCHES = {}
for config_name in build_configs:
    BRANCHES[config_name] = {}
    branch_config = branch_configs[build_configs[config_name]['branch_config']]
    if branch_config['branch_name'] != '':
        BRANCHES[config_name]['branch_name'] = branch_config['branch_name']
    key_copy(build_configs[config_name], BRANCHES[config_name], [ 'branch_config', 'leak_threshold', 'env' ] )

    for platform in branch_config['platforms']:
        # for each platform's keys...
        key_copy(build_configs[config_name]['platforms'][platform], BRANCHES[config_name]['platforms'][platform], [] )

        if build_configs[config_name]['leak_threshold'].has_key(platform) \
           and build_configs[config_name].has_key('builder_type') and build_configs[config_name]['builder_type'] == 'bloat':
            BRANCHES[config_name]['platforms'][platform]['leak_threshold'] = build_configs[config_name]['leak_threshold'][platform]
        key_copy(platforms[platform], BRANCHES[config_name]['platforms'][platform], ['display_name','SYMBOL_SERVER_SSH_KEY'] )

        #Codesighs not supported on win32
        if build_configs[config_name].get('codesighs') == True:
            if platform == 'win32':
                BRANCHES[config_name]['platforms']['win32']['codesighs'] = False

        # set environment from various sources
        BRANCHES[config_name]['platforms'][platform]['env'] = {}
        key_copy(build_configs[config_name]['env'], BRANCHES[config_name]['platforms'][platform]['env'], [] )
        if platforms[platform].has_key('env'):
            key_copy(platforms[platform]['env'], BRANCHES[config_name]['platforms'][platform]['env'], [] )
        key_copy(build_configs[config_name]['platforms'][platform]['env'], BRANCHES[config_name]['platforms'][platform]['env'], [] )
        if config_name not in ['comm-central-trunk-bloat', 'comm-1.9.2-unittest']: #TODO
            BRANCHES[config_name]['platforms'][platform]['env']['SYMBOL_SERVER_SSH_KEY'] = platforms[platform]['SYMBOL_SERVER_SSH_KEY']

#TODO - make changes to avoid these last minute cleanups

for branch in ['comm-1.9.2-bloat', 'comm-1.9.2']:
    del BRANCHES[branch]['platforms']['linux64']

# 32-64 universal switch for mac
for branch in ['comm-central-trunk-bloat']:
    del BRANCHES[branch]['platforms']['macosx64']
for branch in ['comm-central-trunk']:
    del BRANCHES[branch]['platforms']['macosx']

for branch in ['comm-1.9.2', 'comm-central-trunk']:
    del BRANCHES[branch]['builder_type']
for branch in ['comm-1.9.2-unittest']:
    for platform in ['linux', 'linux64', 'macosx', 'win32']:
        for key in ['env', 'platform_objdir', 'update_platform']:
            if BRANCHES[branch]['platforms'][platform].has_key(key):
                del BRANCHES[branch]['platforms'][platform][key]

for branch in sorted(build_configs.keys()):
    for platform in ('linux','linux64','macosx', 'macosx64'):
        if BRANCHES[branch]['platforms'].get(platform):
            # Enable ccache statistics for linuxes and mac
            BRANCHES[branch]['platforms'][platform]['enable_ccache'] = True
    for platform in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms'][platform]['builds_before_reboot'] = 1

for branch in ['comm-central-trunk']:
  for platform in ['linux','linux64']:
    BRANCHES[branch]['platforms']['linux']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/lib'
    BRANCHES[branch]['platforms']['linux64']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/lib64'

# ----------------

HGURL = 'http://hg.mozilla.org/'
HGHOST = 'hg.mozilla.org'
CONFIG_REPO_URL = 'http://hg.mozilla.org/build/buildbot-configs'
CONFIG_REPO_PATH = 'build/buildbot-configs'
COMPARE_LOCALES_REPO_PATH = 'build/compare-locales'
CONFIG_SUBDIR = 'thunderbird'
OBJDIR = 'objdir-tb'
STAGE_USERNAME = 'tbirdbld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_GROUP = 'thunderbird'
STAGE_SSH_KEY = 'tbirdbld_dsa'

AUS2_USER = 'tbirdbld'
AUS2_SSH_KEY = 'tbirdbld_dsa'
AUS2_HOST = 'momo-build-adm-01.sj.mozillamessaging.com'

DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/thunderbird'
PRODUCT = 'mail'
MOZ_APP_NAME = 'thunderbird'


DEFAULTS = {
    'factory':                'build',
    'hgurl':                  HGURL,
    'branch_name':            'comm-central',
    'stage_base_path':        '/home/ftp/pub/mozilla.org/thunderbird',
    'mozilla_central_branch': 'releases/mozilla-1.9.1',
    'add_poll_branches':      [ 'dom-inspector','users/gozer_mozillamessaging.com/test' ],
    'period':                 60 * 60 * 8,
    'nightly_hour':          [3],
    'nightly_minute':        [0],
    'clobber_url':            "http://build.mozillamessaging.com/clobberer/",
    'builder_type':           "build",
    'tinderbox_tree':         "ThunderbirdTest",
    'codesighs':               False,
    'mozmill':                 False,
    'product_name':           'Thunderbird',
    'brand_name':             'Shredder',
    'app_name':			'thunderbird',
    'build_space':             10,
    'l10n_nightly_updates':    False,

    'create_partial':          False,
    'create_snippet':          False,

    'stage_username':		STAGE_USERNAME,
    'stage_server':		STAGE_SERVER,
    'stage_group':		STAGE_GROUP,
    'stage_ssh_key':		STAGE_SSH_KEY,
    'enable_checktests':        False,
    'exec_xpcshell_suites':     True,

    'graph_server':		'graphs.mozilla.org',
    'graph_selector':           '/server/collect.cgi',

    # Unit Test
    'client_py_args':       ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--hg-options=--verbose --time'],

    'build_tools_repo': "build/tools",
    'hg_rev_shortnames': {
      'mozilla-central':        'moz',
      'comm-central':           'cc',
      'dom-inspector':          'domi',
      'releases/mozilla-1.9.1': 'moz191',
      'releases/mozilla-1.9.2': 'moz192',
    }
}


# Release automation expect to find these
STAGE_BASE_PATH=DEFAULTS['stage_base_path']
COMPARE_LOCALES_TAG = 'RELEASE_AUTOMATION'

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
