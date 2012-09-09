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
releaseConfig['version']                    = '2.12.1'
releaseConfig['appVersion']                 = '2.12.1'
releaseConfig['milestone']                  = '15.0.1'
releaseConfig['buildNumber']                = 2
releaseConfig['baseTag']                    = 'SEAMONKEY_2_12_1'
#  Old version info
releaseConfig['oldVersion']                 = '2.12'
releaseConfig['oldAppVersion']              = '2.12'
releaseConfig['oldBuildNumber']             = 1
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_12'
releaseConfig['oldRepoPath']                = 'releases/comm-release'
#  Next (nightly) version info
#     not yet available
#  Repository configuration, for tagging
releaseConfig['skip_tag']                   = False
releaseConfig['relbranchPrefix']            = 'SEA_COMM'
releaseConfig['sourceRepoName']             = 'comm-release' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'releases/comm-release'
releaseConfig['sourceRepoRevision']         = '378bed8d856f'
releaseConfig['relbranchOverride']          = 'SEA_COMM150_20120907_RELBRANCH'
releaseConfig['productVersionFile']         = 'suite/config/version.txt'
#releaseConfig['productVersionFile']         = ''
#   Mozilla
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-release'
releaseConfig['mozillaRepoRevision']        = 'a347058c607a'
releaseConfig['mozillaRelbranchOverride']   = 'COMM1501_2012090708_RELBRANCH' # put Gecko relbranch here that we base upon
#   Inspector
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = '869a1de4fc3f'
releaseConfig['inspectorRelbranchOverride'] = 'DOMI_2_0_13'
#   Venkman
releaseConfig['venkmanRepoPath']            = 'venkman' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = '6fcfa71a2039'
releaseConfig['venkmanRelbranchOverride']   = 'SEA2_12_RELBRANCH'
#   Chatzilla
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = 'e25c0b12b768'
releaseConfig['chatzillaRelbranchOverride'] = 'SEA2_12_RELBRANCH'
#  L10n repositories
releaseConfig['l10nRepoPath']               = 'releases/l10n/mozilla-release'
releaseConfig['l10nRelbranchOverride']      = 'SEA_COMM150_20120907_RELBRANCH'
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
releaseConfig['cvsroot']                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
releaseConfig['patcherConfig']              = 'mozRelease-seamonkey-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']            = 'UPDATE_PACKAGING_R14'
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

# Major update configuration
releaseConfig['majorUpdateRepoPath']        = None

# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#releaseConfig['tuxedoConfig']              = 'seamonkey-tuxedo.ini'
#releaseConfig['tuxedoServerUrl']           = 'https://bounceradmin.mozilla.com/api/'
