import socket
import struct

# 创建原生 socket，设置为混杂模式
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
sock.bind(('wlan1', 0))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 无限循环接收数据包
while True:
    data, addr = sock.recvfrom(65535)

    # 解析数据包头
    header = data[:24]
    fields = struct.unpack('!6s6sH', header)
    dst_mac = fields[0]
    src_mac = fields[1]
    eth_type = fields[2]

    # 判断是否为 IP 数据包
    if eth_type == 0x0800:
        ip_header = data[14:34]
        ip_fields = struct.unpack('!BBHHHBBH4s4s', ip_header)
        version_ihl = ip_fields[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        ip_len = ip_fields[2]
        src = socket.inet_ntoa(ip_fields[8])
        dst = socket.inet_ntoa(ip_fields[9])

        # 判断是否为 UDP 数据包
        if ip_fields[6] == 17:
            udp_header = data[34:42]
            udp_fields = struct.unpack('!HHHH', udp_header)
            src_port = udp_fields[0]
            dst_port = udp_fields[1]
            udp_len = udp_fields[2]

            # 输出 IP 和 UDP 信息
            print(f"IP: {src} -> {dst}, length: {ip_len}")
            print(f"UDP: {src_port} -> {dst_port}, length: {udp_len}")