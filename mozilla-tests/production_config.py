SLAVES = {
    'xp_ix': {},
    'win7_ix': {},
    'win7_ix_devedition': {},
    'win7_vm': {},
    'win7_vm_devedition': {},
    'win7_vm_gfx': {},
    'win7_vm_gfx_devedition': {},
    'win8': {},
    'win8_64_devedition': {},
    'win10': {},
    'win10_64_devedition': {},
    'yosemite_r7': {},
    'yosemite_r7_devedition': {},
    'ubuntu32_vm': {},
    'ubuntu64_vm': {},
    'ubuntu64_vm_large': {},
    'ubuntu64_vm_lnx_large': {},
    'ubuntu64-asan_vm_lnx_large': {},
    'ubuntu64_hw': {},
    'ubuntu64_hw_qr': {},
    'ubuntu64_hw_stylo': {},
    'ubuntu64_hw_devedition': {},
    'win64_vm': {},
}

for i in range(3, 11):  # Bug 1297173 // Bug 1299468 // Bug 1317723 // Bug 1337394 // Bug 1395682 // Bug 1367102
    SLAVES['xp_ix']['t-xp32-ix-%03i' % i] = {}

for i in range(1, 151):   #  Move 111 machines from Windows 7 pool to Windows XP and Windows 8 // Bug 1297173 // Bug 1299468
    SLAVES['win7_ix']['t-w732-ix-%03i' % i] = {}

for i in range(1, 101) + range(102, 600):  # Omit 101 due to win7 golden issues // Bug 1223509
    SLAVES['win7_vm']['t-w732-spot-%03i' % i] = {}

for i in range(1, 201):
    SLAVES['win7_vm_gfx']['g-w732-spot-%03i' % i] = {}

# Bug 1302530 - Add ondemand g-w732 instances
for i in range(1, 101):
    SLAVES['win7_vm_gfx']['g-w732-ec2-%03i' % i] = {}

for i in range(1, 102) + range(103, 207) + range(208, 217):  # Omit 102 for win10 // Bug 1191481 // Bug 1255812 // Bug 1299468 // Bug 1317723 //Bug1397225 //Bug1397879 //Bug1398238 //Bug1398884
    SLAVES['win8']['t-w864-ix-%03i' % i] = {}

for i in range(1, 216):
    SLAVES['win10']['t-w1064-ix-%03i' % i] = {}

for i in range(1, 393):
    SLAVES['yosemite_r7']['t-yosemite-r7-%04i' % i] = {}

for i in range(1, 800) + range(1000, 1100):
    SLAVES['ubuntu32_vm']['tst-linux32-spot-%03i' % i] = {}

for i in range(1, 200) + range(301, 500) + range(601, 800) + range(901, 1100) + range(1201, 1452):  # Bug 1252248
    SLAVES['ubuntu64_vm_large']['tst-emulator64-spot-%03i' % i] = {}

for i in range(1, 2601):  # Bug 1252248
    SLAVES['ubuntu64_vm']['tst-linux64-spot-%03i' % i] = {}

for i in range(1, 90):       #Bug 1337394
    SLAVES['ubuntu64_hw']['talos-linux64-ix-%03i' % i] = {}

for i in range(1, 3):
    SLAVES['win64_vm']['tst-w64-ec2-%03i' % i] = {}

SLAVES['ubuntu64-asan_vm'] = SLAVES['ubuntu64_vm']
SLAVES['win8_64'] = SLAVES['win8']
SLAVES['win10_64'] = SLAVES['win10']
SLAVES['ubuntu64_vm_mobile'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm_armv7_mobile'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm_armv7_large'] = SLAVES['ubuntu64_vm_large']
SLAVES['ubuntu64_vm_lnx_large'] = SLAVES['ubuntu64_vm_large']
SLAVES['ubuntu64-asan_vm_lnx_large'] = SLAVES['ubuntu64_vm_large']
SLAVES['ubuntu64_hw_qr'] = SLAVES['ubuntu64_hw']
SLAVES['ubuntu64_hw_stylo'] = SLAVES['ubuntu64_hw']
SLAVES['ubuntu64_hw_styloseq'] = SLAVES['ubuntu64_hw']
SLAVES['ubuntu64_hw_devedition'] = SLAVES['ubuntu64_hw']
SLAVES['yosemite_r7_devedition'] = SLAVES['yosemite_r7']
SLAVES['win7_ix_devedition'] = SLAVES['win7_ix']
SLAVES['win7_vm_devedition'] = SLAVES['win7_vm']
SLAVES['win7_vm_gfx_devedition'] = SLAVES['win7_vm_gfx']
SLAVES['win8_64_devedition'] = SLAVES['win8']
SLAVES['win10_64_devedition'] = SLAVES['win10']

TRY_SLAVES = {}

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org',
                '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'build_tools_repo_path': 'build/tools',
    'mozharness_repo': 'https://hg.mozilla.org/build/mozharness',
    'mozharness_tag': 'production',
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
    'mozilla-esr52': {
        'tinderbox_tree': 'Mozilla-Esr52',
        'mobile_tinderbox_tree': 'Mozilla-Esr52',
    },
    'mozilla-beta': {
        'tinderbox_tree': 'Mozilla-Beta',
        'mobile_tinderbox_tree': 'Mozilla-Beta',
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
