import socket
import struct
import time
import traceback

# byxxx
def parse_packet(data):
    packet = {}

    # eth
    eth_data_len = len(data) - 14
    eth_fmt = '!6s6s2s%ds' % eth_data_len
    eth_tuple = struct.unpack(eth_fmt, data)

    packet['smac'] = eth_tuple[1]
    packet['dmac'] = eth_tuple[0]
    packet['type'] = eth_tuple[2]
    if packet['type'] != b'\x08\x00':  # ETH_P_IP
        return packet

    # ip
    data = eth_tuple[-1]
    ip_header_len = (int(data[0]) % 0x10) * 4
    ip_option_len = ip_header_len - 20
    ip_data_len = len(data) - ip_header_len
    ip_fmt = '!ss2s2s2sss2s4s4s%ds%ds' % (ip_option_len, ip_data_len)
    ip_tuple = struct.unpack(ip_fmt, data)

    packet['protocol'] = ip_tuple[6]
    packet['src'] = socket.inet_ntoa(ip_tuple[8])   # output human readable
    packet['dst'] = socket.inet_ntoa(ip_tuple[9])
    if packet['protocol'] != b'\x06':  # IP_P_TCP
        return packet

    # tcp
    data = ip_tuple[-1]
    tcp_header_len = (int(data[12]) >> 4) * 4
    tcp_option_len = tcp_header_len - 20
    tcp_data_len = len(data) - tcp_header_len
    tcp_fmt = '!2s2s4s4sss2s2s2s%ds%ds' % (tcp_option_len, tcp_data_len)
    tcp_tuple = struct.unpack(tcp_fmt, data)

    packet['sport'] = tcp_tuple[0]
    packet['dport'] = tcp_tuple[1]
    packet['seq_num'] = tcp_tuple[2]
    packet['ack_num'] = tcp_tuple[3]
    packet['flags'] = tcp_tuple[5]
    packet['tcp_data_len'] = tcp_data_len

    return packet


if __name__ == '__main__':
    nic = 'wlan1'

    # ETH_P_IP 0x0800,  ETH_P_ALL 0x0003, ETH_P_ARP 0x0806
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))  # ETH_P_ALL
    s.bind((nic, 0))
    s.settimeout(1000)  # s

    while True:
        # recv
        data = s.recv(65536)

        # parse
        packet = parse_packet(data)
        if packet.get("protocol") == b"\x06":
	        print(packet)

