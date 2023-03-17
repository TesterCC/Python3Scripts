# -*- coding=utf-8 -*-
# https://blog.csdn.net/weixin_58439331/article/details/127119632

# packing

import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
# I -> int 4 bytes; 2s -> 2bytes; f -> 4bytes
s = struct.Struct('!I2sf')
packed_data = s.pack(*values)

print("原始值：", values)
print("格式符：", s.format)
print("占用字节：", s.size)

# 二进制数据的十六进制表示，b'0100000061620000cdcc2c40'
print("打包结果：", binascii.hexlify(packed_data))


'''
4+2+4=10 bytes，why s.size is 12?

在这个例子中，字符串 "ab" 被编码为字节串 "b'ab'"，并且它由 "2s" 格式字段引用。在这个格式字段中，"2" 表示该字段应该始终包含两个字符，且该字段的长度总是 2 个字节。因此，它生成了两个字节的占位符，对应于 "ab" 的两个字符。

当您使用结构体格式将值打包成二进制数据时（在本例中通过 s.pack()），struct 模块会将需要填充的缺失段填充为零，以便整个数据区域的字节数是处理每个值所需的字节数之和。为此，在本例中，字节串 "ab" 的长度是 2 字节，按照结构中格式符的顺序和处理要求打包成了 4 个字节，超过了实际值所需的 2 个字节。

因此， s.size 输出值是 12 个字节，其中前 4 个字节对应于整型值 1，接下来的 2 个字节对应于字节串 "ab"，最后的 4 个字节对应于浮点值 2.7。在所有这些字节之间，还有额外的 2 字节被添加，以满足结构体格式中的 "2s" 等长度不足字段的要求。因此，总字节数为 4 + 2 + 4 + 2 = 12 字节。
'''