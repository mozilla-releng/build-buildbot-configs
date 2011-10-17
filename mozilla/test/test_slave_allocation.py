from twisted.trial import unittest

import production_config as prod
import staging_config as stag
import preproduction_config as preprod

class SlaveCheck(unittest.TestCase):

    def test_all_prod_vs_try(self):
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

    def test_prod_is_subset_of_stag(self):
        prod_slaves = [x for k, s in prod.SLAVES.iteritems() for x in s]
        stag_slaves = [x for k, s in stag.SLAVES.iteritems() for x in s]
        if hasattr(prod, 'TRY_SLAVES'):
            prod_slaves.extend([x for k, s in prod.TRY_SLAVES.iteritems() for x
                                in s])
        if hasattr(stag, 'TRY_SLAVES'):
            stag_slaves.extend([x for k, s in stag.TRY_SLAVES.iteritems() for x
                                in s])
        in_prod_but_stag = []
        for slave in prod_slaves:
            if slave not in stag_slaves:
                in_prod_but_stag.append(slave)

        self.assertEqual(
            in_prod_but_stag, [],
            'Production slaves should be a subset of staging slaves, ' + \
            'however the following production slaves are not listed in ' + \
            'staging:\n%s' % '\n'.join(sorted(in_prod_but_stag))
        )

    def test_preprod_vs_stag(self):
        preprod_slaves = [x for k, s in preprod.SLAVES.iteritems() for x in s]
        stag_slaves = [x for k, s in stag.SLAVES.iteritems() for x in s]
        if hasattr(preprod, 'TRY_SLAVES'):
            preprod_slaves.extend([x for k, s in preprod.TRY_SLAVES.iteritems() for x
                                in s])
        if hasattr(stag, 'TRY_SLAVES'):
            stag_slaves.extend([x for k, s in stag.TRY_SLAVES.iteritems() for x
                                in s])
        self.assertEqual(
            stag_slaves, preprod_slaves,
            'Staging and preproduction slaves should be the same'
        )

