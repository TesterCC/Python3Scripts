from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11
from scapy.layers.inet import IP, TCP, UDP

wifi_interface = "wlan0mon"
lan_interface = "eth0"


# 实现无线网卡同时且仅抓取802.11或TCP包
def packet_forward(packet):
    if packet.haslayer(TCP):
        print(packet.summary())
        # print(packet.hexdump()) # error
        scapy.all.sendp(packet, iface=lan_interface)


# capture packets
sniff(iface=wifi_interface, prn=packet_forward, filter="tcp")
