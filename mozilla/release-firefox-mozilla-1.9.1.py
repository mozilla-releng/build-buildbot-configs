releaseConfig = {}

releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'
releaseConfig['sourceRepoName']      = 'mozilla-1.9.1'
releaseConfig['sourceRepoPath']      = 'releases/mozilla-1.9.1'
releaseConfig['sourceRepoRevision']  = '612ad84a4004'
releaseConfig['relbranchOverride']   = 'GECKO19116_20101122_RELBRANCH'
releaseConfig['l10nRepoPath']        = 'releases/l10n-mozilla-1.9.1'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-1.9.1'
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6 
releaseConfig['mergeLocales']        = False
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION'
}
releaseConfig['cvsroot']             = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
releaseConfig['productName']         = 'firefox'
releaseConfig['appName']             = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
releaseConfig['version']             = '3.5.16'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '1.9.1.16'
releaseConfig['buildNumber']         = 2
releaseConfig['baseTag']             = 'FIREFOX_3_5_16'
releaseConfig['oldVersion']          = '3.5.15'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'FIREFOX_3_5_15'
releaseConfig['enUSPlatforms']       = ('linux', 'win32', 'macosx')
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['unittestPlatforms']   = ()
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['patcherConfig']       = 'moz191-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R11'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage-old.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus2.mozilla.org'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = True
releaseConfig['useBetaChannel']      = 1
releaseConfig['verifyConfigs']       = {
    'linux':  'moz191-firefox-linux.cfg',
    'macosx': 'moz191-firefox-mac.cfg',
    'win32':  'moz191-firefox-win32.cfg'
}
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'
releaseConfig['majorUpdateRepoPath'] = 'releases/mozilla-1.9.2'
releaseConfig['majorUpdateToVersion']   = '3.6.13'
releaseConfig['majorUpdateAppVersion']  = releaseConfig['majorUpdateToVersion']
releaseConfig['majorUpdateBuildNumber'] = 3
releaseConfig['majorUpdateBaseTag']     = 'FIREFOX_3_6_13'
releaseConfig['majorUpdateReleaseNotesUrl']  = 'http://www.mozilla.com/%locale%/firefox/3.6/details/index.html'
releaseConfig['majorUpdatePatcherConfig']    = 'moz191-branch-major-update-patcher2.cfg'
releaseConfig['majorUpdateVerifyConfigs']    = {
    'linux':  'moz191-firefox-linux-major.cfg',
    'macosx': 'moz191-firefox-mac-major.cfg',
    'win32':  'moz191-firefox-win32-major.cfg'
}
# Tuxedo/Bouncer related
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api/'
# Release Notification configuration
releaseConfig['AllRecipients']       = ['release@mozilla.com',]
releaseConfig['PassRecipients']      = ['release@mozilla.com',]
releaseConfig['releaseTemplates']    = 'release_templates'

