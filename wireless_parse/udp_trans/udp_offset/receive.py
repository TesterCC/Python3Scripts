import socket

# 接收端IP和端口
server_ip = '127.0.0.1'
server_port = 9999

# 要保存的文件名和初始偏移量
filename = 'test.txt'
offset = 0

# 创建UDP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

# 接收数据包并写入文件
with open(filename, 'ab') as f:
    while True:
        packet, address = server_socket.recvfrom(1024)
        client_offset = int.from_bytes(packet[:8], byteorder='big')
        data = packet[8:]
        if client_offset == offset:
            f.write(data)
            offset += len(data)
        else:
            server_socket.sendto(bytes(offset), address)

# 关闭Socket
server_socket.close()