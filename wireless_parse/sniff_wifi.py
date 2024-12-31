# coding=utf-8
"""
DATE:   2021/8/9
AUTHOR: TesterCC
"""

# 抓包 sniffer pkt; 发包forward pkt
# ref: https://cloud.tencent.com/developer/article/1694737
# https://blog.csdn.net/GFS_lele/article/details/105132287

from scapy.all import *

from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon
from scapy.layers.inet import IP, TCP, UDP

interface = "wlan0"
ap_list = []


def info(pkt):
    # if pkt.haslayer('Ethernet'):
    #     print(
    #         f"[Eth] Ethernet Info: {pkt['Ethernet'].src} -> {pkt['Ethernet'].dst}, type is {pkt['Ethernet'].type} ")

    # if pkt.haslayer('IP'):
    #     print(
    #         f"[IP] IP Info: {pkt['IP'].src} -> {pkt['IP'].dst}, protocol is : {pkt['IP'].proto}, ttl is : {pkt['IP'].ttl}")

    if pkt.haslayer(Dot11Beacon):
        if pkt.addr2 not in ap_list:
            ap_list.append(pkt.addr2)
            print(f"[802.11] SSID --> {pkt.info}, -- BSSID --> {pkt.addr2}")
            # SSID --> b'CTC', -- BSSID --> 00:c0:02:2c:a5:a2

    if pkt.haslayer('TCP'):
        # print(f"[D] {pkt[TCP]}")
        src = pkt[IP].src
        dst = pkt[IP].dst
        src_port = pkt[TCP].sport
        dst_port = pkt[TCP].dport
        tcp_flag = pkt.getlayer(TCP).flags
        print(f"[TCP] src: {src}:{src_port}, dst: {dst}:{dst_port}, tcp flag: {tcp_flag}")

    # if pkt.haslayer('UDP'):
    #     print(f"[UDP] UDP Info: {pkt['UDP'].sport} -> {pkt['UDP'].dport}, udp data length: {pkt['UDP'].len}")

    # if pkt.haslayer('ARP'):
    #     print(f"[ARP] ARP Info: {pkt['ARP'].psrc} -> {pkt['ARP'].pdst}; [ARP] ARP hw Info: {pkt['ARP'].hwsrc} -> {pkt['ARP'].hwdst}")

    # print(pkt.show())
    # pkt.display()  # 这个是优化为可度的展示
    # print(pkt.haslayer('Ether'))  # True or False


sniff(iface=interface, prn=info, count=0)

'''
　　count：抓包的数量，0表示无限制；
　　store：保存抓取的数据包或者丢弃，1保存，0丢弃
　　offline：从 pcap 文件读取数据包，而不进行嗅探，默认为None
　　prn：为每一个数据包定义一个函数，如果返回了什么，则显示。例如：prn = lambda x: x.summary()；（packct.summar()函数返回的是对包的统计性信息）
　　filter：过滤规则，使用wireshark里面的过滤语法
　　L2socket：使用给定的 L2socket
　　timeout：在给定的时间后停止嗅探，默认为 None
　　opened_socket：对指定的对象使用 .recv() 进行读取；
　　stop_filter：定义一个函数，决定在抓到指定数据包后停止抓包，如：stop_filter = lambda x: x.haslayer(TCP)；
　　iface：指定抓包的接口
'''
