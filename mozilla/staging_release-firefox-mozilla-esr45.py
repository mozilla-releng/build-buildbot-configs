# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
EMAIL_RECIPIENTS = []

releaseConfig = {}
releaseConfig['base_clobber_url'] = 'https://api-pub-build.allizom.org/clobberer/forceclobber'

# Release Notification
releaseConfig['AllRecipients']       = EMAIL_RECIPIENTS
releaseConfig['ImportantRecipients'] = EMAIL_RECIPIENTS
releaseConfig['AVVendorsRecipients'] = EMAIL_RECIPIENTS
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[staging-release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['stage_product']       = 'firefox'
releaseConfig['appName']             = 'browser'
#  Current version info
releaseConfig['version']             = '38.0esr'
releaseConfig['appVersion']          = '38.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_38_0esr'
releaseConfig['partialUpdates']      = {}
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '{{ version }}pre'
releaseConfig['nextMilestone']       = releaseConfig['nextAppVersion']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-esr45',
        'path': 'users/stage-ffxbld/mozilla-esr45',
        'revision': 'default',
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
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-esr45'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_0_9_5',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/partner-repacks': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = True

# Mercurial account
releaseConfig['hgUsername']          = 'stage-ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_rsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'ftp.stage.mozaws.net'
releaseConfig['stagingServer']       = 'upload.ffxbld.productdelivery.stage.mozaws.net'
releaseConfig['previousReleasesStagingServer'] = 'archive.mozilla.org'
releaseConfig['S3Credentials']       = '/builds/release-s3.credentials'
releaseConfig['S3Bucket']            = 'net-mozaws-stage-delivery-firefox'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus4-dev.allizom.org'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = False
releaseConfig['releaseChannel']      = 'esr'
releaseConfig['updateChannels'] = {
    # ruleId needs to be updated with the ID from AUS
    "esr": {
        "versionRegex": r"^.*$",
        "ruleId": "esr45-dev",
        "patcherConfig": "mozEsr45-branch-patcher2.cfg",
        "localTestChannel": "esr-localtest",
        "cdnTestChannel": "esr-cdntest",
        "verifyConfigs": {
            "linux":  "mozEsr45-firefox-linux.cfg",
            "linux64":  "mozEsr45-firefox-linux64.cfg",
            "macosx64": "mozEsr45-firefox-mac64.cfg",
            "win32":  "mozEsr45-firefox-win32.cfg",
        },
        "testChannels": {
            "esr-cdntest": {
                "ruleId": "esr45-cdntest-dev",
            },
            "esr-localtest": {
                "ruleId": "esr45-localtest-dev",
            },
        }
    }
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'users/stage-ffxbld/partner-repacks'

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://admin-bouncer.stage.mozaws.net/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_firefox_esr.py'

# Misc configuration
releaseConfig['build_tools_repo_path'] = "users/stage-ffxbld/tools"
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
