hgUsername         = 'ffxbld'
hgSshKey           = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName     = 'mozilla-1.9.2'
sourceRepoPath     = 'releases/mozilla-1.9.2'
sourceRepoRevision = '448d0d2d310c'
relbranchOverride  = 'GECKO192_20100105_RELBRANCH'
l10nRepoPath       = 'releases/l10n-mozilla-1.9.2'
l10nRevisionFile   = 'l10n-changesets_mozilla-1.9.2'
cvsroot            = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
productName        = 'firefox'
appName            = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version            = '3.6rc2'
appVersion         = '3.6'
milestone          = '1.9.2'
buildNumber        = 1
baseTag            = 'FIREFOX_3_6rc2'
oldVersion         = '3.6rc1'
oldAppVersion      = '3.6'
oldBuildNumber     = 1
oldBaseTag         = 'FIREFOX_3_6rc1'
enUSPlatforms      = ('linux', 'win32', 'macosx', 'wince')
l10nPlatforms      = ('linux', 'win32', 'macosx')
patcherConfig      = 'moz192-branch-patcher2.cfg'
patcherToolsTag    = 'UPDATE_PACKAGING_R10'
ftpServer          = 'ftp.mozilla.org'
stagingServer      = 'stage-old.mozilla.org'
bouncerServer      = 'download.mozilla.org'
talosTestPlatforms = ('linux', 'win32', 'macosx')
unittestPlatforms  = ('linux', 'win32', 'macosx')
ausServerUrl       = 'https://aus2.mozilla.org'
useBetaChannel     = 0
verifyConfigs      = {'linux':  'moz192-firefox-linux.cfg',
                      'macosx': 'moz192-firefox-mac.cfg',
                      'win32':  'moz192-firefox-win32.cfg'}
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
