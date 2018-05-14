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
    'objdir': 'obj-firefox',
    'objdir_unittests': 'objdir',
    'stage_username': 'ffxbld',
    'stage_base_path': '/home/ftp/pub',
    'stage_group': None,
    'stage_ssh_key': 'ffxbld_rsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_ffx/',
    'symbol_server_post_upload_cmd': '/usr/local/bin/post-symbol-upload.py',
    'symbol_server_mobile_path': '/mnt/netapp/breakpad/symbols_mob/',
    'balrog_credentials_file': 'BuildSlaves.py',
    'hg_username': 'ffxbld',
    'hg_ssh_key': '~cltbld/.ssh/ffxbld_rsa',
    'graph_selector': '/server/collect.cgi',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'mozharness_repo_path': 'build/mozharness',
    'mozharness_tag': 'production',
    'script_repo_manifest': 'https://hg.mozilla.org/%(repo_path)s/raw-file/%(revision)s/' + \
                            'testing/mozharness/mozharness.json',
    # mozharness_archiver_repo_path tells the factory to use a copy of mozharness from within the
    #  gecko tree and also allows us to overwrite which gecko repo to use. Useful for platforms
    # like Thunderbird
    'mozharness_archiver_repo_path': '%(repo_path)s',
    'use_mozharness_repo_cache': True,
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
        'win32-devedition': {},
        'win32-add-on-devel': {},
        'win64': {},
        'win64-devedition': {},
        'win64-add-on-devel': {},
        'macosx64': {},
        'macosx64-devedition': {},
        'linux-debug': {},
        'linux64-debug': {},
        'linux64-asan': {},
        'linux64-asan-debug': {},
        'linux64-av': {},
        'linux64-devedition': {},
        'macosx64-debug': {},
        'win32-debug': {},
        'win64-debug': {},
        'android-api-15': {},
        'android-x86': {},
        'android-api-15-debug': {},
    },
    'pgo_strategy': None,
    'pgo_platforms': ('linux', 'win32', 'win64',),
    'periodic_start_hours': range(0, 24, 6),
    'enable_blocklist_update': False,
    'enable_hsts_update': False,
    'enable_hpkp_update': False,
    'file_update_on_closed_tree': False,
    'file_update_set_approval': True,
    'enable_nightly': True,
    'enabled_products': ['firefox', 'mobile'],

    # List of keys in BRANCH_PROJECTS that will be activated for the BRANCH
    'branch_projects': ['spidermonkey_tier_1'],

    'hash_type': 'sha512',
    'updates_enabled': False,
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

}
GLOBAL_VARS.update(localconfig.GLOBAL_VARS.copy())

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']

GLOBAL_ENV = {
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_AUTOMATION': '1',
}

