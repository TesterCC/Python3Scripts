from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP


def packet_callback(packet):
    # 检查数据包是否包含IP和UDP头部信息
    if IP in packet and UDP in packet:
        # 检查数据包目的IP为192.168.100.3，源IP为192.168.100.2的条件
        if packet[IP].dst == "192.168.100.3" and packet[IP].src == "192.168.100.2":
            # 修改数据包的源IP和目的IP
            packet[IP].src = "192.168.100.3"
            packet[IP].dst = "192.168.100.6"
            # 发送修改过的数据包
            send(packet)

# 设置监听过滤器
sniff(filter="udp", prn=packet_callback, store=0)
