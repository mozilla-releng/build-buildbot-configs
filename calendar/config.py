HGURL = 'http://hg.mozilla.org/'
HGHOST = 'hg.mozilla.org'
CONFIG_REPO_URL = 'http://hg.mozilla.org/build/buildbot-configs'
CONFIG_REPO_PATH = 'build/buildbot-configs'
COMPARE_LOCALES_REPO_PATH = 'build/compare-locales'
CONFIG_SUBDIR = 'calendar'
LOCALE_REPO_URL = 'http://hg.mozilla.org/releases/l10n/mozilla-aurora/%(locale)s'
OBJDIR = 'objdir-tb'
STAGE_USERNAME = 'calbld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_GROUP = 'calendar'
STAGE_SSH_KEY = 'calbld_dsa'
AUS2_USER = 'calbld'
AUS2_HOST = 'aus-staging.sj.mozillamessaging.com'
DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/calendar/'
PRODUCT = 'calendar'
MOZ_APP_NAME = 'calendar'
SYMBOL_SERVER_HOST = 'dm-symbolpush01.mozilla.org'
SYMBOL_SERVER_USER = 'calbld'
SYMBOL_SERVER_PATH = '/mnt/netapp/breakpad/symbols_sbrd/'
SYMBOL_SERVER_POST_UPLOAD_CMD = '/usr/local/bin/post-symbol-upload.py'

ORGANIZATION = 'community'

BUILDERS = {
    'linux': {
        'community': [ 'momo-vm-cal-linux-01' ],
    },
    'linux64': {
        'momo': ['momo-vm-cal-linux64-01'],
    },
    'macosx': {
#        '10.5': {
#            'community': [ 'cb-xserve03' ],
#        },
        '10.6': {
            'momo':      [ 'mini64-cal-01' ],
        }
    },
    'win32': {
        'community': [ 'cb-sb-win32-tbox' ],
    },
}

DEFAULTS = {
    'factory':                'build',
    'hgurl':                  HGURL,
    'branch_name':            'comm-central',
    'stage_base_path':        '/home/ftp/pub/mozilla.org/calendar',
    'mozilla_central_branch': 'releases/mozilla-1.9.1',
    'l10n_repo':              'releases/l10n/mozilla-aurora',
    'add_poll_branches':      [ ],
    'period':                 60 * 60 * 8,
    'nightly_hour':           [3],
    'nightly_minute':         [0],
    'irc':                    True,
    'clobber_url':            "http://build.mozillamessaging.com/clobberer/",
    'builder_type':           "build",
    'tinderbox_tree':         "ThunderbirdTest",
    'codesighs':              False,
    'mozmill':                False,
    'product_name':           'sunbird',
    'brand_name':             'Sunbird',
    'app_name':               'calendar',
    'build_space':            8,
    'l10n_nightly_updates':   False,
 
    'stage_username':         STAGE_USERNAME,
    'stage_server':           STAGE_SERVER,
    'stage_group':            STAGE_GROUP,
    'stage_ssh_key':          STAGE_SSH_KEY,
    
    # Unit Test
    'client_py_args':       ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--hg-options=--verbose --time'],

    'clobber_url':  "http://build.mozillamessaging.com/clobberer/",
    'build_tools_repo': "build/tools",
    'hg_rev_shortnames': {
      'mozilla-central':        'moz',
      'comm-central':           'cc',
      'dom-inspector':          'domi',
      'releases/mozilla-1.9.1': 'moz191',
      'releases/mozilla-1.9.2': 'moz192',
      'releases/mozilla-aurora':   'mozaurora',
      'releases/comm-1.9.1':    'cc191',
    }
}

# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-release': {},
    'comm-beta': {},
    'comm-aurora': {},
    'comm-central': {},
}

######## lightning-release
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-release']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx64': {},
}

