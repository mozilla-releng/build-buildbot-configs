from copy import deepcopy

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, TRY_SLAVES

import master_common
reload(master_common)
from master_common import setMainFirefoxVersions, items_before, items_at_least

GLOBAL_VARS = {
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'hgurl': 'https://hg.mozilla.org/',
    'hghost': 'hg.mozilla.org',
    'config_subdir': 'mozilla2',
    'objdir': 'obj-firefox',
    'objdir_unittests': 'objdir',
    'stage_username': 'ffxbld',
    'stage_username_xulrunner': 'xrbld',
    'stage_base_path': '/home/ftp/pub',
    'stage_group': None,
    'stage_ssh_key': 'ffxbld_dsa',
    'stage_ssh_xulrunner_key': 'xrbld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_ffx/',
    'symbol_server_post_upload_cmd': '/usr/local/bin/post-symbol-upload.py',
    'symbol_server_mobile_path': '/mnt/netapp/breakpad/symbols_mob/',
    'symbol_server_xulrunner_path': '/mnt/netapp/breakpad/symbols_xr/',
    'balrog_credentials_file': 'BuildSlaves.py',
    'hg_username': 'ffxbld',
    'hg_ssh_key': '~cltbld/.ssh/ffxbld_dsa',
    'graph_selector': '/server/collect.cgi',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'mozharness_repo_path': 'build/mozharness',
    'mozharness_tag': 'production',
    'multi_locale_merge': True,
    'default_build_space': 5,
    'default_l10n_space': 3,
    'default_clobber_time': 24*7,  # 1 week
    'unittest_suites': [
        ('mochitest', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-browser-chrome', ['mochitest-browser-chrome']),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-a11y', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
    ],
    'platforms': {
        'linux': {},
        'linux64': {},
        'win32': {},
        'win64': {},
        'macosx64': {},
        'linux-debug': {},
        'linux64-br-haz': {},
        'linux64-debug': {},
        'linux64-asan': {},
        'linux64-asan-debug': {},
        'linux64-st-an-debug': {},
        'linux64-mulet': {},
        'linux64-cc': {},
        'macosx64-debug': {},
        'win32-debug': {},
        'win64-debug': {},
        'android': {},
        'android-x86': {},
        'android-armv6': {},
        'android-debug': {},
    },
    'pgo_strategy': None,
    'pgo_platforms': ('linux', 'linux64', 'win32',),
    'periodic_start_hours': range(0, 24, 6),
    'enable_blocklist_update': False,
    'enable_hsts_update': False,
    'enable_hpkp_update': False,
    'file_update_on_closed_tree': False,
    'file_update_set_approval': True,
    'enable_nightly': True,
    'enabled_products': ['firefox', 'mobile'],
    'enable_valgrind': True,
    'enable_xulrunner': False,
    'valgrind_platforms': ('linux64',),

    # List of keys in BRANCH_PROJECTS that will be activated for the BRANCH
    'branch_projects': ['spidermonkey_tier_1'],

    # if true, this branch will get bundled and uploaded to ftp.m.o for users
    # to download and thereby accelerate their cloning
    'enable_weekly_bundle': False,

    'hash_type': 'sha512',
    'create_snippet': False,
    'create_partial': False,
    'create_partial_l10n': False,
    'l10n_modules': [
            'browser',
            'dom',
            'extensions/reporter',
            'extensions/spellcheck',
            'netwerk',
            'other-licenses/branding/firefox',
            'security/manager',
            'services/sync',
            'toolkit',
            ],
    'use_old_updater': False,
    # rather than repeat these options in each of these options in
    # every platform, let's define the arguments here and when we want to
    # turn an existing platform into say a 'nightly' version, add the options
    #  from here and append it to 'extra_options'
    'mozharness_desktop_extra_options': {
        'nightly': ['--enable-nightly'],
        'pgo': ['--enable-pgo'],
    },
    # list platforms with mozharness l10n repacks enabled.
    # mozharness repacks will be enabled per branch
    'mozharness_desktop_l10n_platforms': [
        'linux', 'linux64', 'macosx64'
    ],
    # bug 1027890: excluding win32/win64 for now
}
GLOBAL_VARS.update(localconfig.GLOBAL_VARS.copy())

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']
SYMBOL_SERVER_POST_UPLOAD_CMD = GLOBAL_VARS['symbol_server_post_upload_cmd']
SYMBOL_SERVER_MOBILE_PATH = GLOBAL_VARS['symbol_server_mobile_path']

GLOBAL_ENV = {
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_AUTOMATION': '1',
}

PLATFORM_VARS = {
        'linux': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt', '-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_32_builds.py',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 10,
                'use_credentials_file': True,
                'config': 'single_locale/linux.py',
            },
            'dep_signing_servers': 'dep-signing',
            'base_name': 'Linux %(branch)s',
            'product_name': 'firefox',
            'unittest_platform': 'linux-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'mozconfig': 'linux/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/linux32/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/linux32/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux',
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': False,
            'l10n_check_test': True,
            'nightly_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux32/releng.manifest',
            'tooltool_l10n_manifest_src': 'browser/config/tooltool-manifests/linux32/l10n.manifest',
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
                        'valgrind',
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
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
            ],
        },
        'linux64': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt', '-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            # because non-unified platforms are defined at misc level,
            # we can not add a new platform in config.py for this but instead
            #  add another config on all non-unified able platforms
            'mozharness_non_unified_extra_args': [
                '--config', 'builds/releng_base_linux_64_builds.py',
                '--custom-build-variant-cfg', 'non-unified',
            ],
            'mozharness_desktop_l10n': {
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 10,
                'use_credentials_file': True,
                'config': 'single_locale/linux64.py',
            },
            'product_name': 'firefox',
            'unittest_platform': 'linux64-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/linux64/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': False,
            'l10n_check_test': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/releng.manifest',
            'tooltool_l10n_manifest_src': 'browser/config/tooltool-manifests/linux64/l10n.manifest',
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
                        'valgrind', 'dbus-x11',
                        'pulseaudio-libs-devel',
                        'gstreamer-devel', 'gstreamer-plugins-base-devel',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
            ],
        },
        'linux64-asan': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt','-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'asan',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },

            'product_name': 'firefox',
            'unittest_platform': 'linux64-asan-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Linux x86-64 %(branch)s asan',
            'mozconfig': 'in_tree',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/nightly-asan',
            'enable_xulrunner': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': False,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64-asan',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64-asan',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': False,
            'create_snippet': False,
            'create_partial': False,
            'test_pretty_names': False,
            'l10n_check_test': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/asan.manifest',
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
                        'valgrind',
                        'pulseaudio-libs-devel',
                        'gstreamer-devel', 'gstreamer-plugins-base-devel',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
            ],
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
        },
        'linux64-asan-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt','-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'asan-and-debug',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },

            'enable_nightly': True,
            'product_name': 'firefox',
            'unittest_platform': 'linux64-asan-debug',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Linux x86-64 %(branch)s debug asan',
            'mozconfig': 'in_tree',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/debug-asan',
            'enable_xulrunner': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': False,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64-asan-debug',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64-asan-debug',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': False,
            'create_snippet': False,
            'create_partial': False,
            'test_pretty_names': False,
            'l10n_check_test': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/asan.manifest',
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
                        'valgrind',
                        'pulseaudio-libs-devel',
                        'gstreamer-devel', 'gstreamer-plugins-base-devel',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
            ],
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
        },
        'linux64-st-an-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt','-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'stat-and-debug',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },

            'enable_nightly': False,
            'product_name': 'firefox',
            'unittest_platform': 'linux64-st-an-debug',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Linux x86-64 %(branch)s debug static analysis',
            'mozconfig': 'in_tree',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/debug-static-analysis-clang',
            'enable_xulrunner': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': False,
            'download_symbols': False,
            'packageTests': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64-st-an-debug',
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64-st-an-debug',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': False,
            'enable_build_analysis': False,
            'create_snippet': False,
            'create_partial': False,
            'test_pretty_names': False,
            'l10n_check_test': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/clang.manifest',
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
                        'valgrind',
                        'pulseaudio-libs-devel',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                        'gstreamer-devel', 'gstreamer-plugins-base-devel',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
            ],
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
        },
        'linux64-sh-haz': {
            'mozharness_config': {
                'script_name': 'scripts/spidermonkey_build.py',
                'extra_args': [
                    '--config-file', 'hazards/build_shell.py',
                    '--config-file', 'hazards/common.py',
                ],
            },
            'stage_product': 'firefox',
            'product_name': 'firefox',
            'base_name': '%(platform)s_%(branch)s',
            'slaves': SLAVES['mock'],
            'try_by_default': False,
            'consider_for_nightly': False,
            'mock_target': 'mozilla-centos6-x86_64',
        },
        'linux64-br-haz': {
            'mozharness_config': {
                'script_name': 'scripts/spidermonkey_build.py',
                'extra_args': [
                    '--config-file', 'hazards/build_browser.py',
                    '--config-file', 'hazards/common.py',
                ],
            },

            'stage_product': 'firefox',
            'product_name': 'firefox',
            'base_name': '%(platform)s_%(branch)s',
            'slaves': SLAVES['mock'],
            'try_by_default': True,
            'consider_for_nightly': False,
            'mock_target': 'mozilla-centos6-x86_64',
        },
        'linux64-mulet': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt','-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'mulet',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },

            'consider_for_nightly': False,
            'enable_nightly': False,
            'enable_xulrunner': False,
            'enable_opt_unittests': True,
            'try_by_default': True,
            'upload_symbols': False,
            'packageTests': True,

            'product_name': 'firefox',
            'unittest_platform': 'linux64-mulet-opt',
            'base_name': 'Linux x86-64 Mulet %(branch)s',
            'slaves': SLAVES['mock'],
            'mozconfig': 'in_tree',
            'src_mozconfig': 'b2g/dev/config/mozconfigs/linux64/mulet',
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64-mulet',
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/releng.manifest',
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
                        'valgrind', 'dbus-x11',
                        'pulseaudio-libs-devel',
                        'gstreamer-devel', 'gstreamer-plugins-base-devel',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
            ],
        },
        'linux64-cc': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt', '-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'code-coverage',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'consider_for_nightly': False,
            'enable_nightly': False,
            'enable_xulrunner': False,
            'enable_opt_unittests': True,
            'try_by_default': False,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,

            'product_name': 'firefox',
            'unittest_platform': 'linux64-cc-opt',
            'app_name': 'browser',
            'base_name': 'Linux x86-64 Code Coverage %(branch)s',
            'mozconfig': 'in_tree',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/code-coverage',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64-cc',
            'update_platform': 'Linux_x86_64-gcc3',
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_checktests': True,
            'enable_build_analysis': False,
            'test_pretty_names': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/releng.manifest',
            'tooltool_l10n_manifest_src': 'browser/config/tooltool-manifests/linux64/l10n.manifest',
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
                        'valgrind', 'dbus-x11',
                        'pulseaudio-libs-devel',
                        'gstreamer-devel', 'gstreamer-plugins-base-devel',
                        'freetype-2.3.11-6.el6_1.8.x86_64',
                        'freetype-devel-2.3.11-6.el6_1.8.x86_64',
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
            ],
        },
        'macosx64': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt', '-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_mac_64_builds.py',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            # because non-unified platforms are defined at misc level,
            # we can not add a new platform in config.py for this but instead
            #  add another config on all non-unified able platforms
            'mozharness_non_unified_extra_args': [
                '--config', 'builds/releng_base_mac_64_builds.py',
                '--custom-build-variant-cfg', 'non-unified',
            ],
            'mozharness_desktop_l10n': {
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 10,
                'use_credentials_file': True,
                'config': 'single_locale/macosx64.py',
            },

            'product_name': 'firefox',
            'unittest_platform': 'macosx64-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'OS X 10.7 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/macosx-universal/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/macosx-universal/xulrunner',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': "%s/i386" % OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx64',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'macosx64',
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
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': False,
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/macosx64/releng.manifest',
            'tooltool_l10n_manifest_src': 'browser/config/tooltool-manifests/macosx64/l10n.manifest',
            'enable_ccache': True,
        },
        'macosx64-mulet': {
            'product_name': 'firefox',
            'unittest_platform': 'macosx64-mulet-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'OS X Mulet %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'src_mozconfig': 'b2g/dev/config/mozconfigs/macosx-universal/mulet',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': False,
            'download_symbols': False,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': "%s/i386" % OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx64-mulet',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'macosx64-mulet',
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
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/macosx64/releng.manifest',
            'tooltool_l10n_manifest_src': 'browser/config/tooltool-manifests/macosx64/l10n.manifest',
            'enable_ccache': True,
        },
        'win32': {
            'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
            'reboot_command': [
                'c:/mozilla-build/python27/python', '-u',
                'scripts/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt','-n', '1', '-z'
            ],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_windows_32_builds.py',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            # because non-unified platforms are defined at misc level,
            # we can not add a new platform in config.py for this but instead
            #  add another config on all non-unified able platforms
            'mozharness_non_unified_extra_args': [
                '--config', 'builds/releng_base_windows_32_builds.py',
                '--custom-build-variant-cfg', 'non-unified',
            ],
            'mozharness_desktop_l10n': {
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 10,
                'use_credentials_file': True,
                'config': 'single_locale/win32.py',
            },

            'product_name': 'firefox',
            'unittest_platform': 'win32-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/win32/nightly',
            'src_xulrunner_mozconfig': 'xulrunner/config/mozconfigs/win32/xulrunner',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'enable_installer': True,
            'enable_post_linker_size': True,
            'packageTests': True,
            'slaves': SLAVES['win64-rev2'],
            'l10n_slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win32',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_dsa",
                'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}nsis-2.46u;${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': False,
            'l10n_check_test': True,
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win32/releng.manifest',
            'tooltool_l10n_manifest_src': 'browser/config/tooltool-manifests/win32/l10n.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'win64': {
            'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
            'mozharness_desktop_l10n': {
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 10,
                'use_credentials_file': True,
                'config': 'single_locale/win64.py',
            },
            'reboot_command': [
                'c:/mozilla-build/python27/python', '-u',
                'scripts/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt','-n', '1', '-z'
            ],

            'product_name': 'firefox',
            'unittest_platform': 'win64-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 6.1 x86-64 %(branch)s',
            'src_mozconfig': 'browser/config/mozconfigs/win64/nightly',
            'mozconfig': 'win64/%(branch)s/nightly',
            # XXX we cannot build xulrunner on Win64 -- see bug 575912
            'enable_xulrunner': False,
            'profiled_build': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'try_by_default': False,
            'slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win64',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86_64-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/c/Users/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'win64',
                'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': False,
            'l10n_check_test': True,
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_l10n_manifest_src': 'browser/config/tooltool-manifests/win64/l10n.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'linux-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt','-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_32_builds.py',
                    '--custom-build-variant-cfg', 'debug',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },

            'enable_nightly': False,
            'enable_xulrunner': False,
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/linux32/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 15,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
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
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux32/releng.manifest',
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
                        'valgrind',
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
                ('/builds/gapi.data', '/builds/gapi.data'),
            ],
        },
        'linux64-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt','-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'debug',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            # because non-unified platforms are defined at misc level,
            # we can not add a new platform in config.py for this but instead
            #  add another config on all non-unified able platforms
            'mozharness_non_unified_extra_args': [
                '--config', 'builds/releng_base_linux_64_builds.py',
                '--custom-build-variant-cfg', 'debug-and-non-unified',
            ],

            'enable_nightly': False,
            'enable_xulrunner': False,
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': False,
            'packageTests': True,
            'build_space': 14,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'linux64-debug',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
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
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/releng.manifest',
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
                ('/builds/gapi.data', '/builds/gapi.data'),
            ],
        },
        'macosx64-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt', '-n', '1', '-z'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_mac_64_builds.py',
                    '--custom-build-variant-cfg', 'debug',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            # because non-unified platforms are defined at misc level,
            # we can not add a new platform in config.py for this but instead
            #  add another config on all non-unified able platforms
            'mozharness_non_unified_extra_args': [
                '--config', 'builds/releng_base_mac_64_builds.py',
                '--custom-build-variant-cfg', 'debug-and-non-unified',
            ],

            'enable_nightly': False,
            'enable_xulrunner': False,
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'OS X 10.7 64-bit %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/macosx64/debug',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 10,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx64-debug',
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
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
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/macosx64/releng.manifest',
            'enable_ccache': True,
        },
        'win32-debug': {
            'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
            'reboot_command': [
                'c:/mozilla-build/python27/python', '-u',
                'scripts/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt','-n', '1', '-z'
            ],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_windows_32_builds.py',
                    '--custom-build-variant-cfg', 'debug',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            # because non-unified platforms are defined at misc level,
            # we can not add a new platform in config.py for this but instead
            #  add another config on all non-unified able platforms
            'mozharness_non_unified_extra_args': [
                '--config', 'builds/releng_base_windows_32_builds.py',
                '--custom-build-variant-cfg', 'debug-and-non-unified',
            ],

            'enable_nightly': False,
            'enable_xulrunner': False,
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/win32/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'build_space': 9,
            'slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win32-debug',
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}nsis-2.46u;${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win32/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'win64-debug': {
            'enable_nightly': False,
            'enable_xulrunner': False,
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 6.1 x86-64 %(branch)s leak test',
            'mozconfig': 'win64/%(branch)s/debug',
            'src_mozconfig': 'browser/config/mozconfigs/win64/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'build_space': 9,
            'try_by_default': False,
            'slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win64-debug',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}nsis-2.46u;${MOZILLABUILD}python27;${MOZILLABUILD}buildbotve\\scripts;${PATH}",
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'consider_for_nightly': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'android': {
            'product_name': 'firefox',
            'unittest_platform': 'android-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Android 2.3 %(branch)s',
            'mozconfig': 'android/%(branch)s/nightly',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android/nightly',
            'mobile_dir': 'mobile/android',
            'enable_xulrunner': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 16,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'create_partial': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_arm-eabi-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64-android',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial',
                              'ccache', 'android-sdk15', 'android-sdk16',
                              'android-ndk5', 'android-ndk8', 'zip',
                              'java-1.7.0-openjdk-devel', 'zlib-devel',
                              'glibc-static', 'openssh-clients', 'mpfr',
                              "gcc472_0moz1", "gcc473_0moz1", 'wget', 'glibc.i686',
                              'libstdc++.i686', 'zlib.i686',
                              'freetype-2.3.11-6.el6_1.8.x86_64', 'ant', 'ant-apache-regexp'],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/mozilla-api.key', '/builds/mozilla-api.key'),
            ],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SHIP_LICENSED_FONTS': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/opt/local/bin:/tools/python/bin:/tools/buildbot/bin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/home/',
            },
            'enable_opt_unittests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
            'is_mobile_l10n': True,
            'l10n_chunks': 5,
            'multi_locale': True,
            'multi_locale_script': 'scripts/multil10n.py',
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android/releng.manifest',
        },
        'android-armv6': {
            'enable_nightly': False,
            'product_name': 'firefox',
            'unittest_platform': 'android-armv6-opt',
            'app_name': 'browser',
            'base_name': 'Android 2.3 Armv6 %(branch)s',
            'mozconfig': 'android-armv6/%(branch)s/nightly',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android-armv6/nightly',
            'mobile_dir': 'mobile/android',
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'packageTests': True,
            'enable_xulrunner': False,
            'profiled_build': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_arm-eabi-gcc3-armv6',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64-android',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial',
                              'ccache', 'android-sdk15', 'android-sdk16',
                              'android-ndk5', 'android-ndk8', 'zip',
                              'java-1.7.0-openjdk-devel', 'zlib-devel',
                              'glibc-static', 'openssh-clients', 'mpfr', 'bc',
                              "gcc472_0moz1", "gcc473_0moz1", 'wget', 'glibc.i686',
                              'libstdc++.i686', 'zlib.i686',
                              'freetype-2.3.11-6.el6_1.8.x86_64', 'ant', 'ant-apache-regexp'],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/mozilla-api.key', '/builds/mozilla-api.key'),
            ],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SHIP_LICENSED_FONTS': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/bin:/usr/bin',
            },
            'enable_opt_unittests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android-armv6",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
            'is_mobile_l10n': False,
            'multi_locale': True,
            'multi_locale_script': 'scripts/multil10n.py',
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android-armv6/releng.manifest',
        },
        'android-x86': {
            'product_name': 'firefox',
            'unittest_platform': 'android-x86-opt',
            'app_name': 'browser',
            'base_name': 'Android 4.2 x86 %(branch)s',
            'mozconfig': 'android-x86/%(branch)s/nightly',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android-x86/nightly',
            'mobile_dir': 'mobile/android',
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'packageTests': True,
            'enable_xulrunner': False,
            'profiled_build': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'use_mock': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'mock_target': 'mozilla-centos6-x86_64-android',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial',
                              'ccache', 'android-sdk15', 'android-sdk16',
                              'android-ndk7', 'android-ndk8', 'yasm', 'zip',
                              'java-1.7.0-openjdk-devel', 'zlib-devel',
                              'glibc-static', 'openssh-clients', 'mpfr', 'bc',
                              "gcc472_0moz1", "gcc473_0moz1", 'glibc.i686', 'libstdc++.i686',
                              'zlib.i686', 'freetype-2.3.11-6.el6_1.8.x86_64', 'ant', 'ant-apache-regexp'],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/mozilla-api.key', '/builds/mozilla-api.key'),
            ],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/bin:/usr/bin',
            },
            'enable_opt_unittests': False,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android-x86",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
            'is_mobile_l10n': False,
            'multi_locale': True,
            'multi_locale_script': 'scripts/multil10n.py',
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android-x86/releng.manifest',
        },
        'android-debug': {
            'enable_nightly': False,
            'product_name': 'firefox',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Android 2.3 Debug %(branch)s',
            'mozconfig': 'android-debug/%(branch)s/nightly',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android/debug',
            'mobile_dir': 'mobile/android',
            'enable_xulrunner': False,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'create_snippet': False,
            'create_partial': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Android_arm-eabi-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'enable_nonunified_build': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64-android',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial',
                              'ccache', 'android-sdk15', 'android-sdk16',
                              'android-ndk5', 'android-ndk8', 'zip', "gcc472_0moz1", "gcc473_0moz1",
                              'java-1.7.0-openjdk-devel', 'zlib-devel',
                              'glibc-static', 'openssh-clients', 'mpfr',
                              'wget', 'glibc.i686', 'libstdc++.i686',
                              'zlib.i686', 'freetype-2.3.11-6.el6_1.8.x86_64', 'ant', 'ant-apache-regexp'],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/mozilla-api.key', '/builds/mozilla-api.key'),
            ],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/mock_mozilla/.ssh/ffxbld_dsa",
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SHIP_LICENSED_FONTS': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/bin:/usr/bin',
            },
            'enable_opt_unittests': False,
            'talos_masters': None,
            'unittest_masters': GLOBAL_VARS['unittest_masters'],
            'stage_platform': "android-debug",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android/releng.manifest',
        },
}
# Additional fixups for lion
PLATFORM_VARS["macosx64-lion"] = deepcopy(PLATFORM_VARS["macosx64"])
PLATFORM_VARS["macosx64-lion-debug"] = deepcopy(PLATFORM_VARS["macosx64-debug"])
PLATFORM_VARS["macosx64-lion"]["base_name"] = 'OS X 10.7 %(branch)s'
PLATFORM_VARS["macosx64-lion-debug"]["base_name"] = 'OS X 10.7 64-bit %(branch)s leak test'
PLATFORM_VARS["macosx64-lion"]["slaves"] = SLAVES['macosx64-lion']
PLATFORM_VARS["macosx64-lion-debug"]["slaves"] = SLAVES['macosx64-lion']

