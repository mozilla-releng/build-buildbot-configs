from copy import deepcopy

from config import GLOBAL_VARS, PLATFORM_VARS

import thunderbird_project_branches
reload(thunderbird_project_branches)
from thunderbird_project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

# Note that thunderbird_localconfig.py is symlinked to one of: thunderbird_{production,staging}_config.py
import thunderbird_localconfig
reload(thunderbird_localconfig)

# Can't reload this one because it gets reloaded in another file
from localconfig import SLAVES, TRY_SLAVES

import master_common
reload(master_common)
from master_common import setMainCommVersions, items_at_least, items_before

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
PLATFORM_VARS = deepcopy(PLATFORM_VARS)

GLOBAL_VARS.update(thunderbird_localconfig.GLOBAL_VARS.copy())
GLOBAL_VARS.update({
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'objdir': 'objdir-tb',
    'objdir_unittests': 'objdir',
    'mozilla_srcdir': 'mozilla',
    'stage_username': 'tbirdbld',
    'stage_group': None,
    'stage_ssh_key': 'tbirdbld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_tbrd/',
    'hg_username': 'tbirdbld',
    'hg_ssh_key': '~cltbld/.ssh/tbirdbld_dsa',
    'unittest_suites': [
        ('xpcshell', ['xpcshell']),
        ('mozmill', ['mozmill']),
    ],
    'platforms': {
        'linux': {},
        'linux64': {},
        'win32': {},
        'win64': {},
        'macosx64': {},
        'linux64-av': {},
        'linux-debug': {},
        'linux64-debug': {},
        'macosx64-debug': {},
        'win32-debug': {},
    },
    'pgo_platforms': list(),
    'pgo_strategy': None,
    'periodic_start_hours': range(0, 24, 6),
    'product_name': 'thunderbird', # Not valid for mobile builds
    'app_name': 'mail',     # Not valid for mobile builds
    'brand_name': 'Daily', # Not valid for mobile builds
    'enable_blocklist_update': False,
    'enable_hsts_update': False,
    'enable_hpkp_update': False,
    'file_update_on_closed_tree': False,
    'file_update_set_approval': True,
    'use_ftp_for_xpcshell': True,
    'enable_nightly': True,
    'enable_perproduct_builds': True,
    'enabled_products': ['thunderbird'],

    'hash_type': 'sha512',
    'updates_enabled': False,
    'create_partial': False,
    'create_partial_l10n': False,
    'l10n_modules': [
            'mail',
            'editor',
            'other-licenses/branding/thunderbird',
            'netwerk',
            'dom',
            'toolkit',
            'security/manager',
        ],
    'default_l10n_space': 4,
    'scratchbox_path': '/builds/scratchbox/moz_scratchbox',
    'scratchbox_home': '/scratchbox/users/cltbld/home/cltbld',
    'use_old_updater': False,
})

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
builder_prefix = "TB "

GLOBAL_ENV = {
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_AUTOMATION': '1',
}

