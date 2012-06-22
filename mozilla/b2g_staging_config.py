from copy import deepcopy

from production_config import GLOBAL_VARS, MOCK_DL120G7, TRY_MOCK_DL120G7, \
    BUILDS_BEFORE_REBOOT

GLOBAL_VARS = deepcopy(GLOBAL_VARS)

SLAVES = {
    'mock': MOCK_DL120G7
}

TRY_SLAVES = {
    'mock': TRY_MOCK_DL120G7,
}

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'tinderbox_tree': 'MozillaTest',
    },
    'mozilla-inbound': {
        'tinderbox_tree': 'MozillaTest',
    },
    'try': {
        'tinderbox_tree': 'MozillaTest',
        'package_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
