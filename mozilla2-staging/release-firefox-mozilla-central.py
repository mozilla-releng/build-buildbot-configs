hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName      = 'mozilla-central'
# This parameter (and it's l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
sourceRepoClonePath = sourceRepoName
sourceRepoPath      = 'users/stage-ffxbld/mozilla-central'
# TODO: Add a sourceRepoRevision before trying to use this config to tag
sourceRepoRevision  = ''
relbranchOverride   = ''
l10nRepoClonePath   = 'l10n-central'
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
version             = '3.7a5'
appVersion          = version
milestone           = '1.9.3a5'
buildNumber         = 1
baseTag             = 'FIREFOX_3_7a5'
oldVersion          = '3.7a4'
oldAppVersion       = oldVersion
oldBuildNumber      = 1
oldBaseTag          = 'FIREFOX_3_7a4'
enUSPlatforms       = ('linux', 'linux64', 'win32', 'macosx', 'macosx64')
l10nPlatforms       = enUSPlatforms
talosTestPlatforms  = enUSPlatforms
unittestPlatforms   = enUSPlatforms
xulrunnerPlatforms  = enUSPlatforms
patcherConfig       = 'moz193-branch-patcher2.cfg'
binaryName          = 'MozillaDeveloperPreview'
oldBinaryName       = 'MozillaDeveloperPreview'
patcherToolsTag     = 'UPDATE_PACKAGING_R11'
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
bouncerServer       = 'download.mozilla.org'
ausServerUrl        = 'http://staging-stage.build.mozilla.org'
ausUser             = 'cltbld'
ausSshKey           = 'cltbld_dsa'
releaseNotesUrl     = 'http://www.mozilla.org/projects/devpreview/releasenotes/'
useBetaChannel      = 0
# TODO: create these files before 3.7a2
verifyConfigs       = {'linux':    'moz193-firefox-linux.cfg',
                       'linux64':  'moz193-firefox-linux64.cfg',
                       'macosx':   'moz193-firefox-mac.cfg',
                       'macosx64': 'moz193-firefox-mac64.cfg',
                       'win32':    'moz193-firefox-win32.cfg'}
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
majorUpdateRepoPath = None
