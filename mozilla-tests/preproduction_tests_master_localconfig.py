c = BuildmasterConfig = {}
c['slavePortnum'] = 9012

from buildbot.status.html import WebStatus
c['status'] = [
    WebStatus(http_port=8012, allowForce=True)
]

c['buildbotURL'] = 'http://preproduction-master.srv.releng.scl3.mozilla.com:8012/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1236:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, PLATFORMS, PROJECTS
import thunderbird_config
import b2g_config
from b2g_config import PROJECTS as B2G_PROJECTS
import mobile_config
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_THUNDERBIRD_BRANCHES = thunderbird_config.BRANCHES.keys()
ACTIVE_B2G_BRANCHES = b2g_config.BRANCHES.keys()
ACTIVE_MOBILE_BRANCHES = mobile_config.BRANCHES.keys()
ACTIVE_PLATFORMS = dict((platform, None) for platform in PLATFORMS.keys())
ACTIVE_THUNDERBIRD_PLATFORMS = dict((platform, None) for platform in thunderbird_config.PLATFORMS.keys())
ACTIVE_MOBILE_PLATFORMS = dict((platform, None) for platform in mobile_config.PLATFORMS.keys())
ACTIVE_PROJECTS = PROJECTS.keys()
ACTIVE_B2G_PROJECTS = B2G_PROJECTS.keys()

QUEUEDIR = "/dev/shm/queue"
