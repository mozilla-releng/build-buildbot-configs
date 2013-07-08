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

from config import BRANCHES, SLAVES, PROJECTS, ACTIVE_PROJECT_BRANCHES, BRANCH_PROJECTS
from b2g_config import ACTIVE_PROJECT_BRANCHES as ACTIVE_B2G_PROJECT_BRANCHES
if 'limit_branches' in master_config:
    ACTIVE_BRANCHES = [x.encode("utf-8") for x in master_config['limit_branches']]
else:
    ACTIVE_BRANCHES = ACTIVE_PROJECT_BRANCHES[:]
    ACTIVE_BRANCHES.extend([
        'mozilla-central',
        'mozilla-beta',
        'mozilla-aurora',
        'mozilla-release',
        'mozilla-esr17',
        'mozilla-b2g18',
        'mozilla-b2g18_v1_0_1',
        'mozilla-b2g18_v1_1_0_hd',
    ])
if 'limit_tb_branches' in master_config:
    ACTIVE_THUNDERBIRD_BRANCHES = [x.encode("utf-8") for x in master_config['limit_tb_branches']]
else:
    ACTIVE_THUNDERBIRD_BRANCHES = [
        'comm-central',
        'comm-beta',
        'comm-aurora',
        'comm-release',
        'comm-esr17',
    ]
if 'limit_b2g_branches' in master_config:
    ACTIVE_B2G_BRANCHES = [x.encode("utf-8") for x in master_config['limit_b2g_branches']]
else:
    ACTIVE_B2G_BRANCHES = ACTIVE_B2G_PROJECT_BRANCHES[:]
    ACTIVE_B2G_BRANCHES.extend([
        'mozilla-central',
        'mozilla-b2g18',
        'mozilla-b2g18_v1_0_1',
        'mozilla-b2g18_v1_1_0_hd',
    ])

if 'limit_projects' in master_config:
    ACTIVE_PROJECTS = [x.encode("utf-8") for x in master_config['limit_projects']]
else:
    ACTIVE_PROJECTS = PROJECTS.keys()
ACTIVE_PROJECTS = [p for p in ACTIVE_PROJECTS if not PROJECTS[p].get('enable_try')]

if 'limit_branch_projects' in master_config:
    ACTIVE_BRANCH_PROJECTS = [x.encode("utf-8") for x in master_config['limit_branch_projects']]
else:
    ACTIVE_BRANCH_PROJECTS = BRANCH_PROJECTS.keys()
ACTIVE_BRANCH_PROJECTS = [p for p in ACTIVE_BRANCH_PROJECTS if not BRANCH_PROJECTS[p].get('enable_try')]

ACTIVE_RELEASE_BRANCHES = []
ACTIVE_THUNDERBIRD_RELEASE_BRANCHES = []
ACTIVE_MOBILE_RELEASE_BRANCHES = []
ENABLE_RELEASES = False
if 'release_branches' in master_config:
    ACTIVE_RELEASE_BRANCHES.extend(master_config['release_branches'])
    ENABLE_RELEASES = True
if 'thunderbird_release_branches' in master_config:
    ACTIVE_THUNDERBIRD_RELEASE_BRANCHES.extend(master_config['thunderbird_release_branches'])
    ENABLE_RELEASES = True
if 'mobile_release_branches' in master_config:
    ACTIVE_MOBILE_RELEASE_BRANCHES.extend(master_config['mobile_release_branches'])
    ENABLE_RELEASES = True

# Set up our fast slaves
# No need to reload, this is reloaded by builder_master.cfg
import buildbotcustom.misc
buildbotcustom.misc.fastRegexes.extend([
    'linux-ix-',
    'linux64-ix-',
    ])

QUEUEDIR = master_config.get("queuedir", "/dev/shm/queue")
