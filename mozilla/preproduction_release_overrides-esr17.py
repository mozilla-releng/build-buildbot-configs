releaseConfig['sourceRepositories']['mozilla']['path'] = 'users/prepr-ffxbld/mozilla-esr17'
releaseConfig['sourceRepositories']['mozilla']['clonePath'] = 'releases/mozilla-esr17'
releaseConfig['l10nRepoClonePath']   = 'releases/l10n/mozilla-esr17'
releaseConfig['otherReposToTag']     = {
    'users/prepr-ffxbld/compare-locales': 'RELEASE_AUTOMATION',
    'users/prepr-ffxbld/buildbot': 'production-0.8',
    'users/prepr-ffxbld/mozharness': 'default',
}
