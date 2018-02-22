from copy import deepcopy
from master_common import items_before, setMainCommVersions, get_gecko_version


SLAVES = {
    'linux': ['sea-vm-linux32-%i' % x for x in range(1,7)],
    'linux64': ['sea-vm-linux64-%i' % x for x in [1]],
    'win32': ['sea-win32-%02i' % x for x in [1,2,3,4]] + #iX machines
             ['sea-vm-win32-%i' % x for x in range(1,5)],
    'win64': [],
    'macosx64': #['cb-sea-miniosx64-%02i' % x for x in [1,2,3]] +
                ['sea-mini-osx64-%i' % x for x in [3]],
    'mock': ['sea-hp-linux64-%i' % x for x in range(2,14)],
}


GLOBAL_VARS = {
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'hgurl': 'https://hg.mozilla.org/',
    'hghost': 'hg.mozilla.org',
    'config_subdir': 'seamonkey',
    'irc_bot_name': 'sea-build-bot', #?
    'irc_bot_channels': ['mozbot'], #?
    'objdir': 'objdir',
    'objdir_unittests': 'objdir',
    'stage_username': 'seabld',
    'stage_base_path': '/home/ftp/pub',
    'stage_group': 'seamonkey',
    'stage_ssh_key': 'seabld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_sea/',
    'symbol_server_post_upload_cmd': '/usr/local/bin/post-symbol-upload.py',
    'aus2_user': 'seabld',
    'aus2_ssh_key': 'seabld_dsa',
    'balrog_username': 'stage-seabld',
    'balrog_api_root': 'https://balrog-admin.stage.mozaws.net/api',
    'hg_username': 'seabld',
    'hg_ssh_key': '~seabld/.ssh/seabld_dsa',
    'graph_selector': '/server/collect.cgi',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'default_build_space': 5,
    'default_l10n_space': 3,
    'default_clobber_time': 24*7, # 1 week
    'unittest_suites': [
        ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
            'mochitest-a11y']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
    ],
    # Unittest suites to run directly in the unittest build cycle
    'unittest_exec_xpcshell_suites': False,
    'unittest_exec_reftest_suites': False,
    'unittest_exec_mochi_suites': False,
    'unittest_exec_mozmill_suites': False,
    'geriatric_masters': [],
    'geriatric_branches': {},
    'platforms': {
        'linux': {},
        'linux64': {},
        'win32': {},
        'macosx64': {},
        'linux-debug': {},
        'linux64-debug': {},
        'macosx64-debug': {},
        'win32-debug': {},
    },
    'pgo_strategy': None,
    'pgo_platforms': list(),
    'enable_shark': False,
    'enable_codecoverage': False,
    'enable_blocklist_update': False,
    'blocklist_update_on_closed_tree': False,
    'enable_nightly': True,
    'enable_valgrind': False,
    'enable_xulrunner': False,

    # if true, this branch will get bundled and uploaded to ftp.m.o for users
    # to download and thereby accelerate their cloning
    'enable_weekly_bundle': False,

    'hash_type': 'sha512',
    'create_snippet': False,
    'create_partial': False,
    'create_partial_l10n': False,
    'l10n_modules': [
            'suite', 'editor/ui',
            'netwerk', 'dom', 'toolkit',
            'security/manager',
            'sync/services',
            ],
    'use_old_updater': False,
    'idle_timeout': 60*60*12,     # 12 hours

    # staging/production-dependent settings - all is production for us
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'upload.seabld.productdelivery.prod.mozaws.net',
    'archive_server': 'archive.mozilla.org',
    'aus2_host': 'aus2-community.mozilla.org',
    'download_base_url': 'https://archive.mozilla.org/pub/seamonkey',
    'pip_server': 'http://pypi.pub.build.mozilla.org/pub',
    'graph_server': None,
    'build_tools_repo_path': 'users/Callek_gmail.com/tools',
    'all_locales_file': 'suite/locales/all-locales',
    # 'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://callek.net/always_clobber.php',
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning
    'talos_masters': [],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [('cb-seamonkey-linuxmaster-01.mozilla.org:9010', False, 5)],
    'weekly_tinderbox_tree': 'Testing',
    'l10n_tinderbox_tree': 'Mozilla-l10n',
    'tinderbox_tree': 'MozillaTest',
    'pgo_strategy': None,
    'enabled_products': ['seamonkey'],
    'tooltool_url_list': ['https://api.pub.build.mozilla.org/tooltool/'],
    'mock_packages_i686' : ['autoconf213', 'python', 'zip',
                            'mozilla-python27-mercurial-3.9.1-1.el6.x86_64',
                            'git-1.7.1-2.el6_0.1.i686', 'ccache',
                            'glibc-static.i686', 'libstdc++-static.i686', 'perl-Test-Simple', 'perl-Config-General',
                            'gtk2-devel.i686', 'libnotify-devel.i686', 'yasm',
                            'alsa-lib-devel.i686', 'libcurl-devel.i686',
                            'wireless-tools-devel.i686', 'libX11-devel.i686',
                            'libXt-devel.i686', 'mesa-libGL-devel.i686',
                            'gnome-vfs2-devel.i686', 'GConf2-devel.i686', 'wget',
                            'mpfr',  # required for system compiler
                            'xorg-x11-font*',  # fonts required for PGO
                            'imake',  # required for makedepend!?!
                            'gcc45_0moz3', 'gcc454_0moz1', 'gcc472_0moz1', 'gcc473_0moz1', 'yasm', 'ccache',  # <-- from releng repo
                            'valgrind', 'mozilla-python27-virtualenv',
                            'pulseaudio-libs-devel.i686',
                            'gstreamer-devel.i686', 'gstreamer-plugins-base-devel.i686',
                            # Packages already installed in the mock environment, as x86_64
                            # packages.
                            'glibc-devel.i686', 'libgcc.i686', 'libstdc++-devel.i686',
                            # yum likes to install .x86_64 -devel packages that satisfy .i686
                            # -devel packages dependencies. So manually install the dependencies
                            # of the above packages.
                            'ORBit2-devel.i686', 'atk-devel.i686', 'cairo-devel.i686',
                            'check-devel.i686', 'dbus-devel.i686', 'dbus-glib-devel.i686',
                            'fontconfig-devel.i686', 'glib2-devel.i686',
                            'hal-devel.i686', 'libICE-devel.i686', 'libIDL-devel.i686',
                            'libSM-devel.i686', 'libXau-devel.i686', 'libXcomposite-devel.i686',
                            'libXcursor-devel.i686', 'libXdamage-devel.i686', 'libXdmcp-devel.i686',
                            'libXext-devel.i686', 'libXfixes-devel.i686', 'libXft-devel.i686',
                            'libXi-devel.i686', 'libXinerama-devel.i686', 'libXrandr-devel.i686',
                            'libXrender-devel.i686', 'libXxf86vm-devel.i686', 'libdrm-devel.i686',
                            'libidn-devel.i686', 'libpng-devel.i686', 'libxcb-devel.i686',
                            'libxml2-devel.i686', 'pango-devel.i686', 'perl-devel.i686',
                            'pixman-devel.i686', 'zlib-devel.i686',
                            # Freetype packages need to be installed be version, because a newer
                            # version is available, but we don't want it for Firefox builds.
                            'freetype-2.3.11-6.el6_1.8.i686', 'freetype-devel-2.3.11-6.el6_1.8.i686',
                            'freetype-2.3.11-6.el6_1.8.x86_64',
                            # SeaMonkey needs these for update runs until Bug 1057920 is fixed.
                            'cvs', 'rsh',
                            ],
    'mock_packages_x86-64' : ['autoconf213', 'python', 'zip',
                            'mozilla-python27-mercurial-3.9.1-1.el6',
                            'git-1.7.9.4-2.el6', 'ccache',
                            'glibc-static', 'libstdc++-static', 'perl-Test-Simple', 'perl-Config-General',
                            'gtk2-devel', 'libnotify-devel', 'yasm',
                            'alsa-lib-devel', 'libcurl-devel',
                            'wireless-tools-devel', 'libX11-devel',
                            'libXt-devel', 'mesa-libGL-devel',
                            'gnome-vfs2-devel', 'GConf2-devel', 'wget',
                            'mpfr', # required for system compiler
                            'xorg-x11-font*', # fonts required for PGO
                            'imake', # required for makedepend!?!
                            'gcc45_0moz3', 'gcc473_0moz1', 'yasm', 'ccache', # <-- from releng repo
                            'valgrind', 'dbus-x11', 'mozilla-python27-virtualenv',
                            'pulseaudio-libs-devel',
                            'gstreamer-devel', 'gstreamer-plugins-base-devel',
                            'freetype-2.3.11-6.el6_1.8.x86_64',
                            'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                            # SeaMonkey needs these for update runs until Bug 1057920 is fixed.
                            'cvs', 'rsh', 'zlib', 'zlib-devel',
                            ],
}

