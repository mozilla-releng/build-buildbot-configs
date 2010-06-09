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
version             = '3.5.8'
appVersion          = version
milestone           = '1.9.1.8'
buildNumber         = 1
baseTag             = 'FIREFOX_3_5_8'
oldVersion          = '3.5.7'
oldAppVersion       = '3.5.7'
oldBuildNumber      = 1
oldBaseTag          = 'FIREFOX_3_5_7'
enUSPlatforms       = ('linux', 'win32', 'macosx')
talosTestPlatforms  = ()
unittestPlatforms   = ()
l10nPlatforms       = enUSPlatforms
xulrunnerPlatforms  = enUSPlatforms
patcherConfig       = 'moz191-branch-patcher2.cfg'
patcherToolsTag     = 'UPDATE_PACKAGING_R11'
binaryName          = productName.capitalize()
oldBinaryName       = binaryName
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
bouncerServer       = 'download.mozilla.org'
ausServerUrl        = 'http://staging-stage.build.mozilla.org'
ausUser             = 'cltbld'
ausSshKey           = 'cltbld_dsa'
releaseNotesUrl     = None
useBetaChannel      = 1
verifyConfigs       = {'linux':  'moz191-firefox-linux.cfg',
                       'macosx': 'moz191-firefox-mac.cfg',
                       'win32':  'moz191-firefox-win32.cfg'}
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
majorUpdateRepoPath    = 'users/stage-ffxbld/mozilla-1.9.2'
majorUpdateToVersion   = '3.6rc2'
majorUpdateAppVersion  = '3.6'
majorUpdateBuildNumber = 1
majorUpdateBaseTag     = 'FIREFOX_3_6rc2'
majorUpdateReleaseNotesUrl = 'http://www.mozilla.com/%locale%/firefox/3.6/details/index.html'
majorUpdatePatcherConfig = 'moz191-branch-major-update-patcher2.cfg'
majorUpdateVerifyConfigs = {'linux':  'moz191-firefox-linux-major.cfg',
                            'macosx': 'moz191-firefox-mac-major.cfg',
                            'win32':  'moz191-firefox-win32-major.cfg'}
# Tuxedo/Bouncer related
tuxedoConfig        = 'firefox-tuxedo.ini'
tuxedoServerUrl     = 'https://tuxedo.stage.mozilla.com/api/'
