from buildbot.steps.shell import ShellCommand, WithProperties, SetProperty
from buildbotcustom.process.factory import BaseRepackFactory, CCBaseRepackFactory, identToProperties


class BaseExtensionRepackFactory(BaseRepackFactory):

    def __init__(self, platform, extensionPath, extensionName, enUSBinaryURL, objdir='',
                 baseWorkDir='build', mozRepoPath='', mozconfig=None, configRepoPath=None,
                 configSubDir=None, mozconfigBranch='default', mozillaDir='', env={}, **kwargs):

        self.baseWorkDir = baseWorkDir
        self.objdir = objdir
        self.extensionPath = extensionPath
        self.extensionName = extensionName
        self.mozconfigBranch = mozconfigBranch
        self.env = env
        self.platform = platform

        # This is needed for buildbot 0.7
        if mozconfig and configSubDir and configRepoPath:
            self.mozconfig = 'configs/%s/%s' % (configSubDir, mozconfig)
            self.configRepoPath = configRepoPath
            self.configRepo = self.getRepository(self.configRepoPath, kwargs['hgHost'])

        self.env.update({'EN_US_BINARY_URL': enUSBinaryURL})
        
        # Set up postUploadCmd
        self.setupPostUpload(**kwargs)  

        # bb0.8: BaseRepackFactory.__init__(self, mozillaDir=mozillaDir, env=env, **kwargs)
        BaseRepackFactory.__init__(self, mozillaDir=mozillaDir, **kwargs)


    def getExtWorkDir(self):
        return '%s/%s/%s/%s' % (self.baseWorkDir,
                                self.origSrcDir,
                                self.objdir,
                                self.extensionPath)

    def setupPostUpload(self, **kwargs):
        assert 'project' in kwargs
        assert 'repoPath' in kwargs
        if 'branchName' in kwargs:
          uploadDir = '%s-l10n/%s-xpi' % (kwargs['branchName'], self.platform)
        else:
          uploadDir = '%s-l10n/%s-xpi' % (self.getRepoName(kwargs['repoPath']), self.platform)

        postUploadCmd = ['post_upload.py',
                         '-p %s ' % kwargs['project'],
                         '-b %s ' % uploadDir,
                         '--nightly-dir=%s/nightly' % self.extensionName,
                         '--buildid %(buildid)s',
                         '--release-to-latest',
                         '--release-to-dated',
                         '--no-shortdir']

        self.postUploadCmd = WithProperties(' '.join(postUploadCmd))
        

    def downloadBuilds(self):
        # Call make wget-en-US, but in the extension directory
        self.addStep(ShellCommand,
            name='wget_enUS',
            command=['make', 'wget-en-US'],
            descriptionDone='wget en-US',
            env=self.env,
            haltOnFailure=True,
            workdir=self.getExtWorkDir()
        )

    def updateEnUS(self):
        # Call make unpack, but in the extension directory
        self.addStep(ShellCommand,
            name='make_unpack',
            command=['make', 'unpack'],
            haltOnFailure=True,
            workdir=self.getExtWorkDir(),
        )

        # Extensions using this factory might want to to package a mock
        # application.ini so that they can use printconfigsettings.py to read
        # the ident properties easier.
        self.addStep(SetProperty,
         name='make_ident',
         command=['make', 'ident'],
         haltOnFailure=True,
         extract_fn=identToProperties(),
         workdir=self.getExtWorkDir()
        )
        self.addStep(ShellCommand,
         name='update_to_packaged_rev',
         command=['hg', 'update', '-r', WithProperties('%(moz_revision)s')],
         haltOnFailure=True,
         workdir='%s/%s' % (self.baseWorkDir, self.origSrcDir)
        )

    def doRepack(self):
        # Let the extension repackage the l10n files
        self.addStep(ShellCommand,
            name='make_repack_l10n',
            command=['sh','-c',
                     WithProperties('make repack-l10n-%(locale)s')],
            env=self.env,
            haltOnFailure=True,
            description=['make', 'repack-l10n-AB_CD'],
            workdir=self.getExtWorkDir()
        )

    def doUpload(self):
        # Call make l10n-upload-ab_CD, but in the extension directory
        self.addStep(ShellCommand,
            name='make_l10n_upload',
            command=['make', WithProperties('l10n-upload-%(locale)s')],
            env=self.uploadEnv,
            workdir=self.getExtWorkDir(),
            haltOnFailure=True,
            flunkOnFailure=True
        )

    def updateSources(self):
        self.addStep(ShellCommand,
         name='update_locale_source',
         command=['hg', 'up', '-C', '-r', self.l10nTag],
         description='update workdir',
         workdir=WithProperties('build/' + self.l10nRepoPath + '/%(locale)s'),
         haltOnFailure=True
        )
        self.addStep(SetProperty,
            command=['hg', 'ident', '-i'],
            haltOnFailure=True,
            property='l10n_revision',
            workdir=WithProperties('build/' + self.l10nRepoPath +  '/%(locale)s')
        )