GLOBAL_ENVS = {
  'MOZ_CRASHREPORTER_NO_REPORT': '1',
  'TINDERBOX_OUTPUT': '1',
  'MOZ_AUTOMATION': '1',
}

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']
SYMBOL_SERVER_POST_UPLOAD_CMD = GLOBAL_VARS['symbol_server_post_upload_cmd']
BUILDS_BEFORE_REBOOT = 1

PLATFORM_VARS = {
        'linux': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'src_mozconfig': 'suite/config/mozconfigs/linux32/nightly',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'build_space': 10,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_platform': 'linux',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'symbolpush.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'DISPLAY': ':2',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',

                # LD_LIBRARY_PATH needs to be set to properly run elfhack during build process (Bug 904485)
                'LD_LIBRARY_PATH': '/tools/gcc-4.5/lib',
            },
            'objdir': 'objdir',
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/linux32/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/linux32/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'],
            'tooltool_token': '/builds/tooltool.token',
            'balrog_credentials_file': '/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': False,
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64',
            'mock_packages': GLOBAL_VARS['mock_packages_i686'],
            'mock_copyin_files': [('/home/seabld/.ssh', '/home/mock_mozilla/.ssh'),
                                  ('/home/seabld/.hgrc', '/builds/.hgrc'),
                                  ('/tools/tooltool.py', '/builds/tooltool.py'),
                                  ('/builds/tooltool.token', '/builds/tooltool.token'),
                                  ('/builds/balrog.token', '/builds/balrog.token'),
                                  ('/builds/release-s3.credentials', '/builds/release-s3.credentials'),
                                  ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                                  ('/builds/google-api.key', '/builds/google-api.key')]
        },
        'linux64': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'src_mozconfig': 'suite/config/mozconfigs/linux64/nightly',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'build_space': 10,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_platform': 'linux64',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'symbolpush.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/seabld/.ssh/seabld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'DISPLAY': ':2',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',

                # LD_LIBRARY_PATH needs to be set to properly run elfhack during build process (Bug 904485)
                'LD_LIBRARY_PATH': '/tools/gcc-4.5/lib64',
            },
            'objdir': 'objdir',
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/linux64/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/linux64/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'], 
            'tooltool_token': '/builds/tooltool.token',
            'balrog_credentials_file': '/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': False,
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64',
            'mock_packages': GLOBAL_VARS['mock_packages_x86-64'],
            'mock_copyin_files': [('/home/seabld/.ssh', '/home/mock_mozilla/.ssh'),
                                  ('/home/seabld/.hgrc', '/builds/.hgrc'),
                                  ('/tools/tooltool.py', '/builds/tooltool.py'),
                                  ('/builds/tooltool.token', '/builds/tooltool.token'),
                                  ('/builds/release-s3.credentials', '/builds/release-s3.credentials'),
                                  ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                                  ('/builds/google-api.key', '/builds/google-api.key')]
        },
        'macosx64': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'OS X 10.6 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'src_mozconfig': 'suite/config/mozconfigs/macosx64/nightly',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'build_space': 8,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['macosx64'],
            'platform_objdir': OBJDIR,
            'stage_platform': 'macosx64',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_ccache': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'symbolpush.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/Users/seabld/.ssh/seabld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'macosx64',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'LC_ALL': 'C',
                'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/macosx64/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/macosx64/releng.manifest',
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'tooltool_script': ['/tools/tooltool.py'],
            'tooltool_token': '/builds/tooltool.token',
            'balrog_credentials_file': '/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': True,
            'stage_product': 'seamonkey',
            'enable_pymake': False,
        },
        'win32': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'src_mozconfig': 'suite/config/mozconfigs/win32/nightly',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'build_space': 9,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'stage_platform': 'win32',
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'symbolpush.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'PYTHON': 'python2.7.exe',
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
                # Source server support, bug 506702
                'PDBSTR_PATH': 'c:/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}nsis-2.46u;${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/win32/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/win32/releng.manifest',
            'tooltool_script': ['python2.7', 'd:/mozilla-build/tooltool.py'],
            'tooltool_token': 'e:/builds/tooltool.token',
            'balrog_credentials_file': 'c:/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': True,
        },
        'win64': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'WINNT 6.1 x86-64 %(branch)s',
            'mozconfig': 'win64/%(branch)s/nightly',
            'src_mozconfig': 'suite/config/mozconfigs/win64/nightly',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['win64'],
            'platform_objdir': OBJDIR,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'stage_platform': 'win64',
            'update_platform': 'WINNT_x86-64-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': 'symbolpush.mozilla.org',
                'SYMBOL_SERVER_USER': 'seabld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'PYTHON': 'python2.7.exe',
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/seabld/.ssh/seabld_dsa",
                # Source server support, bug 506702
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}nsis-3.0b1;${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/win64/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_script': ['python2.7', 'd:/mozilla-build/tooltool.py'],
            'tooltool_token': 'e:/builds/tooltool.token',
            'balrog_credentials_file': 'c:/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': True,
        },
        'linux-debug': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'src_mozconfig': 'suite/config/mozconfigs/linux32/debug',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 7,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_platform': 'linux-debug',
            'enable_ccache': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_unittests': True,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/linux32/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/linux32/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'],
            'tooltool_token': '/builds/tooltool.token',
            'balrog_credentials_file': '/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': False,
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64',
            'mock_packages': GLOBAL_VARS['mock_packages_i686'],
            'mock_copyin_files': [('/home/seabld/.ssh', '/home/mock_mozilla/.ssh'),
                                  ('/home/seabld/.hgrc', '/builds/.hgrc'),
                                  ('/tools/tooltool.py', '/builds/tooltool.py'),
                                  ('/builds/tooltool.token', '/builds/tooltool.token'),
                                  ('/builds/balrog.token', '/builds/balrog.token'),
                                  ('/builds/release-s3.credentials', '/builds/release-s3.credentials'),
                                  ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                                  ('/builds/google-api.key', '/builds/google-api.key')]
        },
        'linux64-debug': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'src_mozconfig': 'suite/config/mozconfigs/linux64/debug',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'build_space': 10,
            'download_symbols': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_platform': 'linux64-debug',
            'enable_ccache': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'DISPLAY': ':2',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
                # LD_LIBRARY_PATH needs to be set to properly run elfhack during build process (Bug 904485)
                'LD_LIBRARY_PATH': '/tools/gcc-4.5/lib64',
            },
            'objdir': 'objdir',
            'enable_unittests': True,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/linux64/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/linux64/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'], 
            'tooltool_token': '/builds/tooltool.token',
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': False,
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64',
            'mock_packages': GLOBAL_VARS['mock_packages_x86-64'],
            'mock_copyin_files': [('/home/seabld/.ssh', '/home/mock_mozilla/.ssh'),
                                  ('/home/seabld/.hgrc', '/builds/.hgrc'),
                                  ('/tools/tooltool.py', '/builds/tooltool.py'),
                                  ('/builds/tooltool.token', '/builds/tooltool.token'),
                                  ('/builds/release-s3.credentials', '/builds/release-s3.credentials'),
                                  ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                                  ('/builds/google-api.key', '/builds/google-api.key')]
        },
        'macosx64-debug': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'OS X 10.6 %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'src_mozconfig': 'suite/config/mozconfigs/macosx64/debug',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 5,
            'slaves': SLAVES['macosx64'],
            'platform_objdir': OBJDIR,
            'stage_platform': 'macosx64-debug',
            'enable_ccache': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
            },
            'enable_unittests': True,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/macosx64/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/macosx64/releng.manifest',
            'tooltool_script': ['/tools/tooltool.py'],
            'tooltool_token': '/builds/tooltool.token',
            'balrog_credentials_file': '/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': False,
        },
        'win32-debug': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'src_mozconfig': 'suite/config/mozconfigs/win32/debug',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 8,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'enable_shared_checkouts': True,
            'stage_platform': 'win32-debug',
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}nsis-2.46u;${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
                'PYTHON': 'python2.7.exe',
            },
            'enable_unittests': True,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/win32/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/win32/releng.manifest',
            'tooltool_script': ['python2.7', 'd:/mozilla-build/tooltool.py'],
            'tooltool_token': 'e:/builds/tooltool.token',
            'balrog_credentials_file': 'c:/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': True,
        },
        'win64-debug': {
            'product_name': 'seamonkey',
            'app_name': 'suite',
            'brand_name': 'SeaMonkey',
            'base_name': 'WINNT 6.1 x86-64 %(branch)s leak test',
            'mozconfig': 'win64/%(branch)s/debug',
            'src_mozconfig': 'suite/config/mozconfigs/win64/debug',
            'profiled_build': False,
            'builds_before_reboot': BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 9,
            'slaves': SLAVES['win64'],
            'platform_objdir': OBJDIR,
            'enable_shared_checkouts': True,
            'stage_platform': 'win64-debug',
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}nsis-3.0b1;${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
                'PYTHON': 'python2.7.exe',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'tooltool_manifest_src': 'suite/config/tooltool-manifests/win64/releng.manifest',
            'test_tooltool_manifest_src': 'testing/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_script': ['python2.7', 'd:/mozilla-build/tooltool.py'],
            'tooltool_token': 'e:/builds/tooltool.token',
            'balrog_credentials_file': 'c:/builds/balrog.token',
            'balrog_submitter_extra_args': [],
            'balrog_submit': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'stage_product': 'seamonkey',
            'enable_pymake': True,
        },
}

