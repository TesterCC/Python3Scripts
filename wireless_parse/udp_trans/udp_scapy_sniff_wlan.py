from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11
from scapy.layers.inet import IP, TCP, UDP

import os

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")


def packet_callback(packet):
    if packet[IP].src == '192.168.100.2':
        if packet.haslayer(UDP) and packet[UDP].dport == 9999:
            packet[IP].src = '192.168.100.3'
            packet[IP].dst = '192.168.100.6'
            send(packet, verbose=0)


sniff(filter="udp and dst port 9999 and src host 192.168.100.2", prn=packet_callback, iface="wlan0mon")
