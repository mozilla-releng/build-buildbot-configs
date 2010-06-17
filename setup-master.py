#!/usr/bin/env python
"""setup-master.py master_dir master [master_num]

Sets up mozilla buildbot master in master_dir.  Some masters require an
additional number since they have been split up, e.g. mozilla2"""

import os, glob, shutil, subprocess

class MasterConfig:
    def __init__(self, name=None, globs=None, renames=None, local_links=None):
        self.name = name or None
        self.globs = globs or []
        self.renames = renames or []
        self.local_links = local_links or []

    def __add__(self, o):
        retval = MasterConfig(
                name = self.name or o.name,
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
            for f in glob.glob(os.path.join(self.name, g)):
                dst = os.path.join(master_dir, os.path.basename(f))
                if os.path.lexists(dst):
                    os.unlink(dst)
                src = os.path.join("..", f)
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
            shutil.copy(os.path.join(self.name, src), dst)

mozilla2_staging = MasterConfig(
        'mozilla2-staging',
        globs=['*.py', '*.cfg', '*.ini', 'l10n-changesets*'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        local_links=[],
        )

mozilla2_staging1 = mozilla2_staging + MasterConfig(
        local_links=[
            ('master1.cfg', 'master.cfg'),
            ('release_config1.py', 'release_config.py'),
            ('release_mobile_config1.py', 'release_mobile_config.py'),
            ],
        )

mozilla2_staging2 = mozilla2_staging + MasterConfig(
        local_links=[
            ('master2.cfg', 'master.cfg'),
            ('release_config2.py', 'release_config.py'),
            ('release_mobile_config2.py', 'release_mobile_config.py'),
            ],
        )

try_staging = mozilla2_staging + MasterConfig(
        local_links=[
            ('master3.cfg', 'master.cfg'),
            ('release_config1.py', 'release_config.py'),
            ('release_mobile_config1.py', 'release_mobile_config.py'),
            ],
        )

mozilla2 = MasterConfig(
        'mozilla2',
        globs=['*.py', '*.cfg', '*.ini', 'l10n-changesets*'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        local_links=[],
        )

mozilla2_1 = mozilla2 + MasterConfig(
        local_links=[
            ('master1.cfg', 'master.cfg'),
            ('release_config1.py', 'release_config.py'),
            ('release_mobile_config1.py', 'release_mobile_config.py'),
            ],
        )

mozilla2_2 = mozilla2 + MasterConfig(
        local_links=[
            ('master2.cfg', 'master.cfg'),
            ('release_config2.py', 'release_config.py'),
            ('release_mobile_config2.py', 'release_mobile_config.py'),
            ],
        )

try_master = mozilla2 + MasterConfig(
        local_links=[
            ('master3.cfg', 'master.cfg'),
            ('release_config1.py', 'release_config.py'),
            ('release_mobile_config1.py', 'release_mobile_config.py'),
            ],
        )

debsign = MasterConfig(
        'debsign',
        globs=['*.py', '*.cfg'],
        renames=[
            ('passwords.py.template', 'passwords.py'),
        ],
        local_links=[],
        )

debsign_production = debsign + MasterConfig(
        local_links=[
            ('master-production.cfg', 'master.cfg'),
            ('config-production.py', 'config.py'),
            ],
        )

debsign_staging = debsign + MasterConfig(
        local_links=[
            ('master-staging.cfg', 'master.cfg'),
            ('config-staging.py', 'config.py'),
            ],
        )

mobile_rw = MasterConfig(
        'mobile-rw',
        globs=['*.py', '*.cfg'],
        local_links=[],
        )

mobile_rw_production = mobile_rw + MasterConfig(
        local_links=[
            ('config-production.py', 'config.py'),
            ],
        )

mobile_rw_staging = mobile_rw + MasterConfig(
        local_links=[
            ('config-staging.py', 'config.py'),
            ],
        )

talos_staging = MasterConfig(
        'talos-staging-pool',
        globs=['*.py', '*.cfg'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        )

talos_staging_try = MasterConfig(
        'talos-staging-try',
        globs=['*.py', '*.cfg'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        )

talos = MasterConfig(
        'talos-pool',
        globs=['*.py', '*.cfg'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        )

talos_r3 = MasterConfig(
        'talos-r3',
        globs=['*.py', '*.cfg'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        )

talos_try = MasterConfig(
        'talos-try',
        globs=['*.py', '*.cfg'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        )

mozilla = MasterConfig(
        'mozilla',
        globs=['*.py', '*.cfg'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ('passwords.py.template', 'passwords.py'),
            ],
        )

mozilla_staging_scheduler_master_sm01 = mozilla + MasterConfig(
        local_links = [
            ('staging_scheduler_master_sm01_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_builder_master_sm01 = mozilla + MasterConfig(
        local_links = [
            ('staging_builder_master_sm01_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_staging_univeral_master_sm02 = mozilla + MasterConfig(
        local_links = [
            ('staging_builder_master_sm02_localconfig.py', 'master_localconfig.py'),
            ('staging_config.py', 'localconfig.py'),
            ('universal_master_sqlite.cfg', 'master.cfg'),
            ]
        )

mozilla_production_scheduler_master = mozilla + MasterConfig(
        local_links = [
            ('production_scheduler_master_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('scheduler_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_pm01 = mozilla + MasterConfig(
        local_links = [
            ('production_builder_master_pm01_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_try_builder_master_pm02 = mozilla + MasterConfig(
        local_links = [
            ('production_try_builder_master_pm02_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )

mozilla_production_builder_master_pm03 = mozilla + MasterConfig(
        local_links = [
            ('production_builder_master_pm03_localconfig.py', 'master_localconfig.py'),
            ('production_config.py', 'localconfig.py'),
            ('builder_master.cfg', 'master.cfg'),
            ]
        )


masters = {
        'mozilla': [
            mozilla_staging_scheduler_master_sm01,
            mozilla_staging_builder_master_sm01,
            mozilla_staging_univeral_master_sm02,
            mozilla_production_scheduler_master,
            mozilla_production_builder_master_pm01,
            mozilla_production_builder_master_pm03,
            mozilla_production_try_builder_master_pm02,
         ],
        # These don't work with 0.8.0 yet:
        # 'mozilla2-staging': [mozilla2_staging1, mozilla2_staging2, try_staging],
        # 'mozilla2': [mozilla2_1, mozilla2_2, try_master],
        # 'talos-staging': [talos_staging],
        # 'talos-staging-try': [talos_staging_try],
        # 'talos': [talos],
        # 'talos-try': [talos_try],
        # 'talos-r3': [talos_r3],
        # 'debsign': [debsign_production, debsign_staging],
        # 'mobile_rw': [mobile_rw_production, mobile_rw_staging],
        }

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser(__doc__)
    parser.set_defaults(action=None)
    parser.add_option("-l", "--list", action="store_const", dest="action", const="list")

    options, args = parser.parse_args()

    if options.action == "list":
        for master_name, master_list in sorted(masters.items()):
            n = len(master_list)
            if n == 1:
                print master_name
            else:
                for i in range(1,n+1):
                    print master_name, i
        parser.exit()

    if len(args) < 2:
        parser.error("You need at least 2 arguments")

    master_dir, master_name = args[:2]

    if master_name not in masters:
        parser.error("Unknown master %s" % master_name)

    n = len(masters[master_name])
    if n == 1:
        if len(args) > 2:
            parser.error("Master %s doesn't require a number" % master_name)
        m = masters[master_name][0]
    else:
        if len(args) == 2:
            parser.error("Master %s requires a number" % master_name)
        try:
            master_num = int(args[2])
        except ValueError:
            parser.error("master_num must be an integer")

        if not 1 <= master_num <= n:
            parser.error("master_num must be between 1 and %s" % n)
        # master_num-1 because we accept 1-based numbers, and the array is 0-based
        m = masters[master_name][master_num-1]

    m.createMaster(master_dir)
