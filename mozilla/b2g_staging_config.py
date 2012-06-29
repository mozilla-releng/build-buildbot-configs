from copy import deepcopy
import staging_config as sc

GLOBAL_VARS = deepcopy(sc.GLOBAL_VARS)

SLAVES = {
    'mock': sc.SLAVES['mock'] + sc.TRY_SLAVES['mock']
}

TRY_SLAVES = SLAVES.copy()

# Local branch overrides
BRANCHES = {
    'try': {
        'package_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
BUILDS_BEFORE_REBOOT = sc.BUILDS_BEFORE_REBOOT
