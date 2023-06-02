import socket
import struct
import ctypes

# 定义IP头部结构体
class IP(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_ubyte, 4),
        ("ihl", ctypes.c_ubyte, 4),
        ("tos", ctypes.c_ubyte),
        ("len", ctypes.c_ushort),
        ("id", ctypes.c_ushort),
        ("flags", ctypes.c_ushort, 3),
        ("frag_offset", ctypes.c_ushort, 13),
        ("ttl", ctypes.c_ubyte),
        ("protocol_num", ctypes.c_ubyte),
        ("sum", ctypes.c_ushort),
        ("src", ctypes.c_uint32),
        ("dst", ctypes.c_uint32)
    ]

    def __new__(self, buffer):
        return self.from_buffer_copy(buffer)

    def __init__(self, buffer):
        # 计算IP头部的checksum
        self.checksum = self.calculate_checksum(buffer[0:20])

    def calculate_checksum(self, buffer):
        # 将checksum字段设置为0
        self.sum = 0

        # 计算checksum
        count_to = (self.iplength // 2) * 2
        sum = 0
        count = 0
        while count < count_to:
            this_val = buffer[count+1] * 256 + buffer[count]
            sum = sum + this_val
            sum = sum & 0xffffffff
            count = count + 2
        if count_to < self.iplength:
            sum = sum + buffer[self.iplength-1]
            sum = sum & 0xffffffff
        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer

    def to_bytes(self):
        return ctypes.string_at(ctypes.byref(self), ctypes.sizeof(self))

# 设置网络接口和监听的端口号
interface = "wlan0mon"
port = 80

# 监听数据包
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
sniffer.bind((interface, port))

# 接收数据包
while True:
    packet = sniffer.recvfrom(65565)[0]

    # 解析IP头部
    ip_header = packet[14:34]
    iph = IP(ip_header)

    # 获取源IP和目标IP地址
    src_ip = socket.inet_ntoa(iph.src)
    dst_ip = socket.inet_ntoa(iph.dst)

    print("src_ip: ", src_ip)
    print("dst_ip: ", dst_ip)

    # 判断是否为目标数据包
    if src_ip == '192.168.100.102' and dst_ip == '192.168.101.7':
        # 替换目标IP地址和端口号
        iph.dst = socket.inet_aton('192.168.100.106')
        iph.src = socket.inet_aton('192.168.101.3')

        # 重新计算IP头部的checksum
        iph.checksum = iph.calculate_checksum(iph.to_bytes())

        # 构造新的数据包
        new_packet = packet[:14] + iph.to_bytes() + packet[34:]

        # 发送数据包
        sender = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        sender.bind((interface, 0))
        sender.send(new_packet)