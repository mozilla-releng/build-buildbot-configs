
# Buildbot configuration file


import types

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
    'add_poll_branches':      [ 'dom-inspector'],
    'period':                 60 * 60 * 8,
    'nightly_hour':          [3],
    'nightly_minute':        [0],
    'clobber_url':            "http://build.mozillamessaging.com/clobberer/",
    'builder_type':           "build",
    'tinderbox_tree':         "ThunderbirdTest",
    'codesighs':               False,
    'mozmill':                 False,
    'product_name':           'Thunderbird',
    'brand_name':             'Daily',
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
      'releases/mozilla-aurora':'mozaurora',
    }
}


def makeSlaveList(platformName, isTest, buildConfig, platformConfig):
    bc = buildConfig
    pc = platformConfig
    if platformName == 'linux':
        if isTest:
            return ['momo-vm-fedora12-%02i' % x for x in range(2,5+1)]
        else:
            return ['momo-vm-linux-%02i' % x for x in range(2,9+1) + range(11,16+1)]
    elif platformName == 'linux64':
        if isTest:
            return ['momo-vm-fedora12-64-%02i' % x for x in range(2,5+1)]
        else:
            return ['momo-vm-linux64-%02i' % x for x in range(2,3+1) + range(5,10+1)]
    elif platformName == 'macosx':
        if isTest:
            return ['tb2-darwin9-slave%02i' % x for x in [55,56,57,58,65,67,70]]
        else:
            return ['tb2-darwin9-slave%02i' % x for x in [55,56,57,58,65,67,70]]
    elif platformName == 'macosx64':
        if isTest:
            return [ 'tb2-darwin10-slave%02i'  % x for x in [60,61,62,63,66,69]]
        else:
            return ['momo-xserve-01'] + [ 'tb2-darwin10-slave%02i'  % x for x in [60,61,62,63,66,69]]
    elif platformName == 'win32':
        if isTest:
            return ['momo-vm-win2k3-%02i' % x for x in [1,2,4,5,6,7] + range(8,15+1) + range(17,19+1)]
        else:
            return ['momo-vm-win2k3-%02i' % x for x in [1,2,4,5,6,7] + range(8,15+1) + range(17,19+1)]
    else:
        raise Exception("Invalid platformName '%s'" % platformName)

