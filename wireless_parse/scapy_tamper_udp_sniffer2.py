from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP

# 打开UDP校验和自动计算功能
conf.checksum_checks = True

# 接收数据包
# packets = sniff(filter="udp and dst port 9999")
packets = sniff(filter="udp")

for packet in packets:
    # 对数据包IP和UDP层进行修改
    packet.show()
    packet[IP].src = '192.168.100.3'
    packet[IP].dst = '192.168.100.6'
    # packet[UDP].sport = 8001
    # packet[UDP].dport = 8002
    # packet[UDP].payload = bytes.fromhex("deadbeef")

    # 计算校验和并发送数据包
    del packet[UDP].chksum
    del packet[IP].chksum

    packet.show()
    send(packet, verbose=False)
