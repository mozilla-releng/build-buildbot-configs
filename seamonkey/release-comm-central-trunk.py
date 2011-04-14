hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-2.0' # buildbot branch name
sourceRepoPath             = 'comm-central'
sourceRepoRevision         = 'a842a749a221'
relbranchOverride          = 'COMM20_20110405_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-2.0'
mozillaRepoRevision        = '08724a0335a3'
mozillaRelbranchOverride   = 'COMM20_20110405_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = 'fcfb387360fd'
inspectorRelbranchOverride = 'COMM20_20110405_RELBRANCH'
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = '9126bebdf047'
venkmanRelbranchOverride   = 'COMM20_20110405_RELBRANCH'
chatzillaRepoPath          = 'chatzilla' # leave empty if chatzilla is not to be tagged
chatzillaRepoRevision      = '29d3c6d2a751'
chatzillaRelbranchOverride = 'COMM20_20110405_RELBRANCH'
l10nRepoPath               = 'releases/l10n-mozilla-2.0'
l10nRevisionFile           = 'l10n-changesets_comm_central_trunk'
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
version                    = '2.1b3'
appVersion                 = version
milestone                  = '2.0'
buildNumber                = 3
baseTag                    = 'SEAMONKEY_2_1b3'
oldVersion                 = '2.1b2'
oldAppVersion              = oldVersion
oldBuildNumber             = 2
oldBaseTag                 = 'SEAMONKEY_2_1b2'
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
