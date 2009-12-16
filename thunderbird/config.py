HGURL = 'http://hg.mozilla.org/'
HGHOST = 'hg.mozilla.org'
CONFIG_REPO_URL = 'http://hg.mozilla.org/build/buildbot-configs'
CONFIG_REPO_PATH = 'build/buildbot-configs'
COMPARE_LOCALES_REPO_PATH = 'build/compare-locales'
CONFIG_SUBDIR = 'thunderbird'
LOCALE_REPO_URL = 'http://hg.mozilla.org/releases/l10n-mozilla-1.9.1/%(locale)s'
OBJDIR = 'objdir-tb'
STAGE_USERNAME = 'tbirdbld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_GROUP = 'thunderbird'
STAGE_SSH_KEY = 'tbirdbld_dsa'
AUS2_USER = 'tbirdbld'
AUS2_HOST = 'aus2-staging.mozilla.org'
DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/thunderbird'
PRODUCT = 'mail'
MOZ_APP_NAME = 'thunderbird'

BUILDERS = {
    'linux': {
        'momo': [ 'momo-vm-%02i' % x for x in [2,7,12]],
    },
    'macosx': {
        '10.5': {
            'momo': [ 'momo-vm-osx-leopard-%02i' % x for x in [2,3,4,5] ],
        },
    },
    'win32': {
        'momo': [ 'momo-vm-%02i' % x for x in [4,6,13,15,16] ] + [ 'momo-vm-win2k3-%02i' % x for x in [ 1,4,5 ] ],
    },
}

DEFAULTS = {
    'factory':                'build',
    'hgurl':                  HGURL,
    'branch_name':            'comm-central',
    'stage_base_path':        '/home/ftp/pub/mozilla.org/thunderbird',
    'mozilla_central_branch': 'releases/mozilla-1.9.1',
    'add_poll_branches':      [ 'dom-inspector' ],
    'period':                 60 * 60 * 8,
    'irc':                    True,
    'clobber_url':            "http://build.mozillamessaging.com/clobberer/",
    'builder_type':           "build",
    'tinderbox_tree':         "ThunderbirdTest",
    'codesighs':               False,
    'product_name':           'Thunderbird',
    'brand_name':             'Shredder',
    'l10n_nightly_updates':    False,
    
    # Unit Test
    'client_py_args':       ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--hg-options=--verbose --time'],

    'clobber_url':  "http://build.mozillamessaging.com/clobberer/",
    'build_tools_repo': "build/tools",
    'hg_rev_shortnames': {
      'mozilla-central':        'm-c',
      'comm-central':           'rev',
      'dom-inspector':          'domi',
      'releases/mozilla-1.9.1': 'moz',
      'releases/comm-1.9.1':    'rev',
    }
}

# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-central': {},
    'comm-central-trunk': {},
    'comm-central-bloat': {},
    'comm-central-trunk-bloat': {},
    'comm-1.9.1-lightning': {},
    'comm-central-lightning' {},
    'comm-1.9.1-sunbird': {},
    'comm-1.9.1-unittest': {},
    'comm-1.9.2-unittest': {},
    'comm-central-unittest': {},
}

# thunderbird-unittest

BRANCHES['comm-1.9.1-unittest'] = {
    #Follow the 3.0rc1 release branch until we release 3.0
    'client_py_args' :  DEFAULTS['client_py_args'] + ['--mozilla-rev=COMM1915_20091112_RELBRANCH']
    'factory': 'CCUnittestBuildFactory',
    'builder_type': 'check',
    'nightly': False,
    'hg_branch': 'releases/comm-1.9.1',
    'branch_name': 'comm-1.9.1',
    'tinderbox_tree': 'Thunderbird3.0',
    'irc_nick': 'thunderbot',
    'irc_channels': ['maildev'],
    'platforms': {
        'linux': {
            'base_name': 'Linux comm-1.9.1',
            'slaves': BUILDERS['linux']['momo'],
        },
        'win32': {
            'base_name': 'WINNT 5.2 comm-1.9.1',
            'slaves': BUILDERS['win32']['momo'],
        },
       'macosx': {
            'base_name': 'MacOSX 10.5 comm-1.9.1',
            'slaves': BUILDERS['macosx']['10.5']['momo'],
        },
    }
}