PLATFORM_VARS = {
        'linux': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': [
                '/tools/checkouts/mozharness/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt', '-n', '1', '-z'
            ],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_32_builds.py',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 6,
                'use_credentials_file': True,
                'script_timeout': 1800,
                'script_maxtime': 2 * 3600,
            },
            'dep_signing_servers': 'dep-signing',
            'base_name': 'Linux %(branch)s',
            'product_name': 'firefox',
            'unittest_platform': 'linux-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'mozconfig': 'linux/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/linux32/nightly',
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
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': None,
            'test_pretty_names': False,
            'l10n_check_test': True,
            'nightly_signing_servers': 'dep-signing',
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux32/releng.manifest',
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
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/google-oauth-api.key', '/builds/google-oauth-api.key'),
                ('/builds/mozilla-desktop-geoloc-api.key', '/builds/mozilla-desktop-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
            ],
        },
        'linux64': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': [
                '/tools/checkouts/mozharness/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt', '-n', '1', '-z'
            ],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 6,
                'use_credentials_file': True,
                'script_timeout': 1800,
                'script_maxtime': 2 * 3600,
            },
            'enable_nightly': False,
            'product_name': 'firefox',
            'unittest_platform': 'linux64-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/linux64/nightly',
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
            'enable_checktests': True,
            'enable_build_analysis': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': False,
            'l10n_check_test': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
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
                        'dbus-x11',
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
                ('/builds/google-oauth-api.key', '/builds/google-oauth-api.key'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/builds/mozilla-desktop-geoloc-api.key', '/builds/mozilla-desktop-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
            ],
        },
        'linux64-av': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
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
        'linux64-asan': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': [
                '/tools/checkouts/mozharness/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt', '-n', '1', '-z'
            ],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'asan',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
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
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': False,
            'updates_enabled': False,
            'create_partial': False,
            'test_pretty_names': False,
            'l10n_check_test': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/asan.manifest',
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
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/google-oauth-api.key', '/builds/google-oauth-api.key'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/builds/mozilla-desktop-geoloc-api.key', '/builds/mozilla-desktop-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
            ],
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
        },
        'linux64-asan-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': [
                '/tools/checkouts/mozharness/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt', '-n', '1', '-z'
            ],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'asan-and-debug',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
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
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
                'PATH': '/tools/buildbot/bin:/usr/local/bin:/usr/lib64/ccache:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/tools/git/bin:/tools/python27/bin:/tools/python27-mercurial/bin:/home/cltbld/bin',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'enable_build_analysis': False,
            'updates_enabled': False,
            'create_partial': False,
            'test_pretty_names': False,
            'l10n_check_test': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/linux64/asan.manifest',
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
                        ],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/google-oauth-api.key', '/builds/google-oauth-api.key'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/builds/mozilla-desktop-geoloc-api.key', '/builds/mozilla-desktop-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
            ],
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
        },
        'linux64-devedition': {},
        'macosx64': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt', '-n', '1', '-z'],
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_mac_64_builds.py',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 8,
                'use_credentials_file': True,
                'script_timeout': 1800,
                'script_maxtime': 3 * 3600,
            },

            'product_name': 'firefox',
            'unittest_platform': 'macosx64-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'OS X 10.7 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/macosx-universal/nightly',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'macosx64',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
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
            'enable_ccache': True,
        },
        'macosx64-devedition': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt', '-n', '1', '-z'],
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_mac_64_builds.py',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                    '--custom-build-variant-cfg', 'devedition',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 8,
                'use_credentials_file': True,
                'script_timeout': 1800,
                'script_maxtime': 3 * 3600,
            },

            'product_name': 'firefox',
            'unittest_platform': 'macosx64-devedition',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'OS X 10.7 %(branch)s devedition',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/macosx-universal/devedition',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx64-lion'],
            'platform_objdir': OBJDIR,
            'stage_product': 'devedition',
            'stage_platform': 'macosx64',
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
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
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(7.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 20,
                'use_credentials_file': True,
                'script_timeout': 2 * 3600,
                'script_maxtime': 3 * 3600,
            },

            'product_name': 'firefox',
            'unittest_platform': 'win32-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/win32/nightly',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'enable_installer': True,
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
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
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
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'win32-devedition': {
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
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                    '--custom-build-variant-cfg', 'devedition',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(7.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 20,
                'use_credentials_file': True,
                'script_timeout': 2 * 3600,
                'script_maxtime': 3 * 3600,
            },

            'product_name': 'firefox',
            'unittest_platform': 'win32-devedition',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 5.2 %(branch)s devedition',
            'mozconfig': 'win32/%(branch)s/nightly',
            'src_mozconfig': 'browser/config/mozconfigs/win32/devedition',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'slaves': SLAVES['win64-rev2'],
            'l10n_slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'devedition',
            'stage_platform': 'win32',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
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
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'win32-add-on-devel': {
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
                    '--custom-build-variant-cfg', 'add-on-devel',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 20,
                'use_credentials_file': True,
                'script_timeout': 2 * 3600,
                'script_maxtime': 3 * 3600,
            },

            'product_name': 'firefox',
            'unittest_platform': 'win32-add-on-devel-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 5.2 add-on-devel %(branch)s',
            'mozconfig': 'win32/%(branch)s/add-on-devel',
            'src_mozconfig': 'browser/config/mozconfigs/win32/add-on-devel',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'slaves': SLAVES['win64-rev2'],
            'l10n_slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win32-add-on-devel',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
            },
            'test_pretty_names': False,
            'updates_enabled': False,
            'l10n_check_test': True,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win32/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'win64': {
            'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_windows_64_builds.py',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(7.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 20,
                'use_credentials_file': True,
                'script_timeout': 2 * 3600,
                'script_maxtime': 3 * 3600,
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
            'profiled_build': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'enable_installer': True,
            'packageTests': True,
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
                'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'win64-devedition': {
            'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_windows_64_builds.py',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                    '--custom-build-variant-cfg', 'devedition',
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(7.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 20,
                'use_credentials_file': True,
                'script_timeout': 2 * 3600,
                'script_maxtime': 3 * 3600,
            },
            'reboot_command': [
                'c:/mozilla-build/python27/python', '-u',
                'scripts/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt','-n', '1', '-z'
            ],

            'product_name': 'firefox',
            'unittest_platform': 'win64-devedition',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 6.1 x86-64 %(branch)s devedition',
            'src_mozconfig': 'browser/config/mozconfigs/win64/devedition',
            'mozconfig': 'win64/%(branch)s/nightly',
            'profiled_build': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'devedition',
            'stage_platform': 'win64',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86_64-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
            'test_pretty_names': True,
            'l10n_check_test': True,
            # These refer to items in passwords.secrets
            # nightly_signing_servers defaults to dep-signing because we don't want
            # random new branches to accidentally use nightly-signing, which signs
            # with valid keys. Any branch that needs to be signed with these keys
            # must be overridden explicitly.
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'win64-add-on-devel': {
            'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_windows_64_builds.py',
                    '--custom-build-variant-cfg', 'add-on-devel',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'mozharness_desktop_l10n': {
                'capable': True,
                'scriptName': 'scripts/desktop_l10n.py',
                'l10n_chunks': 20,
                'use_credentials_file': True,
                'script_timeout': 2 * 3600,
                'script_maxtime': 3 * 3600,
            },
            'reboot_command': [
                'c:/mozilla-build/python27/python', '-u',
                'scripts/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt','-n', '1', '-z'
            ],

            'product_name': 'firefox',
            'unittest_platform': 'win64-add-on-devel-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'WINNT 6.1 x86-64 add-on-devel %(branch)s',
            'src_mozconfig': 'browser/config/mozconfigs/win64/add-on-devel',
            'mozconfig': 'win64/%(branch)s/add-on-devel',
            'profiled_build': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'enable_installer': True,
            'packageTests': True,
            'slaves': SLAVES['win64-rev2'],
            'platform_objdir': OBJDIR,
            'stage_product': 'firefox',
            'stage_platform': 'win64-add-on-devel',
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86_64-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
            },
            'enable_opt_unittests': False,
            'updates_enabled': False,
            'test_pretty_names': True,
            'l10n_check_test': True,
            # The status of this build doesn't affect the last good revision
            # algorithm for nightlies
            'consider_for_nightly': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        'linux-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': [
                '/tools/checkouts/mozharness/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt', '-n', '1', '-z'
            ],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_32_builds.py',
                    '--custom-build-variant-cfg', 'debug',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },

            'enable_nightly': False,
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
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/google-oauth-api.key', '/builds/google-oauth-api.key'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/builds/mozilla-desktop-geoloc-api.key', '/builds/mozilla-desktop-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
            ],
        },
        'linux64-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': [
                '/tools/checkouts/mozharness/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt', '-n', '1', '-z'
            ],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_linux_64_builds.py',
                    '--custom-build-variant-cfg', 'debug',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },

            'enable_nightly': False,
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
                ('/builds/gapi.data', '/builds/gapi.data'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
                ('/builds/google-oauth-api.key', '/builds/google-oauth-api.key'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/builds/mozilla-desktop-geoloc-api.key', '/builds/mozilla-desktop-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
            ],
        },
        'macosx64-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'reboot_command': ['scripts/external_tools/count_and_reboot.py',
                               '-f', '../reboot_count.txt', '-n', '1', '-z'],
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_mac_64_builds.py',
                    '--custom-build-variant-cfg', 'debug',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },

            'enable_nightly': False,
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
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(7.5 * 3600),
            },

            'enable_nightly': False,
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
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'HG_SHARE_BASE_DIR': 'c:/builds/hg-shared',
                'BINSCOPE': 'C:\Program Files (x86)\Microsoft\SDL BinScope\BinScope.exe',
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
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
            'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_windows_64_builds.py',
                    '--custom-build-variant-cfg', 'debug',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(7.5 * 3600),
            },
            'reboot_command': [
                'c:/mozilla-build/python27/python', '-u',
                'scripts/external_tools/count_and_reboot.py',
                '-f', '../reboot_count.txt','-n', '1', '-z'
            ],
            'enable_nightly': False,
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
                'PATH': "${MOZILLABUILD}\\nsis-3.0b1;${MOZILLABUILD}\\nsis-2.46u;${MOZILLABUILD}\\python27;${MOZILLABUILD}\\buildbotve\\scripts;${PATH}",
                'TOOLTOOL_CACHE': '/c/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/c/builds',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': None,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'consider_for_nightly': False,
            'tooltool_manifest_src': 'browser/config/tooltool-manifests/win64/releng.manifest',
            'tooltool_script': ['python', '/c/mozilla-build/tooltool.py'],
        },
        # In release promotion, the API level is just used to name an identify API-agnostic
        # machines. Thus, there is no need to upgrade/define a new config for higher APIs.
        # For more details, see https://bugzilla.mozilla.org/show_bug.cgi?id=1384482#c85
        # and following comments.
        'android-api-15': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_android_64_builds.py',
                    '--custom-build-variant-cfg', 'api-15',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'product_name': 'firefox',
            'unittest_platform': 'android-api-15-opt',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Android armv7 API 15+ %(branch)s',
            'mozconfig': 'in_tree',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android-api-15/nightly',
            'mobile_dir': 'mobile/android',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 16,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'create_partial': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64-android',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial',
                              'ccache', 'zip',
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
                ('/builds/mozilla-fennec-geoloc-api.key', '/builds/mozilla-fennec-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/builds/adjust-sdk.token', '/builds/adjust-sdk.token'),
                ('/builds/adjust-sdk-beta.token', '/builds/adjust-sdk-beta.token'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
            ],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
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
            'stage_platform': "android-api-15",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
            'is_mobile_l10n': True,
            'l10n_chunks': 5,
            'multi_locale': True,
            'multi_locale_script': 'scripts/multil10n.py',
            'multi_locale_config_platform': 'android',
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'],
            'update_platform': 'Android_arm-eabi-gcc3',
            'updates_enabled': False,
        },
        'android-x86': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'tools_repo_cache': '/tools/checkouts/build-tools',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_android_64_builds.py',
                    '--custom-build-variant-cfg', 'x86',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
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
                              'ccache', 'yasm', 'zip',
                              'java-1.7.0-openjdk-devel', 'zlib-devel',
                              'glibc-static', 'openssh-clients', 'mpfr', 'bc',
                              "gcc472_0moz1", "gcc473_0moz1", 'glibc.i686', 'libstdc++.i686',
                              'zlib.i686', 'freetype-2.3.11-6.el6_1.8.x86_64', 'ant', 'ant-apache-regexp'],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/mozilla-api.key', '/builds/mozilla-api.key'),
                ('/builds/mozilla-fennec-geoloc-api.key', '/builds/mozilla-fennec-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/builds/adjust-sdk.token', '/builds/adjust-sdk.token'),
                ('/builds/adjust-sdk-beta.token', '/builds/adjust-sdk-beta.token'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
            ],
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
            'tooltool_script': ['/builds/tooltool.py'],
            'updates_enabled': False,
        },
        'android-api-15-debug': {
            'mozharness_python': '/tools/buildbot/bin/python',
            'mozharness_desktop_build': {
                'script_name': 'scripts/fx_desktop_build.py',
                'extra_args': [
                    '--config', 'builds/releng_base_android_64_builds.py',
                    '--custom-build-variant-cfg', 'api-15-debug',
                    '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
                ],
                'script_timeout': 3 * 3600,
                'script_maxtime': int(5.5 * 3600),
            },
            'enable_nightly': False,
            'product_name': 'firefox',
            'unittest_platform': 'android-api-15-debug',
            'app_name': 'browser',
            'brand_name': 'Minefield',
            'base_name': 'Android armv7 API 15+ %(branch)s debug',
            'mozconfig': 'in_tree',
            'src_mozconfig': 'mobile/android/config/mozconfigs/android-api-15/debug',
            'mobile_dir': 'mobile/android',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 14,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'updates_enabled': False,
            'create_partial': False,
            'slaves': SLAVES['mock'],
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'nightly_signing_servers': 'dep-signing',
            'dep_signing_servers': 'dep-signing',
            'use_mock': True,
            'mock_target': 'mozilla-centos6-x86_64-android',
            'mock_packages': ['autoconf213', 'mozilla-python27-mercurial',
                              'ccache', 'zip', "gcc472_0moz1", "gcc473_0moz1",
                              'java-1.7.0-openjdk-devel', 'zlib-devel',
                              'glibc-static', 'openssh-clients', 'mpfr',
                              'wget', 'glibc.i686', 'libstdc++.i686',
                              'zlib.i686', 'freetype-2.3.11-6.el6_1.8.x86_64', 'ant', 'ant-apache-regexp'],
            'mock_copyin_files': [
                ('/home/cltbld/.ssh', '/home/mock_mozilla/.ssh'),
                ('/home/cltbld/.hgrc', '/builds/.hgrc'),
                ('/home/cltbld/.boto', '/builds/.boto'),
                ('/builds/mozilla-api.key', '/builds/mozilla-api.key'),
                ('/builds/mozilla-fennec-geoloc-api.key', '/builds/mozilla-fennec-geoloc-api.key'),
                ('/builds/crash-stats-api.token', '/builds/crash-stats-api.token'),
                ('/builds/adjust-sdk.token', '/builds/adjust-sdk.token'),
                ('/builds/adjust-sdk-beta.token', '/builds/adjust-sdk-beta.token'),
                ('/builds/relengapi.tok', '/builds/relengapi.tok'),
                ('/usr/local/lib/hgext', '/usr/local/lib/hgext'),
                ('/tools/tooltool.py', '/builds/tooltool.py'),
            ],
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'TOOLTOOL_CACHE': '/builds/tooltool_cache',
                'TOOLTOOL_HOME': '/builds',
                'MOZ_OBJDIR': OBJDIR,
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
            'stage_platform': "android-api-15-debug",
            'stage_product': 'mobile',
            'post_upload_include_platform': True,
            'tooltool_manifest_src': 'mobile/android/config/tooltool-manifests/android/releng.manifest',
            'tooltool_script': ['/builds/tooltool.py'],
            'updates_enabled': False,
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
        'platforms': ['mock', 'macosx64-lion', 'win64-rev2'],
    },
}

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
#    <gecko>/js/src/devtools/automation/variants/.
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
            'linux64-debug':  [],
            'linux-debug': ['arm-sim'],
            'macosx64-debug': [],
            'win32-debug': ['plaindebug', 'compacting'],
            'win32': ['plain'],
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
    }
}

