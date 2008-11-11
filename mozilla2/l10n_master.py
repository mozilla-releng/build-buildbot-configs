# -*- python -*-
# ex: set syntax=python:

#configuration file for l10n
import l10n_config
reload(l10n_config)
from l10n_config import *

# l10n logic
import buildbotcustom.l10n
reload(buildbotcustom.l10n)

builders = []

from buildbot.process import factory
from buildbot.steps.shell import ShellCommand, Compile, WithProperties

#### Factory
BRANCH = 'mozilla-central' 
PROJECT = 'firefox'

L10nNightlyFactory = factory.BuildFactory()
L10nNightlyFactory.addStep(ShellCommand,
# This will remove the folder from which we upload the packages that are generated
    command=['rm','-rf', BRANCH+'/dist/upload'],
    workdir=".",
    haltOnFailure = True)
L10nNightlyFactory.addStep(ShellCommand,
    command = ['sh', '-c', 'mkdir -p l10n-central'],
    descriptionDone="mkdir l10n-central",
    workdir="."
)
L10nNightlyFactory.addStep(ShellCommand,
    command = ['sh', '-c',
                 'if [ -d '+BRANCH+' ]; then ' +
                 'hg -R '+BRANCH+' pull -r tip ; ' +
                 'else ' +
                 'hg clone http://hg.mozilla.org/'+BRANCH+'/ ; ' +
                 'fi '
                 '&& hg -R '+BRANCH+' update'],
    descriptionDone = BRANCH + "'s source", 
    workdir = ".",
    haltOnFailure = True
)
L10nNightlyFactory.addStep(ShellCommand,
    command = ['sh', '-c',
               WithProperties('if [ -d %(locale)s ]; then ' +
                              'hg -R %(locale)s pull -r tip ; ' +
                              'else ' +
                              'hg clone http://hg.mozilla.org/l10n-central/%(locale)s/ ; ' +
                              'fi '
                              '&& hg -R %(locale)s update')],
    descriptionDone = "locale's source",
    workdir="l10n-central"
)
L10nNightlyFactory.addStep(ShellCommand,
    command = ['make','-f','client.mk','configure'],
    env={'CONFIGURE_ARGS':'--enable-application=browser'},
    haltOnFailure=True,
    descriptionDone="autoconf",
    workdir = BRANCH
)
L10nNightlyFactory.addStep(Compile,
    command = ['sh', '--',
               './configure', '--enable-application=browser',
               '--disable-compile-environment',
               '--with-l10n-base=../l10n-central'],
    description="configure",
    descriptionDone="configure done",
    haltOnFailure=True,
    workdir=BRANCH,
)
L10nNightlyFactory.addStep(ShellCommand,
    command=["make", "wget-en-US"],
    descriptionDone="wget en-US",
    env={'EN_US_BINARY_URL':enUS_binaryURL},
    haltOnFailure = True,
    workdir=BRANCH+"/browser/locales"
)
#It seems that I need to set env={'PKG_DMG_SOURCE':PROJECT}
#because of /packager.mk#144
L10nNightlyFactory.addStep(ShellCommand,
    command=["make", WithProperties("installers-%(locale)s")],
    env={'PKG_DMG_SOURCE':PROJECT},
    haltOnFailure = True,
    workdir=BRANCH+"/browser/locales"
)
L10nNightlyFactory.addStep(ShellCommand,
    command=["make", WithProperties("prepare-upload-latest-%(locale)s")],
    haltOnFailure=True,
    workdir=BRANCH+"/browser/locales"
)
# This will upload everything in dist/upload, I assume that the first 
# step run in this build is "rm -rf BRANCH/dist/upload"
L10nNightlyFactory.addStep(ShellCommand,
    name = "upload locale",
    command=['sh','-c','scp -i ~/.ssh/ffxbld_dsa -r * ffxbld@'+ftpserver+":"+uploadPath],
    description="uploading packages", 
    descriptionDone="uploaded packages",
    workdir=BRANCH+"/dist/upload/latest"
)
