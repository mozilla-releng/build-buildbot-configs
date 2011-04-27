releaseConfig = {}

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com',]
releaseConfig['PassRecipients']      = ['release@mozilla.com',]
releaseConfig['AVVendorsRecipients'] = ['release@mozilla.com',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[staging-release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['appName']             = 'browser'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
#  Current version info
releaseConfig['version']             = '3.5.17'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '1.9.1.17'
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_3_5_17'
#  Old version info
releaseConfig['oldVersion']          = '3.5.16'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 2
releaseConfig['oldBaseTag']          = 'FIREFOX_3_5_16'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '3.5.18pre'
releaseConfig['nextMilestone']       = '1.9.1.18pre'
#  Repository configuration, for tagging
## Staging repository path
releaseConfig['userRepoRoot'] = 'users/stage-ffxbld'
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-1.9.1',
        'clonePath': 'releases/mozilla-1.9.1',
        'path': 'users/stage-ffxbld/mozilla-1.9.1',
        'revision': 'bc91b067f42f',
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
releaseConfig['l10nRepoClonePath']   = 'releases/l10n-mozilla-1.9.1'
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld/l10n-mozilla-1.9.1'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-1.9.1'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_AUTOMATION',
    'users/stage-ffxbld/buildbot': 'production-0.8'
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'win32', 'macosx')
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['unittestPlatforms']   = ()
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = False

# Mercurial account
releaseConfig['hgUsername']          = 'stage-ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['cvsroot']             = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
releaseConfig['patcherConfig']       = 'moz191-branch-patcher2.cfg'
releaseConfig['commitPatcherConfig'] = False
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R11_1'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'staging-stage.build.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'http://staging-stage.build.mozilla.org'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = True
releaseConfig['useBetaChannel']      = 1
releaseConfig['verifyConfigs']       = {
    'linux':  'moz191-firefox-linux.cfg',
    'macosx': 'moz191-firefox-mac.cfg',
    'win32':  'moz191-firefox-win32.cfg'
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'users/stage-ffxbld/partner-repacks'

# Major update configuration
releaseConfig['majorUpdateRepoPath'] = 'users/stage-ffxbld/mozilla-2.0'
releaseConfig['majorUpdateToVersion']   = '4.0rc1'
releaseConfig['majorUpdateAppVersion']  = '4.0'
releaseConfig['majorUpdateBuildNumber'] = 1
releaseConfig['majorUpdateBaseTag']     = 'FIREFOX_4_0rc1'
releaseConfig['majorUpdateReleaseNotesUrl']  = 'https://www.mozilla.com/%locale%/firefox/4.0/details/'
releaseConfig['majorUpdatePatcherConfig']    = 'moz191-branch-major-update-patcher2.cfg'
releaseConfig['majorPatcherToolsTag']        = 'UPDATE_PACKAGING_R11_1_MU'
releaseConfig['majorUpdateVerifyConfigs']    = {
    'linux':  'moz191-firefox-linux-major.cfg',
    'macosx': 'moz191-firefox-mac-major.cfg',
    'win32':  'moz191-firefox-win32-major.cfg'
}
releaseConfig['majorFakeMacInfoTxt'] = True
# Tuxedo/Bouncer configuration
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://tuxedo.stage.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')

# Misc configuration
releaseConfig['enable_repo_setup'] = True
