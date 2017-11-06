# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
releaseConfig = {}
releaseConfig['base_clobber_url'] = 'https://api.pub.build.mozilla.org/clobberer/forceclobber'

# Release Notification
releaseConfig['AllRecipients']       = ['<release-automation-notifications@mozilla.com>',]
releaseConfig['ImportantRecipients'] = ['<release-drivers@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'fennec'
releaseConfig['stage_product']       = 'mobile'
releaseConfig['appName']             = 'mobile'
releaseConfig['relbranchPrefix']     = 'MOBILE'
#  Current version info
releaseConfig['version']             = '53.0.1'
releaseConfig['appVersion']          = '53.0.1'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FENNEC_53_0_1'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['version']
releaseConfig['nextMilestone']       = releaseConfig['version']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mobile': {
        'name': 'mozilla-release',
        'path': 'releases/mozilla-release',
        'revision': 'f50b8b33a3523b542db42008c27551edf1baad58',
        'relbranch': None,
        'bumpFiles': {
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'browser/config/version_display.txt': {
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
releaseConfig['l10nRepoPath']        = 'l10n-central'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mobile-release.json'
releaseConfig['l10nJsonFile']        = releaseConfig['l10nRevisionFile']
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']        = ('android-api-15', 'android-x86')
releaseConfig['notifyPlatforms']      = releaseConfig['enUSPlatforms']
releaseConfig['unittestPlatforms']    = ()
releaseConfig['talosTestPlatforms']   = ()
releaseConfig['enableUnittests']      = False

# L10n configuration
releaseConfig['l10nPlatforms']       = ('android-api-15',)
releaseConfig['l10nNotifyPlatforms'] = releaseConfig['l10nPlatforms']
releaseConfig['mergeLocales']        = True
releaseConfig['enableMultiLocale']   = True

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_rsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'archive.mozilla.org'
releaseConfig['stagingServer']       = 'upload.ffxbld.productdelivery.prod.mozaws.net'
releaseConfig['S3Credentials']       = '/builds/release-s3.credentials'
releaseConfig['S3Bucket']            = 'net-mozaws-prod-delivery-archive'
releaseConfig['ausServerUrl']        = 'https://aus4.mozilla.org'

# Partner repack configuration
releaseConfig['doPartnerRepacks']       = True
releaseConfig['partnerRepackPlatforms'] = ()
releaseConfig['partnerRepackConfig'] = {
    'use_mozharness': True,
    'platforms': {
        'android': {
            'script': 'scripts/mobile_partner_repack.py',
            'config_file': 'partner_repacks/release_mozilla-release_android.py',
         },
    },
}

# mozconfigs
releaseConfig['mozconfigs']          = {
    'android-api-15': 'mobile/android/config/mozconfigs/android-api-15/release',
    'android-x86': 'mobile/android/config/mozconfigs/android-x86/release',
}
releaseConfig['source_mozconfig']    = 'browser/config/mozconfigs/linux64/source'
releaseConfig['releaseChannel']        = 'release'
releaseConfig["updateChannels"] = {
    "release": {
        "ruleId": -1, # TBD
        "localTestChannel": "release-localtest",
        "cdnTestChannel": "release-cdntest",
        "testChannels": {
            "release-localtest": {
                "ruleId": -1, # TBD
            },
            "release-cdntest": {
                "ruleId": -1, # TBD
            }
        }
    }
}

# Fennec specific
releaseConfig['usePrettyNames']           = False
releaseConfig['disableStandaloneRepacks'] = True
releaseConfig['disableVirusCheck']        = True
releaseConfig['enableUpdatePackaging']    = False
releaseConfig['balrog_api_root']          = None

releaseConfig['single_locale_options'] = {
    'android-api-15': [
        '--cfg',
        'single_locale/release_mozilla-release_android_api_15.py',
        '--tag-override', '%s_RELEASE' % releaseConfig['baseTag'],
        '--cfg', 'single_locale/production.py',
        '--no-taskcluster-upload',
    ],
}

releaseConfig['multilocale_config'] = {
    'platforms': {
        'android-api-15':
            'multi_locale/release_mozilla-release_android.json',
        'android-x86':
            'multi_locale/release_mozilla-release_android-x86.json',
    },
    'multilocaleOptions': [
        '--tag-override=%s_RELEASE' % releaseConfig['baseTag'],
        '--pull-locale-source',
        '--add-locales',
        '--package-multi',
        '--summary',
    ]
}
releaseConfig['enableSigningAtBuildTime'] = True
releaseConfig['enablePartialMarsAtBuildTime'] = False
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('android-api-15', 'android-x86', 'linux')
releaseConfig['partialUpdates']      = {}
releaseConfig['bouncerServer']       = 'download.mozilla.org'

releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_fennec.py'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['bouncer_aliases'] = {
    'Fennec-%(version)s': 'fennec-latest',
}
releaseConfig['skip_updates']        = True