for platform in PLATFORM_VARS.values():
    if 'env' not in platform:
        platform['env'] = deepcopy(GLOBAL_ENV)
    else:
        platform['env'].update((k, v) for k, v in GLOBAL_ENV.items() if k not in platform['env'])

PROJECTS = {
    'fuzzing': {
        'platforms': ['mock-hw', 'macosx64-lion', 'win64-rev2'],
    },
}

# For bug 978211, we are using MOZ_AUTOMATION to trigger the automation build
# steps from mach. However, these build variants already use mach, and so they
# would inadvertently trigger the automation steps. We can remove the
# MOZ_AUTOMATION environment variable for them, since it's not used anyway.
del PLATFORM_VARS["linux64-sh-haz"]["env"]["MOZ_AUTOMATION"]
del PLATFORM_VARS["linux64-br-haz"]["env"]["MOZ_AUTOMATION"]

# Override config settings with local settings
def apply_localconfig(config, local):
    for k, v in local.items():
        if k not in config:
            config[k] = {}
        config[k].update(v)

apply_localconfig(PROJECTS, localconfig.PROJECTS)

# Branch-associated projects
#
# BRANCHES values contain a 'branch_projects' key containing a list of
# BRANCH_PROJECTS keys to instantiate for that branch. These are intended for
# builds that are associated with one or more branches, but use separate
# scheduling and build mechanisms. Each project will have a 'branch' key filled
# in with the name of the branch to which it applies.
#
# Configuration keys:
#
#  project_name - pattern used to construct (part of) the builder name. It
#    can use %-interpolation to select anything from the config, which
#    usually means it will contain "%(branch)s".
#
# Spidermonkey-specific configuration keys:
#
#  variants - mapping of platforms (with build configuration, eg linux64-debug)
#    to an array of variant names. These names correspond to files in
#    build-tools/scripts/spidermonkey_builds/.
#
#  enable_try - this project should be active for the try server
#
#  try_by_default - list of variants that should be triggered by default on
#    try. If a variant is missing from this list, then the build will only be
#    triggered if the corresponding base platform is explicitly requested in
#    the -p option of trychooser. For example, |-p all| will not trigger such a
#    project, but either |-p linux64| or |-p all,linux64| will (assuming the
#    project has both 'platforms' and 'variants' entries for 'linux' or
#    'linux64'.)
#
BRANCH_PROJECTS = {
    # Builds that should trigger backouts if they break. Should be on all trees
    # feeding into mozilla-central.
    'spidermonkey_tier_1': {
        'variants': {
            'linux64-debug':  ['rootanalysis', 'generational'],
            'linux-debug': ['arm-sim'],
        },
        'platforms': {
            'linux': {},
            'linux-debug': {},
            'linux64': {},
            'linux64-debug': {},
            'win32': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
            'macosx64': {},
            'macosx64-debug': {},
        },
        'hgurl': 'https://hg.mozilla.org/',
    },

    # Try server builds only triggered on changes to the spidermonkey source
    'spidermonkey_try': {
        'enable_try': True,
        'try_by_default': {
            'rootanalysis': True, # all platforms for which it is defined
            'generational': set(['linux64-debug']),
            'arm-sim': True,
        },
        'variants': {
            'linux': ['warnaserr'],
            'linux-debug': ['arm-sim', 'warnaserrdebug'],
            'linux64':  ['warnaserr'],
            'linux64-debug':  ['rootanalysis', 'generational', 'exactrooting', 'warnaserrdebug'],
            'win32': ['generational', 'warnaserr'],
            'win32-debug': ['generational', 'warnaserrdebug'],
        },
        'platforms': {
            'linux': {},
            'linux-debug': {},
            'linux64': {},
            'linux64-debug': {},
            'win32': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
            'macosx64': {},
            'macosx64-debug': {},
        },
        'hgurl': 'https://hg.mozilla.org/',
    },

    # Non-tier-1 builds that provide useful information but are hidden on tbpl.
    # These will probably be run on the subset of the trees that the relevant
    # developers will actually look.
    'spidermonkey_info': {
        'variants': {
            'linux':          ['warnaserr'],
            'linux-debug':    ['warnaserrdebug'],
            'linux64':        ['warnaserr'],
            'linux64-debug':  ['warnaserrdebug'],
        },
        'platforms': {
            'linux': {},
            'linux-debug': {},
            'linux64': {},
            'linux64-debug': {},
            'win32': {},
            'win32-debug': {},
            'win64': {},
            'win64-debug': {},
            'macosx64': {},
            'macosx64-debug': {},
        },
        'hgurl': 'https://hg.mozilla.org/',
    },
}