PLATFORM_VARS = {
        'linux': {
            'product_name': 'thunderbird',
            'unittest_platform': 'linux-opt',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'src_mozconfig': 'mail/config/mozconfigs/linux32/nightly',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'linux',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': None,
            'test_pretty_names': False,
            'l10n_check_test': False,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/linux32/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'],
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64',
            'mock_packages': \
                       ['autoconf213', 'python', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
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
                        # gtk3 neeeded for update verify step
                        'tooltool-gtk3-1-1.18bc52b0599b1308b667e282abb45f47597bfc98a5140cfcab8da71dacf89dd76d0dee22a04ce26fe7ad1f04e2d6596991f9e5b01fd2aaaab5542965f596b0e6.i686',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
            ],
        },
        'linux64': {
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'product_name': 'thunderbird',
            'unittest_platform': 'linux64-opt',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'src_mozconfig': 'mail/config/mozconfigs/linux64/nightly',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'linux64',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': None,
            'test_pretty_names': False,
            'l10n_check_test': False,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/linux64/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'],
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64',
            'mock_packages': \
                       ['autoconf213', 'python', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                        'glibc-static', 'libstdc++-static', 'perl-Test-Simple', 'perl-Config-General',
                        'gtk2-devel', 'libnotify-devel', 'yasm',
                        'alsa-lib-devel', 'libcurl-devel',
                        'wireless-tools-devel', 'libX11-devel',
                        'libXt-devel', 'mesa-libGL-devel',
                        'gnome-vfs2-devel', 'GConf2-devel', 'wget',
                        'mpfr', # required for system compiler
                        'xorg-x11-font*', # fonts required for PGO
                        'imake', # required for makedepend!?!
                        'gcc45_0moz3', 'gcc454_0moz1', 'gcc472_0moz1', 'gcc473_0moz1', 'yasm', 'ccache', # <-- from releng repo
                        'pulseaudio-libs-devel',
                        'gstreamer-devel', 'gstreamer-plugins-base-devel',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                        # gtk3 neeeded for update verify step
                        'tooltool-gtk3-1-1.3915f8ec396c56a8a92e6f9695b70f09ce9d1582359d1258e37e3fd43a143bc974410e4cfc27f500e095f34a8956206e0ebf799b7287f0f38def0d5e34ed71c9.x86_64',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
            ],
        },
        'linux64-av': {
            'product_name': 'thunderbird',
            'mozharness_python': '/tools/buildbot/bin/python',
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'use_mock': False,
            'stage_product': None,
            'slaves': SLAVES['linux64-av'],
        },
        'macosx64': {
            'product_name': 'thunderbird',
            'unittest_platform': 'macosx64-opt',
            'app_name': 'mail',
            'base_name': builder_prefix + 'OS X 10.7 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'src_mozconfig': 'mail/config/mozconfigs/macosx64/nightly',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'macosx64',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'LC_ALL': 'C',
                'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'test_pretty_names': False,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/macosx64/releng.manifest',
            'enable_ccache': True,
        },
        'win32': {
            'product_name': 'thunderbird',
            'unittest_platform': 'win32-opt',
            'app_name': 'mail',
            'base_name': builder_prefix + 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'src_mozconfig': 'mail/config/mozconfigs/win32/nightly',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'slaves': SLAVES['win64-rev2'],
            'l10n_slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'win32',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'PDBSTR_PATH': 'C:/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'test_pretty_names': False,
            'l10n_check_test': False,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/win32/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'win64': {
            'product_name': 'thunderbird',
            'unittest_platform': 'win64-opt',
            'app_name': 'mail',
            'base_name': builder_prefix + 'WINNT 6.1 x86-64 %(branch)s',
            'src_mozconfig': 'mail/config/mozconfigs/win64/nightly',
            'mozconfig': 'win64/%(branch)s/nightly',
            'profiled_build': True,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'try_by_default': False,
            'slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'win64',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86_64-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'PDBSTR_PATH': 'C:/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'test_pretty_names': True,
            'l10n_check_test': False,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'linux-debug': {
            'enable_nightly': False,
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'src_mozconfig': 'mail/config/mozconfigs/linux32/debug',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 10,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'linux-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/linux32/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'],
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64',
            'mock_packages': \
                       ['autoconf213', 'python', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                        'glibc-static.i686', 'libstdc++-static.i686',
                        'perl-Test-Simple', 'perl-Config-General',
                        'gtk2-devel.i686', 'libnotify-devel.i686', 'yasm',
                        'alsa-lib-devel.i686', 'libcurl-devel.i686',
                        'wireless-tools-devel.i686', 'libX11-devel.i686',
                        'libXt-devel.i686', 'mesa-libGL-devel.i686',
                        'gnome-vfs2-devel.i686', 'GConf2-devel.i686', 'wget',
                        'mpfr',  # required for system compiler
                        'xorg-x11-font*',  # fonts required for PGO
                        'imake',  # required for makedepend!?!
                        'gcc45_0moz3', 'gcc454_0moz1', 'gcc472_0moz1', 'gcc473_0moz1', 'yasm', 'ccache',  # <-- from releng repj
                        'pulseaudio-libs-devel.i686',
                        'gstreamer-devel.i686', 'gstreamer-plugins-base-devel.i686',
                        # Packages already installed in the mock environment,
                        # as x86_64 packages.
                        'glibc-devel.i686', 'libgcc.i686', 'libstdc++-devel.i686',
                        # yum likes to install .x86_64 -devel packages that satisfy .i686
                        # -devel packages dependencies. So manually install the
                        # dependencies of the above packages.
                        'ORBit2-devel.i686', 'atk-devel.i686', 'cairo-devel.i686',
                        'check-devel.i686', 'dbus-devel.i686', 'dbus-glib-devel.i686',
                        'fontconfig-devel.i686', 'glib2-devel.i686',
                        'hal-devel.i686', 'libICE-devel.i686', 'libIDL-devel.i686',
                        'libSM-devel.i686', 'libXau-devel.i686', 'libXcomposite-devel.i686',
                        'libXcursor-devel.i686', 'libXdamage-devel.i686',
                        'libXdmcp-devel.i686', 'libXext-devel.i686',
                        'libXfixes-devel.i686', 'libXft-devel.i686',
                        'libXi-devel.i686', 'libXinerama-devel.i686', 'libXrandr-devel.i686',
                        'libXrender-devel.i686', 'libXxf86vm-devel.i686', 'libdrm-devel.i686',
                        'libidn-devel.i686', 'libpng-devel.i686', 'libxcb-devel.i686',
                        'libxml2-devel.i686', 'pango-devel.i686', 'perl-devel.i686',
                        'pixman-devel.i686', 'zlib-devel.i686',
                        'freetype-2.3.11-6.el6_1.8.i686', 'freetype-devel-2.3.11-6.el6_1.8.i686',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
            ],
        },
        'linux64-debug': {
            'enable_nightly': False,
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'base_name': builder_prefix + 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'src_mozconfig': 'mail/config/mozconfigs/linux64/debug',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': False,
            'packageTests': True,
            'build_space': 10,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'linux64-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/linux64/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'],
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64',
            'mock_packages': \
                       ['autoconf213', 'python', 'zip', 'mozilla-python27-mercurial', 'git', 'ccache',
                        'glibc-static', 'libstdc++-static', 'perl-Test-Simple', 'perl-Config-General',
                        'gtk2-devel', 'libnotify-devel', 'yasm',
                        'alsa-lib-devel', 'libcurl-devel',
                        'wireless-tools-devel', 'libX11-devel',
                        'libXt-devel', 'mesa-libGL-devel',
                        'gnome-vfs2-devel', 'GConf2-devel', 'wget',
                        'mpfr', # required for system compiler
                        'xorg-x11-font*', # fonts required for PGO
                        'imake', # required for makedepend!?!
                        'gcc45_0moz3', 'gcc454_0moz1', 'gcc472_0moz1', 'gcc473_0moz1', 'yasm', 'ccache', # <-- from releng repo
                        'pulseaudio-libs-devel',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                        'gstreamer-devel', 'gstreamer-plugins-base-devel',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
            ],
        },
        'macosx64-debug': {
            'enable_nightly': False,
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'base_name': builder_prefix + 'OS X 10.7 64-bit %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'src_mozconfig': 'mail/config/mozconfigs/macosx64/debug',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 10,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'macosx64-debug',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'LC_ALL': 'C',
                'PATH': '/tools/python/bin:/tools/buildbot/bin:/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/macosx64/releng.manifest',
            'enable_ccache': True,
        },
        'win32-debug': {
            'enable_nightly': False,
            'product_name': 'thunderbird',
            'app_name': 'mail',
            'base_name': builder_prefix + 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'src_mozconfig': 'mail/config/mozconfigs/win32/debug',
            'profiled_build': False,
            'builds_before_reboot': thunderbird_localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'build_space': 10,
            'slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'thunderbird',
            'stage_platform': 'win32-debug',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'mail/config/tooltool-manifests/win32/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
}

for platform in PLATFORM_VARS.values():
    if 'env' not in platform:
        platform['env'] = deepcopy(GLOBAL_ENV)
    else:
        platform['env'].update((k, v) for k, v in GLOBAL_ENV.items() if k not in platform['env'])

# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'comm-central': {
    },
    'comm-beta': {
    },
    'comm-esr52': {
        'gecko_version': 52,
    },
    'try-comm-central': {
    },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

