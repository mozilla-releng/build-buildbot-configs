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

# Give the release builders priority over other builders
def prioritizeBuilders(botmaster, builders):
    def sortkey(builder):
        builds = builder.getBuildable(1)
        if builds:
            # The builder that gets sorted first, gets run first, but the build
            # request priorities are in ascending order (higher priority gets
            # run next), so flip the sign of the priority so that higher
            # priorities sort to the front
            req_priority = -builds[0].priority
            submitted_at = builds[0].submittedAt
        else:
            req_priority = 0
            submitted_at = None

        if builder.builder_status.category.startswith('release'):
            priority = 0
        elif builder.builder_status.category.startswith('try'):
            priority = 2
        else:
            priority = 1

        return priority, req_priority, submitted_at
    builders.sort(key=sortkey)
    return builders
c['prioritizeBuilders'] = prioritizeBuilders

import passwords
reload(passwords)
if hasattr(passwords, 'PULSE_PASSWORD'):
    # Send pulse messages
    import re
    import buildbotcustom.status.pulse
    reload(buildbotcustom.status.pulse)
    from buildbotcustom.status.pulse import PulseStatus
    from mozillapulse.publishers import GenericPublisher
    from mozillapulse.config import PulseConfiguration
    c['status'].append(PulseStatus(
        GenericPublisher(PulseConfiguration(
            user=passwords.PULSE_USERNAME,
            password=passwords.PULSE_PASSWORD,
            ),
            exchange=passwords.PULSE_EXCHANGE),
        ignoreBuilders=[re.compile('.*shadow-central.*'), re.compile('fuzzer-.*')],
        send_logs=False,
        ))
