from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11
from scapy.layers.inet import IP, TCP, UDP


# 实现无线网卡同时且仅抓取802.11或TCP包
def packet_callback(packet):
    if packet.haslayer(Dot11) or packet.haslayer(TCP):
        print(packet.summary())


# capture packets
sniff(iface="wlan0", prn=packet_callback, filter=lambda p: (Dot11 in p or TCP in p))
