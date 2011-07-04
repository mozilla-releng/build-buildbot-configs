hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName      = 'mozilla-central'
# This parameter (and it's l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
sourceRepoClonePath = sourceRepoName
sourceRepoPath      = 'users/stage-ffxbld/mozilla-central'
# TODO: Add a sourceRepoRevision before trying to use this config to tag
sourceRepoRevision  = ''
relbranchOverride   = ''
l10nRepoClonePath   = 'l10n-central'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets'
# mergeLocales allows missing localized strings to be filled in by their en-US
# equivalent string. This is on (True) by default for nightly builds, but 
# should be False for releases *EXCEPT* alphas and early betas. If in doubt, 
# ask release-drivers.
mergeLocales        = True
cvsroot             = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
productName         = 'firefox'
appName             = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '4.0b2'
appVersion          = version
# NB: this will become 2.0.x not 2.0.0.x, bug 577875
milestone           = '2.0b2'
buildNumber         = 1
baseTag             = 'FIREFOX_4_0b2'
oldVersion          = '4.0b1'
oldAppVersion       = oldVersion
oldBuildNumber      = 2
oldBaseTag          = 'FIREFOX_4_0b1'
enUSPlatforms       = ('linux', 'linux64', 'win32', 'macosx', 'macosx64')
l10nPlatforms       = enUSPlatforms
talosTestPlatforms  = enUSPlatforms
unittestPlatforms   = enUSPlatforms
xulrunnerPlatforms  = enUSPlatforms
patcherConfig       = 'moz193-branch-patcher2.cfg'
binaryName          = 'Firefox'
oldBinaryName       = binaryName
patcherToolsTag     = 'UPDATE_PACKAGING_R12'
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'dev-stage01.build.sjc1.mozilla.com'
bouncerServer       = 'download.mozilla.org'
ausServerUrl        = 'http://dev-stage01.build.sjc1.mozilla.com'
ausUser             = 'cltbld'
ausSshKey           = 'cltbld_dsa'
testOlderPartials   = False
releaseNotesUrl     = 'http://www.mozilla.org/projects/devpreview/releasenotes/'
useBetaChannel      = 0
verifyConfigs       = {'linux':    'moz193-firefox-linux.cfg',
                       'linux64':  'moz193-firefox-linux64.cfg',
                       'macosx':   'moz193-firefox-mac.cfg',
                       'macosx64': 'moz193-firefox-mac64.cfg',
                       'win32':    'moz193-firefox-win32.cfg'}
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
majorUpdateRepoPath = None
# Tuxedo/Bouncer related
tuxedoConfig        = 'firefox-tuxedo.ini'
tuxedoServerUrl     = 'https://tuxedo.stage.mozilla.com/api/'
