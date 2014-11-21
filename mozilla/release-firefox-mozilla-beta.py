# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True
releaseConfig['base_clobber_url'] = 'https://api.pub.build.mozilla.org/clobberer/forceclobber'

# Release Notification
releaseConfig['AllRecipients']       = ['<release@mozilla.com>',
                                        '<release-mgmt@mozilla.com>',
                                        '<qa-drivers@mozilla.com>']
releaseConfig['ImportantRecipients'] = ['<release-drivers@mozilla.org>',]
releaseConfig['AVVendorsRecipients'] = ['<av-vendor-release-announce@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['stage_product']       = 'firefox'
releaseConfig['appName']             = 'browser'
#  Current version info
releaseConfig['version']             = '34.0b11'
releaseConfig['appVersion']          = '34.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_34_0b11'
releaseConfig['partialUpdates']      = {

    '34.0b9': {
        'appVersion': '34.0',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_34_0b9',
    },

    '34.0b10': {
        'appVersion': '34.0',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_34_0b10',
    },

}
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-beta',
        'path': 'releases/mozilla-beta',
        'revision': '0bcee2fc8e0b',
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
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-beta'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-beta'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
    'build/mozharness': 'production',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = False

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = True

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_rsa'

# Update-specific configuration
releaseConfig['patcherConfig']       = 'mozBeta-branch-patcher2.cfg'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus3.mozilla.org'
releaseConfig['ausHost']             = 'aus3-staging.mozilla.org'
releaseConfig['ausUser']             = 'ffxbld'
releaseConfig['ausSshKey']           = 'ffxbld_rsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['updateVerifyChunks']  = 6
releaseConfig['verifyConfigs']       = {
    'linux':  'mozBeta-firefox-linux.cfg',
    'linux64':  'mozBeta-firefox-linux64.cfg',
    'macosx64': 'mozBeta-firefox-mac64.cfg',
    'win32':  'mozBeta-firefox-win32.cfg'
}
releaseConfig['mozconfigs']          = {
    'linux': 'browser/config/mozconfigs/linux32/beta',
    'linux64': 'browser/config/mozconfigs/linux64/beta',
    'macosx64': 'browser/config/mozconfigs/macosx-universal/beta',
    'win32': 'browser/config/mozconfigs/win32/beta',
}
releaseConfig['xulrunner_mozconfigs']          = {
    'linux': 'xulrunner/config/mozconfigs/linux32/xulrunner',
    'linux64': 'xulrunner/config/mozconfigs/linux64/xulrunner',
    'macosx64': 'xulrunner/config/mozconfigs/macosx-universal/xulrunner',
    'win32': 'xulrunner/config/mozconfigs/win32/xulrunner',
}
releaseConfig['releaseChannel']        = 'beta'
releaseConfig['releaseChannelRuleIds'] = [32]
releaseConfig['localTestChannel']      = 'beta-localtest'
releaseConfig['cdnTestChannel']        = 'beta-cdntest'
releaseConfig['testChannelRuleIds']    = [25,45]

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = True
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_firefox_beta.py'

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['enableAutomaticPushToMirrors'] = True
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['ftpSymlinkName'] = 'latest-beta'

releaseConfig['bouncer_aliases'] = {
    'Firefox-%(version)s': 'firefox-beta-latest',
    'Firefox-%(version)s-stub': 'firefox-beta-stub',
}