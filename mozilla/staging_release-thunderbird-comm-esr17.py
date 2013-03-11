# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
EMAIL_RECIPIENTS = []

releaseConfig = {}
releaseConfig['skip_repo_setup']        = True
releaseConfig['disable_tinderbox_mail'] = True
releaseConfig['base_clobber_url'] = 'http://clobberer-stage.pvt.build.mozilla.org/always_clobber.php'

# Release Notification
releaseConfig['AllRecipients']       = EMAIL_RECIPIENTS
releaseConfig['ImportantRecipients'] = EMAIL_RECIPIENTS
releaseConfig['AVVendorsRecipients'] = EMAIL_RECIPIENTS
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[staging-release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'thunderbird'
releaseConfig['appName']             = 'mail'
releaseConfig['mozilla_dir']         = 'mozilla'
#  Current version info
releaseConfig['version']             = '17.0esr'
releaseConfig['appVersion']          = '17.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'THUNDERBIRD_17_0esr'
releaseConfig['partialUpdates']      = {}  # TODO for 17.0.1esr
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
## Staging repository path
releaseConfig['userRepoRoot'] = 'users/stage-ffxbld'
releaseConfig['sourceRepositories']  = {
    'comm': {
        'name': 'comm-esr17',
        'clonePath': 'releases/comm-esr17',
        'path': 'users/stage-ffxbld/comm-esr17',
        'revision': 'default',
        'relbranch': None,
        'bumpFiles': {
            'mail/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
        }
    },
    'mozilla': {
        'name': 'mozilla-esr17',
        'clonePath': 'releases/mozilla-esr17',
        'path': 'users/stage-ffxbld/mozilla-esr17',
        'revision': 'default',
        'relbranch': None,
        'bumpFiles': {
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
releaseConfig['l10nRepoClonePath']   = 'releases/l10n/mozilla-release'
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_thunderbird-esr17'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_0_9_5',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/partner-repacks': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['xulrunnerPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests'] = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'mail/locales/shipped-locales'
releaseConfig['l10nChunks']          = 2
releaseConfig['mergeLocales']        = True

# Mercurial account
releaseConfig['hgUsername']          = 'stage-ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['patcherConfig']       = 'mozEsr17-thunderbird-branch-patcher2.cfg'  # TODO for 17.0.1esr
releaseConfig['ftpServer']           = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['stagingServer']       = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['previousReleasesStagingServer'] = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'http://dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausHost']             = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausUser']             = 'tbirdbld'
releaseConfig['ausSshKey']           = 'tbirdbld_dsa'
releaseConfig['releaseNotesUrl']     = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
releaseConfig['testOlderPartials']   = False
releaseConfig['verifyConfigs']       = {}  # TODO for 17.0.1esr
releaseConfig['mozconfigs']          = {
    'linux': 'mail/config/mozconfigs/linux32/esr',
    'linux64': 'mail/config/mozconfigs/linux64/esr',
    'macosx64': 'mail/config/mozconfigs/macosx-universal/esr',
    'win32': 'mail/config/mozconfigs/win32/esr',
}
releaseConfig['releaseChannel']      = 'esr'

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'users/stage-ffxbld/partner-repacks'

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://tuxedo.stage.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['build_tools_repo_path'] = "users/stage-ffxbld/tools"
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux', 'linux64')
releaseConfig['ftpSymlinkName'] = 'latest-esr'
