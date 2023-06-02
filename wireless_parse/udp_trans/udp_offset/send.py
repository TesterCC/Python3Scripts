import socket

# 发送端IP和端口
client_ip = '127.0.0.1'
client_port = 8888

# 目标IP和端口
server_ip = '127.0.0.1'
server_port = 9999

# 要传输的文件名和初始偏移量
filename = 'test.txt'
offset = 0

# 创建UDP Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据包
with open(filename, 'rb') as f:
    f.seek(offset)
    data = f.read(1024)  # 每次发送1024字节
    while data:
        packet = bytes(offset) + data
        client_socket.sendto(packet, (server_ip, server_port))
        offset += len(data)
        f.seek(offset)
        data = f.read(1024)

# 关闭Socket
client_socket.close()