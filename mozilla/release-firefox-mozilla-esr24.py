# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
releaseConfig = {}

releaseConfig['disable_tinderbox_mail'] = True
releaseConfig['base_clobber_url'] = 'http://clobberer.pvt.build.mozilla.org/always_clobber.php'

# Release Notification
releaseConfig['AllRecipients']       = ['<release@mozilla.com>',
                                        '<release-mgmt@mozilla.com>',
                                        '<qa-drivers@mozilla.com>']
releaseConfig['ImportantRecipients'] = ['<release-drivers@mozilla.org>', '<mikeperry@torproject.org>']
releaseConfig['AVVendorsRecipients'] = ['<av-vendor-release-announce@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['appName']             = 'browser'
#  Current version info
releaseConfig['version']             = '24.5.0esr'
releaseConfig['appVersion']          = '24.5.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_24_5_0esr'
releaseConfig['partialUpdates']      = {

    '24.4.0esr': {
        'appVersion': '24.4.0',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_24_4_0esr',
    },

}
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '24.5.0esrpre'
releaseConfig['nextMilestone']       = releaseConfig['nextAppVersion']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        # XXX remove js/src/config/milestone.txt when setting up ESR31
        'name': 'mozilla-esr24',
        'path': 'releases/mozilla-esr24',
        'revision': '2dcea6a55d16',
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
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-release'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-esr24'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_0_9_5',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
    'build/mozharness': 'production',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['xulrunnerPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = True

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['patcherConfig']       = 'mozEsr24-branch-patcher2.cfg'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus3.mozilla.org'
releaseConfig['ausHost']             = 'aus3-staging.mozilla.org'
releaseConfig['ausUser']             = 'ffxbld'
releaseConfig['ausSshKey']           = 'ffxbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['useBetaChannel']      = 1
releaseConfig['updateVerifyChunks']  = 6
releaseConfig['verifyConfigs']       = {
    'linux':  'mozEsr24-firefox-linux.cfg',
    'linux64':  'mozEsr24-firefox-linux64.cfg',
    'macosx64': 'mozEsr24-firefox-mac64.cfg',
    'win32':  'mozEsr24-firefox-win32.cfg'
}
releaseConfig['mozconfigs']          = {
    'linux': 'browser/config/mozconfigs/linux32/release',
    'linux64': 'browser/config/mozconfigs/linux64/release',
    'macosx64': 'browser/config/mozconfigs/macosx-universal/release',
    'win32': 'browser/config/mozconfigs/win32/release',
}
releaseConfig['releaseChannel']      = 'esr'

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_firefox_esr.py'

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['enableAutomaticPushToMirrors'] = True
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['ftpSymlinkName'] = 'latest-esr'