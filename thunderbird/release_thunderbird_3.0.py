hgUsername                 = 'tbirdbld'
hgSshKey                   = '~cltbld/.ssh/tbirdbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-1.9.1' # buildbot branch name
sourceRepoPath             = 'releases/comm-1.9.1'
sourceRepoRevision         = 'b8e06312e645' # from GO email for comm-1.9.1 branch
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
relbranchOverride          = '' # leave blank if you want buildbot to create a tag on comm-1.9.1
mozillaRepoPath            = 'releases/mozilla-1.9.1'
mozillaRepoRevision        = 'ead1204d8b81'
# If blank, automation will create its own branch based on COMM_<date>_RELBRANCH
# You typically want to set this to the gecko relbranch if doing a release off
# a specific gecko version.
mozillaRelbranchOverride   = 'COMM1919_20100316_RELBRANCH' # put Gecko relbranch here that we base upon
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = '18a1c983c8ee'
inspectorRelbranchOverride = ''
buildToolsRepoPath            = '' # leave empty if buildTools is not to be tagged
buildToolsRepoRevision        = '6a83a90371e2'
buildToolsRelbranchOverride   = ''
venkmanRepoPath            = '' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = ''
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ''
chatzillaTimestamp         = '' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n-mozilla-1.9.1'
l10nRevisionFile           = 'l10n-thunderbird-changesets-3.0'
toolsRepoPath              = 'build/tools'
cvsroot                    = ':ext:cltbld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'mail/config/version-191.txt'
productName                = 'thunderbird'
brandName                  = 'Thunderbird'
appName                    = 'mail'
ftpName                    = appName
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '3.0.4'
appVersion                 = version
#XXX: Not entirely certain if/where this is used.
# Look in release-firefox-mozilla-1.9.1.py for the milestone value
milestone                  = '1.9.1.9'
buildNumber                = 1
baseTag                    = 'THUNDERBIRD_3_0_4'
# The old version is the revision from which we should generate update snippets.
oldVersion                 = '3.0.3'
oldAppVersion              = oldVersion
oldBuildNumber             = 1
oldBaseTag                 = 'THUNDERBIRD_3_0_3'
enUSPlatforms             = ('linux', 'win32', 'macosx')
l10nPlatforms             = enUSPlatforms
#unittestPlatforms         = enUSPlatforms
unittestPlatforms          = ()
xulrunnerPlatforms         = ()
# Patcher should stay the same until we move to gecko 2.0
patcherConfig              = 'moz19-thunderbird-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausUser                    = 'tbirdbld_dsa'
ausSshKey                  = 'tbirdbld'
ausServerUrl               = 'https://aus2.mozillamessaging.com'
releaseNotesUrl		   = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
testOlderPartials          = True
doPartnerRepacks	   = False
useBetaChannel             = 1
verifyConfigs              = {'linux':  'moz19-thunderbird-linux.cfg',
                              'macosx': 'moz19-thunderbird-mac.cfg',
                              'win32':  'moz19-thunderbird-win32.cfg'}

# Version numbers we are updating _TO_
majorUpdateRepoPath    = 'releases/mozilla-1.9.2'
majorUpdateSourceRepoPath = 'releases/comm-1.9.2'
majorUpdateToVersion   = '3.1.4'
majorUpdateAppVersion  = majorUpdateToVersion
majorUpdateBuildNumber = 2
majorUpdateBaseTag     = 'THUNDERBIRD_3_1_4'
majorUpdateReleaseNotesUrl = 'http://www.mozillamessaging.com/%locale%/thunderbird/3.1/details/index.html'
majorUpdatePatcherConfig = 'moz192-thunderbird-branch-major-update-patcher2.cfg'
majorUpdateVerifyConfigs = {'linux':  'moz191-thunderbird-linux-major.cfg',
                            'macosx': 'moz191-thunderbird-mac-major.cfg',
                            'win32':  'moz191-thunderbird-win32-major.cfg'}
