from buildbot.util import json
from buildbot.status.html import WebStatus
from buildbot import manhole

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

from config import BRANCHES, PROJECTS, TRY_SLAVES, BRANCH_PROJECTS
ACTIVE_BRANCHES = ['try']
ACTIVE_THUNDERBIRD_BRANCHES = ['try-comm-central']
ACTIVE_B2G_BRANCHES = ['try']
ACTIVE_RELEASE_BRANCHES = []
ACTIVE_THUNDERBIRD_RELEASE_BRANCHES = []
ACTIVE_MOBILE_RELEASE_BRANCHES = []
ACTIVE_PROJECTS = [k for k,v in PROJECTS.items() if v.get('enable_try')]
ACTIVE_BRANCH_PROJECTS = [k for k,v in BRANCH_PROJECTS.items() if v.get('enable_try')]

# Override with TRY_SLAVES
SLAVES = TRY_SLAVES

# Set up our fast slaves
# No need to reload, this is reloaded by builder_master.cfg
import buildbotcustom.misc
buildbotcustom.misc.fastRegexes.extend([
    'linux-ix-',
    'linux64-ix-',
    ])
ENABLE_RELEASES = False

QUEUEDIR = master_config.get("queuedir", "/dev/shm/queue")
