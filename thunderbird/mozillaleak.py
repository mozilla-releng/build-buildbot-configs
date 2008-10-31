from buildbot.steps.shell import Compile, ShellCommand


import buildbotcustom.steps.misc
import buildbotcustom.steps.test
import buildbotcustom.steps.transfer
import buildbotcustom.steps.updates
reload(buildbotcustom.steps.misc)
reload(buildbotcustom.steps.test)
reload(buildbotcustom.steps.transfer)
reload(buildbotcustom.steps.updates)

from buildbotcustom.steps.misc import SetMozillaBuildProperties
from buildbotcustom.steps.test import AliveTest, CompareBloatLogs, \
  CompareLeakLogs, Codesighs, GraphServerPost
from buildbotcustom.steps.transfer import MozillaStageUpload
from buildbotcustom.steps.updates import CreateCompleteUpdateSnippet

def addLeakTestSteps(self,branch,platform,platformName):
        # we want the same thing run a few times here, with different
        # extraArgs
        env = platform['env']
        objdir = platform['platform_objdir']
        leak_threshold = platform.get('leak_threshold', branch.get('leak_threshold', 7261838))
        self.addStep(ShellCommand,
            description=['run leak tests'],
            env=env,
            command=['perl','mailnews/test/performance/bloat/runtest.pl',objdir],
        )
        self.addStep(ShellCommand,
         env=env,
         command=['cp', 'bloat.log', '../bloat.log'],
        )
        self.addStep(CompareBloatLogs,
         bloatLog='../bloat.log',
         bloatDiffPath='mozilla/tools/rb/bloatdiff.pl',
         env=env,
         testnameprefix='Mail',
         testname='Mail',
        )
        self.addStep(ShellCommand,
         env=env,
         command=['cp', 'malloc.log','../malloc.log',],
        )
        self.addStep(ShellCommand,
         env=env,
         command=['cp', 'sdleak.log', '../sdleak.log',],
        )
        self.addStep(CompareLeakLogs,
         mallocLog='../malloc.log',
         platform=platformName,
         leakFailureThreshold=leak_threshold,
         env=env,
         objdir='objdir-tb/mozilla',
         testname='current',
         testnameprefix='Mail'
        )
#        self.addStep(GraphServerPost,
#         server=self.graphServer,
#         selector=self.graphSelector,
#         branch=self.graphBranch,
#         resultsname=self.baseName
#        )
        self.addStep(CompareLeakLogs,
         mallocLog='../malloc.log.old',
         platform=platformName,
         leakFailureThreshold=leak_threshold,
         env=env,
         objdir="objdir-tb/mozilla",
         testname='previous',
         testnameprefix='Mail'
        )
        self.addStep(ShellCommand,
         env=env,
         workdir='.',
         command=['bash', '-c',
                  'perl build/mozilla/tools/trace-malloc/diffbloatdump.pl '
                  '--depth=15 --use-address /dev/null sdleak.log '
                  '> sdleak.tree']
        )
        self.addStep(ShellCommand,
          env=env,
          command=['cp', '../sdleak.log', '../sdleak.log.old'],
        )
        self.addStep(ShellCommand,
          env=env,
          command=['cp', '../malloc.log', '../malloc.log.old'],
        )
        self.addStep(ShellCommand,
          env=env,
          command=['cp', '../bloat.log', '../bloat.log.old'],
        )
        if platformName in ('macosx', 'linux'):
            self.addStep(ShellCommand,
             env=env,
             workdir='.',
             command=['cp', 'sdleak.tree', 'sdleak.tree.raw']
            )
            self.addStep(ShellCommand,
             env=env,
             workdir='.',
             command=['/bin/bash', '-c', 
                      'perl '
                      'build/mozilla/tools/rb/fix-%s-stack.pl '
                      'sdleak.tree.raw '
                      '> sdleak.tree' % platformName]
            )
        self.addStep(ShellCommand,
         env=env,
         command=['perl', 'mozilla/tools/trace-malloc/diffbloatdump.pl',
                  '--depth=15', '../sdleak.tree.old', '../sdleak.tree']
        )
        self.addStep(ShellCommand,
          env=env,
          command=['cp', '../sdleak.tree', '../sdleak.tree.old'],
        )

