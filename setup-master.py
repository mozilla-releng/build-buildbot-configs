#!/usr/bin/env python
"""setup-master.py master_dir master_name

Sets up mozilla buildbot master in master_dir."""

import os, glob, shutil, subprocess, urllib, tempfile
try:
    import simplejson as json
except ImportError:
    import json

class MasterConfig:
    def __init__(self, name=None, config_dir=None, globs=None, renames=None, local_links=None, extras=None):
        self.name = name or None
        self.config_dir = config_dir
        self.globs = globs or []
        self.renames = renames or []
        self.local_links = local_links or []
        self.extras = extras or []

    def __add__(self, o):
        retval = MasterConfig(
                name = self.name or o.name,
                config_dir = self.config_dir or o.config_dir,
                globs = self.globs + o.globs,
                renames = self.renames + o.renames,
                local_links = self.local_links + o.local_links,
                extras = self.extras + o.extras,
                )
        return retval

    def createMaster(self, master_dir, buildbot):
        null = open(os.devnull, "w")
        subprocess.check_call([buildbot, 'create-master', master_dir], stdout=null)
        null.close()
        if not os.path.exists(master_dir):
            os.makedirs(master_dir)
        for g in self.globs:
            for f in glob.glob(os.path.join(self.config_dir, g)):
                dst = os.path.join(master_dir, os.path.basename(f))
                if os.path.lexists(dst):
                    os.unlink(dst)
                src = os.path.abspath(f)
                os.symlink(src, dst)

        for src, dst in self.local_links:
            dst = os.path.join(master_dir, dst)
            if os.path.lexists(dst):
                os.unlink(dst)
            os.symlink(src, dst)

        for src, dst in self.renames:
            dst = os.path.join(master_dir, dst)
            if os.path.lexists(dst):
                os.unlink(dst)
            shutil.copy(os.path.join(self.config_dir, src), dst)

        for extra_filename, extra_data in self.extras:
            f = open(os.path.join(master_dir, extra_filename), 'w').write(extra_data)

        # Remove leftover files
        for f in "Makefile.sample", "master.cfg.sample":
            dst = os.path.join(master_dir, f)
            if os.path.exists(dst):
                os.unlink(dst)



    def testMaster(self, buildbot, universal=False):
        print "TEST-INFO starting %s" % self.name
        test_output_dir = os.environ.get('TEMP', 'test-output')
        if not os.path.isdir(test_output_dir):
            os.mkdir(test_output_dir)
        test_dir = tempfile.mkdtemp(prefix='%s-'%self.name, dir=os.path.join(os.getcwd(), test_output_dir))
        test_log_filename = test_dir+'.log'
        test_log = open(test_log_filename, 'w')
        print "TEST-INFO creating master"
        try:
            self.createMaster(test_dir, buildbot)
            print "TEST-INFO created master"
        except (OSError, subprocess.CalledProcessError):
            print "TEST-FAIL %s failed to be created" % self.name
            return (300, None, None)
        null = open(os.devnull, "w")
        rc = subprocess.call([buildbot, 'checkconfig'],
                             cwd=test_dir, stdout=test_log, stderr=subprocess.STDOUT)
        test_log.close()
        log = open(test_log_filename)
        log_size = os.path.getsize(test_log_filename)
        # We expect that the reconfig done message is before the last K of output
        if log_size > 1024:
            log.seek(log_size - 1024)
        log_tail = log.readlines()
        if 'Config file is good!' in [x.strip() for x in log_tail] and rc == 0:
            print "TEST-PASS checkconfig OK for %s" % self.name
            shutil.rmtree(test_dir)
            os.remove(test_log_filename)
            return (0, None, None)
        else:
            if rc == 0:
                print "TEST-FAIL checkconfig returned 0 for %s but didn't print 'Config file is good!'" % \
                        self.name
            else:
                print "TEST-FAIL %s failed to run checkconfig" % self.name
            print "TEST-INFO log is in %s" % test_log_filename
            return (rc, test_log_filename, test_dir)


