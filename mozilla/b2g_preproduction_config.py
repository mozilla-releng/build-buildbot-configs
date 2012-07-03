from copy import deepcopy
import preproduction_config as ppc

from preproduction_config import GLOBAL_VARS, BUILDS_BEFORE_REBOOT, \
    SYMBOL_SERVER_HOST

GLOBAL_VARS = deepcopy(ppc.GLOBAL_VARS)

# Local branch overrides
BRANCHES = {
    'try': {
        'package_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
BUILDS_BEFORE_REBOOT = ppc.BUILDS_BEFORE_REBOOT
