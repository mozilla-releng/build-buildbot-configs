from copy import deepcopy
import production_config as pc

from production_config import GLOBAL_VARS, BUILDS_BEFORE_REBOOT, \
    SYMBOL_SERVER_HOST

GLOBAL_VARS = deepcopy(pc.GLOBAL_VARS)

# Local branch overrides
BRANCHES = {
    'try': {
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
BUILDS_BEFORE_REBOOT = pc.BUILDS_BEFORE_REBOOT