def load_masters_json(masters_json, role=None, universal=False):
    if 'http' in masters_json:
        masters = json.load(urllib.urlopen(masters_json))
    else:
        masters = json.load(open(masters_json))

    retval = []
    for m in masters:
        # Unsupported...for now!
        if m['role'] in ('scheduler',):
            continue

        # Sometimes we only want masters of a specific role to be loaded
        if role and m['role'] != role:
                continue

        if m['environment'] == 'production':
            environment_config = 'production_config.py'
        elif m['environment'] == 'staging':
            environment_config = 'staging_config.py'
        elif m['environment'] == 'preproduction':
            environment_config = 'preproduction_config.py'
        c = MasterConfig(name=m['name'],
                globs=[
                    'config.py',
                    environment_config,
                    'master_common.py',
                    'project_branches.py',
                    ],
                renames=[
                    ('BuildSlaves.py.template', 'BuildSlaves.py'),
                    ('passwords.py.template', 'passwords.py'),
                    ],
                local_links=[
                    (environment_config, 'localconfig.py'),
                    ],
                extras=[
                    ('master_config.json', json.dumps(m, indent=2, sort_keys=True)),
                    ]
                )

        if universal:
            c.name += '-universal'
            mastercfg = 'universal_master_sqlite.cfg'
        else:
            if m['role'] == 'tests':
                mastercfg = 'tests_master.cfg'
            elif m['role'] == 'build' or m['role'] == 'try':
                mastercfg = 'builder_master.cfg'
            else:
                raise AssertionError("What is a %s role?" % m['role'])

        if m['role'] == 'build':
            c.config_dir = 'mozilla'
            c.globs.append('l10n-changesets*')
            c.globs.append('release_templates')
            c.globs.append('release-firefox*.py')
            c.globs.append('release-fennec*.py')
            c.globs.append(mastercfg)
            c.globs.append('build_localconfig.py')
            c.local_links.append((mastercfg, 'master.cfg'))
            c.local_links.append(('build_localconfig.py', 'master_localconfig.py'))
        elif m['role'] == 'try':
            c.config_dir = 'mozilla'
            c.local_links.append((mastercfg, 'master.cfg'))
            c.local_links.append(('try_localconfig.py', 'master_localconfig.py'))
            c.globs.append(mastercfg)
            c.globs.append('try_localconfig.py')
        elif m['role'] == 'tests':
            c.config_dir = 'mozilla-tests'
            c.local_links.append((mastercfg, 'master.cfg'))
            c.local_links.append(('tests_localconfig.py', 'master_localconfig.py'))
            c.globs.append('tests_localconfig.py')
            c.globs.append(mastercfg)

        retval.append(c)
    return retval

debsign = MasterConfig(
        config_dir='debsign',
        globs=['*.py', '*.cfg'],
        renames=[
            ('passwords.py.template', 'passwords.py'),
        ],
        local_links=[],
        )

debsign_production = debsign + MasterConfig(
        "production-debsign",
        local_links=[
            ('master-production.cfg', 'master.cfg'),
            ('config-production.py', 'config.py'),
            ],
        )

debsign_staging = debsign + MasterConfig(
        "staging-debsign",
        local_links=[
            ('master-staging.cfg', 'master.cfg'),
            ('config-staging.py', 'config.py'),
            ],
        )

mobile = MasterConfig(
        config_dir='mobile',
        globs=['*.py', '*.cfg'],
        local_links=[],
        )

mobile_production = mobile + MasterConfig(
        "production-mobile",
        local_links=[
            ('config-production.py', 'config.py'),
            ],
        )

mobile_staging = mobile + MasterConfig(
        "staging-mobile",
        local_links=[
            ('config-staging.py', 'config.py'),
            ],
        )

mozilla_base = MasterConfig(
        config_dir='mozilla',
        globs=['*config.py', '*localconfig.py', 'master_common.py',
               'project_branches.py', '*.cfg', 'l10n-changesets*',
               'release_templates'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ('passwords.py.template', 'passwords.py'),
            ],
        )

