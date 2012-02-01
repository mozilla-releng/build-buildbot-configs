releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com',]
releaseConfig['ImportantRecipients'] = ['release@mozilla.com',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[staging-release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'fennec'
releaseConfig['appName']             = 'mobile'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
releaseConfig['relbranchPrefix']     = 'MOBILE'
#  Current version info
releaseConfig['version']             = '11.0b1'
releaseConfig['appVersion']          = '11.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FENNEC_11_0b1'
#  Old version info
releaseConfig['oldVersion']          = '10.0b6'
releaseConfig['oldAppVersion']       = '10.0'
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'FENNEC_10_0b6'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mobile': {
        'name': 'mozilla-beta',
        'clonePath': 'releases/mozilla-beta',
        'path': 'users/stage-ffxbld/mozilla-beta',
        'revision': 'default:',
        'relbranch': None,
        'bumpFiles': {
            'mobile/android/confvars.sh': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'mobile/xul/confvars.sh': {
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
releaseConfig['l10nRepoClonePath']   = 'releases/l10n/mozilla-beta'
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mobile-beta.json'
releaseConfig['l10nJsonFile'] = releaseConfig['l10nRevisionFile']
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_AUTOMATION',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/partner-repacks': 'default',
    'users/stage-ffxbld/mozharness': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']        = ('android', 'android-xul')
releaseConfig['notifyPlatforms']       = ('android',)
releaseConfig['signedPlatforms']      = releaseConfig['enUSPlatforms']
releaseConfig['unittestPlatforms']    = ()
releaseConfig['talosTestPlatforms']   = ()
releaseConfig['enableUnittests']      = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['l10nChunks']          = 2
releaseConfig['mergeLocales']        = True
releaseConfig['enableMultiLocale']   = True

# Mercurial account
releaseConfig['hgUsername']          = 'stage-ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'dev-stage01.build.sjc1.mozilla.com'
releaseConfig['stagingServer']       = 'dev-stage01.build.sjc1.mozilla.com'
releaseConfig['ausServerUrl']        = 'http://dev-stage01.build.sjc1.mozilla.com'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'

# Partner repack configuration
releaseConfig['doPartnerRepacks']       = False
releaseConfig['partnersRepoPath']       = 'users/stage-ffxbld/partner-repacks'
releaseConfig['partnerRepackPlatforms'] = ()

# mozconfigs
releaseConfig['mozconfigs']          = {
    'android': 'mobile/android/config/mozconfigs/android/release',
    'android-xul': 'mobile/xul/config/mozconfigs/android/release',
}

# Misc configuration
releaseConfig['enable_repo_setup']       = False

releaseConfig['mozharness_config'] = {
    'platforms': {
        'android':
            'multi_locale/staging_release_mozilla-beta_android.json',
        'android-xul':
            'multi_locale/staging_release_mozilla-beta_android-xul.json',
    },
    'multilocaleOptions': [
        '--tag-override=%s_RELEASE' % releaseConfig['baseTag'],
        '--user-repo-override=users/stage-ffxbld',
        '--only-pull-locale-source',
        '--only-add-locales',
        '--only-package-multi',
    ]
}
releaseConfig['usePrettyNames']           = False
releaseConfig['disableBouncerEntries']    = True
releaseConfig['disableStandaloneRepacks'] = True
releaseConfig['disableL10nVerification']  = True
releaseConfig['disablePermissionCheck']   = True
releaseConfig['disableVirusCheck']        = True
releaseConfig['disablePushToMirrors']     = True


# Staging config
releaseConfig['build_tools_repo_path'] = "users/stage-ffxbld/tools"
releaseConfig['skip_release_download'] = True
releaseConfig['enableSigningAtBuildTime'] = False
releaseConfig['enablePartialMarsAtBuildTime'] = False
