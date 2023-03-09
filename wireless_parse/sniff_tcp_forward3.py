from scapy.all import *

wifi_interface = "wlan0mon"
lan_interface = "eth0"


# 实现无线网卡同时且仅抓取802.11或TCP包
def packet_forward(packet):
    scapy.all.send(packet['IP'], iface=lan_interface)


# capture packets
sniff(iface=wifi_interface, prn=packet_forward, filter="ip")
