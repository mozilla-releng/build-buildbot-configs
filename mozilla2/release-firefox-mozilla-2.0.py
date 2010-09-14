hgUsername         = 'ffxbld'
hgSshKey           = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName     = 'mozilla-central'
sourceRepoPath     = sourceRepoName
sourceRepoRevision = '633e895d5e84'
relbranchOverride  = 'GECKO20b5_20100831_RELBRANCH'
l10nRepoPath       = 'l10n-central'
l10nRevisionFile   = 'l10n-changesets_mozilla-2.0'
# mergeLocales allows missing localized strings to be filled in by their en-US
# equivalent string. This is on (True) by default for nightly builds, but
# should be False for releases *EXCEPT* alphas and early betas. If in doubt,
# ask release-drivers.
mergeLocales       = True
cvsroot            = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
productName        = 'firefox'
appName            = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version            = '4.0b6'
appVersion         = version
# NB: this will become 2.0.x not 2.0.0.x, bug 577875
milestone          = '2.0b6'
buildNumber        = 2
baseTag            = 'FIREFOX_4_0b6'
oldVersion         = '4.0b5'
oldAppVersion      = oldVersion
oldBuildNumber     = 1
oldBaseTag         = 'FIREFOX_4_0b5'
enUSPlatforms      = ('linux', 'linux64', 'win32', 'macosx', 'macosx64')
l10nPlatforms      = enUSPlatforms
xulrunnerPlatforms = ()
patcherConfig      = 'moz20-branch-patcher2.cfg'
patcherToolsTag    = 'UPDATE_PACKAGING_R12'
binaryName         = 'Firefox'
oldBinaryName      = binaryName
ftpServer          = 'ftp.mozilla.org'
stagingServer      = 'stage-old.mozilla.org'
talosTestPlatforms = enUSPlatforms
unittestPlatforms  = enUSPlatforms
bouncerServer      = 'download.mozilla.org'
ausServerUrl       = 'https://aus2.mozilla.org'
ausUser            = 'cltbld'
ausSshKey          = 'cltbld_dsa'
testOlderPartials  = False
releaseNotesUrl    = 'http://www.mozilla.com/%locale%/firefox/4.0b6/releasenotes/'
useBetaChannel     = 0
verifyConfigs      = {'linux':    'moz20-firefox-linux.cfg',
                      'linux64':  'moz20-firefox-linux64.cfg',
                      'macosx':   'moz20-firefox-mac.cfg',
                      'macosx64': 'moz20-firefox-mac64.cfg',
                      'win32':    'moz20-firefox-win32.cfg'}
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
majorUpdateRepoPath = None
# Tuxedo/Bouncer related
tuxedoConfig        = 'firefox-tuxedo.ini'
tuxedoServerUrl     = 'https://bounceradmin.mozilla.com/api/'
