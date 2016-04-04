################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Please refer to the README for information about making permanent changes.  #
################################################################################
#   GYP file for zyre Node.js binding
{
  'targets': [
    {
      'target_name': 'zyre',
      'sources': [
          '../../../czmq/bindings/nodejs/binding.cc',
          'binding.cc'
      ],
      'include_dirs': [
          "<!(node -e \"require('nan')\")",
          '../../../libzmq/include',
          '../../../czmq/include',
          '../../include'
      ],
      'conditions': [
        [ 'OS=="win"', {
          'defines': [
            'ZMQ_STATIC',
            'CZMQ_STATIC',
            'ZYRE_STATIC'
          ],
          'libraries': [
            'ws2_32',
            'advapi32',
            'iphlpapi',
            'Rpcrt4'
          ]
        }],
        [ 'OS=="mac"', {
        }],
        [ 'OS=="linux"', {
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-fPIC'
            ],
          },
          'libraries': [
            '-lpthread'
          ]
        }],
      ],
      'dependencies': [
          '../../builds/gyp/project.gyp:libzyre'
      ]
    }
  ]
}
