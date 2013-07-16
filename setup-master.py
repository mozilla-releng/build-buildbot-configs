#!/usr/bin/env python
"""setup-master.py master_dir master_name

Sets up mozilla buildbot master in master_dir."""

import os
import glob
import shutil
import subprocess
import urllib
import tempfile
import sys
import logging
try:
    import simplejson as json
    assert json
except ImportError:
    import json


class MasterConfig:
    def __init__(self, name=None, config_dir=None, globs=None, renames=None, local_links=None, extras=None, log=None):
        self.name = name or None
        self.config_dir = config_dir
        self.globs = globs or []
        self.renames = renames or []
        self.local_links = local_links or []
        self.extras = extras or []
        self.log = log or None

    def __add__(self, o):
        retval = MasterConfig(
            name=self.name or o.name,
            config_dir=self.config_dir or o.config_dir,
            globs=self.globs + o.globs,
            renames=self.renames + o.renames,
            local_links=self.local_links + o.local_links,
            extras=self.extras + o.extras,
        )
        return retval

    def createMaster(self, master_dir, buildbot, logfile=None):
        # The following is needed to maintain exisitng behaviour
        # of printing stderr of buildbot
        if logfile:
            self.log.debug('opening "%s" for buildbot create master stdout and stderr' % logfile)
            s_out = open(logfile, 'w+')
            s_err = subprocess.STDOUT
        else:
            s_out = open(os.devnull, 'w+')
            s_err = sys.stderr
        subprocess.check_call([buildbot, 'create-master', master_dir],
                              stdout=s_out, stderr=s_err)
        s_out.close()
        if not os.path.exists(master_dir):
            self.log.debug('mkdir -p %s' % master_dir)
            os.makedirs(master_dir)
        for g in self.globs:
            for f in glob.glob(os.path.join(self.config_dir, g)):
                dst = os.path.join(master_dir, os.path.basename(f))
                if os.path.lexists(dst):
                    self.log.debug('rm -f %s' % dst)
                    os.unlink(dst)
                src = os.path.abspath(f)
                self.log.debug('ln -s %s %s' % (src, dst))
                os.symlink(src, dst)

        for src, dst in self.local_links:
            dst = os.path.join(master_dir, dst)
            if os.path.lexists(dst):
                self.log.debug('rm -f %s' % dst)
                os.unlink(dst)
            self.log.debug('ln -s %s %s' % (src, dst))
            os.symlink(src, dst)

        for src, dst in self.renames:
            dst = os.path.join(master_dir, dst)
            if os.path.lexists(dst):
                self.log.debug('rm -f %s' % dst)
                os.unlink(dst)
            self.log.debug(
                'cp %s %s' % (os.path.join(self.config_dir, src), dst))
            shutil.copy(os.path.join(self.config_dir, src), dst)

        for extra_filename, extra_data in self.extras:
            self.log.debug('writing %s to %s' % (
                extra_data.replace('\n', '\\n'), extra_filename))
            f = open(os.path.join(
                master_dir, extra_filename), 'w').write(extra_data)

        # Remove leftover files
        for f in "Makefile.sample", "master.cfg.sample":
            dst = os.path.join(master_dir, f)
            if os.path.exists(dst):
                os.unlink(dst)

    def logFile(self, filename):
        self.log.info("starting to print log file '%s'" % filename)
        f = open(filename)
        data = f.readline()
        while data != '':
            self.log.info(data.rstrip('\n'))
            data = f.readline()
        f.close()
        self.log.info("finished printing log file '%s'" % filename)

    def testMaster(self, buildbot, universal=False, error_logs=False):
        test_output_dir = os.environ.get('TEMP', 'test-output')
        if not os.path.isdir(test_output_dir):
            os.mkdir(test_output_dir)
        test_dir = tempfile.mkdtemp(prefix='%s-' % self.name, dir=os.path.join(
            os.getcwd(), test_output_dir))
        test_log_filename = test_dir + '-checkconfig.log'
        create_log_filename = test_dir + '-create-master.log'
        test_log = open(test_log_filename, 'w')
        self.log.info('creating "%s" master' % self.name)
        try:
            self.createMaster(test_dir, buildbot, logfile=create_log_filename)
            self.log.info(
                'created  "%s" master, running checkconfig' % self.name)
        except (OSError, subprocess.CalledProcessError):
            self.log.error('TEST-FAIL failed to create "%s"' % self.name)
            if error_logs:
                self.logFile(create_log_filename)
            return (300, create_log_filename, None)
        rc = subprocess.call([buildbot, 'checkconfig'],
                             cwd=test_dir, stdout=test_log, stderr=subprocess.STDOUT)
        test_log.close()
        log = open(test_log_filename)
        log_size = os.path.getsize(test_log_filename)
        # We expect that the reconfig done message is before the last K of
        # output
        if log_size > 1024:
            log.seek(log_size - 1024)
        log_tail = log.readlines()
        if 'Config file is good!' in [x.strip() for x in log_tail] and rc == 0:
            self.log.info("TEST-PASS checkconfig OK for %s" % self.name)
            shutil.rmtree(test_dir)
            os.remove(test_log_filename)
            return (0, None, None)
        else:
            if error_logs:
                self.logFile(test_log_filename)
            if rc == 0:
                self.log.warn('checkconfig returned 0 for %s but didn\'t print "Config file is good!"' %
                              self.name)
            else:
                self.log.error(
                    "TEST-FAIL %s failed to run checkconfig" % self.name)
                self.log.info(
                    'log for "%s" is "%s"' % (self.name, test_log_filename))
            return (rc, test_log_filename, test_dir)


