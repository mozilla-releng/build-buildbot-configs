hgUsername                 = 'seabld'
hgSshKey                   = '~seabld/.ssh/seabld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.1' # buildbot branch name
sourceRepoPath             = 'releases/comm-1.9.1'
sourceRepoRevision         = 'b8e06312e645'
relbranchOverride          = ''
mozillaRepoPath            = 'releases/mozilla-1.9.1'
mozillaRepoRevision        = 'FIREFOX_3_5_9_RELEASE'
mozillaRelbranchOverride   = 'GECKO1919_20100315_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = 'f6c78804ebb4'
inspectorRelbranchOverride = 'COMM_1_9_1_BRANCH'
venkmanRepoPath            = 'venkman' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = 'f13c813e4ec6'
venkmanRelbranchOverride   = 'COMM_1_9_1_BRANCH'
chatzillaRepoPath          = 'chatzilla' # leave empty if chatzilla is not to be tagged
chatzillaRepoRevision      = 'f5fd1b073bf8'
chatzillaRelbranchOverride = 'COMM_1_9_1_BRANCH'
l10nRepoPath               = 'releases/l10n-mozilla-1.9.1'
l10nRevisionFile           = 'l10n-changesets'
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
version                    = '2.0.4'
appVersion                 = version
milestone                  = '1.9.1.9'
buildNumber                = 1
baseTag                    = 'SEAMONKEY_2_0_4'
oldVersion                 = '2.0.3'
oldAppVersion              = oldVersion
oldBuildNumber             = 1
oldBaseTag                 = 'SEAMONKEY_2_0_3'
enUSPlatforms              = ('linux', 'linux64', 'win32', 'macosx')
l10nPlatforms              = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz191-seamonkey-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
talosTestPlatforms         = ()
unittestPlatforms          = ()
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2-community.mozilla.org'
useBetaChannel             = 1
verifyConfigs              = {'linux':  'moz191-seamonkey-linux.cfg',
                              'macosx': 'moz191-seamonkey-mac.cfg',
                              'win32':  'moz191-seamonkey-win32.cfg'}
