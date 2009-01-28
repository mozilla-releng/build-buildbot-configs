hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName      = 'mozilla-1.9.1'
# This parameter (and it's l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
sourceRepoClonePath = 'releases/mozilla-1.9.1'
sourceRepoPath      = 'users/stage-ffxbld/mozilla-1.9.1'
sourceRepoRevision  = '9074662447ae'
relbranchOverride   = ''
baseTag             = 'FIREFOX_3_1b3'
l10nRepoClonePath   = 'releases/l10n-mozilla-1.9.1'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets'
cvsroot             = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
productName         = 'firefox'
appName             = 'browser'
appVersion          = '3.1b3'
milestone           = '1.9.1b3'
buildNumber         = 1
oldVersion          = '3.1b2'
oldBuildNumber      = 2
oldBaseTag          = 'FIREFOX_3_1b2'
releasePlatforms    = ('linux', 'win32', 'macosx')
patcherConfig       = 'moz191-branch-patcher2.cfg'
patcherToolsTag     = 'UPDATE_PACKAGING_R6'
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
bouncerServer       = 'download.mozilla.org'
ausServerUrl        = 'http://staging-stage.build.mozilla.org'
useBetaChannel      = 0
linuxVerifyConfig   = 'moz191-firefox-linux.cfg'
macVerifyConfig     = 'moz191-firefox-mac.cfg'
win32VerifyConfig   = 'moz191-firefox-win32.cfg'
