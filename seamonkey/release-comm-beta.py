hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-beta' # buildbot branch name
sourceRepoPath             = 'releases/comm-beta'
sourceRepoRevision         = 'e12265030c2e'
relbranchOverride          = 'COMM50_20110626_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-beta'
mozillaRepoRevision        = '3fb6ad7c725e'
mozillaRelbranchOverride   = 'COMM50_20110626_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = '697016a1e944'
inspectorRelbranchOverride = 'COMM50_20110626_RELBRANCH'
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = '5e7659a617fa'
venkmanRelbranchOverride   = 'COMM50_20110626_RELBRANCH'
chatzillaRepoPath          = 'chatzilla' # leave empty if chatzilla is not to be tagged
chatzillaRepoRevision      = '5a0e370d6cf4'
chatzillaRelbranchOverride = 'COMM50_20110626_RELBRANCH'
l10nRepoPath               = 'releases/l10n/mozilla-beta'
l10nRelbranchOverride      = 'COMM50_20110626_RELBRANCH'
l10nRevisionFile           = 'l10n-changesets-comm-beta'
cvsroot                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
#productVersionFile         = 'suite/config/version-20.txt'
productVersionFile         = ''
# mergeLocales allows missing localized strings to be filled in by their en-US
# equivalent string. This is on (True) by default for nightly builds, but
# should be False for releases *EXCEPT* alphas and early betas. If in doubt,
# ask release-drivers.
mergeLocales               = True
productName                = 'seamonkey'
brandName                  = 'SeaMonkey'
appName                    = 'suite'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '2.2b2'
usePrettyLongVer           = False
appVersion                 = '2.2'
milestone                  = '5.0'
buildNumber                = 2
baseTag                    = 'SEAMONKEY_2_2b2'
oldVersion                 = '2.2b1'
oldAppVersion              = 2.2
oldBuildNumber             = 2
oldBaseTag                 = 'SEAMONKEY_2_2b1'
oldRepoPath                = 'releases/comm-beta'
enUSPlatforms              = ('linux', 'linux64', 'win32', 'macosx64')
l10nPlatforms              = ('linux', 'win32', 'macosx64')
patcherConfig              = 'mozBeta-seamonkey-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R14'
binaryName                 = brandName
oldBinaryName              = binaryName
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
talosTestPlatforms         = ()
unittestPlatforms          = ()
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2-community.mozilla.org'
testOlderPartials          = False
releaseNotesUrl            = None
useBetaChannel             = 0
verifyConfigs              = {'linux':  'mozBeta-seamonkey-linux.cfg',
                              'macosx64': 'mozBeta-seamonkey-mac64.cfg',
                              'win32':  'mozBeta-seamonkey-win32.cfg'}
majorUpdateRepoPath        = None
# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#tuxedoConfig        = 'seamonkey-tuxedo.ini'
#tuxedoServerUrl     = 'https://bounceradmin.mozilla.com/api/'
