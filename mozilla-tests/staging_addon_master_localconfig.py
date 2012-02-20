c = BuildmasterConfig = {}
c['slavePortnum'] = 9010

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8010, allowForce=True)
]

c['buildbotURL'] = 'http://talos-addon-master1.amotest.scl1.mozilla.com:8010/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1235:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, PLATFORMS, PROJECTS
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
# I changed my mind; do only trunk
ACTIVE_BRANCHES = ['addontester', 'addonbaselinetester']
ACTIVE_PROJECTS = [] #PROJECTS.keys()
ACTIVE_PLATFORMS = dict((k,None) for k in PLATFORMS.keys())

QUEUEDIR = "/dev/shm/queue"
