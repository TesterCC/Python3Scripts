from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon
from scapy.layers.inet import IP, TCP, UDP

interface = "wlan0"
ap_list = []


def info(pkt):
    
    if pkt.haslayer('Ethernet'):
        print("[+] Get {} Info:".format("Ethernet"))
        print(pkt['Ethernet'].src)
        print(pkt['Ethernet'].dst)
        print(pkt['Ethernet'].type)
        print("\n")
        
    if pkt.haslayer(Dot11Beacon):
        if pkt.addr2 not in ap_list:
            ap_list.append(pkt.addr2)
            print(f"[802.11] SSID --> {pkt.info}, -- BSSID --> {pkt.addr2}")
            # SSID --> b'CTC', -- BSSID --> 00:c0:02:2c:a5:a2

    if pkt.haslayer(TCP):
        # print(f"[D] {pkt[TCP]}")
        src = pkt[TCP].sport
        dst = pkt[TCP].dport
        tcp_flag = pkt.getlayer(TCP).flags
        print(f"[TCP] src: {src}, dst: {dst}, flag: {tcp_flag}")

    if pkt.haslayer('UDP'):
        print("[+] Get {} Info:".format("UDP"))
        print(pkt['UDP'].sport)
        print(pkt['UDP'].dport)
        print(pkt['UDP'].len)
        print("\n")

    if pkt.haslayer('ARP'):
        print("[+] Get {} Info:".format("ARP"))
        print(pkt['ARP'].psrc)
        print(pkt['ARP'].pdst)
        print(pkt['ARP'].hwsrc)
        print(pkt['ARP'].hwdst)
        print("\n")


sniff(iface=interface, prn=info)
