# coding=utf-8
import os
import time
import socket
import struct
import traceback

# standard ref
# parse_eth
# parse_arp
# parse_ip
# parse_icmp
# parse_tcp
# parse_udp

# intb                          # 字节转化为整型
# ipb                           # 字节转换为IP字符串

# compute_checksum
# make_eth_header
# make_ip_header
# make_tcp_header

# send_icmp
# send_tcp                      # 发送tcp包
# send_syn                      # 发送syn包
# send_rst                      # 发送rst包

# get_nic_info


def parse_eth(data):
    eth_packet = {}

    eth_data_len = len(data) - 14
    eth_fmt = '!6s6s2s%ds' % eth_data_len
    eth_tuple = struct.unpack(eth_fmt, data)

    eth_packet['dmac'] = eth_tuple[0]
    eth_packet['smac'] = eth_tuple[1]
    eth_packet['type'] = eth_tuple[2]
    eth_packet['eth_data'] = eth_tuple[3]

    return eth_packet


def parse_arp(data):
    arp_packet = {}

    arp_data_len = len(data) - 28
    arp_fmt = '!2s2s1s1s2s6s4s6s4s%ds' % arp_data_len
    arp_tuple = struct.unpack(arp_fmt, data)

    arp_packet['hardware_type'] = arp_tuple[0]
    arp_packet['protocol_type'] = arp_tuple[1]
    arp_packet['hardware_size'] = arp_tuple[2]
    arp_packet['protocol_size'] = arp_tuple[3]
    arp_packet['opcode'] = arp_tuple[4]  # 0x0001 request, 0x0002 reply
    arp_packet['sender_mac'] = arp_tuple[5]
    arp_packet['sender_ip'] = arp_tuple[6]
    arp_packet['target_mac'] = arp_tuple[7]
    arp_packet['target_ip'] = arp_tuple[8]
    arp_packet['option_data'] = arp_tuple[9]

    return arp_packet


def parse_ip(data):
    ip_packet = {}

    ip_data_len = len(data) - 20
    ip_fmt = '!2s2s2s2s1s1s2s4s4s%ds' % ip_data_len
    ip_tuple = struct.unpack(ip_fmt, data)

    ip_packet['version_and_header_len'] = ip_tuple[0]
    ip_packet['len'] = ip_tuple[1]
    ip_packet['id'] = ip_tuple[2]
    ip_packet['flags'] = ip_tuple[3]
    ip_packet['ttl'] = ip_tuple[4]
    ip_packet['protocol'] = ip_tuple[5]
    ip_packet['checksum'] = ip_tuple[6]
    ip_packet['src'] = ip_tuple[7]
    ip_packet['dst'] = ip_tuple[8]
    ip_packet['ip_data'] = ip_tuple[9] if ip_data_len > 0 else b''

    return ip_packet


def parse_icmp(data):
    icmp_packet = {}

    icmp_data_len = len(data) - 8
    icmp_fmt = '!1s1s2s2s2s%ds' % icmp_data_len
    icmp_tuple = struct.unpack(icmp_fmt, data)

    icmp_packet['type'] = icmp_tuple[0]  # 0x08 request, 0x00 reply
    icmp_packet['code'] = icmp_tuple[1]
    icmp_packet['checksum'] = icmp_tuple[2]
    icmp_packet['id'] = icmp_tuple[3]
    icmp_packet['seq'] = icmp_tuple[4]
    icmp_packet['icmp_data'] = icmp_tuple[5] if icmp_data_len > 0 else b''

    return icmp_packet


def parse_tcp(data):
    tcp_packet = {}

    tcp_data_len = len(data) - 20
    tcp_fmt = '!2s2s4s4s2s2s2s2s%ds' % tcp_data_len
    tcp_tuple = struct.unpack(tcp_fmt, data)

    tcp_packet['sport'] = tcp_tuple[0]
    tcp_packet['dport'] = tcp_tuple[1]
    tcp_packet['seq'] = tcp_tuple[2]
    tcp_packet['ack'] = tcp_tuple[3]
    tcp_packet['flags'] = tcp_tuple[4]
    tcp_packet['window_size'] = tcp_tuple[5]
    tcp_packet['checksum'] = tcp_tuple[6]
    tcp_packet['urgent_pointer'] = tcp_tuple[7]
    tcp_packet['tcp_data'] = tcp_tuple[8] if tcp_data_len > 0 else b''

    return tcp_packet


