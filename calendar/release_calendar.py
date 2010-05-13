hgUsername                 = 'calbld'
hgSshKey                   = '~calbld/.ssh/calbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.2-lightning' # buildbot branch name
sourceRepoPath             = 'comm-central'
sourceRepoRevision         = '19d5618679fe'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
relbranchOverride          = ''
mozillaRepoPath            = 'releases/mozilla-1.9.2'
mozillaRepoRevision        = 'dcf8e50115bc'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
mozillaRelbranchOverride   = ''
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = '27b0e9ef1715'
inspectorRelbranchOverride = ''
buildToolsRepoPath            = '' # leave empty if buildTools is not to be tagged
buildToolsRepoRevision        = ''
buildToolsRelbranchOverride   = ''
venkmanRepoPath            = '' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = ''
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ''
chatzillaTimestamp         = '' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n-mozilla-1.9.2'
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
version                    = '1.0b2'
appVersion                 = '1.0b2'
#XXX: Not entirely certain if/where this is used.
milestone                  = '1.9.2.5'
buildNumber                = 1
baseTag                    = 'CALENDAR_1_0b2'
# The old version is the revision from which we should generate update snippets.
oldVersion                 = ''
oldAppVersion              = oldVersion
oldBuildNumber             = 1
oldBaseTag                 = ''
releasePlatforms           = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz19-calendar-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2-community.mozilla.org'
useBetaChannel             = 1
verifyConfigs              = {'linux':  'moz19-calendar-linux.cfg',
                              'macosx': 'moz19-calendar-mac.cfg',
                              'win32':  'moz19-calendar-win32.cfg'}
