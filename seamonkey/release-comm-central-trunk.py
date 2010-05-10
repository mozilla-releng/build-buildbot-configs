hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-central-trunk' # buildbot branch name
sourceRepoPath             = 'comm-central'
sourceRepoRevision         = 'e9d005c309d8'
relbranchOverride          = ''
mozillaRepoPath            = 'mozilla-central'
mozillaRepoRevision        = '6d517fe3d7ae'
mozillaRelbranchOverride   = '' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = '27b0e9ef1715'
inspectorRelbranchOverride = ''
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = '05ab405b963d'
venkmanRelbranchOverride   = ''
chatzillaRepoPath          = 'chatzilla' # leave empty if chatzilla is not to be tagged
chatzillaRepoRevision      = 'b774ffc606f0'
chatzillaRelbranchOverride = ''
l10nRepoPath               = 'l10n-central'
l10nRevisionFile           = 'l10n-changesets'
cvsroot                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'suite/config/version.txt'
productName                = 'seamonkey'
brandName                  = 'SeaMonkey'
appName                    = 'suite'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '2.1a1'
appVersion                 = version
milestone                  = '1.9.3a4'
buildNumber                = 1
baseTag                    = 'SEAMONKEY_2_1a1'
oldVersion                 = ''
oldAppVersion              = oldVersion
oldBuildNumber             = 1
oldBaseTag                 = ''
enUSPlatforms              = ('linux', 'linux64', 'win32', 'macosx')
l10nPlatforms              = ()
# TODO: create this file before 2.1a2
patcherConfig              = 'moz193-seamonkey-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
talosTestPlatforms         = ()
unittestPlatforms          = ()
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2-community.mozilla.org'
releaseNotesUrl            = None
useBetaChannel             = 1
# TODO: create these files before first 2.1 requiring updates
verifyConfigs              = {'linux':  'moz193-seamonkey-linux.cfg',
                              'macosx': 'moz193-seamonkey-mac.cfg',
                              'win32':  'moz193-seamonkey-win32.cfg'}
majorUpdateRepoPath        = None