setMainCommVersions(BRANCHES)

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        elif key == 'mobile_platforms' and 'mobile_platforms' in BRANCHES[branch]:
            continue
        else:
            BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                # put default platform set in all branches, but grab any
                # project_branches.py overrides/additional keys
                if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch]:
                    if platform in PROJECT_BRANCHES[branch]['platforms'].keys():
                        if key in PROJECT_BRANCHES[branch]['platforms'][platform].keys():
                            value = deepcopy(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                else:
                    value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                else:
                    value = deepcopy(value)
                BRANCHES[branch]['platforms'][platform][key] = value

            if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch] and \
                    platform in PROJECT_BRANCHES[branch]['platforms']:
                for key, value in PROJECT_BRANCHES[branch]['platforms'][platform].items():
                    if key == 'env':
                        value = deepcopy(PLATFORM_VARS[platform]['env'])
                        value.update(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                    else:
                        value = deepcopy(value)
                    BRANCHES[branch]['platforms'][platform][key] = value
    # Copy in local config
    if branch in thunderbird_localconfig.BRANCHES:
        for key, value in thunderbird_localconfig.BRANCHES[branch].items():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.items():
                    for key, value in platform_config.items():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in thunderbird_localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Check for project branch removing a platform from default platforms
    if branch in ACTIVE_PROJECT_BRANCHES:
        for key, value in PROJECT_BRANCHES[branch].items():
            if key == 'platforms':
                for platform, platform_config in value.items():
                    if platform_config.get('dont_build'):
                        del BRANCHES[branch]['platforms'][platform]

    if BRANCHES[branch]['platforms'].has_key('win64') and branch not in ('try', 'comm-central'):
        del BRANCHES[branch]['platforms']['win64']

######## comm-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['comm-central']['moz_repo_path'] = 'mozilla-central'
BRANCHES['comm-central']['skip_blank_repos'] = True
BRANCHES['comm-central']['call_client_py'] = True
BRANCHES['comm-central']['repo_path'] = 'comm-central'
BRANCHES['comm-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['comm-central']['start_hour'] = [3]
BRANCHES['comm-central']['start_minute'] = [2]
# Enable unit tests
BRANCHES['comm-central']['enable_mac_a11y'] = True
BRANCHES['comm-central']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['comm-central']['enable_l10n'] = True
BRANCHES['comm-central']['l10nNightlyUpdate'] = True
BRANCHES['comm-central']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                              'macosx64']
BRANCHES['comm-central']['l10nDatedDirs'] = True
BRANCHES['comm-central']['l10n_tree'] = 'tbcentral'
#make sure it has an ending slash
BRANCHES['comm-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/thunderbird/nightly/latest-comm-central-l10n/'
BRANCHES['comm-central']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-central'
BRANCHES['comm-central']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.comm-central' % (GLOBAL_VARS['hgurl'])
BRANCHES['comm-central']['enable_multi_locale'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central']['updates_enabled'] = True
BRANCHES['comm-central']['update_channel'] = 'nightly'
BRANCHES['comm-central']['create_partial'] = False
BRANCHES['comm-central']['create_partial_l10n'] = False
BRANCHES['comm-central']['enable_blocklist_update'] = True
BRANCHES['comm-central']['file_update_on_closed_tree'] = False
# Thunderbird no longer builds succesfully on buildbot, so don't try building it
for platform in BRANCHES['comm-central']['platforms'].keys():
    if platform != 'linux64':
        del BRANCHES['comm-central']['platforms'][platform]
# This keeps the 'TB Linux x86-64 comm-central periodic' builder around
# while disabling all other builders
BRANCHES['comm-central']['enable_nightly'] = False
BRANCHES['comm-central']['enable_periodic'] = False
BRANCHES['comm-central']['platforms']['linux64']['enable_dep'] = False


######## comm-esr52
BRANCHES['comm-esr52']['repo_path'] = 'releases/comm-esr52'
BRANCHES['comm-esr52']['moz_repo_path'] = 'releases/mozilla-esr52'
BRANCHES['comm-esr52']['update_channel'] = 'nightly-esr52'
BRANCHES['comm-esr52']['skip_blank_repos'] = True
BRANCHES['comm-esr52']['call_client_py'] = True
BRANCHES['comm-esr52']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['comm-esr52']['start_hour'] = [3]
BRANCHES['comm-esr52']['start_minute'] = [2]
# Enable unit tests
BRANCHES['comm-esr52']['enable_mac_a11y'] = True
BRANCHES['comm-esr52']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['comm-esr52']['enable_l10n'] = False
BRANCHES['comm-esr52']['l10nNightlyUpdate'] = False
BRANCHES['comm-esr52']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                            'macosx64']
BRANCHES['comm-esr52']['l10nDatedDirs'] = True
BRANCHES['comm-esr52']['l10n_tree'] = 'tbrel'
BRANCHES['comm-esr52']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-esr52'
BRANCHES['comm-esr52']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.comm-esr52' % (GLOBAL_VARS['hgurl'])
BRANCHES['comm-esr52']['enable_nightly'] = True
BRANCHES['comm-esr52']['updates_enabled'] = True
BRANCHES['comm-esr52']['create_partial'] = False
BRANCHES['comm-esr52']['enable_blocklist_update'] = True
BRANCHES['comm-esr52']['file_update_on_closed_tree'] = False

######## comm-beta
BRANCHES['comm-beta']['moz_repo_path'] = 'releases/mozilla-beta'
BRANCHES['comm-beta']['skip_blank_repos'] = True
BRANCHES['comm-beta']['call_client_py'] = True
BRANCHES['comm-beta']['repo_path'] = 'releases/comm-beta'
BRANCHES['comm-beta']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['comm-beta']['update_channel'] = 'beta'
BRANCHES['comm-beta']['start_hour'] = [3]
BRANCHES['comm-beta']['start_minute'] = [2]
# Enable unit tests
BRANCHES['comm-beta']['enable_mac_a11y'] = True
BRANCHES['comm-beta']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['comm-beta']['enable_l10n'] = False
BRANCHES['comm-beta']['l10nNightlyUpdate'] = False
BRANCHES['comm-beta']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                           'macosx64']
BRANCHES['comm-beta']['l10nDatedDirs'] = True
BRANCHES['comm-beta']['l10n_tree'] = 'tbbeta'
#make sure it has an ending slash
BRANCHES['comm-beta']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/thunderbird/nightly/latest-comm-beta-l10n/'
BRANCHES['comm-beta']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-comm-beta'
BRANCHES['comm-beta']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.comm-beta' % (GLOBAL_VARS['hgurl'])
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['comm-beta']['enable_nightly'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-beta']['enable_blocklist_update'] = True
BRANCHES['comm-beta']['file_update_on_closed_tree'] = False
# Thunderbird no longer builds succesfully on buildbot, so don't try building it
for platform in BRANCHES['comm-beta']['platforms'].keys():
    if platform != 'linux64':
        del BRANCHES['comm-beta']['platforms'][platform]
# This keeps the 'TB Linux x86-64 comm-central periodic' builder around
# while disabling all other builders
BRANCHES['comm-beta']['enable_periodic'] = False
BRANCHES['comm-beta']['platforms']['linux64']['enable_dep'] = False

######## try
# Try-specific configs
BRANCHES['try-comm-central']['stage_username'] = 'trybld'
BRANCHES['try-comm-central']['stage_ssh_key'] = 'trybld_dsa'
BRANCHES['try-comm-central']['stage_base_path'] = '/home/ftp/pub/thunderbird/try-builds'
BRANCHES['try-comm-central']['enable_merging'] = False
BRANCHES['try-comm-central']['enable_try'] = True
BRANCHES['try-comm-central']['watch_all_branches'] = True
BRANCHES['try-comm-central']['package_dir'] ='%(who)s-%(got_revision)s/'
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try-comm-central']['repo_path'] = 'try-comm-central'
BRANCHES['try-comm-central']['start_hour'] = [3]
BRANCHES['try-comm-central']['start_minute'] = [2]
# Disable Nightly builds
BRANCHES['try-comm-central']['enable_nightly'] = False
BRANCHES['try-comm-central']['enable_mac_a11y'] = True
# only do unittests locally until they are switched over to talos-r3
BRANCHES['try-comm-central']['enable_l10n'] = False
BRANCHES['try-comm-central']['l10nNightlyUpdate'] = False
BRANCHES['try-comm-central']['l10nDatedDirs'] = False
# need this or the master.cfg will bail
BRANCHES['try-comm-central']['platforms']['linux']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try-comm-central']['platforms']['linux64']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try-comm-central']['platforms']['win32']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try-comm-central']['platforms']['macosx64']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try-comm-central']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try-comm-central']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try-comm-central']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try-comm-central']['platforms']['macosx64-debug']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try-comm-central']['platforms']['linux']['upload_symbols'] = False
BRANCHES['try-comm-central']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['try-comm-central']['platforms']['macosx64']['upload_symbols'] = False
# Disabled due to issues, see bug 751559
BRANCHES['try-comm-central']['platforms']['win32']['upload_symbols'] = False

