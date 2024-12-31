# -*- coding: utf-8 -*-
# @Time    : 2023/3/3
# @Author  : SecCodeCat

# coding=utf-8
from scapy.all import *
#  抓不到wlan的tcp
count = input("Input catch tcp num:")
now_time = datetime.now().strftime("%Y%m%d%H%M%S")
filename = "./pcap/test_{0}.pcap".format(now_time)
# filter = 'tcp.port == 2222'
o_open_file = PcapWriter(filename, append=True)


def callback(packet):
    packet.show()
    o_open_file.write(packet)


# apple report: Cannot set promiscuous mode on interface
dpkt_input = sniff(iface="llw0", count=int(count), filter='tcp', prn=callback)