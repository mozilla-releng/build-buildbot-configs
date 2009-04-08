
from twisted.application import service
from buildbot.master import BuildMaster

basedir = r'/home/gozer/opt/src/mozilla.org/build/buildbot-configs/thunderbird-unittest'
configfile = r'master.cfg'

application = service.Application('buildmaster')
BuildMaster(basedir, configfile).setServiceParent(application)

