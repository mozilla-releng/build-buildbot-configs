hgUsername         = 'ffxbld'
hgSshKey           = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName     = 'mozilla-1.9.1'
sourceRepoPath     = 'releases/mozilla-1.9.1'
sourceRepoRevision = 'c204f7bb0064'
relbranchOverride  = 'GECKO1914_20091006_RELBRANCH'
l10nRepoPath       = 'releases/l10n-mozilla-1.9.1'
l10nRevisionFile   = 'l10n-changesets'
cvsroot            = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
productName        = 'firefox'
appName            = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version            = '3.5.5'
appVersion         = version
milestone          = '1.9.1.5'
buildNumber        = 1
baseTag            = 'FIREFOX_3_5_5'
oldVersion         = '3.5.4'
oldAppVersion      = oldVersion
oldBuildNumber     = 3
oldBaseTag         = 'FIREFOX_3_5_4'
enUSPlatforms      = ('linux', 'win32', 'macosx')
l10nPlatforms      = enUSPlatforms
patcherConfig      = 'moz191-branch-patcher2.cfg'
patcherToolsTag    = 'UPDATE_PACKAGING_R9'
ftpServer          = 'ftp.mozilla.org'
stagingServer      = 'stage-old.mozilla.org'
bouncerServer      = 'download.mozilla.org'
ausServerUrl       = 'https://aus2.mozilla.org'
useBetaChannel     = 1
verifyConfigs      = {'linux':  'moz191-firefox-linux.cfg',
                      'macosx': 'moz191-firefox-mac.cfg',
                      'win32':  'moz191-firefox-win32.cfg'}
