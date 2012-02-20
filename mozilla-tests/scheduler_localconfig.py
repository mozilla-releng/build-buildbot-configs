from buildbot.util import json
from buildbot import manhole

master_config = json.load(open('master_config.json'))

c = BuildmasterConfig = {}
c['slavePortnum'] = master_config.get('pb_port', None)

if 'ssh_port' in master_config:
    c['manhole'] = manhole.PasswordManhole(
            "tcp:%(ssh_port)i:interface=127.0.0.1" % master_config,
            "cltbld", "password")

from config import BRANCHES, PLATFORMS, PROJECTS
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_PLATFORMS = dict((platform, None) for platform in PLATFORMS.keys())
ACTIVE_PROJECTS = PROJECTS.keys()

QUEUEDIR = "/dev/shm/queue"
