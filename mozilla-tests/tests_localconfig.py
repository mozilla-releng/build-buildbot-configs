from buildbot.util import json
from buildbot.status.html import WebStatus
from buildbot import manhole
from thunderbird_config import PLATFORMS as THUNDERBIRD_PLATFORMS

master_config = json.load(open('master_config.json'))

c = BuildmasterConfig = {}
c['slavePortnum'] = master_config.get('pb_port', None)
c['status'] = []

if 'http_port' in master_config:
    c['status'].append(
        WebStatus(http_port=master_config['http_port'], allowForce=True))
    c['buildbotURL'] = 'http://%(hostname)s:%(http_port)i/' % master_config

if 'ssh_port' in master_config:
    c['manhole'] = manhole.PasswordManhole(
        "tcp:%(ssh_port)i:interface=127.0.0.1" % master_config,
        "cltbld", "password")

from config import BRANCHES, PLATFORMS, PROJECTS
import thunderbird_config
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_THUNDERBIRD_BRANCHES = thunderbird_config.BRANCHES.keys()
if 'limit_fx_platforms' in master_config:
    ACTIVE_PLATFORMS = dict((p, None) for p in master_config['limit_fx_platforms'])
else:
    ACTIVE_PLATFORMS = dict((k, None) for k in PLATFORMS.keys())
if 'limit_fx_slave_platforms' in master_config:
    ACTIVE_FX_SLAVE_PLATFORMS = master_config['limit_fx_slave_platforms']
else:
    ACTIVE_FX_SLAVE_PLATFORMS = {}
if 'limit_tb_platforms' in master_config:
    ACTIVE_THUNDERBIRD_PLATFORMS = dict((p, None) for p in master_config['limit_tb_platforms'])
else:
    ACTIVE_THUNDERBIRD_PLATFORMS = dict((k, None) for k in THUNDERBIRD_PLATFORMS.keys())
ACTIVE_PROJECTS = PROJECTS.keys()

QUEUEDIR = master_config.get("queuedir", "/dev/shm/queue")