def load_masters_json(masters_json, role=None, universal=False, log=None,
                      dedupe=True, ignored_roles=[]):
    if 'http' in masters_json:
        masters = json.load(urllib.urlopen(masters_json))
    else:
        masters = json.load(open(masters_json))

    if dedupe:
        # Remove masters that are pretty much identical
        # Mapping of unique master representatoin to the first master of that
        # type
        unique_masters = {}
        # List of master instances
        new_masters = []
        for m in masters:
            m0 = m.copy()
            # Remove unimportant stuff
            for k in ("basedir", "bbcustom_dir", "buildbot_bin", "buildbot_python", "buildbot_setup", "datacentre", "db_name", "hostname", "http_port", "master_dir", "name", "pb_port", "ssh_port", "tools_dir"):
                if k in m0:
                    del m0[k]
            k = json.dumps(m0, sort_keys=True)
            if k not in unique_masters:
                unique_masters[k] = m
                new_masters.append(m)
            else:
                log.debug("Skipping %s; same as %s" % (m['name'], unique_masters[k]['name']))
        masters = new_masters

    retval = []
    for m in masters:
        # Sometimes we only want masters of a specific role to be loaded
        if role and m['role'] != role:
            continue
        if ignored_roles and m['role'] in ignored_roles:
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
                         'thunderbird_config.py',
                         '*_config.py',
                         '*_common.py',
                         'b2g_project_branches.py',
                         'project_branches.py',
                         ],
                         renames=[
                         ('BuildSlaves.py.template', 'BuildSlaves.py'),
                        ('passwords.py.template', 'passwords.py'),
                         ],
                         local_links=[
                         (environment_config, 'localconfig.py'),
                        ('thunderbird_' +
                         environment_config, 'thunderbird_localconfig.py'),
                        ('b2g_' + environment_config, 'b2g_localconfig.py'),
                         ],
                         extras=[
                         ('master_config.json', json.dumps(
                          m, indent=2, sort_keys=True)),
                         ],
                         log=log
                         )

        if universal:
            c.name += '-universal'
            mastercfg = 'universal_master_sqlite.cfg'
        else:
            if m['role'] == 'tests':
                mastercfg = 'tests_master.cfg'
            elif m['role'] == 'build' or m['role'] == 'try':
                mastercfg = 'builder_master.cfg'
            elif m['role'] == 'scheduler':
                mastercfg = 'scheduler_master.cfg'
            else:
                raise AssertionError("What is a %s role?" % m['role'])

        if m['role'] == 'build':
            c.config_dir = 'mozilla'
            c.globs.append('l10n-changesets*')
            c.globs.append('release_templates')
            if m['environment'] == 'staging':
                c.globs.append('staging_release-*-*.py')
                # release-*.py -> staging_release-*.py symlinks
                c.local_links.extend(
                    [('staging_release-firefox-mozilla-%s.py' % v,
                      'release-firefox-mozilla-%s.py' % v)
                     for v in ['beta', 'release', 'esr17', 'b2g18']
                     ] +
                    [('staging_release-fennec-mozilla-%s.py' % v,
                      'release-fennec-mozilla-%s.py' % v)
                     for v in ['beta', 'release']
                     ] +
                    [('staging_release-thunderbird-comm-%s.py' % v,
                      'release-thunderbird-comm-%s.py' % v)
                        for v in ['beta', 'release', 'esr17', 'b2g18']
                     ]
                )
            else:
                c.globs.append('release-firefox*.py')
                c.globs.append('release-fennec*.py')
                c.globs.append('release-thunderbird*.py')
            c.globs.append(mastercfg)
            c.globs.append('build_localconfig.py')
            c.local_links.append((mastercfg, 'master.cfg'))
            c.local_links.append(
                ('build_localconfig.py', 'master_localconfig.py'))
        elif m['role'] == 'try':
            c.config_dir = 'mozilla'
            c.local_links.append((mastercfg, 'master.cfg'))
            c.local_links.append(
                ('try_localconfig.py', 'master_localconfig.py'))
            c.globs.append(mastercfg)
            c.globs.append('try_localconfig.py')
        elif m['role'] == 'tests':
            c.config_dir = 'mozilla-tests'
            c.local_links.append((mastercfg, 'master.cfg'))
            c.local_links.append(
                ('tests_localconfig.py', 'master_localconfig.py'))
            c.globs.append('tests_localconfig.py')
            c.globs.append(mastercfg)
        elif m['role'] == 'scheduler':
            if 'build_scheduler' in m['name']:
                c.config_dir = 'mozilla'
                c.globs.append('release-firefox*.py')
                c.globs.append('release-fennec*.py')
                c.globs.append('release-thunderbird*.py')
                c.globs.append('release_templates')
            elif 'tests_scheduler' in m['name']:
                c.config_dir = 'mozilla-tests'
            c.globs.append(mastercfg)
            c.globs.append('scheduler_localconfig.py')
            c.local_links.append((mastercfg, 'master.cfg'))
            c.local_links.append(
                ('scheduler_localconfig.py', 'master_localconfig.py'))

        retval.append(c)
    return retval


