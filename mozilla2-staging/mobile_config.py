# -*- python -*-
# ex: set syntax=python:

OBJDIR = 'objdir'
SBOX_HOME = '/scratchbox/users/cltbld/home/cltbld'

mobile_slaves = {
    'linux-arm': [
        'moz2-linux-slave01',
        'moz2-linux-slave02',
        'moz2-linux-slave03',
        'moz2-linux-slave04',
        'moz2-linux-slave05',
        'moz2-linux-slave06',
        'moz2-linux-slave07',
        'moz2-linux-slave08',
        'moz2-linux-slave09',
        'moz2-linux-slave10',
        'moz2-linux-slave11',
        'moz2-linux-slave12',
        'moz2-linux-slave13',
        'moz2-linux-slave14',
        'moz2-linux-slave15',
        'moz2-linux-slave16',
        'moz2-linux-slave17',
        'moz2-linux-slave18',
        'moz2-linux-slave19',
        'moz2-linux-slave20',
        'moz2-linux-slave21',
        'moz2-linux-slave22',
        'moz2-linux-slave23',
        'moz2-linux-slave24',
        'moz2-linux-slave25',
    ],
    'wince-arm': [
        'moz2-win32-slave01',
        'moz2-win32-slave02',
        'moz2-win32-slave03',
        'moz2-win32-slave04',
        'moz2-win32-slave05',
        'moz2-win32-slave06',
        'moz2-win32-slave07',
        'moz2-win32-slave08',
        'moz2-win32-slave09',
        'moz2-win32-slave10',
        'moz2-win32-slave11',
        'moz2-win32-slave12',
        'moz2-win32-slave13',
        'moz2-win32-slave14',
        'moz2-win32-slave15',
        'moz2-win32-slave16',
        'moz2-win32-slave17',
        'moz2-win32-slave18',
        'moz2-win32-slave19',
        'moz2-win32-slave20',
        'moz2-win32-slave21',
        'moz2-win32-slave22',
        'moz2-win32-slave23',
        'moz2-win32-slave24',
        'moz2-win32-slave25',
        'moz2-win32-slave26',
        'moz2-win32-slave27',
        'moz2-win32-slave28',
        'moz2-win32-slave29',
    ],
}

wince_arm_env = {
    "DEVENVDIR": 'd:\\msvs9\\Common7\\IDE',
    "FRAMEWORK35VERSION": 'v3.5',
    "FRAMEWORKDIR": 'C:\\WINDOWS\\Microsoft.NET\\Framework',
    "FRAMEWORKVERSION": 'v2.0.50727',
    "INCLUDE": 'd:\\msvs9\\VC\\ATLMFC\\INCLUDE;' + \
               'd:\\msvs9\\VC\\INCLUDE;' + \
               'C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\include;',
    "LIB": 'd:\\msvs9\\VC\\ATLMFC\\LIB;' + \
           'd:\\msvs9\\VC\\LIB;C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\lib;',
    "LIBPATH": 'C:\\WINDOWS\\Microsoft.NET\\Framework\\v3.5;' + \
               'C:\\WINDOWS\\Microsoft.NET\\Framework\\v2.0.50727;' + \
               'd:\\msvs9\\VC\\ATLMFC\\LIB;d:\\msvs9\\VC\\LIB;',
    "MOZILLABUILD": 'D:\\mozilla-build\\',
    "MOZILLABUILDDRIVE": 'D:',
    "MOZILLABUILDPATH": '\\mozilla-build\\',
    "MOZ_MSVCVERSION": '9',
    "MOZ_NO_RESET_PATH": '1',
    "MOZ_TOOLS": 'D:\\mozilla-build\\moztools',
    "PATH": 'D:\\mozilla-build\\msys\\local\\bin;' + \
            'd:\\mozilla-build\\wget;' + \
            'd:\\mozilla-build\\7zip;' + \
            'd:\\mozilla-build\\blat261\\full;' + \
            'd:\\mozilla-build\\python25;' + \
            'd:\\mozilla-build\\svn-win32-1.4.2\\bin;' + \
            'd:\\mozilla-build\\upx203w;' + \
            'd:\\mozilla-build\\xemacs\\XEmacs-21.4.19\\i586-pc-win32;' + \
            'd:\\mozilla-build\\info-zip;' + \
            'd:\\mozilla-build\\nsis-2.22;' + \
            'd:\\mozilla-build\\nsis-2.33u;' + \
            '.;' + \
            'D:\\mozilla-build\\msys\\local\\bin;' + \
            'D:\\mozilla-build\\msys\\mingw\\bin;' + \
            'D:\\mozilla-build\\msys\\bin;' + \
            'd:\\msvs9\\Common7\\IDE;' + \
            'd:\\msvs9\\VC\\BIN;' + \
            'd:\\msvs9\\Common7\\Tools;' + \
            'c:\\WINDOWS\\Microsoft.NET\\Framework\\v3.5;' + \
            'c:\\WINDOWS\\Microsoft.NET\\Framework\\v2.0.50727;' + \
            'd:\\msvs9\\VC\\VCPackages;' + \
            'c:\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\bin;' + \
            'c:\\WINDOWS\\system32;' + \
            'c:\\WINDOWS;' + \
            'c:\\WINDOWS\\System32\\Wbem;' + \
            'd:\\mozilla-build\\python25;' + \
            'd:\\mercurial;' + \
            'c:\\Program Files\\Microsoft SQL Server\\90\\Tools\\binn\\;' + \
            'd:\\mozilla-build\\moztools\\bin',
    "SDKDIR": 'D:\\sdks\\v6.0\\',
    "SDKVER": '6',
    "VC8DIR": 'D:\\msvs8\\VC\\',
    "VC9DIR": 'd:\\msvs9\\VC\\',
    "VCINSTALLDIR": 'd:\\msvs9\\VC',
    "VS80COMNTOOLS": 'D:\\msvs8\\Common7\\Tools\\',
    "VS90COMNTOOLS": 'd:\\msvs9\\Common7\\Tools\\',
    "VSINSTALLDIR": 'd:\\msvs9',
}
