releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com',]
releaseConfig['ImportantRecipients'] = ['release@mozilla.com',]
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
releaseConfig['version']             = '3.6.28'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '1.9.2.28'
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_3_6_28'
#  Old version info
releaseConfig['oldVersion']          = '3.6.27'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'FIREFOX_3_6_27'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '3.6.29pre'
releaseConfig['nextMilestone']       = '1.9.2.29pre'
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
    'users/stage-ffxbld/compare-locales': 'RELEASE_0_8_2',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/partner-repacks': 'default'
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'win32', 'macosx')
releaseConfig['notifyPlatforms']     = ('linux', 'win32', 'macosx')
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']

# Unittests
releaseConfig['enableUnittests']     = True
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
releaseConfig['ausHost']             = 'dev-stage01.build.sjc1.mozilla.com'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = True
releaseConfig['useBetaChannelForRelease'] = True
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
releaseConfig['majorUpdateToVersion']   = '11.0'
releaseConfig['majorUpdateAppVersion']  = releaseConfig['majorUpdateToVersion']
releaseConfig['majorUpdateBuildNumber'] = 2
releaseConfig['majorUpdateBaseTag']     = 'FIREFOX_11_0'
releaseConfig['majorUpdateReleaseNotesUrl']  = 'https://www.mozilla.org/%locale%/firefox/latest/details/from-3.6.html'
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
releaseConfig['enableSigningAtBuildTime'] = False
releaseConfig['enablePartialMarsAtBuildTime'] = False
