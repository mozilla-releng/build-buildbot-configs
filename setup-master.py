#!/usr/bin/env python
"""setup-master.py master_dir master_name

Sets up mozilla buildbot master in master_dir."""

import os, glob, shutil, subprocess

class MasterConfig:
    def __init__(self, name=None, config_dir=None, globs=None, renames=None, local_links=None):
        self.name = name or None
        self.config_dir = config_dir
        self.globs = globs or []
        self.renames = renames or []
        self.local_links = local_links or []

    def __add__(self, o):
        retval = MasterConfig(
                name = self.name or o.name,
                config_dir = self.config_dir or o.config_dir,
                globs = self.globs + o.globs,
                renames = self.renames + o.renames,
                local_links = self.local_links + o.local_links,
                )
        return retval

    def createMaster(self, master_dir):
        null = open(os.devnull, "w")
        subprocess.check_call(['buildbot', 'create-master', master_dir], stdout=null)
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

mozilla2_staging = MasterConfig(
        config_dir='mozilla2-staging',
        globs=['*.py', '*.cfg', '*.ini', 'l10n-changesets*'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        local_links=[],
        )

mozilla2_staging1 = mozilla2_staging + MasterConfig(
        "staging-moz2_master",
        local_links=[
            ('master1.cfg', 'master.cfg'),
            ('release_config1.py', 'release_config.py'),
            ('release_mobile_config1.py', 'release_mobile_config.py'),
            ],
        )

mozilla2_staging2 = mozilla2_staging + MasterConfig(
        "staging-moz2_master2",
        local_links=[
            ('master2.cfg', 'master.cfg'),
            ('release_config2.py', 'release_config.py'),
            ('release_mobile_config2.py', 'release_mobile_config.py'),
            ],
        )

mozilla2 = MasterConfig(
        config_dir='mozilla2',
        globs=['*.py', '*.cfg', '*.ini', 'l10n-changesets*'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        local_links=[],
        )

mozilla2_1 = mozilla2 + MasterConfig(
        "pm-moz2_master",
        local_links=[
            ('master1.cfg', 'master.cfg'),
            ('release_config1.py', 'release_config.py'),
            ('release_mobile_config1.py', 'release_mobile_config.py'),
            ],
        )

mozilla2_2 = mozilla2 + MasterConfig(
        "pm02-moz2_master",
        local_links=[
            ('master2.cfg', 'master.cfg'),
            ('release_config2.py', 'release_config.py'),
            ('release_mobile_config2.py', 'release_mobile_config.py'),
            ],
        )

mozilla2_3 = mozilla2 + MasterConfig(
        "pm-2-moz2_master",
        local_links=[
            ('master3.cfg', 'master.cfg'),
            ('release_config3.py', 'release_config.py'),
            ('release_mobile_config3.py', 'release_mobile_config.py'),
            ],
        )

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

mozilla = MasterConfig(
        config_dir='mozilla',
        globs=['*.py', '*.cfg', 'l10n-changesets*', 'release_templates'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ('passwords.py.template', 'passwords.py'),
            ],
        )

mozilla_staging_scheduler_master_sm01 = mozilla + MasterConfig(
        "staging-scheduler_master",
        local_links = [
            ('staging_scheduler_master_sm01_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ('release_config', 'release_config_sm01.py'),
            ]
        )

mozilla_staging_builder_master_sm01 = mozilla + MasterConfig(
        "staging-builder_master1",
        local_links = [
            ('staging_builder_master_sm01_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ('release_config_sm01.py', 'release_config.py'),
            ]
        )

mozilla_staging_univeral_master_sm02 = mozilla + MasterConfig(
        "staging-builder_master2",
        local_links = [
            ('staging_builder_master_sm02_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ('release_config_sm02.py', 'release_config.py'),
            ]
        )

mozilla_staging_univeral_master_sm03 = mozilla + MasterConfig(
        "staging-builder_master3",
        local_links = [
            ('staging_builder_master_sm03_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ('release_config_sm03.py', 'release_config.py'),
            ]
        )

mozilla_production_scheduler_master = mozilla + MasterConfig(
        "pm01-scheduler",
        local_links = [
            ('production_scheduler_master_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_pm01 = mozilla + MasterConfig(
        "pm01-builder",
        local_links = [
            ('production_builder_master_pm01_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_pm02 = mozilla + MasterConfig(
        "pm02-trybuilder",
        local_links = [
            ('production_try_builder_master_pm02_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm01 = mozilla + MasterConfig(
        "bm01-trybuilder",
        local_links = [
            ('production_try_builder_master_bm01_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm02 = mozilla + MasterConfig(
        "bm02-trybuilder",
        local_links = [
            ('production_try_builder_master_bm02_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_bm03 = mozilla + MasterConfig(
        "bm03-trybuilder",
        local_links = [
            ('production_try_builder_master_bm03_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_pm03 = mozilla + MasterConfig(
        "pm03-builder",
        local_links = [
            ('production_builder_master_pm03_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_bm01 = mozilla + MasterConfig(
        "bm01-builder",
        local_links = [
            ('production_builder_master_bm01_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_bm02 = mozilla + MasterConfig(
        "bm02-builder",
        local_links = [
            ('production_builder_master_bm02_localconfig.py', 'master_localconfig.py'),
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
            ('tests_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_tests_master_talos_master02 = mozilla_tests + MasterConfig(
        "talos-master02-tests_master",
        local_links = [
            ('production_tests_master_talos-master02_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('tests_master.cfg', 'master.cfg'),
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

mozilla_production_tests_master_bm01_1 = mozilla_tests + MasterConfig(
        "bm01_1-tests_master",
        local_links = [
            ('production_tests_master_bm01_1_localconfig.py', 'master_localconfig.py'),
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

mozilla_preproduction_scheduler_master = mozilla + MasterConfig(
        "preprod-scheduler_master",
        local_links = [
            ('preproduction_scheduler_master_localconfig.py', 'master_localconfig.py'),
            ('preproduction_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ]
        )

mozilla_preproduction_builder_master = mozilla + MasterConfig(
        "preprod-builder",
        local_links = [
            ('preproduction_builder_master_localconfig.py', 'master_localconfig.py'),
            ('preproduction_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

masters = [
        mozilla2_staging1, mozilla2_staging2,
        mozilla2_1, mozilla2_2, mozilla2_3,
        debsign_production, debsign_staging,
        mobile_production, mobile_staging,
        ]

# Buildbot 0.8.0 masters
masters_080 = [
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
        mozilla_production_builder_master_bm01,
        mozilla_production_builder_master_bm02,

        # Test masters
        mozilla_staging_tests_scheduler_master,
        mozilla_staging_tests_master1,
        mozilla_staging_tests_master2,
        mozilla_preproduction_tests_scheduler_master,
        mozilla_preproduction_tests_master,
        mozilla_production_tests_scheduler_master,
        mozilla_production_tests_master_talos_master02,
        mozilla_production_tests_master_tm01,
        mozilla_production_tests_master_bm01_1,
        mozilla_production_tests_master_bm01_2,
        mozilla_production_tests_master_bm02_1,
        mozilla_production_tests_master_bm02_2,

        # Preproduction masters
        mozilla_preproduction_scheduler_master,
        mozilla_preproduction_builder_master,
    ]

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser(__doc__)
    parser.set_defaults(action=None)
    parser.add_option("-l", "--list", action="store_const", dest="action", const="list")
    parser.add_option("-8", action="store_true", dest="buildbot080", default=False)

    options, args = parser.parse_args()

    if options.buildbot080:
        master_list = masters_080
    else:
        master_list = masters

    # Make sure we don't have duplicate names
    master_map = dict((m.name, m) for m in master_list)
    assert len(master_map.values()) == len(master_list), "Duplicate master names"

    if options.action == "list":
        for m in master_list:
            print m.name
        parser.exit()

    if len(args) < 1:
        parser.error("You need at least 2 arguments")

    master_dir, master_name = args[:2]

    if master_name not in master_map:
        parser.error("Unknown master %s" % master_name)

    m = master_map[master_name]
    m.createMaster(master_dir)
