releaseConfig = {}
releaseConfig['skip_repo_setup']       = True
releaseConfig['disable_tinderbox_mail'] = True

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com',]
releaseConfig['ImportantRecipients'] = ['release@mozilla.com',]
releaseConfig['AVVendorsRecipients'] = ['release@mozilla.com',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[staging-release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'thunderbird'
releaseConfig['appName']             = 'mail'
releaseConfig['mozilla_dir']         = 'mozilla'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
#  Current version info
releaseConfig['version']             = '12.0b5'
releaseConfig['appVersion']          = '12.0'
releaseConfig['milestone']           = '12.0'
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'THUNDERBIRD_12_0b5'
#  Old version info
releaseConfig['oldVersion']          = '12.0b4'
releaseConfig['oldAppVersion']       = '12.0'
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'THUNDERBIRD_12_0b4'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
## Staging repository path
releaseConfig['userRepoRoot'] = 'users/stage-ffxbld'
releaseConfig['sourceRepositories']  = {
    'comm': {
        'name': 'comm-beta',
        'clonePath': 'releases/comm-beta',
        'path': 'users/stage-ffxbld/comm-beta',
        'revision': 'THUNDERBIRD_12_0b5_RELEASE',
        'relbranch': None,
        'bumpFiles': {
            'mail/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
        }
    },
    'mozilla': {
        'name': 'mozilla-beta',
        'clonePath': 'releases/mozilla-beta',
        'path': 'users/stage-ffxbld/mozilla-beta',
        'revision': 'THUNDERBIRD_12_0b5_RELEASE',
        'relbranch': None,
        'bumpFiles': {
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
            'js/src/config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoClonePath']   = 'releases/l10n/mozilla-beta'
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_thunderbird-beta'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_AUTOMATION',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/mozharness': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['xulrunnerPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'mail/locales/shipped-locales'
releaseConfig['l10nChunks']          = 2
releaseConfig['mergeLocales']        = True

# Mercurial account
releaseConfig['hgUsername']          = 'stage-ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['cvsroot']             = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
releaseConfig['patcherConfig']       = 'mozBeta-thunderbird-branch-patcher2.cfg'
releaseConfig['commitPatcherConfig'] = False
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R16'
releaseConfig['ftpServer']           = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['stagingServer']       = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'http://dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausHost']             = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = False
releaseConfig['verifyConfigs']       = {
    'linux':  'mozBeta-thunderbird-linux.cfg',
    'linux64':  'mozBeta-thunderbird-linux64.cfg',
    'macosx64': 'mozBeta-thunderbird-mac64.cfg',
    'win32':  'mozBeta-thunderbird-win32.cfg'
}
releaseConfig['mozconfigs']          = {
    'linux': 'mail/config/mozconfigs/linux32/release',
    'linux64': 'mail/config/mozconfigs/linux64/release',
    'macosx64': 'mail/config/mozconfigs/macosx-universal/release',
    'win32': 'mail/config/mozconfigs/win32/release',
}
releaseConfig['releaseChannel']      = 'beta'

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'users/stage-ffxbld/partner-repacks'

# Major update configuration
releaseConfig['majorUpdateRepoPath'] = None
# Tuxedo/Bouncer configuration
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://tuxedo.stage.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')
releaseConfig['releaseUptake']       = 3
releaseConfig['releasetestUptake']   = 1

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['build_tools_repo_path'] = "users/stage-ffxbld/tools"
releaseConfig['enableAutomaticPushToMirrors'] = True
releaseConfig['enableSigningAtBuildTime'] = False
releaseConfig['enablePartialMarsAtBuildTime'] = False
