hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.1' # buildbot branch name
sourceRepoPath             = 'comm-central'
sourceRepoRevision         = '48147c4781e9'
relbranchOverride          = ''
mozillaRepoPath            = 'releases/mozilla-1.9.1'
mozillaRepoRevision        = '1e7c406956d3'
#mozillaRelbranchOverride   = 'GECKO191_20090616_RELBRANCH' # put Gecko relbranch here that we base upon
mozillaRelbranchOverride   = ''
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = 'ef29512d86ae'
inspectorRelbranchOverride = ''
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = '06ea5135b7f3'
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ':ext:seabld@cvs.mozilla.org:/cvsroot'
chatzillaTimestamp         = '2009-07-16 00:00' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n-mozilla-1.9.1'
l10nRevisionFile           = 'l10n-changesets'
#toolsRepoPath              = 'build/tools'
toolsRepoPath              = 'users/seabld/tools'
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
version                    = '2.0b1'
appVersion                 = version
milestone                  = '1.9.1.1'
buildNumber                = 1
baseTag                    = 'SEAMONKEY_2_0b1'
oldVersion                 = '2.0a3'
oldAppVersion              = oldVersion
oldBuildNumber             = 2
oldBaseTag                 = 'SEAMONKEY_2_0a3'
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
