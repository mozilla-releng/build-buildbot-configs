import json
import urllib2
import httplib
from datetime import date
import sys
import os


seta_branches = ['fx-team', 'mozilla-inbound']
# todo: should get platform names from PLATFORMS in config.py

today = date.today().strftime("%Y-%m-%d")
#android has different slave platforms within the same opt|debug list
seta_platforms = {"Rev4 MacOSX Snow Leopard 10.6": ("macosx64", ["snowleopard"]),
                  "Windows XP 32-bit": ("win32", ["xp-ix"]),
                  "Windows 7 32-bit": ("win32", ["win7-ix"]),
                  "Windows 8 64-bit": ("win64", ["win8_64"]),
                  "Ubuntu VM 12.04": ("linux", ["ubuntu32_vm"]),
                  "Ubuntu VM 12.04 x64": ("linux64", ["ubuntu64_vm", "ubuntu64_vm_lnx_large"]),
                  "Ubuntu ASAN VM 12.04 x64": ("linux64-asan", ["ubuntu64-asan_vm", "ubuntu64-asan_vm_lnx_large"]),
                  "Ubuntu TSAN VM 12.04 x64": ("linux64-tsan", ["ubuntu64_vm", "ubuntu64_vm_lnx_large"]),
                  "Rev7 MacOSX Yosemite 10.10.5": ("macosx64", ["yosemite_r7"]),
                  "Ubuntu Code Coverage VM 12.04 x64": ("linux64-cc", ["ubuntu64_vm", "ubuntu64_vm_lnx_large"]),                  
                  "android-2-3-armv7-api9": ("android-api-9", ["ubuntu64_vm_mobile", "ubuntu64_vm_large"]),
                  "android-4-3-armv7-api15": ("android-api-15", ["ubuntu64_vm_armv7_mobile", "ubuntu64_vm_armv7_large"])                  
                  }

#define seta branches and default values for skipcount and skiptimeout
skipconfig_defaults_platform = {}
for sp in seta_platforms:
    if sp == "android-4-3-armv7-api15":
        continue
    for slave_sp in seta_platforms[sp][1]:
        if slave_sp in ["xp-ix"]:
            skipconfig_defaults_platform[slave_sp] = (14, 7200)
        else:
            skipconfig_defaults_platform[slave_sp] = (7, 3600)

def get_seta_platforms(branch, platform_filter):
    # For offline work
    if os.environ.get('DISABLE_SETA'):
        return []


    url = "http://alertmanager.allizom.org/data/setadetails/?date=" + today + "&buildbot=1&branch=" + branch + "&inactive=1"
    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print('HTTPError = ' + str(e.code))
        raise
    except urllib2.URLError, e:
        print('URLError = ' + str(e.reason))
        raise
    except httplib.HTTPException, e:
        print('HTTPException')
        raise
    except Exception:
        import traceback
        print('generic exception: ' + traceback.format_exc())
        raise
    data = json.loads(response.read())
    c['jobtypes'] = data.get('jobtypes', None)
    platforms = []
    for p in c['jobtypes'][today]:
        if "android-4-3-armv7-api15" in p:
            continue
        if 'talos' in p:
            platform = ' '.join(p.encode('utf-8').split()[0:-3])
        else:
            platform = ' '.join(p.encode('utf-8').split()[0:-4])
        if platform_filter == "mobile" and "android" not in platform:
            continue
        if platform_filter == "desktop" and "android" in platform:
            continue
        if platform not in platforms:
            platforms.append(platform)
    return(platforms)


def sort_android_tests(platform, slave_platform, tests):
    """create a dictionary that maps slave platform to tests"""
    """initialize the dictionary of tests per platform"""
    tests_by_slave_platform = {}
    for s in slave_platform:
        tests_by_slave_platform[s] = []
    for t in tests:
        if t.split()[-1].startswith('plain-reftest'):
            tests_by_slave_platform[slave_platform[1]].append(t)
        elif t.split()[-1].startswith('crashtest'):
            tests_by_slave_platform[slave_platform[1]].append(t)
        elif t.split()[-1].startswith('jsreftest'):
            tests_by_slave_platform[slave_platform[1]].append(t)
        else:
            tests_by_slave_platform[slave_platform[0]].append(t)
    return tests_by_slave_platform


def print_configs(branch, plat, test_dict, BRANCHES):

    for sp in test_dict:
        test_config = {}
        for t in test_dict[sp]:
            test = t.split()[-1]
            test_type = t.split()[-3]
            test_config[test_type, test] = skipconfig_defaults_platform[str(sp)]
            BRANCHES[branch]['platforms'][plat][str(sp)]['skipconfig'] = test_config


def define_configs(branch, platforms, BRANCHES):

    for p in platforms:
        tests = []
        for job in c['jobtypes'][today]:
            if "android-4-3-armv7-api15" in job:
                continue
            if p in job:
                tests.append(job.encode('utf-8'))
        test_dict = {}
        if len(tests) > 0:
            tests_sorted = sorted(tests)
            platform = seta_platforms[p][0]
            # temp fix for bug 1238752
            if platform == "android-api-15":
               continue
            if (len(seta_platforms[p][1])) == 1:
                slave_platform = seta_platforms[p][1][0]
                test_dict[slave_platform] = tests_sorted
            else:
                slave_platform = seta_platforms[p][1]
                test_dict = sort_android_tests(platform, slave_platform, tests_sorted)

            print_configs(branch, platform, test_dict, BRANCHES)

c = {}

def loadSkipConfig(BRANCHES, platform_filter):
    """arguments are desktop|android"""
    for b in seta_branches:
        platforms = get_seta_platforms(b, platform_filter)
        if platforms:
            define_configs(b, platforms, BRANCHES)