BRANCHES['comm-release']['mozilla_central_branch'] = 'releases/mozilla-release'
BRANCHES['comm-release']['download_base_url'] = DOWNLOAD_BASE_URL + 'sunbird'
BRANCHES['comm-release']['branch_name'] = 'comm-release'
BRANCHES['comm-release']['hg_branch'] = 'releases/comm-release'
BRANCHES['comm-release']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman'] + ['--mozilla-repo=http://hg.mozilla.org/releases/mozilla-release']
BRANCHES['comm-release']['mozconfig'] = 'mozconfig-lightning'
BRANCHES['comm-release']['period'] = 60 * 60 * 10
BRANCHES['comm-release']['nightly_hour'] = [0]
BRANCHES['comm-release']['nightly'] = False
# Lightning doesn't need to package Thunderbird
BRANCHES['comm-release']['package'] = False
BRANCHES['comm-release']['upload_stage'] = True
BRANCHES['comm-release']['upload_complete_mar'] = False
#Might be better off per-platform instead of per-branch here.
BRANCHES['comm-release']['upload_glob'] = "mozilla/dist/xpi-stage/{lightning,gdata-provider}.xpi"
BRANCHES['comm-release']['stage_username'] = 'calbld'
BRANCHES['comm-release']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/lightning'
BRANCHES['comm-release']['stage_group'] = 'calendar'
BRANCHES['comm-release']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-release']['codesighs'] = False
BRANCHES['comm-release']['l10n'] = False
BRANCHES['comm-release']['l10n_tree'] = 'calendar10x'
BRANCHES['comm-release']['l10n_repo'] = 'releases/l10n/mozilla-release'
BRANCHES['comm-release']['irc_nick'] = 'calbuild'
BRANCHES['comm-release']['irc_channels'] = [ 'maildev', 'calendar' ]
BRANCHES['comm-release']['extensions'] = {
    'lightning': {
        'subdir': "calendar/lightning",
        'download_base_url': DOWNLOAD_BASE_URL + 'lightning',
        'l10n': True
    }
}

BRANCHES['comm-release']['platforms']['linux']['base_name'] = 'Linux comm-release lightning'
BRANCHES['comm-release']['platforms']['linux64']['base_name'] = 'Linux x86_64 comm-release lightning'
BRANCHES['comm-release']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-release lightning'
BRANCHES['comm-release']['platforms']['macosx64']['base_name'] = 'MacOSX 10.6 comm-release lightning'
BRANCHES['comm-release']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-release']['platforms']['linux64']['profiled_build'] = False
BRANCHES['comm-release']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-release']['platforms']['macosx64']['profiled_build'] = False
BRANCHES['comm-release']['platforms']['linux']['milestone'] = "comm-release/linux-xpi"
BRANCHES['comm-release']['platforms']['linux64']['milestone'] = "comm-release/linux64-xpi"
BRANCHES['comm-release']['platforms']['win32']['milestone'] = "comm-release/win32-xpi"
BRANCHES['comm-release']['platforms']['macosx64']['milestone'] = "comm-release/macosx-xpi"
BRANCHES['comm-release']['platforms']['macosx64']['upload_glob'] = "mozilla/dist/universal/xpi-stage/{lightning,gdata-provider}.xpi"
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-release']['create_snippet'] = False
BRANCHES['comm-release']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-release']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-release']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['comm-release']['platforms']['macosx64']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-release']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-release']['platforms']['linux64']['upload_symbols'] = True
BRANCHES['comm-release']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-release']['platforms']['macosx64']['upload_symbols'] = True
BRANCHES['comm-release']['tinderbox_tree'] = 'Calendar-Release'
BRANCHES['comm-release']['platforms']['linux']['slaves'] = BUILDERS['linux']['community']
BRANCHES['comm-release']['platforms']['linux64']['slaves'] = BUILDERS['linux64']['momo']
BRANCHES['comm-release']['platforms']['win32']['slaves'] = BUILDERS['win32']['community']
BRANCHES['comm-release']['platforms']['macosx64']['slaves'] = BUILDERS['macosx']['10.6']['momo']

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-release']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-release']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['comm-release']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-release']['platforms']['macosx64']['platform_objdir'] = '%s/i386' % OBJDIR
BRANCHES['comm-release']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/calbld_dsa',
}
BRANCHES['comm-release']['platforms']['linux64']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/calbld_dsa',
}
BRANCHES['comm-release']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/c/Documents and Settings/calbld/.ssh/calbld_dsa',
}
BRANCHES['comm-release']['platforms']['macosx64']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'DISABLE_LIGHTNING_INSTALL': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/Users/cltbld/.ssh/calbld_dsa',
}

