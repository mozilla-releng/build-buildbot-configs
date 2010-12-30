releaseConfig = {}

releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'
releaseConfig['sourceRepoName']      = 'mozilla-central'
releaseConfig['sourceRepoPath']      = releaseConfig['sourceRepoName']
releaseConfig['sourceRepoRevision']  = 'abe884259481'
releaseConfig['relbranchOverride']   = ''
releaseConfig['l10nRepoPath']        = 'l10n-central'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-2.0'
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = True
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8'
}
releaseConfig['cvsroot']             = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
releaseConfig['productName']         = 'firefox'
releaseConfig['appName']             = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
releaseConfig['version']             = '4.0b8'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '2.0b8'
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_4_0b8'
releaseConfig['oldVersion']          = '4.0b7'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'FIREFOX_4_0b7'
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['unittestPlatforms']   = releaseConfig['enUSPlatforms']
releaseConfig['xulrunnerPlatforms']  = ()
releaseConfig['patcherConfig']       = 'moz20-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R12'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage-old.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus2.mozilla.org'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = 'http://www.mozilla.com/%locale%/firefox/4.0b8/releasenotes/'
releaseConfig['testOlderPartials']   = False
releaseConfig['useBetaChannel']      = 0
releaseConfig['verifyConfigs']       = {
    'linux':  'moz20-firefox-linux.cfg',
    'linux64':  'moz20-firefox-linux64.cfg',
    'macosx64': 'moz20-firefox-mac64.cfg',
    'win32':  'moz20-firefox-win32.cfg'
}
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'
releaseConfig['majorUpdateRepoPath'] = None
# Tuxedo/Bouncer related
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api/'
# Release Notification configuration
releaseConfig['AllRecipients']       = ['release@mozilla.com',]
releaseConfig['PassRecipients']      = ['release-drivers@mozilla.com',]
releaseConfig['releaseTemplates']    = 'release_templates'

