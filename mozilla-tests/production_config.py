SLAVES = {
    'fedora': dict([("talos-r3-fed-%03i" % x, {}) for x in range(11,103) \
        if x not in [18, 59]]), # bug 731793, bug 779574
    'fedora64' : dict([("talos-r3-fed64-%03i" % x, {}) for x in range (40,72)]),
    'xp': dict([("talos-r3-xp-%03i" % x, {}) for x in range(1,142) \
        if x not in [4, 45, 58, 59]]), # bug 856604, 661377, 780515, 753357
    'xp-ix': dict([("t-xp32-ix-%03i" % x, {}) for x in range(1,101)]),
    'win7': dict([("talos-r3-w7-%03i" % x, {}) for x in range(4,135) \
        if x not in [10, 17]]), # bug 861326 & bug 747734
    'win7-ix': dict([("t-w732-ix-%03i" % x, {}) for x in range(1,101)]),
    'win8': dict([("t-w864-ix-%03i" % x, {}) for x in range(1,101)]),
    'snowleopard': dict([("talos-r4-snow-%03i" % x, {}) for x in range(1,85) \
        if x not in [46, 81, 83]]), # bug 824754, bug 729090
    'lion': dict([("talos-r4-lion-%03i" % x, {}) for x in range(1,91) \
        if x not in [58, 81, 83]]), # bug 730545, bug 729090 (x2)
    'mountainlion': dict([("talos-mtnlion-r5-%03i" % x, {}) for x in range(1,90)]),
    'tegra_android': dict([('tegra-%03i' % x, {'http_port': '30%03i' % x, 'ssl_port': '31%03i' % x}) \
        for x in range(31,371) \
        if x not in range(122,129) + [30,33,34,43,44,49,65,69,77,131,137,143,147,\
            153,156,161,175,176,180,184,185,186,193,197,198,202,203,204,205,222,224,\
            226,241,268,275,289,291,292,301]]), # decommissioned tegras
    'panda_android': dict(
        [('panda-%04i' % x, {'http_port': '30%03i' % x, 'ssl_port': '31%03i' % x}) \
            for x in range(22,33) + range(34,45) + range(46,82) + range(522,874) + range(885,887)]
    ),
    'b2g_panda': dict([("panda-%04i" % x, {}) for x in range(82,522) + range(33,34) + range(45,46)]),
    'ubuntu32_vm': dict([("tst-linux32-ec2-%03i" % x, {}) for x in range(1, 900)]),
    'ubuntu64_vm': dict([("tst-linux64-ec2-%03i" % x, {}) for x in range(1, 900)]),
    'ubuntu32_hw': dict([("talos-linux32-ix-%03i" % x, {}) for x in range(1, 101)]),
    'ubuntu64_hw': dict([("talos-linux64-ix-%03i" % x, {}) for x in range(1, 101)]),
}

SLAVES['tegra_android-armv6'] = SLAVES['tegra_android']
SLAVES['tegra_android-noion'] = SLAVES['tegra_android']
SLAVES['fedora-b2g'] = SLAVES['fedora']
# Use "-b2g" suffix to make misc.py generate unique builder names
SLAVES['ubuntu32_vm-b2gdt'] = SLAVES['ubuntu32_vm']
SLAVES['ubuntu64_vm-b2g'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2gdt'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_hw-b2g'] = SLAVES['ubuntu64_hw']
SLAVES['b2g_panda_gaia_central'] = SLAVES['b2g_panda']

TRY_SLAVES = {}

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org',
                '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'disable_tinderbox_mail': True,
    'build_tools_repo_path': 'build/tools',
    'mozharness_repo': 'http://hg.mozilla.org/build/mozharness',
    'mozharness_tag': 'production',
    'stage_server': 'stage.mozilla.org',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_dsa',
    'datazilla_url': 'https://datazilla.mozilla.org/talos',
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
    'mozilla-esr17': {
        'tinderbox_tree': 'Mozilla-Esr17',
        'mobile_tinderbox_tree': 'Mozilla-Esr17',
    },
    'mozilla-b2g18': {
        'tinderbox_tree': 'Mozilla-B2g18',
        'mobile_tinderbox_tree': 'Mozilla-B2g18',
    },
    'mozilla-b2g18_v1_0_1': {
        'tinderbox_tree': 'Mozilla-B2g18_v1_0_1',
        'mobile_tinderbox_tree': 'Mozilla-B2g18_v1_0_1',
    },
    'mozilla-beta': {
        'tinderbox_tree': 'Mozilla-Beta',
        'mobile_tinderbox_tree': 'Mozilla-Beta',
    },
    'mozilla-aurora': {
        'tinderbox_tree': 'Mozilla-Aurora',
        'mobile_tinderbox_tree': 'Mozilla-Aurora',
    },
    'places': {
        'tinderbox_tree': 'Places',
        'mobile_tinderbox_tree': 'Places',
    },
    'electrolysis': {
        'tinderbox_tree': 'Electrolysis',
        'mobile_tinderbox_tree': 'Electrolysis',
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
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'package_dir': '%(who)s-%(got_revision)s',
        'stage_username': 'trybld',
        'stage_ssh_key': 'trybld_dsa',
    },
    'jaegermonkey': {
        'tinderbox_tree': 'Jaegermonkey',
        'mobile_tinderbox_tree': 'Jaegermonkey',
    },
}

PLATFORM_VARS = {
}

PROJECTS = {
    'jetpack': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'tinderbox_tree': 'Jetpack',
    },
}
