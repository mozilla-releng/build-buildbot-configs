c = BuildmasterConfig = {}
c['slavePortnum'] = 9012

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8012, allowForce=True)
]

c['buildbotURL'] = 'http://talos-master02.build.mozilla.org:8012/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1235:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_PLATFORMS = {'win32': None, 'linux64': None, 'macosx64': None}
