# -*- coding=utf-8 -*-
# https://blog.csdn.net/weixin_58439331/article/details/127119632

'''
将数据打包成二进制通常是用在对性能要求很高的场景。
在这类场景中可以通过避免为每个打包结构分配新缓冲区的开销来优化。
pack_into()和unpack_from()方法支持直接写入预先分配的缓冲区。
对性能有要求时的处理方式
'''

import array
import binascii
import ctypes
import struct

s = struct.Struct('I 2s f')
values = (1, 'ab'.encode('utf-8'), 2.7)

print('原始值:', values)

print('使用ctypes模块string buffer')

b = ctypes.create_string_buffer(s.size)
print('原始buffer  :', binascii.hexlify(b.raw))
s.pack_into(b, 0, *values)
print('打包结果写入 :', binascii.hexlify(b.raw))
print('解包        :', s.unpack_from(b, 0))

print('使用array模块')

a = array.array('b', b'\0' * s.size)
print('原始值   :', binascii.hexlify(a))
s.pack_into(a, 0, *values)
print('打包写入 :', binascii.hexlify(a))
print('解包     :', s.unpack_from(a, 0))

