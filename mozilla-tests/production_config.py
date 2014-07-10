SLAVES = {
    'xp-ix': {},
    'win7-ix': {},
    'win8': {},
    'snowleopard': {},
    'mountainlion': {},
    'mavericks': {},
    'tegra_android': {},
    'panda_android': {},
    'ubuntu32_vm': {},
    'ubuntu64_vm': {},
    'ubuntu32_hw': {},
    'ubuntu64_hw': {},
    'win64_vm': {},
}

for i in range(1,131):
    SLAVES['xp-ix']['t-xp32-ix-%03i' % i] = {}

for i in range(1,131):
    SLAVES['win7-ix']['t-w732-ix-%03i' % i] = {}

for i in range(1,131):
    SLAVES['win8']['t-w864-ix-%03i' % i] = {}

for i in range(1,167):
    SLAVES['snowleopard']['t-snow-r4-%04i' % i] = {}

for i in range(1,87) + range(88,101):
    SLAVES['mountainlion']['talos-mtnlion-r5-%03i' % i] = {}

for i in range(1,4):
    SLAVES['mavericks']['t-mavericks-r5-%03i' % i] = {}

for i in range(31,33) + range(35,43) + range(45,49) + range(50,53) + \
         range(54,56) + range(57,64) + range(66,69) + range(70,75) + [77] + \
         range(79,86) + range(87,90) + range(91,106) + range(107,112) + \
         range(113,116) + range(117,124) + range(129,131) + range(132,137) + \
         range(138,143) + range(144,147) + range(148,153) + range(154,156) + \
         range(157,162) + range(163,172) + [173,174] + range(177,180) + \
         range(181,184) + range(187,193) + range(194,197) + range(198,221) + \
         [223,225] + range(227,230) + range(231,241) + range(242,289) + \
         range(293,295) + [297,299,301] + [304,309] + range(311,314) + \
         range(315,319) + range(320,322) + [329,331] + range(334,336) + \
         range(338,340) + range(343,346) + [348] + range(351,356) + [357] + \
         range(361,365) + [367,369]:
    SLAVES['tegra_android']['tegra-%03i' % i] = {
        'http_port': '30%03i' % i,
        'ssl_port': '31%03i' % i,
    }

for i in range(22,307) + range(320,874) + range(885,910):
    SLAVES['panda_android']['panda-%04i' % i] = {
        'http_port': '30%03i' % i,
        'ssl_port': '31%03i' % i,
    }

for i in range(1,100) + range(300,360):
    SLAVES['ubuntu32_vm']['tst-linux32-ec2-%03i' % i] = {}

for i in range(1,800):
    SLAVES['ubuntu32_vm']['tst-linux32-spot-%03i' % i] = {}

for i in range(1000, 1100):
    SLAVES['ubuntu32_vm']['tst-linux32-spot-%i' % i] = {}

for i in range(1,100) + range(301,400):
    SLAVES['ubuntu64_vm']['tst-linux64-ec2-%03i' % i] = {}

for i in range(1,1000):
    SLAVES['ubuntu64_vm']['tst-linux64-spot-%03i' % i] = {}

for i in range(1000, 1300):
    SLAVES['ubuntu64_vm']['tst-linux64-spot-%i' % i] = {}

for i in range(1,56):
    SLAVES['ubuntu32_hw']['talos-linux32-ix-%03i' % i] = {}

for i in range(1,120):
    SLAVES['ubuntu64_hw']['talos-linux64-ix-%03i' % i] = {}

for i in range(1,3):
    SLAVES['win64_vm']['tst-w64-ec2-%03i' % i] = {}

SLAVES['tegra_android-armv6'] = SLAVES['tegra_android']
SLAVES['ubuntu64-asan_vm'] = SLAVES['ubuntu64_vm']
# Use "-b2g" suffix to make misc.py generate unique builder names
SLAVES['ubuntu32_vm-b2gdt'] = SLAVES['ubuntu32_vm']
SLAVES['ubuntu64_vm-b2g'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2gdt'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator-jb'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator-kk'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_hw-b2g'] = SLAVES['ubuntu64_hw']
SLAVES['ubuntu64_hw-b2g-emulator'] = SLAVES['ubuntu64_hw']
SLAVES['mountainlion-b2gdt'] = SLAVES['mountainlion']
SLAVES['win8_64'] = SLAVES['win8']
SLAVES['ubuntu64_hw_mobile'] = SLAVES['ubuntu64_hw']
SLAVES['ubuntu64_vm_mobile'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_hw_armv6_mobile'] = SLAVES['ubuntu64_hw']
SLAVES['ubuntu64_vm_armv6_mobile'] = SLAVES['ubuntu64_vm']

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
    'mozilla-esr31': {
        'tinderbox_tree': 'Mozilla-Esr31',
        'mobile_tinderbox_tree': 'Mozilla-Esr31',
    },
    'mozilla-b2g28_v1_3': {
        'tinderbox_tree': 'Mozilla-B2g28-v1.3',
        'mobile_tinderbox_tree': 'Mozilla-B2g28-v1.3',
    },
    'mozilla-b2g28_v1_3t': {
        'tinderbox_tree': 'Mozilla-B2g28-v1.3t',
        'mobile_tinderbox_tree': 'Mozilla-B2g28-v1.3t',
    },
    'mozilla-b2g30_v1_4': {
        'tinderbox_tree': 'Mozilla-B2g30-v1.4',
        'mobile_tinderbox_tree': 'Mozilla-B2g30-v1.4',
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
B2G_PROJECTS = {}