for platform in PLATFORM_VARS.values():
  if 'env' not in platform:
    platform['env'] = deepcopy(GLOBAL_ENVS)
  else:
    platform['env'].update((k, v) for k, v in GLOBAL_ENVS.items() if k not in platform['env'])

# All branches that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'comm-central-trunk': {},
    'comm-beta': {},
    'comm-esr': {},
    'comm-release': {},
}

setMainCommVersions(BRANCHES)

# Set the COMM ESR version
COMM_ESR_VER = BRANCHES["comm-esr"]["gecko_version"]

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

######## comm-central-trunk
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-central-trunk']['repo_path'] = 'comm-central'
BRANCHES['comm-central-trunk']['mozilla_repo_path'] = 'mozilla-central'
BRANCHES['comm-central-trunk']['l10n_repo_path'] = 'l10n-central'
BRANCHES['comm-central-trunk']['start_hour'] = [0]
BRANCHES['comm-central-trunk']['start_minute'] = [30]
BRANCHES['comm-central-trunk']['enable_mac_a11y'] = True
BRANCHES['comm-central-trunk']['unittest_build_space'] = 6
BRANCHES['comm-central-trunk']['enable_blocklist_update'] = True
BRANCHES['comm-central-trunk']['blocklist_update_on_closed_tree'] = True
# And code coverage
BRANCHES['comm-central-trunk']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-central-trunk']['enable_l10n'] = True
BRANCHES['comm-central-trunk']['enable_l10n_onchange'] = True
BRANCHES['comm-central-trunk']['l10nNightlyUpdate'] = True
BRANCHES['comm-central-trunk']['l10n_platforms'] = ['linux', 'win32', 'macosx64', 'win64']
BRANCHES['comm-central-trunk']['l10nDatedDirs'] = True
BRANCHES['comm-central-trunk']['l10n_tree'] = 'sea22x'
BRANCHES['comm-central-trunk']['mozilla_srcdir'] = 'mozilla'
#make sure it has an ending slash
BRANCHES['comm-central-trunk']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-central-trunk-l10n/'
BRANCHES['comm-central-trunk']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-central-trunk'
BRANCHES['comm-central-trunk']['allLocalesFile'] = 'suite/locales/all-locales'
BRANCHES['comm-central-trunk']['localesURL'] = \
    '%s/comm-central/raw-file/tip/suite/locales/all-locales' % (GLOBAL_VARS['hgurl'])
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-trunk']['create_snippet'] = True
BRANCHES['comm-central-trunk']['update_channel'] = 'nightly'
BRANCHES['comm-central-trunk']['create_partial'] = True
BRANCHES['comm-central-trunk']['create_partial_l10n'] = True
BRANCHES['comm-central-trunk']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/SeaMonkey/comm-central-trunk'
BRANCHES['comm-central-trunk']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/SeaMonkey/comm-central-trunk'
# staging/production-dependent settings - all is production for us
BRANCHES['comm-central-trunk']['tinderbox_tree'] = 'SeaMonkey'
BRANCHES['comm-central-trunk']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey'

