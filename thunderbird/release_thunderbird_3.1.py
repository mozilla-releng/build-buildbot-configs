hgUsername                 = 'tbirdbld'
hgSshKey                   = '~cltbld/.ssh/tbirdbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.2' # buildbot branch name
sourceRepoPath             = 'comm-central'
sourceRepoRevision         = '0d8aabd78c66'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
relbranchOverride          = 'COMM192_20100119_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-1.9.2'
mozillaRepoRevision        = '818851040d95'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
mozillaRelbranchOverride   = 'COMM192_20100119_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = ''
inspectorRelbranchOverride = 'COMM192_20100119_RELBRANCH'
venkmanRepoPath            = '' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = ''
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ''
chatzillaTimestamp         = '' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n-mozilla-1.9.2'
l10nRevisionFile           = 'l10n-thunderbird-changesets-3.1'
toolsRepoPath              = 'build/tools'
cvsroot                    = ':ext:cltbld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'mail/config/version-192.txt'
productName                = 'thunderbird'
brandName                  = 'Lanikai'
appName                    = 'mail'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '3.1a1'
appVersion                 = version
#XXX: Not entirely certain if/where this is used.
milestone                  = '1.9.2'
buildNumber                = 2
baseTag                    = 'THUNDERBIRD_3_1_a1'
# The old version is the revision from which we should generate update snippets.
oldVersion                 = ''
oldAppVersion              = ''
oldBuildNumber             = 1
oldBaseTag                 = ''
releasePlatforms           = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz192-thunderbird-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2.mozillamessaging.com'
useBetaChannel             = 0
verifyConfigs              = {'linux':  'moz192-thunderbird-linux.cfg',
                              'macosx': 'moz192-thunderbird-mac.cfg',
                              'win32':  'moz192-thunderbird-win32.cfg'}
