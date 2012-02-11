releaseConfig = {}

releaseConfig['hgUsername']                 = 'seabld'
releaseConfig['hgSshKey']                   = '~seabld/.ssh/seabld_dsa'
releaseConfig['relbranchPrefix']            = 'SEA_COMM'
releaseConfig['sourceRepoName']             = 'comm-beta' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'releases/comm-beta'
releaseConfig['sourceRepoRevision']         = '458dad0ffd8f'
releaseConfig['relbranchOverride']          = ''
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-beta'
releaseConfig['mozillaRepoRevision']        = '700391b27db1'
releaseConfig['mozillaRelbranchOverride']   = 'COMM110_2012020802_RELBRANCH' # put Gecko relbranch here that we base upon
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = '589ef9b749f5'
releaseConfig['inspectorRelbranchOverride'] = 'DOMI_2_0_10'
releaseConfig['venkmanRepoPath']            = 'venkman' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = 'a38583d7164a'
releaseConfig['venkmanRelbranchOverride']   = ''
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = 'CHATZILLA_0_9_88_RELEASE'
releaseConfig['chatzillaRelbranchOverride'] = ''
releaseConfig['l10nRepoPath']               = 'releases/l10n/mozilla-beta'
releaseConfig['l10nRelbranchOverride']      = ''
releaseConfig['l10nRevisionFile']           = 'l10n-changesets-comm-beta'
releaseConfig['cvsroot']                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
#releaseConfig['productVersionFile']        = 'suite/config/version-20.txt'
releaseConfig['productVersionFile']         = ''
# mergeLocales allows missing localized strings to be filled in by their en-US
# equivalent string. This is on (True) by default for nightly builds, but
# should be False for releases *EXCEPT* alphas and early betas. If in doubt,
# ask release-drivers.
releaseConfig['mergeLocales']               = True
releaseConfig['productName']                = 'seamonkey'
releaseConfig['brandName']                  = 'SeaMonkey'
releaseConfig['appName']                    = 'suite'
releaseConfig['skip_tag']                   = False
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
releaseConfig['version']                    = '2.8b2'
releaseConfig['appVersion']                 = '2.8'
releaseConfig['milestone']                  = '11.0'
releaseConfig['buildNumber']                = 1
releaseConfig['baseTag']                    = 'SEAMONKEY_2_8b2'
releaseConfig['oldVersion']                 = '2.8b1'
releaseConfig['oldAppVersion']              = '2.8'
releaseConfig['oldBuildNumber']             = 1
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_8b1'
releaseConfig['oldRepoPath']                = 'releases/comm-beta'
releaseConfig['enUSPlatforms']              = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['l10nPlatforms']              = ('linux', 'win32', 'macosx64')
releaseConfig['patcherConfig']              = 'mozBeta-seamonkey-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']            = 'UPDATE_PACKAGING_R14'
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
releaseConfig['verifyConfigs']              = {'linux':  'mozBeta-seamonkey-linux.cfg',
                                               'macosx64': 'mozBeta-seamonkey-mac64.cfg',
                                               'win32':  'mozBeta-seamonkey-win32.cfg'}
releaseConfig['majorUpdateRepoPath']        = None
# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#releaseConfig['tuxedoConfig']              = 'seamonkey-tuxedo.ini'
#releaseConfig['tuxedoServerUrl']           = 'https://bounceradmin.mozilla.com/api/'
releaseConfig['releaseChannel']             = 'beta'