def filter_masters(master_list):
    return [m for m in master_list if m != 'preprod-release-master']

if __name__ == "__main__":

    from optparse import OptionParser

    parser = OptionParser(__doc__)
    parser.set_defaults(action=None, masters_json=None)
    parser.add_option("-l", "--list", action="store_true", dest="list")
    parser.add_option("-t", "--test", action="store_true", dest="test")
    parser.add_option(
        "-8", action="store_true", dest="buildbot08", default=False)
    parser.add_option("-b", "--buildbot", dest="buildbot", default="buildbot")
    parser.add_option("-j", "--masters-json", dest="masters_json",
                      default="http://hg.mozilla.org/build/tools/raw-file/tip/buildfarm/maintenance/production-masters.json")
    parser.add_option("-R", "--role", dest="role", default=None)
    parser.add_option(
        "-u", "--universal", dest="universal", action="store_true")
    parser.add_option("-q", "--quiet", dest="quiet", action="store_true")
    parser.add_option(
        "-e", "--error-logs", dest="error_logs", action="store_true")
    parser.add_option("-d", "--debug", dest="debug", action="store_true")
    parser.add_option("--ignore-role", dest="ignored_roles", action="append", default=[],
                      help="Ignore masters with this role. May be passed multiple times.")

    options, args = parser.parse_args()

    if options.debug:
        loglvl = logging.DEBUG
    elif options.quiet:
        loglvl = logging.ERROR
    else:
        loglvl = logging.INFO

    ignored_roles = options.ignored_roles or ["servo"]

    log = logging.getLogger('setup-master')
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(loglvl)
    cf = logging.Formatter('%(levelname)-5s - %(message)s')
    ch.setFormatter(cf)
    log.addHandler(ch)

    log.debug('using master json file from "%s"' % options.masters_json)
    if options.role:
        log.info('filtering by "%s" roles' % options.role)

    dedupe = options.test
    master_list = load_masters_json(options.masters_json, role=options.role,
                                    log=log, universal=options.universal,
                                    dedupe=dedupe, ignored_roles=ignored_roles)
    if options.test:
        log.debug('adding universal builders because we are testing')
        # a universal scheduler master doesn't make any sense
        ignored_roles += ['scheduler']
        uni_masters = load_masters_json(options.masters_json, role=options.role, universal=not options.universal, log=log, ignored_roles=ignored_roles)
        master_list.extend(uni_masters)

    # Make sure we don't have duplicate names
    master_map = dict((m.name, m) for m in master_list)
    assert len(
        master_map.values()) == len(master_list), "Duplicate master names"
    assert len(master_list) > 0, "No masters specified. Bad role?"

    if options.list:
        for m in filter_masters(master_list):
            print m.name
    elif options.test:
        failing_masters = []
        # Test the masters, once normally and onces as a universal master
        for m in filter_masters(master_list):
            rc, logfile, dir = m.testMaster(
                options.buildbot, error_logs=options.error_logs)
            if rc != 0:
                failing_masters.append((m.name, logfile, dir))
        # Print a summary including a list of useful output
        log.info("TEST-SUMMARY: %s tested, %s failed" % (len(
            master_list), len(failing_masters)))
        for rc, logfile, dir in failing_masters:
            def s(n):
                if n is not None:
                    return n[len(os.getcwd()) + 1:]
            log.info("FAILED-MASTER %s, log: '%s', dir: '%s'" %
                     (rc, s(logfile), s(dir)))
        exit(len(failing_masters))
    elif len(args) == 2:
        master_dir, master_name = args[:2]

        if options.universal:
            master_name = master_name + '-universal'

        if master_name not in master_map:
            log.error("Unknown master %s" % master_name)

        m = master_map[master_name]
        m.createMaster(master_dir, options.buildbot)
    else:
        parser.print_usage()
        parser.exit()
