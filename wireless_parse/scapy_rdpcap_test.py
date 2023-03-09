import scapy.all

# windows version
vm = 'VMware Virtual Ethernet Adapter for VMnet8'


packet_list = scapy.all.rdpcap('scapy_rdpcap_test.pcap')
print(len(packet_list))


# 2层
for i, packet in enumerate(packet_list):
    if 'Ethernet' in packet:
        scapy.all.send(packet['Ethernet'], iface=vm)

    
# 3层
for i, packet in enumerate(packet_list):
    if 'IP' in packet:
        scapy.all.send(packet['IP'], iface=vm)
    
