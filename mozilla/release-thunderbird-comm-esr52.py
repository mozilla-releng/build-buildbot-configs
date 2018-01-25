# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
releaseConfig = {}

releaseConfig['base_clobber_url'] = 'https://api.pub.build.mozilla.org/clobberer/forceclobber'

# Release Notification
releaseConfig['AllRecipients']       = ['<release-automation-notifications-thunderbird@mozilla.org>',]
releaseConfig['ImportantRecipients'] = ['<thunderbird-drivers@mozilla.org>',]
releaseConfig['AVVendorsRecipients'] = ['<av-vendor-release-announce@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'thunderbird'
releaseConfig['stage_product']       = 'thunderbird'
releaseConfig['appName']             = 'mail'
releaseConfig['relbranchPrefix']     = 'THUNDERBIRD'
releaseConfig['mozilla_srcdir']      = 'mozilla'
#  Current version info
releaseConfig['version']             = '52.6.0'
releaseConfig['appVersion']          = '52.6.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'THUNDERBIRD_52_6_0'
releaseConfig['partialUpdates']      = {

    '52.5.2': {
        'appVersion': '52.5.2',
        'buildNumber': 1,
        'baseTag': 'THUNDERBIRD_52_5_2',
    },

    '52.5.0': {
        'appVersion': '52.5.0',
        'buildNumber': 1,
        'baseTag': 'THUNDERBIRD_52_5_0',
    },

    '52.4.0': {
        'appVersion': '52.4.0',
        'buildNumber': 3,
        'baseTag': 'THUNDERBIRD_52_4_0',
    },

}
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'comm': {
        'name': 'comm-esr52',
        'path': 'releases/comm-esr52',
        'revision': '490869ee85a2',
        'relbranch': None,
        'bumpFiles': {
            'mail/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'mail/config/version_display.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
        }
    },
    'mozilla': {
        'name': 'mozilla-esr52',
        'path': 'releases/mozilla-esr52',
        'revision': 'ec540cbe2082',
        'relbranch': None,
        'bumpFiles': {
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
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_thunderbird-esr52'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = False

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'mail/locales/shipped-locales'
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = True

# Mercurial account
releaseConfig['hgUsername']          = 'tbirdbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/tbirdbld_dsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'archive.mozilla.org'
releaseConfig['stagingServer']       = 'upload.tbirdbld.productdelivery.prod.mozaws.net'
releaseConfig['S3Credentials']       = '/builds/release-s3.credentials'
releaseConfig['S3Bucket']            = 'net-mozaws-prod-delivery-archive'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus4.mozilla.org'
releaseConfig['releaseNotesUrl']     = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['updateVerifyChunks']  = 6
releaseConfig['mozconfigs']          = {
    'linux': 'mail/config/mozconfigs/linux32/release',
    'linux64': 'mail/config/mozconfigs/linux64/release',
    'macosx64': 'mail/config/mozconfigs/macosx-universal/release',
    'win32': 'mail/config/mozconfigs/win32/release',
}
releaseConfig['source_mozconfig']      = 'mail/config/mozconfigs/linux64/source'
releaseConfig['releaseChannel']        = 'release'
releaseConfig['updateChannels'] = {
    # ruleId needs to be updated with the ID from AUS
    "release": {
        "versionRegex": r"^.*$",
        # https://bugzilla.mozilla.org/show_bug.cgi?id=1426790
        # Alias: thunderbird-esr52
        "ruleId": "516",
        "patcherConfig": "mozEsr52-thunderbird-branch-patcher2.cfg",
        "localTestChannel": "release-localtest",
        "cdnTestChannel": "release-cdntest",
        "verifyConfigs": {
            "linux":  "comm-esr52-thunderbird-linux.cfg",
            "linux64":  "comm-esr52-thunderbird-linux64.cfg",
            "macosx64": "comm-esr52-thunderbird-mac64.cfg",
            "win32":  "comm-esr52-thunderbird-win32.cfg",
        },
        "testChannels": {
            "release-localtest": {
                "ruleId": "thunderbird-esr52-localtest",
            },
            "release-cdntest": {
                "ruleId": "thunderbird-esr52-cdntest",
            },
        },
    },
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_thunderbird.py'
releaseConfig['bouncer_aliases'] = {
    'Thunderbird-%(version)s': 'thunderbird-latest',
}

# Misc configuration
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['extra_signing_env'] = {'TOOLTOOL_DIR': '%(basedir)s/comm-esr52'}
