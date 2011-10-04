hgUsername                 = 'calbld'
hgSshKey                   = '~cltbld/.ssh/calbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-beta' # buildbot branch name
sourceRepoPath             = 'releases/comm-beta'
sourceRepoRevision         = '05355991600d'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
relbranchOverride          = ''
mozillaRepoPath            = 'releases/mozilla-beta'
mozillaRepoRevision        = '4d8d9922dfca'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
mozillaRelbranchOverride   = 'COMM80_20110929_RELBRANCH'
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
l10nRepoPath               = 'releases/l10n-miramar'
l10nRevisionFile           = 'l10n-calendar-changesets'
l10nRevisionUrl            = 'http://hg.mozilla.org/build/buildbot-configs/raw-file/CALENDAR_1_0b7_RELEASE/calendar/l10n-calendar-changesets'
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
version                    = '1.0rc1'
appVersion                 = '1.0rc1'
#XXX: Not entirely certain if/where this is used.
milestone                  = '7.0'
buildNumber                = 1
baseTag                    = 'CALENDAR_1_0rc1'
# The old version is the revision from which we should generate update snippets.
oldVersion                 = '1.0b7'
oldAppVersion              = oldVersion
oldBuildNumber             = 1
oldBaseTag                 = ''
releasePlatforms           = ('linux', 'linux64', 'win32', 'macosx64')
patcherConfig              = 'moz19-calendar-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R14'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2-community.mozilla.org'
useBetaChannel             = 1
l10nPlatforms              = ('linux', 'win32', 'macosx')
l10nPlatforms              = ()
verifyConfigs              = {'linux':  'moz19-calendar-linux.cfg',
                              'linux64': 'moz19-calendar-linux.cfg',
                              'macosx64': 'moz19-calendar-mac.cfg',
                              'win32':  'moz19-calendar-win32.cfg'}
