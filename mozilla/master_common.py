import time
import random
from twisted.python import log

c = BuildmasterConfig = {}
c['projectName'] = "Firefox"
c['projectURL'] = "http://wiki.mozilla.org/Firefox"
c['logMaxSize'] = 50 * 1024 * 1024
c['changeHorizon'] = None
c['logCompressionMethod'] = 'gz'
c['eventHorizon'] = 20
c['buildCacheSize'] = 10
c['changeCacheSize'] = 10000

c['status'] = []
c['slaves'] = []
c['builders'] = []
c['schedulers'] = []
c['change_source'] = []

# Builders from these branches are given custom priority, default is 2 for unlisted branches
BRANCH_PRIORITIES = {
    'mozilla-central': 3,
    'comm-central': 3,
    'mozilla-aurora': 3,
    'comm-aurora': 3,
    'mozilla-beta': 2,
    'comm-beta': 2,
    'mozilla-release': 0,
    'comm-release': 0,
    'mozilla-esr10': 1,
    'mozilla-esr17': 1,
    'comm-esr10': 1,
    'comm-esr17': 1,
    'try': 4,
    'try-comm-central': 4,
    'alder': 5,
    'ash': 5,
    'birch': 5,
    'cedar': 5,
    'elm': 5,
    'holly': 5,
    'larch': 5,
    'maple': 5,
    'oak': 5,
    'pine': 5,
}

# Give the release builders priority over other builders
def prioritizeBuilders(botmaster, builders):
    s = time.time()
    # Get the list pending builds, at most one per builder
    db = botmaster.db
    q = ("SELECT br.buildername, max(br.priority), min(br.submitted_at)"
            " FROM buildrequests AS br"
            " WHERE br.complete=0"
            " AND (br.claimed_at<?"
            "      OR (br.claimed_by_name=?"
            "          AND br.claimed_by_incarnation!=?))"
            " GROUP BY br.buildername ")
    requests = db.runQueryNow(db.quoteq(q),
            (time.time() - 3600, botmaster.master_name, botmaster.master_incarnation))

    # Filter out requests we're not running builders for
    allBuilderNames = set(builder.name for builder in builders)
    requests = filter(lambda request: request[0] in allBuilderNames, requests)

    # Turn into a dictionary keyed by buildername
    requests = dict( (request[0], request) for request in requests )

    # Remove builders we don't have requests for
    builders = filter(lambda builder: builder.name in requests, builders)

    # Our sorting function
    def sortkey(builder):
        request = requests[builder.name]
        req_priority = request[1]
        submitted_at = request[2]

        # Default priority is 2
        priority = 2
        if builder.builder_status.category.startswith('release'):
            priority = 0
        elif builder.properties and builder.properties.has_key('branch'):
            for branch, p in BRANCH_PRIORITIES.iteritems():
                if branch in builder.properties['branch']:
                    priority = p
                    break

        # Add some randomness here so that builders with the same priority,
        # req_priority, submitted_at get processed in a different order each
        # time
        return priority, req_priority, submitted_at, random.random()

    builders.sort(key=sortkey)
    log.msg("Sorted %i builders in %.2fs" % (len(builders), time.time() - s))
    return builders
c['prioritizeBuilders'] = prioritizeBuilders
