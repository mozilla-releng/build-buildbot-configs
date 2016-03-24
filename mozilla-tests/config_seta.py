import json
import urllib2
from datetime import date
import os
import re
import time
import socket


seta_branches = ['fx-team', 'mozilla-inbound']
# todo: should get platform names from PLATFORMS in config.py

today = date.today().strftime("%Y-%m-%d")
# android has different slave platforms within the same opt|debug list
seta_platforms = {"Rev4 MacOSX Snow Leopard 10.6": ("macosx64", ["snowleopard"]),
                  "Windows XP 32-bit": ("win32", ["xp-ix"]),
                  "Windows 7 32-bit": ("win32", ["win7-ix"]),
                  "Windows 8 64-bit": ("win64", ["win8_64"]),
                  "Ubuntu VM 12.04": ("linux", ["ubuntu32_vm"]),
                  "Ubuntu VM 12.04 x64": ("linux64", ["ubuntu64_vm", "ubuntu64_vm_lnx_large"]),
                  "Ubuntu HW 12.04 x64": ("linux64", ["ubuntu64_hw"]),
                  "Ubuntu ASAN VM 12.04 x64": ("linux64-asan", ["ubuntu64-asan_vm", "ubuntu64-asan_vm_lnx_large"]),
                  "Ubuntu TSAN VM 12.04 x64": ("linux64-tsan", ["ubuntu64_vm", "ubuntu64_vm_lnx_large"]),
                  "Rev7 MacOSX Yosemite 10.10.5": ("macosx64", ["yosemite_r7"]),
                  "Ubuntu Code Coverage VM 12.04 x64": ("linux64-cc", ["ubuntu64_vm", "ubuntu64_vm_lnx_large"]),
                  "android-4-3-armv7-api11": ("android-api-15", ["ubuntu64_vm_armv7_mobile", "ubuntu64_vm_armv7_large"]),
                  "android-4-3-armv7-api15": ("android-api-15", ["ubuntu64_vm_armv7_mobile", "ubuntu64_vm_armv7_large"])
                  }

# platforms and tests to exclude from configs because they are deprecated or lacking data
platform_exclusions = ["android-2-3-armv7-api9"]
test_exclusions = re.compile('\[funsize\]|\[TC\]')

# define seta branches and default values for skipcount and skiptimeout
skipconfig_defaults_platform = {}
for sp in seta_platforms:
    for slave_sp in seta_platforms[sp][1]:
        if slave_sp in ["xp-ix"]:
            skipconfig_defaults_platform[slave_sp] = (14, 7200)
        else:
            skipconfig_defaults_platform[slave_sp] = (7, 3600)


def wfetch(url, retries=5):
    while True:
        try:
            response = urllib2.urlopen(url, timeout=30)
            return json.loads(response.read())
        except urllib2.HTTPError, e:
            print("Failed to fetch '%s': %s" % (url, str(e)))
        except urllib2.URLError, e:
            print("Failed to fetch '%s': %s" % (url, str(e)))
        except socket.timeout, e:
            print("Time out accessing %s: %s" % (url, str(e)))
        except socket.error, e:
            print("Socket error when accessing %s: %s" % (url, str(e)))
        except ValueError, e:
            print("JSON parsing error %s: %s" % (url, str(e)))
        if retries < 1:
            raise Exception("Could not fetch url '%s'" % url)
        retries -= 1
        print("Retrying")
        time.sleep(60)


def get_seta_platforms(branch, platform_filter):
    # For offline work
    if os.environ.get('DISABLE_SETA'):
        return []

    url = "http://alertmanager.allizom.org/data/setadetails/?date=" + today + "&buildbot=1&branch=" + branch + "&inactive=1"
    data = wfetch(url)
    c['jobtypes'] = data.get('jobtypes', None)
    platforms = []
    for p in c['jobtypes'][today]:
        platform = p.encode('utf-8').split(branch)[0].rstrip()
        if platform in platform_exclusions:
            continue
        if platform_filter == "mobile" and "android" not in platform:
            continue
        if platform_filter == "desktop" and "android" in platform:
            continue
        if platform not in platforms:
            platforms.append(platform)
    return(platforms)


def sort_android_tests(platform, worker_platform, tests):
    """create a dictionary that maps slave platform to tests"""
    """initialize the dictionary of tests per platform"""
    tests_by_worker_platform = {}
    for s in worker_platform:
        tests_by_worker_platform[s] = []
    for t in tests:
        if any([t.split()[-1].startswith(target) for target in ['plain-reftest', 'crashtest', 'jsreftest']]):
            tests_by_worker_platform[worker_platform[1]].append(t)
        else:
            tests_by_worker_platform[worker_platform[0]].append(t)
    return tests_by_worker_platform


def print_configs(branch, plat, test_dict, BRANCHES):

    for sp in test_dict:
        test_config = {}
        for t in test_dict[sp]:
            test = t.split()[-1]
            test_type = (t.split(branch)[1]).split()[0]
            test_config[test_type, test] = skipconfig_defaults_platform[str(sp)]
        BRANCHES[branch]['platforms'][plat][str(sp)]['skipconfig'] = test_config


def define_configs(branch, platforms, BRANCHES):

    for p in platforms:
        tests = []
        for job in c['jobtypes'][today]:
            if p in platform_exclusions:
                continue
            if re.search(test_exclusions, job):
                continue
            if p in job:
                tests.append(job.encode('utf-8'))

        if not tests:
            continue

        test_dict = {}
        tests_sorted = sorted(tests)
        platform = seta_platforms[p][0]
        if (len(seta_platforms[p][1])) == 1:
            worker_platform = seta_platforms[p][1][0]
            test_dict[worker_platform] = tests_sorted
        else:
            worker_platform = seta_platforms[p][1]
            test_dict = sort_android_tests(platform, worker_platform, tests_sorted)

        print_configs(branch, platform, test_dict, BRANCHES)


c = {}


def loadSkipConfig(BRANCHES, platform_filter):
    """arguments are desktop|android"""
    for b in seta_branches:
        platforms = get_seta_platforms(b, platform_filter)
        if platforms:
            define_configs(b, platforms, BRANCHES)