def parse_udp(data):
    udp_packet = {}

    udp_data_len = len(data) - 8
    # 2s refer to 2 bytes， UDP packet first 8 bytes, 16bits == 2bytes (1bytes = 8bits, here 2bytes)
    # udp src port 16bits (2bytes), udp dst port 16bits (2bytes), udp length 16bits (2bytes), udp checksum 16bits (2bytes)
    udp_fmt = '!2s2s2s2s%ds' % udp_data_len
    udp_tuple = struct.unpack(udp_fmt, data)

    udp_packet['sport'] = udp_tuple[0]
    udp_packet['dport'] = udp_tuple[1]
    udp_packet['len'] = udp_tuple[2]
    udp_packet['checksum'] = udp_tuple[3]
    udp_packet['udp_data'] = udp_tuple[4] if udp_data_len > 0 else b''

    return udp_packet


def intb(data):
    return int.from_bytes(data, 'big')


def ipb(data):
    return '.'.join(['%d' % byte for byte in data])


def compute_checksum(data):
    '''
    计算校验和逻辑：
    1- 用 \x00\x00 在校验和位置占位
    2- 所有数据加总
    3- 如果加总后大于 0x1 0000，则将高位和低位拆开再加总，重复这个过程，直到结果不大于 0x10000
    4- 使用 0xFFFF - 结果 = 校验和
    5- 将 校验和 替换到第一步的 \x00\x00 占位处

    例子：
    IP头：
    45 00    00 31
    89 F5    00 00
    6E 06    00 00（校验字段）
    DE B7   45 5D       ->    222.183.69.93   (源IP地址)
    C0 A8   00 DC       ->    192.168.0.220  (目的IP地址)

    计算：
    4500 + 0031 + 89F5 + 0000 + 6E06 + 0000 + DEB7 + 455D + C0A8 + 00DC =3 22C4 （结果大于 1 0000, 继续迭代计算)
    0003 22C4  =>  0003 + 22C4 = 22C7
    FFFF - 22C7 = DD38      -> 校验和
    最终头部：
    45 00    00 31
    89 F5    00 00
    6E 06    DD 38（校验字段）
    DE B7   45 5D       ->    222.183.69.93   (源IP地址)
    C0 A8   00 DC       ->    192.168.0.220  (目的IP地址)


    校验和 验证逻辑：
    1- 将头部加总
    2- 加总后结果一定大于 0x1 0000
    3- 用 高位 + 低位 = 0xFFFF 则说明 校验和正常

    例子：
    4500 + 0031 + 89F5 + 0000 + 6E06 + DD38 + DEB7 + 455D + C0A8 + 00DC =3 FFFC
    0003 + FFFC = FFFF      ->校验和正常
    '''

    # padding
    if len(data) % 2 == 1:
        data += b'\x00'

    # add
    checksum = 0
    for i in range(int(len(data) / 2)):
        checksum += data[i * 2] * 0x100 + data[i * 2 + 1]

    # 32 -> 16
    while checksum > 0x10000:
        checksum = int(checksum / 0x10000) + (checksum % 0x10000)

    # 0xffff diff
    checksum = 0xffff - checksum

    return checksum


def make_eth_header(smac, dmac):
    ip_type = b'\x08\x00'
    header = dmac + smac + ip_type

    return header


def make_ip_header(src, dst, data_len, protocol=b'\x06'):
    ipv4 = b'\x45\x00'
    ip_len = struct.pack("!H", 20 + data_len)
    _id = b'\x24\x6e'
    flags = b'\x40\x00'  # don't flag
    ttl = b'\x40'  # 64
    checksum = b'\x00\x00'

    #
    check_data = ipv4 + ip_len + _id + flags + ttl + protocol + checksum + src + dst
    checksum = struct.pack("!H", compute_checksum(check_data))

    # 
    ip_header = ipv4 + ip_len + _id + flags + ttl + protocol + checksum + src + dst

    return ip_header


