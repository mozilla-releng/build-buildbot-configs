hgUsername          = 'ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mobile-trunk'
mozSourceRepoName      = 'mozilla-central'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoPath      = 'mozilla-central'
mozSourceRepoRevision  = '4791cfde3ca0'
mobileSourceRepoName      = 'mobile-browser'
mobileSourceRepoPath      = 'mobile-browser'
mobileSourceRepoRevision  = '840649eabc3b'
mozRelbranchOverride      = 'GECKO20b7pre_20100929_RELBRANCH'
l10nRelbranchOverride     = 'GECKO20b7pre_20100929_RELBRANCH'
mobileRelbranchOverride   = 'GECKO20b7pre_20100929_RELBRANCH'
l10nRepoPath        = 'l10n-central'
l10nRevisionFile    = 'l10n-changesets_mobile-2.0.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = True
disableMultiLocale  = True
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '4.0b1'
appVersion          = version
milestone           = '2.0b7pre'
buildNumber         = 1
baseTag             = 'FENNEC_4_0b1'
oldVersion          = '2.0a1'
oldAppVersion       = oldVersion
oldBuildNumber      = 3
oldBaseTag          = 'FENNEC_2_0a1'
enUSPlatforms       = ('maemo5-gtk', 'android-r7')
l10nPlatforms       = ()
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
