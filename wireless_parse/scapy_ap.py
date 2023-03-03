from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon

interface = "wlan0"
ap_list = []


def info(fm):
    if fm.haslayer(Dot11Beacon):
        if fm.addr2 not in ap_list:
            ap_list.append(fm.addr2)
            print(f"SSID --> {fm.info}, -- BSSID --> {fm.addr2}")
            # SSID --> b'CTC', -- BSSID --> 00:c0:02:2c:a5:a2

sniff(iface=interface, prn=info)
