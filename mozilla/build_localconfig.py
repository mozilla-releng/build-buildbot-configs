from buildbot.util import json
from buildbot.status.html import WebStatus
from buildbot import manhole
import master_common

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
from thunderbird_config import ACTIVE_PROJECT_BRANCHES as ACTIVE_THUNDERBIRD_PROJECT_BRANCHES
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
        'mozilla-esr31',
        'mozilla-b2g28_v1_3t',
        'mozilla-b2g30_v1_4',
        'mozilla-b2g32_v2_0',
        'mozilla-b2g34_v2_1',
    ])
if 'limit_tb_branches' in master_config:
    ACTIVE_THUNDERBIRD_BRANCHES = [x.encode("utf-8") for x in master_config['limit_tb_branches']]
else:
    ACTIVE_THUNDERBIRD_BRANCHES = ACTIVE_THUNDERBIRD_PROJECT_BRANCHES[:]
    ACTIVE_THUNDERBIRD_BRANCHES.extend([
        'comm-central',
        'comm-beta',
        'comm-aurora',
        'comm-esr31',
    ])
if 'limit_b2g_branches' in master_config:
    ACTIVE_B2G_BRANCHES = [x.encode("utf-8") for x in master_config['limit_b2g_branches']]
else:
    ACTIVE_B2G_BRANCHES = ACTIVE_B2G_PROJECT_BRANCHES[:]
    ACTIVE_B2G_BRANCHES.extend([
        'mozilla-central',
        'mozilla-b2g28_v1_3t',
        'mozilla-b2g30_v1_4',
        'mozilla-b2g32_v2_0',
        'mozilla-b2g34_v2_1',
    ])
    # MERGE DAY: Remove the following block when we are sure b2g CI is moved to
    # taskcluster
    # Add mozilla-aurora on odd-numbered m-c gecko versions
    # b = {'mozilla-central': {}}
    # master_common.setMainFirefoxVersions(b)
    # Starting with v2.2, b2g automation will be handled by taskcluster
    # if b['mozilla-central']['gecko_version'] % 2:
    #    ACTIVE_B2G_BRANCHES.append('mozilla-aurora')
    # MERGE DAY: end

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

QUEUEDIR = master_config.get("queuedir", "/dev/shm/queue")
