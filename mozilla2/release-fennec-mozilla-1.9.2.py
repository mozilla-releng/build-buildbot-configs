hgUsername          = 'ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mobile-1.9.2'
mozSourceRepoName      = 'mozilla-1.9.2'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoPath      = 'releases/mozilla-1.9.2'
mozSourceRepoRevision  = '3596945fe21e'
mobileSourceRepoName      = 'mobile-browser'
mobileSourceRepoPath      = 'mobile-browser'
mobileSourceRepoRevision  = '44cf520a5194'
relbranchOverride   = ''
l10nRepoPath        = 'releases/l10n-mozilla-1.9.2'
l10nRevisionFile    = 'l10n-changesets_mobile-1.0.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = False
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '1.0rc1'
appVersion          = '1.0'
milestone           = '1.9.2'
buildNumber         = 1
baseTag             = 'FENNEC_1_0'
enUSPlatforms       = ('maemo',)
l10nPlatforms       = enUSPlatforms
talosTestPlatforms  = ()
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'staging.mozilla.org'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (stagingServer, version, buildNumber)
