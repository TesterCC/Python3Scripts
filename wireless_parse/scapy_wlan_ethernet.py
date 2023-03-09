from scapy.all import *

wifi_interface = "wlan0mon"
lan_interface = "eth0"

packet = sniff(iface=wifi_interface, filter="tcp", count=1)
print(packet.hexdump())

for i in range(100):
    print(packet.summary())
    sendp(packet, iface=lan_interface)