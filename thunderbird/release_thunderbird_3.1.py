hgUsername                 = 'tbirdbld'
hgSshKey                   = '~cltbld/.ssh/tbirdbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.2' # buildbot branch name
sourceRepoPath             = 'releases/comm-1.9.2'
sourceRepoRevision         = '01ddbab92467'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
relbranchOverride          = 'COMM1927_20100701_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-1.9.2'
mozillaRepoRevision        = '2502e5ae6981'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
mozillaRelbranchOverride   = 'GECKO1927_20100701_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = 'c1b38e365772'
inspectorRelbranchOverride = 'COMM1924_20100519_RELBRANCH'
buildToolsRepoPath            = '' # leave empty if buildTools is not to be tagged
buildToolsRepoRevision        = ''
#buildToolsRepoRevision        = '479375734669'
buildToolsRelbranchOverride   = ''
venkmanRepoPath            = '' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = ''
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ''
chatzillaTimestamp         = '' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n-mozilla-1.9.2'
l10nRevisionFile           = 'l10n-thunderbird-changesets-3.1'
toolsRepoPath              = 'build/tools'
buildToolsRepoPath	   = ''
cvsroot                    = ':ext:cltbld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'mail/config/version-192.txt'
productName                = 'thunderbird'
brandName                  = 'Thunderbird'
appName                    = 'mail'
ftpName                    = appName
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '3.1.1'
appVersion                 = '3.1.1'
#XXX: Not entirely certain if/where this is used.
milestone                  = '1.9.2.7'
buildNumber                = 2
baseTag                    = 'THUNDERBIRD_3_1_1'
# The old version is the revision from which we should generate update snippets.
oldVersion                 = '3.1rc2'
oldAppVersion              = '3.1'
oldBuildNumber             = 1
oldBaseTag                 = 'THUNDERBIRD_3_1_rc2'
releasePlatforms           = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz192-thunderbird-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R11'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2.mozillamessaging.com'
useBetaChannel             = 1
l10nPlatforms              = ['linux', 'macosx', 'win32' ]
verifyConfigs              = {'linux':  'moz192-thunderbird-linux.cfg',
                              'macosx': 'moz192-thunderbird-mac.cfg',
                              'win32':  'moz192-thunderbird-win32.cfg'}