def make_tcp_header(src, dst, sport, dport, seq, ack, flags, data):
    protocol = b'\x00\x06'
    tcp_len = struct.pack("!H", 20 + len(data))
    header_len = b'\x50'
    window = b'\x00\x00'
    checksum = b'\x00\x00'
    urgent_pointer = b'\x00\x00'

    #
    pseudo_header = src + dst + protocol + tcp_len
    pseudo_header += sport + dport + seq + ack
    pseudo_header += header_len + flags + window
    pseudo_header += checksum + urgent_pointer + data
    checksum = struct.pack("!H", compute_checksum(pseudo_header))

    #
    tcp_header = sport + dport + seq + ack
    tcp_header += header_len + flags + window
    tcp_header += checksum + urgent_pointer

    return tcp_header


def send_icmp(s, smac, dmac, src, dst):
    data = b'\x08\x00\x3d\x5a\x00\x01\x10\x01\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69'

    # packet
    ip_header = make_ip_header(src, dst, len(data), protocol=b'\x01')
    eth_header = make_eth_header(smac, dmac)
    packet = eth_header + ip_header + data

    s.send(packet)


def send_tcp(s, smac, dmac, src, dst, sport, dport, seq, ack, flags, data):
    tcp_header = make_tcp_header(src, dst, sport, dport, seq, ack, flags, data)
    ip_header = make_ip_header(src, dst, len(tcp_header + data))
    eth_header = make_eth_header(smac, dmac)
    packet = eth_header + ip_header + tcp_header + data
    s.send(packet)


def send_syn(s, smac, dmac, src, dst, sport, dport):
    seq = b'\x01\x02\x03\x04'
    ack = b'\x00\x00\x00\x00'
    flags = b'\x02'  # syn = 0x02
    data = b''
    send_tcp(s, smac, dmac, src, dst, sport, dport, seq, ack, flags, data)


def send_rst(s, smac, dmac, src, dst, sport, dport, seq, ack):
    flags = struct.pack('!B', (0x04 | 0x10))  # ack = 0x10, rst = 0x04
    data = b''
    send_tcp(s, smac, dmac, src, dst, sport, dport, seq, ack, flags, data)


def get_nic_info(nic):
    nic_info = {'ip': '', 'mac': '', 'gw': '', 'gw_mac': ''}

    try:
        # ip, gw
        ifcfg_file = '/etc/sysconfig/network-scripts/ifcfg-%s' % nic
        with open(ifcfg_file) as f:
            for conf in f.readlines():
                try:
                    k = conf.split('=')[0].strip().replace('"', '')
                    v = conf.split('=')[1].strip().replace('"', '')
                    if k == 'IPADDR':
                        nic_info['ip'] = struct.pack('4B', *[int(byte) for byte in v.split(".")])
                    if k == 'GATEWAY':
                        nic_info['gw'] = struct.pack('4B', *[int(byte) for byte in v.split(".")])
                except:
                    pass

        if nic_info['ip'] == '' or nic_info['gw'] == '':
            raise

        # mac
        s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))  # ETH_P_IP
        s.settimeout(5)
        s.bind((nic, 0))
        os.system('nohup ping %s -c 10 &' % ipb(nic_info['gw']))

        start_time = time.time()
        while True:
            if time.time() - start_time > 10:
                break

            try:
                data = s.recv(65536)
            except:
                continue

            eth_packet = parse_eth(data)
            if eth_packet['type'] != b'\x08\x00':
                continue

            ip_packet = parse_ip(eth_packet['eth_data'])
            if ip_packet['src'] == nic_info['ip']:
                nic_info['mac'] = eth_packet['smac']
            if ip_packet['dst'] == nic_info['ip']:
                nic_info['mac'] = eth_packet['dmac']
            if ip_packet['src'] == nic_info['gw']:
                nic_info['gw_mac'] = eth_packet['smac']
            if ip_packet['dst'] == nic_info['gw']:
                nic_info['gw_mac'] = eth_packet['dmac']
            if nic_info['mac'] != '' and nic_info['gw_mac'] != '':
                break

    except:
        traceback.print_exc()
        pass

    return nic_info
