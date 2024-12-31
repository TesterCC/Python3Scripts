from scapy.all import *

# 抓取所有包
def sniff_packet(iface):
    sniff(iface=iface, prn=lambda x: x.summary())


if __name__ == '__main__':
    iface = "wlan0"
    sniff_packet(iface)
