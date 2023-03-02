import struct
import re

# 读取pcap包文件
with open('example.pcap', 'rb') as f:
    pcap_data = f.read()

# 解析pcap包头
pcap_header = struct.unpack('IHHIIII', pcap_data[:24])
magic_number = pcap_header[0]
version_major = pcap_header[1]
version_minor = pcap_header[2]
thiszone = pcap_header[3]
sigfigs = pcap_header[4]
snaplen = pcap_header[5]
network = pcap_header[6]

# 解析pcap数据包
packet_header = struct.unpack('IIII', pcap_data[24:40])
timestamp = packet_header[0]
packet_length = packet_header[2]

# 读取数据包中的user-agent内容
user_agent = re.search(b'User-Agent: (.+?)\r\n', pcap_data[54:54+packet_length])
if user_agent:
    user_agent = user_agent.group(1)
    print(f'User-Agent: {user_agent.decode()}')

    # 在user-agent末尾增加标记xyz
    user_agent_xyz = user_agent + b'xyz'
    print(f'User-Agent with xyz: {user_agent_xyz.decode()}')
else:
    print('No User-Agent found.')