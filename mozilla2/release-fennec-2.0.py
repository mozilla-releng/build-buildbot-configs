hgUsername          = 'ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mobile-2.0'
mozSourceRepoName      = 'mozilla-2.1'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoPath      = 'releases/mozilla-2.1'
mozSourceRepoRevision  = 'FILLMEIN'
mobileSourceRepoName      = 'mobile-2.0'
mobileSourceRepoPath      = 'releases/mobile-2.0'
mobileSourceRepoRevision  = 'FILLMEIN'
mozRelbranchOverride      = ''
l10nRelbranchOverride     = ''
mobileRelbranchOverride   = ''
l10nRepoPath        = 'releases/l10n-mozilla-2.0'
l10nRevisionFile    = 'l10n-changesets_mobile-2.0.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = True
enableMultiLocale   = True
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '4.0'
appVersion          = version
milestone           = '2.1'
buildNumber         = 1
baseTag             = 'FENNEC_4_0rc1'
oldVersion          = '4.0b5'
oldAppVersion       = oldVersion
oldBuildNumber      = 3
oldBaseTag          = 'FENNEC_4_0b5'
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
