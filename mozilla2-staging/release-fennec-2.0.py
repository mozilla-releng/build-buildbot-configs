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
disableMultiLocale  = False
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '4.0b2'
appVersion          = version
milestone           = '4.0b7pre'
buildNumber         = 1
baseTag             = 'FENNEC_4_0b2'
oldVersion          = '4.0b1'
oldAppVersion       = oldVersion
oldBuildNumber      = 1
oldBaseTag          = 'FENNEC_4_0b1'
enUSPlatforms       = ('maemo5-gtk', 'android-r7')
l10nPlatforms       = ('maemo5-gtk',)
enUSDesktopPlatforms = ('linux-i686', 'macosx-i686', 'win32-i686')
l10nDesktopPlatforms = ()
talosTestPlatforms  = ()
ausBaseUploadDir    = '/opt/aus2/incoming/3/Fennec'
ftpServer           = 'staging-stage.build.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (ftpServer, version, buildNumber)
ausServerUrl        = 'http://staging-stage.build.mozilla.org'
ausUser             = 'cltbld'
ausSshKey           = 'id_rsa'
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
partnerRepackPlatforms = ('maemo5-gtk',)
