from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11
from scapy.layers.inet import IP, TCP, UDP

wifi_interface = "wlan0mon"
lan_interface = "eth0"


# 实现无线网卡同时且仅抓取802.11或TCP包
def packet_callback(packet):
    # if packet.haslayer(Dot11) or packet.haslayer(TCP):
    if packet.haslayer(TCP):
        print(packet.summary())

        # 三层转发，如果转发到本地网卡，src不是自己的貌似会被跑掉，待验证
        # 首先判断是否为TCP包

        # 构建IP头部，将目标地址设置为本地IP
        ip = IP(dst="", src=packet[IP].src)
        # 构建TCP头部，将源端口和目标端口互换，同时将SYN和ACK标志位翻转
        tcp = TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, flags=packet[TCP].flags)
        # 构建新的数据包，将目的地址和源地址进行交换
        new_packet = ip / tcp / packet[TCP].payload
        # 发送数据包
        send(new_packet, iface=lan_interface)


# capture packets
sniff(iface="wlan0mon", prn=packet_callback, filter="tcp")
