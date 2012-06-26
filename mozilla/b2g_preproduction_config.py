from copy import deepcopy

from preproduction_config import GLOBAL_VARS, MOCK_DL120G7, TRY_MOCK_DL120G7, \
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
    'try': {
        'package_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
