c = BuildmasterConfig = {}
c['slavePortnum'] = 9012

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8012, allowForce=True)
]

c['buildbotURL'] = 'http://tools-staging-master02.mv.mozilla.com:8012/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1235:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, PLATFORMS, PROJECTS
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
# I changed my mind; do only trunk
ACTIVE_BRANCHES = ['mozilla-central']
ACTIVE_PROJECTS = PROJECTS.keys()
ACTIVE_PLATFORMS = dict((k,None) for k in PLATFORMS.keys())

QUEUEDIR = "/dev/shm/queue"
