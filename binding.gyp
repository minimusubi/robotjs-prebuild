{
    'variables': {
        'openssl_fips': '',
    },
    'targets': [{
        'target_name': 'robotjs',
        'include_dirs': [
            "<!(node -p \"require('node-addon-api').include_dir\")",
            "<!(node -e \"require('nan')\")",
        ],
        'cflags_cc': [
            '-std=c++17',
            '-fno-rtti',
            '-fno-exceptions',
        ],
        'cflags': [
            '-Wall',
            '-Wparentheses',
            '-Winline',
            '-Wbad-function-cast',
            '-Wdisabled-optimization'
        ],
        'conditions': [
            ['OS == "mac"', {
                'xcode_settings': {
                    'CLANG_CXX_LANGUAGE_STANDARD': 'c++17'
                },
                'include_dirs': [
                    'System/Library/Frameworks/CoreFoundation.Framework/Headers',
                    'System/Library/Frameworks/Carbon.Framework/Headers',
                    'System/Library/Frameworks/ApplicationServices.framework/Headers',
                    'System/Library/Frameworks/OpenGL.framework/Headers',
                ],
                'link_settings': {
                    'libraries': [
                        '-framework Carbon',
                        '-framework CoreFoundation',
                        '-framework ApplicationServices',
                        '-framework OpenGL'
                    ]
                }
            }],

            ['OS == "linux"', {
                'link_settings': {
                    'libraries': [
                        '-lpng',
                        '-lz',
                        '-lX11',
                        '-lXtst'
                    ]
                },

                'sources': [
                    'src/xdisplay.c'
                ]
            }],

            ["OS=='win'", {
                'defines': ['IS_WINDOWS'],
                "msbuild_settings": {
                    "ClCompile": {
                        "LanguageStandard": "stdcpp17"
                    }
                }
            }]
        ],

        'sources': [
            'src/robotjs.cc',
            'src/deadbeef_rand.c',
            'src/mouse.c',
            'src/keypress.c',
            'src/keycode.c',
            'src/screen.c',
            'src/screengrab.c',
            'src/snprintf.c',
            'src/MMBitmap.c'
        ]
    }]
}
