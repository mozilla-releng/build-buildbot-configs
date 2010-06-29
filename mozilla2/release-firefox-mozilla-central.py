hgUsername         = 'ffxbld'
hgSshKey           = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName     = 'mozilla-central'
sourceRepoPath     = sourceRepoName
sourceRepoRevision = 'd08120d3792e'
relbranchOverride  = ''
l10nRepoPath       = 'l10n-central'
l10nRevisionFile   = 'l10n-changesets'
cvsroot            = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
productName        = 'firefox'
appName            = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version            = '4.0b1'
appVersion         = version
milestone          = '2.0b1'
buildNumber        = 1
baseTag            = 'FIREFOX_4_0b1'
oldVersion         = '3.7a5'
oldAppVersion      = oldVersion
oldBuildNumber     = 1
oldBaseTag         = 'FIREFOX_3_7a5'
enUSPlatforms      = ('linux', 'linux64', 'win32', 'macosx', 'macosx64')
l10nPlatforms      = ()
xulrunnerPlatforms = ()
patcherConfig      = 'moz193-branch-patcher2.cfg'
patcherToolsTag    = 'UPDATE_PACKAGING_R11'
binaryName         = 'Firefox'
oldBinaryName      = 'MozillaDeveloperPreview'
ftpServer          = 'ftp.mozilla.org'
stagingServer      = 'stage-old.mozilla.org'
talosTestPlatforms = enUSPlatforms
unittestPlatforms  = enUSPlatforms
bouncerServer      = 'download.mozilla.org'
ausServerUrl       = 'https://aus2.mozilla.org'
ausUser            = 'cltbld'
ausSshKey          = 'cltbld_dsa'
releaseNotesUrl    = 'http://www.mozilla.com/firefox/4.0b1/releasenotes'
useBetaChannel     = 0
verifyConfigs       = {'linux':    'moz193-firefox-linux.cfg',
                       'linux64':  'moz193-firefox-linux64.cfg',
                       'macosx':   'moz193-firefox-mac.cfg',
                       'macosx64': 'moz193-firefox-mac64.cfg',
                       'win32':    'moz193-firefox-win32.cfg'}
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
majorUpdateRepoPath = None
# Tuxedo/Bouncer related
tuxedoConfig        = 'firefox-devpreview-tuxedo.ini'
tuxedoServerUrl     = 'https://bounceradmin.mozilla.com/api/'