class CCBaseExtensionRepackFactory(BaseExtensionRepackFactory, CCBaseRepackFactory):
 
    # XXX Unfortunately the buildbot factory uses --enable-application=%(appName)
    # appName needs to be calendar, but we want to build mail+calendar in the
    # Lightning case. Adding this appends another --enable-application, which is
    # taken since its the later argument.
    # We must also add --enable-calendar as we're currently not getting the mozconfigs
    # for repacks (which probably is the right, quicker thing to do as well).
    extraConfigureArgs = ['--enable-application=mail']

    def __init__(self, platform, extensionName, extensionPath, enUSBinaryURL, objdir='',
                 baseWorkDir='build', mozRepoPath='', mozconfig=None, configRepoPath=None,
                 configSubDir=None, env={}, **kwargs):

        # Unfortunately we have to set these ourselves, python inheritance can
        # be very annoying.
        self.baseWorkDir = baseWorkDir
        self.objdir = objdir
        self.extensionName = extensionName
        self.extensionPath = extensionPath
        self.l10nTag = 'default'
        self.mozRepoPath = mozRepoPath
        self.env = env.copy()
        self.platform = platform


        self.setupPostUpload(**kwargs)

        # Now initialize our base factories.
        CCBaseRepackFactory.__init__(self,
                                     baseWorkDir=baseWorkDir,
                                     mozRepoPath=mozRepoPath, **kwargs)

        BaseExtensionRepackFactory.__init__(self,
                                        platform=platform,
                                        extensionPath=extensionPath,
                                        extensionName=extensionName,
                                        enUSBinaryURL=enUSBinaryURL,
                                        baseWorkDir=baseWorkDir,
                                        mozRepoPath=mozRepoPath,
                                        mozconfig=mozconfig,
                                        configRepoPath=configRepoPath,
                                        configSubDir=configSubDir,
                                        mozillaDir='mozilla',
                                        env=env,
                                        **kwargs)

    def getSources(self):
        # Getting the sources should happen in the comm-central factory so that
        # client.py can do its magic.
        CCBaseRepackFactory.getSources(self);

    def updateEnUS(self):
        # Call make unpack, but in the extension directory
        self.addStep(ShellCommand,
            command=['make', 'unpack'],
            haltOnFailure=True,
            workdir=self.getExtWorkDir(),
        )

        # Extensions using this factory might want to to package a mock
        # application.ini so that they can use printconfigsettings.py to read
        # the ident properties easier.
        self.addStep(SetProperty,
         command=['make', 'ident'],
         haltOnFailure=True,
         extract_fn=identToProperties(),
         workdir=self.getExtWorkDir()
        )
        self.addStep(ShellCommand,
         command=['hg', 'update', '-r', WithProperties('%(comm_revision)s')],
         haltOnFailure=True,
         workdir='%s/%s' % (self.baseWorkDir, self.origSrcDir)
        )
        self.addStep(ShellCommand,
         command=['hg', 'update', '-r', WithProperties('%(moz_revision)s')],
         haltOnFailure=True,
         workdir='%s/%s' % (self.baseWorkDir, self.mozillaSrcDir)
        )

class NightlyExtensionRepackFactory(BaseExtensionRepackFactory):
    def __init__(self, **kwargs):

        BaseExtensionRepackFactory.__init__(self, **kwargs)

class CCNightlyExtensionRepackFactory(CCBaseExtensionRepackFactory):
    def __init__(self,
                  mozconfig=None, configRepoPath=None, configSubDir=None, mozconfigBranch='default',
                  **kwargs):

        # This is needed for buildbot 0.7
        self.mozconfigBranch = mozconfigBranch
        if mozconfig and configSubDir and configRepoPath:
            self.mozconfig = 'configs/%s/%s' % (configSubDir, mozconfig)
            self.configRepoPath = configRepoPath
            self.configRepo = self.getRepository(self.configRepoPath, kwargs['hgHost'])
        # end buildbot 0.7

        CCBaseExtensionRepackFactory.__init__(self,
                                              mozconfig=mozconfig,
                                              configRepoPath=configRepoPath,
                                              configSubDir=configSubDir,
                                              **kwargs)

    def getMozconfig(self):
        if self.mozconfig:
            self.addStep(ShellCommand(
             name='rm_configs',
             command=['rm', '-rf', 'configs'],
             description=['remove', 'configs'],
             workdir='build/'+self.origSrcDir,
             haltOnFailure=True
            ))
            # Buildbot 0.7 requires this, later use MercurialCloneCommand
            self.addStep(ShellCommand(
             name='checkout_configs',
             command=['hg', 'clone', self.configRepo, 'configs'],
             description=['checkout', 'configs'],
             workdir='build/'+self.origSrcDir,
             haltOnFailure=True
            ))
            self.addStep(ShellCommand(
             name='hg_update',
             command=['hg', 'update', '-r', self.mozconfigBranch],
             description=['updating', 'mozconfigs'],
             workdir="build/%s/configs" % self.origSrcDir,
             haltOnFailure=True
            ))
            self.addStep(ShellCommand(
             # cp configs/mozilla2/$platform/$branchname/$type/mozconfig .mozconfig
             name='copy_mozconfig',
             command=['cp', self.mozconfig, '.mozconfig'],
             description=['copy mozconfig'],
             workdir='build/'+self.origSrcDir,
             haltOnFailure=True
            ))
            self.addStep(ShellCommand,
             name='cat_mozconfig',
             command=['cat', '.mozconfig'],
             workdir='build/'+self.origSrcDir
            )