BRANCHES['comm-1.9.2-unittest'] = {
    'factory': 'CCUnittestBuildFactory',
    'builder_type': 'check',
    'hg_branch': 'comm-central',
    'branch_name': 'comm-1.9.2',
    'mozilla_central_branch': 'releases/mozilla-1.9.2'
    'nightly': False,
    'tinderbox_tree': 'Thunderbird3.1',
    'client_py_args': DEFAULTS['client_py_args'] + ['--mozilla-repo=http://hg.mozilla.org/releases/mozilla-1.9.2'],
    'platforms': {
        'linux': {
            'base_name': 'Linux comm-1.9.2',
            'slaves': BUILDERS['linux']['momo'],
        },
        'win32': {
            'base_name': 'WINNT 5.2 comm-1.9.2',
            'slaves': BUILDERS['win32']['momo'],
        },
       'macosx': {
            'base_name': 'MacOSX 10.5 comm-1.9.2',
            'slaves': BUILDERS['macosx']['10.5']['momo'],
        },
    },
}
BRANCHES['comm-central-unittest'] = {
    'factory': 'CCUnittestBuildFactory',
    'builder_type': 'check',
    'hg_branch': 'comm-central',
    'mozilla_central_branch': 'mozilla-central',
    'nightly': False,
    'tinderbox_tree': 'Thunderbird',
    'irc_nick': 'thunderbot-trunk',
    'irc_channels': ['maildev'],
    'client_py_args': DEFAULTS['client_py_args'] + ['--mozilla-repo=http://hg.mozilla.org/mozilla-central'],
    'platforms': {
        'linux': {
            'base_name': 'Linux comm-central',
            'slaves': BUILDERS['linux']['momo'],
        },
        'win32': {
            'base_name': 'WINNT 5.2 comm-central',
            'slaves': BUILDERS['win32']['momo'],
        },
       'macosx': {
            'base_name': 'MacOSX 10.5 comm-central',
            'slaves': BUILDERS['macosx']['10.5']['momo'],
        },

    },
}

######## thunderbird-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
    'macosx-shark': {},
}
BRANCHES['comm-central']['mozilla_central_branch'] = 'releases/mozilla-1.9.1'
#Follow the 3.0rc1 release branch until we release 3.0
BRANCHES['comm-central']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--hg-options=--verbose --time'] + ['--mozilla-rev=COMM1915_20091112_RELBRANCH']
BRANCHES['comm-central']['cvsroot'] = ':pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot'
BRANCHES['comm-central']['mozconfig'] = 'nightly/mozconfig'
BRANCHES['comm-central']['package'] = True
BRANCHES['comm-central']['branch_name'] = 'comm-1.9.1'
BRANCHES['comm-central']['hg_branch'] = 'releases/comm-1.9.1'
#Disable when producing release builds
#BRANCHES['comm-central']['nightly'] = False
BRANCHES['comm-central']['upload_stage'] = True
BRANCHES['comm-central']['milestone'] = 'comm-1.9.1'
BRANCHES['comm-central']['codesighs'] = True
BRANCHES['comm-central']['l10n'] = True
BRANCHES['comm-central']['l10n_repo'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['comm-central']['l10n_tree'] = 'tb30x'
BRANCHES['comm-central']['platforms']['macosx-shark']['l10n'] = False
BRANCHES['comm-central']['irc_nick'] = 'thunderbuild'
BRANCHES['comm-central']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1'
BRANCHES['comm-central']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-1.9.1'
BRANCHES['comm-central']['platforms']['macosx']['base_name'] = 'MacOSX 10.5 comm-1.9.1'
BRANCHES['comm-central']['platforms']['macosx-shark']['base_name'] = 'MacOSX 10.5 comm-1.9.1 shark'
BRANCHES['comm-central']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['macosx-shark']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central']['create_snippet'] = True
BRANCHES['comm-central']['platforms']['macosx-shark']['create_snippet'] = False
BRANCHES['comm-central']['aus'] = {
    'user': 'tbirdbld',
    'host': 'aus-staging.sj.mozillamessaging.com',
    'base_upload_dir': '/opt/aus/build/0/Thunderbird/comm-1.9.1',
}
BRANCHES['comm-central']['l10n_nightly_updates'] = True
BRANCHES['comm-central']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['comm-central']['platforms']['macosx-shark']['update_platform'] = 'Darwin_Universal-gcc3-shark'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['macosx-shark']['upload_symbols'] = False
BRANCHES['comm-central']['tinderbox_tree'] = 'Thunderbird3.0'
BRANCHES['comm-central']['platforms']['linux']['slaves'] = BUILDERS['linux']['momo']
BRANCHES['comm-central']['platforms']['win32']['slaves'] = BUILDERS['win32']['momo']
BRANCHES['comm-central']['platforms']['macosx']['slaves'] = BUILDERS['macosx']['10.5']['momo']
BRANCHES['comm-central']['platforms']['macosx-shark']['slaves'] = BUILDERS['macosx']['10.5']['momo']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central']['platforms']['macosx-shark']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['macosx-shark']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## thunderbird-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-trunk']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
}
BRANCHES['comm-central-trunk']['mozilla_central_branch'] = 'mozilla-central'
BRANCHES['comm-central-trunk']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--mozilla-repo=http://hg.mozilla.org/mozilla-central','--hg-options=--verbose --time']
BRANCHES['comm-central-trunk']['cvsroot'] = ':pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot'
BRANCHES['comm-central-trunk']['mozconfig'] = 'nightly/mozconfig'
BRANCHES['comm-central-trunk']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-trunk']['package'] = True
#Disable when producing release builds
#BRANCHES['comm-central-trunk']['nightly'] = False
BRANCHES['comm-central-trunk']['upload_stage'] = True
BRANCHES['comm-central-trunk']['milestone'] = 'comm-central-trunk'
BRANCHES['comm-central-trunk']['codesighs'] = True
BRANCHES['comm-central-trunk']['l10n'] = True
BRANCHES['comm-central-trunk']['l10n_repo'] = 'l10n-central'
BRANCHES['comm-central-trunk']['l10n_tree'] = 'tb31x'
BRANCHES['comm-central-trunk']['irc_nick'] = 'thunderbuild-trunk'
BRANCHES['comm-central-trunk']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central-trunk']['platforms']['linux']['base_name'] = 'Linux comm-central'
BRANCHES['comm-central-trunk']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-central'
BRANCHES['comm-central-trunk']['platforms']['macosx']['base_name'] = 'MacOSX 10.5 comm-central'
BRANCHES['comm-central-trunk']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['macosx']['profiled_build'] = False

# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-trunk']['create_snippet'] = True
BRANCHES['comm-central-trunk']['aus'] = {
    'user': 'tbirdbld',
    'host': 'aus-staging.sj.mozillamessaging.com',
    'base_upload_dir': '/opt/aus/build/0/Thunderbird/comm-central',
}
BRANCHES['comm-central-trunk']['l10n_nightly_updates'] = True
BRANCHES['comm-central-trunk']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-trunk']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-trunk']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-trunk']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['tinderbox_tree'] = 'Thunderbird'
BRANCHES['comm-central-trunk']['platforms']['linux']['slaves'] = BUILDERS['linux']['momo']
BRANCHES['comm-central-trunk']['platforms']['win32']['slaves'] = BUILDERS['win32']['momo']
BRANCHES['comm-central-trunk']['platforms']['macosx']['slaves'] = BUILDERS['macosx']['10.5']['momo']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-trunk']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-trunk']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## lightning-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-1.9.1-lightning']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}

BRANCHES['comm-1.9.1-lightning']['mozilla_central_branch'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-1.9.1-lightning']['branch_name'] = 'comm-1.9.1'
BRANCHES['comm-1.9.1-lightning']['hg_branch'] = 'releases/comm-1.9.1'
BRANCHES['comm-1.9.1-lightning']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-1.9.1-lightning']['cvsroot'] = ':ext:calbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-1.9.1-lightning']['mozconfig'] = 'mozconfig-calendar'
BRANCHES['comm-1.9.1-lightning']['period'] = 60 * 60 * 6
BRANCHES['comm-1.9.1-lightning']['package'] = True
BRANCHES['comm-1.9.1-lightning']['upload_stage'] = True
BRANCHES['comm-1.9.1-lightning']['upload_complete_mar'] = False
#Might be better off per-platform instead of per-branch here.
BRANCHES['comm-1.9.1-lightning']['upload_glob'] = "mozilla/dist/xpi-stage/{lightning,gdata-provider}.xpi"
BRANCHES['comm-1.9.1-lightning']['stage_username'] = 'calbld'
BRANCHES['comm-1.9.1-lightning']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/lightning'
BRANCHES['comm-1.9.1-lightning']['stage_group'] = 'calendar'
BRANCHES['comm-1.9.1-lightning']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-1.9.1-lightning']['codesighs'] = False
BRANCHES['comm-1.9.1-lightning']['l10n'] = False
BRANCHES['comm-1.9.1-lightning']['irc_nick'] = 'calbuild'
BRANCHES['comm-1.9.1-lightning']['irc_channels'] = [ 'maildev', 'calendar' ]
BRANCHES['comm-1.9.1-lightning']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1 lightning'
BRANCHES['comm-1.9.1-lightning']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-1.9.1 lightning'
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['base_name'] = 'MacOSX 10.5 comm-1.9.1 lightning'
BRANCHES['comm-1.9.1-lightning']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-1.9.1-lightning']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-1.9.1-lightning']['platforms']['linux']['milestone'] = "comm-1.9.1/linux-xpi"
BRANCHES['comm-1.9.1-lightning']['platforms']['win32']['milestone'] = "comm-1.9.1/win32-xpi"
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['milestone'] = "comm-1.9.1/macosx-xpi"
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['upload_glob'] = "mozilla/dist/universal/xpi-stage/{lightning,gdata-provider}.xpi"

# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-1.9.1-lightning']['create_snippet'] = False
BRANCHES['comm-1.9.1-lightning']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-1.9.1-lightning']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-1.9.1-lightning']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-1.9.1-lightning']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-1.9.1-lightning']['tinderbox_tree'] = 'Calendar1.0'
BRANCHES['comm-1.9.1-lightning']['platforms']['linux']['slaves'] = [
    'cb-sb-linux-tbox',
]
BRANCHES['comm-1.9.1-lightning']['platforms']['win32']['slaves'] = [
    'cb-sb-win32-tbox',
]
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['slaves'] = [
    'cb-xserve03',
]

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-1.9.1-lightning']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.1-lightning']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-1.9.1-lightning']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1-lightning']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1-lightning']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## lightning-trunk
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-lightning']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}

BRANCHES['comm-central-lightning']['mozilla_central_branch'] = 'mozilla-central'
BRANCHES['comm-central-lightning']['branch_name'] = 'comm-central'
BRANCHES['comm-central-lightning']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-lightning']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-central-lightning']['cvsroot'] = ':ext:calbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-central-lightning']['mozconfig'] = 'mozconfig-calendar'
BRANCHES['comm-central-lightning']['period'] = 60 * 60 * 6
BRANCHES['comm-central-lightning']['package'] = True
BRANCHES['comm-central-lightning']['upload_stage'] = True
BRANCHES['comm-central-lightning']['upload_complete_mar'] = False
#Might be better off per-platform instead of per-branch here.
BRANCHES['comm-central-lightning']['upload_glob'] = "mozilla/dist/xpi-stage/{lightning,gdata-provider}.xpi"
BRANCHES['comm-central-lightning']['stage_username'] = 'calbld'
BRANCHES['comm-central-lightning']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/lightning'
BRANCHES['comm-central-lightning']['stage_group'] = 'calendar'
BRANCHES['comm-central-lightning']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-central-lightning']['codesighs'] = False
BRANCHES['comm-central-lightning']['l10n'] = False
BRANCHES['comm-central-lightning']['irc_nick'] = 'lt-trunk-builds'
BRANCHES['comm-central-lightning']['irc_channels'] = [ 'calendar' ]
BRANCHES['comm-central-lightning']['platforms']['linux']['base_name'] = 'Linux comm-central lightning'
BRANCHES['comm-central-lightning']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-central lightning'
BRANCHES['comm-central-lightning']['platforms']['macosx']['base_name'] = 'MacOSX 10.5 comm-central lightning'
BRANCHES['comm-central-lightning']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-lightning']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-lightning']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central-lightning']['platforms']['linux']['milestone'] = "comm-central/linux-xpi"
BRANCHES['comm-central-lightning']['platforms']['win32']['milestone'] = "comm-central/win32-xpi"
BRANCHES['comm-central-lightning']['platforms']['macosx']['milestone'] = "comm-central/macosx-xpi"
BRANCHES['comm-central-lightning']['platforms']['macosx']['upload_glob'] = "mozilla/dist/universal/xpi-stage/{lightning,gdata-provider}.xpi"

# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-lightning']['create_snippet'] = False
BRANCHES['comm-central-lightning']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-lightning']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-lightning']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-lightning']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-lightning']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-lightning']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-lightning']['tinderbox_tree'] = 'Sunbird'
BRANCHES['comm-central-lightning']['platforms']['linux']['slaves'] = [
    'cb-sb-linux-tbox',
]
BRANCHES['comm-central-lightning']['platforms']['win32']['slaves'] = [
    'cb-sb-win32-tbox',
]
BRANCHES['comm-central-lightning']['platforms']['macosx']['slaves'] = [
    'cb-xserve03',
]

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-lightning']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-lightning']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-lightning']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-lightning']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-lightning']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-lightning']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## sunbird-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-1.9.1-sunbird']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}
BRANCHES['comm-1.9.1-sunbird']['mozilla_central_branch'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-1.9.1-sunbird']['branch_name'] = 'comm-1.9.1'
BRANCHES['comm-1.9.1-sunbird']['hg_branch'] = 'releases/comm-1.9.1'
BRANCHES['comm-1.9.1-sunbird']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-1.9.1-sunbird']['cvsroot'] = ':ext:calbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-1.9.1-sunbird']['mozconfig'] = 'mozconfig-sunbird'
BRANCHES['comm-1.9.1-sunbird']['period'] = 60 * 60 * 6
BRANCHES['comm-1.9.1-sunbird']['package'] = True
BRANCHES['comm-1.9.1-sunbird']['upload_stage'] = True
BRANCHES['comm-1.9.1-sunbird']['milestone'] = 'comm-1.9.1'
BRANCHES['comm-1.9.1-sunbird']['stage_username'] = 'calbld'
BRANCHES['comm-1.9.1-sunbird']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/sunbird'
BRANCHES['comm-1.9.1-sunbird']['stage_project'] = 'calendar/sunbird'
BRANCHES['comm-1.9.1-sunbird']['stage_group'] = 'calendar'
BRANCHES['comm-1.9.1-sunbird']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-1.9.1-sunbird']['codesighs'] = False
BRANCHES['comm-1.9.1-sunbird']['l10n'] = True
BRANCHES['comm-1.9.1-sunbird']['l10n_repo'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['comm-1.9.1-sunbird']['l10n_tree'] = 'sunbird10x'
BRANCHES['comm-1.9.1-sunbird']['product'] = 'calendar'
BRANCHES['comm-1.9.1-sunbird']['appname'] = 'sunbird'
BRANCHES['comm-1.9.1-sunbird']['brand_name'] = 'Sunbird'
BRANCHES['comm-1.9.1-sunbird']['product_name'] = 'Sunbird'
BRANCHES['comm-1.9.1-sunbird']['irc_nick'] = 'sunbuild'
BRANCHES['comm-1.9.1-sunbird']['irc_channels'] = [ 'maildev','calendar' ]
BRANCHES['comm-1.9.1-sunbird']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1 sunbird'
BRANCHES['comm-1.9.1-sunbird']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-1.9.1 sunbird'
BRANCHES['comm-1.9.1-sunbird']['platforms']['macosx']['base_name'] = 'MacOSX 10.5 comm-1.9.1 sunbird'
BRANCHES['comm-1.9.1-sunbird']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-1.9.1-sunbird']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-1.9.1-sunbird']['platforms']['macosx']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-1.9.1-sunbird']['create_snippet'] = True
BRANCHES['comm-1.9.1-sunbird']['aus'] = {
    'user': 'calbld',
    'host': 'aus2-community.mozilla.org',
    'base_upload_dir': '/opt/aus2/build/0/Sunbird/trunk',
}
BRANCHES['comm-1.9.1-sunbird']['download_base_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/calendar/sunbird'
BRANCHES['comm-1.9.1-sunbird']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-1.9.1-sunbird']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-1.9.1-sunbird']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-1.9.1-sunbird']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-1.9.1-sunbird']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-1.9.1-sunbird']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-1.9.1-sunbird']['tinderbox_tree'] = 'Calendar1.0'
BRANCHES['comm-1.9.1-sunbird']['platforms']['linux']['slaves'] = [
    'cb-sb-linux-tbox',
]
BRANCHES['comm-1.9.1-sunbird']['platforms']['win32']['slaves'] = [
    'cb-sb-win32-tbox',
]
BRANCHES['comm-1.9.1-sunbird']['platforms']['macosx']['slaves'] = [
    'cb-xserve03',
]

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-1.9.1-sunbird']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.1-sunbird']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-1.9.1-sunbird']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-1.9.1-sunbird']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1-sunbird']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-1.9.1-sunbird']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}


######## thunderbird-bloat
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-bloat']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
}

