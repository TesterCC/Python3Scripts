from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11
from scapy.layers.inet import IP, TCP, UDP
# iface = 'eth0'
# mac = '00:0c:29:7a:fe:fd' # iface's mac

packet_list = scapy.all.rdpcap('udp9999.pcap')
for packet in packet_list:
    if packet.haslayer(UDP) and packet[UDP].dport == 9999:
        # packet.show()
        packet[IP].src = '192.168.100.3'
        packet[IP].dst = '192.168.100.6'
        sendp(packet, verbose=0)
    # if 'IP' not in packet: continue
    # ether = scapy.all.Ether(src=mac, dst=mac, type='IPv4')
    # packet = ether/packet['IP']
    # scapy.all.sendp(packet, iface=iface)
