from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP


# 定义一个处理 UDP 数据包的函数
def handle_udp_packet(packet):
    # 如果数据包类型为 UDP 数据包，则进行处理
    if packet.haslayer(UDP):
        # packet.show()
        # 获取原始 IP 头部信息和 UDP 头部信息
        ip_header = packet[IP]
        udp_header = packet[UDP]

        ip_header.src = '192.168.100.3'
        ip_header.dst = '192.168.100.6'

        del ip_header.chksum
        del udp_header.chksum
        # # 修改 UDP 数据包的源端口号和目的端口号
        # udp_header.sport = 1234
        # udp_header.dport = 5678

        # 计算新的校验和值
        udp_header.checksum = None
        new_udp_checksum = UDP(str(udp_header)).chksum
        udp_header.checksum = new_udp_checksum

        # 计算新的 IP 校验和
        ip_header.checksum = None
        new_ip_checksum = IP(str(ip_header)).chksum
        ip_header.checksum = new_ip_checksum

        # 将修改后的数据包发送到目的地址
        send(packet)


# 监听网卡上的数据包
sniff(filter="udp", prn=handle_udp_packet)
