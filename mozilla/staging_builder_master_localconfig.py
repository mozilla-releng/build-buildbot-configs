c = BuildmasterConfig = {}
c['slavePortnum'] = 9010

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8010, allowForce=True)
]

c['buildbotURL'] = 'http://staging-master.build.mozilla.org:8010/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole(1235, "cltbld", "password")

from config import BRANCHES
# Do everything!
#ACTIVE_BRANCHES = BRANCHES.keys()
#ACTIVE_BRANCHES.remove('tryserver')
# I changed my mind; do only trunk
ACTIVE_BRANCHES = ['mozilla-central']
