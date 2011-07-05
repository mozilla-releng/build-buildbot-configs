hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mozilla-mobile-5.0'
mozSourceRepoName      = 'mozilla-mobile-5.0'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoClonePath = 'releases/mozilla-mobile-5.0'
mozSourceRepoPath      = 'users/stage-ffxbld/mozilla-mobile-5.0'
mozSourceRepoRevision  = 'default'
mobileSourceRepoName      = 'mobile-5.0'
mobileSourceRepoClonePath = 'releases/mobile-5.0'
mobileSourceRepoPath      = 'users/stage-ffxbld/mobile-5.0'
mobileSourceRepoRevision  = 'default'
mozRelbranchOverride   = ''
l10nRelbranchOverride   = ''
mobileRelbranchOverride   = ''
mozconfigDir              = 'mozilla-beta'
l10nRepoClonePath   = 'releases/l10n/mozilla-beta'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets_mobile-5.0.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = True
enableMultiLocale   = True
androidMozharnessConfig = "multi_locale/staging_5.0_release_android.json"
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '5.0b1'
appVersion          = version
milestone           = '5.0'
buildNumber         = 1
baseTag             = 'FENNEC_5_0b1'
oldVersion          = '4.0.1'
oldAppVersion       = oldVersion
oldBuildNumber      = 1
oldBaseTag          = 'FENNEC_4_0_1'
enUSPlatforms       = ('maemo5-gtk', 'android-r7')
l10nPlatforms       = ('maemo5-gtk',)
enUSDesktopPlatforms = ('linux-i686', 'macosx-i686', 'win32-i686')
l10nDesktopPlatforms = ()
talosTestPlatforms  = ()
ausBaseUploadDir    = '/opt/aus2/incoming/3/Fennec'
ftpServer           = 'dev-stage01.build.sjc1.mozilla.com'
stagingServer       = 'dev-stage01.build.sjc1.mozilla.com'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (ftpServer, version, buildNumber)
ausServerUrl        = 'http://dev-stage01.build.sjc1.mozilla.com'
ausUser             = 'cltbld'
ausSshKey           = 'id_rsa'
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
partnerRepackPlatforms = ('maemo5-gtk',)
