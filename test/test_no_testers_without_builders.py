'''
This script generates a list of buildbot test builders that do not
have a build to trigger it.
'''
import os

from mozci.platforms import determine_upstream_builder
from mozci.sources.allthethings import fetch_allthethings_data


def test_no_testers_without_builders():
    # We need to assert that allthethings.json has been generated
    # before running this test rather than fetching the one from the server
    # This is important as we want to test against the latest list of builders
    assert os.path.exists("allthethings.json")

    orphan_builders = []

    j = fetch_allthethings_data(verify=False)
    builders = j["builders"].keys()
    assert builders is not None, "The list of builders cannot be empty."

    for builder in sorted(builders):
        if determine_upstream_builder(builder) is None:
            orphan_builders.append(builder)

    assert len(orphan_builders) == 0, \
        "There are downstream builders without upstream builders to trigger them."
