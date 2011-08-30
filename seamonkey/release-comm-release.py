hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'SEA_COMM'
sourceRepoName             = 'comm-release' # buildbot branch name
sourceRepoPath             = 'releases/comm-release'
sourceRepoRevision         = '22450ee15399'
relbranchOverride          = 'COMM60_20110820_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-release'
mozillaRepoRevision        = '6176fcd0daf8'
mozillaRelbranchOverride   = 'SEAMONKEY_2_3_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = 'DOMI_2_0_10_RELEASE'
inspectorRelbranchOverride = 'DOMI_2_0_10'
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = '5e7659a617fa'
venkmanRelbranchOverride   = ''
chatzillaRepoPath          = 'chatzilla' # leave empty if chatzilla is not to be tagged
chatzillaRepoRevision      = '144f0c279a3b'
chatzillaRelbranchOverride = ''
l10nRepoPath               = 'releases/l10n/mozilla-release'
l10nRelbranchOverride      = ''
l10nRevisionFile           = 'l10n-changesets-comm-release'
cvsroot                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
#productVersionFile         = 'suite/config/version.txt'
productVersionFile         = ''
# mergeLocales allows missing localized strings to be filled in by their en-US
# equivalent string. This is on (True) by default for nightly builds, but
# should be False for releases *EXCEPT* alphas and early betas. If in doubt,
# ask release-drivers.
mergeLocales               = True
productName                = 'seamonkey'
brandName                  = 'SeaMonkey'
appName                    = 'suite'
skip_tag                   = True
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '2.3.2'
usePrettyLongVer           = False
appVersion                 = '2.3.2'
milestone                  = '6.0.1'
buildNumber                = 1
baseTag                    = 'SEAMONKEY_2_3_2'
oldVersion                 = '2.3.1'
oldAppVersion              = '2.3.1'
oldBuildNumber             = 1
oldBaseTag                 = 'SEAMONKEY_2_3_1'
oldRepoPath                = 'releases/comm-release'
enUSPlatforms              = ('linux', 'linux64', 'win32', 'macosx64')
l10nPlatforms              = ('linux', 'win32', 'macosx64')
patcherConfig              = 'mozRelease-seamonkey-branch-patcher2.cfg'
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
useBetaChannel             = 1
verifyConfigs              = {'linux':  'mozRelease-seamonkey-linux.cfg',
                              'macosx64': 'mozRelease-seamonkey-mac64.cfg',
                              'win32':  'mozRelease-seamonkey-win32.cfg'}
majorUpdateRepoPath        = None
# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#tuxedoConfig        = 'seamonkey-tuxedo.ini'
#tuxedoServerUrl     = 'https://bounceradmin.mozilla.com/api/'
