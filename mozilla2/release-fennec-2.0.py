hgUsername          = 'ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mobile-trunk'
mozSourceRepoName      = 'mozilla-central'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoPath      = 'mozilla-central'
mozSourceRepoRevision  = 'FILLMEIN'
mobileSourceRepoName      = 'mobile-browser'
mobileSourceRepoPath      = 'mobile-browser'
mobileSourceRepoRevision  = 'FILLMEIN'
mozRelbranchOverride      = 'GECKO20b5pre_20100820_RELBRANCH'
l10nRelbranchOverride     = ''
mobileRelbranchOverride   = ''
l10nRepoPath        = 'l10n-central'
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
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'stage.mozilla.org'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (ftpServer, version, buildNumber)
doPartnerRepacks    = True
partnersRepoPath    = 'build/partner-repacks'
partnerRepackPlatforms = ('maemo4', 'maemo5-gtk')
