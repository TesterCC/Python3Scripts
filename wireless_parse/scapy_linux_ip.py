from scapy.all import *
from scapy.layers.inet import IP, TCP

# windows version，目前在linux下收不到
vm = 'eth0'

packet_list = scapy.all.rdpcap('scapy_test.pcap')
print(len(packet_list))


# # 2层
# for i, packet in enumerate(packet_list):
#     if 'Ethernet' in packet:
#         scapy.all.send(packet['Ethernet'], iface=vm)

    
# 3层
for i, packet in enumerate(packet_list):
    if 'IP' in packet:
        scapy.all.send(packet['IP'], iface=vm)
    
