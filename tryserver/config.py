CVSROOT      = ":ext:trybld@cvs.mozilla.org:/cvsroot"
OBJDIR       = "objdir"
PKG_BASENAME = "firefox-try"
SCP_STRING   = "trybld@build.mozilla.org:/builds/tryserver"
TALOS_TRY_MASTER = "qm-rhel02.mozilla.org:9985"
PACKAGE_URL  = "http://build.mozilla.org/tryserver-builds/%(uploadpath)s"
WIN32_ENVIRONMENT = {
    'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': 'obj-firefox',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'SYMBOL_SERVER_HOST': 'build.mozilla.org',
    'SYMBOL_SERVER_USER': 'trybld',
    'SYMBOL_SERVER_PATH': '/symbols/windows',
    'SYMBOL_SERVER_SSH_KEY': '$ENV{HOME}/.ssh/id_dsa',
    'NO_FAIL_ON_TEST_ERRORS': '1'   
}
