c = BuildmasterConfig = {}
c['slavePortnum'] = 9009 # No slaves should be connecting here

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1234:interface=127.0.0.1", "cltbld", "password")

