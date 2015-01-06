# buildbot-configs
This repository is a downstream read-only copy of:
http://hg.mozilla.org/build/buildbot-configs/

### Submitting changes
We do not support the github Pull Request workflow, since github is only a downstream
mirror for us. However, feel free to fork from us and make changes. Then, rather than
submitting a pull request, please create a patch for your changes (capture the output
of your changes using e.g. git diff) and attach the patch file to a Bugzilla bug,
created in the following component:
https://bugzilla.mozilla.org/enter_bug.cgi?product=Release%20Engineering&component=General%20Automation

This bug will get triaged by us.

### To run unit tests
```
pip install tox
tox
```

### To run tests in travis
Please note if you fork this repository and wish to run the tests in travis,
you will need to enable your github fork in travis. You can log in with your
github account, you do not need to set up a new one. To enable:
* https://travis-ci.org/profile

After enabling, you will need to push changes to your repo in order for a travis
job to be triggered.

### To match commits to upstream hg changesets
Add this following section to the .git/config file in your local clone:
```
[remote "mozilla"]
	url = git@github.com:mozilla/build-buildbot-configs
	fetch = +refs/heads/*:refs/remotes/mozilla/*
	fetch = +refs/notes/*:refs/notes/*
```
then to match a git commit to an upstream hg changeset:
```
git fetch mozilla
git log
```
This will produce output like this:
```
commit 2fd4885606c72d72a8d7554918b39d6d7c9bf308
Author: Peter Moore <pmoore@mozilla.com>
Date:   Mon Dec 22 13:46:05 2014 +0100

    Bug 1113255 - Generate FxOS pvtbuilds on m-c 3 hours earlier (at 0100 PT instead of 0400 PT),r=Bebe

Notes:
    Upstream source: https://hg.mozilla.org/build/buildbot-configs/rev/c5ee8731b724a5038b5af0818d3a19c70ad1338e

commit 666973f3778824ee67feab5c7f8198c55e402e1d
Author: Massimo Gervasini <mgervasini@mozilla.com>
Date:   Mon Dec 22 13:10:37 2014 +0100

    Bug 1113255 - Generate FxOS pvtbuilds on m-c at 1300,r=pmoore

Notes:
    Upstream source: https://hg.mozilla.org/build/buildbot-configs/rev/637b09eb1d144b2af42a0b72acfdc854db08aae6

commit 52f6363345c4fefb1d8396bdf069b63d5633d4b9
Author: Armen Zambrano Gasparnian <armenzg@mozilla.com>
Date:   Fri Dec 19 15:46:10 2014 -0500

    Bug 1112779 - Disable Mulet mochitest jobs on every tree except Try/Cedar. r=rail

Notes:
    Upstream source: https://hg.mozilla.org/build/buildbot-configs/rev/b545cad5b3cde80731be68b3a5a511e5684f3e43


```
This allows you to map a git commit SHA to an hg changeset SHA ("Upstream source").

### Related repositories

Please also see:
* https://github.com/mozilla/build-buildbotcustom/
* https://hg.mozilla.org/build/buildbot/ (not mirrored to github)

Happy contributing! =)
