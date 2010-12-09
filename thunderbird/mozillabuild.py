def getConfig(defaults, branch, value, default=None):
    return branch.get(value, defaults.get(value, default))

import buildbotcustom.changes.hgpoller
from buildbotcustom.changes.hgpoller import HgAllLocalesPoller, HgPoller

def setupHGPollersFromBranches(defaults, branches, change_source):
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
        poll_branch = getConfig(defaults, branch, 'hg_branch')
        for b in [poll_branch] + [getConfig(defaults, branch, 'mozilla_central_branch')] + getConfig(defaults, branch, 'add_poll_branches'):
            if not sources.get(poll_branch):
                sources[poll_branch] = {}
            sources[poll_branch][b] = 1

    for branch in sorted(sources.keys()):
        for poll in sorted(sources[branch].keys()):
            pushlog = "%s/%s/json-pushes?full=1" % (hgurl, poll)
            change_source.append(HgPoller(
                hgURL="%s/" % hgurl,
                pushlogUrlOverride=pushlog,
                branch=branch,
                pollInterval=1*60
            ))
        
from buildbot.steps.shell import ShellCommand, WithProperties
def uploadUpdateSnippet(f, aus, platform):
    full_upload_dir = '%s/%s/%%(buildid)s/en-US' % \
        ( aus['base_upload_dir'],
          platform['update_platform'])

    f.addStep(ShellCommand(
        name='create aus2 upload dir',
        command=['ssh', '-l', aus['user'], aus['host'],
             WithProperties('mkdir -p %s' % full_upload_dir)],
        description=['create', 'aus2', 'upload', 'dir'],
        haltOnFailure=False,
        flunkOnFailure=False,
    ))

    f.addStep(ShellCommand(
        name='upload complete snippet',
        command=['scp', '-o', 'User=%s' % aus['user'],
             'dist/update/complete.update.snippet',
             WithProperties('%s:%s/complete.txt' % \
               (aus['host'], full_upload_dir))],
        workdir='build/%s/mozilla' % platform['platform_objdir'],
        description=['upload', 'complete', 'snippet'],
        haltOnFailure=False,
        flunkOnFailure=False,
    ))
    
