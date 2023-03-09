import scapy.all

# byxxx
wifi_interface = 'MediaTek Wi-Fi 6 MT7921 Wireless LAN Card'
local_interface = 'Realtek PCIe GbE Family Controller'


packet = scapy.all.sniff(count=1, filter='tcp', iface=wifi_interface)
'''
['_T', '__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__iterlen__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_elt2pkt', '_elt2show', '_elt2sum', 
'afterglow', 'canvas_dump', 'conversations', 'diffplot', 'filter', 'getlayer', 'hexdump', 
'hexraw', 'listname', 'make_lined_table', 'make_table', 'make_tex_table', 'multiplot', 
'nsummary', 'nzpadding', 'padding', 'pdfdump', 'plot', 'psdump', 'rawhexdump', 'replace', 
'res', 'sessions', 'show', 'sr', 'stats', 'summary', 'svgdump', 'timeskew_graph']
'''
# print(dir(packet))

print(packet.hexdump())
# print(packet.rawhexdump())
# print(packet.summary())


'''
比较常用的函数包括
arpcachepoison（用于arp毒化攻击，也叫arp欺骗攻击）
arping（用于构造一个ARP的who-has包） 
send(用于发3层报文)
sendp（用于发2层报文）
sniff（用于网络嗅探，类似Wireshark和tcpdump）
sr（发送+接收3层报文）
srp（发送+接收2层报文）
'''
# print(dir(scapy.all.sendp))
# print(help(scapy.all.sendp))

scapy.all.sendp(packet, iface=local_interface)





# if_list = scapy.all.get_if_list()
# print(if_list)
# print()


# ifaces = scapy.all.conf.ifaces
# print(ifaces)
# print()
# print(ifaces.dev_from_index(1))

'''
['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_npcap_requirement', '_npcap_get', '_npcap_set', 
'availablemodes', 'availablemodulations', 'cache_mode', 'channel', 'description', 'dummy', 
'flags', 'frequence', 'guid', 'index', 'ip', 'ips', 'ipv4_metric', 'ipv6_metric', 'is_valid', 
'ismonitor', 'l2listen', 'l2socket', 'l3socket', 'mac', 'mode', 'modulation', 'name', 
'network_name', 'provider', 'raw80211', 'setchannel', 'setfrequence', 'setmode', 'setmodulation', 'setmonitor', 'update']
'''
# print(dir(ifaces.dev_from_index(1)))


# print(scapy.all.ls())


# def sniff_callback(packet):
    # print(packet)

# scapy.all.sniff(prn=sniff_callback)

