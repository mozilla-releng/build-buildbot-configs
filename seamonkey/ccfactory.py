from datetime import datetime
import os.path, re
from time import strftime

from twisted.python import log

from buildbot.process.factory import BuildFactory
from buildbot.steps.shell import ShellCommand, WithProperties, SetProperty
from buildbot.steps.source import Mercurial
from buildbot.steps.transfer import FileDownload

#import buildbotcustom.steps.misc
#import buildbotcustom.steps.release
#import buildbotcustom.steps.test
#import buildbotcustom.steps.transfer
#import buildbotcustom.steps.updates
#import buildbotcustom.steps.talos
#import buildbotcustom.steps.unittest
#import buildbotcustom.env
#reload(buildbotcustom.steps.misc)
#reload(buildbotcustom.steps.release)
#reload(buildbotcustom.steps.test)
#reload(buildbotcustom.steps.transfer)
#reload(buildbotcustom.steps.updates)
#reload(buildbotcustom.steps.talos)
#reload(buildbotcustom.steps.unittest)
#reload(buildbotcustom.env)

from buildbotcustom.steps.misc import SetMozillaBuildProperties, \
  TinderboxShellCommand, SendChangeStep, GetBuildID, MozillaClobberer, \
  FindFile, DownloadFile, UnpackFile, SetBuildProperty, GetHgRevision
from buildbotcustom.steps.release import UpdateVerify, L10nVerifyMetaDiff
from buildbotcustom.steps.test import AliveTest, CompareBloatLogs, \
  CompareLeakLogs, Codesighs, GraphServerPost
from buildbotcustom.steps.transfer import MozillaStageUpload
from buildbotcustom.steps.updates import CreateCompleteUpdateSnippet
from buildbotcustom.env import MozillaEnvironments

import buildbotcustom.steps.unittest as unittest_steps

import buildbotcustom.steps.talos as talos_steps

# we're basically just extending buildbotcustom.process.factory
#import buildbotcustom.process.factory
#reload(buildbotcustom.process.factory)
from buildbotcustom.process.factory import *

class CCReleaseTaggingFactory(ReleaseTaggingFactory):
    def __init__(self, chatzillaTimestamp, cvsroot, **kwargs):
        ReleaseTaggingFactory.__init__(self, **kwargs)

        # need to repeat those definitions here
        buildTag = '%s_BUILD%s' % (kwargs['baseTag'], str(kwargs['buildNumber']))
        releaseTag = '%s_RELEASE' % kwargs['baseTag']

        if cvsroot and chatzillaTimestamp:
            self.addStep(ShellCommand,
             command=['cvs', '-d', cvsroot, '-q',
                      'checkout', '-P', '-D', chatzillaTimestamp,
                      '-d', 'chatzilla', 'mozilla/extensions/irc'],
             workdir='.',
             description=['check out ChatZilla'],
             haltOnFailure=True,
             timeout=30*60 # 30 minutes
            )
            for tag in (buildTag, releaseTag):
                self.addStep(ShellCommand,
                 command=['cvs', '-d', cvsroot, 'tag',
                          '-D', chatzillaTimestamp,
                          '-F', tag],
                 workdir='chatzilla',
                 description=['tag ChatZilla'],
                 haltOnFailure=True
                )

