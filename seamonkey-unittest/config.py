HGURL = 'http://hg.mozilla.org/'
# for chatzilla/venkman
CVSROOT = ':ext:seabld@cvs.mozilla.org:/cvsroot'
ADD_POLL_BRANCH = 'mozilla-central'
CONFIG_REPO_URL = 'http://hg.mozilla.org/build/buildbot-configs'
CONFIG_SUBDIR = 'seamonkey-unittest'
OBJDIR = 'objdir'


# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-central': {}
}

######## seamonkey-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}
BRANCHES['comm-central']['platforms']['linux']['name'] = 'Linux comm-central dep unit test'
BRANCHES['comm-central']['platforms']['win32']['name'] = 'Win2k3 comm-central dep unit test'
BRANCHES['comm-central']['platforms']['macosx']['name'] = 'MacOSX 10.4 comm-central dep unit test'
BRANCHES['comm-central']['tinderbox_tree'] = 'SeaMonkey'
BRANCHES['comm-central']['platforms']['linux']['mochitest_leakthreshold'] = '143792'
BRANCHES['comm-central']['platforms']['win32']['mochitest_leakthreshold'] = '21313'
BRANCHES['comm-central']['platforms']['macosx']['mochitest_leakthreshold'] = '21320'
BRANCHES['comm-central']['platforms']['linux']['mochichrome_leakthreshold'] = '8380'
BRANCHES['comm-central']['platforms']['win32']['mochichrome_leakthreshold'] = '8345'
BRANCHES['comm-central']['platforms']['macosx']['mochichrome_leakthreshold'] = '8472'
BRANCHES['comm-central']['platforms']['linux']['mochibrowser_leakthreshold'] = '0'
BRANCHES['comm-central']['platforms']['win32']['mochibrowser_leakthreshold'] = '0'
BRANCHES['comm-central']['platforms']['macosx']['mochibrowser_leakthreshold'] = '0'
BRANCHES['comm-central']['platforms']['linux']['slaves'] = [
    'cn-sea-qm-centos5-01'
]
BRANCHES['comm-central']['platforms']['win32']['slaves'] = [
    'cn-sea-qm-win2k3-01'
]
BRANCHES['comm-central']['platforms']['macosx']['slaves'] = [
    'cb-sea-miniosx01'
]
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central']['platforms']['linux']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1'
}
BRANCHES['comm-central']['platforms']['win32']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1'
}
BRANCHES['comm-central']['platforms']['macosx']['env'] = {
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1'
}
