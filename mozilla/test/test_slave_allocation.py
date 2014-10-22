from twisted.trial import unittest

import production_config as prod
import staging_config as stag
import preproduction_config as preprod


class SlaveCheck(unittest.TestCase):

    def test_prod_vs_try(self):
        if hasattr(prod, 'TRY_SLAVES'):
            prod_slaves = [x for k, s in prod.SLAVES.iteritems() for x in s]
            try_slaves = [x for k, s in prod.TRY_SLAVES.iteritems() for x in s]
            common_slaves = set(prod_slaves) & set(try_slaves)
            self.assertEqual(
                common_slaves, set([]),
                'Try slaves must not be used in production, however the ' + \
                'following slaves used for both:\n%s' % \
                '\n'.join(common_slaves)
            )
