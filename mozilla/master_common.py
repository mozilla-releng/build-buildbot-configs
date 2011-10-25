import time
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
    'mozilla-central': 1,
    'mozilla-aurora': 1,
    'mozilla-beta': 0,
    'mozilla-release': 0,
    'mozilla-1.9.2': 1,
    'try': 3,
    'addontester': 4,
    'addonbaselinetester': 4,
    'alder': 4,
    'ash': 4,
    'birch': 4,
    'cedar': 4,
    'elm': 4,
    'holly': 4,
    'larch': 4,
    'maple': 4,
    'oak': 4,
    'pine': 4,
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

        return priority, req_priority, submitted_at

    builders.sort(key=sortkey)
    log.msg("Sorted %i builders in %.2fs" % (len(builders), time.time() - s))
    return builders
c['prioritizeBuilders'] = prioritizeBuilders
