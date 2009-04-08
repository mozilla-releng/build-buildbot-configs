from datetime import datetime
import os.path, re
from time import strftime

from twisted.python import log

from buildbot.process.factory import BuildFactory
from buildbot.steps.shell import ShellCommand, WithProperties, SetProperty
from buildbot.steps.source import Mercurial
from buildbot.steps.transfer import FileDownload

import buildbotcustom.steps.misc
import buildbotcustom.steps.release
import buildbotcustom.steps.test
import buildbotcustom.steps.transfer
import buildbotcustom.steps.updates
import buildbotcustom.unittest.steps
import buildbotcustom.process.factory
import buildbotcustom.env
reload(buildbotcustom.steps.misc)
reload(buildbotcustom.steps.release)
reload(buildbotcustom.steps.test)
reload(buildbotcustom.steps.transfer)
reload(buildbotcustom.steps.updates)
reload(buildbotcustom.unittest.steps)
reload(buildbotcustom.process.factory)
reload(buildbotcustom.env)

from buildbotcustom.steps.misc import SetMozillaBuildProperties, TinderboxShellCommand, \
  SendChangeStep, GetBuildID
from buildbotcustom.steps.release import UpdateVerify, L10nVerifyMetaDiff
from buildbotcustom.steps.test import AliveTest, CompareBloatLogs, \
  CompareLeakLogs, Codesighs, GraphServerPost
from buildbotcustom.steps.transfer import MozillaStageUpload
from buildbotcustom.steps.updates import CreateCompleteUpdateSnippet
from buildbotcustom.env import MozillaEnvironments

# we're basically just extending buildbotcustom.process.factory
from buildbotcustom.process.factory import *

import buildbotcustom.unittest.steps as unittest_steps

class CCMercurialBuildFactory(MercurialBuildFactory):
    def __init__(self, mozRepoPath, **kwargs):
        self.mozRepoPath = mozRepoPath

    def addSourceSteps(self):
        self.addStep(Mercurial, mode='update',
         baseURL='http://%s/' % self.hgHost,
         defaultBranch=self.repoPath,
         alwaysUseLatest=True,
         timeout=60*60 # 1 hour
        )

        if self.buildRevision:
            self.addStep(ShellCommand,
             command=['hg', 'up', '-C', '-r', self.buildRevision],
             haltOnFailure=True
            )
            self.addStep(SetProperty,
             command=['hg', 'identify', '-i'],
             property='got_revision'
            )
        changesetLink = '<a href=http://%s/%s/rev' % (self.hgHost, self.repoPath)
        changesetLink += '/%(got_revision)s title="Built from revision %(got_revision)s">rev:%(got_revision)s</a>'
        self.addStep(ShellCommand,
         command=['echo', 'TinderboxPrint:', WithProperties(changesetLink)]
        )
        self.addStep(ShellCommand,
         name="client.py checkout",
         command=['python', 'client.py', 'checkout']
        )

        self.addStep(SetProperty,
         command=['hg', 'identify', '-i'],
         workdir='build/mozilla',
         property='hg_revision'
        )
        changesetLink = '<a href=http://%s/%s/rev' % (self.hgHost, self.mozRepoPath)
        changesetLink += '/%(hg_revision)s title="Built from Mozilla revision %(hg_revision)s">moz:%(hg_revision)s</a>'
        self.addStep(ShellCommand,
         command=['echo', 'TinderboxPrint:', WithProperties(changesetLink)]
        )


