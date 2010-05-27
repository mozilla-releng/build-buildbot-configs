
from twisted.application import service
from buildbot.master import BuildMaster

from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile

basedir = r'/buildbot/buildbot-configs/calendar'
configfile = r'master.cfg'

logfile = DailyLogFile("twistd.log", "logs")
application = service.Application('buildmaster')

application.setComponent(ILogObserver, FileLogObserver(logfile).emit)
BuildMaster(basedir, configfile).setServiceParent(application)




