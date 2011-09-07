hgUsername                 = 'calbld'
hgSshKey                   = '~calbld/.ssh/calbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-aurora-lightning' # buildbot branch name
sourceRepoPath             = 'releases/comm-aurora'
sourceRepoRevision         = '653d6c77512a'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
relbranchOverride          = 'COMM50_20110620_RELBRANCH'
mozillaRepoPath            = 'releases/mozilla-aurora'
mozillaRepoRevision        = '9dcd813b2fc8'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
mozillaRelbranchOverride   = 'COMM50_20110620_RELBRANCH'
inspectorRepoPath          = '' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = ''
inspectorRelbranchOverride = ''
buildToolsRepoPath            = '' # leave empty if buildTools is not to be tagged
buildToolsRepoRevision        = ''
buildToolsRelbranchOverride   = ''
venkmanRepoPath            = '' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = ''
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ''
chatzillaTimestamp         = '' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n/mozilla-aurora'
l10nRevisionFile           = 'l10n-calendar-changesets'
toolsRepoPath              = 'build/tools'
cvsroot                    = ':ext:calbld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'calendar/sunbird/config/version.txt'
productName                = 'sunbird'
brandName                  = 'Sunbird'
appName                    = 'calendar'
ftpName			   = 'calendar/sunbird'
projectName                = 'sunbird'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '1.0b4'
appVersion                 = '1.0b4'
#XXX: Not entirely certain if/where this is used.
milestone                  = '5.0'
buildNumber                = 1
baseTag                    = 'CALENDAR_1_0b4'
# The old version is the revision from which we should generate update snippets.
oldVersion                 = '1.0b2'
oldAppVersion              = oldVersion
oldBuildNumber             = 2
oldBaseTag                 = ''
releasePlatforms           = ()
patcherConfig              = 'moz19-calendar-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R11'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2-community.mozilla.org'
useBetaChannel             = 1
l10nPlatforms              = ('linux', 'win32', 'macosx')
verifyConfigs              = {'linux':  'moz19-calendar-linux.cfg',
                              'macosx': 'moz19-calendar-mac.cfg',
                              'win32':  'moz19-calendar-win32.cfg'}
