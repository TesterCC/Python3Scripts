# -*- coding=utf-8 -*-
import socket
import struct
import textwrap
import argparse

# version v1/cheat_v1.py
import time


def get_version():
    version = "1.0.1.20230515-debug"
    ret = f"Current Version: {version}"
    return ret


def compute_checksum(data):
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

def parse_packet_v2(data):
    packet = {}
    pass

def parse_packet(data):
    packet = {}

    input_data = data
    # eth
    eth_data_len = len(data) - 14
    eth_fmt = '!6s6s2s%ds' % eth_data_len
    eth_tuple = struct.unpack(eth_fmt, data)

    packet['smac'] = eth_tuple[1]
    packet['dmac'] = eth_tuple[0]
    packet['type'] = eth_tuple[2]

    print(">>>>> packet:\n", packet)

    print(packet['smac'], packet['dmac'])
    if packet['type'] != b'\x08\x00':  # ETH_P_IP
        return None

    # ip
    data = eth_tuple[-1]
    ip_header_len = (int(data[0]) % 0x10) * 4
    ip_option_len = ip_header_len - 20
    ip_data_len = len(data) - ip_header_len
    ip_fmt = '!ss2s2s2sss2s4s4s%ds%ds' % (ip_option_len, ip_data_len)
    ip_tuple = struct.unpack(ip_fmt, data)

    packet['protocol'] = ip_tuple[6]
    packet['src'] = socket.inet_ntoa(ip_tuple[8])
    packet['dst'] = socket.inet_ntoa(ip_tuple[9])

    if packet['protocol'] != b'\x11':  # IP_P_UDP
        return None

    # udp
    data = ip_tuple[-1]
    udp_data_len = len(data) - 8
    udp_fmt = '!2s2s2s2s%ds' % udp_data_len
    udp_tuple = struct.unpack(udp_fmt, data)

    packet['sport'] = udp_tuple[0]
    packet['dport'] = udp_tuple[1]
    packet['len'] = udp_tuple[2]
    packet['checksum'] = udp_tuple[3]
    packet['udp_data'] = udp_tuple[4] if udp_data_len > 0 else b''

    print("==", packet['protocol'], packet['src'], packet['sport'], packet['dst'], packet['dport'], packet['len'])
    return packet


def get_new_body_v2(src, dst, body):
    # udp
    protocol = b'\x00\x11'
    blen = struct.pack("!H", len(body))
    bsrc = socket.inet_aton(src)
    bdst = socket.inet_aton(dst)
    checksum_data = bsrc + bdst + protocol + blen + body[:6] + b"\x00\x00" + body[8:]
    bchecksum = struct.pack("!H", compute_checksum(checksum_data))
    return body[:6] + bchecksum + body[8:]


def run(args):
    na_ip = args.na
    nb_ip = args.nb
    nc_ip = args.nc
    nd_ip = args.nd

    b_nb_ip = socket.inet_aton(nb_ip)
    b_nc_ip = socket.inet_aton(nc_ip)
    b_nd_ip = socket.inet_aton(nd_ip)

    nic = args.nic

    print(f'node a : {args.na}')
    print(f'node b : {args.nb}')
    print(f'node c : {args.nc}')
    print(f'node d : {args.nd}')
    print(f'network interface card : {args.nic}')

    recv_s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))  # ETH_P_IP
    recv_s.bind((nic, 0))

    send_fd = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    send_fd.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    buf_len = 4096

    while True:
        buf = recv_s.recv(buf_len)
        pack = parse_packet(buf)
        if pack is None:
            continue

        if pack["src"] == na_ip and pack["dst"] == nb_ip:
            _, phdr, body = struct.unpack("!14s20s%ds" % (len(buf) - 34), buf)

            # todo na -> nb, nc -> nd
            print(nc_ip, nd_ip)
            body = get_new_body_v2(nc_ip, nd_ip, body)

            # change dst mac
            # newpack = phdr[:10] + b"\x00\x00" + phdr[12:-8] + b_nb_ip + b_nc_ip
            newpack = phdr[:10] + b"\x00\x00" + phdr[12:-8] + b_nc_ip + b_nd_ip
            checksum = struct.pack("!H", compute_checksum(newpack))
            dst_port = struct.unpack("<H", body[2:4])[0]

            # bpack = phdr[:10] + checksum + phdr[12:-8] + b_nb_ip + b_nc_ip + body
            bpack = phdr[:10] + checksum + phdr[12:-8] + b_nc_ip + b_nd_ip + body
            print("bpack", bpack)
            # send_fd.sendto(bpack, (nc_ip, dst_port))
            send_fd.sendto(bpack, (nd_ip, dst_port))
            time.sleep(0.001)


if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser(
            description='Cheat Netflow Tool - Debug',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''Example:
            python3 cheat_v2.py -a 192.168.100.2 -b 192.168.101.7 -c 192.168.100.3 -d 192.168.100.6 -i wlan1
            '''))

        parser.add_argument('-a', '--na', type=str, default="", required=True, help='node a ip address')
        parser.add_argument('-b', '--nb', type=str, default="", required=True, help='node b ip address')
        parser.add_argument('-c', '--nc', type=str, default="", required=True, help='node c ip address, monitor server')
        parser.add_argument('-d', '--nd', type=str, default="", required=True, help='node d ip address')
        parser.add_argument('-i', '--nic', type=str, default="wlan1", help='wireless network card')
        parser.add_argument('-V', '--version', action='version', version=get_version(), help='display version info')
        args = parser.parse_args()

        run(args)

    except Exception as e:
        pass
