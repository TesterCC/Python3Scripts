import struct

# 网络字节序，大端序，数据封装测试

# 方法1：个人认为这个更优
file_header = 0xF3EC2B12
packed_data = struct.pack(">I", file_header)
print(len(packed_data), packed_data)

# 方法2：
hex_str = "F3EC2B12"
bytes_data = bytes.fromhex(hex_str)
print(len(bytes_data), bytes_data)

# output
# 4 b'\xf3\xec+\x12'