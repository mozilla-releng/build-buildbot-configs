SLAVES = {
    'fedora': dict([("talos-r3-fed-%03i" % x, {}) for x in range(11,103) \
        if x not in [01, 02, 18, 57, 59, 70]]), # bug 799528, bug 731300, bug 731793, bug 753367, bug 779574, bug 740505
    'fedora64' : dict([("talos-r3-fed64-%03i" % x, {}) for x in range (37,72) \
        if x not in [32,58]]), # bug 785862, bug 751893
    'xp-ix': dict([("t-xp32-ix-%03i" % x, {}) for x in range(1,131)]),
    'win7-ix': dict([("t-w732-ix-%03i" % x, {}) for x in range(1,131)]),
    'win8': dict([("t-w864-ix-%03i" % x, {}) for x in range(1,131)]),
    'snowleopard':dict(
        [("talos-r4-snow-%03i" % x, {}) for x in range(1,171) if x not in [81, 84]] +
        [("t-snow-r4-%04i" % x, {}) for x in range(1,167)]
    ),
    'mountainlion': dict([("talos-mtnlion-r5-%03i" % x, {}) for x in range(1,90) \
        if x not in [87]]), # bug 786994
    'mavericks': dict([("t-mavericks-r5-%03i" % x, {}) for x in range(1,6)]),
    'tegra_android': dict([('tegra-%03i' % x, {'http_port': '30%03i' % x, 'ssl_port': '31%03i' % x}) \
        for x in range(31,371) \
        if x not in range(122,129) + [30,33,34,43,44,49,53,65,69,77,78,86,106,131,137,143,147,\
            153,156,161,162,175,176,180,184,185,186,193,197,198,202,203,204,205,222,224,\
            226,241,268,275,289,291,292,301,307,320,349,368]]), # decommissioned tegras
    'panda_android': dict(
        [('panda-%04i' % x, {'http_port': '30%03i' % x, 'ssl_port': '31%03i' % x}) \
            for x in range(22,257) + range(270,307) + range(320,874) + range(885,910)]
    ),
    'ubuntu32_vm': dict(
        [("tst-linux32-ec2-%03i" % x, {}) for x in range(1, 900)] +
        [("tst-linux32-spot-%03i" % x, {}) for x in range(1, 1000)]
    ),
    'ubuntu64_vm': dict(
        [("tst-linux64-ec2-%03i" % x, {}) for x in range(1, 900)] +
        [("tst-linux64-spot-%03i" % x, {}) for x in range(1, 1000)]
    ),
    'ubuntu32_hw': dict([("talos-linux32-ix-%03i" % x, {}) for x in range(1, 56)]),
    'ubuntu64_hw': dict([("talos-linux64-ix-%03i" % x, {}) for x in range(1, 120)]),
    'win64_vm': dict([('tst-w64-ec2-%03i' % x, {}) for x in range(100)]),
}

SLAVES['tegra_android-armv6'] = SLAVES['tegra_android']
SLAVES['tegra_android-noion'] = SLAVES['tegra_android']
SLAVES['fedora-b2g'] = SLAVES['fedora']
SLAVES['fedora-b2g-emulator'] = SLAVES['fedora']
SLAVES['ubuntu64-asan_vm'] = SLAVES['ubuntu64_vm']
# Use "-b2g" suffix to make misc.py generate unique builder names
SLAVES['ubuntu32_vm-b2gdt'] = SLAVES['ubuntu32_vm']
SLAVES['ubuntu64_vm-b2g'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2gdt'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator-jb'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_hw-b2g'] = SLAVES['ubuntu64_hw']
SLAVES['ubuntu64_hw-b2g-emulator'] = SLAVES['ubuntu64_hw']
SLAVES['mountainlion-b2gdt'] = SLAVES['mountainlion']
SLAVES['vm_android_2_3'] = SLAVES['ubuntu64_vm']
SLAVES['win8_64'] = SLAVES['win8']

TRY_SLAVES = {}

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org',
                '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'disable_tinderbox_mail': True,
    'build_tools_repo_path': 'build/tools',
    'mozharness_repo': 'https://hg.mozilla.org/build/mozharness',
    'mozharness_tag': 'production',
    'stage_server': 'stage.mozilla.org',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_dsa',
    'datazilla_url': 'https://datazilla.mozilla.org/talos',
    'blob_upload': True,
}


# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'tinderbox_tree': 'Firefox',
        'mobile_tinderbox_tree': 'Firefox',
    },
    'mozilla-release': {
        'tinderbox_tree': 'Mozilla-Release',
        'mobile_tinderbox_tree': 'Mozilla-Release',
    },
    'mozilla-esr24': {
        'tinderbox_tree': 'Mozilla-Esr24',
        'mobile_tinderbox_tree': 'Mozilla-Esr24',
    },
    'mozilla-b2g18': {
        'tinderbox_tree': 'Mozilla-B2g18',
        'mobile_tinderbox_tree': 'Mozilla-B2g18',
    },
    'mozilla-b2g18_v1_1_0_hd': {
        'tinderbox_tree': 'Mozilla-B2g18-v1.1.0hd',
        'mobile_tinderbox_tree': 'Mozilla-B2g18-v1.1.0hd',
    },
    'mozilla-b2g26_v1_2': {
        'tinderbox_tree': 'Mozilla-B2g26-v1.2',
        'mobile_tinderbox_tree': 'Mozilla-B2g26-v1.2',
    },
    'mozilla-b2g28_v1_3': {
        'tinderbox_tree': 'Mozilla-B2g28-v1.3',
        'mobile_tinderbox_tree': 'Mozilla-B2g28-v1.3',
    },
    'mozilla-b2g28_v1_3t': {
        'tinderbox_tree': 'Mozilla-B2g28-v1.3t',
        'mobile_tinderbox_tree': 'Mozilla-B2g28-v1.3t',
    },
    'mozilla-beta': {
        'tinderbox_tree': 'Mozilla-Beta',
        'mobile_tinderbox_tree': 'Mozilla-Beta',
    },
    'mozilla-aurora': {
        'tinderbox_tree': 'Mozilla-Aurora',
        'mobile_tinderbox_tree': 'Mozilla-Aurora',
    },
    'addontester': {
        'tinderbox_tree': 'AddonTester',
        'mobile_tinderbox_tree': 'AddonTester',
    },
    'addonbaselinetester': {
        'tinderbox_tree': 'AddonTester',
        'mobile_tinderbox_tree': 'AddonTester',
    },
    'try': {
        'tinderbox_tree': 'Try',
        'mobile_tinderbox_tree': 'Try',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'enable_merging': False,
        'slave_key': 'try_slaves',
        'package_url': 'https://ftp-ssl.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'package_dir': '%(who)s-%(got_revision)s',
        'stage_username': 'trybld',
        'stage_ssh_key': 'trybld_dsa',
    },
}

PLATFORM_VARS = {
}

PROJECTS = {
    'jetpack': {
        'scripts_repo': 'https://hg.mozilla.org/build/tools',
        'tinderbox_tree': 'Jetpack',
    },
}