BRANCHES['comm-central-bloat']['mozilla_central_branch'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-central-bloat']['branch_name'] = 'comm-1.9.1'
BRANCHES['comm-central-bloat']['hg_branch'] = 'releases/comm-1.9.1'
#Follow the 3.0rc1 release branch until we release 3.0
BRANCHES['comm-central-bloat']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--hg-options=--verbose --time'] + ['--mozilla-rev=COMM1915_20091112_RELBRANCH']
BRANCHES['comm-central-bloat']['cvsroot'] = ':pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot' 
BRANCHES['comm-central-bloat']['mozconfig'] = 'debug/mozconfig'
BRANCHES['comm-central-bloat']['nightly'] = False
BRANCHES['comm-central-bloat']['leak'] = True
BRANCHES['comm-central-bloat']['package'] = False
BRANCHES['comm-central-bloat']['upload_stage'] = False
BRANCHES['comm-central-bloat']['codesighs'] = False
BRANCHES['comm-central-bloat']['l10n'] = False
BRANCHES['comm-central-bloat']['irc_nick'] = 'thunderbloat'
BRANCHES['comm-central-bloat']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central-bloat']['builder_type'] = 'bloat'
BRANCHES['comm-central-bloat']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1'
BRANCHES['comm-central-bloat']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-1.9.1'
BRANCHES['comm-central-bloat']['platforms']['macosx']['base_name'] = 'MacOSX 10.5 comm-1.9.1'
BRANCHES['comm-central-bloat']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-bloat']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-bloat']['platforms']['macosx']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-bloat']['create_snippet'] = False
BRANCHES['comm-central-bloat']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-bloat']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-bloat']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-bloat']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['tinderbox_tree'] = 'Thunderbird3.0'
BRANCHES['comm-central-bloat']['platforms']['linux']['leak_threshold'] = 970000
BRANCHES['comm-central-bloat']['platforms']['macosx']['leak_threshold'] = 2500000
BRANCHES['comm-central-bloat']['platforms']['win32']['leak_threshold'] =  110000
BRANCHES['comm-central-bloat']['platforms']['linux']['slaves'] = BUILDERS['linux']['momo']
BRANCHES['comm-central-bloat']['platforms']['win32']['slaves'] = BUILDERS['win32']['momo']
BRANCHES['comm-central-bloat']['platforms']['macosx']['slaves'] = BUILDERS['macosx']['10.5']['momo']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-bloat']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['macosx']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'XPCOM_DEBUG_BREAK': 'stack',
    'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
}
BRANCHES['comm-central-bloat']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'XPCOM_DEBUG_BREAK': 'stack',
}
BRANCHES['comm-central-bloat']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'XPCOM_DEBUG_BREAK': 'stack',
}

######## thunderbird-bloat (mozilla-central)
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-trunk-bloat']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
}

BRANCHES['comm-central-trunk-bloat']['mozilla_central_branch'] = 'mozilla-central'
BRANCHES['comm-central-trunk-bloat']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--mozilla-repo=http://hg.mozilla.org/mozilla-central', '--hg-options=--verbose --time']
BRANCHES['comm-central-trunk-bloat']['cvsroot'] = ':pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot'
BRANCHES['comm-central-trunk-bloat']['mozconfig'] = 'debug/mozconfig'
BRANCHES['comm-central-trunk-bloat']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-trunk-bloat']['builder_type'] = 'bloat'
BRANCHES['comm-central-trunk-bloat']['nightly'] = False
BRANCHES['comm-central-trunk-bloat']['leak'] = True
BRANCHES['comm-central-trunk-bloat']['package'] = False
BRANCHES['comm-central-trunk-bloat']['upload_stage'] = False
BRANCHES['comm-central-trunk-bloat']['codesighs'] = False
BRANCHES['comm-central-trunk-bloat']['l10n'] = False
BRANCHES['comm-central-trunk-bloat']['irc_nick'] = 'thunderbloat-trunk'
BRANCHES['comm-central-trunk-bloat']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['base_name'] = 'Linux comm-central'
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-central'
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['base_name'] = 'MacOSX 10.5 comm-central'
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-trunk-bloat']['create_snippet'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-trunk-bloat']['tinderbox_tree'] = 'Thunderbird'
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['leak_threshold'] = 970000
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['leak_threshold'] = 2300000
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['leak_threshold'] =  110000
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['slaves'] = BUILDERS['linux']['momo']
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['slaves'] = BUILDERS['win32']['momo']
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['slaves'] = BUILDERS['macosx']['10.5']['momo']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
    'XPCOM_DEBUG_BREAK': 'stack',
}
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'XPCOM_DEBUG_BREAK': 'stack',
}
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'XPCOM_DEBUG_BREAK': 'stack',
}

# Release automation expect to find these
STAGE_BASE_PATH=DEFAULTS['stage_base_path']
COMPARE_LOCALES_TAG = 'RELEASE_AUTOMATION'
