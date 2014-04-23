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
import thunderbird_config
import b2g_config
from b2g_config import PROJECTS as B2G_PROJECTS
import mobile_config
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_THUNDERBIRD_BRANCHES = thunderbird_config.BRANCHES.keys()
ACTIVE_B2G_BRANCHES = b2g_config.BRANCHES.keys()
ACTIVE_MOBILE_BRANCHES = mobile_config.BRANCHES.keys()
ACTIVE_PLATFORMS = dict((platform, None) for platform in PLATFORMS.keys())
ACTIVE_THUNDERBIRD_PLATFORMS = dict((platform, None) for platform in thunderbird_config.PLATFORMS.keys())
ACTIVE_B2G_PLATFORMS = dict((platform, None) for platform in b2g_config.PLATFORMS.keys())
ACTIVE_MOBILE_PLATFORMS = dict((platform, None) for platform in mobile_config.PLATFORMS.keys())
ACTIVE_PROJECTS = PROJECTS.keys()
ACTIVE_B2G_PROJECTS = B2G_PROJECTS.keys()

QUEUEDIR = "/dev/shm/queue"
