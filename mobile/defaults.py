from copy import deepcopy
#
# {{{1 Platform Defaults
#
default_platform = {}
default_platform['slaves'] = []
default_platform['poll_interval'] = 5*60
default_platform['reboot'] = True
default_platform['reboot_cmd'] = ['sudo', 'reboot-user']
default_platform['disable_scaling'] = False
default_platform['nightly'] = True
default_platform['per_checkin'] = True
default_platform['unit_build_dirs'] = []
default_platform['talos_build_dirs'] = []
default_platform['browser_wait'] = 20
default_platform['talos_suites'] = {
    'tp4': {},
    'tp4_nochrome': {},
    'tpan': {},
    'tzoom': {},
    'ts': {},
    'twinopen': {},
    'tdhtml': {},
    'tsvg': {},
    'tsspider': {},
#    'tgfx': {},
}
default_platform['talos_suites']['tp4']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tp4']['timeout'] = 1.5*60*60
default_platform['talos_suites']['tp4']['nochrome'] = False
default_platform['talos_suites']['tp4_nochrome']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tp4_nochrome']['timeout'] = 1.5*60*60
default_platform['talos_suites']['tp4_nochrome']['nochrome'] = True
default_platform['talos_suites']['tpan']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tpan']['timeout'] = 1.5*60*60
default_platform['talos_suites']['tpan']['nochrome'] = True
default_platform['talos_suites']['tzoom']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tzoom']['timeout'] = 1.5*60*60
default_platform['talos_suites']['tzoom']['nochrome'] = True
default_platform['talos_suites']['ts']['config_file'] = 'mobile.config'
default_platform['talos_suites']['ts']['timeout'] = 60*60
default_platform['talos_suites']['ts']['nochrome'] = False
default_platform['talos_suites']['twinopen']['config_file'] = 'mobile.config'
default_platform['talos_suites']['twinopen']['timeout'] = 60*60
default_platform['talos_suites']['twinopen']['nochrome'] = False
default_platform['talos_suites']['tdhtml']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tdhtml']['timeout'] = 60*60
default_platform['talos_suites']['tdhtml']['nochrome'] = True
default_platform['talos_suites']['tsvg']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tsvg']['timeout'] = 60*60
default_platform['talos_suites']['tsvg']['nochrome'] = True
default_platform['talos_suites']['tsspider']['config_file'] = 'mobile.config'
default_platform['talos_suites']['tsspider']['timeout'] = 60*60
default_platform['talos_suites']['tsspider']['nochrome'] = True
#default_platform['talos_suites']['tgfx']['config_file'] = 'mobile.config'
#default_platform['talos_suites']['tgfx']['timeout'] = 60*60
#default_platform['talos_suites']['tgfx']['nochrome'] = True

default_platform['test_suites'] = {
    'mochitest1': {}, #Enabled for testing my factory/config changes.
    'mochitest2': {},
    'mochitest3': {},
    'mochitest4': {},
#    'chrome':     {},
    'browser-chrome': {},
#bug632903    'reftest':    {},
#    'crashtest':  {},
#    'xpcshell':   {},
}
default_platform['test_suites']['mochitest1']['test_type'] = "mochitest"
default_platform['test_suites']['mochitest1']['timeout'] = 60*60
default_platform['test_suites']['mochitest1']['clients'] = (1,4) #i.e. 1 of 4
default_platform['test_suites']['mochitest1']['known_fail_count'] = 0
default_platform['test_suites']['mochitest2']['test_type'] = "mochitest"
default_platform['test_suites']['mochitest2']['timeout'] = 60*60
default_platform['test_suites']['mochitest2']['clients'] = (2,4)
default_platform['test_suites']['mochitest2']['known_fail_count'] = 0
default_platform['test_suites']['mochitest3']['test_type'] = "mochitest"
default_platform['test_suites']['mochitest3']['timeout'] = 60*60
default_platform['test_suites']['mochitest3']['clients'] = (3,4)
default_platform['test_suites']['mochitest3']['known_fail_count'] = 0
default_platform['test_suites']['mochitest4']['test_type'] = "mochitest"
default_platform['test_suites']['mochitest4']['timeout'] = 60*60
default_platform['test_suites']['mochitest4']['clients'] = (4,4)
default_platform['test_suites']['mochitest4']['known_fail_count'] = 0
#default_platform['test_suites']['chrome']['test_type'] = 'chrome'
#default_platform['test_suites']['chrome']['timeout'] = 60*60
#default_platform['test_suites']['chrome']['known_fail_count'] = 545
default_platform['test_suites']['browser-chrome']['test_type'] = 'browser-chrome'
default_platform['test_suites']['browser-chrome']['timeout'] = 60*60
default_platform['test_suites']['browser-chrome']['known_fail_count'] = 0
#default_platform['test_suites']['reftest']['test_type'] = 'reftest'
#default_platform['test_suites']['reftest']['timeout'] = 60*60
#default_platform['test_suites']['reftest']['known_fail_count'] = 310
#default_platform['test_suites']['crashtest']['test_type'] = 'crashtest'
#default_platform['test_suites']['crashtest']['timeout'] = 60*60
#default_platform['test_suites']['crashtest']['known_fail_count'] = 0
#default_platform['test_suites']['xpcshell']['test_type'] = 'xpcshell'
#default_platform['test_suites']['xpcshell']['timeout'] = 60*60
#default_platform['test_suites']['xpcshell']['known_fail_count'] = 0

#
# {{{2 Nokia N810 Specializations
#
default_n810 = deepcopy(default_platform)
default_n810['talos_tarball'] = 'http://10.250.48.135/maemo/talos.tar.bz2'
default_n810['pageloader_tarball'] = 'http://10.250.48.135/maemo/pageloader.tar.bz2'
default_n810['maemkit_tarball'] = 'http://10.250.48.135/maemo/maemkit.tar.bz2'
default_n810['tp4_tarball'] = 'http://10.250.48.135/maemo/tp4.tar.bz2'
default_n810['tp4_parent_dir'] = '/tools'
default_n810['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
default_n810['disable_scaling'] = True
default_n810['reboot'] = True
default_n810['reboot_cmd'] = ['sudo', 'reboot-user']
default_n810['browser_wait'] = 20
default_n810['env'] = {
    #Turns out that this variable is critical but isn't set properly
    #by running buildbot, even though a standard environment should
    #be set up by running buildbot under sudo
    'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/tmp/session_bus_socket'
}

#
# {{{2 Nokia N900 Specializations
#
default_n900 = deepcopy(default_platform)
default_n900['talos_tarball'] = 'http://10.250.48.135/maemo5/talos.tar.bz2'
default_n900['pageloader_tarball'] = 'http://10.250.48.135/maemo5/pageloader.tar.bz2'
default_n900['maemkit_tarball'] = 'http://10.250.48.135/maemo5/maemkit.tar.bz2'
default_n900['tp4_tarball'] = 'http://10.250.48.135/maemo5/tp4.tar.bz2'
default_n900['tp4_parent_dir'] = '/home/user'
default_n900['reboot'] = True
default_n900['reboot_cmd'] = ['sudo', 'reboot-user']
default_n900['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'

