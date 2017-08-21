import json
import os


_gecko_versions = None


def get_gecko_version(branch_name):
    global _gecko_versions
    if not _gecko_versions:
        version_file = os.path.join(os.path.dirname(__file__),
                                    "gecko_versions.json")
        _gecko_versions = json.load(open(version_file))
    return _gecko_versions[branch_name]

# Typical usage pattern:
#
#   set cfg = current_behavior
#   for (b in items_before(BRANCHES, 'gecko_version', N)):
#     set cfg = previous_behavior
#
def items_before(map, key, maxval):
    """
    yield all items from the dict 'map' where mapvalue[key] is present and less
    than 'maxval' (assume that anything missing a value is later than the
    threshold you're testing for.)
    """
    for k, v in map.items():
        value = v.get(key)
        if value and cmp(value, maxval) < 0:
            yield (k, v)

def setMainCommVersions(BRANCHES):
    # MERGE DAY
    BRANCHES['comm-release']['gecko_version'] = get_gecko_version("comm-release")
    BRANCHES['comm-beta']['gecko_version'] = get_gecko_version("comm-beta")
    BRANCHES['comm-esr']['gecko_version'] = get_gecko_version("comm-esr")
