c = BuildmasterConfig = {}
c['slavePortnum'] = 9008 # No slaves should be connecting here

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1233:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, PLATFORMS, PROJECTS
# Do everything!
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_PLATFORMS = dict((platform, None) for platform in PLATFORMS.keys())
ACTIVE_PROJECTS = PROJECTS.keys()

QUEUEDIR = "/dev/shm/queue"
