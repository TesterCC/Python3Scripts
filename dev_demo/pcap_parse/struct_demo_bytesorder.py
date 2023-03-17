# -*- coding=utf-8 -*-
# https://blog.csdn.net/weixin_58439331/article/details/127119632

import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
print('原始值  : ', values)

endianness = [
    ('@', 'native, native'),
    ('=', 'native, standard'),
    ('<', 'little-endian'),
    ('>', 'big-endian'),
    ('!', 'network'),
]

for code, name in endianness:
    s = struct.Struct(code + ' I 2s f')
    packed_data = s.pack(*values)
    print("-"*66)
    print('格式符  : ', s.format, 'for', name)
    print('占用字节: ', s.size)
    print('打包结果: ', binascii.hexlify(packed_data))
    print('解包结果: ', s.unpack(packed_data))
