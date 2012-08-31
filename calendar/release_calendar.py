### This needs to be filled in ###

branchSuffix               = 'beta'

sourceRepoRevision         = 'ee519271a134'
mozillaRepoRevision        = 'THUNDERBIRD_16_0b1_RELEASE'

milestone                  = '16.0'

version                    = '1.8b1'
buildNumber                = 1

oldVersion                 = '1.7'
oldBuildNumber             = 1

relbranchOverride          = ''
mozillaRelbranchOverride   = ''

### Nothing else needs to be changed ###

hgUsername                 = 'calbld'
hgSshKey                   = '~cltbld/.ssh/calbld_dsa'
relbranchPrefix            = 'CAL'
sourceRepoName             = 'comm-' + branchSuffix # buildbot branch name
sourceRepoPath             = 'releases/' + sourceRepoName
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
mozillaRepoPath            = 'releases/mozilla-' + branchSuffix
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
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
l10nRevisionFile           = 'l10n-calendar-changesets'
l10nRepoPath               = 'releases/l10n/mozilla-' + branchSuffix
toolsRepoPath              = 'build/tools'
cvsroot                    = ':ext:calbld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'calendar/sunbird/config/version.txt'
# version-bump.pl needs an app name, which we have to hack a bit for Lightning.
productBumpName            = 'calendar/sunbird'
productName                = 'lightning'
brandName                  = 'Lightning'
appName                    = 'calendar'
ftpName			   = 'calendar/lightning'
projectName                = 'lightning'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
baseTag                    = 'CALENDAR_' + version.replace(".", "_")
appVersion                 = version
#XXX: Not entirely certain if/where this is used.
# The old version is the revision from which we should generate update snippets.
oldAppVersion              = oldVersion
oldBaseTag                 = 'CALENDAR_' + oldVersion.replace(".", "_")
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
