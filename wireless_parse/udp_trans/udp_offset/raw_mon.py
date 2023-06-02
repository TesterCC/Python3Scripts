import socket

# 监听网卡wlan0mon
iface = 'wlan0mon'

# can use  可以抓到原始包
# 创建原始套接字
raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

# 绑定网卡接口
raw_socket.bind((iface, 0))

# 循环读取数据包
while True:
    packet = raw_socket.recvfrom(65535)[0]  # 最大数据包长度为65535
    # 处理数据包
    print(packet)