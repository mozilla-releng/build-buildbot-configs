SLAVES = {
    'n810': ['maemo-n810-%02i' % x for x in range(1,41)],
}

BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.2': {},
    'tracemonkey'  : {},
}

#
# {{{1 mozilla-central
#
BRANCHES['mozilla-central']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-central']['graph_server'] = "graphs-stage-old.mozilla.org"
BRANCHES['mozilla-central']['platforms'] = {
    'n810': {},
}
BRANCHES['mozilla-central']['platforms']['n810']['base_name'] = 'Maemo mozilla-central'
BRANCHES['mozilla-central']['platforms']['n810']['slaves'] = SLAVES['n810']
BRANCHES['mozilla-central']['platforms']['n810']['buildbot_branch'] = 'maemo-trunk'
BRANCHES['mozilla-central']['platforms']['n810']['talos_branch'] = 'mobile'
BRANCHES['mozilla-central']['platforms']['n810']['poll_interval'] = 5*60
BRANCHES['mozilla-central']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/mobile-trunk/',
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-trunk/',
]
BRANCHES['mozilla-central']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/mobile-trunk/',
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-trunk/',
]
BRANCHES['mozilla-central']['platforms']['n810']['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites'] = {
    'tp3': {},
    'non_tp1': {},
    'non_tp2': {},
}
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp3']['suite_name'] = 'N810 mozilla-central talos Tp3'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp3']['build_dir'] = 'n810-trunk-tp'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp3']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp3']['active_tests'] = {
    'tp':   90,
}
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp3']['disable_jit'] = False
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp1']['suite_name'] = 'N810 mozilla-central talos non-Tp1'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp1']['build_dir'] = 'n810-trunk-non-tp1'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp1']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp1']['active_tests'] = {
    'ts':   60,
#    'tpan':   60,
#    'tzoom':   60,
    'twinopen':   60,
    'tdhtml':   60,
}
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp1']['disable_jit'] = False
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp2']['suite_name'] = 'N810 mozilla-central talos non-Tp2'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp2']['build_dir'] = 'n810-trunk-non-tp2'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp2']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp2']['active_tests'] = {
    'tsvg':   60,
    'tsspider':   60,
    'tgfx':   60,
}
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['non_tp2']['disable_jit'] = False
BRANCHES['mozilla-central']['platforms']['n810']['test_suites'] = {
    'mochitest1': {},
    'mochitest2': {},
    'mochitest3': {},
    'mochitest4': {},
    'chrome':     {},
    'reftest':    {},
    'crashtest':  {},
    'xpcshell':   {},
}
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest1']['testType'] = "mochitest"
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest1']['totalClients'] = 4
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest1']['clientNumber'] = 1
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest1']['knownFailCount'] = 11
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest2']['testType'] = "mochitest"
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest2']['totalClients'] = 4
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest2']['clientNumber'] = 2
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest2']['knownFailCount'] = 223
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest3']['testType'] = "mochitest"
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest3']['totalClients'] = 4
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest3']['clientNumber'] = 3
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest3']['knownFailCount'] = 72
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest4']['testType'] = "mochitest"
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest4']['totalClients'] = 4
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest4']['clientNumber'] = 4
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['mochitest4']['knownFailCount'] = 188
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['chrome']['knownFailCount'] = 545
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['reftest']['knownFailCount'] = 98
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['crashtest']['knownFailCount'] = 4
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['xpcshell']['knownFailCount'] = 182

