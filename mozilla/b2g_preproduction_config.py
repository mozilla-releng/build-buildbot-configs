from copy import deepcopy
import preproduction_config as ppc

GLOBAL_VARS = deepcopy(ppc.GLOBAL_VARS)

SLAVES = {
    'mock': ppc.SLAVES['mock'] + ppc.TRY_SLAVES['mock']
}

TRY_SLAVES = SLAVES.copy()

# Local branch overrides
BRANCHES = {
    'try': {
        'package_url': 'http://preproduction-stage.srv.releng.scl3.mozilla.com/pub/mozilla.org/b2g/try-builds',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
BUILDS_BEFORE_REBOOT = ppc.BUILDS_BEFORE_REBOOT
