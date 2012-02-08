releaseConfig = {}

releaseConfig['hgUsername']                 = 'seabld'
releaseConfig['hgSshKey']                   = '~seabld/.ssh/seabld_dsa'
releaseConfig['relbranchPrefix']            = 'COMM'
releaseConfig['sourceRepoName']             = 'comm-2.0' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'releases/comm-2.0'
releaseConfig['sourceRepoRevision']         = '1e53b6fcfb1d'
releaseConfig['relbranchOverride']          = 'COMM201_20110508_RELBRANCH'
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-2.0'
releaseConfig['mozillaRepoRevision']        = 'ff616f6ced18'
releaseConfig['mozillaRelbranchOverride']   = 'COMM20_053111_RELBRANCH' # put Gecko relbranch here that we base upon
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = '0bb7db177214'
releaseConfig['inspectorRelbranchOverride'] = 'COMM201_20110508_RELBRANCH'
releaseConfig['venkmanRepoPath']            = 'venkman' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = '65c389ee756c'
releaseConfig['venkmanRelbranchOverride']   = 'COMM201_20110508_RELBRANCH'
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = '210002e2b7e7'
releaseConfig['chatzillaRelbranchOverride'] = 'COMM201_20110508_RELBRANCH'
releaseConfig['l10nRepoPath']               = 'releases/l10n-mozilla-2.0'
releaseConfig['l10nRelbranchOverride']      = 'default'
releaseConfig['l10nRevisionFile']           = 'l10n-changesets-comm-2.0'
releaseConfig['cvsroot']                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
#productVersionFile                         = 'suite/config/version-20.txt'
releaseConfig['productVersionFile']         = ''
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
releaseConfig['version']                    = '2.1'
releaseConfig['appVersion']                 = '2.1'
releaseConfig['milestone']                  = '2.0.1'
releaseConfig['buildNumber']                = 1
releaseConfig['baseTag']                    = 'SEAMONKEY_2_1'
releaseConfig['oldVersion']                 = '2.1rc2'
releaseConfig['oldAppVersion']              = 2.1
releaseConfig['oldBuildNumber']             = 2
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_1rc2'
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
releaseConfig['useBetaChannel']             = 1
releaseConfig['verifyConfigs']              = {'linux':  'moz20-seamonkey-linux.cfg',
                                               'macosx64': 'moz20-seamonkey-mac.cfg',
                                               'win32':  'moz20-seamonkey-win32.cfg'}
releaseConfig['majorUpdateRepoPath']        = None
# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#releaseConfig['tuxedoConfig']              = 'seamonkey-tuxedo.ini'
#releaseConfig['tuxedoServerUrl']           = 'https://bounceradmin.mozilla.com/api/'
