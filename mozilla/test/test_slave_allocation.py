from twisted.trial import unittest
from twisted.python import log

import production_config as prod
import staging_config as stag

class SlaveCheck(unittest.TestCase):
    def test_Win32_Prod_Try(self):
        self.assertEqual(set(prod.WIN32_IXS) & set(prod.TRY_WIN32_IXS), set([]))

    def test_Win64_Prod_Try(self):
        self.assertEqual(set(prod.WIN64_IXS) & set(prod.TRY_WIN64_IXS), set([]))

    def test_Linux32_Prod_Try(self):
        self.assertEqual(set(prod.LINUX_IXS) & set(prod.TRY_LINUX_IXS), set([]))

    def test_Linux64_Prod_Try(self):
        self.assertEqual(set(prod.LINUX64_IXS) & set(prod.TRY_LINUX64_IXS), set([]))

