from copy import deepcopy
import localconfig

from localconfig import GLOBAL_VARS, BUILDS_BEFORE_REBOOT, \
    SYMBOL_SERVER_HOST

GLOBAL_VARS = deepcopy(localconfig.GLOBAL_VARS)

# Local branch overrides
BRANCHES = {
    'try': {
        'package_url': 'https://ftp-ssl.mozilla.org/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
BUILDS_BEFORE_REBOOT = localconfig.BUILDS_BEFORE_REBOOT
