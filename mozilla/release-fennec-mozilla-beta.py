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
releaseConfig['version']             = '46.0b10'
releaseConfig['appVersion']          = '46.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FENNEC_46_0b10'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextVersion']         = releaseConfig['version']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mobile': {
        'name': 'mozilla-beta',
        'path': 'releases/mozilla-beta',
        'revision': '9ea83990839b',
        'relbranch': None,
        'bumpFiles': {
            'browser/config/version_display.txt': {
                'version': releaseConfig['version'],
                'nextVersion': lambda x: x
            },
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': lambda x: x
            },
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': lambda x: x
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-beta'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mobile-beta.json'
releaseConfig['l10nJsonFile']        = releaseConfig['l10nRevisionFile']
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
}

# Platform configuration
releaseConfig['enUSPlatforms']        = ('android-api-9', 'android-api-15', 'android-x86')
releaseConfig['notifyPlatforms']      = releaseConfig['enUSPlatforms']
releaseConfig['unittestPlatforms']    = ()
releaseConfig['talosTestPlatforms']   = ()
releaseConfig['enableUnittests']      = False

# L10n configuration
releaseConfig['l10nPlatforms']       = ('android-api-9', 'android-api-15')
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
releaseConfig['doPartnerRepacks']       = False
releaseConfig['partnersRepoPath']       = 'build/partner-repacks'
releaseConfig['partnerRepackPlatforms'] = ()

# mozconfigs
releaseConfig['mozconfigs']          = {
    'android-api-9': 'mobile/android/config/mozconfigs/android-api-9-10-constrained/release',
    'android-api-15': 'mobile/android/config/mozconfigs/android-api-15/release',
    'android-x86': 'mobile/android/config/mozconfigs/android-x86/release',
}
releaseConfig['source_mozconfig']    = 'browser/config/mozconfigs/linux64/source'
releaseConfig['releaseChannel']      = 'beta'
releaseConfig["updateChannels"] = {
    "beta": {
        "ruleId": 91,
        "localTestChannel": "beta-localtest",
        "cdnTestChannel": "beta-cdntest",
        "testChannels": {
            "beta-localtest": {
                "ruleId": 89,
            },
            "beta-cdntest": {
                "ruleId": 90,
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
    'android-api-9': [
        '--cfg',
        'single_locale/release_mozilla-beta_android_api_9.py',
        '--tag-override', '%s_RELEASE' % releaseConfig['baseTag'],
        '--cfg', 'single_locale/production.py',
        '--no-taskcluster-upload',
    ],
    'android-api-15': [
        '--cfg',
        'single_locale/release_mozilla-beta_android_api_15.py',
        '--tag-override', '%s_RELEASE' % releaseConfig['baseTag'],
        '--cfg', 'single_locale/production.py',
        '--no-taskcluster-upload',
    ],
}

releaseConfig['multilocale_config'] = {
    'platforms': {
        'android-api-9':
            'multi_locale/release_mozilla-beta_android.json',
        'android-api-15':
            'multi_locale/release_mozilla-beta_android.json',
        'android-x86':
            'multi_locale/release_mozilla-beta_android-x86.json',
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
releaseConfig['mock_platforms'] = ('android-api-9', 'android-api-15', 'android-x86', 'linux')
releaseConfig['enableAutomaticPushToMirrors'] = True
releaseConfig['partialUpdates']      = {}
releaseConfig['bouncerServer']       = 'download.mozilla.org'
# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_fennec.py'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['bouncer_aliases'] = {
    'Fennec-%(version)s': 'fennec-beta-latest',
}
releaseConfig['skip_updates']        = True