######## comm-beta
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-beta']['repo_path'] = 'releases/comm-beta'
BRANCHES['comm-beta']['mozilla_repo_path'] = 'releases/mozilla-beta'
BRANCHES['comm-beta']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['comm-beta']['enable_nightly'] = False
BRANCHES['comm-beta']['start_hour'] = [0]
BRANCHES['comm-beta']['start_minute'] = [30]
BRANCHES['comm-beta']['enable_mac_a11y'] = True
BRANCHES['comm-beta']['unittest_build_space'] = 6
BRANCHES['comm-beta']['enable_blocklist_update'] = False # for now
BRANCHES['comm-beta']['blocklist_update_on_closed_tree'] = True
# And code coverage
BRANCHES['comm-beta']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-beta']['enable_l10n'] = False
BRANCHES['comm-beta']['enable_l10n_onchange'] = True
BRANCHES['comm-beta']['l10nNightlyUpdate'] = True
BRANCHES['comm-beta']['l10n_platforms'] = ['linux', 'win32', 'macosx64']
BRANCHES['comm-beta']['l10nDatedDirs'] = True
BRANCHES['comm-beta']['l10n_tree'] = 'sea_beta'
BRANCHES['comm-beta']['mozilla_srcdir'] = 'mozilla'
#make sure it has an ending slash
BRANCHES['comm-beta']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-beta-l10n/'
BRANCHES['comm-beta']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-beta'
BRANCHES['comm-beta']['allLocalesFile'] = 'suite/locales/all-locales'
BRANCHES['comm-beta']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/seamonkey-production/seamonkey/l10n/all-locales.comm-beta' % (GLOBAL_VARS['hgurl'])
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-beta']['create_snippet'] = True
BRANCHES['comm-beta']['update_channel'] = 'beta'
BRANCHES['comm-beta']['create_partial'] = True
BRANCHES['comm-beta']['create_partial_l10n'] = True
BRANCHES['comm-beta']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/SeaMonkey/comm-beta'
BRANCHES['comm-beta']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/SeaMonkey/comm-beta'
# staging/production-dependent settings - all is production for us
BRANCHES['comm-beta']['tinderbox_tree'] = 'SeaMonkey-Beta'
BRANCHES['comm-beta']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey-Beta'

