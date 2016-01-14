releaseConfig = {}

# Release Notification
#  not used yet
# Basic product configuration
#  Names for the product/files
releaseConfig['productName']                = 'seamonkey'
releaseConfig['brandName']                  = 'SeaMonkey'
releaseConfig['appName']                    = 'suite'
releaseConfig['binaryName']                 = releaseConfig['brandName']
releaseConfig['oldBinaryName']              = releaseConfig['binaryName']
#  Current version info
releaseConfig['version']                    = '2.40'
releaseConfig['appVersion']                 = '2.40'
releaseConfig['milestone']                  = '43.0'
releaseConfig['buildNumber']                = 2 
releaseConfig['baseTag']                    = 'SEAMONKEY_2_40'
#  Old version info
releaseConfig['oldVersion']                 = '2.39'
releaseConfig['oldAppVersion']              = '2.39'
releaseConfig['oldBuildNumber']             = 1
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_39'
releaseConfig['oldRepoPath']                = 'releases/comm-release'
#  Next (nightly) version info
#     not yet available
#  Repository configuration, for tagging
releaseConfig['skip_tag']                   = False 
releaseConfig['relbranchPrefix']            = 'SEA_COMM'
releaseConfig['sourceRepoName']             = 'comm-release' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'releases/comm-release'
releaseConfig['sourceRepoRevision']         = '860e55fe632e'
releaseConfig['relbranchOverride']          = ''
releaseConfig['productVersionFile']         = 'suite/config/version.txt'
#releaseConfig['productVersionFile']         = ''
#   Mozilla
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-release'
releaseConfig['mozillaRepoRevision']        = 'FIREFOX_43_0_1_BUILD1'
releaseConfig['mozillaRelbranchOverride']   = '' # put Gecko relbranch here that we base upon
#   Inspector
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = 'SEA2_37_RELBRANCH'
releaseConfig['inspectorRelbranchOverride'] = ''
#   Venkman
releaseConfig['venkmanRepoPath']            = '' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = ''
releaseConfig['venkmanRelbranchOverride']   = ''
#   Chatzilla
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = 'CHATZILLA_0_9_92_RELEASE'
releaseConfig['chatzillaRelbranchOverride'] = ''
#  L10n repositories
releaseConfig['l10nRepoPath']               = 'releases/l10n/mozilla-release'
releaseConfig['l10nRelbranchOverride']      = ''
releaseConfig['l10nRevisionFile']           = 'l10n-changesets-comm-release'
#  Support repositories
#   not used yet

# Platform configuration
releaseConfig['enUSPlatforms']              = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['talosTestPlatforms']         = ()

# Unittests
releaseConfig['unittestPlatforms']          = ()

# L10n configuration
releaseConfig['l10nPlatforms']              = ('linux', 'win32', 'macosx64')
releaseConfig['mergeLocales']               = True

# Mercurial account
releaseConfig['hgUsername']                 = 'seabld'
releaseConfig['hgSshKey']                   = '~seabld/.ssh/seabld_dsa'

# Update-specific configuration
releaseConfig['patcherConfig']              = 'mozRelease-seamonkey-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']            = 'UPDATE_PACKAGING_R18'
releaseConfig['ftpServer']                  = 'ftp.mozilla.org'
releaseConfig['stagingServer']              = 'stage.mozilla.org'
releaseConfig['bouncerServer']              = 'download.mozilla.org'
releaseConfig['ausServerUrl']               = 'https://aus2-community.mozilla.org'
releaseConfig['testOlderPartials']          = False
releaseConfig['releaseNotesUrl']            = None
releaseConfig['releaseChannel']             = 'release'
releaseConfig['verifyConfigs']              = {
    'linux': 'mozRelease-seamonkey-linux.cfg',
    'macosx64': 'mozRelease-seamonkey-mac64.cfg',
    'win32': 'mozRelease-seamonkey-win32.cfg'
}
releaseConfig['mozconfigs']                 = {
    'linux': 'suite/config/mozconfigs/linux32/release',
    'linux64': 'suite/config/mozconfigs/linux64/release',
    'macosx64': 'suite/config/mozconfigs/macosx-universal/release',
    'win32': 'suite/config/mozconfigs/win32/release',
}

# Source step requires a properly configured source tree in order
# to upload the tarball.  re: bug 1118778
releaseConfig['source_mozconfig'] = releaseConfig['mozconfigs']['linux64']

# Major update configuration
releaseConfig['majorUpdateRepoPath']        = None

# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#releaseConfig['tuxedoConfig']              = 'seamonkey-tuxedo.ini'
#releaseConfig['tuxedoServerUrl']           = 'https://bounceradmin.mozilla.com/api/'

# Mock
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux', 'linux64')
