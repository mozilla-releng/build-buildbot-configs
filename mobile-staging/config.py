SLAVES = {
    'n810': ['maemo-n810-%02i' % x for x in [1,3,4,5,6] + range(9,81)],
    'n900': ['n900-%03i' % x for x in range(1,21)],
}

BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.2': {},
    'tracemonkey'  : {},
    'electrolysis': {},
    'places': {},
    'lorentz': {},
    'try': {},
}

#
# {{{1 Branch Defaults
#
defaultBranch = {}
defaultBranch['tinderbox_tree'] = "MozillaTest"
defaultBranch['graph_server'] = "graphs-stage.mozilla.org" 
defaultBranch['platforms'] = {}
defaultBranch['buildbot_branch'] = 'default_branch'

#
# {{{1 Platform Defaults
#
defaultPlatform = {}
defaultPlatform['slaves'] = []
defaultPlatform['talos_branch'] = 'talos_branch'
defaultPlatform['poll_interval'] = 5*60
defaultPlatform['reboot'] = True
defaultPlatform['rebootCmd'] = 'reboot ; sleep 600'
defaultPlatform['poller_string'] = 'invalid.nonexistant' #For overriding
defaultPlatform['talos_suites'] = {
    'tp4': {},
    'tp4_nochrome': {},
    'tpan': {},
    'tzoom': {},
    'ts': {},
    'twinopen': {},
    'tdhtml': {},
    'tsvg': {},
    'tsspider': {},
    'tgfx': {},
}
defaultPlatform['talos_suites']['tp4']['suite_name'] = 'talos Tp4'
defaultPlatform['talos_suites']['tp4']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['tp4']['timeout'] = 90
defaultPlatform['talos_suites']['tp4_nochrome']['suite_name'] = 'talos Tp4 nochrome'
defaultPlatform['talos_suites']['tp4_nochrome']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['tp4_nochrome']['timeout'] = 90
defaultPlatform['talos_suites']['tpan']['suite_name'] = 'talos Tpan'
defaultPlatform['talos_suites']['tpan']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['tpan']['timeout'] = 90
defaultPlatform['talos_suites']['tzoom']['suite_name'] = 'talos Tzoom'
defaultPlatform['talos_suites']['tzoom']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['tzoom']['timeout'] = 90
defaultPlatform['talos_suites']['ts']['suite_name'] = 'talos Ts'
defaultPlatform['talos_suites']['ts']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['ts']['timeout'] = 60
defaultPlatform['talos_suites']['twinopen']['suite_name'] = 'talos Twinopen'
defaultPlatform['talos_suites']['twinopen']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['twinopen']['timeout'] = 60
defaultPlatform['talos_suites']['tdhtml']['suite_name'] = 'talos Tdhtml'
defaultPlatform['talos_suites']['tdhtml']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['tdhtml']['timeout'] = 60
defaultPlatform['talos_suites']['tsvg']['suite_name'] = 'talos Tsvg'
defaultPlatform['talos_suites']['tsvg']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['tsvg']['timeout'] = 60
defaultPlatform['talos_suites']['tsspider']['suite_name'] = 'talos Tsspider'
defaultPlatform['talos_suites']['tsspider']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['tsspider']['timeout'] = 60
defaultPlatform['talos_suites']['tgfx']['suite_name'] = 'talos Tgfx'
defaultPlatform['talos_suites']['tgfx']['config_file'] = 'mobile.config'
defaultPlatform['talos_suites']['tgfx']['timeout'] = 60
defaultPlatform['test_suites'] = {
    'mochitest1': {},
    'mochitest2': {},
    'mochitest3': {},
    'mochitest4': {},
    'chrome':     {},
    'reftest':    {},
    'crashtest':  {},
    'xpcshell':   {},
}
defaultPlatform['test_suites']['mochitest1']['testType'] = "mochitest"
defaultPlatform['test_suites']['mochitest1']['totalClients'] = 4
defaultPlatform['test_suites']['mochitest1']['clientNumber'] = 1
defaultPlatform['test_suites']['mochitest1']['knownFailCount'] = 11
defaultPlatform['test_suites']['mochitest2']['testType'] = "mochitest"
defaultPlatform['test_suites']['mochitest2']['totalClients'] = 4
defaultPlatform['test_suites']['mochitest2']['clientNumber'] = 2
defaultPlatform['test_suites']['mochitest2']['knownFailCount'] = 223
defaultPlatform['test_suites']['mochitest3']['testType'] = "mochitest"
defaultPlatform['test_suites']['mochitest3']['totalClients'] = 4
defaultPlatform['test_suites']['mochitest3']['clientNumber'] = 3
defaultPlatform['test_suites']['mochitest3']['knownFailCount'] = 72
defaultPlatform['test_suites']['mochitest4']['testType'] = "mochitest"
defaultPlatform['test_suites']['mochitest4']['totalClients'] = 4
defaultPlatform['test_suites']['mochitest4']['clientNumber'] = 4
defaultPlatform['test_suites']['mochitest4']['knownFailCount'] = 188
defaultPlatform['test_suites']['chrome']['knownFailCount'] = 545
defaultPlatform['test_suites']['reftest']['knownFailCount'] = 98
defaultPlatform['test_suites']['crashtest']['knownFailCount'] = 4
defaultPlatform['test_suites']['xpcshell']['knownFailCount'] = 182