######## lightning-beta
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-beta']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx64': {},
}

BRANCHES['comm-beta']['mozilla_central_branch'] = 'releases/mozilla-beta'
BRANCHES['comm-beta']['download_base_url'] = DOWNLOAD_BASE_URL + 'sunbird'
BRANCHES['comm-beta']['branch_name'] = 'comm-beta'
BRANCHES['comm-beta']['hg_branch'] = 'releases/comm-beta'
BRANCHES['comm-beta']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman'] + ['--mozilla-repo=http://hg.mozilla.org/releases/mozilla-beta']
BRANCHES['comm-beta']['mozconfig'] = 'mozconfig-lightning'
BRANCHES['comm-beta']['period'] = 60 * 60 * 10
BRANCHES['comm-beta']['nightly_hour'] = [0]
BRANCHES['comm-beta']['nightly'] = False
# Lightning doesn't need to package Thunderbird
BRANCHES['comm-beta']['package'] = False
BRANCHES['comm-beta']['upload_stage'] = True
BRANCHES['comm-beta']['upload_complete_mar'] = False
#Might be better off per-platform instead of per-branch here.
BRANCHES['comm-beta']['upload_glob'] = "mozilla/dist/xpi-stage/{lightning,gdata-provider}.xpi"
BRANCHES['comm-beta']['stage_username'] = 'calbld'
BRANCHES['comm-beta']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/lightning'
BRANCHES['comm-beta']['stage_group'] = 'calendar'
BRANCHES['comm-beta']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-beta']['codesighs'] = False
BRANCHES['comm-beta']['l10n'] = False
BRANCHES['comm-beta']['l10n_tree'] = 'calendar10x'
BRANCHES['comm-beta']['l10n_repo'] = 'releases/l10n/mozilla-beta'
BRANCHES['comm-beta']['irc_nick'] = 'calbuild'
BRANCHES['comm-beta']['irc_channels'] = [ 'maildev', 'calendar' ]
BRANCHES['comm-beta']['extensions'] = {
    'lightning': {
        'subdir': "calendar/lightning",
        'download_base_url': DOWNLOAD_BASE_URL + 'lightning',
        'l10n': True
    }
}

