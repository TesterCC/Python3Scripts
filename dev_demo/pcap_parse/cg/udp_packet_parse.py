import ipaddress


def parse_udp_packet(data):
    data['smac'] = ':'.join('{:02x}'.format(x) for x in data['smac'])  # 将MAC地址转换为字符串，格式为 xx:xx:xx:xx:xx:xx
    data['dmac'] = ':'.join('{:02x}'.format(x) for x in data['dmac'])

    data['type'] = data['type'].hex()  # 将数据帧类型转换为16进制字符串
    data['protocol'] = data['protocol'].hex()  # 将协议类型转换为16进制字符串

    data['src'] = str(ipaddress.IPv4Address(data['src']))  # 将IP地址转换为字符串类型
    data['dst'] = str(ipaddress.IPv4Address(data['dst']))

    data['sport'] = int.from_bytes(data['sport'], byteorder='big')  # 将端口号转换为10进制数字类型
    data['dport'] = int.from_bytes(data['dport'], byteorder='big')

    data['len'] = int.from_bytes(data['len'], byteorder='big')  # 将UDP数据包长度转换为10进制数字类型
    data['checksum'] = data['checksum'].hex()  # 将UDP校验和转换为16进制字符串

    data['udp_data'] = data['udp_data'].decode('utf-8')


if __name__ == '__main__':
    parse_udp_packet()
