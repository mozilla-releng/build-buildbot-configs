c = BuildmasterConfig = {}
c['slavePortnum'] = 9012

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8012, allowForce=True)
]

c['buildbotURL'] = 'http://staging-master.build.mozilla.org:8012/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1237:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, SLAVES
ACTIVE_BRANCHES = BRANCHES.keys()

# Set up our fast slaves
# No need to reload, this is reloaded by builder_master.cfg
import buildbotcustom.misc
buildbotcustom.misc.fastRegexes.extend([
    '-ix-',
    'xserve',
    ])
