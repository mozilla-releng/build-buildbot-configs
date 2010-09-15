hgUsername                 = 'tbirdbld'
hgSshKey                   = '~cltbld/.ssh/tbirdbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.2' # buildbot branch name
sourceRepoPath             = 'releases/comm-1.9.2'
sourceRepoRevision         = 'da29bc7c880d'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
relbranchOverride          = 'COMM1929_20100825_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-1.9.2'
mozillaRepoRevision        = 'c2b6766f960d'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
mozillaRelbranchOverride   = 'COMM1929_20100825_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = 'c1b38e365772'
inspectorRelbranchOverride = 'COMM1929_20100910_RELBRANCH'
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
version                    = '3.1.4'
appVersion                 = '3.1.4'
#XXX: Not entirely certain if/where this is used.
milestone                  = '1.9.2.9'
buildNumber                = 2
baseTag                    = 'THUNDERBIRD_3_1_4'
# The old version is the revision from which we should generate update snippets.
oldVersion                 = '3.1.3'
oldAppVersion              = '3.1.3'
oldBuildNumber             = 1
oldBaseTag                 = 'THUNDERBIRD_3_1_3'
releasePlatforms           = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz192-thunderbird-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R11'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
releaseNotesUrl            = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
ausServerUrl               = 'https://aus2.mozillamessaging.com'
testOlderPartials          = True
useBetaChannel             = 1
l10nPlatforms              = ['linux', 'macosx', 'win32' ]
verifyConfigs              = {'linux':  'moz192-thunderbird-linux.cfg',
                              'macosx': 'moz192-thunderbird-mac.cfg',
                              'win32':  'moz192-thunderbird-win32.cfg'}
