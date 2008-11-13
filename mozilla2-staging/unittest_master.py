# -*- python -*-
# ex: set syntax=python:

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla-specific Buildbot steps.
#
# The Initial Developer of the Original Code is
# Mozilla Corporation.
# Portions created by the Initial Developer are Copyright (C) 2007
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Rob Campbell <rcampbell@mozilla.com>
#   Chris Cooper <ccooper@mozilla.com>
#   Ben Hearsum <bhearsum@mozilla.com>
# ***** END LICENSE BLOCK *****

import os.path
from buildbot.process import factory
from buildbot.scheduler import Scheduler, Periodic
from buildbot.status import tinderbox
from buildbot.steps.source import Mercurial
from buildbot.steps.shell import Compile, ShellCommand, WithProperties

import buildbotcustom.env
import buildbotcustom.misc
import buildbotcustom.unittest.steps
import buildbotcustom.steps.misc
reload(buildbotcustom.env)
reload(buildbotcustom.misc)
reload(buildbotcustom.unittest.steps)
reload(buildbotcustom.steps.misc)

from buildbotcustom.env import *
from buildbotcustom.misc import isHgPollerTriggered
from buildbotcustom.unittest.steps import *
from buildbotcustom.steps.misc import CreateDir, TinderboxShellCommand

import unittest_config
reload(unittest_config)
from unittest_config import *

import config as nightly_config
reload(nightly_config)

status = []
schedulers = []
change_source = []
builders = []

status.append(tinderbox.TinderboxMailNotifier(
    fromaddr="lblakk@mozilla.com",
    tree="UnitTest",
    extraRecipients=["tinderbox-daemon@tinderbox.mozilla.org"],
    relayhost="localhost",
    logCompression="bzip2",
    errorparser="unittest"
))

####### SCHEDULERS

## configure the Schedulers

schedulers = []
schedulers.append(Scheduler(
    name="unittest mozilla-central",
    branch="mozilla-central",
    treeStableTimer=5*60,
    builderNames=['Linux mozilla-central unit test',
                  'OS X 10.5.2 mozilla-central unit test',
                  'WINNT 5.2 mozilla-central unit test'],
    fileIsImportant=lambda c: isHgPollerTriggered(c, nightly_config.HGURL)
))

schedulers.append(Periodic(
    name="unittest mozilla-central-periodic",
    branch="mozilla-central",
    periodicBuildTimer=60*60*3, # three hours
    builderNames=['Linux mozilla-central unit test',
                  'OS X 10.5.2 mozilla-central unit test',
                  'WINNT 5.2 mozilla-central unit test'],
))

schedulers.append(Scheduler(
    name="unittest tracemonkey",
    branch="tracemonkey",
    treeStableTimer=5*60,
    builderNames=['Linux tracemonkey unit test',
                  'OS X 10.5.2 tracemonkey unit test',
                  'WINNT 5.2 tracemonkey unit test'],
))

####### BUILDERS

# the 'builders' list defines the Builders. Each one is configured with a
# dictionary, using the following keys:
#  name (required): the name used to describe this bilder
#  slavename (required): which slave to use, must appear in c['bots']
#  builddir (required): which subdirectory to run the builder in
#  factory (required): a BuildFactory to define how the build is run
#  periodicBuildTime (optional): if set, force a build every N seconds


# the first BuildStep is typically responsible for obtaining a copy of the
# change_source. There are source-obtaining Steps in buildbot/process/step.py for
# CVS, SVN, and others.

def addPrintChangesetStep(factory, env={}):
    changesetLink = '<a href=http://hg.mozilla.org/mozilla-central/index.cgi/rev/%(got_revision)s title="Built from revision %(got_revision)s">rev:%(got_revision)s</a>'
    factory.addStep(ShellCommand(
        command=['echo', 'TinderboxPrint:', WithProperties(changesetLink)],
        env=env
    ))

def addPrintTraceMonkeyChangesetStep(factory, env={}):
    changesetLink = '<a href=http://hg.mozilla.org/tracemonkey/index.cgi/rev/%(got_revision)s title="Built from revision %(got_revision)s">rev:%(got_revision)s</a>'
    factory.addStep(ShellCommand(
        command=['echo', 'TinderboxPrint:', WithProperties(changesetLink)],
        env=env
    ))

##
## Linux UnitTest
##

moz2_linux_unittest_factory = factory.BuildFactory()
moz2_linux_unittest_factory.addStep(Mercurial, mode='update',
    baseURL='http://hg.mozilla.org/',
    defaultBranch='mozilla-central')
