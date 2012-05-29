releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com','akeybl@mozilla.com','Callek@gmail.com']
releaseConfig['ImportantRecipients'] = ['thunderbird-drivers@mozilla.org',]
releaseConfig['AVVendorsRecipients'] = ['av-vendor-release-announce@mozilla.org',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'thunderbird'
releaseConfig['appName']             = 'mail'
releaseConfig['mozilla_dir']         = 'mozilla'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
#  Current version info
releaseConfig['version']             = '11.0'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = releaseConfig['version']
releaseConfig['buildNumber']         = 2
releaseConfig['baseTag']             = 'THUNDERBIRD_11_0'
#  Old version info
releaseConfig['oldVersion']          = '10.0.2'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'THUNDERBIRD_10_0_2'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'comm': {
        'name': 'comm-release',
        'path': 'releases/comm-release',
        'revision': '832c448e5d0a',
        'relbranch': None,
        'bumpFiles': {
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
        }
    },
    'mozilla': {
        'name': 'mozilla-release',
        'path': 'releases/mozilla-release',
        'revision': '5bcfa0da3be9',
        'relbranch': None,
        'bumpFiles': {},
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-release'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_thunderbird-release'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
    'build/mozharness': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['xulrunnerPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests'] = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'mail/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = True

# Mercurial account
releaseConfig['hgUsername']          = 'tbirdbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/tbirdbld_dsa'

# Update-specific configuration
releaseConfig['cvsroot']             = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
releaseConfig['patcherConfig']       = 'mozRelease-thunderbird-branch-patcher2.cfg'
releaseConfig['commitPatcherConfig'] = True
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R15'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus3.mozilla.org'
releaseConfig['ausHost']             = 'aus3-staging.mozilla.org'
releaseConfig['ausUser']             = 'tbirdbld'
releaseConfig['ausSshKey']           = 'auspush'
releaseConfig['releaseNotesUrl']     = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
releaseConfig['testOlderPartials']   = False
releaseConfig['verifyConfigs']       = {
    'linux':  'mozRelease-thunderbird-linux.cfg',
    'linux64':  'mozRelease-thunderbird-linux64.cfg',
    'macosx64': 'mozRelease-thunderbird-mac64.cfg',
    'win32':  'mozRelease-thunderbird-win32.cfg'
}
releaseConfig['mozconfigs']          = {
    'linux': 'mail/config/mozconfigs/linux32/release',
    'linux64': 'mail/config/mozconfigs/linux64/release',
    'macosx64': 'mail/config/mozconfigs/macosx-universal/release',
    'win32': 'mail/config/mozconfigs/win32/release',
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = True
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Major update configuration
releaseConfig['majorUpdateRepoPath'] = None
# Tuxedo/Bouncer configuration
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['enableSigningAtBuildTime'] = False
releaseConfig['enablePartialMarsAtBuildTime'] = False
