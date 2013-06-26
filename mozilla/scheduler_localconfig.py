from buildbot.util import json
from buildbot import manhole

master_config = json.load(open('master_config.json'))

c = BuildmasterConfig = {}
c['slavePortnum'] = master_config.get('pb_port', None)

if 'ssh_port' in master_config:
    c['manhole'] = manhole.PasswordManhole(
            "tcp:%(ssh_port)i:interface=127.0.0.1" % master_config,
            "cltbld", "password")

QUEUEDIR = "/dev/shm/queue"

from config import BRANCH_PROJECTS

ACTIVE_RELEASE_BRANCHES = []
ACTIVE_THUNDERBIRD_RELEASE_BRANCHES = []
ACTIVE_MOBILE_RELEASE_BRANCHES = []
ACTIVE_BRANCH_PROJECTS = [k for k,v in BRANCH_PROJECTS.items() if not v.get('enable_try')]
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
