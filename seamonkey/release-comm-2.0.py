hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-2.0' # buildbot branch name
sourceRepoPath             = 'releases/comm-2.0'
sourceRepoRevision         = '4c1e17da32ec'
relbranchOverride          = 'COMM201_20110508_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-2.0'
mozillaRepoRevision        = 'ac9cf29de0d2'
mozillaRelbranchOverride   = 'GECKO201_2011041321_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = '0bb7db177214'
inspectorRelbranchOverride = 'COMM201_20110508_RELBRANCH'
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = '65c389ee756c'
venkmanRelbranchOverride   = 'COMM201_20110508_RELBRANCH'
chatzillaRepoPath          = 'chatzilla' # leave empty if chatzilla is not to be tagged
chatzillaRepoRevision      = '210002e2b7e7'
chatzillaRelbranchOverride = 'COMM201_20110508_RELBRANCH'
l10nRepoPath               = 'releases/l10n-mozilla-2.0'
l10nRevisionFile           = 'l10n-changesets-comm-2.0'
cvsroot                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'suite/config/version-20.txt'
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
version                    = '2.1rc1'
appVersion                 = '2.1'
milestone                  = '2.0.1'
buildNumber                = 2
baseTag                    = 'SEAMONKEY_2_1rc1'
oldVersion                 = '2.1b3'
oldAppVersion              = oldVersion
oldBuildNumber             = 3
oldBaseTag                 = 'SEAMONKEY_2_1b3'
enUSPlatforms              = ('linux', 'linux64', 'win32', 'macosx64')
l10nPlatforms              = ('linux', 'win32', 'macosx64')
patcherConfig              = 'moz20-seamonkey-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R13'
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
verifyConfigs              = {'linux':  'moz20-seamonkey-linux.cfg',
                              'macosx64': 'moz20-seamonkey-mac.cfg',
                              'win32':  'moz20-seamonkey-win32.cfg'}
majorUpdateRepoPath        = None
# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#tuxedoConfig        = 'seamonkey-tuxedo.ini'
#tuxedoServerUrl     = 'https://bounceradmin.mozilla.com/api/'
