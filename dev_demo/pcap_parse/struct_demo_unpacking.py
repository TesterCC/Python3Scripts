# -*- coding=utf-8 -*-
# https://blog.csdn.net/weixin_58439331/article/details/127119632

# unpacking

import struct
import binascii

# 二进制数据的十六进制表示，b'0100000061620000cdcc2c40'
# 大端序（网络字节序）表示，b'000000016162402ccccd'

# packed_data = binascii.unhexlify(b'0100000061620000cdcc2c40')
# s = struct.Struct('I2sf')

packed_data = binascii.unhexlify(b'000000016162402ccccd')
s = struct.Struct('!I2sf')

unpacked_data = s.unpack(packed_data)
print('解包结果:', unpacked_data)

# output
# 解包结果: (1, b'ab', 2.700000047683716)   # 如果您需要使用单精度浮点数，请只使用前7位有效数字，避免舍入误差。