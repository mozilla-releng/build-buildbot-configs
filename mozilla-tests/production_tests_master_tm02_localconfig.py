c = BuildmasterConfig = {}
c['slavePortnum'] = 9012

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8012, allowForce=True)
]

c['buildbotURL'] = 'http://test-master02.build.mozilla.org:8012/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1235:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
# macosx64 is here so that the leopard slaves test the i386+x86_64 universal
# binary, opt unit and talos
ACTIVE_PLATFORMS = {'macosx': None, 'linux': None, 'macosx64': None}
