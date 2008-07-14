# -*- Python -*-

from buildbot.process import factory
#from buildbot.process import step
#from buildbot.process.step import ShellCommand
from buildbot.steps.shell import ShellCommand

MozillaEnvironments = { }

# standard vc8 express build env; vc8 normal will be very similar, just different
# platform SDK location.  we can build both from one generic template.
MozillaEnvironments['vc8_express'] = {
    "MOZ_TOOLS": '/cygdrive/d/moztools',
    "VSINSTALLDIR": 'C:\\Program Files\\Microsoft Visual Studio 8',
    "VS80COMMTOOLS": 'C:\\Program Files\\Microsoft Visual Studio 8\\Common7\\Tools\\',
    "VCINSTALLDIR": 'C:\\Program Files\\Microsoft Visual Studio 8\\VC',
    "FrameworkDir": 'C:\\WINDOWS\\Microsoft.NET\\Framework',
    "FrameworkVersion": 'v2.0.50727',
    "FrameworkSDKDir": 'C:\\Program Files\\Microsoft Visual Studio 8\\SDK\\v2.0',
    "DevEnvDir": "C:\\Program Files\\Microsoft Visual Studio 8\\VC\\Common7\\IDE",
    "MSVCDir": 'C:\\Program Files\\Microsoft Visual Studio 8\\VC',
    "PATH": 'C:\\Program Files\\Microsoft Visual Studio 8\\Common7\\IDE;' + \
            'C:\\Program Files\\Microsoft Visual Studio 8\\VC\\bin;' + \
            'C:\\Program Files\\Microsoft Visual Studio 8\\VC\\PlatformSDK\\bin;' + \
            'C:\\Program Files\\Microsoft Visual Studio 8\\VC;' + \
            'C:\\Program Files\\Microsoft Visual Studio 8\\Common7\\Tools;' + \
            'C:\\Program Files\\Microsoft Visual Studio 8\\Common7\\Tools\\bin;' + \
            'd:\\moztools\\bin;' + \
            'd:\\cygwin\\bin;' + \
            'd:\\buildtools\\NSIS;' + \
            'd:\\buildtools\\7-zip;' + \
            'd:\\buildtools\\upx;' + \
	    'C:\\WINDOWS\system32;',
    "INCLUDE": 'C:\\Program Files\\Microsoft Visual Studio 8\\VC\\ATLMFC\\INCLUDE;' + \
               'C:\\Program Files\\Microsoft Visual Studio 8\\VC\\INCLUDE;' + \
               'C:\\Program Files\\Microsoft Visual Studio 8\\VC\\PlatformSDK\\include',
    "LIB": 'C:\\Program Files\\Microsoft Visual Studio 8\\VC\\ATLMFC\\LIB;' + \
           'C:\\Program Files\\Microsoft Visual Studio 8\\VC\\LIB;' + \
           'C:\\Program Files\\Microsoft Visual Studio 8\\VC\\PlatformSDK\\lib'
}

class MozillaCheckoutClientMk(ShellCommand):
    haltOnFailure = True
    cvsroot = ":pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot"
    
    def __init__(self, **kwargs):
        if 'cvsroot' in kwargs:
            self.cvsroot = kwargs['cvsroot']
        if not 'command' in kwargs:
            kwargs['command'] = ["cvs", "-d", self.cvsroot, "co", "mozilla/client.mk"]
        ShellCommand.__init__(self, **kwargs)

    def describe(self, done=False):
        return ["client.mk update"]

class MozillaClientMkPull(ShellCommand):
    haltOnFailure = True
    def __init__(self, **kwargs):
        if not 'project' in kwargs or kwargs['project'] is None:
            self.project = "browser"
        else:
            self.project = kwargs['project']
            del kwargs['project']
        if not 'workdir' in kwargs:
            kwargs['workdir'] = "mozilla"
        if not 'command' in kwargs:
            kwargs['command'] = ["make", "-f", "client.mk", "pull_all"]
        env = {}
        if 'env' in kwargs:
            env = kwargs['env'].copy()
        env['MOZ_CO_PROJECT'] = self.project
        kwargs['env'] = env
        ShellCommand.__init__(self, **kwargs)

    def describe(self, done=False):
        if not done:
            return ["pulling (" + self.project + ")"]
        return ["pull (" + self.project + ")"]

class MozillaPackage(ShellCommand):
    name = "package"
    warnOnFailure = True
    description = ["packaging"]
    descriptionDone = ["package"]
    command = ["make"]