apply_localconfig(BRANCH_PROJECTS, localconfig.BRANCH_PROJECTS)

# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {
    },
    'mozilla-release': {
        'branch_projects': []
    },
    'mozilla-beta': {
        'branch_projects': []
    },
    'mozilla-aurora': {
        'branch_projects': []
    },
    'mozilla-esr24': {
        'branch_projects': [],
        'lock_platforms': True,
        'gecko_version': 24,
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
    },
    'mozilla-esr31': {
        'branch_projects': [],
        'lock_platforms': True,
        'gecko_version': 31,
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
    },
    'mozilla-b2g28_v1_3': {
        'branch_projects': [],
        'lock_platforms': True,
        'gecko_version': 28,
        'platforms': {
            # desktop for gecko security reproduciton (per akeybl
            # https://bugzil.la/818378#c8)
            'linux': {},
            'linux64': {},
            'win32': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
        },
    },
    'mozilla-b2g28_v1_3t': {
        'branch_projects': [],
        'lock_platforms': True,
        'gecko_version': 28,
        'platforms': {},
    },
    'mozilla-b2g30_v1_4': {
        'branch_projects': [],
        'lock_platforms': True,
        'gecko_version': 30,
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
    },
    'mozilla-b2g32_v2_0': {
        'branch_projects': [],
        'lock_platforms': True,
        'gecko_version': 32,
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
    },
    'try': {
        'branch_projects': ['spidermonkey_try'],
        # For now, only run shell rooting hazards builds on try. (Browser
        # hazard builds run everywhere, not just on try.)
        'extra_platforms': {
            'linux64-sh-haz': {},
        },
    },
}