#
# {{{1 mozilla-1.9.2
#
BRANCHES['mozilla-1.9.2']['tinderbox_tree'] = "MozillaTest"
BRANCHES['mozilla-1.9.2']['graph_server'] = "graphs-stage-old.mozilla.org"
BRANCHES['mozilla-1.9.2']['platforms'] = {
    'n810': {},
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['base_name'] = 'Maemo mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['slaves'] = SLAVES['n810']
BRANCHES['mozilla-1.9.2']['platforms']['n810']['buildbot_branch'] = 'maemo-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_branch'] = 'mobile-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['poll_interval'] = 5*60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/mobile-1.9.2/',
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-1.9.2/',
]
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-1.9.2/',
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/mobile-1.9.2/',
]
BRANCHES['mozilla-1.9.2']['platforms']['n810']['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites'] = {
    'tp3': {},
    'non_tp1': {},
    'non_tp2': {},
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp3']['suite_name'] = 'N810 mozilla-1.9.2 talos Tp3'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp3']['build_dir'] = 'n810-1.9.2-tp'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp3']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp3']['active_tests'] = {
    'tp':   90,
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp3']['disable_jit'] = False
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp1']['suite_name'] = 'N810 mozilla-1.9.2 talos non-Tp1'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp1']['build_dir'] = 'n810-1.9.2-non-tp1'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp1']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp1']['active_tests'] = {
    'ts':   60,
#    'tpan':   60,
#    'tzoom':   60,
    'twinopen':   60,
    'tdhtml':   60,
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp1']['disable_jit'] = False
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp2']['suite_name'] = 'N810 mozilla-1.9.2 talos non-Tp2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp2']['build_dir'] = 'n810-1.9.2-non-tp2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp2']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp2']['active_tests'] = {
    'tsvg':   60,
    'tsspider':   60,
    'tgfx':   60,
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['non_tp2']['disable_jit'] = False
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites'] = {
    'mochitest1': {},
    'mochitest2': {},
    'mochitest3': {},
    'mochitest4': {},
    'chrome':     {},
    'reftest':    {},
    'crashtest':  {},
    'xpcshell':   {},
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest1']['testType'] = "mochitest"
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest1']['totalClients'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest1']['clientNumber'] = 1
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest1']['knownFailCount'] = 11
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest2']['testType'] = "mochitest"
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest2']['totalClients'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest2']['clientNumber'] = 2
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest2']['knownFailCount'] = 223
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest3']['testType'] = "mochitest"
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest3']['totalClients'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest3']['clientNumber'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest3']['knownFailCount'] = 72
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest4']['testType'] = "mochitest"
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest4']['totalClients'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest4']['clientNumber'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['mochitest4']['knownFailCount'] = 188
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['chrome']['knownFailCount'] = 545
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['reftest']['knownFailCount'] = 98
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['crashtest']['knownFailCount'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['xpcshell']['knownFailCount'] = 182

#
# {{{1 TraceMonkey
#
BRANCHES['tracemonkey']['tinderbox_tree'] = "MozillaTest"
BRANCHES['tracemonkey']['graph_server'] = "graphs-stage-old.mozilla.org"
BRANCHES['tracemonkey']['platforms'] = {
    'n810': {},
}
BRANCHES['tracemonkey']['platforms']['n810']['base_name'] = 'Maemo tracemonkey'
BRANCHES['tracemonkey']['platforms']['n810']['slaves'] = SLAVES['n810']
BRANCHES['tracemonkey']['platforms']['n810']['buildbot_branch'] = 'maemo-tm'
BRANCHES['tracemonkey']['platforms']['n810']['talos_branch'] = 'mobile-tracemonkey'
BRANCHES['tracemonkey']['platforms']['n810']['poll_interval'] = 5*60
BRANCHES['tracemonkey']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/mobile-tracemonkey/',
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-tracemonkey/',
]
BRANCHES['tracemonkey']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/tinderbox-builds/mobile-tracemonkey/',
    'http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mobile-tracemonkey/',
]
BRANCHES['tracemonkey']['platforms']['n810']['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites'] = {
    'tp3': {},
    'non_tp1': {},
    'non_tp2': {},
}
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp3']['suite_name'] = 'N810 tracemonkey talos Tp3'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp3']['build_dir'] = 'n810-tm-tp'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp3']['config_file'] = 'mobile-tracemonkey.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp3']['active_tests'] = {
    'tp':   90,
}
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp3']['disable_jit'] = False
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp1']['suite_name'] = 'N810 tracemonkey talos non-Tp1'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp1']['build_dir'] = 'n810-tm-non-tp1'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp1']['config_file'] = 'mobile-tracemonkey.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp1']['active_tests'] = {
    'ts':   60,
#    'tpan':   60,
#    'tzoom':   60,
    'twinopen':   60,
    'tdhtml':   60,
}
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp1']['disable_jit'] = False
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp2']['suite_name'] = 'N810 tracemonkey talos non-Tp2'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp2']['build_dir'] = 'n810-tm-non-tp2'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp2']['config_file'] = 'mobile-tracemonkey.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp2']['active_tests'] = {
    'tsvg':   60,
    'tsspider':   60,
    'tgfx':   60,
}
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['non_tp2']['disable_jit'] = False
BRANCHES['tracemonkey']['platforms']['n810']['test_suites'] = {
    'mochitest1': {},
    'mochitest2': {},
    'mochitest3': {},
    'mochitest4': {},
    'chrome':     {},
    'reftest':    {},
    'crashtest':  {},
    'xpcshell':   {},
}
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest1']['testType'] = "mochitest"
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest1']['totalClients'] = 4
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest1']['clientNumber'] = 1
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest1']['knownFailCount'] = 11
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest2']['testType'] = "mochitest"
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest2']['totalClients'] = 4
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest2']['clientNumber'] = 2
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest2']['knownFailCount'] = 223
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest3']['testType'] = "mochitest"
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest3']['totalClients'] = 4
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest3']['clientNumber'] = 3
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest3']['knownFailCount'] = 72
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest4']['testType'] = "mochitest"
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest4']['totalClients'] = 4
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest4']['clientNumber'] = 4
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['mochitest4']['knownFailCount'] = 188
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['chrome']['knownFailCount'] = 545
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['reftest']['knownFailCount'] = 98
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['crashtest']['knownFailCount'] = 4
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['xpcshell']['knownFailCount'] = 182
