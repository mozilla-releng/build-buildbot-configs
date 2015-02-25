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
releaseConfig['AllRecipients']       = ['<release+releasespam@mozilla.com>',
                                        '<release-mgmt@mozilla.com>',
                                        '<qa-drivers@mozilla.com>']
releaseConfig['ImportantRecipients'] = ['<release-automation-notifications@mozilla.com>',]
releaseConfig['AVVendorsRecipients'] = ['<av-vendor-release-announce@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['stage_product']       = 'firefox'
releaseConfig['appName']             = 'browser'
#  Current version info
releaseConfig['version']             = '36.0'
releaseConfig['appVersion']          = '36.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 2
releaseConfig['baseTag']             = 'FIREFOX_36_0'
releaseConfig['partialUpdates']      = {

    '35.0': {
        'appVersion': '35.0',
        'buildNumber': 3,
        'baseTag': 'FIREFOX_35_0',
    },

    '35.0.1': {
        'appVersion': '35.0.1',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_35_0_1',
    },

    '34.0.5': {
        'appVersion': '34.0.5',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_34_0_5',
    },

}
releaseConfig['extraPartials']       = {
    '36.0b10': {
        'appVersion': '36.0',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_36_0b10',
    },
}
# What's New Page for Hello TODO: remove on request
releaseConfig['openURL'] = 'https://www.mozilla.org/%locale%/firefox/36.0/whatsnew/?oldversion=%OLD_VERSION%'

# TODO: set this properly when we start shipping win64 on release
#releaseConfig['HACK_first_released_version'] = {'win64': TBD}

#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-release',
        'path': 'releases/mozilla-release',
        'revision': 'a2ffa9047bf4',
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
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-release'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-release'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
    'build/mozharness': 'production',
}

# Platform configuration
# TODO: add win64 when we're ready to ship it
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
releaseConfig['patcherConfig']       = 'mozRelease-branch-patcher2.cfg'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus4.mozilla.org'
releaseConfig['ausHost']             = None
releaseConfig['ausUser']             = 'ffxbld'
releaseConfig['ausSshKey']           = 'ffxbld_rsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['updateVerifyChunks']  = 6
releaseConfig['verifyConfigs']       = {
    'linux':  'mozRelease-firefox-linux.cfg',
    'linux64':  'mozRelease-firefox-linux64.cfg',
    'macosx64': 'mozRelease-firefox-mac64.cfg',
    'win32':  'mozRelease-firefox-win32.cfg',
    #'win64':  'mozRelease-firefox-win64.cfg',
}
releaseConfig['mozconfigs']          = {
    'linux': 'browser/config/mozconfigs/linux32/release',
    'linux64': 'browser/config/mozconfigs/linux64/release',
    'macosx64': 'browser/config/mozconfigs/macosx-universal/release',
    'win32': 'browser/config/mozconfigs/win32/release',
    #'win64': 'browser/config/mozconfigs/win64/release',
}
releaseConfig['xulrunner_mozconfigs']          = {
    'linux': 'xulrunner/config/mozconfigs/linux32/xulrunner',
    'linux64': 'xulrunner/config/mozconfigs/linux64/xulrunner',
    'macosx64': 'xulrunner/config/mozconfigs/macosx-universal/xulrunner',
    'win32': 'xulrunner/config/mozconfigs/win32/xulrunner',
    #'win64': 'xulrunner/config/mozconfigs/win64/xulrunner',
}
releaseConfig['releaseChannel']        = 'release'
releaseConfig['releaseChannelRuleIds'] = [33]
releaseConfig['localTestChannel']      = 'release-localtest'
releaseConfig['cdnTestChannel']        = 'release-cdntest'
releaseConfig['testChannelRuleIds']    = [56,57]

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = True
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'
releaseConfig['syncPartnerBundles']  = True

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_firefox_release.py'

# Misc configuration
releaseConfig['makeIndexFiles'] = True
releaseConfig['enable_repo_setup'] = False
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['ftpSymlinkName'] = 'latest'

releaseConfig['bouncer_aliases'] = {
    'Firefox-%(version)s': 'firefox-latest',
    'Firefox-%(version)s-stub': 'firefox-stub',
}