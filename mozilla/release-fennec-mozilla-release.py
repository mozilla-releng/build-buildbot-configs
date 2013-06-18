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
releaseConfig['AllRecipients']       = ['<release@mozilla.com>','<release-mgmt@mozilla.com>']
releaseConfig['ImportantRecipients'] = ['<release-drivers@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'fennec'
releaseConfig['appName']             = 'mobile'
releaseConfig['relbranchPrefix']     = 'MOBILE'
#  Current version info
releaseConfig['version']             = '22.0'
releaseConfig['appVersion']          = '22.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FENNEC_22_0'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['version']
releaseConfig['nextMilestone']       = releaseConfig['version']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mobile': {
        'name': 'mozilla-release',
        'path': 'releases/mozilla-release',
        'revision': '67c554a06d47',
        'relbranch': None,
        'bumpFiles': {
            'mobile/android/confvars.sh': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
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
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mobile-release.json'
releaseConfig['l10nJsonFile']        = releaseConfig['l10nRevisionFile']
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
    'build/mozharness': 'production',
}

# Platform configuration
releaseConfig['enUSPlatforms']        = ('android', 'android-armv6')
releaseConfig['notifyPlatforms']      = releaseConfig['enUSPlatforms']
releaseConfig['unittestPlatforms']    = ()
releaseConfig['talosTestPlatforms']   = ()
releaseConfig['enableUnittests']      = False

# L10n configuration
releaseConfig['l10nPlatforms']       = ('android',)
releaseConfig['l10nNotifyPlatforms'] = releaseConfig['l10nPlatforms']
releaseConfig['mergeLocales']        = True
releaseConfig['enableMultiLocale']   = True

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus3.mozilla.org'
releaseConfig['ausHost']             = 'aus3-staging.mozilla.org'
releaseConfig['ausUser']             = 'ffxbld'
releaseConfig['ausSshKey']           = 'auspush'

# Partner repack configuration
releaseConfig['doPartnerRepacks']       = True
releaseConfig['partnersRepoPath']       = 'build/partner-repacks'
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
    'android': 'mobile/android/config/mozconfigs/android/release',
    'android-armv6': 'mobile/android/config/mozconfigs/android-armv6/release',
}

# Misc configuration
releaseConfig['enable_repo_setup']       = False

# Fennec specific
releaseConfig['usePrettyNames']           = False
releaseConfig['disableBouncerEntries']    = True
releaseConfig['disableStandaloneRepacks'] = True
releaseConfig['disablePermissionCheck']   = True
releaseConfig['disableVirusCheck']        = True
releaseConfig['disablePushToMirrors']     = True
releaseConfig['enableUpdatePackaging']    = False

releaseConfig['single_locale_options'] = {
    'android': [
        '--cfg',
        'single_locale/release_mozilla-release_android.py',
        '--tag-override', '%s_RELEASE' % releaseConfig['baseTag'],
    ],
}

releaseConfig['multilocale_config'] = {
    'platforms': {
        'android':
            'multi_locale/release_mozilla-release_android.json',
        'android-armv6':
            'multi_locale/release_mozilla-release_android-armv6.json',
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
releaseConfig['autoGenerateChecksums'] = False
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('android','android-armv6','linux')