######## generic branch configs
for branch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[branch]
    BRANCHES[branch]['brand_name'] = branchConfig.get('brand_name', GLOBAL_VARS['brand_name'])
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['mozilla_dir'] = branchConfig.get('mozilla_dir', 'mozilla')
    BRANCHES[branch]['mozilla_srcdir'] = branchConfig.get('mozilla_srcdir', 'mozilla')
    BRANCHES[branch]['enabled_products'] = branchConfig.get('enabled_products',
                                                            GLOBAL_VARS['enabled_products'])
    BRANCHES[branch]['enable_nightly'] = branchConfig.get('enable_nightly', False)
    BRANCHES[branch]['enable_mobile'] = branchConfig.get('enable_mobile', True)
    BRANCHES[branch]['pgo_strategy'] = branchConfig.get('pgo_strategy', None)
    BRANCHES[branch]['periodic_start_hours'] = branchConfig.get('periodic_start_hours', range(0, 24, 6))
    BRANCHES[branch]['start_hour'] = branchConfig.get('start_hour', [4])
    BRANCHES[branch]['start_minute'] = branchConfig.get('start_minute', [2])
    # Enable unit tests
    BRANCHES[branch]['enable_mac_a11y'] = branchConfig.get('enable_mac_a11y', True)
    BRANCHES[branch]['unittest_build_space'] = branchConfig.get('unittest_build_space', 6)
    # L10n configuration is not set up for project_branches
    BRANCHES[branch]['enable_l10n'] = branchConfig.get('enable_l10n', False)
    BRANCHES[branch]['l10nNightlyUpdate'] = branchConfig.get('l10nNightlyUpdate', False)
    BRANCHES[branch]['l10nDatedDirs'] = branchConfig.get('l10nDatedDirs', False)
    # nightly updates
    BRANCHES[branch]['updates_enabled'] = branchConfig.get('updates_enabled', False)
    BRANCHES[branch]['update_channel'] = branchConfig.get('update_channel', 'nightly-%s' % branch)
    BRANCHES[branch]['create_partial'] = branchConfig.get('create_partial', False)
    BRANCHES[branch]['create_partial_l10n'] = branchConfig.get('create_partial_l10n', False)
    BRANCHES[branch]['l10nUploadPath'] = \
        '/home/ftp/pub/mozilla.org/thunderbird/nightly/latest-' + branch + '-l10n/'
    BRANCHES[branch]['enUS_binaryURL'] = GLOBAL_VARS['download_base_url'] + branchConfig.get('enUS_binaryURL', '')
    # Platform-specific defaults/interpretation
    for platform in BRANCHES[branch]['platforms']:
        # point to the mozconfigs, default is generic
        if platform.endswith('debug'):
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform.split('-')[0] + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/debug'
        else:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/nightly'
        # Project branches should be allowed to override the signing servers.
        # If a branch does not set dep_signing_servers, it should be set to the global default.
        BRANCHES[branch]['platforms'][platform]['dep_signing_servers'] = branchConfig.get('platforms', {}).get(platform, {}).get('dep_signing_servers',
                                                                         PLATFORM_VARS[platform].get('dep_signing_servers'))
        # If a branch does not set nightly_signing_servers, it should be set to its dep signing server,
        # which may have already been set to the global default.
        BRANCHES[branch]['platforms'][platform]['nightly_signing_servers'] = branchConfig.get('platforms', {}).get(platform, {}).get('nightly_signing_servers',
                                                                             BRANCHES[branch]['platforms'][platform]['dep_signing_servers'])


