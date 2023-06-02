import binascii

with open("./rppd_v2_1685722369.txt", "rb") as f:
    # with open("test_receive_data_1685355049.txt", "rb") as f: # ok
    data = f.read()


# 将二进制数据转换为Wireshark / tcpdump格式的数据
hex_data = binascii.hexlify(data)
dump_data = ''
for i in range(0, len(hex_data), 32):
    line = hex_data[i:i+32].decode('ascii')
    # dump_data += f"{line[:8]} {line[8:16]} {line[16:24]} {line[24:]}\n"
    dump_data += f"{line[:4]} {line[4:8]} {line[8:12]} {line[12:16]} {line[16:20]} {line[20:24]} {line[24:28]} {line[28:]}\n"

print(dump_data)
