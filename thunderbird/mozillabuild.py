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
            pushlogUrlOverride = '%s/%s/pushlog' % (hgurl, b),
            if not sources.get(b):
                sources[b] = pushlogUrlOverride

    for branch in sorted(sources.keys()):
        change_source.append(HgPoller(
            hgURL="%s/" % hgurl,
            pushlogUrlOverride="%s/%s/pushlog" % (hgurl,branch),
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
    
