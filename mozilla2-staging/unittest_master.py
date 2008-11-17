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
from buildbot.scheduler import Scheduler, Periodic
from buildbot.status import tinderbox

import buildbotcustom.misc
reload(buildbotcustom.misc)

from buildbotcustom.misc import isHgPollerTriggered
from buildbotcustom.process.factory import UnittestBuildFactory

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

##
## Linux UnitTest
##

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
    'factory': UnittestBuildFactory(
        platform='linux',
        config_repo_url = nightly_config.CONFIG_REPO_URL,
        config_dir = nightly_config.CONFIG_SUBDIR,
        branch = 'mozilla-central'
    ),
    'category': 'mozilla-central',
}

builders.append(mozilla2_firefox_unix_test_builder)

##
## Linux TraceMonkey Unittest
##

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
    'factory': UnittestBuildFactory(
        platform='linux',
        config_repo_url = nightly_config.CONFIG_REPO_URL,
        config_dir = nightly_config.CONFIG_SUBDIR,
        branch = 'tracemonkey'
    ),
    'category': 'tracemonkey',
}

builders.append(mozilla2_firefox_unix_test_builder2)

##
## Mac UnitTest
##

mozilla2_firefox_osx_test_builder = {
    'name': 'OS X 10.5.2 mozilla-central unit test',
    'slavenames': ['bm-xserve16', 'bm-xserve17', 'bm-xserve18', 'bm-xserve19',
                   'bm-xserve22',
                   'moz2-darwin9-slave01', 'moz2-darwin9-slave02',
                   'moz2-darwin9-slave03', 'moz2-darwin9-slave04'],
    'builddir': 'mozilla-central-macosx-unittest',
    'factory': UnittestBuildFactory(
        platform='macosx',
        config_repo_url = nightly_config.CONFIG_REPO_URL,
        config_dir = nightly_config.CONFIG_SUBDIR,
        branch = 'mozilla-central'
    ),
    'category': 'mozilla-central',
}

builders.append(mozilla2_firefox_osx_test_builder)

##
## Mac TraceMonkey UnitTest
##

mozilla2_firefox_osx_test_builder2 = {
    'name': 'OS X 10.5.2 tracemonkey unit test',
    'slavenames': ['bm-xserve16', 'bm-xserve17', 'bm-xserve18', 'bm-xserve19',
                   'bm-xserve22',
                   'moz2-darwin9-slave01', 'moz2-darwin9-slave02',
                   'moz2-darwin9-slave03', 'moz2-darwin9-slave04'],
    'builddir': 'tracemonkey-macosx-unittest',
    'factory': UnittestBuildFactory(
        platform='macosx',
        config_repo_url = nightly_config.CONFIG_REPO_URL,
        config_dir = nightly_config.CONFIG_SUBDIR,
        branch = 'tracemonkey'
    ),
    'category': 'tracemonkey',
}

builders.append(mozilla2_firefox_osx_test_builder2)

##
## Win2k3 UnitTest
##

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
    'factory': UnittestBuildFactory(
        platform='win32',
        config_repo_url = nightly_config.CONFIG_REPO_URL,
        config_dir = nightly_config.CONFIG_SUBDIR,
        branch = 'mozilla-central'
    ),
    'category': 'mozilla-central',
}

builders.append(firefox_trunk_win2k3_builder)

##
## Win2k3 TraceMonkey UnitTest
##

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
    'factory': UnittestBuildFactory(
        platform='win32',
        config_repo_url = nightly_config.CONFIG_REPO_URL,
        config_dir = nightly_config.CONFIG_SUBDIR,
        branch = 'tracemonkey'
    ),
    'category': 'tracemonkey',
}

builders.append(firefox_trunk_win2k3_builder2)
