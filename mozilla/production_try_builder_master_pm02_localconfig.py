c = BuildmasterConfig = {}
c['slavePortnum'] = 9011

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8011, allowForce=True)
]

c['buildbotURL'] = 'http://production-master02.build.mozilla.org:8011/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1236:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, TRY_SLAVES, PROJECTS
ACTIVE_BRANCHES = ['try']
ACTIVE_RELEASE_BRANCHES = []
ACTIVE_MOBILE_RELEASE_BRANCHES = []
# Override with TRY_SLAVES
SLAVES = TRY_SLAVES

# Don't do any projects
ACTIVE_PROJECTS = []

# Set up our fast slaves
# No need to reload, this is reloaded by builder_master.cfg
import buildbotcustom.misc
buildbotcustom.misc.fastRegexes.extend([
    'linux-ix-',
    'linux64-ix-',
    'xserve',
    ])
ENABLE_RELEASES = False
RESERVED_SLAVES = None

QUEUEDIR = "/dev/shm/queue"
