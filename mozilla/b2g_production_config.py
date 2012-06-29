from copy import deepcopy
import production_config as pc

GLOBAL_VARS = deepcopy(pc.GLOBAL_VARS)

SLAVES = {
    'mock': pc.SLAVES['mock']
}

TRY_SLAVES = {
    'mock': pc.TRY_SLAVES['mock']
}

# Local branch overrides
BRANCHES = {
    'try': {
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
BUILDS_BEFORE_REBOOT = pc.BUILDS_BEFORE_REBOOT
