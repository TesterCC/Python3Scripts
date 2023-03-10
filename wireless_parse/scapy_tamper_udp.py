from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11
from scapy.layers.inet import IP, TCP, UDP

# can use, can send udp
iface = 'wlan1'
mac = '90:de:80:48:32:51' # iface's mac

packet_list = scapy.all.rdpcap('udp0310.pcap')
for packet in packet_list:
    if 'IP' not in packet: continue

    if packet.haslayer(UDP):
        # packet.show()
        packet[IP].src = '192.168.100.3'
        packet[IP].dst = '192.168.100.6'

        # compute  checksum and update packet
        del packet[IP].chksum
        del packet[UDP].chksum

        packet[UDP] = packet[UDP].__class__(packet[UDP])
        packet[IP] = packet[IP].__class__(packet[IP])
        chksum = UDP(str(packet[UDP])).chksum
        packet[UDP].chksum = chksum
        packet[IP].chksum = None  # 让scapy自动计算新的IP校验和

        ether = scapy.all.Ether(src=mac, dst=mac, type='IPv4')
        packet = ether / packet['IP']
        # scapy.all.sendp(packet, iface=iface)
        scapy.all.send(packet)
