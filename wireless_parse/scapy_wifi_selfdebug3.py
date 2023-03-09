from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11
from scapy.layers.inet import IP, TCP, UDP

# can use, can send udp
iface = 'wlan1'
mac = '90:de:80:48:32:51' # iface's mac

packet_list = scapy.all.rdpcap('udp9999.pcap')
for packet in packet_list:
    if 'IP' not in packet: continue

    if packet.haslayer(UDP):
        # packet.show()
        packet[IP].src = '192.168.100.3'
        packet[IP].dst = '192.168.100.6'
        del packet[IP].chksum
        del packet[UDP].chksum

        ether = scapy.all.Ether(src=mac, dst=mac, type='IPv4')
        packet = ether / packet['IP']
        scapy.all.sendp(packet, iface=iface)
