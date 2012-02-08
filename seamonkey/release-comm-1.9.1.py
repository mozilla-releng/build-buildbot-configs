releaseConfig = {}

releaseConfig['hgUsername']                 = 'seabld'
releaseConfig['hgSshKey']                   = '~seabld/.ssh/seabld_dsa'
releaseConfig['relbranchPrefix']            = 'COMM'
releaseConfig['sourceRepoName']             = 'comm-1.9.1' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'releases/comm-1.9.1'
releaseConfig['sourceRepoRevision']         = 'b292e787146b'
releaseConfig['relbranchOverride']          = 'COMM19119_20110416_RELBRANCH'
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-1.9.1'
releaseConfig['mozillaRepoRevision']        = 'FIREFOX_3_5_19_RELEASE'
releaseConfig['mozillaRelbranchOverride']   = 'GECKO19119_2011041408_RELBRANCH' # put Gecko relbranch here that we base upon
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = 'f6c78804ebb4'
releaseConfig['inspectorRelbranchOverride'] = 'COMM_1_9_1_BRANCH'
releaseConfig['venkmanRepoPath']            = 'venkman' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = 'f13c813e4ec6'
releaseConfig['venkmanRelbranchOverride']   = 'COMM_1_9_1_BRANCH'
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = 'f5fd1b073bf8'
releaseConfig['chatzillaRelbranchOverride'] = 'COMM_1_9_1_BRANCH'
releaseConfig['l10nRepoPath']               = 'releases/l10n-mozilla-1.9.1'
releaseConfig['l10nRevisionFile']           = 'l10n-changesets'
releaseConfig['l10nRelbranchOverride']      = 'COMM_1_9_1_BRANCH'
releaseConfig['cvsroot']                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
releaseConfig['productVersionFile']         = 'suite/config/version-191.txt'
# mergeLocales allows missing localized strings to be filled in by their en-US
# equivalent string. This is on (True) by default for nightly builds, but
# should be False for releases *EXCEPT* alphas and early betas. If in doubt,
# ask release-drivers.
releaseConfig['mergeLocales']               = False
releaseConfig['productName']                = 'seamonkey'
releaseConfig['brandName']                  = 'SeaMonkey'
releaseConfig['appName']                    = 'suite'
releaseConfig['skip_tag']                   = False
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
releaseConfig['version']                    = '2.0.14'
releaseConfig['appVersion']                 = version
releaseConfig['milestone']                  = '1.9.1.19'
releaseConfig['buildNumber']                = 2
releaseConfig['baseTag']                    = 'SEAMONKEY_2_0_14'
releaseConfig['oldVersion']                 = '2.0.13'
releaseConfig['oldAppVersion']              = oldVersion
releaseConfig['oldBuildNumber']             = 1
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_0_13'
releaseConfig['oldRepoPath']                = 'releases/comm-1.9.1'
releaseConfig['enUSPlatforms']              = ('linux', 'linux64', 'win32', 'macosx')
releaseConfig['l10nPlatforms']              = ('linux', 'win32', 'macosx')
releaseConfig['patcherConfig']              = 'moz191-seamonkey-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']            = 'UPDATE_PACKAGING_R11_1'
releaseConfig['binaryName']                 = releaseConfig['brandName']
releaseConfig['oldBinaryName']              = releaseConfig['binaryName']
releaseConfig['ftpServer']                  = 'ftp.mozilla.org'
releaseConfig['stagingServer']              = 'stage-old.mozilla.org'
releaseConfig['talosTestPlatforms']         = ()
releaseConfig['unittestPlatforms']          = ()
releaseConfig['bouncerServer']              = 'download.mozilla.org'
releaseConfig['ausServerUrl']               = 'https://aus2-community.mozilla.org'
releaseConfig['testOlderPartials']          = True
releaseConfig['releaseNotesUrl']            = None
releaseConfig['useBetaChannel']             = 1
releaseConfig['verifyConfigs']              = {'linux':  'moz191-seamonkey-linux.cfg',
                                               'macosx': 'moz191-seamonkey-mac.cfg',
                                               'win32':  'moz191-seamonkey-win32.cfg'}
releaseConfig['majorUpdateRepoPath']        = 'releases/mozilla-release'
releaseConfig['majorPatcherToolsTag']       = 'UPDATE_PACKAGING_R11_1_MU'
releaseConfig['majorUpdateSourceRepoPath']  = 'releases/comm-release'
releaseConfig['majorUpdatePatcherConfig']   = 'moz191-seamonkey-branch-major-patcher2.cfg'
releaseConfig['majorUpdateVerifyConfigs']   = {'linux':  'moz191-seamonkey-linux-major.cfg',
                                               'macosx': 'moz191-seamonkey-mac-major.cfg',
                                               'win32':  'moz191-seamonkey-win32-major.cfg'}
releaseConfig['majorUpdateToVersion']       = '2.6.1'
releaseConfig['majorUpdateAppVersion']      = '2.6.1'
releaseConfig['majorUpdateBaseTag']         = 'SEAMONKEY_2_6_1'
releaseConfig['majorUpdateBuildNumber']     = 1
releaseConfig['majorUpdateReleaseNotesUrl'] = 'https://www.mozilla.org/start/unsupported/%locale%/index.html'

# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#releaseConfig['tuxedoConfig']              = 'seamonkey-tuxedo.ini'
#releaseConfig['tuxedoServerUrl']           = 'https://bounceradmin.mozilla.com/api/'
