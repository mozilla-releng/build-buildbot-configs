# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    'build-system': {},
    'devtools':{
        'enable_nightly': True,
    },
    # Disabled because of builder limit problems - bug 721854
    #'electrolysis': {},
    'fx-team': {
        'repo_path': 'integration/fx-team',
        'enable_nightly': False,
    },
    'graphics': {},
    'ionmonkey': {
        'enable_nightly': True
    },
    'jaegermonkey': {
        'enable_nightly': True
    },
    'mozilla-inbound': {
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
    },
    # Disabled because of builder limit problems - bug 721854
    #'places': {},
    # B2G builds not required on the profiling branch
    #'profiling': {},
    'services-central': {
        'repo_path': 'services/services-central'
    },
    # B2G builds not required on the UX branch
    #'ux': {
    #    'branch_name': 'UX',
    #    'mobile_branch_name': 'UX',
    #    'build_branch': 'UX',
    #    'enable_nightly': True,
    #},
    #####  TWIGS aka RENTABLE BRANCHES
    'alder': {},
    'ash': {
        'mozharness_repo_path': 'users/asasaki_mozilla.com/ash-mozharness',
    },
    'birch': {
        'enable_perproduct_builds': True,
    },
    'cedar': {},
    'cypress': {
        'enable_perproduct_builds': True,
    },
    'date': {},
    'gaia-master': {
        'repo_path': 'mozilla-central',
        'poll_repo': 'integration/gaia-central',
        'lock_platforms': True,
        'platforms': {
            'panda': {
                'mozharness_config': {
                    'script_name': 'scripts/b2g_build.py',
                    'extra_args': ['--target', 'panda', '--config', 'b2g/releng.py',
                                   '--gaia-languages-file', 'locales/languages_dev.json',
                                   '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                                   '--additional-source-tarballs', 'download-panda.tar.bz2',
                                   '--checkout-revision', 'default'],
                    'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
                }
            }
        }
    },
    # Customizations for windows update service changes (bug 481815)
    #'elm': {},
    'fig': {},
    'gum': {},
    'holly': {},
    # Bug 848025 - disable b2g builds for jamun
    #'jamun': {},
    'larch': {},
    'maple': {},
    # Customizations for integration work for bugs 481815 and 307181
    'oak': {
        'enable_nightly': True
    },
    'pine': {},
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()