mozilla_production = mozilla_base + MasterConfig(
    globs=['release-firefox-*.py', 'release-fennec-*.py'],
    )

mozilla_staging = mozilla_base + MasterConfig(
    globs=['staging_release-*-*.py'],
    local_links=[('staging_release-firefox-mozilla-%s.py' % v,
                  'release-firefox-mozilla-%s.py' % v)
                 for v in ['1.9.2', 'beta', 'release']] + \
                [('staging_release-fennec-mozilla-%s.py' % v,
                  'release-fennec-mozilla-%s.py' % v)
                 for v in ['beta', 'release']]
    )

mozilla_staging_scheduler_master_sm01 = mozilla_staging + MasterConfig(
        "staging-scheduler_master",
        local_links = [
            ('staging_scheduler_master_sm01_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_builder_master_sm01 = mozilla_staging + MasterConfig(
        "staging-builder_master1",
        local_links = [
            ('staging_builder_master_sm01_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_univeral_master_sm02 = mozilla_staging + MasterConfig(
        "staging-builder_master2",
        local_links = [
            ('staging_builder_master_sm02_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_univeral_master_sm03 = mozilla_staging + MasterConfig(
        "staging-builder_master3",
        local_links = [
            ('staging_builder_master_sm03_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ]
        )

mozilla_production_scheduler_master = mozilla_production + MasterConfig(
        "pm01-scheduler",
        local_links = [
            ('production_scheduler_master_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_pm01 = mozilla_production + MasterConfig(
        "pm01-builder",
        local_links = [
            ('production_builder_master_pm01_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_pm02 = mozilla_production + MasterConfig(
        "pm02-trybuilder",
        local_links = [
            ('production_try_builder_master_pm02_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm01 = mozilla_production + MasterConfig(
        "bm01-trybuilder",
        local_links = [
            ('production_try_builder_master_bm01_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm02 = mozilla_production + MasterConfig(
        "bm02-trybuilder",
        local_links = [
            ('production_try_builder_master_bm02_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm03 = mozilla_production + MasterConfig(
        "bm03-trybuilder",
        local_links = [
            ('production_try_builder_master_bm03_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm04 = mozilla_base + MasterConfig(
        "bm04-try1",
        local_links = [
            ('production_try_builder_master_bm04_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm05 = mozilla_base + MasterConfig(
        "bm05-trybuilder",
        local_links = [
            ('production_try_builder_master_bm05_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm06 = mozilla_base + MasterConfig(
        "bm06-try1",
        local_links = [
            ('production_try_builder_master_bm06_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_pm03 = mozilla_production + MasterConfig(
        "pm03-builder",
        local_links = [
            ('production_builder_master_pm03_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_bm01 = mozilla_production + MasterConfig(
        "bm01-builder",
        local_links = [
            ('production_builder_master_bm01_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_bm02 = mozilla_production + MasterConfig(
        "bm02-builder",
        local_links = [
            ('production_builder_master_bm02_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_bm04 = mozilla_base + MasterConfig(
        "bm04-build1",
        local_links = [
            ('production_builder_master_bm04_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_bm05 = mozilla_base + MasterConfig(
        "bm05-builder",
        local_links = [
            ('production_builder_master_bm05_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_bm06 = mozilla_base + MasterConfig(
        "bm06-build1",
        local_links = [
            ('production_builder_master_bm06_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_tests = MasterConfig(
        config_dir="mozilla-tests",
        globs=['*.py', '*.cfg'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ('passwords.py.template', 'passwords.py'),
            ],
        )

mozilla_staging_tests_scheduler_master = mozilla_tests + MasterConfig(
        "staging-tests_scheduler",
        local_links = [
            ('staging_tests_scheduler_master.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_tests_master1 = mozilla_tests + MasterConfig(
        "staging-tests_master1",
        local_links = [
            ('staging_tests_master_stm01_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_tests_master2 = mozilla_tests + MasterConfig(
        "staging-tests_master2",
        local_links = [
            ('staging_tests_master_stm02_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_ateam_master1 = mozilla_tests + MasterConfig(
        "staging-ateam_master1",
        local_links = [
            ('staging_ateam_master01_localconfig.py', 'master_localconfig.py'),
            ('staging_ateam_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_ateam_master2 = mozilla_tests + MasterConfig(
        "staging-ateam_master2",
        local_links = [
            ('staging_ateam_master02_localconfig.py', 'master_localconfig.py'),
            ('staging_ateam_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_addon_master = mozilla_tests + MasterConfig(
        "staging-addon_master",
        local_links = [
            ('staging_addon_master_localconfig.py', 'master_localconfig.py'),
            ('staging_addon_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ]
        )

mozilla_production_addon_master = mozilla_tests + MasterConfig(
        "production-addon_master",
        local_links = [
            ('production_addon_master_localconfig.py', 'master_localconfig.py'),
            ('production_addon_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ]
        )

mozilla_preproduction_tests_scheduler_master = mozilla_tests + MasterConfig(
        "preproduction-tests_scheduler",
        local_links = [
            ('preproduction_tests_scheduler_master_localconfig.py', 'master_localconfig.py'),
            ('preproduction_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_preproduction_tests_master = mozilla_tests + MasterConfig(
        "preproduction-tests_master",
        local_links = [
            ('preproduction_tests_master_localconfig.py', 'master_localconfig.py'),
            ('preproduction_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_scheduler_master = mozilla_tests + MasterConfig(
        "pm02-tests_scheduler",
        local_links = [
            ('production_tests_scheduler_master_pm02_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_master_tm01 = mozilla_tests + MasterConfig(
        "tm01-tests_master",
        local_links = [
            ('production_tests_master_tm01_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_master_bm01_2 = mozilla_tests + MasterConfig(
        "bm01_2-tests_master",
        local_links = [
            ('production_tests_master_bm01_2_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_master_bm02_1 = mozilla_tests + MasterConfig(
        "bm02_1-tests_master",
        local_links = [
            ('production_tests_master_bm02_1_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_master_bm02_2 = mozilla_tests + MasterConfig(
        "bm02_2-tests_master",
        local_links = [
            ('production_tests_master_bm02_2_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_master_bm04 = mozilla_tests + MasterConfig(
        "bm04-tests1",
        local_links = [
            ('production_tests_master_bm04_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_master_bm05 = mozilla_tests + MasterConfig(
        "bm05-tests_master",
        local_links = [
            ('production_tests_master_bm05_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_master_bm06 = mozilla_tests + MasterConfig(
        "bm06-tests1",
        local_links = [
            ('production_tests_master_bm06_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_preproduction_scheduler_master = mozilla_production + MasterConfig(
        "preprod-scheduler_master",
        local_links = [
            ('preproduction_scheduler_master_localconfig.py', 'master_localconfig.py'),
            ('preproduction_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ]
        )

mozilla_preproduction_builder_master = mozilla_production + MasterConfig(
        "preprod-builder",
        local_links = [
            ('preproduction_builder_master_localconfig.py', 'master_localconfig.py'),
            ('preproduction_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_preproduction_release_master = mozilla_production + MasterConfig(
        "preprod-release-master",
        local_links = [
            ('preproduction_release_master_localconfig.py', 'master_localconfig.py'),
            ('preproduction_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

# Buildbot 0.7 masters
masters_07 = [
        debsign_production, debsign_staging,
        mobile_production, mobile_staging,
        ]

# Buildbot 0.8 masters
masters_08 = [
        # Build Masters
        mozilla_staging_scheduler_master_sm01,
        mozilla_staging_builder_master_sm01,
        mozilla_staging_univeral_master_sm02,
        mozilla_staging_univeral_master_sm03,
        mozilla_production_scheduler_master,
        mozilla_production_builder_master_pm01,
        mozilla_production_builder_master_pm03,
        mozilla_production_try_builder_master_pm02,
        mozilla_production_try_builder_master_bm01,
        mozilla_production_try_builder_master_bm02,
        mozilla_production_try_builder_master_bm03,
        mozilla_production_try_builder_master_bm04,
        mozilla_production_try_builder_master_bm05,
        mozilla_production_try_builder_master_bm06,
        mozilla_production_builder_master_bm01,
        mozilla_production_builder_master_bm02,
        mozilla_production_builder_master_bm04,
        mozilla_production_builder_master_bm05,
        mozilla_production_builder_master_bm06,

        # Test masters
        mozilla_staging_tests_scheduler_master,
        mozilla_staging_tests_master1,
        mozilla_staging_tests_master2,
        mozilla_staging_ateam_master1,
        mozilla_staging_ateam_master2,
        mozilla_staging_addon_master,
        mozilla_production_addon_master,
        mozilla_preproduction_tests_scheduler_master,
        mozilla_preproduction_tests_master,
        mozilla_production_tests_scheduler_master,
        mozilla_production_tests_master_tm01,
        mozilla_production_tests_master_bm01_2,
        mozilla_production_tests_master_bm02_1,
        mozilla_production_tests_master_bm02_2,
        mozilla_production_tests_master_bm04,
        mozilla_production_tests_master_bm05,
        mozilla_production_tests_master_bm06,

        # Preproduction masters
        mozilla_preproduction_scheduler_master,
        mozilla_preproduction_builder_master,
        mozilla_preproduction_release_master,
    ]

def filter_masters(master_list):
    rv = []
    for master in master_list:
        if master.name != 'preprod-release-master':
            rv.append(master)
    return master_list

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser(__doc__)
    parser.set_defaults(action=None, masters_json=None)
    parser.add_option("-l", "--list", action="store_true", dest="list")
    parser.add_option("-t", "--test", action="store_true", dest="test")
    parser.add_option("-7", action="store_true", dest="buildbot07", default=False)
    parser.add_option("-8", action="store_true", dest="buildbot08", default=False)
    parser.add_option("-b", "--buildbot", dest="buildbot", default="buildbot")
    parser.add_option("-j", "--masters-json", dest="masters_json", \
        default="http://hg.mozilla.org/build/tools/raw-file/tip/buildfarm/maintenance/production-masters.json")
    parser.add_option("-R", "--role", dest="role", default=None)
    parser.add_option("-u", "--universal", dest="universal", action="store_true")

    options, args = parser.parse_args()

    if options.buildbot08:
        master_list = masters_08
    elif options.buildbot07:
        master_list = masters_07
    else:
        master_list = load_masters_json(options.masters_json, role=options.role)
        if options.test:
            master_list.extend(load_masters_json(options.masters_json, role=options.role, universal=True))

    # Make sure we don't have duplicate names
    master_map = dict((m.name, m) for m in master_list)
    assert len(master_map.values()) == len(master_list), "Duplicate master names"
    assert len(master_list) > 0, "No masters specified. Bad role?"

    if options.list:
        for m in filter_masters(master_list):
            print m.name
    elif options.test:
        failing_masters = []
        # Test the masters, once normally and onces as a universal master
        for m in filter_masters(master_list):
            rc, log, dir = m.testMaster(options.buildbot)
            if rc != 0:
                failing_masters.append((m.name, log, dir))
        # Print a summary including a list of useful output
        print "TEST-SUMMARY: %s tested, %s failed" % (len(master_list), len(failing_masters))
        for rc, log, dir in failing_masters:
            def s(n):
                if n is not None:
                    return n[len(os.getcwd())+1:]
            print " -%s, log: '%s', dir: '%s'" % (rc, s(log), s(dir))
        if len(failing_masters) > 0:
            exit(1)
    elif len(args) == 2:
        master_dir, master_name = args[:2]

        if master_name not in master_map:
            parser.error("Unknown master %s" % master_name)

        m = master_map[master_name]
        m.createMaster(master_dir, options.buildbot)
    else:
        parser.print_usage()
        parser.exit()
