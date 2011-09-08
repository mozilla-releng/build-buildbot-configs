c = BuildmasterConfig = {}
c['slavePortnum'] = 9201

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8201, allowForce=True)
]

c['buildbotURL'] = 'http://buildbot-master04.build.mozilla.org:8201/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:7201:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, PLATFORMS, PROJECTS
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_PLATFORMS = {'macosx': None, 'macosx64': None, 'linux': None, 'linux64': None}
ACTIVE_PROJECTS = PROJECTS.keys()

QUEUEDIR = "/dev/shm/queue"
