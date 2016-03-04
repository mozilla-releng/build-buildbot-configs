SLAVES = {
    'xp-ix': {},
    'win7-ix': {},
    'win7-all': {},
    'win8': {},
    'win10': {},
    'snowleopard': {},
    'yosemite': {},
    'yosemite_r7': {},
    'panda_android': {},
    'ubuntu32_vm': {},
    'ubuntu64_vm': {},
    'ubuntu64_vm_large': {},
    'ubuntu64_vm_lnx_large': {},
    'ubuntu64-asan_vm_lnx_large': {},
    'ubuntu64_hw': {},
    'win64_vm': {},
}

for i in range(1, 133):  # XP slaves from 153 to 173 moved to Win 7 pool // Bug 1226729 // Bug 1239785
    SLAVES['xp-ix']['t-xp32-ix-%03i' % i] = {}

for i in range(1, 282):   # Move some XP test machines to the Windows 7 pool from 234 to 253 // Bug 1226729 // Bug 1239785 // Bug 1252258
    SLAVES['win7-ix']['t-w732-ix-%03i' % i] = {}
    SLAVES['win7-all']['t-w732-ix-%03i' % i] = {}

for i in range(1, 400):
    SLAVES['win7-all']['t-w732-spot-%03i' % i] = {}

for i in range(1, 102) + range(103, 195):  # Omit 102 for win10 // Bug 1191481
    SLAVES['win8']['t-w864-ix-%03i' % i] = {}

for i in range(1, 3) + range(11, 12):  # Bug 1252258
    SLAVES['win10']['t-w1064-ix-%04i' % i] = {}
for i in range(102, 103):  # Use win8's 102 for win10 // Bug 1191481
    SLAVES['win10']['t-w864-ix-%03i' % i] = {}

for i in range(1, 34) + range(35, 93) + range(95, 147) + range(164, 166):  # slaves 0034&0093&0094&0153 have been decommed
    SLAVES['snowleopard']['t-snow-r4-%04i' % i] = {}

for i in range(1, 3) + range(7, 8):   #slaves decomm bug 1226180
    SLAVES['yosemite']['t-yosemite-r5-%04i' % i] = {}

for i in range(1, 201):
    SLAVES['yosemite_r7']['t-yosemite-r7-%04i' % i] = {}

for i in range(22, 910):
    SLAVES['panda_android']['panda-%04i' % i] = {
        'http_port': '30%03i' % i,
        'ssl_port': '31%03i' % i,
    }

for i in range(1, 800) + range(1000, 1100):
    SLAVES['ubuntu32_vm']['tst-linux32-spot-%03i' % i] = {}

for i in range(1, 200) + range(301, 500) + range(601, 800) + range(901, 1100) + range(1201, 1452):  # Bug 1252248
    SLAVES['ubuntu64_vm_large']['tst-emulator64-spot-%03i' % i] = {}

for i in range(1, 2601):  # Bug 1252248
    SLAVES['ubuntu64_vm']['tst-linux64-spot-%03i' % i] = {}

for i in range(1, 70):
    SLAVES['ubuntu64_hw']['talos-linux64-ix-%03i' % i] = {}

for i in range(1, 3):
    SLAVES['win64_vm']['tst-w64-ec2-%03i' % i] = {}

SLAVES['ubuntu64-asan_vm'] = SLAVES['ubuntu64_vm']
# Use "-b2g" suffix to make misc.py generate unique builder names
SLAVES['ubuntu32_vm-b2gdt'] = SLAVES['ubuntu32_vm']
SLAVES['ubuntu64_vm-b2g'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-lg-emulator'] = SLAVES['ubuntu64_vm_large']
SLAVES['ubuntu64_vm-b2g-emulator-jb'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator-kk'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_hw-b2g'] = SLAVES['ubuntu64_hw']
SLAVES['win8_64'] = SLAVES['win8']
SLAVES['win10_64'] = SLAVES['win10']
SLAVES['ubuntu64_vm_mobile'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm_armv7_mobile'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm_armv7_large'] = SLAVES['ubuntu64_vm_large']
SLAVES['ubuntu64_vm_lnx_large'] = SLAVES['ubuntu64_vm_large']
SLAVES['ubuntu64-asan_vm_lnx_large'] = SLAVES['ubuntu64_vm_large']

TRY_SLAVES = {}

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org',
                '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'build_tools_repo_path': 'build/tools',
    'mozharness_repo': 'https://hg.mozilla.org/build/mozharness',
    'mozharness_tag': 'production',
    'stage_server': 'upload.ffxbld.productdelivery.prod.mozaws.net',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_rsa',
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
    'mozilla-esr38': {
        'tinderbox_tree': 'Mozilla-Esr38',
        'mobile_tinderbox_tree': 'Mozilla-Esr38',
    },
    'mozilla-esr45': {
        'tinderbox_tree': 'Mozilla-Esr45',
        'mobile_tinderbox_tree': 'Mozilla-Esr45',
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
        'package_url': 'https://archive.mozilla.org/pub/firefox/try-builds',
        'package_dir': '%(who)s-%(got_revision)s/',
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
