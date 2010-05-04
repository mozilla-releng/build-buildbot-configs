c = BuildmasterConfig = {}
c['slavePortnum'] = 9009 # No slaves should be connecting here

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole(1234, "cltbld", "password")

