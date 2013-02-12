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
        'enable_nightly': True,
    },
    # Turning off graphics - bug 649507
    #'graphics': {},
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
    # Only need to build on OS X (testing gcc OS X builds still work)
    #'birch': {},
    'cedar': {},
    # Customizations for b2g 1.1 work (bug 822783 & bug 819368)
    'date': {
        'enable_nightly': True,
        'enable_l10n': False,
        'enable_xulrunner': False,
        'enabled_products': ['b2g'],
        'product_prefix': 'b2g',
        'unittest_suites': [],
        # XXX: this seems like it should be at the platform level
        'enable_multi_locale': True,
        'lock_platforms': True,
        'platforms': {
            'ics_armv7a_gecko': {},
            'ics_armv7a_gecko-debug': {},
            'linux32_gecko': {},
            'linux64_gecko': {},
            'macosx64_gecko': {},
            'win32_gecko': {},
            'linux32_gecko_localizer': {},
            'linux64_gecko_localizer': {},
            'macosx64_gecko_localizer': {},
            'win32_gecko_localizer': {},
            'panda': {},
            'unagi': {
                'enable_nightly': True,
            },
            'unagi_eng': {},
            'otoro': {},
        },
    },
    # Customizations for windows update service changes (bug 481815)
    #'elm': {},
    'fig': {},
    'gum': {},
    'holly': {},
    'jamun': {},
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