apply_localconfig(BRANCH_PROJECTS, localconfig.BRANCH_PROJECTS)

# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {
        'merge_builds': False,
    },
    'mozilla-release': {
        'merge_builds': False,
    },
    'mozilla-beta': {
        'merge_builds': False,
    },
    'mozilla-esr52': {
        'merge_builds': False,
        'lock_platforms': True,
        'gecko_version': 52,
        'platforms': {
            'linux': {},
            'linux64': {},
            'macosx64': {},
            'win32': {},
            'win64': {},
            'linux64-asan': {},
            'linux64-av': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'win64-debug': {},
        },
    },
    'try': {
        'branch_projects': [],
        # Now that gecko 60+ is TC-only and nothing else active uses buildbot
        # Make try pushes assume gecko 52! - Bug 1459249
        'lock_platforms': True,
        'gecko_version': 52,
        'platforms': {
            'linux': {},
            'linux64': {},
            'macosx64': {},
            'win32': {},
            'win64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
            'win64-debug': {},
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

######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['mozilla-central']['enable_perproduct_builds'] = True
BRANCHES['mozilla-central']['start_hour'] = [3]
BRANCHES['mozilla-central']['start_minute'] = [2]
# Enable PGO Builds on this branch
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'
BRANCHES['mozilla-central']['periodic_start_hours'] = range(1, 24, 3)
BRANCHES['mozilla-central']['periodic_start_minute'] = 30
# Enable unit tests
BRANCHES['mozilla-central']['enable_mac_a11y'] = True
BRANCHES['mozilla-central']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
BRANCHES['mozilla-central']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-central']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64', 'win64']
BRANCHES['mozilla-central']['l10nDatedDirs'] = True
BRANCHES['mozilla-central']['l10n_tree'] = 'fxcentral'
# make sure it has an ending slash
BRANCHES['mozilla-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-central-l10n/'
BRANCHES['mozilla-central']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-central'
BRANCHES['mozilla-central']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-central' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-central']['enable_multi_locale'] = True
BRANCHES['mozilla-central']['upload_mobile_symbols'] = True
# Enable desktop repacks with mozharness
BRANCHES['mozilla-central']['desktop_mozharness_repacks_enabled'] = True

# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-central']['updates_enabled'] = True
BRANCHES['mozilla-central']['update_channel'] = 'nightly'
BRANCHES['mozilla-central']['create_partial'] = True
BRANCHES['mozilla-central']['create_partial_l10n'] = True
BRANCHES['mozilla-central']['enable_blocklist_update'] = True
BRANCHES['mozilla-central']['enable_hsts_update'] = True
BRANCHES['mozilla-central']['enable_hpkp_update'] = True
BRANCHES['mozilla-central']['platforms']['android-x86']['updates_enabled'] = True
BRANCHES['mozilla-central']['platforms']['android-api-15']['updates_enabled'] = True
BRANCHES['mozilla-central']['platforms']['linux']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['linux64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['win32']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['win64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['android-api-15']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['platforms']['macosx64']['nightly_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-central']['l10n_extra_configure_args'] = ['--with-macbundlename-prefix=Firefox']

######## mozilla-release
BRANCHES['mozilla-release']['repo_path'] = 'releases/mozilla-release'
BRANCHES['mozilla-release']['update_channel'] = 'release'
BRANCHES['mozilla-release']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['mozilla-release']['start_hour'] = [3]
BRANCHES['mozilla-release']['start_minute'] = [2]
# Enable PGO Builds on this branch
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'
# Enable unit tests
BRANCHES['mozilla-release']['enable_mac_a11y'] = True
# L10n configuration
BRANCHES['mozilla-release']['enable_l10n'] = False
BRANCHES['mozilla-release']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-release']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-release']['l10nDatedDirs'] = True
BRANCHES['mozilla-release']['l10n_tree'] = 'fxrel'
BRANCHES['mozilla-release']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-release'
BRANCHES['mozilla-release']['localesURL'] = \
    '%s/build/buildbot-configs/raw-file/production/mozilla/l10n/all-locales.mozilla-release' % (GLOBAL_VARS['hgurl'])
BRANCHES['mozilla-release']['enable_multi_locale'] = True
BRANCHES['mozilla-release']['upload_mobile_symbols'] = True
# temp disable nightlies (which includes turning off enable_l10n and l10nNightlyUpdate)
BRANCHES['mozilla-release']['enable_nightly'] = False
BRANCHES['mozilla-release']['enable_blocklist_update'] = True
BRANCHES['mozilla-release']['enabled_products'] = ['firefox', 'mobile']
BRANCHES['mozilla-release']['enable_perproduct_builds'] = False
### Release Promotion
BRANCHES['mozilla-release']['enable_release_promotion'] = {
    "firefox": True,
    "fennec": True,
}
# used by process/release.py
BRANCHES['mozilla-release']['tuxedoServerUrl'] = "https://bounceradmin.mozilla.com/api"
BRANCHES['mozilla-release']['single_locale_branch_config'] = {
    "firefox": "mozilla-release",
}
BRANCHES['mozilla-release']['bouncer_submitter_config'] = {
    "firefox": "releases/bouncer_firefox_release.py",
    "fennec": 'releases/bouncer_fennec.py',
}
BRANCHES['mozilla-release']['uptake_monitoring_config'] = {
    "firefox": 'releases/bouncer_firefox_release.py',
    "fennec": 'releases/bouncer_fennec.py',
}
BRANCHES['mozilla-release']['postrelease_version_bump_config'] = {
    "firefox": 'releases/postrelease_firefox_release.py',
    # configs are generic so can be reused
    "fennec": 'releases/postrelease_firefox_release.py',
}
BRANCHES['mozilla-release']['postrelease_bouncer_aliases_config'] = {
    "firefox": 'releases/bouncer_firefox_release.py',
    "fennec": 'releases/bouncer_fennec.py',
}
BRANCHES['mozilla-release']['postrelease_mark_as_shipped_config'] = {
    "firefox": 'releases/postrelease_firefox_release.py',
    # configs are generic so can be reused
    "fennec": 'releases/postrelease_firefox_release.py',
}
BRANCHES['mozilla-release']['updates_config'] = {
    "firefox": 'releases/updates_firefox_release.py',
    # TODO - fennec
    "fennec": "",
}
BRANCHES['mozilla-release']['beetmover_credentials'] = "/builds/release-s3.credentials"
BRANCHES['mozilla-release']['stage_product'] = {
    'firefox': 'firefox',
    'fennec': 'mobile'
}
BRANCHES['mozilla-release']['platforms']['linux']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-release']['platforms']['linux64']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-release']['platforms']['macosx64']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-release']['platforms']['win32']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-release']['platforms']['win64']['dep_signing_servers'] = 'release-signing'
# used by releasetasks
BRANCHES['mozilla-release']['bouncer_enabled'] = True
BRANCHES['mozilla-release']['postrelease_version_bump_enabled'] = {
    "firefox": True,
    "fennec": True,
}
BRANCHES['mozilla-release']['postrelease_bouncer_aliases_enabled'] = True
BRANCHES['mozilla-release']['postrelease_mark_as_shipped_enabled'] = True
BRANCHES['mozilla-release']['uptake_monitoring_enabled'] = True
BRANCHES['mozilla-release']['push_to_candidates_enabled'] = True
BRANCHES['mozilla-release']['push_to_releases_automatic'] = False
BRANCHES['mozilla-release']['beetmover_buckets'] = {
    "firefox": "net-mozaws-prod-delivery-firefox",
    "fennec": "net-mozaws-prod-delivery-archive",
}
BRANCHES['mozilla-release']['uptake_monitoring_platforms'] = {
    "firefox": ("linux", "linux64", "win32", "win64", "macosx64"),
    "fennec": ("android-api-15", "android-x86"),
}
BRANCHES['mozilla-release']['signing_class'] = {
    "firefox": "release-signing",
    "fennec": "release-signing",
}
BRANCHES['mozilla-release']['signing_cert'] = {
    "firefox": "release",
    "fennec": "release",
}
BRANCHES['mozilla-release']['root_home_dir'] = {
    "firefox": "desktop",
    "fennec": "mobile",
}
BRANCHES['mozilla-release']['release_platforms'] = ("linux", "linux64", "win32", "win64", "macosx64")
BRANCHES['mozilla-release']['l10n_release_platforms'] = ("linux", "linux64", "win32", "win64", "macosx64")
BRANCHES['mozilla-release']['partner_repacks_platforms'] = {
    "firefox": ("linux", "linux64", "win32", "win64", "macosx64")
}
BRANCHES['mozilla-release']['eme_free_repacks_platforms'] = {
    "firefox": ("win32", "win64", "macosx64")
}
BRANCHES['mozilla-release']['partner_repack_config'] = {
    "firefox": {
        "script_name": "scripts/desktop_partner_repacks.py",
        "extra_args": [
            "--cfg", "partner_repacks/release_mozilla-release_desktop.py",
            "--s3cfg", "/builds/partners-s3cfg",
        ],
    },
    # TODO - add fennec support
    # 'fennec': {}
}
BRANCHES['mozilla-release']['updates_builder_enabled'] = True
BRANCHES['mozilla-release']['update_verify_enabled'] = True
BRANCHES['mozilla-release']['mirror_requiring_channels'] = ['release']
BRANCHES['mozilla-release']['release_channel_mappings'] = {
  "firefox": [
        [r"^\d+\.0$", ["beta", "release"]],  # RC, 45.0
        [r"^\d+\.\d+\.\d+$", ["release"]],  # Other (dot releaseas), 45.0.4
    ]
}
# Bug 1313434, CI builds on all named branches
BRANCHES['mozilla-release']['watch_all_branches'] = True
# platform to TC index mapping to help finding prmotable CI builds
BRANCHES['mozilla-release']['tc_indexes'] = {
    "firefox": {
        "linux": {
            "unsigned": "gecko.v2.mozilla-release.nightly.revision.{rev}.firefox.linux-opt",
            "signed": "gecko.v2.mozilla-release.signed-nightly.revision.{rev}.firefox-l10n.linux-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-release.nightly.revision.{rev}.firefox.linux-nightly-repackage-signing",
            "ci_system": "tc",
        },
        "linux64": {
            "unsigned": "gecko.v2.mozilla-release.nightly.revision.{rev}.firefox.linux64-opt",
            "signed": "gecko.v2.mozilla-release.signed-nightly.revision.{rev}.firefox-l10n.linux64-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-release.nightly.revision.{rev}.firefox.linux64-nightly-repackage-signing",
            "ci_system": "tc",
        },
        "macosx64": {
            "unsigned": "gecko.v2.mozilla-release.nightly.revision.{rev}.firefox.macosx64-opt",
            "signed": "gecko.v2.mozilla-release.signed-nightly.revision.{rev}.firefox-l10n.macosx64-opt.en-US",
            "repackage": "gecko.v2.mozilla-release.nightly.revision.{rev}.firefox.macosx64-nightly-repackage",
            "repackage-signing": "gecko.v2.mozilla-release.nightly.revision.{rev}.firefox.macosx64-nightly-repackage-signing",
            "ci_system": "tc",
        },
        "win32": {
            "unsigned": "gecko.v2.mozilla-release.revision.{rev}.firefox-l10n.win32-opt.en-US",
            "signed": "gecko.v2.mozilla-release.signed-nightly.revision.{rev}.firefox-l10n.win32-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-release.revision.{rev}.firefox-l10n.win32-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
        "win64": {
            "unsigned": "gecko.v2.mozilla-release.revision.{rev}.firefox-l10n.win64-opt.en-US",
            "signed": "gecko.v2.mozilla-release.signed-nightly.revision.{rev}.firefox-l10n.win64-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-release.revision.{rev}.firefox-l10n.win64-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
    },
    # TODO: fennec
}
# Recompress complete MARs from LZMA to BZ2 for updates from versions < 56.0. We did this until 57.0.4.
BRANCHES['mozilla-release']['lzma_to_bz2'] = False

######## mozilla-beta
BRANCHES['mozilla-beta']['repo_path'] = 'releases/mozilla-beta'
BRANCHES['mozilla-beta']['l10n_repo_path'] = 'releases/l10n/mozilla-beta'
BRANCHES['mozilla-beta']['update_channel'] = 'beta'
BRANCHES['mozilla-beta']['start_hour'] = [3]
BRANCHES['mozilla-beta']['start_minute'] = [2]
# Enable PGO Builds on this branch
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'
# Enable unit tests
BRANCHES['mozilla-beta']['enable_mac_a11y'] = True
BRANCHES['mozilla-beta']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['mozilla-beta']['enable_l10n'] = False
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
BRANCHES['mozilla-beta']['platforms']['android-api-15']['enable_dep'] = True
BRANCHES['mozilla-beta']['platforms']['android-api-15-debug']['enable_dep'] = True
BRANCHES['mozilla-beta']['enabled_products'] = ['firefox', 'mobile', 'devedition']
BRANCHES['mozilla-beta']['enable_perproduct_builds'] = False
### Release Promotion
# enables/disables BB builders
BRANCHES['mozilla-beta']['enable_release_promotion'] = {
    "firefox": True,
    "fennec": True,
    "devedition": True,
}
# used by process/release.py
BRANCHES['mozilla-beta']['tuxedoServerUrl'] = "https://bounceradmin.mozilla.com/api"
BRANCHES['mozilla-beta']['single_locale_branch_config'] = {
    "firefox": "mozilla-beta",
    "devedition": "mozilla-beta_devedition",
}
BRANCHES['mozilla-beta']['bouncer_submitter_config'] = {
    "firefox": "releases/bouncer_firefox_beta.py",
    "devedition": "releases/bouncer_firefox_devedition.py",
    "fennec": 'releases/bouncer_fennec_beta.py',
}
BRANCHES['mozilla-beta']['uptake_monitoring_config'] = {
    "firefox": 'releases/bouncer_firefox_beta.py',
    "devedition": "releases/bouncer_firefox_devedition.py",
    "fennec": 'releases/bouncer_fennec_beta.py',
}
BRANCHES['mozilla-beta']['postrelease_version_bump_config'] = {
    # configs are generic so can be reused
    "firefox": 'releases/postrelease_firefox_beta.py',
    "fennec": 'releases/postrelease_firefox_beta.py',
    "devedition": 'releases/postrelease_firefox_beta.py',
}
BRANCHES['mozilla-beta']['postrelease_bouncer_aliases_config'] = {
    "firefox": 'releases/bouncer_firefox_beta.py',
    "devedition": "releases/bouncer_firefox_devedition.py",
    "fennec": 'releases/bouncer_fennec_beta.py',
}
BRANCHES['mozilla-beta']['postrelease_mark_as_shipped_config'] = {
    "firefox": 'releases/postrelease_firefox_beta.py',
    # configs are generic so can be reused
    "fennec": 'releases/postrelease_firefox_beta.py',
    "devedition": "releases/postrelease_firefox_beta.py",
}
BRANCHES['mozilla-beta']['updates_config'] = {
    "firefox": 'releases/updates_firefox_beta.py',
    "devedition": 'releases/updates_firefox_devedition.py',
    # TODO - fennec
    "fennec": "",
}
BRANCHES['mozilla-beta']['beetmover_credentials'] = "/builds/release-s3.credentials"
BRANCHES['mozilla-beta']['stage_product'] = {
    'firefox': 'firefox',
    'fennec': 'mobile',
    'devedition': 'devedition'
}
BRANCHES['mozilla-beta']['platforms']['linux']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-beta']['platforms']['linux64']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-beta']['platforms']['macosx64']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-beta']['platforms']['win32']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-beta']['platforms']['win64']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-beta']['platforms']['macosx64-devedition']['dep_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-beta']['platforms']['win32-devedition']['dep_signing_servers'] = 'nightly-signing'
BRANCHES['mozilla-beta']['platforms']['win64-devedition']['dep_signing_servers'] = 'nightly-signing'
# used by releasetasks
BRANCHES['mozilla-beta']['binary_transparency_enabled'] = False
BRANCHES['mozilla-beta']['bouncer_enabled'] = True
BRANCHES['mozilla-beta']['updates_builder_enabled'] = True
BRANCHES['mozilla-beta']['update_verify_enabled'] = True
BRANCHES['mozilla-beta']['postrelease_version_bump_enabled'] = {
    "firefox": True,
    "devedition": True,
    "fennec": True,
}
BRANCHES['mozilla-beta']['postrelease_bouncer_aliases_enabled'] = True
BRANCHES['mozilla-beta']['postrelease_mark_as_shipped_enabled'] = True
BRANCHES['mozilla-beta']['uptake_monitoring_enabled'] = True
BRANCHES['mozilla-beta']['push_to_candidates_enabled'] = True
BRANCHES['mozilla-beta']['push_to_releases_automatic'] = True
BRANCHES['mozilla-beta']['release_channel_mappings'] = {
    "firefox": [["^.*$", ["beta"]]],
    "devedition": [["^.*$", ["aurora"]]],
}
BRANCHES['mozilla-beta']['beetmover_buckets'] = {
    "firefox": "net-mozaws-prod-delivery-firefox",
    "fennec": "net-mozaws-prod-delivery-archive",
    "devedition": "net-mozaws-prod-delivery-archive",
}
BRANCHES['mozilla-beta']['uptake_monitoring_platforms'] = {
    "firefox": ("linux", "linux64", "win32", "win64", "macosx64"),
    "fennec": ("android-api-15", "android-x86"),
    "devedition": ("linux", "linux64", "win32", "win64", "macosx64"),
}
BRANCHES['mozilla-beta']['signing_class'] = {
    "firefox": "release-signing",
    "fennec": "release-signing",
    "devedition": "nightly-signing",
}
BRANCHES['mozilla-beta']['signing_cert'] = {
    "firefox": "release",
    "fennec": "release",
    "devedition": "nightly",
}
BRANCHES['mozilla-beta']['accepted_mar_channel_id'] = {
    "firefox": "firefox-mozilla-beta",
    "devedition": "firefox-mozilla-aurora",
    # TODO: fennec
}
BRANCHES['mozilla-beta']['root_home_dir'] = {
    "firefox": "desktop",
    "devedition": "desktop",
    "fennec": "mobile",
}
BRANCHES['mozilla-beta']['release_platforms'] = ("linux", "linux64", "win32", "win64", "macosx64")
BRANCHES['mozilla-beta']['l10n_release_platforms'] = ("linux", "linux64", "win32", "win64", "macosx64")
BRANCHES['mozilla-beta']['partner_repacks_platforms'] = {
    "firefox": ("linux", "linux64", "win32", "win64", "macosx64")
}
BRANCHES['mozilla-beta']['eme_free_repacks_platforms'] = {
    "firefox": ("win32", "win64", "macosx64")
}
BRANCHES['mozilla-beta']['partner_repack_config'] = {
    "firefox": {
        "script_name": "scripts/desktop_partner_repacks.py",
        "extra_args": [
            "--cfg", "partner_repacks/release_mozilla-release_desktop.py",
            "--s3cfg", "/builds/partners-s3cfg",
        ],
    },
    # TODO - add fennec support
    # 'fennec': {}
}
BRANCHES['mozilla-beta']['snap_enabled'] = {"firefox": True}
BRANCHES['mozilla-beta']['update_verify_channel'] = {
    "firefox": 'beta-cdntest',
    "devedition": 'aurora-cdntest',
}
BRANCHES['mozilla-beta']['update_verify_requires_cdn_push'] = True
# platform to TC index mapping to help finding prmotable CI builds
BRANCHES['mozilla-beta']['tc_indexes'] = {
    "firefox": {
        "linux": {
            "unsigned": "gecko.v2.mozilla-beta.nightly.revision.{rev}.firefox.linux-opt",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.firefox-l10n.linux-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.nightly.revision.{rev}.firefox.linux-nightly-repackage-signing",
            "ci_system": "tc",
        },
        "linux64": {
            "unsigned": "gecko.v2.mozilla-beta.nightly.revision.{rev}.firefox.linux64-opt",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.firefox-l10n.linux64-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.nightly.revision.{rev}.firefox.linux64-nightly-repackage-signing",
            "ci_system": "tc",
        },
        "macosx64": {
            "unsigned": "gecko.v2.mozilla-beta.nightly.revision.{rev}.firefox.macosx64-opt",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.firefox-l10n.macosx64-opt.en-US",
            "repackage": "gecko.v2.mozilla-beta.nightly.revision.{rev}.firefox.macosx64-nightly-repackage",
            "repackage-signing": "gecko.v2.mozilla-beta.nightly.revision.{rev}.firefox.macosx64-nightly-repackage-signing",
            "ci_system": "tc",
        },
        "win32": {
            "unsigned": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.win32-opt.en-US",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.firefox-l10n.win32-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.win32-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
        "win64": {
            "unsigned": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.win64-opt.en-US",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.firefox-l10n.win64-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.win64-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
    },
    "devedition": {
        "linux": {
            "unsigned": "gecko.v2.mozilla-beta.nightly.revision.{rev}.devedition.linux-opt",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.devedition-l10n.linux-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.linux-devedition-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
        "linux64": {
            "unsigned": "gecko.v2.mozilla-beta.nightly.revision.{rev}.devedition.linux64-opt",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.devedition-l10n.linux64-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.linux64-devedition-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
        "macosx64": {
            "unsigned": "gecko.v2.mozilla-beta.nightly.revision.{rev}.devedition.macosx64-opt",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.devedition-l10n.macosx64-opt.en-US",
            "repackage": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.macosx64-devedition-nightly-repackage.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.macosx64-devedition-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
        "win32": {
            "unsigned": "gecko.v2.mozilla-beta.revision.{rev}.devedition-l10n.win32-opt.en-US",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.devedition-l10n.win32-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.win32-devedition-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
        "win64": {
            "unsigned": "gecko.v2.mozilla-beta.revision.{rev}.devedition-l10n.win64-opt.en-US",
            "signed": "gecko.v2.mozilla-beta.signed-nightly.revision.{rev}.devedition-l10n.win64-opt.en-US",
            "repackage-signing": "gecko.v2.mozilla-beta.revision.{rev}.firefox-l10n.win64-devedition-nightly-repackage-signing.en-US",
            "ci_system": "tc",
        },
    },
    # TODO: fennec
}
# Recompress complete MARs from LZMA to BZ2 for versions >= 56.0
BRANCHES['mozilla-beta']['lzma_to_bz2'] = False

######## mozilla-esr52
BRANCHES['mozilla-esr52']['repo_path'] = 'releases/mozilla-esr52'
BRANCHES['mozilla-esr52']['update_channel'] = 'esr'
BRANCHES['mozilla-esr52']['l10n_repo_path'] = 'releases/l10n/mozilla-release'
BRANCHES['mozilla-esr52']['start_hour'] = [0]
BRANCHES['mozilla-esr52']['start_minute'] = [15]
BRANCHES['mozilla-esr52']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr52']['enable_mac_a11y'] = True
BRANCHES['mozilla-esr52']['platforms']['macosx64']['platform_objdir'] = "%s/x86_64" % OBJDIR
# L10n configuration
BRANCHES['mozilla-esr52']['enable_l10n'] = False
BRANCHES['mozilla-esr52']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-esr52']['l10n_platforms'] = ['linux', 'linux64', 'win32', 'macosx64', 'win64']
BRANCHES['mozilla-esr52']['l10nDatedDirs'] = True
BRANCHES['mozilla-esr52']['l10n_tree'] = 'fxesr52'
BRANCHES['mozilla-esr52']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-esr52'
BRANCHES['mozilla-esr52']['enable_nightly'] = False
BRANCHES['mozilla-esr52']['enable_nightly_everytime'] = False
BRANCHES['mozilla-esr52']['updates_enabled'] = False
BRANCHES['mozilla-esr52']['create_partial'] = False
BRANCHES['mozilla-esr52']['enable_blocklist_update'] = True
BRANCHES['mozilla-esr52']['enable_hsts_update'] = True
BRANCHES['mozilla-esr52']['enable_hpkp_update'] = True
BRANCHES['mozilla-esr52']['enabled_products'] = ['firefox']
### Release Promotion
BRANCHES['mozilla-esr52']['enable_release_promotion'] = {
    "firefox": True,
}
# used by process/release.py
BRANCHES['mozilla-esr52']['tuxedoServerUrl'] = "https://bounceradmin.mozilla.com/api"
BRANCHES['mozilla-esr52']['single_locale_branch_config'] = {
    "firefox": "mozilla-esr52",
}
BRANCHES['mozilla-esr52']['bouncer_submitter_config'] = {
    "firefox": "releases/bouncer_firefox_esr.py",
}
BRANCHES['mozilla-esr52']['uptake_monitoring_config'] = {
    "firefox": 'releases/bouncer_firefox_esr.py',
}
BRANCHES['mozilla-esr52']['postrelease_version_bump_config'] = {
    "firefox": 'releases/postrelease_firefox_esr52.py',
}
BRANCHES['mozilla-esr52']['postrelease_bouncer_aliases_config'] = {
    "firefox": 'releases/bouncer_firefox_esr.py',
}
BRANCHES['mozilla-esr52']['postrelease_mark_as_shipped_config'] = {
    "firefox": 'releases/postrelease_firefox_esr52.py',
}
BRANCHES['mozilla-esr52']['updates_config'] = {
    "firefox": 'releases/updates_firefox_esr52.py',
}
BRANCHES['mozilla-esr52']['beetmover_credentials'] = "/builds/release-s3.credentials"
BRANCHES['mozilla-esr52']['stage_product'] = {
    'firefox': 'firefox',
}
BRANCHES['mozilla-esr52']['platforms']['linux']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-esr52']['platforms']['linux64']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-esr52']['platforms']['macosx64']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-esr52']['platforms']['win32']['dep_signing_servers'] = 'release-signing'
BRANCHES['mozilla-esr52']['platforms']['win64']['dep_signing_servers'] = 'release-signing'
# used by releasetasks
BRANCHES['mozilla-esr52']['bouncer_enabled'] = True
BRANCHES['mozilla-esr52']['postrelease_version_bump_enabled'] = {"firefox": True}
BRANCHES['mozilla-esr52']['postrelease_bouncer_aliases_enabled'] = True
BRANCHES['mozilla-esr52']['postrelease_mark_as_shipped_enabled'] = True
BRANCHES['mozilla-esr52']['uptake_monitoring_enabled'] = True
BRANCHES['mozilla-esr52']['push_to_candidates_enabled'] = True
BRANCHES['mozilla-esr52']['push_to_releases_automatic'] = False
BRANCHES['mozilla-esr52']['beetmover_buckets'] = {
    "firefox": "net-mozaws-prod-delivery-firefox",
}
BRANCHES['mozilla-esr52']['uptake_monitoring_platforms'] = {
    "firefox": ("linux", "linux64", "win32", "win64", "macosx64"),
}
BRANCHES['mozilla-esr52']['signing_class'] = {
    "firefox": "release-signing",
}
BRANCHES['mozilla-esr52']['signing_cert'] = {
    "firefox": "release",
}
BRANCHES['mozilla-esr52']['root_home_dir'] = {
    "firefox": "desktop",
}
BRANCHES['mozilla-esr52']['release_platforms'] = ("linux", "linux64", "win32", "win64", "macosx64")
BRANCHES['mozilla-esr52']['l10n_release_platforms'] = ("linux", "linux64", "win32", "win64", "macosx64")
BRANCHES['mozilla-esr52']['updates_builder_enabled'] = True
BRANCHES['mozilla-esr52']['update_verify_enabled'] = True
BRANCHES['mozilla-esr52']['release_channel_mappings'] = {"firefox": [["^.*$", ["esr"]]]}
# Bug 1342117, CI builds on all named branches
BRANCHES['mozilla-esr52']['watch_all_branches'] = True
BRANCHES['mozilla-esr52']['sha1_repacks_platforms'] = ("win32",)
BRANCHES['mozilla-esr52']['partner_repack_config'] = {
    "firefox": {
        "script_name": "scripts/desktop_partner_repacks.py",
        "extra_args": [
            "--cfg", "partner_repacks/release_mozilla-esr52_desktop.py",
            "--s3cfg", "/builds/partners-s3cfg",
        ],
    },
}
BRANCHES['mozilla-esr52']['tc_indexes'] = {
    "firefox": {
        "linux": {
            "signed": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.linux-opt",
            "unsigned": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.linux-opt",
            "ci_system": "bb",
        },
        "linux64": {
            "signed": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.linux64-opt",
            "unsigned": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.linux64-opt",
            "ci_system": "bb",
        },
        "macosx64": {
            "signed": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.macosx64-opt",
            "unsigned": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.macosx64-opt",
            "ci_system": "bb",
        },
        "win32": {
            "signed": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.win32-opt",
            "unsigned": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.win32-opt",
            "ci_system": "bb",
        },
        "win64": {
            "signed": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.win64-opt",
            "unsigned": "gecko.v2.mozilla-esr52.revision.{rev}.firefox.win64-opt",
            "ci_system": "bb",
        },
    },
}
# Recompress complete MARs from LZMA to BZ2 for versions >= 56.0
BRANCHES['mozilla-esr52']['lzma_to_bz2'] = False

######## try
# Try-specific configs
BRANCHES['try']['l10n_repo_path'] = 'l10n-central'
BRANCHES['try']['stage_username'] = 'trybld'
BRANCHES['try']['stage_username_mobile'] = 'trybld'
BRANCHES['try']['stage_ssh_key'] = 'trybld_dsa'
BRANCHES['try']['stage_ssh_mobile_key'] = 'trybld_dsa'
BRANCHES['try']['stage_base_path'] = '/home/ftp/pub/firefox/try-builds'
BRANCHES['try']['stage_base_path_mobile'] = '/home/ftp/pub/firefox/try-builds'
BRANCHES['try']['enable_merging'] = False
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['watch_all_branches'] = True
BRANCHES['try']['pgo_strategy'] = 'try'
BRANCHES['try']['enable_mac_a11y'] = True
BRANCHES['try']['platforms']['macosx64']['platform_objdir'] = "%s/x86_64" % OBJDIR
BRANCHES['try']['package_dir'] = '%(who)s-%(got_revision)s/'
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try']['repo_path'] = 'try'
BRANCHES['try']['start_hour'] = [3]
BRANCHES['try']['start_minute'] = [2]
# Disable Nightly builds
BRANCHES['try']['enable_nightly'] = False
BRANCHES['try']['enable_mac_a11y'] = True
BRANCHES['try']['enable_l10n'] = True
BRANCHES['try']['desktop_mozharness_repacks_enabled'] = True
BRANCHES['try']['l10n_platforms'] = ['linux', 'linux64', 'win32', 'macosx64',
                                     'win64']
BRANCHES['try']['enable_l10n_dep_scheduler'] = False
BRANCHES['try']['enable_nightly'] = False
BRANCHES['try']['l10nNightlyUpdate'] = False
BRANCHES['try']['l10nDatedDirs'] = False
# need this or the master.cfg will bail
BRANCHES['try']['platforms']['linux']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['win32']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['win64']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['win64-debug']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['macosx64']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['macosx64-debug']['slaves'] = TRY_SLAVES['macosx64-lion']
for platform in BRANCHES['try']['platforms'].keys():
    # Disable symbol upload across the board
    BRANCHES['try']['platforms'][platform]['upload_symbols'] = False
    # only one l10n builder
    if BRANCHES['try']['platforms'][platform].get('mozharness_desktop_l10n', {}).get('l10n_chunks'):
       BRANCHES['try']['platforms'][platform]['mozharness_desktop_l10n']['l10n_chunks'] = 1

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
    #make sure it has an ending slash
    BRANCHES[branch]['l10nUploadPath'] = \
        '/home/ftp/pub/mozilla.org/firefox/nightly/latest-' + branch + '-l10n/'
    BRANCHES[branch]['enUS_binaryURL'] = GLOBAL_VARS['download_base_url'] + branchConfig.get('enUS_binaryURL', '')
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

        # If a branch does not set nightly_signing_servers, first check if it wants
        # a different signing server set for all platforms, if not it should be set to
        # its dep signing server, which may have already been set to the global default.
        BRANCHES[branch]['platforms'][platform]['nightly_signing_servers'] = \
            branchConfig.get('nightly_signing_servers', branchConfig.get('platforms', {}).get(
                             platform, {}).get('nightly_signing_servers',
                             BRANCHES[branch]['platforms'][platform]['dep_signing_servers']))

# Expand out the branch_projects into a full PROJECT object per branch. This
# must come after the BRANCHES configuration above, so that
# BRANCHES[*]['enable_try'] is set when appropriate.
# Bug 1401549 - Disable Buildbot Windows Spidermonkey jobs on Firefox >= 57
non_trunk_branches = []
for name, branch in items_before(BRANCHES, 'gecko_version', 57):
    non_trunk_branches.append(name)

for b, branch in BRANCHES.items():
    if b not in non_trunk_branches:
        continue
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

# Only test pretty names on train branches, not m-c or project branches.
for branch in ("mozilla-beta", "mozilla-release", "mozilla-esr52"):
    for platform in ("linux", "linux64", "macosx64", "win32", "win64"):
        if platform in BRANCHES[branch]['platforms']:
            BRANCHES[branch]['platforms'][platform]['test_pretty_names'] = True

# enable mozharness desktop builds on 45.0 and higher
for name, branch in items_at_least(BRANCHES, 'gecko_version', 45):
    # if true, any platform with mozharness_desktop_build in its config
    # will use mozharness instead of MozillaBuildFactory
    branch['desktop_mozharness_builds_enabled'] = True

# enable mozharness mobile builds on m-a, m-c, and m-c related branches
mc_gecko_version = BRANCHES['mozilla-central']['gecko_version']
for name, branch in items_before(BRANCHES, 'gecko_version', mc_gecko_version):
    for platform in branch['platforms'].keys():
        if 'android' in platform:
            # we don't want to disable the branch level item: "desktop_mozharness_builds_enabled"
            # we do want to remove the platform level item: "mozharness_desktop_build"
            del branch['platforms'][platform]['mozharness_desktop_build']

##Bug 1268542 - Disable Linux64 Debug builds and tests in buildbot
for name, branch in items_at_least(BRANCHES, 'gecko_version', 48):
    for platform in branch['platforms'].keys():
        if platform not in ['linux64-debug']:
            continue
        del branch['platforms'][platform]

# Bug 1282849 - disable fennec debug builds and tests in buildbot
for name, branch in items_at_least(BRANCHES, 'gecko_version', 50):
    for platform in branch['platforms'].keys():
        if platform not in ['android-api-15-debug']:
            continue
        del branch['platforms'][platform]

#Bug 1282468 - disable buildbot asan builds on trunk
for name, branch in items_at_least(BRANCHES, 'gecko_version', 51):
    for platform in branch['platforms'].keys():
        if 'linux64-asan' in platform:
            del branch['platforms'][platform]

# Bug 1391283 - remove addon devel builds from beta
# remove from esr, releaes as this rides the trains
for name, branch in items_before(BRANCHES, 'gecko_version', 55 ):
    for platform in ['win32-add-on-devel', 'win64-add-on-devel']:
        if platform in branch['platforms']:
            del branch['platforms'][platform]
for name, branch in items_at_least(BRANCHES, 'gecko_version', 56):
     for platform in ['win32-add-on-devel', 'win64-add-on-devel']:
        if platform in branch['platforms']:
            del branch['platforms'][platform]

# Bug 1293730 - Fennec x86 builds as tier 1
for name, branch in items_at_least(BRANCHES, 'gecko_version', 51):
    for platform in branch['platforms'].keys():
        if 'android-x86' in platform:
            if branch['enable_nightly'] or branch.get("enable_release_promotion"):
                # keep the nightly but remove the CI equivalent
                branch['platforms'][platform]["enable_dep"] = False
            else:
                # remove all the android-x86 build jobs on this branch
                del branch['platforms'][platform]

# Bug 1253312 - Disable Linux32 debug builds and tests on trunk
for name, branch in items_at_least(BRANCHES, 'gecko_version', 53):
    for platform in branch['platforms'].keys():
        if platform not in ['linux-debug']:
            continue
        del branch['platforms'][platform]

# Bug 1330680 - patches to disable bb nightlies on linux32/linux64/android on m-c + trunk
for name, branch in items_at_least(BRANCHES, 'gecko_version', 53):
    for platform in branch['platforms']:
        if platform not in ['linux', 'linux64', 'android-api-15', 'android-x86']:
            continue
        # Bug 1332930 Shutting off buildbot nighties shut off periodicupdates
        branch['platforms'][platform]['enable_dep'] = False
        branch['platforms'][platform]['enable_nightly'] = False
        if platform in branch['pgo_platforms']:
            branch['pgo_platforms'] = [p for p in branch['pgo_platforms'] if p != platform]

# Bug 1351326 - patches to disable mac bb nightlies on trunk + m-c
for name, branch in items_at_least(BRANCHES, 'gecko_version', 56):
    for platform in branch['platforms']:
        if platform not in ['macosx64']:
            continue
        # Bug 1332930 Shutting off buildbot nighties shut off periodicupdates
        branch['platforms'][platform]['enable_dep'] = False
        branch['platforms'][platform]['enable_nightly'] = False
        if platform in branch['pgo_platforms']:
            branch['pgo_platforms'] = [p for p in branch['pgo_platforms'] if p != platform]

# Bug 1354605 - patches to disable win bb nightlies on trunk + m-c
for name, branch in items_at_least(BRANCHES, 'gecko_version', 56):
    if "try" in name:  # remove this condition once we don't need buildbot windows builds on try
        continue
    for platform in branch['platforms']:
        if platform not in ['win32', 'win64']:
            continue
        # Bug 1332930 Shutting off buildbot nighties shut off periodicupdates
        branch['platforms'][platform]['enable_dep'] = False
        branch['platforms'][platform]['enable_nightly'] = False
        if platform in branch['pgo_platforms']:
            branch['pgo_platforms'] = [p for p in branch['pgo_platforms'] if p != platform]

# Bug 1361414 - disable buildbot macosx debug builds on trunk
for name, branch in items_at_least(BRANCHES, 'gecko_version', 55):
    for platform in branch['platforms'].keys():
        if platform not in ['macosx64-debug']:
            continue
        del branch['platforms'][platform]

# Bug 1362387, Bug 1387878 - remove devedition builds from Buildbot
for branch in BRANCHES.keys():
    for platform in BRANCHES[branch]['platforms'].keys():
        if platform not in ['linux64-devedition', 'macosx64-devedition',
                            'win32-devedition', 'win64-devedition']:
            continue
        del BRANCHES[branch]['platforms'][platform]

# Support cross-channel l10n in 57+ -- Bug 1397721
for name, branch in items_at_least(BRANCHES, 'gecko_version', 57):
    if 'l10n_repo_path' not in branch:
        continue
    branch['l10n_repo_path'] = 'l10n-central'

# Bug 1401549 - Disable Buildbot Windows Spidermonkey jobs
for name, branch in items_at_least(BRANCHES, 'gecko_version', 57):
    if 'branch_projects' not in BRANCHES[name].keys():
        continue
    BRANCHES[name]['branch_projects'] = [i for i in BRANCHES[name]['branch_projects'] if i != 'spidermonkey_tier_1']

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
            print('%s: %s' % (k, l))
