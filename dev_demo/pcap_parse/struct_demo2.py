import struct

s = struct.Struct('2s')
packed_data = s.pack(b'ab')

# 输出字节串
print(packed_data)

# 输出十六进制字符串
print(packed_data.hex())   # 6162
# 从这些输出中可以看出，packed_data 是有效的字节串，其内容是 b'ab'。同时，十六进制表示形式 6162 对应于 b'ab'。

# 字节串以字符串形式表示
print(f'{packed_data!r}')

# 解码为 Unicode 字符串
print(packed_data.decode('utf-8'))

'''
这里打包后的字节串是 b'ab'，而输出的结果是 b'\x02ab'。这个附加的字节 '\x02' 表示该字符串包含 2 个字符（字节）。

因此，即使该打包数据的实际长度为 10 字节，由于 Python 的 struct 模块在内部添加了一个用于描述字符串长度的字节，因此 s.size 将反映为 12。
'''