BRANCHES['comm-beta']['platforms']['linux']['base_name'] = 'Linux comm-beta lightning'
BRANCHES['comm-beta']['platforms']['linux64']['base_name'] = 'Linux x86_64 comm-beta lightning'
BRANCHES['comm-beta']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-beta lightning'
BRANCHES['comm-beta']['platforms']['macosx64']['base_name'] = 'MacOSX 10.6 comm-beta lightning'
BRANCHES['comm-beta']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-beta']['platforms']['linux64']['profiled_build'] = False
BRANCHES['comm-beta']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-beta']['platforms']['macosx64']['profiled_build'] = False
BRANCHES['comm-beta']['platforms']['linux']['milestone'] = "comm-beta/linux-xpi"
BRANCHES['comm-beta']['platforms']['linux64']['milestone'] = "comm-beta/linux64-xpi"
BRANCHES['comm-beta']['platforms']['win32']['milestone'] = "comm-beta/win32-xpi"
BRANCHES['comm-beta']['platforms']['macosx64']['milestone'] = "comm-beta/macosx-xpi"
BRANCHES['comm-beta']['platforms']['macosx64']['upload_glob'] = "mozilla/dist/universal/xpi-stage/{lightning,gdata-provider}.xpi"
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-beta']['create_snippet'] = False
BRANCHES['comm-beta']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-beta']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-beta']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['comm-beta']['platforms']['macosx64']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-beta']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-beta']['platforms']['linux64']['upload_symbols'] = True
BRANCHES['comm-beta']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-beta']['platforms']['macosx64']['upload_symbols'] = True
BRANCHES['comm-beta']['tinderbox_tree'] = 'Calendar-Beta'
BRANCHES['comm-beta']['platforms']['linux']['slaves'] = BUILDERS['linux']['community']
BRANCHES['comm-beta']['platforms']['linux64']['slaves'] = BUILDERS['linux64']['momo']
BRANCHES['comm-beta']['platforms']['win32']['slaves'] = BUILDERS['win32']['community']
BRANCHES['comm-beta']['platforms']['macosx64']['slaves'] = BUILDERS['macosx']['10.6']['momo']

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-beta']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-beta']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['comm-beta']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-beta']['platforms']['macosx64']['platform_objdir'] = '%s/i386' % OBJDIR
BRANCHES['comm-beta']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/calbld_dsa',
}
BRANCHES['comm-beta']['platforms']['linux64']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/calbld_dsa',
}
BRANCHES['comm-beta']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/c/Documents and Settings/calbld/.ssh/calbld_dsa',
}
BRANCHES['comm-beta']['platforms']['macosx64']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'DISABLE_LIGHTNING_INSTALL': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/Users/cltbld/.ssh/calbld_dsa',
}

######## lightning-aurora
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-aurora']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx64': {},
}

BRANCHES['comm-aurora']['mozilla_central_branch'] = 'releases/mozilla-aurora'
BRANCHES['comm-aurora']['download_base_url'] = DOWNLOAD_BASE_URL + 'sunbird'
BRANCHES['comm-aurora']['branch_name'] = 'comm-aurora'
BRANCHES['comm-aurora']['hg_branch'] = 'releases/comm-aurora'
BRANCHES['comm-aurora']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman'] + ['--mozilla-repo=http://hg.mozilla.org/releases/mozilla-aurora']
BRANCHES['comm-aurora']['mozconfig'] = 'mozconfig-lightning'
BRANCHES['comm-aurora']['period'] = 60 * 60 * 10
BRANCHES['comm-aurora']['nightly_hour'] = [0]
# Lightning doesn't need to package Thunderbird
BRANCHES['comm-aurora']['package'] = False
BRANCHES['comm-aurora']['upload_stage'] = True
BRANCHES['comm-aurora']['upload_complete_mar'] = False
#Might be better off per-platform instead of per-branch here.
BRANCHES['comm-aurora']['upload_glob'] = "mozilla/dist/xpi-stage/{lightning,gdata-provider}.xpi"
BRANCHES['comm-aurora']['stage_username'] = 'calbld'
BRANCHES['comm-aurora']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/lightning'
BRANCHES['comm-aurora']['stage_group'] = 'calendar'
BRANCHES['comm-aurora']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-aurora']['codesighs'] = False
BRANCHES['comm-aurora']['l10n'] = False
BRANCHES['comm-aurora']['l10n_tree'] = 'calendar10x'
BRANCHES['comm-aurora']['l10n_repo'] = 'releases/l10n/mozilla-aurora'
BRANCHES['comm-aurora']['irc_nick'] = 'calbuild'
BRANCHES['comm-aurora']['irc_channels'] = [ 'maildev', 'calendar' ]
BRANCHES['comm-aurora']['extensions'] = {
    'lightning': {
        'subdir': "calendar/lightning",
        'download_base_url': DOWNLOAD_BASE_URL + 'lightning',
        'l10n': True
    }
}

