hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.1' # buildbot branch name
sourceRepoPath             = 'comm-central'
sourceRepoRevision         = 'e9f0d3cb9180'
relbranchOverride          = ''
mozillaRepoPath            = 'releases/mozilla-1.9.1'
mozillaRepoRevision        = 'f2eb72702e5b'
mozillaRelbranchOverride   = 'GECKO1914_20091006_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = 'f1fc2297e2c5'
inspectorRelbranchOverride = ''
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = '7d45be8a1900'
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ':ext:seabld@cvs.mozilla.org:/cvsroot'
chatzillaTimestamp         = '2009-10-07 00:00' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n-mozilla-1.9.1'
l10nRevisionFile           = 'l10n-changesets'
toolsRepoPath              = 'build/tools'
cvsroot                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'suite/config/version-191.txt'
productName                = 'seamonkey'
brandName                  = 'SeaMonkey'
appName                    = 'suite'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '2.0rc1'
appVersion                 = '2.0'
milestone                  = '1.9.1.4'
buildNumber                = 1
baseTag                    = 'SEAMONKEY_2_0rc1'
oldVersion                 = '2.0b2'
oldAppVersion              = oldVersion
oldBuildNumber             = 1
oldBaseTag                 = 'SEAMONKEY_2_0b2'
releasePlatforms           = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz191-seamonkey-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2-community.mozilla.org'
useBetaChannel             = 0
verifyConfigs              = {'linux':  'moz191-seamonkey-linux.cfg',
                              'macosx': 'moz191-seamonkey-mac.cfg',
                              'win32':  'moz191-seamonkey-win32.cfg'}