addPrintChangesetStep(moz2_linux_unittest_factory)
moz2_linux_unittest_factory.addStep(ShellCommand,
    name="buildbot configs",
    command=['hg', 'clone', nightly_config.CONFIG_REPO_URL, 'mozconfigs'],
    flunkOnFailure=False,
    workdir='.'
)
moz2_linux_unittest_factory.addStep(ShellCommand, name="copy mozconfig",
    command=['cp',
             'mozconfigs/%s/linux-unittest/mozconfig' % \
               nightly_config.CONFIG_SUBDIR,
             'build/.mozconfig'],
    workdir='.')
moz2_linux_unittest_factory.addStep(ShellCommand, name='mozconfig contents',
    command=['cat', '.mozconfig'])
moz2_linux_unittest_factory.addStep(Compile,
    warningPattern='',
    command=['make', '-f', 'client.mk', 'build'])
moz2_linux_unittest_factory.addStep(MozillaCheck, 
    warnOnWarnings=True,
    timeout=60*5,
    workdir="build/objdir")
moz2_linux_unittest_factory.addStep(CreateProfile,
        warnOnWarnings=True,
        workdir="build",
        command = r'python testing/tools/profiles/createTestingProfile.py --clobber --binary objdir/dist/bin/firefox',
        env=MozillaEnvironments['linux-centos-unittest'],
        clobber=True)
