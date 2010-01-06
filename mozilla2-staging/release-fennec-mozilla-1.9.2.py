hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mobile-1.9.2'
mozSourceRepoName      = 'mozilla-1.9.2'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoClonePath = 'releases/mozilla-1.9.2'
mozSourceRepoPath      = 'users/stage-ffxbld/mozilla-1.9.2'
mozSourceRepoRevision  = '32f7c526813a'
mobileSourceRepoName      = 'mobile-browser'
mobileSourceRepoClonePath = 'mobile-browser'
mobileSourceRepoPath      = 'users/stage-ffxbld/mobile-browser'
mobileSourceRepoRevision  = 'b05200e571c8'
mozRelbranchOverride   = ''
l10nRelbranchOverride   = ''
mobileRelbranchOverride   = ''
l10nRepoClonePath   = 'releases/l10n-mozilla-1.9.2'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets_mobile-1.0.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = True
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '1.0rc1'
appVersion          = '1.0'
milestone           = '1.9.2'
buildNumber         = 1
baseTag             = 'FENNEC_1_0rc1'
enUSPlatforms       = ('maemo',)
l10nPlatforms       = enUSPlatforms
talosTestPlatforms  = ()
ftpServer           = 'staging-stage.build.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (ftpServer, version, buildNumber)
