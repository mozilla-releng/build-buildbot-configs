releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com','akeybl@mozilla.com','Callek@gmail.com']
releaseConfig['ImportantRecipients'] = ['release-drivers@mozilla.org',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'fennec'
releaseConfig['appName']             = 'mobile'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
releaseConfig['relbranchPrefix']     = 'MOBILE'
#  Current version info
releaseConfig['version']             = '10.0.3esr'
releaseConfig['appVersion']          = '10.0.3'
releaseConfig['milestone']           = '10.0.3'
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FENNEC_10_0_3esr'
#  Old version info
releaseConfig['oldVersion']          = '10.0.2esr'
releaseConfig['oldAppVersion']       = '10.0.2'
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'FENNEC_10_0_2esr'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '10.0.4esrpre'
releaseConfig['nextMilestone']       = '10.0.4esrpre'
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mobile': {
        'name': 'mozilla-esr10',
        'path': 'releases/mozilla-esr10',
        'revision': '039e4d5bb2ce',
        'relbranch': None,
        'bumpFiles': {
            'mobile/confvars.sh': {
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
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mobile-esr10.json'
releaseConfig['l10nJsonFile']        = releaseConfig['l10nRevisionFile']
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_0_8_2',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
    'build/mozharness': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']        = ('linux-android',)
releaseConfig['notifyPlatforms']      = ('linux-android',)
releaseConfig['signedPlatforms']      = ('linux-android',)
releaseConfig['unittestPlatforms']    = ()
releaseConfig['talosTestPlatforms']   = ()
releaseConfig['enableUnittests']      = True

# L10n configuration
releaseConfig['l10nPlatforms']       = ()
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = True
releaseConfig['enableMultiLocale']   = True

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus2.mozilla.org'
releaseConfig['ausHost']             = 'aus2-staging.mozilla.org'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'

# Partner repack configuration
releaseConfig['doPartnerRepacks']       = True
releaseConfig['partnersRepoPath']       = 'build/partner-repacks'
releaseConfig['partnerRepackPlatforms'] = ()

# mozconfigs
releaseConfig['mozconfigs']          = {
    'linux-android': 'mobile/config/mozconfigs/android/release',
}

# Misc configuration
releaseConfig['enable_repo_setup']       = False

# Fennec specific
releaseConfig['usePrettyNames']           = False
releaseConfig['disableBouncerEntries']    = True
releaseConfig['disableStandaloneRepacks'] = True
releaseConfig['disableL10nVerification']  = True
releaseConfig['disablePermissionCheck']   = True
releaseConfig['disableVirusCheck']        = True
releaseConfig['disablePushToMirrors']     = True

releaseConfig['multilocale_config'] = {
    'platforms': {
        'linux-android':
            'multi_locale/release_mozilla-release_linux-android.json',
    },
    'multilocaleOptions': [
        '--tag-override=%s_RELEASE' % releaseConfig['baseTag'],
        '--only-pull-locale-source',
        '--only-add-locales',
        '--only-package-multi',
    ]
}
releaseConfig['enableSigningAtBuildTime'] = False
releaseConfig['enablePartialMarsAtBuildTime'] = False