#
# {{{2 Nokia N810 Specializations
#
defaultN810 = deepcopy(defaultPlatform)
defaultN810['talos_scripts'] = 'http://staging-mobile-master.build.mozilla.org/maemo/talos.tar.bz2'
defaultN810['talos_pageloader'] = 'http://staging-mobile-master.build.mozilla.org/maemo/pageloader.tar.bz2'
defaultN810['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
defaultN810['slaves'] = SLAVES['n810']

#
# {{{2 Nokia N900 Specializations
#
defaultN900 = deepcopy(defaultPlatform)
default['rebootCmd'] = "sudo reboot-user ; sleep 600"
defaultN900['talos_scripts'] = 'http://staging-mobile-master.build.mozilla.org/maemo/talos.tar.bz2'
defaultN900['talos_pageloader'] = 'http://staging-mobile-master.build.mozilla.org/maemo/pageloader.tar.bz2'
defaultN900['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2' #May need to specialize this for QT
defaultN900['slaves'] = SLAVES['n900']


# {{{1 Mozilla Central
BRANCHES['mozilla-central'] = deepcopy(defaultBranch)
#TODO: BRANCHES['mozilla-central']['tinderbox_tree'] = "LALA"
BRANCHES['mozilla-central']['talos_branch'] = 'mobile'

# {{{2 Mozilla Central n810 GTK Specializations
BRANCHES['mozilla-central']['platforms'].update({'n810': deepcopy(defaultN810)})
BRANCHES['mozilla-central']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-trunk/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-trunk/',
]
BRANCHES['mozilla-central']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-trunk/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-trunk/',
]

#
# {{{2 Mozilla Central n900 GTK Specializations
# When Maemo 5 builds start happening, change the *_build_dirs to be n900 ones
BRANCHES['mozilla-central']['platforms'].update({'n900': deepcopy(defaultN900)})
BRANCHES['mozilla-central']['platforms']['n900']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-trunk/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-trunk/',
]
BRANCHES['mozilla-central']['platforms']['n900']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-trunk/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-trunk/',
]

#
# {{{2 Mozilla Central n900 QT Specializations
# Until QT builds start showing up, this will poll and find nothing
BRANCHES['mozilla-central']['platforms'].update({'n900-qt': deepcopy(defaultN900)}
BRANCHES['mozilla-central']['platforms']['n900-qt']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-trunk-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-trunk-qt/',
]
BRANCHES['mozilla-central']['platforms']['n900-qt']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-trunk-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-trunk-qt/',
]

# {{{1 Tracemonkey
BRANCHES['tracemonkey'] = deepcopy(defaultBranch)
#TODO: BRANCHES['tracemonkey']['tinderbox_tree'] = "LALA"
BRANCHES['tracemonkey']['talos_branch'] = 'mobile'

# {{{2 Tracemonkey n810 GTK Specializations
BRANCHES['tracemonkey']['platforms'].update({'n810': deepcopy(defaultN810)})
BRANCHES['tracemonkey']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-tracemonkey/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-tracemonkey/',
]
BRANCHES['tracemonkey']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-tracemonkey/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-tracemonkey/',
]

#
# {{{2 Tracemonkey n900 GTK Specializations
# When Maemo 5 builds start happening, change the *_build_dirs to be n900 ones
BRANCHES['tracemonkey']['platforms'].update({'n900': deepcopy(defaultN900)})
BRANCHES['tracemonkey']['platforms']['n900']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-tracemonkey/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-tracemonkey/',
]
BRANCHES['tracemonkey']['platforms']['n900']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-tracemonkey/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-tracemonkey/',
]

#
# {{{2 Tracemonkey n900 QT Specializations
# Until QT builds start showing up, this will poll and find nothing
BRANCHES['tracemonkey']['platforms'].update({'n900-qt': deepcopy(defaultN900)}
BRANCHES['tracemonkey']['platforms']['n900-qt']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-tracemonkey-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-tracemonkey-qt/',
]
BRANCHES['tracemonkey']['platforms']['n900-qt']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-tracemonkey-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-tracemonkey-qt/',
]

# {{{1 Electrolysis
BRANCHES['electrolysis'] = deepcopy(defaultBranch)
#TODO: BRANCHES['electrolysis']['tinderbox_tree'] = "LALA"
BRANCHES['electrolysis']['talos_branch'] = 'mobile'

# {{{2 Electrolysis n810 GTK Specializations
BRANCHES['electrolysis']['platforms'].update({'n810': deepcopy(defaultN810)})
BRANCHES['electrolysis']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-electrolysis/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-electrolysis/',
]
BRANCHES['electrolysis']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-electrolysis/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-electrolysis/',
]

