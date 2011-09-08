c = BuildmasterConfig = {}
c['slavePortnum'] = 9010

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8010, allowForce=True)
]

c['buildbotURL'] = 'http://preproduction-master.build.mozilla.org:8010/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1235:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, SLAVES, PROJECTS
ACTIVE_BRANCHES = [b for b in BRANCHES.keys() if b != 'mozilla-1.9.1']
ACTIVE_PROJECTS = [p for p in PROJECTS.keys() if p != 'fuzzing']
ACTIVE_RELEASE_BRANCHES = []
ACTIVE_MOBILE_RELEASE_BRANCHES = []

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