moz2_linux_unittest_factory.addStep(MozillaUnixReftest, warnOnWarnings=True,
    workdir="build/layout/reftests",
    timeout=60*5,
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_unittest_factory.addStep(MozillaUnixCrashtest, warnOnWarnings=True,
    workdir="build/testing/crashtest",
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_unittest_factory.addStep(MozillaMochitest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    timeout=60*5,
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_unittest_factory.addStep(MozillaMochichrome, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_unittest_factory.addStep(MozillaBrowserChromeTest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_unittest_factory.addStep(MozillaA11YTest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    env=MozillaEnvironments['linux-centos-unittest'])

mozilla2_firefox_unix_test_builder = {
    'name': 'Linux mozilla-central unit test',
    'slavenames': ['moz2-linux-slave1', 'moz2-linux-slave02',
                   'moz2-linux-slave03', 'moz2-linux-slave04',
                   'moz2-linux-slave05', 'moz2-linux-slave06',
                   'moz2-linux-slave07', 'moz2-linux-slave08',
                   'moz2-linux-slave09', 'moz2-linux-slave10',
                   'moz2-linux-slave11', 'moz2-linux-slave12',
                   'moz2-linux-slave13', 'moz2-linux-slave14',
                   'moz2-linux-slave15', 'moz2-linux-slave16',
                   'moz2-linux-slave17', 'moz2-linux-slave18'],
    'builddir': 'mozilla-central-linux-unittest',
    'factory': moz2_linux_unittest_factory,
    'category': 'mozilla-central',
}

builders.append(mozilla2_firefox_unix_test_builder)

##
## Linux TraceMonkey Unittest
##

moz2_linux_tracemonkey_unittest_factory = factory.BuildFactory()
moz2_linux_tracemonkey_unittest_factory.addStep(Mercurial, mode='update',
    baseURL='http://hg.mozilla.org/',
    defaultBranch='tracemonkey')
addPrintTraceMonkeyChangesetStep(moz2_linux_tracemonkey_unittest_factory)
moz2_linux_tracemonkey_unittest_factory.addStep(ShellCommand,
    name="buildbot configs",
    command=['hg', 'clone', nightly_config.CONFIG_REPO_URL, 'mozconfigs'],
    workdir='.'
)
moz2_linux_tracemonkey_unittest_factory.addStep(ShellCommand, name="copy mozconfig",
    command=['cp',
             'mozconfigs/%s/linux-unittest/mozconfig' % \
               nightly_config.CONFIG_SUBDIR,
             'build/.mozconfig'],
    workdir='.')
moz2_linux_tracemonkey_unittest_factory.addStep(ShellCommand, name='mozconfig contents',
    command=['cat', '.mozconfig'])
moz2_linux_tracemonkey_unittest_factory.addStep(Compile,
    warningPattern='',
    command=['make', '-f', 'client.mk', 'build'])
moz2_linux_tracemonkey_unittest_factory.addStep(MozillaCheck, 
    warnOnWarnings=True,
    timeout=60*5,
    workdir="build/objdir")
moz2_linux_tracemonkey_unittest_factory.addStep(CreateProfile,
        warnOnWarnings=True,
        workdir="build",
        command = r'python testing/tools/profiles/createTestingProfile.py --clobber --binary objdir/dist/bin/firefox',
        env=MozillaEnvironments['linux-centos-unittest'],
        clobber=True)
moz2_linux_tracemonkey_unittest_factory.addStep(MozillaUnixReftest, warnOnWarnings=True,
    workdir="build/layout/reftests",
    timeout=60*5,
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_tracemonkey_unittest_factory.addStep(MozillaUnixCrashtest, warnOnWarnings=True,
    workdir="build/testing/crashtest",
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_tracemonkey_unittest_factory.addStep(MozillaMochitest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    timeout=60*5,
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_tracemonkey_unittest_factory.addStep(MozillaMochichrome, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_tracemonkey_unittest_factory.addStep(MozillaBrowserChromeTest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    env=MozillaEnvironments['linux-centos-unittest'])
moz2_linux_tracemonkey_unittest_factory.addStep(MozillaA11YTest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    env=MozillaEnvironments['linux-centos-unittest'])

mozilla2_firefox_unix_test_builder2 = {
    'name': 'Linux tracemonkey unit test',
    'slavenames': ['moz2-linux-slave1', 'moz2-linux-slave02',
                   'moz2-linux-slave03', 'moz2-linux-slave04',
                   'moz2-linux-slave05', 'moz2-linux-slave06',
                   'moz2-linux-slave07', 'moz2-linux-slave08',
                   'moz2-linux-slave09', 'moz2-linux-slave10',
                   'moz2-linux-slave11', 'moz2-linux-slave12',
                   'moz2-linux-slave13', 'moz2-linux-slave14',
                   'moz2-linux-slave15', 'moz2-linux-slave16',
                   'moz2-linux-slave17', 'moz2-linux-slave18'],
    'builddir': 'tracemonkey-linux-unittest',
    'factory': moz2_linux_unittest_factory,
    'category': 'tracemonkey',
}

builders.append(mozilla2_firefox_unix_test_builder2)

##
## Mac UnitTest
##

moz2_darwin_unittest_factory = factory.BuildFactory()
moz2_darwin_unittest_factory.addStep(Mercurial, mode='update',
    baseURL='http://hg.mozilla.org/',
    defaultBranch='mozilla-central')
addPrintChangesetStep(moz2_darwin_unittest_factory)
moz2_darwin_unittest_factory.addStep(ShellCommand,
    name="buildbot configs",
    command=['hg', 'clone', nightly_config.CONFIG_REPO_URL, 'mozconfigs'],
    flunkOnFailure=False,
    workdir='.'
)
moz2_darwin_unittest_factory.addStep(ShellCommand, name="copy mozconfig",
    command=['cp',
             'mozconfigs/%s/macosx-unittest/mozconfig' % \
               nightly_config.CONFIG_SUBDIR,
             'build/.mozconfig'],
    workdir='.')
moz2_darwin_unittest_factory.addStep(ShellCommand, name='mozconfig contents',
    command=['cat', '.mozconfig'])
moz2_darwin_unittest_factory.addStep(Compile,
    warningPattern='',
    command=['make', '-f', 'client.mk', 'build'])
moz2_darwin_unittest_factory.addStep(MozillaCheck, 
    warnOnWarnings=True,
    timeout=60*5,
    workdir="build/objdir")
moz2_darwin_unittest_factory.addStep(CreateProfile,
    warnOnWarnings=True,
    workdir="build",
    command = r'python testing/tools/profiles/createTestingProfile.py --clobber --binary objdir/dist/bin/firefox',
    env=MozillaEnvironments['mac-osx-unittest'],
    clobber=True)
moz2_darwin_unittest_factory.addStep(MozillaOSXReftest, warnOnWarnings=True,
    workdir="build/layout/reftests",
    timeout=60*5,
    env=MozillaEnvironments['mac-osx-unittest'])
moz2_darwin_unittest_factory.addStep(MozillaOSXCrashtest, warnOnWarnings=True,
    workdir="build/testing/crashtest",
    env=MozillaEnvironments['mac-osx-unittest'])
moz2_darwin_unittest_factory.addStep(MozillaOSXMochitest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    timeout=60*5,
    env=MozillaEnvironments['mac-osx-unittest'])
moz2_darwin_unittest_factory.addStep(MozillaOSXMochichrome, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    leakThreshold="8",
    env=MozillaEnvironments['mac-osx-unittest'])
moz2_darwin_unittest_factory.addStep(MozillaOSXBrowserChromeTest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    env=MozillaEnvironments['mac-osx-unittest'])

mozilla2_firefox_osx_test_builder = {
    'name': 'OS X 10.5.2 mozilla-central unit test',
    'slavenames': ['bm-xserve16', 'bm-xserve17', 'bm-xserve18', 'bm-xserve19',
                   'bm-xserve22',
                   'moz2-darwin9-slave01', 'moz2-darwin9-slave02',
                   'moz2-darwin9-slave03', 'moz2-darwin9-slave04'],
    'builddir': 'mozilla-central-macosx-unittest',
    'factory': moz2_darwin_unittest_factory,
    'category': 'mozilla-central',
}

builders.append(mozilla2_firefox_osx_test_builder)

##
## Mac TraceMonkey UnitTest
##

moz2_darwin_tracemonkey_unittest_factory = factory.BuildFactory()
moz2_darwin_tracemonkey_unittest_factory.addStep(Mercurial, mode='update',
    baseURL='http://hg.mozilla.org/',
    defaultBranch='tracemonkey')
addPrintTraceMonkeyChangesetStep(moz2_darwin_unittest_factory)
moz2_darwin_tracemonkey_unittest_factory.addStep(ShellCommand,
    name="buildbot configs",
    command=['hg', 'clone', nightly_config.CONFIG_REPO_URL, 'mozconfigs'],
    workdir='.'
)
moz2_darwin_tracemonkey_unittest_factory.addStep(ShellCommand, name="copy mozconfig",
    command=['cp',
             'mozconfigs/%s/macosx-unittest/mozconfig' % \
               nightly_config.CONFIG_SUBDIR,
             'build/.mozconfig'],
    workdir='.')
moz2_darwin_tracemonkey_unittest_factory.addStep(ShellCommand, name='mozconfig contents',
    command=['cat', '.mozconfig'])
moz2_darwin_tracemonkey_unittest_factory.addStep(Compile,
    warningPattern='',
    command=['make', '-f', 'client.mk', 'build'])
moz2_darwin_tracemonkey_unittest_factory.addStep(MozillaCheck, 
    warnOnWarnings=True,
    timeout=60*5,
    workdir="build/objdir")
moz2_darwin_tracemonkey_unittest_factory.addStep(CreateProfile,
    warnOnWarnings=True,
    workdir="build",
    command = r'python testing/tools/profiles/createTestingProfile.py --clobber --binary objdir/dist/bin/firefox',
    env=MozillaEnvironments['mac-osx-unittest'],
    clobber=True)
moz2_darwin_tracemonkey_unittest_factory.addStep(MozillaOSXReftest, warnOnWarnings=True,
    workdir="build/layout/reftests",
    timeout=60*5,
    env=MozillaEnvironments['mac-osx-unittest'])
moz2_darwin_tracemonkey_unittest_factory.addStep(MozillaOSXCrashtest, warnOnWarnings=True,
    workdir="build/testing/crashtest",
    env=MozillaEnvironments['mac-osx-unittest'])
moz2_darwin_tracemonkey_unittest_factory.addStep(MozillaOSXMochitest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    timeout=60*5,
    env=MozillaEnvironments['mac-osx-unittest'])
moz2_darwin_tracemonkey_unittest_factory.addStep(MozillaOSXMochichrome, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    leakThreshold="8",
    env=MozillaEnvironments['mac-osx-unittest'])
moz2_darwin_tracemonkey_unittest_factory.addStep(MozillaOSXBrowserChromeTest, warnOnWarnings=True,
    workdir="build/objdir/_tests/testing/mochitest",
    env=MozillaEnvironments['mac-osx-unittest'])

mozilla2_firefox_osx_test_builder2 = {
    'name': 'OS X 10.5.2 tracemonkey unit test',
    'slavenames': ['bm-xserve16', 'bm-xserve17', 'bm-xserve18', 'bm-xserve19',
                   'bm-xserve22',
                   'moz2-darwin9-slave01', 'moz2-darwin9-slave02',
                   'moz2-darwin9-slave03', 'moz2-darwin9-slave04'],
    'builddir': 'tracemonkey-macosx-unittest',
    'factory': moz2_darwin_unittest_factory,
    'category': 'tracemonkey',
}

builders.append(mozilla2_firefox_osx_test_builder2)

##
## Win2k3 UnitTest
##

moz2_win32_unittest_factory = factory.BuildFactory()

moz2_win32_unittest_factory.addStep(TinderboxShellCommand, name="kill sh",
    description='kill sh',
    descriptionDone="killed sh",
    command="pskill -t sh.exe",
    workdir="D:\\Utilities")
moz2_win32_unittest_factory.addStep(TinderboxShellCommand, name="kill make",
    description='kill make',
    descriptionDone="killed make",
    command="pskill -t make.exe",
    workdir="D:\\Utilities")
moz2_win32_unittest_factory.addStep(TinderboxShellCommand, name="kill firefox",
    description='kill firefox',
    descriptionDone="killed firefox",
    command="pskill -t firefox.exe",
    workdir="D:\\Utilities")
moz2_win32_unittest_factory.addStep(Mercurial, mode='update',
    baseURL='http://hg.mozilla.org/',
    defaultBranch='mozilla-central')
addPrintChangesetStep(moz2_win32_unittest_factory,
                      MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_unittest_factory.addStep(ShellCommand,
    name="buildbot configs",
    command=['hg', 'clone', nightly_config.CONFIG_REPO_URL, 'mozconfigs'],
    flunkOnFailure=False,
    workdir='.'
)
moz2_win32_unittest_factory.addStep(ShellCommand, name="copy mozconfig",
    command=['cp',
             'mozconfigs/%s/win32-unittest/mozconfig' % \
               nightly_config.CONFIG_SUBDIR,
             'build/.mozconfig'],
    workdir='.')
moz2_win32_unittest_factory.addStep(ShellCommand, name="mozconfig contents",
    command=["type", ".mozconfig"],
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_unittest_factory.addStep(Compile, 
    command=["make", "-f", "client.mk", "build"],
    timeout=60*20,
    warningPattern='', 
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_unittest_factory.addStep(MozillaCheck, warnOnWarnings=True, 
    workdir="build\\objdir",
    timeout=60*5,
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_unittest_factory.addStep(CreateProfileWin,
    warnOnWarnings=True,
    workdir="build",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'],
    command = r'python testing\tools\profiles\createTestingProfile.py --clobber --binary objdir\dist\bin\firefox.exe',
    clobber=True)
moz2_win32_unittest_factory.addStep(MozillaWin32Reftest, warnOnWarnings=True,
    workdir="build\\layout\\reftests",
    timeout=60*5,
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_unittest_factory.addStep(MozillaWin32Crashtest, warnOnWarnings=True,
    workdir="build\\testing\\crashtest",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_unittest_factory.addStep(MozillaWin32Mochitest, warnOnWarnings=True,
    workdir="build\\objdir\\_tests\\testing\\mochitest",
    timeout=60*5,
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
# Can use the regular build step here. Perl likes the PATHs that way anyway.
moz2_win32_unittest_factory.addStep(MozillaWin32Mochichrome, warnOnWarnings=True,
    workdir="build\\objdir\\_tests\\testing\\mochitest",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_unittest_factory.addStep(MozillaWin32BrowserChromeTest, warnOnWarnings=True,
    workdir="build\\objdir\\_tests\\testing\\mochitest",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_unittest_factory.addStep(MozillaWin32A11YTest, warnOnWarnings=True,
    workdir="build\\objdir\\_tests\\testing\\mochitest",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])

firefox_trunk_win2k3_builder = {
    'name': "WINNT 5.2 mozilla-central unit test",
    'slavenames': ['moz2-win32-slave1', 'moz2-win32-slave02',
                   'moz2-win32-slave03', 'moz2-win32-slave04',
                   'moz2-win32-slave05', 'moz2-win32-slave06',
                   'moz2-win32-slave07', 'moz2-win32-slave08',
                   'moz2-win32-slave09', 'moz2-win32-slave10',
                   'moz2-win32-slave11', 'moz2-win32-slave12',
                   'moz2-win32-slave13', 'moz2-win32-slave14',
                   'moz2-win32-slave15', 'moz2-win32-slave16',
                   'moz2-win32-slave17', 'moz2-win32-slave18'],
    'builddir': "mozilla-central-win32-unittest",
    'factory': moz2_win32_unittest_factory,
    'category': 'mozilla-central',
}

builders.append(firefox_trunk_win2k3_builder)

##
## Win2k3 TraceMonkey UnitTest
##

moz2_win32_tracemonkey_unittest_factory = factory.BuildFactory()

moz2_win32_tracemonkey_unittest_factory.addStep(TinderboxShellCommand, name="kill sh",
    description='kill sh',
    descriptionDone="killed sh",
    command="pskill -t sh.exe",
    workdir="D:\\Utilities")
moz2_win32_tracemonkey_unittest_factory.addStep(TinderboxShellCommand, name="kill make",
    description='kill make',
    descriptionDone="killed make",
    command="pskill -t make.exe",
    workdir="D:\\Utilities")
moz2_win32_tracemonkey_unittest_factory.addStep(TinderboxShellCommand, name="kill firefox",
    description='kill firefox',
    descriptionDone="killed firefox",
    command="pskill -t firefox.exe",
    workdir="D:\\Utilities")
moz2_win32_tracemonkey_unittest_factory.addStep(Mercurial, mode='update',
    baseURL='http://hg.mozilla.org/',
    defaultBranch='tracemonkey')
addPrintTraceMonkeyChangesetStep(moz2_win32_unittest_factory,
                      MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_tracemonkey_unittest_factory.addStep(ShellCommand,
    name="buildbot configs",
    command=['hg', 'clone', nightly_config.CONFIG_REPO_URL, 'mozconfigs'],
    workdir='.'
)
moz2_win32_tracemonkey_unittest_factory.addStep(ShellCommand, name="copy mozconfig",
    command=['cp',
             'mozconfigs/%s/win32-unittest/mozconfig' % \
               nightly_config.CONFIG_SUBDIR,
             'build/.mozconfig'],
    workdir='.')
moz2_win32_tracemonkey_unittest_factory.addStep(ShellCommand, name="mozconfig contents",
    command=["type", ".mozconfig"],
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_tracemonkey_unittest_factory.addStep(Compile, 
    command=["make", "-f", "client.mk", "build"],
    timeout=60*20,
    warningPattern='', 
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_tracemonkey_unittest_factory.addStep(MozillaCheck, warnOnWarnings=True, 
    workdir="build\\objdir",
    timeout=60*5,
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_tracemonkey_unittest_factory.addStep(CreateProfileWin,
    warnOnWarnings=True,
    workdir="build",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'],
    command = r'python testing\tools\profiles\createTestingProfile.py --clobber --binary objdir\dist\bin\firefox.exe',
    clobber=True)
moz2_win32_tracemonkey_unittest_factory.addStep(MozillaWin32Reftest, warnOnWarnings=True,
    workdir="build\\layout\\reftests",
    timeout=60*5,
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_tracemonkey_unittest_factory.addStep(MozillaWin32Crashtest, warnOnWarnings=True,
    workdir="build\\testing\\crashtest",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_tracemonkey_unittest_factory.addStep(MozillaWin32Mochitest, warnOnWarnings=True,
    workdir="build\\objdir\\_tests\\testing\\mochitest",
    timeout=60*5,
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
# Can use the regular build step here. Perl likes the PATHs that way anyway.
moz2_win32_tracemonkey_unittest_factory.addStep(MozillaWin32Mochichrome, warnOnWarnings=True,
    workdir="build\\objdir\\_tests\\testing\\mochitest",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_tracemonkey_unittest_factory.addStep(MozillaWin32BrowserChromeTest, warnOnWarnings=True,
    workdir="build\\objdir\\_tests\\testing\\mochitest",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])
moz2_win32_tracemonkey_unittest_factory.addStep(MozillaWin32A11YTest, warnOnWarnings=True,
    workdir="build\\objdir\\_tests\\testing\\mochitest",
    env=MozillaEnvironments['win32-vc8-mozbuild-unittest'])

firefox_trunk_win2k3_builder2 = {
    'name': "WINNT 5.2 tracemonkey unit test",
    'slavenames': ['moz2-win32-slave1', 'moz2-win32-slave02',
                   'moz2-win32-slave03', 'moz2-win32-slave04',
                   'moz2-win32-slave05', 'moz2-win32-slave06',
                   'moz2-win32-slave07', 'moz2-win32-slave08',
                   'moz2-win32-slave09', 'moz2-win32-slave10',
                   'moz2-win32-slave11', 'moz2-win32-slave12',
                   'moz2-win32-slave13', 'moz2-win32-slave14',
                   'moz2-win32-slave15', 'moz2-win32-slave16',
                   'moz2-win32-slave17', 'moz2-win32-slave18'],
    'builddir': "tracemonkey-win32-unittest",
    'factory': moz2_win32_unittest_factory,
    'category': 'tracemonkey',
}

builders.append(firefox_trunk_win2k3_builder2)
