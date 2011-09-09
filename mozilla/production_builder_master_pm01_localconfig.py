c = BuildmasterConfig = {}
c['slavePortnum'] = 9010

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8010, allowForce=True)
]

c['buildbotURL'] = 'http://production-master01.build.mozilla.org:8010/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1235:interface=127.0.0.1", "cltbld", "password")

import config
reload(config)
from config import BRANCHES, SLAVES, PROJECTS, ACTIVE_PROJECT_BRANCHES
ACTIVE_BRANCHES = ['shadow-central', 'mozilla-1.9.2', 'mozilla-central',
        'mozilla-beta', 'mozilla-aurora', 'mozilla-release',
] + ACTIVE_PROJECT_BRANCHES
ACTIVE_PROJECTS = PROJECTS.keys()
ACTIVE_RELEASE_BRANCHES = ['mozilla-1.9.1', 'mozilla-release',]
ACTIVE_MOBILE_RELEASE_BRANCHES = []

# Set up our fast slaves
# No need to reload, this is reloaded by builder_master.cfg
import buildbotcustom.misc
buildbotcustom.misc.fastRegexes.extend([
    'linux-ix-',
    'linux64-ix-',
    'xserve',
    ])
ENABLE_RELEASES = True
RESERVED_SLAVES = "reserved_slaves_pm01"

QUEUEDIR = "/dev/shm/queue"