#
# {{{2 Electrolysis n900 GTK Specializations
# When Maemo 5 builds start happening, change the *_build_dirs to be n900 ones
BRANCHES['electrolysis']['platforms'].update({'n900': deepcopy(defaultN900)})
BRANCHES['electrolysis']['platforms']['n900']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-electrolysis/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-electrolysis/',
]
BRANCHES['electrolysis']['platforms']['n900']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-electrolysis/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-electrolysis/',
]

#
# {{{2 Electrolysis n900 QT Specializations
# Until QT builds start showing up, this will poll and find nothing
BRANCHES['electrolysis']['platforms'].update({'n900-qt': deepcopy(defaultN900)}
BRANCHES['electrolysis']['platforms']['n900-qt']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-electrolysis-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-electrolysis-qt/',
]
BRANCHES['electrolysis']['platforms']['n900-qt']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-electrolysis-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-electrolysis-qt/',
]


# {{{1 Lorentz
BRANCHES['lorentz'] = deepcopy(defaultBranch)
#TODO: BRANCHES['lorentz']['tinderbox_tree'] = "LALA"
BRANCHES['lorentz']['talos_branch'] = 'mobile'

# {{{2 Lorentz n810 GTK Specializations
BRANCHES['lorentz']['platforms'].update({'n810': deepcopy(defaultN810)})
BRANCHES['lorentz']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-lorentz/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-lorentz/',
]
BRANCHES['lorentz']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-lorentz/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-lorentz/',
]

#
# {{{2 Lorentz n900 GTK Specializations
# When Maemo 5 builds start happening, change the *_build_dirs to be n900 ones
BRANCHES['lorentz']['platforms'].update({'n900': deepcopy(defaultN900)})
BRANCHES['lorentz']['platforms']['n900']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-lorentz/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-lorentz/',
]
BRANCHES['lorentz']['platforms']['n900']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-lorentz/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-lorentz/',
]

#
# {{{2 Lorentz n900 QT Specializations
# Until QT builds start showing up, this will poll and find nothing
BRANCHES['lorentz']['platforms'].update({'n900-qt': deepcopy(defaultN900)}
BRANCHES['lorentz']['platforms']['n900-qt']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-lorentz-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-lorentz-qt/',
]
BRANCHES['lorentz']['platforms']['n900-qt']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-lorentz-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-lorentz-qt/',
]


# {{{1 Places
BRANCHES['places'] = deepcopy(defaultBranch)
#TODO: BRANCHES['places']['tinderbox_tree'] = "LALA"
BRANCHES['places']['talos_branch'] = 'mobile'

# {{{2 Places n810 GTK Specializations
BRANCHES['places']['platforms'].update({'n810': deepcopy(defaultN810)})
BRANCHES['places']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-places/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-places/',
]
BRANCHES['places']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-places/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-places/',
]

#
# {{{2 Places n900 GTK Specializations
# When Maemo 5 builds start happening, change the *_build_dirs to be n900 ones
BRANCHES['places']['platforms'].update({'n900': deepcopy(defaultN900)})
BRANCHES['places']['platforms']['n900']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-places/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-places/',
]
BRANCHES['places']['platforms']['n900']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-places/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-places/',
]

#
# {{{2 Places n900 QT Specializations
# Until QT builds start showing up, this will poll and find nothing
BRANCHES['places']['platforms'].update({'n900-qt': deepcopy(defaultN900)}
BRANCHES['places']['platforms']['n900-qt']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-places-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-places-qt/',
]
BRANCHES['places']['platforms']['n900-qt']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-places-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-places-qt/',
]

# {{{1 Try
BRANCHES['try'] = deepcopy(defaultBranch)
#TODO: BRANCHES['try']['tinderbox_tree'] = "LALA"
BRANCHES['try']['talos_branch'] = 'mobile'

# {{{2 Try n810 GTK Specializations
BRANCHES['try']['platforms'].update({'n810': deepcopy(defaultN810)})
BRANCHES['try']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-try/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-try/',
]
BRANCHES['try']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-try/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-try/',
]

#
# {{{2 Try n900 GTK Specializations
# When Maemo 5 builds start happening, change the *_build_dirs to be n900 ones
BRANCHES['try']['platforms'].update({'n900': deepcopy(defaultN900)})
BRANCHES['try']['platforms']['n900']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-try/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-try/',
]
BRANCHES['try']['platforms']['n900']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-try/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-try/',
]

#
# {{{2 Try n900 QT Specializations
# Until QT builds start showing up, this will poll and find nothing
BRANCHES['try']['platforms'].update({'n900-qt': deepcopy(defaultN900)}
BRANCHES['try']['platforms']['n900-qt']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-try-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-try-qt/',
]
BRANCHES['try']['platforms']['n900-qt']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-try-qt/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-try-qt/',
]







