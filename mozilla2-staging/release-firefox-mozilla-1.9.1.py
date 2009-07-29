hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName      = 'mozilla-1.9.1'
# This parameter (and it's l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
sourceRepoClonePath = 'releases/mozilla-1.9.1'
sourceRepoPath      = 'users/stage-ffxbld/mozilla-1.9.1'
sourceRepoRevision  = 'dc0e69abb566'
relbranchOverride   = ''
l10nRepoClonePath   = 'releases/l10n-mozilla-1.9.1'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets'
cvsroot             = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
productName         = 'firefox'
appName             = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '3.5.1'
appVersion          = version
milestone           = '1.9.1.1'
buildNumber         = 1
baseTag             = 'FIREFOX_3_5_1'
oldVersion          = '3.5rc3'
oldAppVersion       = '3.5'
oldBuildNumber      = 2
oldBaseTag          = 'FIREFOX_3_5'
releasePlatforms    = ('linux', 'win32', 'macosx')
patcherConfig       = 'moz191-branch-patcher2.cfg'
patcherToolsTag     = 'UPDATE_PACKAGING_R9'
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
bouncerServer       = 'download.mozilla.org'
ausServerUrl        = 'http://staging-stage.build.mozilla.org'
useBetaChannel      = 0
verifyConfigs       = {'linux':  'moz191-firefox-linux.cfg',
                       'macosx': 'moz191-firefox-mac.cfg',
                       'win32':  'moz191-firefox-win32.cfg'}