######## comm-esr [ currently: 52 ]
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-esr']['repo_path'] = 'releases/comm-esr%d' % COMM_ESR_VER
BRANCHES['comm-esr']['mozilla_repo_path'] = 'releases/mozilla-esr%d' % COMM_ESR_VER
BRANCHES['comm-esr']['l10n_repo_path'] = 'releases/l10n/mozilla-esr%d' % COMM_ESR_VER
BRANCHES['comm-esr']['enable_nightly'] = False
BRANCHES['comm-esr']['start_hour'] = [0]
BRANCHES['comm-esr']['start_minute'] = [30]
BRANCHES['comm-esr']['enable_mac_a11y'] = True
BRANCHES['comm-esr']['unittest_build_space'] = 6
BRANCHES['comm-esr']['enable_blocklist_update'] = False # for now
BRANCHES['comm-esr']['blocklist_update_on_closed_tree'] = True
# And code coverage
BRANCHES['comm-esr']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-esr']['enable_l10n'] = False
BRANCHES['comm-esr']['enable_l10n_onchange'] = True
BRANCHES['comm-esr']['l10nNightlyUpdate'] = True
BRANCHES['comm-esr']['l10n_platforms'] = ['linux', 'win32', 'macosx64']
BRANCHES['comm-esr']['l10nDatedDirs'] = True
BRANCHES['comm-esr']['l10n_tree'] = 'sea_esr'
BRANCHES['comm-esr']['mozilla_srcdir'] = 'mozilla'
#make sure it has an ending slash
BRANCHES['comm-esr']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-esr%d-l10n/' % COMM_ESR_VER
BRANCHES['comm-esr']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-esr%d' % COMM_ESR_VER
BRANCHES['comm-esr']['allLocalesFile'] = 'suite/locales/all-locales'
BRANCHES['comm-esr']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/seamonkey-production/seamonkey/l10n/all-locales.comm-esr' % (GLOBAL_VARS['hgurl'])
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-esr']['create_snippet'] = True
BRANCHES['comm-esr']['update_channel'] = 'release'
BRANCHES['comm-esr']['create_partial'] = True
BRANCHES['comm-esr']['create_partial_l10n'] = True
BRANCHES['comm-esr']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/SeaMonkey/comm-esr%d'
BRANCHES['comm-esr']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/SeaMonkey/comm-esr%d'
# staging/production-dependent settings - all is production for us
BRANCHES['comm-esr']['tinderbox_tree'] = 'SeaMonkey-Esr%d' % COMM_ESR_VER
BRANCHES['comm-esr']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey-Esr%d' % COMM_ESR_VER