BRANCHES['comm-aurora']['platforms']['linux']['base_name'] = 'Linux comm-aurora lightning'
BRANCHES['comm-aurora']['platforms']['linux64']['base_name'] = 'Linux x86_64 comm-aurora lightning'
BRANCHES['comm-aurora']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-aurora lightning'
BRANCHES['comm-aurora']['platforms']['macosx64']['base_name'] = 'MacOSX 10.6 comm-aurora lightning'
BRANCHES['comm-aurora']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-aurora']['platforms']['linux64']['profiled_build'] = False
BRANCHES['comm-aurora']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-aurora']['platforms']['macosx64']['profiled_build'] = False
BRANCHES['comm-aurora']['platforms']['linux']['milestone'] = "comm-aurora/linux-xpi"
BRANCHES['comm-aurora']['platforms']['linux64']['milestone'] = "comm-aurora/linux64-xpi"
BRANCHES['comm-aurora']['platforms']['win32']['milestone'] = "comm-aurora/win32-xpi"
BRANCHES['comm-aurora']['platforms']['macosx64']['milestone'] = "comm-aurora/macosx-xpi"
BRANCHES['comm-aurora']['platforms']['macosx64']['upload_glob'] = "mozilla/dist/universal/xpi-stage/{lightning,gdata-provider}.xpi"
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-aurora']['create_snippet'] = False
BRANCHES['comm-aurora']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-aurora']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-aurora']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['comm-aurora']['platforms']['macosx64']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-aurora']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-aurora']['platforms']['linux64']['upload_symbols'] = True
BRANCHES['comm-aurora']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-aurora']['platforms']['macosx64']['upload_symbols'] = True
BRANCHES['comm-aurora']['tinderbox_tree'] = 'Calendar-Aurora'
BRANCHES['comm-aurora']['platforms']['linux']['slaves'] = BUILDERS['linux']['community']
BRANCHES['comm-aurora']['platforms']['linux64']['slaves'] = BUILDERS['linux64']['momo']
BRANCHES['comm-aurora']['platforms']['win32']['slaves'] = BUILDERS['win32']['community']
BRANCHES['comm-aurora']['platforms']['macosx64']['slaves'] = BUILDERS['macosx']['10.6']['momo']

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-aurora']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-aurora']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['comm-aurora']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-aurora']['platforms']['macosx64']['platform_objdir'] = '%s/i386' % OBJDIR
BRANCHES['comm-aurora']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/calbld_dsa',
}
BRANCHES['comm-aurora']['platforms']['linux64']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/calbld_dsa',
}
BRANCHES['comm-aurora']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/c/Documents and Settings/calbld/.ssh/calbld_dsa',
}
BRANCHES['comm-aurora']['platforms']['macosx64']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'DISABLE_LIGHTNING_INSTALL': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/Users/cltbld/.ssh/calbld_dsa',
}

######## lightning-trunk
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central']['platforms'] = {
    'linux': {},
    'linux64': {},
    'win32': {},
    'macosx64': {}
}

