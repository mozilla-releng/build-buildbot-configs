def getConfig(defaults, branch, value, default=None):
    return branch.get(value, defaults.get(value, default))

import buildbotcustom.changes.hgpoller
reload(buildbotcustom.changes.hgpoller)
from buildbotcustom.changes.hgpoller import HgAllLocalesPoller, HgPoller

def setupHGPollersFromBranches(defaults, branches, change_source, fixed_branch):
    # Figure out the unique pushlogs we should be polling
    
    sources = {}
    l10n = False 
    for name in branches.keys():
        branch = branches[name]
        hgurl = getConfig(defaults, branch, 'hgurl')
        if getConfig(defaults, branch, 'l10n'):
            l10n = True
        
        #Make sure the hg url doesn't have a trailing '/', we'll be adding one
        if hgurl[-1:] == '/':
            hgurl = hgurl[:-1]
        poll_branch = getConfig(defaults, branch, 'master_branch')
        for b in [poll_branch] + [getConfig(defaults, branch, 'mozilla_central_branch')] + getConfig(defaults, branch, 'add_poll_branches'):
            pushlogUrlOverride = '%s/%s/pushlog' % (hgurl, b),
            if not sources.get(b):
                sources[b] = pushlogUrlOverride

    for branch in sorted(sources.keys()):
        change_source.append(HgPoller(
            hgURL=hgurl,
            pushlogUrlOverride="%s/%s/pushlog" % (hgurl,branch),
            branch=branch,
            pollInterval=1*60
        ))

    if l10n:
        # XXX: 100% hard-coded, bad
        change_source.append(HgAllLocalesPoller(
            #XXX: picks the last seen hgurl, bad
            hgURL = "%s/" % hgurl,
            repositoryIndex = 'releases/l10n-mozilla-1.9.1',
            pollInterval=180,
        ))
