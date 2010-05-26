from copy import deepcopy
#
# {{{1 Platform Defaults
#
default_platform = {}
default_platform['slaves'] = []
default_platform['ftp_dir'] = ''
default_platform['poll_interval'] = 5*60
default_platform['reboot'] = True
default_platform['reboot_cmd'] = ['sudo', 'reboot-user']
default_platform['poller_string'] = 'invalid.nonexistant' #For overriding
default_platform['disable_scaling'] = False
default_platform['nightly'] = True
default_platform['per_checkin'] = True
default_platform['unit_build_dirs'] = []
default_platform['talos_build_dirs'] = []
default_platform['browser_wait'] = 7
default_platform['talos_suites'] = {
#     'tp4': {},
#     'tp4_nochrome': {},
    'tpan': {},
    'tzoom': {},
    'ts': {},
    'twinopen': {},
    'tdhtml': {},
    'tsvg': {},
    'tsspider': {},
    'tgfx': {},
}
# default_platform['talos_suites']['tp4']['config_file'] = 'mobile.config'
# default_platform['talos_suites']['tp4']['timeout'] = 1.5*60*60
# default_platform['talos_suites']['tp4_nochrome']['config_file'] = 'mobile.config'
# default_platform['talos_suites']['tp4_nochrome']['timeout'] = 1.5*60*60
default_platform['talos_suites']['tpan']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tpan']['timeout'] = 1.5*60*60
default_platform['talos_suites']['tzoom']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tzoom']['timeout'] = 1.5*60*60
default_platform['talos_suites']['ts']['config_file'] = 'mobile.config'
default_platform['talos_suites']['ts']['timeout'] = 60*60
default_platform['talos_suites']['twinopen']['config_file'] = 'mobile.config'
default_platform['talos_suites']['twinopen']['timeout'] = 60*60
default_platform['talos_suites']['tdhtml']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tdhtml']['timeout'] = 60*60
default_platform['talos_suites']['tsvg']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tsvg']['timeout'] = 60*60
default_platform['talos_suites']['tsspider']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tsspider']['timeout'] = 60*60
default_platform['talos_suites']['tgfx']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tgfx']['timeout'] = 60*60

default_platform['test_suites'] = {
#547130    'mochitest1': {}, #Enabled for testing my factory/config changes.
#547130    'mochitest2': {},
#547130    'mochitest3': {},
#547130    'mochitest4': {},
#547130    'chrome':     {},
    'reftest':    {},
    'crashtest':  {},
    'xpcshell':   {},
}
#default_platform['test_suites']['mochitest1']['test_type'] = "mochitest"
#default_platform['test_suites']['mochitest1']['timeout'] = 60*60
#default_platform['test_suites']['mochitest1']['clients'] = (1,4) #i.e. 1 of 4
#default_platform['test_suites']['mochitest1']['known_fail_count'] = 11
#default_platform['test_suites']['mochitest2']['test_type'] = "mochitest"
#default_platform['test_suites']['mochitest2']['timeout'] = 60*60
#default_platform['test_suites']['mochitest2']['clients'] = (2,4)
#default_platform['test_suites']['mochitest2']['known_fail_count'] = 223
#default_platform['test_suites']['mochitest3']['test_type'] = "mochitest"
#default_platform['test_suites']['mochitest3']['timeout'] = 60*60
#default_platform['test_suites']['mochitest3']['clients'] = (3,4)
#default_platform['test_suites']['mochitest3']['known_fail_count'] = 72
#default_platform['test_suites']['mochitest4']['test_type'] = "mochitest"
#default_platform['test_suites']['mochitest4']['timeout'] = 60*60
#default_platform['test_suites']['mochitest4']['clients'] = (4,4)
#default_platform['test_suites']['mochitest4']['known_fail_count'] = 188
#default_platform['test_suites']['chrome']['test_type'] = 'mochitest'
#default_platform['test_suites']['chrome']['timeout'] = 60*60
#default_platform['test_suites']['chrome']['known_fail_count'] = 545
default_platform['test_suites']['reftest']['test_type'] = 'reftest'
default_platform['test_suites']['reftest']['timeout'] = 60*60
default_platform['test_suites']['reftest']['known_fail_count'] = 310
default_platform['test_suites']['crashtest']['test_type'] = 'crashtest'
default_platform['test_suites']['crashtest']['timeout'] = 60*60
default_platform['test_suites']['crashtest']['known_fail_count'] = 4
default_platform['test_suites']['xpcshell']['test_type'] = 'xpcshell'
default_platform['test_suites']['xpcshell']['timeout'] = 60*60
default_platform['test_suites']['xpcshell']['known_fail_count'] = 182

#
# {{{2 Nokia N810 Specializations
#
default_n810 = deepcopy(default_platform)
default_n810['talos_tarball'] = 'http://staging-mobile-master.build.mozilla.org/maemo/talos.tar.bz2'
default_n810['pageloader_tarball'] = 'http://staging-mobile-master.build.mozilla.org/maemo/pageloader.tar.bz2'
default_n810['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
default_n810['disable_scaling'] = True
default_n810['reboot'] = True
default_n810['reboot_cmd'] = 'reboot ; sleep 600'
default_n810['browser_wait'] = 20

#
# {{{2 Nokia N900 Specializations
#
default_n900 = deepcopy(default_platform)
default_n900['reboot'] = True
default_n900['reboot_cmd'] = ['sudo', 'reboot-user']
default_n900['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'

