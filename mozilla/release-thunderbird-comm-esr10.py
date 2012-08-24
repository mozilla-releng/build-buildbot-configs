releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True
releaseConfig['base_clobber_url'] = 'http://clobberer.pvt.build.mozilla.org/always_clobber.php'

# Release Notification
releaseConfig['AllRecipients']       = ['<release@mozilla.com>',
                                        '<Callek@gmail.com>',
                                        '<mbanner@mozilla.com>']
releaseConfig['ImportantRecipients'] = ['<thunderbird-drivers@mozilla.org>',]
releaseConfig['AVVendorsRecipients'] = ['<av-vendor-release-announce@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'thunderbird'
releaseConfig['appName']             = 'mail'
releaseConfig['mozilla_dir']         = 'mozilla'
#  Current version info
releaseConfig['version']             = '10.0.7esr'
releaseConfig['appVersion']          = '10.0.7'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'THUNDERBIRD_10_0_7esr'
releaseConfig['partialUpdates']      = {
    '10.0.6esr': {
        'appVersion': '10.0.6',
        'buildNumber': 1,
        'baseTag': 'THUNDERBIRD_10_0_6esr',
    }
}
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '10.0.8esrpre'
releaseConfig['nextMilestone']       = '10.0.8esrpre'
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'comm': {
        'name': 'comm-esr10',
        'path': 'releases/comm-esr10',
        'revision': '1d4617eeb9bd',
        'relbranch': None,
        'bumpFiles': {
            'mail/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
        }
    },
    'mozilla': {
        'name': 'mozilla-esr10',
        'path': 'releases/mozilla-esr10',
        'revision': 'a40ed010dcba',
        'relbranch': 'GECKO1007_2012082413_RELBRANCH',
        'bumpFiles': {},
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-release'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_thunderbird-esr10'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_0_8_2',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
    'build/mozharness': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['xulrunnerPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests'] = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'mail/locales/shipped-locales'
releaseConfig['mergeLocales']        = True

# Mercurial account
releaseConfig['hgUsername']          = 'tbirdbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/tbirdbld_dsa'

# Update-specific configuration
releaseConfig['patcherConfig']       = 'mozEsr10-thunderbird-branch-patcher2.cfg'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus3.mozilla.org'
releaseConfig['ausHost']             = 'aus3-staging.mozilla.org'
releaseConfig['ausUser']             = 'tbirdbld'
releaseConfig['ausSshKey']           = 'auspush'
releaseConfig['releaseNotesUrl']     = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
releaseConfig['testOlderPartials']   = False
releaseConfig['useBetaChannel']      = 1
releaseConfig['verifyConfigs']       = {
    'linux':  'mozEsr10-thunderbird-linux.cfg',
    'linux64':  'mozEsr10-thunderbird-linux64.cfg',
    'macosx64': 'mozEsr10-thunderbird-mac64.cfg',
    'win32':  'mozEsr10-thunderbird-win32.cfg'
}
releaseConfig['mozconfigs']          = {
    'linux': 'mail/config/mozconfigs/linux32/release',
    'linux64': 'mail/config/mozconfigs/linux64/release',
    'macosx64': 'mail/config/mozconfigs/macosx-universal/release',
    'win32': 'mail/config/mozconfigs/win32/release',
}
releaseConfig['releaseChannel']      = 'esr'

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')
releaseConfig['releaseUptake']       = 3
releaseConfig['releasetestUptake']   = 1

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['enableAutomaticPushToMirrors'] = True
