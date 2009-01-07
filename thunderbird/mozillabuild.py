def getConfig(defaults, branch, value, default=None):
    return branch.get(value, defaults.get(value, default))

import buildbotcustom.changes.hgpoller
reload(buildbotcustom.changes.hgpoller)
from buildbotcustom.changes.hgpoller import HgPoller

def setupHGPollersFromBranches(defaults, branches, change_source, fixed_branch):
    # Figure out the unique pushlogs we should be polling
    
    sources = {}
    
    for name in branches.keys():
        branch = branches[name]
        hgurl = getConfig(defaults, branch, 'hgurl')
        poll_branch = getConfig(defaults, branch, 'master_branch')
        for b in [poll_branch] + [getConfig(defaults, branch, 'mozilla_central_branch')] + getConfig(defaults, branch, 'add_poll_branches'):
            pushlogUrlOverride = '%s/%s/pushlog' % (hgurl, b),
            if not sources.get(b):
                sources[b] = pushlogUrlOverride

    for branch in sources.keys():
        change_source.append(HgPoller(
            hgURL=hgurl,
            pushlogUrlOverride="%s/%s/pushlog" % (hgurl,branch),
            branch=fixed_branch,
            pollInterval=1*60
        ))
