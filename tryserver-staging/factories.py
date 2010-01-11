from buildbot.process import factory
from buildbot.steps.shell import ShellCommand, WithProperties, SetProperty

import buildbotcustom.env
import buildbotcustom.steps.misc
import buildbotcustom.steps.tryserver
import buildbotcustom.steps.unittest as unittest
reload(buildbotcustom.env)
reload(buildbotcustom.steps.misc)
reload(buildbotcustom.steps.tryserver)
reload(unittest)

from buildbotcustom.env import MozillaEnvironments
from buildbotcustom.steps.misc import TinderboxShellCommand, SendChangeStep
from buildbotcustom.steps.tryserver import MozillaTryProcessing, \
  MozillaClientMk, MozillaDownloadMozconfig, MozillaPatchDownload, \
  MozillaCustomPatch, MozillaCreateUploadDirectory, MozillaUploadTryBuild, \
  MozillaTryServerHgClone

import config
reload(config)
from config import *

s = factory.s

try_cvs_linux_factory = factory.BuildFactory([
    s(MozillaTryProcessing),
    s(ShellCommand, name="remove source and obj dirs",
                    command=["rm", "-rf", "mozilla"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    workdir="."),

    s(ShellCommand, name="dump env vars",
                    workdir=".",
                    command="env | sort"),

    s(MozillaClientMk, cvsroot=CVSROOT),

    s(MozillaDownloadMozconfig, mastersrc="mozconfig-linux",
                                patchDir="patches/"),

    s(ShellCommand, name="source checkout",
                    description=["fetching source"],
                    descriptionDone=["source"],
                    command=["make", "-f", "client.mk", "checkout"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    workdir="mozilla",
                    env={'MOZ_CO_PROJECT': 'browser'}),

    s(MozillaPatchDownload, patchDir="patches/",
                            haltOnFailure=True,
                            flunkOnFailure=True,
                            workdir="mozilla"),
    s(MozillaCustomPatch, workdir="mozilla",
                          haltOnFailure=True,
                          flunkOnFailure=True),

    s(ShellCommand, name="mozconfig contents",
                    command=["cat",".mozconfig"],
                    workdir="mozilla"),

    s(ShellCommand, name="building",
                    description=["building"],
                    descriptionDone=["compile"],
                    command=["make", "-f", "client.mk", "build"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    timeout=3600,
                    workdir="mozilla"),

    s(ShellCommand, name="packaging",
                    description=["creating package"],
                    descriptionDone=["packaging"],
                    command=["make", "package",
                            WithProperties(''.join(["PKG_BASENAME=%s",
                                           "-%s-linux" % PKG_BASENAME]),
                                           "identifier")],
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="mozilla/%s" % OBJDIR),

    s(ShellCommand, name="chmod package",
                    command=["chmod", "666",
                             WithProperties(''.join(["mozilla/%s/dist/" \
                                         % OBJDIR,
                                         "%s",
                                         "-%s-linux.tar.bz2" % PKG_BASENAME]),
                                         "identifier")],

                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),

    s(MozillaCreateUploadDirectory,
                    scpString=SCP_STRING,
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),

    s(MozillaUploadTryBuild,
                    slavedir="mozilla/%s/dist" % OBJDIR,
                    baseFilename="%s-linux.tar.bz2" % PKG_BASENAME,
                    scpString=SCP_STRING,
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),
])
for master,warn in TALOS_TRY_MASTERS:
    try_cvs_linux_factory.addStep(
     SendChangeStep,
         master=master,
         warnOnFailure=warn,
         user='sendchange',
         branch='linux',
         files=[WithProperties(PACKAGE_URL + '/%(uploadpath)s')]
    )

try_cvs_macosx_factory = factory.BuildFactory([
    s(MozillaTryProcessing),
    s(ShellCommand, name="remove source and obj dirs",
                    command=["rm", "-rf", "mozilla"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    workdir="."),

    s(ShellCommand, name="dump env vars",
                    workdir=".",
                    command="env | sort"),

    s(MozillaClientMk, cvsroot=CVSROOT),
    
    s(MozillaDownloadMozconfig, mastersrc="mozconfig-macosx",
                                patchDir="patches/"),

    s(ShellCommand, name="source checkout",
                    description=["fetching source"],
                    descriptionDone=["source"],
                    command=["make", "-f", "client.mk", "checkout"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    workdir="mozilla",
                    env={'MOZ_CO_PROJECT': 'browser'}),

    s(MozillaPatchDownload, patchDir="patches/",
                            haltOnFailure=True,
                            flunkOnFailure=True,
                            workdir="mozilla"),
    s(MozillaCustomPatch, workdir="mozilla",
                          haltOnFailure=True,
                          flunkOnFailure=True),

    s(ShellCommand, name="mozconfig contents",
                    command=["cat",".mozconfig"],
                    workdir="mozilla"),

    s(ShellCommand, name="building",
                    description=["building"],
                    descriptionDone=["compile"],
                    command=["make", "-f", "client.mk", "build"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    timeout=3600,
                    workdir="mozilla"),

    s(ShellCommand, name="packaging",
                    description=["creating package"],
                    descriptionDone=["packaging"],
                    command=["make", "package",
                             WithProperties(''.join(["PKG_BASENAME=%s",
                                            "-%s-macosx" % PKG_BASENAME]),
                                            "identifier")],
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="mozilla/%s/ppc" % OBJDIR),

    s(ShellCommand, name="chmod package",
                    # this gets really ugly here, but it translates to this:
                    # mozilla/$OBJDIR/ppc/dist/$IDENTIFIER-$PKG_BASENAME-macosx.dmg
                    command=["chmod", "666",
                             WithProperties(''.join(["mozilla/%s/ppc/dist/" \
                                              % OBJDIR,
                                              "%s",
                                              "-%s-macosx.dmg" % PKG_BASENAME]),
                                              "identifier")],
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),

    s(MozillaCreateUploadDirectory,
                    scpString=SCP_STRING,
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),

    s(MozillaUploadTryBuild,
                    slavedir="mozilla/%s/ppc/dist" % OBJDIR,
                    baseFilename="%s-macosx.dmg" % PKG_BASENAME,
                    scpString=SCP_STRING,
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),
])
for master,warn in TALOS_TRY_MASTERS:
    try_cvs_macosx_factory.addStep(
     SendChangeStep,
         master=master,
         warnOnFailure=warn,
         user='sendchange',
         branch='macosx',
         files=[WithProperties(PACKAGE_URL + '/%(uploadpath)s')]
    )

try_cvs_win32_factory = factory.BuildFactory([
    s(MozillaTryProcessing),
    s(ShellCommand, name="pacify rmdir",
                    description="Pacify rmdir",
                    descriptionDone="Pacified rmdir",
                    command=["bash", "-c",
                             "if [ ! -d mozilla ]; then mkdir -v mozilla; fi"],
                    workdir="."),

    s(ShellCommand, name="remove source and obj dirs",
                    command=["rmdir", "/s", "/q", "mozilla"],
                    workdir=".",
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    timeout=3600, # 1 hour
                    env=WIN32_ENVIRONMENT),

    s(ShellCommand, name="dump env vars",
                    workdir=".",
                    command="set | sort",
                    env=WIN32_ENVIRONMENT),

    s(MozillaClientMk, cvsroot=CVSROOT),

    s(MozillaDownloadMozconfig, mastersrc="mozconfig-win32",
                                patchDir="patches/"),

    s(ShellCommand, name="source checkout",
                    description=["fetching source"],
                    descriptionDone=["source"],
                    command=["make", "-f", "client.mk", "checkout"],
                    workdir="mozilla",
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    env=WIN32_ENVIRONMENT),

    s(MozillaPatchDownload, patchDir="patches/",
                            haltOnFailure=True,
                            flunkOnFailure=True,
                            workdir="mozilla"),
    s(MozillaCustomPatch, workdir="mozilla",
                          haltOnFailure=True,
                          flunkOnFailure=True),

    s(ShellCommand, name="mozconfig contents",
                    command=["cat",".mozconfig"],
                    workdir="mozilla",
                    env=WIN32_ENVIRONMENT),

    s(ShellCommand, name="building",
                    description=["building"],
                    descriptionDone=["compile"],
                    command=["make", "-f", "client.mk", "build"],
                    workdir="mozilla",
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    timeout=3600,
                    env=WIN32_ENVIRONMENT),

    s(ShellCommand, name="packaging (zip)",
                    description=["creating package"],
                    descriptionDone=["packaging"],
                    command=["make", "package",
                             WithProperties(''.join(["PKG_BASENAME=%s",
                                            "-%s-win32" % PKG_BASENAME]),
                                            "identifier")],
                    workdir="mozilla/%s" % OBJDIR,
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    env=WIN32_ENVIRONMENT),

    s(ShellCommand, name="packaging (exe)",
                    description=["creating package"],
                    descriptionDone=["packaging"],
                    command=["make", "installer",
                             WithProperties(''.join(["PKG_BASENAME=%s",
                                            "-%s-win32" % PKG_BASENAME]),
                                            "identifier")],
                    workdir="mozilla/%s" % OBJDIR,
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    env=WIN32_ENVIRONMENT),

    s(ShellCommand, name="chmod package (exe)",
                    command=["chmod", "666",
                        WithProperties(''.join(["mozilla/%s/dist/install/sea/" \
                            % OBJDIR,
                            "%s", "-%s-win32.installer.exe" % PKG_BASENAME]),
                            "identifier")],
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),

    s(MozillaUploadTryBuild,
                slavedir="mozilla/%s/dist/install/sea" % OBJDIR,
                # the identifier gets prepended to this in the BuildStep
                baseFilename="%s-win32.installer.exe" % PKG_BASENAME,
                scpString=SCP_STRING,
                haltOnFailure=False,
                flunkOnFailure=False,
                workdir="."),

    s(MozillaCreateUploadDirectory,
                    scpString=SCP_STRING,
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),

    s(ShellCommand, name="chmod package (zip)",
                    command=["chmod", "666",
                        WithProperties(''.join(["mozilla/%s/dist/" \
                            % OBJDIR,
                            "%s", "-%s-win32.zip" % PKG_BASENAME]),
                            "identifier")],
                    haltOnFailure=False,
                    flunkOnFailure=False,
                    workdir="."),

    s(MozillaUploadTryBuild,
                slavedir="mozilla/%s/dist" % OBJDIR,
                # the identifier gets prepended to this in the BuildStep
                baseFilename="%s-win32.zip" % PKG_BASENAME,
                scpString=SCP_STRING,
                haltOnFailure=False,
                flunkOnFailure=False,
                workdir="."),

    s(ShellCommand,
                name="build symbols",
                command=["make", "-C", OBJDIR, "buildsymbols"],
                haltOnFailure=True,
                flunkOnFailure=False,
                env=WIN32_ENVIRONMENT,
                workdir="mozilla"),

     s(ShellCommand,
                name="upload symbols",
                command=["make", "-C", OBJDIR, "uploadsymbols"],
                haltOnFailure=True,
                flunkOnFailure=False,
                env=WIN32_ENVIRONMENT,
                workdir="mozilla"),
])
for master,warn in TALOS_TRY_MASTERS:
    try_cvs_win32_factory.addStep(
     SendChangeStep,
         master=master,
         warnOnFailure=warn,
         user='sendchange',
         branch='win32',
         files=[WithProperties(PACKAGE_URL + '/%(uploadpath)s')]
    )

firefox_hg_linux_unittest_factory = factory.BuildFactory([
    s(MozillaTryProcessing),
    s(ShellCommand, name="remove source and obj dirs",
                    command=["rm", "-rf", "mozilla/"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    workdir="."),

    s(ShellCommand, name='rm buildtools',
                    command=['rm', '-rf', 'tools'],
                    description=['clobber', 'build tools'],
                    workdir='.'),

    s(ShellCommand, name='clone buildtools',
                    command=['hg', 'clone', BUILD_TOOLS_REPO],
                    description=['clone', 'build tools'],
                    workdir='.'),

    s(ShellCommand, name="dump env vars",
                    workdir=".",
                    command="env | sort"),

    s(MozillaTryServerHgClone, workdir="mozilla"),

    s(MozillaDownloadMozconfig, mastersrc="mozconfig-linux-unittest",
                                patchDir="patches/"),

    s(MozillaPatchDownload, patchDir="patches/",
                            haltOnFailure=False,
                            flunkOnFailure=True,
                            workdir="mozilla",
                            isOptional=True),

    s(MozillaCustomPatch, workdir="mozilla",
                          haltOnFailure=True,
                          flunkOnFailure=True,
                          isOptional=True),

    s(ShellCommand, name="mozconfig contents",
                    command=["cat", ".mozconfig"],
                    workdir="mozilla"),

    s(ShellCommand, name="building",
                    description=["building"],
                    descriptionDone=["compile"],
                    command=["make", "-f", "client.mk", "build"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    timeout=3600,
                    workdir="mozilla"),

    s(ShellCommand, name="make buildsymbols",
                    command=["make", "buildsymbols"],
                    haltOnFailure=True,
                    workdir="mozilla/%s" % OBJDIR,
    ),

    s(SetProperty, name="get toolsdir",
                   command=['bash', '-c', 'pwd'],
                   property='toolsdir',
                   workdir='tools',
    ),

])

linuxUnittestEnv = MozillaEnvironments['linux-unittest'].copy()
linuxUnittestEnv['MINIDUMP_STACKWALK'] = \
    WithProperties('%(toolsdir:-)s/breakpad/linux/minidump_stackwalk')

firefox_hg_linux_unittest_factory.addStep(
    unittest.MozillaCheck,
      test_name="check",
      warnOnWarnings=True,
      workdir="mozilla/%s" % OBJDIR,
      env=linuxUnittestEnv,
      timeout=5*60, # 5 minutes.
    ),

firefox_hg_linux_unittest_factory.addStep(
    unittest.MozillaCheck,
      test_name="xpcshell-tests",
      warnOnWarnings=True,
      workdir="mozilla/%s" % OBJDIR,
      env=linuxUnittestEnv,
      timeout=5*60, # 5 minutes.
    ),

for test_name in ('reftest', 'crashtest'): 
    firefox_hg_linux_unittest_factory.addStep(
        unittest.MozillaReftest, 
             test_name=test_name, 
             warnOnWarnings=True,
             workdir="mozilla/%s" % OBJDIR,
             env=linuxUnittestEnv,
             timeout=60*5
    )

for test_name in ('mochitest-plain', 'mochitest-chrome', 'mochitest-browser-chrome', 'mochitest-a11y'): 
    firefox_hg_linux_unittest_factory.addStep(
        unittest.MozillaMochitest,
                test_name=test_name,
                warnOnWarnings=True,
                env=linuxUnittestEnv,
                workdir="mozilla/%s" % OBJDIR,
                timeout=60*5
    )


firefox_hg_macosx_unittest_factory = factory.BuildFactory([
    s(MozillaTryProcessing),
    s(ShellCommand, name="remove source and obj dirs",
                    command=["rm", "-rf", "mozilla/"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    workdir="."),

    s(ShellCommand, name='rm buildtools',
                    command=['rm', '-rf', 'tools'],
                    description=['clobber', 'build tools'],
                    workdir='.'),

    s(ShellCommand, name='clone buildtools',
                    command=['hg', 'clone', BUILD_TOOLS_REPO],
                    description=['clone', 'build tools'],
                    workdir='.'),

    s(ShellCommand, name="dump env vars",
                    workdir=".",
                    command="env | sort"),

    s(MozillaTryServerHgClone, workdir="mozilla/"),

    s(MozillaDownloadMozconfig, mastersrc="mozconfig-macosx-unittest",
                                patchDir="patches/"),

    s(MozillaPatchDownload, patchDir="patches/",
                            haltOnFailure=True,
                            flunkOnFailure=True,
                            workdir="mozilla",
                            isOptional=True),

    s(MozillaCustomPatch, workdir="mozilla",
                          haltOnFailure=True,
                          flunkOnFailure=True,
                          isOptional=True),

    s(ShellCommand, name="mozconfig contents",
                    command=["cat", ".mozconfig"],
                    workdir="mozilla"),

    s(ShellCommand, name="building",
                    description=["building"],
                    descriptionDone=["compile"],
                    command=["make", "-f", "client.mk", "build"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    timeout=3600,
                    workdir="mozilla"),

    s(ShellCommand, name="make buildsymbols",
                    command=["make", "buildsymbols"],
                    haltOnFailure=True,
                    workdir="mozilla/%s" % OBJDIR,
    ),

    s(SetProperty, name="get toolsdir",
                   command=['bash', '-c', 'pwd'],
                   property='toolsdir',
                   workdir='tools',
    ),

])

macosxUnittestEnv = MozillaEnvironments['macosx-unittest'].copy()
macosxUnittestEnv['MINIDUMP_STACKWALK'] = \
    WithProperties('%(toolsdir:-)s/breakpad/osx/minidump_stackwalk')

firefox_hg_macosx_unittest_factory.addStep(
    unittest.MozillaCheck,
      test_name="check",
      warnOnWarnings=True,
      workdir="mozilla/%s" % OBJDIR,
      env=macosxUnittestEnv,
      timeout=5*60, # 5 minutes.
    ),

firefox_hg_macosx_unittest_factory.addStep(
    unittest.MozillaCheck,
      test_name="xpcshell-tests",
      warnOnWarnings=True,
      workdir="mozilla/%s" % OBJDIR,
      env=macosxUnittestEnv,
      timeout=5*60, # 5 minutes.
    ),

for test_name in ('reftest', 'crashtest'): 
    firefox_hg_macosx_unittest_factory.addStep(
        unittest.MozillaReftest, 
           test_name=test_name, 
           warnOnWarnings=True,
           workdir="mozilla/%s" % OBJDIR,
           env=macosxUnittestEnv,
           timeout=60*5,
    )

for test_name in ('mochitest-plain', 'mochitest-chrome', 'mochitest-browser-chrome'): 
    firefox_hg_macosx_unittest_factory.addStep(
        unittest.MozillaMochitest,
            test_name=test_name,
            warnOnWarnings=True,
            workdir="mozilla/%s" % OBJDIR,
            env=macosxUnittestEnv,
            timeout=60*5,
    )

firefox_hg_win32_unittest_factory = factory.BuildFactory([
    s(MozillaTryProcessing),
    s(TinderboxShellCommand, name="kill sh",
            description='kill sh',
            descriptionDone="killed sh",
            haltOnFailure=False,
            flunkOnFailure=False,
            command="pskill -t sh.exe",
            workdir="D:\\Utilities"),

    s(TinderboxShellCommand, name="kill make",
            description='kill make',
            descriptionDone="killed make",
            haltOnFailure=False,
            flunkOnFailure=False,
            command="pskill -t make.exe",
            workdir="D:\\Utilities"),

    s(TinderboxShellCommand, name="kill firefox",
            description='kill firefox',
            descriptionDone="killed firefox",
            haltOnFailure=False,
            flunkOnFailure=False,
            command="pskill -t firefox.exe",
            workdir="D:\\Utilities"),

    s(ShellCommand, name="pacify rmdir",
                    description="Pacify rmdir",
                    descriptionDone="Pacified rmdir",
                    command=["bash", "-c",
                             "if [ ! -d mozilla ]; then mkdir -v mozilla; fi"],
                    workdir="."),

    s(ShellCommand, name="remove source and obj dirs",
                    command=["rmdir", "/s", "/q", "mozilla"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    workdir=".",
                    timeout=60*60, # 1 hour
                    env=MozillaEnvironments['win32-unittest']),

    s(ShellCommand, name='rm buildtools',
                    command=['rm', '-rf', 'tools'],
                    description=['clobber', 'build tools'],
                    workdir='.'),

    s(ShellCommand, name='clone buildtools',
                    command=['hg', 'clone', BUILD_TOOLS_REPO],
                    description=['clone', 'build tools'],
                    workdir='.'),

    s(ShellCommand, name="dump env vars",
                    workdir=".",
                    command="set | sort",
                    env=MozillaEnvironments['win32-unittest']),

    s(MozillaTryServerHgClone, workdir="mozilla/"),

    s(MozillaDownloadMozconfig, mastersrc="mozconfig-win32-unittest",
                                patchDir="patches/"),

    s(MozillaPatchDownload, patchDir="patches/",
                            haltOnFailure=True,
                            flunkOnFailure=True,
                            workdir="mozilla",
                            isOptional=True),

    s(MozillaCustomPatch, workdir="mozilla",
                          haltOnFailure=True,
                          flunkOnFailure=True,
                          isOptional=True),

    s(ShellCommand, name="mozconfig contents",
                    command=["cat", ".mozconfig"],
                    workdir="mozilla",
                    env=MozillaEnvironments['win32-unittest']),

    s(ShellCommand, name="building",
                    description=["building"],
                    descriptionDone=["compile"],
                    command=["make", "-f", "client.mk", "build"],
                    haltOnFailure=True,
                    flunkOnFailure=True,
                    workdir="mozilla",
                    timeout=3600,
                    env=MozillaEnvironments['win32-unittest']),

    s(ShellCommand, name="make buildsymbols",
                    command=["make", "buildsymbols"],
                    haltOnFailure=True,
                    workdir="mozilla/%s" % OBJDIR,
    ),

    s(SetProperty, name="get toolsdir",
                   command=['bash', '-c', 'pwd'],
                   property='toolsdir',
                   workdir='tools',
    ),

])

win32UnittestEnv = MozillaEnvironments['win32-unittest'].copy()
win32UnittestEnv['MINIDUMP_STACKWALK'] = \
    WithProperties('%(toolsdir:-)s/breakpad/win32/minidump_stackwalk.exe')

firefox_hg_win32_unittest_factory.addStep(
    unittest.MozillaCheck,
      test_name="check",
      warnOnWarnings=True,
      workdir="mozilla/%s" % OBJDIR,
      env=win32UnittestEnv,
      timeout=5*60, # 5 minutes.
    ),

firefox_hg_win32_unittest_factory.addStep(
    unittest.MozillaCheck,
      test_name="xpcshell-tests",
      warnOnWarnings=True,
      workdir="mozilla/%s" % OBJDIR,
      env=win32UnittestEnv,
      timeout=5*60, # 5 minutes.
    ),

for test_name in ('reftest', 'crashtest'): 
    leakThreshold = None
    if test_name is 'crashtest':
        # Until bug 471647 is fixed
        leakThreshold = 484
    firefox_hg_win32_unittest_factory.addStep(
        unittest.MozillaReftest, 
            test_name=test_name, 
            leakThreshold=leakThreshold,
            warnOnWarnings=True,
            workdir="mozilla/%s" % OBJDIR,
            env=win32UnittestEnv,
            timeout=60*5
    )
         
for test_name in ('mochitest-plain', 'mochitest-chrome', 'mochitest-browser-chrome', 'mochitest-a11y'): 
    leakThreshold = None
    if test_name is 'mochitest-plain':
        # Until bug 471647 is fixed
        leakThreshold = 484
    firefox_hg_win32_unittest_factory.addStep(
        unittest.MozillaMochitest,
            test_name=test_name,
            leakThreshold=leakThreshold,
            warnOnWarnings=True,
            workdir="mozilla/%s" % OBJDIR,
            env=win32UnittestEnv,
            timeout=60*5
    )