BRANCHES['comm-central']['mozilla_central_branch'] = 'mozilla-central'
BRANCHES['comm-central']['download_base_url'] = DOWNLOAD_BASE_URL + 'sunbird'
BRANCHES['comm-central']['branch_name'] = 'comm-central'
BRANCHES['comm-central']['hg_branch'] = 'comm-central'
BRANCHES['comm-central']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-central']['mozconfig'] = 'mozconfig-lightning'
# Period for comm-central disabled in master.cfg
BRANCHES['comm-central']['period'] = 60 * 60 * 10
# Lightning doesn't need to package Thunderbird
BRANCHES['comm-central']['package'] = False
BRANCHES['comm-central']['upload_stage'] = True
BRANCHES['comm-central']['upload_complete_mar'] = False
#Might be better off per-platform instead of per-branch here.
BRANCHES['comm-central']['upload_glob'] = "mozilla/dist/xpi-stage/{lightning,gdata-provider}.xpi"
BRANCHES['comm-central']['stage_username'] = 'calbld'
BRANCHES['comm-central']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/lightning'
BRANCHES['comm-central']['stage_group'] = 'calendar'
BRANCHES['comm-central']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-central']['codesighs'] = False
BRANCHES['comm-central']['l10n'] = False
BRANCHES['comm-central']['l10n_tree'] = 'calendar11x'
BRANCHES['comm-central']['l10n_repo'] = 'l10n-central'
BRANCHES['comm-central']['irc_nick'] = 'lt-trunk-builds'
BRANCHES['comm-central']['irc_channels'] = [ 'calendar' ]

BRANCHES['comm-central']['extensions'] = {
    'lightning': {
        'subdir': "calendar/lightning",
        'download_base_url': DOWNLOAD_BASE_URL + 'lightning',
        'l10n': True
    }
}
BRANCHES['comm-central']['platforms']['linux']['base_name'] = 'Linux comm-central lightning'
BRANCHES['comm-central']['platforms']['linux64']['base_name'] = 'Linux x86_64 comm-central lightning'
BRANCHES['comm-central']['platforms']['win32']['base_name'] = 'WINNT 5.2 comm-central lightning'
BRANCHES['comm-central']['platforms']['macosx64']['base_name'] = 'MacOSX 10.6 comm-central lightning'
BRANCHES['comm-central']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['linux64']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['macosx64']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['linux']['milestone'] = "comm-central/linux-xpi"
BRANCHES['comm-central']['platforms']['linux64']['milestone'] = "comm-central/linux64-xpi"
BRANCHES['comm-central']['platforms']['win32']['milestone'] = "comm-central/win32-xpi"
BRANCHES['comm-central']['platforms']['macosx64']['milestone'] = "comm-central/macosx-xpi"
BRANCHES['comm-central']['platforms']['macosx64']['upload_glob'] = "mozilla/dist/universal/xpi-stage/{lightning,gdata-provider}.xpi"

# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central']['create_snippet'] = False
BRANCHES['comm-central']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central']['platforms']['linux64']['update_platform'] = 'Linux_x86_64-gcc3'
BRANCHES['comm-central']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central']['platforms']['macosx64']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['linux64']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['macosx64']['upload_symbols'] = True
BRANCHES['comm-central']['tinderbox_tree'] = 'CalendarTrunk'
BRANCHES['comm-central']['platforms']['linux']['slaves'] = BUILDERS['linux']['community']
BRANCHES['comm-central']['platforms']['linux64']['slaves'] = BUILDERS['linux64']['momo']
BRANCHES['comm-central']['platforms']['win32']['slaves'] = BUILDERS['win32']['community']
BRANCHES['comm-central']['platforms']['macosx64']['slaves'] = BUILDERS['macosx']['10.6']['momo']

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['linux64']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['macosx64']['platform_objdir'] = '%s/i386' % OBJDIR
BRANCHES['comm-central']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/calbld_dsa',
}
BRANCHES['comm-central']['platforms']['linux64']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'SYMBOL_SERVER_SSH_KEY': '/home/cltbld/.ssh/calbld_dsa',
}
BRANCHES['comm-central']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/c/Documents and Settings/calbld/.ssh/calbld_dsa',
}
BRANCHES['comm-central']['platforms']['macosx64']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'DISABLE_LIGHTNING_INSTALL': '1',
    'SYMBOL_SERVER_HOST': SYMBOL_SERVER_HOST,
    'SYMBOL_SERVER_USER': SYMBOL_SERVER_USER,
    'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
    'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
    'SYMBOL_SERVER_SSH_KEY': '/Users/cltbld/.ssh/calbld_dsa',
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
