c = BuildmasterConfig = {}
c['projectName'] = "Firefox"
c['projectURL'] = "http://wiki.mozilla.org/Firefox"
c['logMaxSize'] = 50 * 1024 * 1024
c['changeHorizon'] = 100
c['logCompressionMethod'] = 'gz'
c['eventHorizon'] = 20
c['buildCacheSize'] = 10

c['status'] = []
c['slaves'] = []
c['builders'] = []
c['schedulers'] = []
c['change_source'] = []

