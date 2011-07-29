from twisted.trial import unittest

import production_config as prod
import staging_config as stag

class SlaveCheck(unittest.TestCase):

    def test_all_prod_vs_try(self):
        prod_slaves = [x for k, s in prod.SLAVES.iteritems() for x in s]
        try_slaves = [x for k, s in prod.TRY_SLAVES.iteritems() for x in s]
        self.assertEqual(set(prod_slaves) & set(try_slaves), set([]))

    def test_prod_is_subset_of_stag(self):
        prod_slaves = [x for k, s in prod.SLAVES.iteritems() for x in s] + \
            [x for k, s in prod.TRY_SLAVES.iteritems() for x in s]
        stag_slaves = [x for k, s in stag.SLAVES.iteritems() for x in s] + \
            [x for k, s in stag.TRY_SLAVES.iteritems() for x in s]
        self.assertTrue(set(prod_slaves) <= set(stag_slaves))
