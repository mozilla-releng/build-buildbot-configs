from copy import deepcopy
import staging_config as sc

from staging_config import GLOBAL_VARS, BUILDS_BEFORE_REBOOT, \
    SYMBOL_SERVER_HOST

GLOBAL_VARS = deepcopy(sc.GLOBAL_VARS)

# Local branch overrides
BRANCHES = {
    'try': {
        'package_url': 'http://dev-stage01.srv.releng.scl3.mozilla.com/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
BUILDS_BEFORE_REBOOT = sc.BUILDS_BEFORE_REBOOT
