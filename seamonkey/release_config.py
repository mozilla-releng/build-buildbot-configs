hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.1' # buildbot branch name
sourceRepoPath             = 'releases/comm-1.9.1'
sourceRepoRevision         = 'ff366121a9c3'
relbranchOverride          = 'COMM1916_20091204_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-1.9.1'
mozillaRepoRevision        = 'FIREFOX_3_5_7_RELEASE'
mozillaRelbranchOverride   = 'GECKO1916_20091130_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = 'SEAMONKEY_2_0_RELEASE'
inspectorRelbranchOverride = 'COMM1914_20091014_RELBRANCH'
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = 'SEAMONKEY_2_0_RELEASE'
venkmanRelbranchOverride   = 'COMM1914_20091014_RELBRANCH'
chatzillaCVSRoot           = ':ext:seabld@cvs.mozilla.org:/cvsroot'
chatzillaTimestamp         = '2009-10-14 00:00' # leave empty if chatzilla is not to be tagged
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
version                    = '2.0.2'
appVersion                 = version
milestone                  = '1.9.1.7'
buildNumber                = 1
baseTag                    = 'SEAMONKEY_2_0_2'
oldVersion                 = '2.0.1'
oldAppVersion              = oldVersion
oldBuildNumber             = 2
oldBaseTag                 = 'SEAMONKEY_2_0_1'
releasePlatforms           = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz191-seamonkey-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2-community.mozilla.org'
useBetaChannel             = 1
verifyConfigs              = {'linux':  'moz191-seamonkey-linux.cfg',
                              'macosx': 'moz191-seamonkey-mac.cfg',
                              'win32':  'moz191-seamonkey-win32.cfg'}
