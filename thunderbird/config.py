
# Buildbot configuration file


import types

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
            return ['mini-%02i' % x for x in range(3,9+1)]
        else:
            return ['mini-%02i' % x for x in range(3,9+1)]
    elif platformName == 'macosx64':
        if isTest:
            return ['mini64-%02i' % x for x in [1] + range(3,6+1)]
        else:
            return ['momo-xserve-01'] + ['mini64-%02i' % x for x in [1] + range(3,6+1)]
    elif platformName == 'win32':
        if isTest:
            return ['momo-vm-win2k3-%02i' % x for x in [1,2,4,5,6] + range(8,15+1) + [17]]
        else:
            return ['momo-vm-win2k3-%02i' % x for x in [1,2,4,5,6] + range(8,15+1) + [17]]
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
                rv['LD_LIBRARY_PATH'] = 'objdir-tb/mozilla/dist/bin'
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
            rv['LD_LIBRARY_PATH'] = 'objdir-tb/mozilla/dist/bin'
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
        if builderType == 'bloat':
            pass
        else:
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
        if builderType == 'bloat':
            pass
        else:
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
    elif platformName == 'macosx64':
        pc['base_name'] = "MacOSX 10.6 %s" % bc['branch_name']
        pc['builds_before_reboot'] = 1
        pc['check_objdir'] = 'objdir-tb/x86_64'
        pc['enable_ccache'] = True
        pc['enable_checktests'] = True
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

def makeBuildConfig(builderType, branchName, mozillaRepo, mozillaCentralBranch):
    bc = {}
    if builderType == 'nightly':
        bc['branch_name'] = branchName
        bc['client_py_extra_args'] = \
            ['--skip-comm',
             '--hg-options=--verbose --time',
             '--skip-venkman',
             '--skip-chatzilla']
        bc['codesighs'] = True
        bc['create_snippet'] = True
        bc['factory'] = 'CCNightlyBuildFactory'
        if branchName == 'comm-1.9.2':
            bc['hg_branch'] = 'releases/comm-1.9.2'
        elif branchName == 'comm-miramar':
            bc['hg_branch'] = 'releases/comm-miramar'
        else:
            bc['hg_branch'] = 'comm-central'
        if branchName == 'comm-central':
            bc['l10n'] = True
            bc['l10n_repo'] = 'l10n-central'
        elif branchName == 'comm-1.9.2':
            bc['l10n'] = True
            bc['l10n_repo'] = 'releases/l10n-mozilla-1.9.2'
        else:
            bc['l10n'] = True
            bc['l10n_repo'] = 'releases/l10n/mozilla-aurora'
            bc['mirror'] = {
                'comm-central' : {
                    'src': 'comm-central',
                    'dst': 'releases/comm-miramar',
                },
                'mozilla-aurora' : {
                    'src' : 'releases/mozilla-aurora',
                    'dst' : 'releases/mozilla-miramar',
                },
            }
        bc['l10n_nightly_updates'] = True
        if branchName == 'comm-1.9.2':
            bc['l10n_tree'] = 'tb31x'
        else:
            bc['l10n_tree'] = 'tb'
        bc['milestone'] = branchName
        bc['mozconfig'] = 'nightly'
        bc['mozilla_central_branch'] = mozillaCentralBranch
        if branchName == 'comm-1.9.2':
            bc['nightly_hour'] = [0]
        bc['package'] = True
        if branchName == 'comm-1.9.2':
            pass
        else:
            bc['packageTests'] = True
        if branchName in ['comm-central', 'comm-1.9.2']:
            pass
        else:
            bc['period'] = 50400
        if branchName == 'comm-central':
            bc['tinderbox_tree'] = 'ThunderbirdTrunk'
        elif branchName == 'comm-1.9.2':
            bc['tinderbox_tree'] = 'Thunderbird3.1'
        else:
            bc['tinderbox_tree'] = 'Miramar'
        bc['upload_stage'] = True
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
             '--mozilla-repo=http://hg.mozilla.org/%s' % mozillaRepo]
        bc['client_py_extra_args'] = ['--skip-venkman', '--skip-chatzilla']
        bc['codesighs'] = False
        bc['create_snippet'] = False
        bc['factory'] = 'CCNightlyBuildFactory'
        if branchName == 'comm-1.9.2':
            bc['hg_branch'] = 'releases/comm-1.9.2'
        elif branchName == 'comm-miramar':
            bc['hg_branch'] = 'releases/comm-miramar'
        else:
            bc['hg_branch'] = 'comm-central'
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
        if branchName == 'comm-central':
            bc['tinderbox_tree'] = 'ThunderbirdTrunk'
        elif branchName == 'comm-1.9.2':
            bc['tinderbox_tree'] = 'Thunderbird3.1'
        else:
            bc['tinderbox_tree'] = 'Miramar'
        bc['upload_stage'] = True
        bc['platforms'] = {}
        for platformName in ['linux', 'linux64', 'macosx', 'macosx64', 'win32']:
            if platformName == 'macosx' and \
               (branchName != 'comm-1.9.2' and builderType != 'bloat'):
                continue
            if platformName == 'macosx64' and builderType == 'bloat':
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
        if branchName == 'comm-1.9.2':
            bc['hg_branch'] = 'releases/comm-1.9.2'
        else:
            bc['hg_branch'] = 'comm-central'
        bc['mozmill'] = True
        bc['nightly'] = False
        bc['mozilla_central_branch'] = mozillaCentralBranch
        bc['tinderbox_tree'] = 'Thunderbird3.1'
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
            if platformName in ['linux64', 'macosx64'] and branchName == 'comm-1.9.2' and builderType != 'check':
                continue
            if platformName in ['macosx64'] and builderType == 'check':
                continue
            bc['platforms'][platformName] = makePlatformConfig(bc, builderType, platformName, branchName)
    else:
        raise Exception("Invalid builderType '%s'" % builderType)
    return bc

BRANCHES = {}

# makeBuildConfig(builderType, branchName, mozillaRepo, mozillaCentralBranch)
BRANCHES['comm-aurora'] = makeBuildConfig('nightly', 'comm-miramar', 'releases/mozilla-miramar', 'releases/mozilla-miramar')
BRANCHES['comm-aurora-bloat'] = makeBuildConfig('bloat', 'comm-miramar', 'releases/mozilla-miramar', 'releases/mozilla-miramar')

BRANCHES['comm-central'] = makeBuildConfig('nightly', 'comm-central', 'mozilla-aurora', 'mozilla-central')
BRANCHES['comm-central-bloat'] = makeBuildConfig('bloat', 'comm-central', 'mozilla-central', 'mozilla-central')
BRANCHES['comm-1.9.2'] = makeBuildConfig('nightly', 'comm-1.9.2', 'mozilla-aurora', 'releases/mozilla-1.9.2')
BRANCHES['comm-1.9.2-bloat'] = makeBuildConfig('bloat', 'comm-1.9.2', 'releases/mozilla-1.9.2', 'releases/mozilla-1.9.2')
BRANCHES['comm-1.9.2-unittest'] = makeBuildConfig('check', 'comm-1.9.2', 'mozilla-aurora', 'releases/mozilla-1.9.2')

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
      'releases/mozilla-aurora':'mozaurora',
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

    for branch in sorted(branches):
        print branch
        pprint.pprint(BRANCHES[branch])
