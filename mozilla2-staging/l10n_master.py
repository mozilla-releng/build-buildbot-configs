# -*- python -*-
# ex: set syntax=python:

import config as nightly_config
reload(nightly_config)

#configuration file for l10n
import l10n_config
reload(l10n_config)
from l10n_config import *

# l10n logic
import buildbotcustom.process.factory
reload(buildbotcustom.process.factory)

from buildbotcustom.process.factory import RepackFactory

L10nNightlyFactory = RepackFactory(
    branch=branch,
    project=project,
    enUSBinaryURL=enUS_binaryURL,
    stageServer=nightly_config.STAGE_SERVER,
    stageUsername=nightly_config.STAGE_USERNAME,
    uploadPath=uploadPath
)