def makePlatformEnv(platformName, builderType, branchName, buildConfig, platformConfig):
    rv = {}
    bc = buildConfig
    pc = platformConfig
    if platformName == 'linux':
        rv['CVS_RSH'] = 'ssh'
        rv['DISPLAY'] = ':2'
        if branchName == 'comm-1.9.2' and builderType == 'nightly':
            pass
        else:
            if builderType == 'bloat':
                rv['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/lib:objdir-tb/mozilla/dist/bin'
            else:
                rv['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/lib'
        rv['MOZ_CRASHREPORTER_NO_REPORT'] = '1'
        rv['MOZ_OBJDIR'] = 'objdir-tb'
        rv['POST_SYMBOL_UPLOAD_CMD'] = '/usr/local/bin/post-symbol-upload.py'
        rv['SYMBOL_SERVER_HOST'] = 'dm-symbolpush01.mozilla.org'
        rv['SYMBOL_SERVER_PATH'] = '/mnt/netapp/breakpad/symbols_tbrd/'
        rv['SYMBOL_SERVER_SSH_KEY'] = '/home/cltbld/.ssh/tbirdbld_dsa'
        rv['SYMBOL_SERVER_USER'] = 'tbirdbld'
        if builderType != 'bloat':
            rv['TINDERBOX_OUTPUT'] = '1'
        if builderType == 'bloat':
            rv['XPCOM_DEBUG_BREAK'] = 'stack'
    elif platformName == 'linux64':
        rv['CVS_RSH'] = 'ssh'
        rv['DISPLAY'] = ':2'
        if builderType == 'bloat':
            rv['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/lib64:objdir-tb/mozilla/dist/bin'
        else:
            rv['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/lib64'
        rv['MOZ_CRASHREPORTER_NO_REPORT'] = '1'
        rv['MOZ_OBJDIR'] = 'objdir-tb'
        rv['POST_SYMBOL_UPLOAD_CMD'] = '/usr/local/bin/post-symbol-upload.py'
        rv['SYMBOL_SERVER_HOST'] = 'dm-symbolpush01.mozilla.org'
        rv['SYMBOL_SERVER_PATH'] = '/mnt/netapp/breakpad/symbols_tbrd/'
        rv['SYMBOL_SERVER_SSH_KEY'] = '/home/cltbld/.ssh/tbirdbld_dsa'
        rv['SYMBOL_SERVER_USER'] = 'tbirdbld'
        if builderType != 'bloat':
            rv['TINDERBOX_OUTPUT'] = '1'
        if builderType == 'bloat':
            rv['XPCOM_DEBUG_BREAK'] = 'stack'
    elif platformName == 'macosx':
        rv['CVS_RSH'] = 'ssh'
        rv['DISPLAY'] = ':2'
        rv['MOZ_CRASHREPORTER_NO_REPORT'] = '1'
        rv['MOZ_OBJDIR'] = 'objdir-tb'
        rv['MOZ_PKG_PLATFORM'] = 'mac'
        rv['POST_SYMBOL_UPLOAD_CMD'] = '/usr/local/bin/post-symbol-upload.py'
        rv['SYMBOL_SERVER_HOST'] = 'dm-symbolpush01.mozilla.org'
        rv['SYMBOL_SERVER_PATH'] = '/mnt/netapp/breakpad/symbols_tbrd/'
        rv['SYMBOL_SERVER_SSH_KEY'] = '/Users/cltbld/.ssh/tbirdbld_dsa'
        rv['SYMBOL_SERVER_USER'] = 'tbirdbld'
        if builderType != 'bloat':
            rv['TINDERBOX_OUTPUT'] = '1'
        if builderType == 'bloat':
            rv['XPCOM_DEBUG_BREAK'] = 'stack'
    elif platformName == 'macosx64':
        rv['CVS_RSH'] = 'ssh'
        rv['MOZ_CRASHREPORTER_NO_REPORT'] = '1'
        rv['MOZ_OBJDIR'] = 'objdir-tb'
        rv['POST_SYMBOL_UPLOAD_CMD'] = '/usr/local/bin/post-symbol-upload.py'
        rv['SYMBOL_SERVER_HOST'] = 'dm-symbolpush01.mozilla.org'
        rv['SYMBOL_SERVER_PATH'] = '/mnt/netapp/breakpad/symbols_tbrd/'
        rv['SYMBOL_SERVER_SSH_KEY'] = '/Users/cltbld/.ssh/tbirdbld_dsa'
        rv['SYMBOL_SERVER_USER'] = 'tbirdbld'
        rv['TINDERBOX_OUTPUT'] = '1'
    elif platformName == 'win32':
        rv['CVS_RSH'] = 'ssh'
        rv['DISPLAY'] = ':2'
        rv['MOZ_CRASHREPORTER_NO_REPORT'] = '1'
        rv['MOZ_OBJDIR'] = 'objdir-tb'
        rv['POST_SYMBOL_UPLOAD_CMD'] = '/usr/local/bin/post-symbol-upload.py'
        rv['SYMBOL_SERVER_HOST'] = 'dm-symbolpush01.mozilla.org'
        rv['SYMBOL_SERVER_PATH'] = '/mnt/netapp/breakpad/symbols_tbrd/'
        rv['SYMBOL_SERVER_SSH_KEY'] = '/c/Documents and Settings/cltbld/.ssh/tbirdbld_dsa'
        rv['SYMBOL_SERVER_USER'] = 'tbirdbld'
        if builderType != 'bloat':
            rv['TINDERBOX_OUTPUT'] = '1'
        if builderType == 'bloat':
            rv['XPCOM_DEBUG_BREAK'] = 'stack'
    else:
        raise Exception("Invalid platformName '%s'" % platformName)
    return rv

def makePlatformConfig(buildConfig, builderType, platformName, branchName):
    bc = buildConfig
    pc = {}
    if platformName == 'linux':
        pc['base_name'] = "Linux %s" % bc['branch_name']
        pc['builds_before_reboot'] = 1
        pc['check_objdir'] = 'objdir-tb'
        pc['enable_ccache'] = True
        if branchName == 'comm-1.9.2' or builderType == 'bloat':
            pass
        else:
            pc['enable_checktests'] = True
        if builderType == 'bloat':
            pc['leak_threshold'] = 970000
        if builderType != 'check':
            pc['platform_objdir'] = 'objdir-tb'
            pc['profiled_build'] = False
            pc['update_platform'] = 'Linux_x86-gcc3'
        if builderType != 'check':
            pc['env'] = makePlatformEnv(platformName, builderType, branchName, buildConfig, pc)
        pc['slaves'] = makeSlaveList(platformName, False, buildConfig, pc)
        pc['test-slaves'] = makeSlaveList(platformName, True, buildConfig, pc)
        if builderType == 'check':
            pass
        elif builderType == 'bloat':
            pc['upload_symbols'] = False
        else:
            pc['upload_symbols'] = True
    elif platformName == 'linux64':
        pc['base_name'] = "Linux x86-64 %s" % bc['branch_name']
        pc['builds_before_reboot'] = 1
        pc['check_objdir'] = 'objdir-tb'
        pc['enable_ccache'] = True
        if builderType not in ['bloat', 'check']:
            pc['enable_checktests'] = True
        if builderType == 'bloat':
            pc['leak_threshold'] = 1400000
        if builderType != 'check':
            pc['platform_objdir'] = 'objdir-tb'
            pc['profiled_build'] = False
            pc['update_platform'] = 'Linux_x86_64-gcc3'
            pc['upload_symbols'] = False
        if builderType != 'check':
            pc['env'] = makePlatformEnv(platformName, builderType, branchName, buildConfig, pc)
        pc['slaves'] = makeSlaveList(platformName, False, buildConfig, pc)
        pc['test-slaves'] = makeSlaveList(platformName, True, buildConfig, pc)
        if builderType == 'check':
            pass
        elif builderType == 'bloat':
            pc['upload_symbols'] = False
        else:
            pc['upload_symbols'] = True
    elif platformName == 'macosx':
        pc['base_name'] = "MacOSX 10.5 %s" % bc['branch_name']
        pc['builds_before_reboot'] = 1
        if builderType == 'check':
            pass
        elif builderType == 'bloat':
            pc['check_objdir'] = 'objdir-tb'
        else:
            pc['check_objdir'] = 'objdir-tb/ppc'
        pc['enable_ccache'] = True
        if builderType == 'bloat':
            if branchName == 'comm-1.9.2':
                pc['leak_threshold'] = 2500000
            else:
                pc['leak_threshold'] = 3400000
        if builderType == 'check':
            pass
        elif builderType == 'bloat':
            pc['platform_objdir'] = 'objdir-tb'
        else:
            pc['platform_objdir'] = 'objdir-tb/ppc'
        if builderType != 'check':
            pc['profiled_build'] = False
            pc['update_platform'] = 'Darwin_Universal-gcc3'
            pc['env'] = makePlatformEnv(platformName, builderType, branchName, buildConfig, pc)
        pc['slaves'] = makeSlaveList(platformName, False, buildConfig, pc)
        pc['test-slaves'] = makeSlaveList(platformName, True, buildConfig, pc)
        if builderType == 'check':
            pass
        elif builderType == 'bloat':
            pc['upload_symbols'] = False
        else:
            pc['upload_symbols'] = True
    elif platformName == 'macosx64':
        pc['base_name'] = "MacOSX 10.6 %s" % bc['branch_name']
        pc['builds_before_reboot'] = 1
        if builderType == 'bloat':
            pc['check_objdir'] = 'objdir-tb'
        else:
            pc['check_objdir'] = 'objdir-tb/x86_64'
        pc['enable_ccache'] = True
        pc['enable_checktests'] = True
        if builderType == 'bloat':
            pc['platform_objdir'] = 'objdir-tb'
        else:
            pc['platform_objdir'] = 'objdir-tb/i386'
        pc['profiled_build'] = False
        pc['update_platform'] = 'Darwin_x86_64-gcc3'
        if builderType != 'check':
            pc['env'] = makePlatformEnv(platformName, builderType, branchName, buildConfig, pc)
        pc['slaves'] = makeSlaveList(platformName, False, buildConfig, pc)
        pc['test-slaves'] = makeSlaveList(platformName, True, buildConfig, pc)
        pc['upload_symbols'] = True
    elif platformName == 'win32':
        pc['base_name'] = "WINNT 5.2 %s" % bc['branch_name']
        pc['builds_before_reboot'] = 1
        pc['check_objdir'] = 'objdir-tb'
        if builderType in ['bloat', 'check']:
            pass
        else:
            pc['codesighs'] = False
        if (branchName == 'comm-1.9.2' or builderType == 'bloat'):
            pass
        else:
            pc['enable_checktests'] = True
        if builderType == 'bloat':
            if branchName == 'comm-1.9.2':
                pc['leak_threshold'] = 110000
            else:
                pc['leak_threshold'] = 1400000
        if builderType != 'check':
            pc['platform_objdir'] = 'objdir-tb'
            pc['profiled_build'] = False
        if builderType != 'check':
            pc['update_platform'] = 'WINNT_x86-msvc'
        if builderType != 'check':
            pc['env'] = makePlatformEnv(platformName, builderType, branchName, buildConfig, pc)
        pc['slaves'] = makeSlaveList(platformName, False, buildConfig, pc)
        pc['test-slaves'] = makeSlaveList(platformName, True, buildConfig, pc)
        if builderType == 'check':
            pass
        elif builderType == 'bloat':
            pc['upload_symbols'] = False
        else:
            pc['upload_symbols'] = True
    else:
        raise Exception("Invalid platformName '%s'" % platformName)
    return pc

def makeAusConfig(branchName):
    ac = {}
    ac['base_upload_dir'] = '/opt/aus/build/0/Thunderbird/%s' % branchName
    ac['host'] = 'aus-staging.sj.mozillamessaging.com'
    ac['user'] = 'tbirdbld'
    return ac

def makeBuildConfig(builderType=None, branchName=None, hgBranch=None,
                    mozillaCentralBranch=None, tinderboxTree=None, allLocalesFile=None,
                    wantNightly=None, wantL10n=None, l10nRepo=None):
    bc = {}
    bc['hg_branch'] = hgBranch
    bc['tinderbox_tree'] = tinderboxTree
    if builderType == 'nightly':
        if wantNightly != None:
            bc['nightly'] = wantNightly
        if wantL10n == None:
            bc['l10n'] = True
            bc['l10n_repo'] = 'releases/l10n-miramar'
        else:
            bc['l10n'] = wantL10n
            bc['l10n_repo'] = l10nRepo
        bc['branch_name'] = branchName
        bc['allLocalesFile'] = \
            '%s/build/buildbot-configs/raw-file/default/thunderbird/l10n/%s' % (HGURL, allLocalesFile)
        # Blocklist settings
        bc['repo_path'] = bc['hg_branch'] # alias
        bc['product_name'] = 'thunderbird'
        if branchName in ['comm-release', 'comm-central-tested']:
            bc['enable_blocklist_update'] = False
        else:
            bc['enable_blocklist_update'] = True
        if branchName in ['comm-central', 'comm-1.9.2']:
            bc['blocklist_update_on_closed_tree'] = True
        else:
            bc['blocklist_update_on_closed_tree'] = False
        bc['hg_ssh_key'] = '/home/cltbld/.ssh/tbirdbld_dsa'
        bc['hg_username'] = 'tbirdbld'
        bc['hgurl'] = DEFAULTS['hgurl']
        bc['build_tools_repo_path'] = DEFAULTS['build_tools_repo']
        # end Blocklist settings
        bc['client_py_extra_args'] = \
            ['--skip-comm',
             '--hg-options=--verbose --time',
             '--skip-venkman',
             '--skip-chatzilla']
        if 'comm-central-tested' in branchName:
            bc['client_py_extra_args'] += ['--known-good']
        bc['codesighs'] = True
        bc['create_snippet'] = True
        bc['factory'] = 'CCNightlyBuildFactory'
        if branchName in ['comm-central-tested']:
            bc['l10n_nightly_updates'] = False
        else:
            bc['l10n_nightly_updates'] = True
        if branchName == 'comm-1.9.2':
            bc['l10n_tree'] = 'tb31x'
        else:
            bc['l10n_tree'] = 'tb'
        bc['milestone'] = branchName
        bc['mozconfig'] = 'nightly'
        bc['mozilla_central_branch'] = mozillaCentralBranch
        if branchName in ['comm-1.9.2']:
            bc['nightly_hour'] = [0]
        bc['package'] = True
        if branchName not in ['comm-central', 'comm-central-tested', 'comm-1.9.2']:
            bc['period'] = 50400
        bc['upload_stage'] = True
        if branchName != 'comm-1.9.2':
            bc['packageTests'] = True
            bc['unittest_masters'] = [
               ('momo-vm-03.sj.mozillamessaging.com:9010',False,3),
              ]
        bc['platforms'] = {}
        for platformName in ['linux', 'linux64', 'macosx', 'macosx64', 'win32']:
            if platformName == 'macosx' and branchName != 'comm-1.9.2':
                continue
            if platformName in ['linux64', 'macosx64'] and branchName == 'comm-1.9.2':
                continue
            bc['platforms'][platformName] = makePlatformConfig(bc, builderType, platformName, branchName)
        bc['aus'] = makeAusConfig(branchName)
    elif builderType == 'bloat':
        bc['branch_name'] = branchName
        bc['builder_type'] = builderType
        bc['client_py_args'] = \
            ['--skip-comm',
             '--hg-options=--verbose --time',
             '--mozilla-repo=http://hg.mozilla.org/%s' % mozillaCentralBranch]
        bc['client_py_extra_args'] = ['--skip-venkman', '--skip-chatzilla']
        if 'comm-central-tested' in branchName:
            bc['client_py_extra_args'] += ['--known-good']
        bc['codesighs'] = False
        bc['create_snippet'] = False
        bc['factory'] = 'CCNightlyBuildFactory'
        bc['l10n'] = False
        bc['leak'] = True
        bc['mozconfig'] = 'debug'
        bc['mozilla_central_branch'] = mozillaCentralBranch
        bc['nightly'] = False
        bc['package'] = False
        if branchName == 'comm-1.9.2':
            pass
        else:
            bc['period'] = 50400
        bc['upload_stage'] = True
        bc['platforms'] = {}
        for platformName in ['linux', 'linux64', 'macosx', 'macosx64', 'win32']:
            if platformName == 'macosx64' and bc['hg_branch'] not in ['comm-central', 'comm-central-tested']:
                continue
            if platformName in ['linux64', 'macosx64'] and \
               branchName == 'comm-1.9.2':
                continue
            bc['platforms'][platformName] = makePlatformConfig(bc, builderType, platformName, branchName)
        bc['upload_stage'] = False
    elif builderType == 'check':
        bc['branch_name'] = branchName
        bc['builder_type'] = builderType
        bc['client_py_extra_args'] = \
            ['--skip-comm',
             '--hg-options=--verbose --time',
             '--skip-venkman',
             '--skip-chatzilla']
        bc['factory'] = 'CCUnittestBuildFactory'
        bc['mozmill'] = True
        bc['nightly'] = False
        bc['mozilla_central_branch'] = mozillaCentralBranch
        if branchName == 'comm-1.9.2':
            pass
        else:
            bc['unittest_masters'] = [
               ('momo-vm-03.sj.mozillamessaging.com:9010',False,3),
              ]
        bc['platforms'] = {}
        for platformName in ['linux', 'linux64', 'macosx', 'macosx64', 'win32']:
            if platformName == 'macosx' and branchName != 'comm-1.9.2':
                continue
            if platformName in ['macosx64']:
                continue
            bc['platforms'][platformName] = makePlatformConfig(bc, builderType, platformName, branchName)
    else:
        raise Exception("Invalid builderType '%s'" % builderType)
    return bc

BRANCHES = {}

BRANCHES['comm-beta'] = makeBuildConfig(
                               builderType   = 'nightly',
                               branchName    = 'comm-beta',
                               hgBranch      = 'releases/comm-beta',
                               mozillaCentralBranch = 'releases/mozilla-beta',
                               tinderboxTree = 'Thunderbird-Beta',
                               allLocalesFile = 'all-locales.comm-beta',
                               wantNightly   = False,
                               wantL10n      = False
                           )
BRANCHES['comm-beta-bloat'] = makeBuildConfig(
                               builderType   = 'bloat',
                               branchName    = 'comm-beta',
                               hgBranch      = 'releases/comm-beta',
                               mozillaCentralBranch = 'releases/mozilla-beta',
                               tinderboxTree = 'Thunderbird-Beta'
                           )
BRANCHES['comm-release'] = makeBuildConfig(
                               builderType   = 'nightly',
                               branchName    = 'comm-release',
                               hgBranch      = 'releases/comm-release',
                               mozillaCentralBranch = 'releases/mozilla-release',
                               tinderboxTree = 'Thunderbird-Release',
                               allLocalesFile = 'all-locales.comm-release',
                               wantNightly   = False,
                               wantL10n      = False
                           )
BRANCHES['comm-release-bloat'] = makeBuildConfig(
                               builderType   = 'bloat',
                               branchName    = 'comm-release',
                               hgBranch      = 'releases/comm-release',
                               mozillaCentralBranch = 'releases/mozilla-release',
                               tinderboxTree = 'Thunderbird-Release'
                           )
BRANCHES['comm-aurora'] = makeBuildConfig(
                               builderType   = 'nightly',
                               branchName    = 'comm-aurora',
                               hgBranch      = 'releases/comm-aurora',
                               mozillaCentralBranch = 'releases/mozilla-aurora',
                               tinderboxTree = 'Thunderbird-Aurora',
                               allLocalesFile = 'all-locales.comm-aurora',
                               wantL10n      = True,
                               l10nRepo      = 'releases/l10n/mozilla-aurora'
                           )
BRANCHES['comm-aurora-bloat'] = makeBuildConfig(
                               builderType   = 'bloat',
                               branchName    = 'comm-aurora',
                               hgBranch      = 'releases/comm-aurora',
                               mozillaCentralBranch = 'releases/mozilla-aurora',
                               tinderboxTree = 'Thunderbird-Aurora'
                           )

BRANCHES['comm-central'] = makeBuildConfig(
                               builderType   = 'nightly',
                               branchName    = 'comm-central',
                               hgBranch      = 'comm-central',
                               mozillaCentralBranch = 'mozilla-central',
                               tinderboxTree = 'ThunderbirdTrunk',
                               allLocalesFile = 'all-locales.comm-central',
                               wantL10n      = True,
                               l10nRepo      = 'l10n-central'
                           )
BRANCHES['comm-central-bloat'] = makeBuildConfig(
                               builderType   = 'bloat',
                               branchName    = 'comm-central',
                               hgBranch      = 'comm-central',
                               mozillaCentralBranch = 'mozilla-central',
                               tinderboxTree = 'ThunderbirdTrunk'
                           )

BRANCHES['comm-central-tested'] = makeBuildConfig(
                               builderType   = 'nightly',
                               branchName    = 'comm-central-tested',
                               hgBranch      = 'comm-central',
                               mozillaCentralBranch = 'mozilla-central',
                               tinderboxTree = 'ThunderbirdTested',
                               wantNightly   = False,
                               wantL10n      = False
                           )
BRANCHES['comm-central-tested-bloat'] = makeBuildConfig(
                               builderType   = 'bloat',
                               branchName    = 'comm-central-tested',
                               hgBranch      = 'comm-central',
                               mozillaCentralBranch = 'mozilla-central',
                               tinderboxTree = 'ThunderbirdTested',
                               wantL10n      = False
                           )

BRANCHES['comm-1.9.2'] = makeBuildConfig(
                               builderType   = 'nightly',
                               branchName    = 'comm-1.9.2',
                               hgBranch      = 'releases/comm-1.9.2',
                               mozillaCentralBranch = 'releases/mozilla-1.9.2',
                               tinderboxTree = 'Thunderbird3.1',
                               allLocalesFile = 'all-locales.comm-1.9.2',
                               wantL10n      = True,
                               l10nRepo      = 'releases/l10n-mozilla-1.9.2'
                           )
BRANCHES['comm-1.9.2-bloat'] = makeBuildConfig(
                               builderType   = 'bloat',
                               branchName    = 'comm-1.9.2',
                               hgBranch      = 'releases/comm-1.9.2',
                               mozillaCentralBranch = 'releases/mozilla-1.9.2',
                               tinderboxTree = 'Thunderbird3.1'
                           )
BRANCHES['comm-1.9.2-unittest'] = makeBuildConfig(
                               builderType   = 'check',
                               branchName    = 'comm-1.9.2',
                               hgBranch      = 'releases/comm-1.9.2',
                               mozillaCentralBranch = 'releases/mozilla-1.9.2',
                               tinderboxTree = 'Thunderbird3.1'
                           )

# ----------------


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

    for branch in sorted(branches):
        print branch
        pprint.pprint(BRANCHES[branch])
