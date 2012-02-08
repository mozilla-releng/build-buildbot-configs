releaseConfig = {}

releaseConfig['hgUsername']                 = 'seabld'
releaseConfig['hgSshKey']                   = '~seabld/.ssh/seabld_dsa'
releaseConfig['relbranchPrefix']            = 'COMM'
releaseConfig['sourceRepoName']             = 'comm-2.0' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'comm-central'
releaseConfig['sourceRepoRevision']         = 'a842a749a221'
releaseConfig['relbranchOverride']          = 'COMM20_20110405_RELBRANCH'
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-2.0'
releaseConfig['mozillaRepoRevision']        = '08724a0335a3'
releaseConfig['mozillaRelbranchOverride']   = 'COMM20_20110405_RELBRANCH' # put Gecko relbranch here that we base upon
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = 'fcfb387360fd'
releaseConfig['inspectorRelbranchOverride'] = 'COMM20_20110405_RELBRANCH'
releaseConfig['venkmanRepoPath']            = 'venkman' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = '9126bebdf047'
releaseConfig['venkmanRelbranchOverride']   = 'COMM20_20110405_RELBRANCH'
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = '29d3c6d2a751'
releaseConfig['chatzillaRelbranchOverride'] = 'COMM20_20110405_RELBRANCH'
releaseConfig['l10nRepoPath']               = 'releases/l10n-mozilla-2.0'
releaseConfig['l10nRevisionFile']           = 'l10n-changesets_comm_central_trunk'
releaseConfig['cvsroot']                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
releaseConfig['productVersionFile']         = 'suite/config/version-20.txt'
# mergeLocales allows missing localized strings to be filled in by their en-US
# equivalent string. This is on (True) by default for nightly builds, but
# should be False for releases *EXCEPT* alphas and early betas. If in doubt,
# ask release-drivers.
releaseConfig['mergeLocales']               = True
releaseConfig['productName']                = 'seamonkey'
releaseConfig['brandName']                  = 'SeaMonkey'
releaseConfig['appName']                    = 'suite'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
releaseConfig['version']                    = '2.1b3'
releaseConfig['appVersion']                 = version
releaseConfig['milestone']                  = '2.0'
releaseConfig['buildNumber']                = 3
releaseConfig['baseTag']                    = 'SEAMONKEY_2_1b3'
releaseConfig['oldVersion']                 = '2.1b2'
releaseConfig['oldAppVersion']              = oldVersion
releaseConfig['oldBuildNumber']             = 2
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_1b2'
releaseConfig['enUSPlatforms']              = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['l10nPlatforms']              = ('linux', 'win32', 'macosx64')
releaseConfig['patcherConfig']              = 'moz20-seamonkey-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']            = 'UPDATE_PACKAGING_R13'
releaseConfig['binaryName']                 = releaseConfig['brandName']
releaseConfig['oldBinaryName']              = releaseConfig['binaryName']
releaseConfig['ftpServer']                  = 'ftp.mozilla.org'
releaseConfig['stagingServer']              = 'stage-old.mozilla.org'
releaseConfig['talosTestPlatforms']         = ()
releaseConfig['unittestPlatforms']          = ()
releaseConfig['bouncerServer']              = 'download.mozilla.org'
releaseConfig['ausServerUrl']               = 'https://aus2-community.mozilla.org'
releaseConfig['testOlderPartials']          = False
releaseConfig['releaseNotesUrl']            = None
releaseConfig['useBetaChannel']             = 0
releaseConfig['verifyConfigs']              = {'linux':  'moz20-seamonkey-linux.cfg',
                                               'macosx64': 'moz20-seamonkey-mac.cfg',
                                               'win32':  'moz20-seamonkey-win32.cfg'}
releaseConfig['majorUpdateRepoPath']        = None
# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#releaseConfig['tuxedoConfig']              = 'seamonkey-tuxedo.ini'
#releaseConfig['tuxedoServerUrl']           = 'https://bounceradmin.mozilla.com/api/'