class CCSourceFactory(ReleaseFactory):
    def __init__(self, productName, version, baseTag, stagingServer,
                 stageUsername, stageSshKey, buildNumber, mozRepoPath,
                 inspectorRepoPath='', venkmanRepoPath='', cvsroot='',
                 autoconfDirs=['.'], buildSpace=1, **kwargs):
        ReleaseFactory.__init__(self, buildSpace=buildSpace, **kwargs)
        releaseTag = '%s_RELEASE' % (baseTag)
        sourceTarball = 'source/%s-%s.source.tar.bz2' % (productName,
                                                         version)
        # '-c' is for "release to candidates dir"
        postUploadCmd = 'post_upload.py -p %s -v %s -n %s -c' % \
          (productName, version, buildNumber)
        uploadEnv = {'UPLOAD_HOST': stagingServer,
                     'UPLOAD_USER': stageUsername,
                     'UPLOAD_SSH_KEY': '~/.ssh/%s' % stageSshKey,
                     'UPLOAD_TO_TEMP': '1',
                     'POST_UPLOAD_CMD': postUploadCmd}

        self.addStep(ShellCommand,
         command=['rm', '-rf', 'source'],
         workdir='.',
         haltOnFailure=True
        )
        self.addStep(ShellCommand,
         command=['mkdir', 'source'],
         workdir='.',
         haltOnFailure=True
        )
        self.addStep(ShellCommand,
         command=['hg', 'clone', self.repository, self.branchName],
         workdir='.',
         description=['clone %s' % self.branchName],
         haltOnFailure=True,
         timeout=30*60 # 30 minutes
        )
        # build up the checkout command that will bring us up to the release version
        co_command = ['python', 'client.py', 'checkout',
                      '--comm-rev=%s' % releaseTag,
                      '--mozilla-repo=%s' % self.getRepository(mozRepoPath),
                      '--mozilla-rev=%s' % releaseTag]
        if inspectorRepoPath:
            co_command.append('--inspector-repo=%s' % self.getRepository(inspectorRepoPath))
            co_command.append('--inspector-rev=%s' % releaseTag)
        else:
            co_command.append('--skip-inspector')
        if venkmanRepoPath:
            co_command.append('--venkman-repo=%s' % self.getRepository(venkmanRepoPath))
            co_command.append('--venkman-rev=%s' % releaseTag)
        else:
            co_command.append('--skip-venkman')
        if cvsroot:
            co_command.append('--cvsroot=%s' % cvsroot)
        else:
            co_command.append('--skip-chatzilla')
        # execute the checkout
        self.addStep(ShellCommand,
         command=co_command,
         workdir=self.branchName,
         description=['update to', releaseTag],
         haltOnFailure=True
        )
        if cvsroot:
            # Update ChatZilla to release tag
            self.addStep(ShellCommand,
             command=['cvs', 'up', '-r', releaseTag],
             workdir='%s/mozilla/extensions/irc' % self.branchName,
             description=['update to', releaseTag],
             haltOnFailure=True
            )
        # the autoconf and actual tarring steps
        # should be replaced by calling the build target
        for dir in autoconfDirs:
            self.addStep(ShellCommand,
             command=['autoconf-2.13'],
             workdir='%s/%s' % (self.branchName, dir),
             haltOnFailure=True
            )
        self.addStep(ShellCommand,
         command=['tar', '-cj', '--owner=0', '--group=0', '--numeric-owner',
                  '--mode=go-w', '--exclude=.hg*', '--exclude=CVS',
                  '--exclude=.cvs*', '-f', sourceTarball, self.branchName],
         workdir='.',
         description=['create tarball'],
         haltOnFailure=True
        )
        self.addStep(ShellCommand,
         command=['python', '%s/mozilla/build/upload.py' % self.branchName,
                  '--base-path', '.', sourceTarball],
         workdir='.',
         env=uploadEnv,
         description=['upload files'],
        )

class CCReleaseBuildFactory(CCMercurialBuildFactory, ReleaseBuildFactory):
    def __init__(self, mozRepoPath='', inspectorRepoPath='',
                 venkmanRepoPath='', cvsroot='', **kwargs):
        self.skipBlankRepos = True
        self.mozRepoPath = mozRepoPath
        self.inspectorRepoPath = inspectorRepoPath
        self.venkmanRepoPath = venkmanRepoPath
        self.cvsroot = cvsroot
        # ReleaseBuildFactory.__init__ turns prettynames on!
        ReleaseBuildFactory.__init__(self, mozillaDir='mozilla', **kwargs)

class CCReleaseRepackFactory(CCBaseRepackFactory, ReleaseRepackFactory):
    def __init__(self, mozRepoPath='', inspectorRepoPath='',
                 venkmanRepoPath='', cvsroot='', **kwargs):
        self.skipBlankRepos = True
        self.mozRepoPath = mozRepoPath
        self.inspectorRepoPath = inspectorRepoPath
        self.venkmanRepoPath = venkmanRepoPath
        self.cvsroot = cvsroot
        # ReleaseRepackFactory.__init__ turns prettynames on!
        ReleaseRepackFactory.__init__(self, mozillaDir='mozilla', **kwargs)

    def updateSources(self):
        ReleaseRepackFactory.updateSources(self)
        self.addStep(ShellCommand,
         command=['hg', 'up', '-C', '-r', self.buildRevision],
         workdir='build/'+self.mozillaSrcDir,
         description=['update mozilla',
                      'to %s' % self.buildRevision],
         haltOnFailure=True
        )
        if self.venkmanRepoPath:
            self.addStep(ShellCommand,
             command=['hg', 'up', '-C', '-r', self.buildRevision],
             workdir='build/'+self.mozillaSrcDir+'/extensions/venkman',
             description=['update venkman',
                          'to %s' % self.buildRevision],
             haltOnFailure=True
            )
        if self.inspectorRepoPath:
            self.addStep(ShellCommand,
             command=['hg', 'up', '-C', '-r', self.buildRevision],
             workdir='build/'+self.mozillaSrcDir+'/extensions/inspector',
             description=['update inspector',
                          'to %s' % self.buildRevision],
             haltOnFailure=True
            )
        if self.cvsroot:
            self.addStep(ShellCommand,
             command=['cvs', 'up', '-r', self.buildRevision],
             workdir='build/'+self.mozillaSrcDir+'/extensions/irc',
             description=['update chatzilla',
                          'to %s' % self.buildRevision],
             haltOnFailure=True
            )

    def downloadBuilds(self):
        # XXX: the current ReleaseRepackFactory.downloadBuilds ONLY works for prettynames!
        ReleaseRepackFactory.downloadBuilds(self)

    # unsure why we need to explicitely do this but after bug 478436 we stopped
    # executing the actual repackaging without this def here
    def doRepack(self):
        ReleaseRepackFactory.doRepack(self)
