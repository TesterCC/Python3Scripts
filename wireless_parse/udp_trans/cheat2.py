import socket
import struct
from tabnanny import check
import time
import threading


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
    if packet['protocol'] != b'\x06':  # IP_P_TCP
        return None

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


def get_new_body(src, dst, body):
    protocol = b'\x00\x06'
    blen = struct.pack("!H", len(body))
    bsrc = socket.inet_aton(src)
    bdst = socket.inet_aton(dst)
    checksum_data = bsrc + bdst + protocol + blen + body[:16] + b"\x00\x00" + body[18:]
    bchecksum = struct.pack("!H", compute_checksum(checksum_data))
    return body[:16] + bchecksum + body[18:]


def main():
    fip = "192.168.100.2"
    fkip = "192.168.100.3"  # if cannot use, change bfkip to local ip
    reip = "192.168.100.6"
    breip = socket.inet_aton(reip)
    bfkip = socket.inet_aton(fkip)
    # dmac = b'\x00\x0c\x29\xb3\x04\xa1'
    # smac = b'\x00\x0c\x29\xf7\xe6\x48'

    nic = 'wlan1'
    recv_s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))  # ETH_P_IP
    recv_s.bind((nic, 0))

    # send_fd = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
    # send_fd = socket.socket(socket.PF_INET, socket.SOCK_RAW) # ETH_P_IP
    send_fd = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    send_fd.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # send_fd.bind(('eth1',0))
    buf_len = 8192

    index = 0
    while True:
        buf = recv_s.recv(buf_len)
        pack = parse_packet(buf)
        if pack is None:
            continue
        print("------------")
        print(pack)
        print("------------")
        if pack["src"] == fip and pack["dst"] == fkip:
            print("start:")
            print(buf)
            _, phdr, body = struct.unpack("!14s20s%ds" % (len(buf) - 34), buf)
            body = get_new_body(fkip, reip, body)

            # change dst mac
            newpack = phdr[:10] + b"\x00\x00" + phdr[12:-8] + bfkip + breip
            checksum = struct.pack("!H", compute_checksum(newpack))
            dst_port = struct.unpack("<H", body[2:4])[0]
            # bpack = dmac + smac + eth[12:] + phdr[:10] + checksum + phdr[12:-4] + breip + body
            bpack = phdr[:10] + checksum + phdr[12:-8] + bfkip + breip + body
            print(bpack)
            send_fd.sendto(bpack, (reip, dst_port))
            # buf = send_fd.recvfrom(buf_len)


if __name__ == "__main__":
    main()
