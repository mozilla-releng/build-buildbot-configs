hgUsername          = 'ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mozilla-mobile-6.0'
mozSourceRepoName      = 'mozilla-mobile-6.0'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoPath      = 'releases/mozilla-mobile-6.0'
mozSourceRepoRevision  = 'f3cf32b9fe40'
mobileSourceRepoName      = 'mobile-6.0'
mobileSourceRepoPath      = 'releases/mobile-6.0'
mobileSourceRepoRevision  = '0822da62ae67'
mozRelbranchOverride      = ''
l10nRelbranchOverride     = ''
mobileRelbranchOverride   = ''
mozconfigDir        = 'mozilla-beta'
l10nRepoPath        = 'releases/l10n/mozilla-beta'
l10nRevisionFile    = 'l10n-changesets_mobile-6.0.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = True
enableMultiLocale   = True
androidMozharnessConfig = "multi_locale/6.0_release_android.json"
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '6.0b1'
appVersion          = '6.0'
milestone           = '6.0'
buildNumber         = 1
baseTag             = 'FENNEC_6_0'
oldVersion          = '5.0'
oldAppVersion       = '5.0'
oldBuildNumber      = 1
oldBaseTag          = 'FENNEC_5_0'
enUSPlatforms       = ('maemo5-gtk', 'android-r7')
l10nPlatforms       = ('maemo5-gtk',)
enUSDesktopPlatforms = ('linux-i686', 'macosx-i686', 'win32-i686')
l10nDesktopPlatforms = ()
talosTestPlatforms  = ()
ausBaseUploadDir    = '/opt/aus2/incoming/3/Fennec'
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'stage.mozilla.org'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (ftpServer, version, buildNumber)
ausServerUrl        = 'http://aus2.mozilla.org'
ausUser             = 'cltbld'
ausSshKey           = 'cltbld_dsa'
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
partnerRepackPlatforms = ('maemo5-gtk',)
