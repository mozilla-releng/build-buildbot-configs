hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mobile-trunk'
mozSourceRepoName      = 'mozilla-central'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoClonePath = 'mozilla-central'
mozSourceRepoPath      = 'users/stage-ffxbld/mozilla-central'
mozSourceRepoRevision  = 'default'
mobileSourceRepoName      = 'mobile-browser'
mobileSourceRepoClonePath = 'mobile-browser'
mobileSourceRepoPath      = 'users/stage-ffxbld/mobile-browser'
mobileSourceRepoRevision  = 'default'
mozRelbranchOverride   = ''
l10nRelbranchOverride   = ''
mobileRelbranchOverride   = ''
l10nRepoClonePath   = 'l10n-central'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets_mobile-2.0.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = True
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '2.0a1'
appVersion          = version
milestone           = '2.0b5pre'
buildNumber         = 1
baseTag             = 'FENNEC_2_0a1'
enUSPlatforms       = ('maemo4', 'maemo5-gtk', 'maemo5-qt', 'android-r7')
l10nPlatforms       = ('maemo4', 'maemo5-gtk', 'maemo5-qt')
enUSDesktopPlatforms = ('linux-i686', 'macosx-i686', 'win32-i686')
l10nDesktopPlatforms = ()
talosTestPlatforms  = ()
ftpServer           = 'staging-stage.build.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (ftpServer, version, buildNumber)
doPartnerRepacks    = True
partnersRepoPath    = 'build/partner-repacks'
partnerRepackPlatforms = ('maemo4', 'maemo5-gtk')
