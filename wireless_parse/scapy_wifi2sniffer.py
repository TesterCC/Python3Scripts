from scapy.all import *

wifi_interface = "wlan0mon"
lan_interface = "eth0"
iface = 'eth0'
mac = '00:0c:29:7a:fe:fd'  # iface's mac


def packet_forward(packet):
    if 'IP' in packet:
        ether = scapy.all.Ether(src=mac, dst=mac, type='IPv4')
        packet = ether / packet['IP']
        scapy.all.sendp(packet, iface=lan_interface)


sniff(iface=wifi_interface, prn=packet_forward, filter="ip")
