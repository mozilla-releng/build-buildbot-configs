releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com',]
releaseConfig['PassRecipients']      = ['release-drivers@mozilla.org',]
releaseConfig['AVVendorsRecipients'] = ['av-vendor-release-announce@mozilla.org',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['appName']             = 'browser'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
#  Current version info
releaseConfig['version']             = '3.5.19'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '1.9.1.19'
releaseConfig['buildNumber']         = 2
releaseConfig['baseTag']             = 'FIREFOX_3_5_19'
#  Old version info
releaseConfig['oldVersion']          = '3.5.18'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'FIREFOX_3_5_18'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '3.5.20pre'
releaseConfig['nextMilestone']       = '1.9.1.20pre'
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-1.9.1',
        'path': 'releases/mozilla-1.9.1',
        'revision': '6a8fcd90b366',
        'relbranch': 'GECKO19119_2011041408_RELBRANCH',
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
releaseConfig['l10nRepoPath']        = 'releases/l10n-mozilla-1.9.1'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-1.9.1'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8'
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'win32', 'macosx')
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests'] = False

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = False

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['cvsroot']             = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
releaseConfig['patcherConfig']       = 'moz191-branch-patcher2.cfg'
releaseConfig['commitPatcherConfig'] = True
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R11_1'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage-old.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus2.mozilla.org'
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
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Major update configuration
releaseConfig['majorUpdateRepoPath'] = 'releases/mozilla-2.0'
releaseConfig['majorUpdateToVersion']   = '4.0.1'
releaseConfig['majorUpdateAppVersion']  = releaseConfig['majorUpdateToVersion']
releaseConfig['majorUpdateBuildNumber'] = 1
releaseConfig['majorUpdateBaseTag']     = 'FIREFOX_4_0_1'
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
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')

# Misc configuration
releaseConfig['enable_repo_setup'] = False