class CCUnittestBuildFactory(MozillaBuildFactory):
    def __init__(self, platform, config_repo_path, config_dir, objdir, mozRepoPath,
            productName=None, brandName=None, mochitest_leak_threshold=None,
            mochichrome_leak_threshold=None, mochibrowser_leak_threshold=None,
            **kwargs):
        self.env = {}
        MozillaBuildFactory.__init__(self, **kwargs)
        self.config_repo_path = config_repo_path
        self.mozRepoPath = mozRepoPath
        self.config_dir = config_dir
        self.objdir = objdir
        self.productName = productName
        if brandName:
            self.brandName = brandName
        else:
            self.brandName = productName.capitalize()
        if mochitest_leak_threshold:
            self.mochitest_leak_threshold = mochitest_leak_threshold
        if mochichrome_leak_threshold:
            self.mochichrome_leak_threshold = mochichrome_leak_threshold
        if mochibrowser_leak_threshold:
            self.mochibrowser_leak_threshold = mochibrowser_leak_threshold

        self.config_repo_url = self.getRepository(self.config_repo_path)

        env_map = {
                'linux': 'linux-centos-unittest',
                'macosx': 'mac-osx-unittest',
                'win32': 'win32-vc8-mozbuild-unittest',
                }

        self.platform = platform.split('-')[0]
        assert self.platform in ('linux', 'linux64', 'win32', 'macosx')

        self.env = MozillaEnvironments[env_map[self.platform]]
        self.env['MOZ_OBJDIR'] = self.objdir

        if self.platform == 'win32':
            self.addStep(TinderboxShellCommand, name="kill hg",
             description='kill hg',
             descriptionDone="killed hg",
             command="pskill -t hg.exe",
             workdir="D:\\PsTools"
            )
            self.addStep(TinderboxShellCommand, name="kill sh",
             description='kill sh',
             descriptionDone="killed sh",
             command="pskill -t sh.exe",
             workdir="D:\\PsTools"
            )
            self.addStep(TinderboxShellCommand, name="kill make",
             description='kill make',
             descriptionDone="killed make",
             command="pskill -t make.exe",
             workdir="D:\\PsTools"
            )
            self.addStep(TinderboxShellCommand, name="kill %s" % self.productName,
             description='kill %s' % self.productName,
             descriptionDone="killed %s" % self.productName,
             command="pskill -t %s.exe" % self.productName,
             workdir="D:\\PsTools"
            )
            self.addStep(TinderboxShellCommand, name="kill xpcshell",
             description='kill xpcshell',
             descriptionDone="killed xpcshell",
             command="pskill -t xpcshell.exe",
             workdir="D:\\PsTools"
            )

        self.addStepNoEnv(Mercurial, mode='update',
         baseURL='http://%s/' % self.hgHost,
         defaultBranch=self.repoPath,
         alwaysUseLatest=True,
         timeout=60*60 # 1 hour
        )

        self.addPrintChangesetStep()

        self.addStepNoEnv(ShellCommand,
         name="client.py checkout",
         command=['python', 'client.py', 'checkout']
        )

        self.addPrintMozillaChangesetStep()

        self.addStep(ShellCommand,
         name="clean configs",
         command=['rm', '-rf', 'mozconfigs'],
         workdir='.'
        )

        self.addStep(ShellCommand,
         name="buildbot configs",
         command=['hg', 'clone', self.config_repo_url, 'mozconfigs'],
         workdir='.'
        )

        self.addCopyMozconfigStep()

        self.addStep(ShellCommand, name='mozconfig contents',
         command=['cat', '.mozconfig']
        )

        self.addStep(ShellCommand,
         command=["make", "-f", "client.mk", "build"],
         description=['compile'],
         timeout=60*60, # 1 hour
         haltOnFailure=1
        )
        self.addStep(ShellCommand,
                     command=['make', 'buildsymbols'],
                     workdir='build/%s' % self.objdir,
                     )

        self.addStep(SetProperty,
         command=['bash', '-c', 'pwd'],
         property='toolsdir',
         workdir='tools'
        )

        platform_minidump_path = {
            'linux': WithProperties('%(toolsdir:-)s/breakpad/linux/minidump_stackwalk'),
            'win32': WithProperties('%(toolsdir:-)s/breakpad/win32/minidump_stackwalk.exe'),
            'macosx': WithProperties('%(toolsdir:-)s/breakpad/osx/minidump_stackwalk'),
            }

        self.env['MINIDUMP_STACKWALK'] = platform_minidump_path[self.platform]

        self.addPreTestSteps()

        self.addStep(unittest_steps.MozillaCheck,
         test_name="check",
         warnOnWarnings=True,
         workdir="build/%s" % self.objdir,
         timeout=5*60, # 5 minutes.
        )

        self.addStep(unittest_steps.MozillaCheck,
         test_name="xpcshell-tests",
         warnOnWarnings=True,
         workdir="build/%s" % self.objdir,
         timeout=5*60, # 5 minutes.
        )

        if platform == 'win32':
            self.addStep(unittest_steps.CreateProfileWin,
             warnOnWarnings=True,
             workdir="build",
             command = r'python mozilla\testing\tools\profiles\createTestingProfile.py --clobber --binary %s\mozilla\dist\bin\%s.exe' %
                          (self.objdir, self.productName),
             clobber=True
            )
        else:
            if platform == 'macosx':
                app_run = '%s.app/Contents/MacOS/%s-bin' % (self.brandName, self.productName)
            else:
                app_run = 'bin/%s' % self.productName
            self.addStep(unittest_steps.CreateProfile,
             warnOnWarnings=True,
             workdir="build",
             command = r'python mozilla/testing/tools/profiles/createTestingProfile.py --clobber --binary %s/mozilla/dist/%s' %
                          (self.objdir, app_run),
             clobber=True
            )

        self.addStep(unittest_steps.MozillaReftest, warnOnWarnings=True,
         test_name="reftest",
         workdir="build/%s" % self.objdir,
         timeout=5*60,
        )
        self.addStep(unittest_steps.MozillaReftest, warnOnWarnings=True,
         test_name="crashtest",
         workdir="build/%s" % self.objdir,
        )
        if self.mochitest_leak_threshold:
            extra_args = "EXTRA_TEST_ARGS='--leak-threshold=%s'" % self.mochitest_leak_threshold
        else:
            extra_args = ""
        self.addStep(unittest_steps.MozillaMochitest, warnOnWarnings=True,
         test_name="mochitest-plain",
         command = ["make", "mochitest-plain", extra_args],
         workdir="build/%s" % self.objdir,
         leakThreshold=mochitest_leak_threshold,
         timeout=5*60,
        )
        if self.mochichrome_leak_threshold:
            extra_args = "EXTRA_TEST_ARGS='--leak-threshold=%s'" % self.mochichrome_leak_threshold
        else:
            extra_args = ""
        self.addStep(unittest_steps.MozillaMochitest, warnOnWarnings=True,
         test_name="mochitest-chrome",
         command = ["make", "mochitest-chrome", extra_args],
         workdir="build/%s" % self.objdir,
        )
        if self.mochibrowser_leak_threshold:
            extra_args = "EXTRA_TEST_ARGS='--leak-threshold=%s'" % self.mochibrowser_leak_threshold
        else:
            extra_args = ""
        self.addStep(unittest_steps.MozillaMochitest, warnOnWarnings=True,
         test_name="mochitest-browser-chrome",
         command = ["make", "mochitest-browser-chrome", extra_args],
         workdir="build/%s" % self.objdir,
        )
        if not self.platform == 'macosx':
          self.addStep(unittest_steps.MozillaMochitest, warnOnWarnings=True,
           test_name="mochitest-a11y",
           workdir="build/%s" % self.objdir,
          )

        self.addPostTestSteps()

        if self.buildsBeforeReboot and self.buildsBeforeReboot > 0:
            self.addPeriodicRebootSteps()

    def addPrintChangesetStep(self):
        changesetLink = '<a href=http://%s/%s/rev' % (self.hgHost, self.repoPath)
        changesetLink += '/%(got_revision)s title="Built from revision %(got_revision)s">rev:%(got_revision)s</a>'
        self.addStep(ShellCommand,
         command=['echo', 'TinderboxPrint:', WithProperties(changesetLink)],
        )

    def addPrintMozillaChangesetStep(self):
        self.addStep(SetProperty,
         command=['hg', 'identify', '-i'],
         workdir='build/mozilla',
         property='hg_revision'
        )
        changesetLink = '<a href=http://%s/%s/rev' % (self.hgHost, self.mozRepoPath)
        changesetLink += '/%(hg_revision)s title="Built from Mozilla revision %(hg_revision)s">moz:%(hg_revision)s</a>'
        self.addStep(ShellCommand,
         command=['echo', 'TinderboxPrint:', WithProperties(changesetLink)]
        )

    def addStep(self, *args, **kw):
        kw.setdefault('env', self.env)
        return BuildFactory.addStep(self, *args, **kw)

    def addStepNoEnv(self, *args, **kw):
        return BuildFactory.addStep(self, *args, **kw)

    def addCopyMozconfigStep(self):
        config_dir_map = {
                'linux': 'linux/%s/unittest' % self.branchName,
                'macosx': 'macosx/%s/unittest' % self.branchName,
                'win32': 'win32/%s/unittest' % self.branchName,
                }
        mozconfig = 'mozconfigs/%s/%s/mozconfig' % \
            (self.config_dir, config_dir_map[self.platform])

        self.addStep(ShellCommand, name="copy mozconfig",
         command=['cp', mozconfig, 'build/.mozconfig'],
         description=['copy mozconfig'],
         workdir='.'
        )

    def addPreTestSteps(self):
        pass

    def addPostTestSteps(self):
        pass
