hgUsername                 = 'tbirdbld'
hgSshKey                   = '~cltbld/.ssh/tbirdbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-central' # buildbot branch name
sourceRepoPath             = 'releases/comm-1.9.1'
sourceRepoRevision         = '0ee60a0ba075'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
relbranchOverride          = 'COMM1915_20091112_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-1.9.1'
mozillaRepoRevision        = '6dc036c10334'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
mozillaRelbranchOverride   = 'COMM1915_20091112_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = '18a1c983c8ee'
inspectorRelbranchOverride = 'COMM1915_20091112_RELBRANCH'
venkmanRepoPath            = '' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = ''
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ''
chatzillaTimestamp         = '' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n-mozilla-1.9.1'
l10nRevisionFile           = 'l10n-thunderbird-changesets'
toolsRepoPath              = 'build/tools'
cvsroot                    = ':ext:cltbld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'mail/config/version-191.txt'
productName                = 'thunderbird'
brandName                  = 'Thunderbird'
appName                    = 'mail'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '3.0rc2'
appVersion                 = '3.0'
#XXX: Not entirely certain if/where this is used.
milestone                  = '1.9.1.5'
buildNumber                = 1
baseTag                    = 'THUNDERBIRD_3_0rc2'
# The old version is the revision from which we should generate update snippets.
oldVersion                 = '3.0rc1'
oldAppVersion              = '3.0'
oldBuildNumber             = 3
oldBaseTag                 = 'THUNDERBIRD_3_0rc1'
releasePlatforms           = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz19-thunderbird-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2.mozillamessaging.com'
useBetaChannel             = 0
verifyConfigs              = {'linux':  'moz19-thunderbird-linux.cfg',
                              'macosx': 'moz19-thunderbird-mac.cfg',
                              'win32':  'moz19-thunderbird-win32.cfg'}
