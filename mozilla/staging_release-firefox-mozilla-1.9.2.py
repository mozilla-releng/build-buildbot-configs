releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True

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
releaseConfig['version']             = '3.6.15'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '1.9.2.15'
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_3_6_15'
#  Old version info
releaseConfig['oldVersion']          = '3.6.14'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 3
releaseConfig['oldBaseTag']          = 'FIREFOX_3_6_14'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '3.6.16pre'
releaseConfig['nextMilestone']       = '1.9.2.16pre'
#  Repository configuration, for tagging
## Staging repository path
releaseConfig['userRepoRoot'] = 'users/stage-ffxbld'
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-1.9.2',
        'clonePath': 'releases/mozilla-1.9.2',
        'path': 'users/stage-ffxbld/mozilla-1.9.2',
        'revision': 'a50a49f952c0',
        'relbranch': 'GECKO19214_2011012112_RELBRANCH',
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
releaseConfig['l10nRelbranch']       = 'GECKO19214_2011012112_RELBRANCH'
releaseConfig['l10nRepoClonePath']   = 'releases/l10n-mozilla-1.9.2'
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-1.9.2'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_AUTOMATION',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/partner-repacks': 'default'
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'win32', 'macosx')
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']

# Unittests
releaseConfig['enableUnittests'] = True
# this variable adds unit tests on the builders
releaseConfig['unittestPlatforms']   = releaseConfig['enUSPlatforms']

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
releaseConfig['patcherConfig']       = 'moz192-branch-patcher2.cfg'
releaseConfig['commitPatcherConfig'] = False
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R11_1'
releaseConfig['ftpServer']           = 'dev-stage01.build.sjc1.mozilla.com'
releaseConfig['stagingServer']       = 'dev-stage01.build.sjc1.mozilla.com'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'http://dev-stage01.build.sjc1.mozilla.com'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = True
releaseConfig['useBetaChannel']      = 1
releaseConfig['verifyConfigs']       = {
    'linux':  'moz192-firefox-linux.cfg',
    'macosx': 'moz192-firefox-mac.cfg',
    'win32':  'moz192-firefox-win32.cfg'
}
releaseConfig['snippetSchema']       = 1

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'users/stage-ffxbld/partner-repacks'

# Major update configuration
releaseConfig['majorUpdateRepoPath'] = 'users/stage-ffxbld/mozilla-release'
releaseConfig['majorUpdateToVersion']   = '4.0rc1'
releaseConfig['majorUpdateAppVersion']  = '4.0'
releaseConfig['majorUpdateBuildNumber'] = 1
releaseConfig['majorUpdateBaseTag']     = 'FIREFOX_4_0rc1'
releaseConfig['majorUpdateReleaseNotesUrl']  = 'https://www.mozilla.com/%locale%/firefox/4.0/details/'
releaseConfig['majorUpdatePatcherConfig']    = 'moz192-branch-major-update-patcher2.cfg'
releaseConfig['majorPatcherToolsTag']        = 'UPDATE_PACKAGING_R11_1_MU'
releaseConfig['majorUpdateVerifyConfigs']    = {
    'linux':  'moz192-firefox-linux-major.cfg',
    'macosx': 'moz192-firefox-mac-major.cfg',
    'win32':  'moz192-firefox-win32-major.cfg'
}
releaseConfig['majorFakeMacInfoTxt'] = True
releaseConfig['majorSnippetSchema']  = 1

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://tuxedo.stage.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')

# Misc configuration
releaseConfig['enable_repo_setup'] = True
releaseConfig['build_tools_repo_path'] = "users/stage-ffxbld/tools"
