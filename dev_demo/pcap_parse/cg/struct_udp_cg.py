import struct

udp_packet = b"\x90\xde\x80H2Q\x00\x19p@\xd9\xe8\x08\x00E\x00\x00%r\x0e@\x00@\x11\x7fc\xc0\xa8d\x02\xc0\xa8d\x03\xc2x'\x0f\x00\x11\xd59test.json"

# 解析IP和UDP头
ip_header = udp_packet[:20]
ip_data = struct.unpack('!BBHHHBBH4s4s', ip_header)
udp_header = udp_packet[20:28]
udp_data = struct.unpack('!HHHH', udp_header)

# 解析负载数据
payload = udp_packet[28:]

# 打印解包后的数据
print('Source IP:', ip_data[8])
print('Destination IP:', ip_data[9])
print('Source Port:', udp_data[0])
print('Destination Port:', udp_data[1])
# print('Payload:', payload.decode('utf-8'))