setMainFirefoxVersions(BRANCHES)

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])
    if 'mobile_platforms' in BRANCHES[branch]:
        if 'platforms' not in BRANCHES[branch]:
            BRANCHES[branch]['platforms'] = deepcopy(BRANCHES[branch]['mobile_platforms'])
        else:
            BRANCHES[branch]['platforms'].update(deepcopy(BRANCHES[branch]['mobile_platforms']))

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        # Don't override something that's set
        elif key in ('enable_weekly_bundle','branch_projects',) and key in BRANCHES[branch]:
            continue
        # If the key is already set then we won't override with GLOBAL_VARS
        # The "platforms" key is handle separatedely (see next for loop)
        elif key == 'platforms' or key not in BRANCHES[branch]:
            BRANCHES[branch][key] = deepcopy(value)

    BRANCHES[branch]['platforms'].update(BRANCHES[branch].get('extra_platforms', {}))

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
                    PROJECT_BRANCHES[branch]['platforms'].has_key(platform):
                for key, value in PROJECT_BRANCHES[branch]['platforms'][platform].items():
                    if key == 'env':
                        value = deepcopy(PLATFORM_VARS[platform]['env'])
                        value.update(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                    else:
                        value = deepcopy(value)
                    BRANCHES[branch]['platforms'][platform][key] = value

    # Copy in local config
    if branch in localconfig.BRANCHES:
        for key, value in localconfig.BRANCHES[branch].items():
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

    for platform, platform_config in localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Check for project branch removing a platform from default platforms
    if branch in ACTIVE_PROJECT_BRANCHES:
        for key, value in PROJECT_BRANCHES[branch].items():
            if key in ('platforms', 'mobile_platforms'):
                for platform, platform_config in value.items():
                    if platform_config.get('dont_build'):
                        del BRANCHES[branch]['platforms'][platform]

    # win64 builds run on a limited set of branches
    if branch not in ('try', 'mozilla-central', 'date', 'oak'):
        for platform in ('win64', 'win64-debug'):
            if platform in BRANCHES[branch]['platforms']:
                del BRANCHES[branch]['platforms'][platform]

    # linux64-cc builds only run on cedar for now
    if branch not in ('cedar',):
        for platform in ('linux64-cc',):
            if platform in BRANCHES[branch]['platforms']:
                del BRANCHES[branch]['platforms'][platform]

######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['mozilla-central']['enable_perproduct_builds'] = True
BRANCHES['mozilla-central']['enable_weekly_bundle'] = True
BRANCHES['mozilla-central']['start_hour'] = [3]
BRANCHES['mozilla-central']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-central']['enable_xulrunner'] = True
# Enable PGO Builds on this branch
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'
BRANCHES['mozilla-central']['periodic_start_hours'] = range(1, 24, 3)
BRANCHES['mozilla-central']['periodic_start_minute'] = 30
# Enable unit tests
BRANCHES['mozilla-central']['enable_mac_a11y'] = True
BRANCHES['mozilla-central']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
BRANCHES['mozilla-central']['enable_l10n_onchange'] = True
BRANCHES['mozilla-central']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-central']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-central']['l10nDatedDirs'] = True
BRANCHES['mozilla-central']['l10n_tree'] = 'fxcentral'
#make sure it has an ending slash
BRANCHES['mozilla-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-central-l10n/'
BRANCHES['mozilla-central']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-central'
BRANCHES['mozilla-central']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-central']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-central' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-central']['enable_multi_locale'] = True
BRANCHES['mozilla-central']['upload_mobile_symbols'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-central']['create_snippet'] = True
BRANCHES['mozilla-central']['update_channel'] = 'nightly'
BRANCHES['mozilla-central']['create_mobile_snippet'] = True
BRANCHES['mozilla-central']['create_partial'] = True
BRANCHES['mozilla-central']['create_partial_l10n'] = True
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_mobile_base_upload_dir'] = '/opt/aus2/incoming/2/Fennec/mozilla-central'
BRANCHES['mozilla-central']['aus2_mobile_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Fennec/mozilla-central'
BRANCHES['mozilla-central']['enable_blocklist_update'] = True
BRANCHES['mozilla-central']['enable_hsts_update'] = True
BRANCHES['mozilla-central']['enable_hpkp_update'] = True
BRANCHES['mozilla-central']['platforms']['android-armv6']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-armv6'
BRANCHES['mozilla-central']['platforms']['android-x86']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-x86'
BRANCHES['mozilla-central']['platforms']['linux']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['linux64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['win32']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['android']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['android-armv6']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['macosx64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['l10n_extra_configure_args'] = ['--with-macbundlename-prefix=Firefox']

######## mozilla-release
BRANCHES['mozilla-release']['repo_path'] = 'releases/mozilla-release'
BRANCHES['mozilla-release']['update_channel'] = 'release'
BRANCHES['mozilla-release']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['mozilla-release']['enable_weekly_bundle'] = True
BRANCHES['mozilla-release']['start_hour'] = [3]
BRANCHES['mozilla-release']['start_minute'] = [2]
BRANCHES['mozilla-release']['enable_xulrunner'] = False
# Enable PGO Builds on this branch
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'
# Enable unit tests
BRANCHES['mozilla-release']['enable_mac_a11y'] = True
# L10n configuration
BRANCHES['mozilla-release']['enable_l10n'] = False
BRANCHES['mozilla-release']['enable_l10n_onchange'] = True
BRANCHES['mozilla-release']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-release']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-release']['l10nDatedDirs'] = True
BRANCHES['mozilla-release']['l10n_tree'] = 'fxrel'
BRANCHES['mozilla-release']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-release'
BRANCHES['mozilla-release']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-release']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-release' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-release']['enable_multi_locale'] = True
BRANCHES['mozilla-release']['upload_mobile_symbols'] = True
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['mozilla-release']['enable_nightly'] = False
BRANCHES['mozilla-release']['enable_blocklist_update'] = True
BRANCHES['mozilla-release']['enable_valgrind'] = False
BRANCHES['mozilla-release']['enabled_products'] = ['firefox', 'mobile']
BRANCHES['mozilla-release']['platforms']['android-armv6']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-armv6'
BRANCHES['mozilla-release']['platforms']['android-x86']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-x86'

######## mozilla-beta
BRANCHES['mozilla-beta']['repo_path'] = 'releases/mozilla-beta'
BRANCHES['mozilla-beta']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['mozilla-beta']['enable_weekly_bundle'] = True
BRANCHES['mozilla-beta']['update_channel'] = 'beta'
BRANCHES['mozilla-beta']['start_hour'] = [3]
BRANCHES['mozilla-beta']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-beta']['enable_xulrunner'] = False
# Enable PGO Builds on this branch
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'
# Enable unit tests
BRANCHES['mozilla-beta']['enable_mac_a11y'] = True
BRANCHES['mozilla-beta']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-beta']['enable_l10n'] = False
BRANCHES['mozilla-beta']['enable_l10n_onchange'] = True
BRANCHES['mozilla-beta']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-beta']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                              'macosx64']
BRANCHES['mozilla-beta']['l10nDatedDirs'] = True
BRANCHES['mozilla-beta']['l10n_tree'] = 'fxbeta'
#make sure it has an ending slash
BRANCHES['mozilla-beta']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-beta-l10n/'
BRANCHES['mozilla-beta']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-beta'
BRANCHES['mozilla-beta']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-beta']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-beta' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-beta']['enable_multi_locale'] = True
BRANCHES['mozilla-beta']['upload_mobile_symbols'] = True
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['mozilla-beta']['enable_nightly'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-beta']['enable_blocklist_update'] = True
BRANCHES['mozilla-beta']['enable_valgrind'] = False
BRANCHES['mozilla-beta']['platforms']['android-armv6']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-armv6'
BRANCHES['mozilla-beta']['platforms']['android-x86']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-x86'
BRANCHES['mozilla-beta']['platforms']['android']['enable_dep'] = True
BRANCHES['mozilla-beta']['platforms']['android-debug']['enable_dep'] = True
BRANCHES['mozilla-beta']['enabled_products'] = ['firefox', 'mobile']
BRANCHES['mozilla-beta']['enable_perproduct_builds'] = True

######## mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = 'releases/mozilla-aurora'
BRANCHES['mozilla-aurora']['l10n_repo_path'] = 'releases/l10n/mozilla-aurora'
BRANCHES['mozilla-aurora']['enable_perproduct_builds'] = True
BRANCHES['mozilla-aurora']['enable_weekly_bundle'] = True
BRANCHES['mozilla-aurora']['start_hour'] = [0]
BRANCHES['mozilla-aurora']['start_minute'] = [40]
BRANCHES['mozilla-aurora']['periodic_start_hours'] = range(1, 24, 6)
BRANCHES['mozilla-aurora']['periodic_start_minute'] = 30
# Enable XULRunner / SDK builds
BRANCHES['mozilla-aurora']['enable_xulrunner'] = True
# Enable PGO Builds on this branch
BRANCHES['mozilla-aurora']['pgo_strategy'] = 'per-checkin'
# Enable unit tests
BRANCHES['mozilla-aurora']['enable_mac_a11y'] = True
BRANCHES['mozilla-aurora']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-aurora']['enable_l10n'] = True
BRANCHES['mozilla-aurora']['enable_l10n_onchange'] = True
BRANCHES['mozilla-aurora']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-aurora']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-aurora']['l10nDatedDirs'] = True
BRANCHES['mozilla-aurora']['l10n_tree'] = 'fxaurora'
#make sure it has an ending slash
BRANCHES['mozilla-aurora']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-aurora-l10n/'
BRANCHES['mozilla-aurora']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-aurora'
BRANCHES['mozilla-aurora']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-aurora']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-aurora' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-aurora']['enable_multi_locale'] = True
BRANCHES['mozilla-aurora']['upload_mobile_symbols'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-aurora']['create_snippet'] = True
BRANCHES['mozilla-aurora']['update_channel'] = 'aurora'
BRANCHES['mozilla-aurora']['create_mobile_snippet'] = True
BRANCHES['mozilla-aurora']['create_partial'] = True
BRANCHES['mozilla-aurora']['create_partial_l10n'] = True
# use mozilla-aurora-test when disabling updates for merges
BRANCHES['mozilla-aurora']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_mobile_base_upload_dir'] = '/opt/aus2/incoming/2/Fennec/mozilla-aurora'
BRANCHES['mozilla-aurora']['aus2_mobile_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Fennec/mozilla-aurora'
BRANCHES['mozilla-aurora']['enable_blocklist_update'] = True
BRANCHES['mozilla-aurora']['enable_hsts_update'] = True
BRANCHES['mozilla-aurora']['enable_hpkp_update'] = True
BRANCHES['mozilla-aurora']['enable_valgrind'] = False
BRANCHES['mozilla-aurora']['platforms']['android-armv6']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-armv6'
# aurora nightlies should use our nightly signing server
BRANCHES['mozilla-aurora']['platforms']['linux']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-aurora']['platforms']['linux64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-aurora']['platforms']['win32']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-aurora']['platforms']['macosx64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-aurora']['l10n_extra_configure_args'] = ['--with-macbundlename-prefix=Firefox']
BRANCHES['mozilla-aurora']['enabled_products'] = ['firefox', 'mobile']

######## mozilla-esr24
BRANCHES['mozilla-esr24']['repo_path'] = 'releases/mozilla-esr24'
BRANCHES['mozilla-esr24']['update_channel'] = 'nightly-esr24'
BRANCHES['mozilla-esr24']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['mozilla-esr24']['enable_weekly_bundle'] = True
BRANCHES['mozilla-esr24']['start_hour'] = [0]
BRANCHES['mozilla-esr24']['start_minute'] = [05]
BRANCHES['mozilla-esr24']['enable_xulrunner'] = False
BRANCHES['mozilla-esr24']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr24']['enable_mac_a11y'] = True
BRANCHES['mozilla-esr24']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-esr24']['enable_l10n'] = False
BRANCHES['mozilla-esr24']['enable_l10n_onchange'] = False
BRANCHES['mozilla-esr24']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-esr24']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                               'macosx64']
BRANCHES['mozilla-esr24']['l10nDatedDirs'] = True
BRANCHES['mozilla-esr24']['l10n_tree'] = 'fxesr24'
BRANCHES['mozilla-esr24']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-esr24'
BRANCHES['mozilla-esr24']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-esr24']['enable_nightly'] = True
BRANCHES['mozilla-esr24']['create_snippet'] = True
BRANCHES['mozilla-esr24']['create_partial'] = True
BRANCHES['mozilla-esr24']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-esr24'
BRANCHES['mozilla-esr24']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-esr24'
BRANCHES['mozilla-esr24']['enable_blocklist_update'] = True
BRANCHES['mozilla-esr24']['enable_hsts_update'] = True
BRANCHES['mozilla-esr24']['enable_valgrind'] = False
BRANCHES['mozilla-esr24']['enabled_products'] = ['firefox']

######## mozilla-esr31
BRANCHES['mozilla-esr31']['repo_path'] = 'releases/mozilla-esr31'
BRANCHES['mozilla-esr31']['update_channel'] = 'nightly-esr31'
BRANCHES['mozilla-esr31']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['mozilla-esr31']['enable_weekly_bundle'] = True
BRANCHES['mozilla-esr31']['start_hour'] = [0]
BRANCHES['mozilla-esr31']['start_minute'] = [05]
BRANCHES['mozilla-esr31']['enable_xulrunner'] = False
BRANCHES['mozilla-esr31']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr31']['enable_mac_a11y'] = True
BRANCHES['mozilla-esr31']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-esr31']['enable_l10n'] = False
BRANCHES['mozilla-esr31']['enable_l10n_onchange'] = False
BRANCHES['mozilla-esr31']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-esr31']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                               'macosx64']
BRANCHES['mozilla-esr31']['l10nDatedDirs'] = True
BRANCHES['mozilla-esr31']['l10n_tree'] = 'fxesr31'
BRANCHES['mozilla-esr31']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-esr31'
BRANCHES['mozilla-esr31']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-esr31']['enable_nightly'] = True
BRANCHES['mozilla-esr31']['create_snippet'] = True
BRANCHES['mozilla-esr31']['create_partial'] = True
BRANCHES['mozilla-esr31']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-esr31'
BRANCHES['mozilla-esr31']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-esr31'
BRANCHES['mozilla-esr31']['enable_blocklist_update'] = True
BRANCHES['mozilla-esr31']['enable_hsts_update'] = True
BRANCHES['mozilla-esr31']['enable_valgrind'] = False
BRANCHES['mozilla-esr31']['enabled_products'] = ['firefox']

######## mozilla-b2g28_v1_3
BRANCHES['mozilla-b2g28_v1_3']['repo_path'] = 'releases/mozilla-b2g28_v1_3'
BRANCHES['mozilla-b2g28_v1_3']['update_channel'] = 'nightly-b2g28'
BRANCHES['mozilla-b2g28_v1_3']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g28_v1_3']['enable_weekly_bundle'] = True
BRANCHES['mozilla-b2g28_v1_3']['enable_perproduct_builds'] = True
BRANCHES['mozilla-b2g28_v1_3']['start_hour'] = [3]
BRANCHES['mozilla-b2g28_v1_3']['start_minute'] = [45]
BRANCHES['mozilla-b2g28_v1_3']['enable_xulrunner'] = False
BRANCHES['mozilla-b2g28_v1_3']['pgo_platforms'] = []
BRANCHES['mozilla-b2g28_v1_3']['enable_mac_a11y'] = True
BRANCHES['mozilla-b2g28_v1_3']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-b2g28_v1_3']['enable_l10n'] = False
BRANCHES['mozilla-b2g28_v1_3']['enable_l10n_onchange'] = False
BRANCHES['mozilla-b2g28_v1_3']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-b2g28_v1_3']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                               'macosx64']
BRANCHES['mozilla-b2g28_v1_3']['l10nDatedDirs'] = True
BRANCHES['mozilla-b2g28_v1_3']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-b2g28_v1_3'
BRANCHES['mozilla-b2g28_v1_3']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-b2g28_v1_3']['enable_nightly'] = False
BRANCHES['mozilla-b2g28_v1_3']['create_snippet'] = False
BRANCHES['mozilla-b2g28_v1_3']['create_partial'] = False
BRANCHES['mozilla-b2g28_v1_3']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-b2g28_v1_3'
BRANCHES['mozilla-b2g28_v1_3']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-b2g28_v1_3'
BRANCHES['mozilla-b2g28_v1_3']['enable_blocklist_update'] = False
BRANCHES['mozilla-b2g28_v1_3']['enable_hsts_update'] = True
BRANCHES['mozilla-b2g28_v1_3']['enable_hpkp_update'] = True
BRANCHES['mozilla-b2g28_v1_3']['enable_valgrind'] = False
BRANCHES['mozilla-b2g28_v1_3']['enabled_products'] = ['firefox', 'mobile']

######## mozilla-b2g28_v1_3t
BRANCHES['mozilla-b2g28_v1_3t']['repo_path'] = 'releases/mozilla-b2g28_v1_3t'
BRANCHES['mozilla-b2g28_v1_3t']['enable_l10n'] = False
BRANCHES['mozilla-b2g28_v1_3t']['enable_nightly'] = False
BRANCHES['mozilla-b2g28_v1_3t']['enable_xulrunner'] = False
BRANCHES['mozilla-b2g28_v1_3t']['enable_valgrind'] = False

######## mozilla-b2g30_v1_4
BRANCHES['mozilla-b2g30_v1_4']['repo_path'] = 'releases/mozilla-b2g30_v1_4'
BRANCHES['mozilla-b2g30_v1_4']['update_channel'] = 'nightly-b2g30'
BRANCHES['mozilla-b2g30_v1_4']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g30_v1_4']['enable_weekly_bundle'] = True
BRANCHES['mozilla-b2g30_v1_4']['enable_perproduct_builds'] = True
BRANCHES['mozilla-b2g30_v1_4']['start_hour'] = [3]
BRANCHES['mozilla-b2g30_v1_4']['start_minute'] = [45]
BRANCHES['mozilla-b2g30_v1_4']['enable_xulrunner'] = False
BRANCHES['mozilla-b2g30_v1_4']['pgo_platforms'] = []
BRANCHES['mozilla-b2g30_v1_4']['enable_mac_a11y'] = True
BRANCHES['mozilla-b2g30_v1_4']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-b2g30_v1_4']['enable_l10n'] = False
BRANCHES['mozilla-b2g30_v1_4']['enable_l10n_onchange'] = False
BRANCHES['mozilla-b2g30_v1_4']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-b2g30_v1_4']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                               'macosx64']
BRANCHES['mozilla-b2g30_v1_4']['l10nDatedDirs'] = True
BRANCHES['mozilla-b2g30_v1_4']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-b2g30_v1_4'
BRANCHES['mozilla-b2g30_v1_4']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-b2g30_v1_4']['enable_nightly'] = False
BRANCHES['mozilla-b2g30_v1_4']['create_snippet'] = False
BRANCHES['mozilla-b2g30_v1_4']['create_partial'] = False
BRANCHES['mozilla-b2g30_v1_4']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-b2g30_v1_4'
BRANCHES['mozilla-b2g30_v1_4']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-b2g30_v1_4'
BRANCHES['mozilla-b2g30_v1_4']['enable_blocklist_update'] = False
BRANCHES['mozilla-b2g30_v1_4']['enable_hsts_update'] = True
BRANCHES['mozilla-b2g30_v1_4']['enable_hpkp_update'] = True
BRANCHES['mozilla-b2g30_v1_4']['enable_valgrind'] = False
BRANCHES['mozilla-b2g30_v1_4']['enabled_products'] = ['firefox', 'mobile']

######## mozilla-b2g32_v2_0
BRANCHES['mozilla-b2g32_v2_0']['repo_path'] = 'releases/mozilla-b2g32_v2_0'
BRANCHES['mozilla-b2g32_v2_0']['update_channel'] = 'nightly-b2g32'
BRANCHES['mozilla-b2g32_v2_0']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['mozilla-b2g32_v2_0']['enable_weekly_bundle'] = True
BRANCHES['mozilla-b2g32_v2_0']['enable_perproduct_builds'] = True
BRANCHES['mozilla-b2g32_v2_0']['start_hour'] = [3]
BRANCHES['mozilla-b2g32_v2_0']['start_minute'] = [45]
BRANCHES['mozilla-b2g32_v2_0']['enable_xulrunner'] = False
BRANCHES['mozilla-b2g32_v2_0']['pgo_platforms'] = []
BRANCHES['mozilla-b2g32_v2_0']['enable_mac_a11y'] = True
BRANCHES['mozilla-b2g32_v2_0']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-b2g32_v2_0']['enable_l10n'] = False
BRANCHES['mozilla-b2g32_v2_0']['enable_l10n_onchange'] = False
BRANCHES['mozilla-b2g32_v2_0']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-b2g32_v2_0']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                               'macosx64']
BRANCHES['mozilla-b2g32_v2_0']['l10nDatedDirs'] = True
BRANCHES['mozilla-b2g32_v2_0']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-b2g32_v2_0'
BRANCHES['mozilla-b2g32_v2_0']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-b2g32_v2_0']['enable_nightly'] = False
BRANCHES['mozilla-b2g32_v2_0']['create_snippet'] = False
BRANCHES['mozilla-b2g32_v2_0']['create_partial'] = False
BRANCHES['mozilla-b2g32_v2_0']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-b2g32_v2_0'
BRANCHES['mozilla-b2g32_v2_0']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-b2g32_v2_0'
BRANCHES['mozilla-b2g32_v2_0']['enable_blocklist_update'] = False
BRANCHES['mozilla-b2g32_v2_0']['enable_hsts_update'] = True
BRANCHES['mozilla-b2g32_v2_0']['enable_hpkp_update'] = True
BRANCHES['mozilla-b2g32_v2_0']['enable_valgrind'] = False
BRANCHES['mozilla-b2g32_v2_0']['enabled_products'] = ['firefox', 'mobile']

######## try
# Try-specific configs
BRANCHES['try']['stage_username'] = 'trybld'
BRANCHES['try']['stage_username_mobile'] = 'trybld'
BRANCHES['try']['stage_ssh_key'] = 'trybld_dsa'
BRANCHES['try']['stage_ssh_mobile_key'] = 'trybld_dsa'
BRANCHES['try']['stage_base_path'] = '/home/ftp/pub/firefox/try-builds'
BRANCHES['try']['stage_base_path_mobile'] = '/home/ftp/pub/firefox/try-builds'
BRANCHES['try']['enable_merging'] = False
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['pgo_strategy'] = 'try'
BRANCHES['try']['package_dir'] = '%(who)s-%(got_revision)s'
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try']['repo_path'] = 'try'
BRANCHES['try']['start_hour'] = [3]
BRANCHES['try']['start_minute'] = [2]
# Disable Nightly builds
BRANCHES['try']['enable_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['try']['enable_xulrunner'] = False
BRANCHES['try']['enable_mac_a11y'] = True
# only do unittests locally until they are switched over to talos-r3
BRANCHES['try']['enable_l10n'] = False
BRANCHES['try']['enable_l10n_onchange'] = False
BRANCHES['try']['l10nNightlyUpdate'] = False
BRANCHES['try']['l10nDatedDirs'] = False
BRANCHES['try']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['try']['aus2_base_upload_dir'] = 'fake'
BRANCHES['try']['platforms']['linux']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-mulet']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['win32']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['win64']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['win64-debug']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['macosx64']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-asan']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-asan-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-st-an-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-sh-haz']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-br-haz']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['macosx64-debug']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['android']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['android-armv6']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['android-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['android-x86']['slaves'] = TRY_SLAVES['mock']
for platform in BRANCHES['try']['platforms'].keys():
    # Sadly, the rule that mobile builds go to /mobile/
    # isn't true for try :(
    BRANCHES['try']['platforms'][platform]['stage_product'] = 'firefox'
    # Disable symbol upload across the board
    BRANCHES['try']['platforms'][platform]['upload_symbols'] = False

######## generic branch configs
for branch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[branch]
    BRANCHES[branch]['product_name'] = branchConfig.get('product_name', None)
    BRANCHES[branch]['app_name'] = branchConfig.get('app_name', None)
    BRANCHES[branch]['brand_name'] = branchConfig.get('brand_name', None)
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['enabled_products'] = branchConfig.get('enabled_products',
                                                            GLOBAL_VARS['enabled_products'])
    BRANCHES[branch]['enable_nightly'] = branchConfig.get('enable_nightly', False)
    BRANCHES[branch]['enable_nightly_everytime'] = branchConfig.get('enable_nightly_everytime', False)
    BRANCHES[branch]['enable_mobile'] = branchConfig.get('enable_mobile', True)
    BRANCHES[branch]['pgo_strategy'] = branchConfig.get('pgo_strategy', None)
    BRANCHES[branch]['periodic_start_hours'] = branchConfig.get('periodic_start_hours', range(0, 24, 6))
    BRANCHES[branch]['periodic_start_minute'] = branchConfig.get('periodic_start_minute', 30)
    BRANCHES[branch]['start_hour'] = branchConfig.get('start_hour', [4])
    BRANCHES[branch]['start_minute'] = branchConfig.get('start_minute', [2])
    # Disable XULRunner / SDK builds
    BRANCHES[branch]['enable_xulrunner'] = branchConfig.get('enable_xulrunner', False)
    # Enable unit tests
    BRANCHES[branch]['enable_mac_a11y'] = branchConfig.get('enable_mac_a11y', True)
    BRANCHES[branch]['unittest_build_space'] = branchConfig.get('unittest_build_space', 6)
    # L10n configuration is not set up for project_branches
    BRANCHES[branch]['enable_l10n'] = branchConfig.get('enable_l10n', False)
    BRANCHES[branch]['l10nNightlyUpdate'] = branchConfig.get('l10nNightlyUpdate', False)
    BRANCHES[branch]['l10nDatedDirs'] = branchConfig.get('l10nDatedDirs', False)
    # nightly updates
    BRANCHES[branch]['create_snippet'] = branchConfig.get('create_snippet', False)
    BRANCHES[branch]['update_channel'] = branchConfig.get('update_channel', 'nightly-%s' % branch)
    BRANCHES[branch]['create_partial'] = branchConfig.get('create_partial', False)
    BRANCHES[branch]['create_partial_l10n'] = branchConfig.get('create_partial_l10n', False)
    BRANCHES[branch]['create_mobile_snippet'] = branchConfig.get('create_mobile_snippet', False)
    BRANCHES[branch]['aus2_user'] = branchConfig.get('aus2_user', GLOBAL_VARS['aus2_user'])
    BRANCHES[branch]['aus2_ssh_key'] = branchConfig.get('aus2_ssh_key', GLOBAL_VARS['aus2_ssh_key'])
    BRANCHES[branch]['aus2_base_upload_dir'] = branchConfig.get('aus2_base_upload_dir', '/opt/aus2/incoming/2/Firefox/' + branch)
    BRANCHES[branch]['aus2_base_upload_dir_l10n'] = branchConfig.get('aus2_base_upload_dir_l10n', '/opt/aus2/incoming/2/Firefox/' + branch)
    BRANCHES[branch]['aus2_mobile_base_upload_dir'] = branchConfig.get('aus2_mobile_base_upload_dir', '/opt/aus2/incoming/2/Fennec/' + branch)
    BRANCHES[branch]['aus2_mobile_base_upload_dir_l10n'] = branchConfig.get('aus2_mobile_base_upload_dir_l10n', '/opt/aus2/incoming/2/Fennec/' + branch)
    #make sure it has an ending slash
    BRANCHES[branch]['l10nUploadPath'] = \
        '/home/ftp/pub/mozilla.org/firefox/nightly/latest-' + branch + '-l10n/'
    BRANCHES[branch]['enUS_binaryURL'] = GLOBAL_VARS['download_base_url'] + branchConfig.get('enUS_binaryURL', '')
    if 'linux' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
    if 'android' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['android']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
    if 'android-armv6' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['android-armv6']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-armv6-' + branch
    if 'android-x86' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['android-x86']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'android-x86-' + branch
    if 'linux64' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-' + branch
    if 'win32' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
    if 'macosx64' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-' + branch
    # Platform-specific defaults/interpretation
    for platform in BRANCHES[branch]['platforms']:
        # point to the mozconfigs, default is generic
        if platform.endswith('debug') and 'android' not in platform:
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

#bug 1042835 Disable armv6 builds and tests everywhere apart from esr31
branches = BRANCHES.keys()
branches.extend(ACTIVE_PROJECT_BRANCHES)
for branch in branches:
    if 'android-armv6' in BRANCHES[branch]['platforms']:
        del BRANCHES[branch]['platforms']['android-armv6']


# Bug 578880, remove the following block after gcc-4.5 switch
branches = BRANCHES.keys()
branches.extend(ACTIVE_PROJECT_BRANCHES)
for branch in branches:
    if 'linux' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['linux']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
        BRANCHES[branch]['platforms']['linux']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if 'linux64' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['linux64']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib64'
        BRANCHES[branch]['platforms']['linux64']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
        }
    if 'linux-debug' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['linux-debug']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib:%s/dist/bin' % OBJDIR
        BRANCHES[branch]['platforms']['linux-debug']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
        }
    if 'linux64-debug' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['linux64-debug']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib64:%s/dist/bin' % OBJDIR
        BRANCHES[branch]['platforms']['linux64-debug']['unittest-env'] = {
            'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
        }

# Expand out the branch_projects into a full PROJECT object per branch. This
# must come after the BRANCHES configuration above, so that
# BRANCHES[*]['enable_try'] is set when appropriate.
for b, branch in BRANCHES.items():
    for name in branch.get('branch_projects', []):
        branch_project = BRANCH_PROJECTS[name]
        if branch.get('enable_try', False) != branch_project.get('enable_try', False):
            continue

        project = deepcopy(branch_project)
        project['project_name'] = name
        project['branch'] = b
        project['branchconfig'] = branch
        branch_project_name = '%s__%s' % (name, b)
        assert branch_project_name not in PROJECTS, '%s already in PROJECTS' % name
        PROJECTS[branch_project_name] = project

for _, branch in items_before(BRANCHES, 'gecko_version', 26):
    for p in 'linux64-asan', 'linux64-asan-debug':
        if p in branch['platforms']:
            del branch['platforms'][p]

# ant test on try
## ant rides the trains (Bug 971841)
# for name, branch in items_before(BRANCHES, 'gecko_version', 30):
for name, branch in BRANCHES.items():
    if "try" in name:
        continue # Remove this condition when we switch to riding trains
    for plat, pc in branch['platforms'].items():
        if 'mock_packages' in pc and "android" in plat:
            pc['mock_packages'] = \
                [x for x in pc['mock_packages'] if x not in (
                    'ant', 'ant-apache-regexp',
                )]

# Don't schedule non-unified builds anywhere except on m-c and derived branches
mc_gecko_version = BRANCHES['mozilla-central']['gecko_version']
for name, branch in items_before(BRANCHES, 'gecko_version', mc_gecko_version):
    for pc in branch['platforms'].values():
        if 'enable_nonunified_build' in pc:
            pc['enable_nonunified_build'] = False
# Don't try to schedule non-unified builds on Try either
for branch in ("try",):
    for pc in BRANCHES[branch]['platforms'].values():
        if 'enable_nonunified_build' in pc:
            pc['enable_nonunified_build'] = False

# Static analysis happens only on m-c and derived branches.
for name, branch in items_before(BRANCHES, 'gecko_version', mc_gecko_version):
    if 'linux64-st-an-debug' in branch['platforms']:
        del branch['platforms']['linux64-st-an-debug']

# Only test pretty names on train branches, not m-c or project branches.
# That's also forced on nonunified builds in buildbotcustom.
for branch in ("mozilla-aurora", "mozilla-beta", "mozilla-release",
               "mozilla-esr24", "mozilla-esr31"):
    for platform in ("linux", "linux64", "macosx64", "win32", "win64"):
        if platform in BRANCHES[branch]['platforms']:
            BRANCHES[branch]['platforms'][platform]['test_pretty_names'] = True

# Mulet landed in gecko 34
for name, branch in items_before(BRANCHES, 'gecko_version', 34):
    if 'linux64-mulet' in branch['platforms']:
        del branch['platforms']['linux64-mulet']

# Exact rooting landed for desktop only in 28.
for name, branch in items_before(BRANCHES, 'gecko_version', 28):
    if 'linux64-br-haz' in branch['platforms']:
        del branch['platforms']['linux64-br-haz']
for name, branch in items_at_least(BRANCHES, 'gecko_version', 28):
    # b2g cannot use exact rooting yet since it has known hazards. If a
    # b2g-only tree were to acquire additional desktop-only hazard, we
    # currently would not care. Eventually, we will get the analysis running on
    # b2g, fix the hazards, turn on exact rooting for b2g, and then turn these
    # builds on.
    if 'b2g' in name and 'inbound' not in name:
        if 'linux64-br-haz' in branch['platforms']:
            del branch['platforms']['linux64-br-haz']

# B2G's INBOUND
for b in ('b2g-inbound',):
    for p in BRANCHES[b]['platforms'].keys():
        if 'linux' not in p:
            BRANCHES[b]['platforms'][p]['enable_checktests'] = False
# END B2G's INBOUND

# desktop repacks with mozharness
for name, branch in BRANCHES.items():
    if branch.get('desktop_mozharness_repacks_enabled'):
        for platform_name in branch['platforms']:
            if platform_name in GLOBAL_VARS['mozharness_desktop_l10n_platforms']:
                pf = branch['platforms'][platform_name]
                pf['desktop_mozharness_repacks_enabled'] = True
        continue
    # for all other branches delete mozharness_desktop_l10n
    for p in branch["platforms"]:
        if "mozharness_desktop_l10n" in p:
            del p["mozharness_desktop_l10n"]

# Bug 950206 - Enable 32-bit Windows builds on Date, test those builds on tst-w64-ec2-XXXX
BRANCHES['date']['platforms']['win32']['unittest_platform'] = 'win64-opt'

if __name__ == "__main__":
    import sys
    import pprint
    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = dict(BRANCHES.items() + PROJECTS.items())

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)
