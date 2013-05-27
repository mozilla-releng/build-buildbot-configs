# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    'build-system': {},
    'devtools': {
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
    # Please sync any customizations made to mozilla-inbound to cypress.
    'mozilla-inbound': {
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
    },
    # Customized to be the same as inbound. bug 866314
    'cypress': {
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
        'platforms': {
            'macosx64_gecko': {
                'enable_checktests': False,
            },
            'win32_gecko': {
                'enable_checktests': False,
            },
        },
    },
    'cedar': {
        'mozharness_tag': 'default',
    },
    'date': {
        'lock_platforms': True,
        'platforms': {},
    },
    # Customizations for windows update service changes (bug 481815)
    #'elm': {},
    'fig': {
        'lock_platforms': True,
        'platforms': {},
    },
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