######## comm-release
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-release']['repo_path'] = 'releases/comm-release'
BRANCHES['comm-release']['mozilla_repo_path'] = 'releases/mozilla-release'
BRANCHES['comm-release']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['comm-release']['enable_nightly'] = False
BRANCHES['comm-release']['start_hour'] = [0]
BRANCHES['comm-release']['start_minute'] = [30]
BRANCHES['comm-release']['enable_mac_a11y'] = True
BRANCHES['comm-release']['unittest_build_space'] = 6
BRANCHES['comm-release']['enable_blocklist_update'] = False # for now
BRANCHES['comm-release']['blocklist_update_on_closed_tree'] = True
# And code coverage
BRANCHES['comm-release']['enable_codecoverage'] = False
# L10n configuration
BRANCHES['comm-release']['enable_l10n'] = False
BRANCHES['comm-release']['enable_l10n_onchange'] = True
BRANCHES['comm-release']['l10nNightlyUpdate'] = True
BRANCHES['comm-release']['l10n_platforms'] = ['linux', 'win32', 'macosx64']
BRANCHES['comm-release']['l10nDatedDirs'] = True
BRANCHES['comm-release']['l10n_tree'] = 'sea_release'
BRANCHES['comm-release']['mozilla_srcdir'] = 'mozilla'
#make sure it has an ending slash
BRANCHES['comm-release']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/seamonkey/nightly/latest-comm-release-l10n/'
BRANCHES['comm-release']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-release'
BRANCHES['comm-release']['allLocalesFile'] = 'suite/locales/all-locales'
BRANCHES['comm-release']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/seamonkey-production/seamonkey/l10n/all-locales.comm-release' % (GLOBAL_VARS['hgurl'])
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-release']['create_snippet'] = True
BRANCHES['comm-release']['update_channel'] = 'release'
BRANCHES['comm-release']['create_partial'] = True
BRANCHES['comm-release']['create_partial_l10n'] = True
BRANCHES['comm-release']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/SeaMonkey/comm-release'
BRANCHES['comm-release']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/SeaMonkey/comm-release'
# staging/production-dependent settings - all is production for us
BRANCHES['comm-release']['tinderbox_tree'] = 'SeaMonkey-Release'
BRANCHES['comm-release']['packaged_unittest_tinderbox_tree'] = 'SeaMonkey-Release'

# Bug 1322402 - mac universal builds dropped at 53, keep using the universal mozconfig and objdir before then
for name, branch in items_before(BRANCHES, 'gecko_version', 53):
    if 'macosx64' in branch['platforms']:
        branch['platforms']['macosx64']['src_mozconfig'] = 'suite/config/mozconfigs/macosx-universal/nightly'
        branch['platforms']['macosx64']['platform_objdir'] = '%s/i386' % OBJDIR

# Bug 1352820 - Set the RelBranch for ESR builds
for branch in BRANCHES:
    if branch == 'comm-esr':
        use_relbranch = 'THUNDERBIRD_52_VERBRANCH'
    else:
        use_relbranch = 'default'
    BRANCHES[branch]['mozilla_relbranch'] = use_relbranch
