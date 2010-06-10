hgUsername         = 'ffxbld'
hgSshKey           = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName     = 'mozilla-1.9.2'
sourceRepoPath     = 'releases/mozilla-1.9.2'
sourceRepoRevision = '41807e6bcb14'
relbranchOverride  = 'GECKO1924_20100413_RELBRANCH'
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
version            = '3.6.4'
appVersion         = version 
milestone          = '1.9.2.4'
buildNumber        = 6
baseTag            = 'FIREFOX_3_6_4'
oldVersion         = '3.6.3'
oldAppVersion      = '3.6.3'
oldBuildNumber     = 1
oldBaseTag         = 'FIREFOX_3_6_3'
enUSPlatforms      = ('linux', 'win32', 'macosx')
l10nPlatforms      = ('linux', 'win32', 'macosx')
talosTestPlatforms = ('linux', 'win32', 'macosx')
unittestPlatforms  = ('linux', 'win32', 'macosx')
xulrunnerPlatforms = enUSPlatforms
patcherConfig      = 'moz192-branch-patcher2.cfg'
patcherToolsTag    = 'UPDATE_PACKAGING_R11'
binaryName         = productName.capitalize()
oldBinaryName      = binaryName
ftpServer          = 'ftp.mozilla.org'
stagingServer      = 'stage-old.mozilla.org'
bouncerServer      = 'download.mozilla.org'
ausServerUrl       = 'https://aus2.mozilla.org'
ausUser            = 'cltbld'
ausSshKey          = 'cltbld_dsa'
releaseNotesUrl    = None
useBetaChannel     = 1
verifyConfigs      = {'linux':  'moz192-firefox-linux.cfg',
                      'macosx': 'moz192-firefox-mac.cfg',
                      'win32':  'moz192-firefox-win32.cfg'}
doPartnerRepacks    = True
partnersRepoPath    = 'build/partner-repacks'
majorUpdateRepoPath = None
# Tuxedo/Bouncer related
tuxedoConfig        = 'firefox-tuxedo.ini'
tuxedoServerUrl     = 'https://bounceradmin.mozilla.com/api/'
