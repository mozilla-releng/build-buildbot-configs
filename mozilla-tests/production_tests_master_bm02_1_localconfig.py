c = BuildmasterConfig = {}
c['slavePortnum'] = 9011

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8011, allowForce=True)
]

c['buildbotURL'] = 'http://buildbot-master2.build.scl1.mozilla.com:8011/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1236:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, PLATFORMS, PROJECTS
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_PLATFORMS = dict((k,None) for k in PLATFORMS.keys())
ACTIVE_PROJECTS = PROJECTS.keys()

QUEUEDIR = "/dev/shm/queue"
