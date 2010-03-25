hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName      = 'firefox-lorentz'
# This parameter (and it's l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
sourceRepoClonePath = 'projects/firefox-lorentz'
sourceRepoPath      = 'users/stage-ffxbld/firefox-lorentz'
sourceRepoRevision  = '846dd0f94c99'
relbranchOverride   = ''
l10nRepoClonePath   = 'releases/l10n-mozilla-1.9.2'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets_firefox-lorentz'
cvsroot             = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
productName         = 'firefox'
appName             = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '3.6.3plugin1'
appVersion          = version
milestone           = '1.9.2.3pre'
buildNumber         = 1
baseTag             = 'FIREFOX_3_6_3plugin1'
oldVersion          = '3.6.2'
oldAppVersion       = oldVersion
oldBuildNumber      = 3
oldBaseTag          = 'FIREFOX_3_6_2'
enUSPlatforms       = ('linux', 'win32', 'macosx')
l10nPlatforms       = ('linux', 'win32', 'macosx')
talosTestPlatforms  = ('linux', 'win32', 'macosx')
unittestPlatforms   = ('linux', 'win32', 'macosx')
patcherConfig       = 'moz192-branch-lorentz-patcher2.cfg'
patcherToolsTag     = 'UPDATE_PACKAGING_R10'
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
bouncerServer       = 'download.mozilla.org'
ausServerUrl        = 'http://staging-stage.build.mozilla.org'
useBetaChannel      = 1
verifyConfigs       = {'linux':  'moz192-firefox-linux-lorentz.cfg',
                       'macosx': 'moz192-firefox-mac-lorentz.cfg',
                       'win32':  'moz192-firefox-win32-lorentz.cfg'}
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
majorUpdateRepoPath = None