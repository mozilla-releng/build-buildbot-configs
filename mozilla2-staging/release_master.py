from buildbot.changes.pb import PBChangeSource
from buildbot.scheduler import Scheduler, Dependent

import buildbotcustom.misc
import buildbotcustom.process.factory
reload(buildbotcustom.misc)
reload(buildbotcustom.process.factory)

from buildbotcustom.misc import get_l10n_repositories
from buildbotcustom.process.factory import ReleaseTaggingFactory, \
  SingleSourceFactory

# this is where all of our important configuration is stored. build number,
# version number, sign-off revisions, etc.
from release_config import *

builders = []
schedulers = []
change_source = []
status = []

##### Change sources and Schedulers
change_source.append(PBChangeSource())

tag_scheduler = Scheduler(
    name='tag',
    branch='release',
    treeStableTimer=0,
    builderNames=['tag'],
)
build_scheduler = Dependent(
    name='build',
    upstream=tag_scheduler,
    builderNames=['source']
)

schedulers.append(tag_scheduler)
schedulers.append(build_scheduler)

##### Builders
repositories = {
    mozillaCentral: {
        'revision': mozillaCentralRevision,
        'relbranchOverride': relbranchOverride,
        'bumpFiles': ['config/milestone.txt', 'browser/config/version.txt',
                      'browser/app/module.ver']
    }
}
l10n_repos = get_l10n_repositories(l10nRevisionFile, l10nCentral,
                                   relbranchOverride)
repositories.update(l10n_repos)

tag_factory = ReleaseTaggingFactory(
    repositories=repositories,
    buildToolsRepo=buildTools,
    productName=productName,
    appName=appName,
    appVersion=appVersion,
    milestone=milestone,
    baseTag=baseTag,
    buildNumber=buildNumber
)

builders.append({
    'name': 'tag',
    'slavenames': ['moz2-linux-slave04'],
    'category': 'release',
    'builddir': 'tag',
    'factory': tag_factory
})


source_factory = SingleSourceFactory(
    repository=mozillaCentral,
    productName=productName,
    appVersion=appVersion,
    baseTag=baseTag
)

builders.append({
   'name': 'source',
   'slavenames': ['moz2-linux-slave04'],
   'category': 'release',
   'builddir': 'source',
   'factory': source_factory
})
