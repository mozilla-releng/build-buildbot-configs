"""test for master.common builderPriority"""
import unittest
import time
import master_common


class builderStatusStub(object):
    """builder status stub"""
    def __init__(self, category):
        self.category = category


def builderPriorityStub(branch):
    """builder priority stub"""
    status = {}
    status['branch'] = branch
    return status


class builderStub(object):
    """builder stub"""
    def __init__(self, name, branch, category):
        self.properties = builderPriorityStub(branch)
        self.name = name
        self.category = category
        self.builder_status = builderStatusStub(category)

    def get_priority_request(self, request):
        """returns the calculated priority of a builder/request"""
        return master_common.builderPriority(self, request)

    def __repr__(self):
        msg = "name: {0}\n".format(self.name)
        msg = "{0}branch: {1}\n".format(msg, self.properties['branch'])
        msg = "{0}category: {1}".format(msg, self.category)
        return msg


def requestStub(priority, submitted_at):
    """request stub"""
    return (None, priority, submitted_at)


class builderProrityTest(unittest.TestCase):
    """tests for builderPriority"""
    def setUp(self):
        """Prepares a bunch of builders/priorities"""
        # low priority branches:
        # generic builder, oak, release
        self.mozilla_beta = builderStub(name='mozilla beta builder',
                                        branch='mozilla-beta',
                                        category='release')
        # generic builder, oak, non release
        self.oak_builder = builderStub(name='oak release',
                                       branch='oak',
                                       category='non-release')
        # high priority branches:
        # generic builder, mozilla-release, release
        self.mr_release = builderStub(name='release job',
                                      branch='mozilla-release',
                                      category='release')

        # generic builder, mozilla-release, non release
        self.mr_builder = builderStub(name='generic release job',
                                      branch='mozilla-release',
                                      category='non-release')

        # l10n stuff... very low priority
        self.l10n_builder = builderStub(name='l10n',
                                        branch='oak',
                                        category='non-release')

        # requests
        # higher priority means it's more important
        submitted_at = int(time.time())
        last_hour = submitted_at - 3600
        last_day = submitted_at - (3600 * 24)
        last_week = submitted_at - (3600 * 24 * 7)
        epoch = 0

        self.high_priority_request = requestStub(9, submitted_at)
        self.low_priority_request = requestStub(1, submitted_at)

        self.one_hour_old_hp_request = requestStub(9, last_hour)
        self.one_hour_old_lp_request = requestStub(1, last_hour)

        self.one_day_old_hp_request = requestStub(9, last_day)
        self.one_day_old_lp_request = requestStub(1, last_day)

        self.one_week_old_hp_request = requestStub(9, last_week)
        self.one_week_old_lp_request = requestStub(1, last_week)

        self.epoch_old_hp_request = requestStub(9, epoch)
        self.epoch_old_lp_request = requestStub(1, epoch)

    def test_stablity(self):
        """same input, same output"""
        mozilla_beta = self.oak_builder
        request = self.high_priority_request
        priority_0 = mozilla_beta.get_priority_request(request)
        priority_1 = mozilla_beta.get_priority_request(request)
        self.assertTrue(priority_0 == priority_1)

    def test_release(self):
        """Release gets the precedence"""
        oak_builder = self.oak_builder
        mozilla_beta = self.mozilla_beta

        request = self.high_priority_request

        # same request, different builders
        priority_0 = mozilla_beta.get_priority_request(request)
        priority_1 = oak_builder.get_priority_request(request)
        self.assertTrue(priority_0 < priority_1)

    def test_branch_priority(self):
        """same request priority, different branches"""
        mozilla_beta = self.mozilla_beta
        oak_builder = self.oak_builder

        # request
        request = self.low_priority_request

        priority_0 = mozilla_beta.get_priority_request(request)
        priority_1 = oak_builder.get_priority_request(request)
        self.assertTrue(priority_0 < priority_1)

    def test_timestamp_priority(self):
        """same builder, same priority different submitted_at"""
        oak_builder = self.oak_builder
        request_1 = self.one_hour_old_lp_request
        request_2 = self.low_priority_request

        priority_0 = oak_builder.get_priority_request(request_1)
        priority_1 = oak_builder.get_priority_request(request_2)
        self.assertTrue(priority_0 < priority_1)

        request_1 = self.one_week_old_hp_request
        request_2 = self.high_priority_request
        priority_0 = oak_builder.get_priority_request(request_1)
        priority_1 = oak_builder.get_priority_request(request_2)
        self.assertTrue(priority_0 < priority_1)

    def test_request_priority(self):
        """same builder, different priority requests"""
        oak_builder = self.oak_builder

        low_priority_request = self.low_priority_request
        high_priority_request = self.high_priority_request

        priority_0 = oak_builder.get_priority_request(high_priority_request)
        priority_1 = oak_builder.get_priority_request(low_priority_request)
        self.assertTrue(priority_0 < priority_1)

    def test_release_priority(self):
        """release builder vs generic builder, release wins regardless other
           builder gets higher priority request"""
        mr_release = self.mr_release
        oak_builder = self.oak_builder

        low_priority_request = self.low_priority_request
        priority_0 = mr_release.get_priority_request(low_priority_request)
        priority_1 = oak_builder.get_priority_request(low_priority_request)
        self.assertTrue(priority_0 < priority_1)

        # now increase oak_builder priority
        high_priority_request = self.high_priority_request
        priority_1 = oak_builder.get_priority_request(high_priority_request)
        self.assertTrue(priority_0 < priority_1)

        # now move back in time oak_builder
        # 1 hour
        one_hour_old_hp_request = self.one_hour_old_hp_request
        priority_1 = oak_builder.get_priority_request(one_hour_old_hp_request)
        self.assertTrue(priority_0 < priority_1)

        # 1 day
        one_day_old_hp_request = self.one_day_old_hp_request
        priority_1 = oak_builder.get_priority_request(one_day_old_hp_request)
        self.assertTrue(priority_0 < priority_1)

        # 1 week
        one_week_old_hp_request = self.one_week_old_hp_request
        priority_1 = oak_builder.get_priority_request(one_week_old_hp_request)
        self.assertTrue(priority_0 < priority_1)

        # well this is a lot of time
        epoch_old_hp_request = self.epoch_old_hp_request
        priority_1 = oak_builder.get_priority_request(epoch_old_hp_request)
        self.assertTrue(priority_0 < priority_1)

        # if you are here, time is not affecting the ordering,
        # update builder type (was mozilla-release vs mozilla-release)
        # now it's mozilla-release vs mozilla-beta
        mozilla_beta = self.mozilla_beta
        priority_1 = mozilla_beta.get_priority_request(epoch_old_hp_request)
        self.assertTrue(priority_0 < priority_1)

        # mr_release always wins
        mr_builder = self.mr_builder
        priority_1 = mr_builder.get_priority_request(epoch_old_hp_request)
        self.assertTrue(priority_0 < priority_1)

    def test_l10n_always_last(self):
        """l10n builders get lowest priority"""
        mr_builder = self.mr_builder
        oak_builder = self.oak_builder
        l10n_builder = self.l10n_builder

        high_priority_request = self.high_priority_request
        low_priority_request = self.low_priority_request

        # different builders same priorities
        priority_0 = mr_builder.get_priority_request(high_priority_request)
        priority_1 = oak_builder.get_priority_request(high_priority_request)
        priority_2 = l10n_builder.get_priority_request(high_priority_request)
        expected = [priority_0, priority_1, priority_2]
        import random
        # reverse expected results and the sort it,
        # result must be identical to expected results
        result = sorted(reversed(expected))
        self.assertTrue(result == expected)

        # different builders, l10n has the highest priority
        # but it must get the lowest overall prioritization
        priority_0 = mr_builder.get_priority_request(low_priority_request)
        priority_1 = oak_builder.get_priority_request(low_priority_request)
        priority_2 = l10n_builder.get_priority_request(high_priority_request)
        expected = [priority_0, priority_1, priority_2]
        # shuffle elements
        result = sorted(expected, key=lambda *args: random.random())
        # and now sort them
        result = sorted(result)
        self.assertTrue(result == expected)

    def test_slaveapi_priority_increase(self):
        """Same builder and we compare a random priority (rp) with a list
           of priorities. Results are stable and unique"""

        import random
        oak_builder = self.oak_builder
        submitted_at = 0

        priorities_range = range(5, 200)
        random.shuffle(priorities_range)
        random_priority = priorities_range.pop(0)
        request = requestStub(random_priority, submitted_at)

        priority_0 = oak_builder.get_priority_request(request)

        lesser = []
        greater = []
        for priority in priorities_range:
            priority_1 = oak_builder.get_priority_request(
                requestStub(priority, submitted_at))
            if priority_1 < priority_0:
                # req has an higher priority request than request
                greater.append(priority)
            elif priority_1 > priority_0:
                lesser.append(priority)
            else:
                # this means that we have two different values that generate
                # the same tuple, make this test fail
                self.assertTrue(priority_0 > priority_1)
        # no repetitions
        self.assertTrue(len(greater) == len(set(greater)))
        self.assertTrue(len(lesser) == len(set(lesser)))
        # disjoint sets
        self.assertTrue(set(greater).isdisjoint(set(lesser)))
        # random_priority is not part of any list
        self.assertFalse(random_priority in greater)
        self.assertFalse(random_priority in lesser)
        #
        self.assertTrue(min(greater) > max(lesser))


if __name__ == '__main__':
    unittest.main()