# Bug 578880, remove the following block after gcc-4.5 switch
branches = BRANCHES.keys()
branches.extend(ACTIVE_PROJECT_BRANCHES)
for branch in branches:
    if BRANCHES[branch]['platforms'].has_key('linux'):
        BRANCHES[branch]['platforms']['linux']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
        BRANCHES[branch]['platforms']['linux']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if BRANCHES[branch]['platforms'].has_key('linux-mobile'):
        BRANCHES[branch]['platforms']['linux-mobile']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
        BRANCHES[branch]['platforms']['linux-mobile']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if BRANCHES[branch]['platforms'].has_key('linux64'):
        BRANCHES[branch]['platforms']['linux64']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib64'
        BRANCHES[branch]['platforms']['linux64']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
        }
    if BRANCHES[branch]['platforms'].has_key('linux-debug'):
        BRANCHES[branch]['platforms']['linux-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib:%s/mozilla/dist/bin' % OBJDIR
        BRANCHES[branch]['platforms']['linux-debug']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if BRANCHES[branch]['platforms'].has_key('linux64-debug'):
        BRANCHES[branch]['platforms']['linux64-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib64:%s/mozilla/dist/bin' % OBJDIR
        BRANCHES[branch]['platforms']['linux64-debug']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
        }

# Only test pretty names on train branches, not c-c.
for branch in branches:
    if branch != "comm-central":
        for platform in ("linux", "linux64", "macosx64", "win32", "win64"):
            if platform in BRANCHES[branch]['platforms']:
                BRANCHES[branch]['platforms'][platform]['test_pretty_names'] = True

# This does not currently affect Thunderbird builds since mozharness is not
# enabled yet.

# Enable mozharness pinning
for _, branch in items_at_least(BRANCHES, 'gecko_version', 30):
    branch['script_repo_manifest'] = \
        "https://hg.mozilla.org/%(moz_repo_path)s/raw-file/default/" + \
        "testing/mozharness/mozharness.json"
    # mozharness_archiver_repo_path tells the factory to use a copy of mozharness from within the
    #  gecko tree and also allows us to overwrite which gecko repo to use. Useful for platforms
    # like Thunderbird
    branch['mozharness_archiver_repo_path'] = '%(moz_repo_path)s'
    branch['mozharness_archiver_rev'] = 'default'

# Cypress is the m-c in c-c repo, so set some specifics
BRANCHES['cypress']['mozharness_archiver_repo_path'] = '%(repo_path)s'
BRANCHES['cypress']['pgo_strategy'] = None
# Enable unit tests
BRANCHES['cypress']['enable_mac_a11y'] = True
BRANCHES['cypress']['unittest_build_space'] = 6
BRANCHES['cypress']['mozilla_srcdir'] = None

# Bug 1322402 - mac universal builds dropped at 53, keep using the universal mozconfig and objdir before then
for name, branch in items_before(BRANCHES, 'gecko_version', 53):
    if 'macosx64' in branch['platforms']:
        branch['platforms']['macosx64']['src_mozconfig'] = 'mail/config/mozconfigs/macosx-universal/nightly'
        branch['platforms']['macosx64']['platform_objdir'] = '%s/i386' % OBJDIR

# Support cross-channel l10n in 57+ -- Bug 1397721
for name, branch in items_at_least(BRANCHES, 'gecko_version', 57):
    if 'l10n_repo_path' not in branch:
        continue
    branch['l10n_repo_path'] = 'l10n-central'


for name, branch in BRANCHES.items():
    # Level 3 Branches
    if name in ('comm-central', 'comm-beta', 'comm-esr52'):
        for platform in branch['platforms'].values():
            platform['env']['MOZ_SCM_LEVEL'] = '3'


if __name__ == "__main__":
    import sys
    import pprint
    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = BRANCHES

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)
