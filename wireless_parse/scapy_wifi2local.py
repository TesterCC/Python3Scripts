import scapy.all
# bydz

iface = 'eth0'
mac = '00:0c:29:7a:fe:fd' # iface's mac

packet_list = scapy.all.rdpcap('scapy_test.pcap')
for packet in packet_list:
    if 'IP' not in packet: continue
    ether = scapy.all.Ether(src=mac, dst=mac, type='IPv4')
    packet = ether/packet['IP']
    scapy.all.sendp(packet, iface=iface)
