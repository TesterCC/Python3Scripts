import os
import socket
import subprocess

"""
run in server:
Python3使用threading库和socket库实现多线程非阻塞式的同时收发数据，要求先发送数据后，能保持长连接并接受后续收到的数据
"""

# 服务器的IP和端口号
HOST = '0.0.0.0'
PORT = 8888

# 创建一个服务器socket对象
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定IP和端口号
server_sock.bind((HOST, PORT))
# 开始监听
server_sock.listen()

print('等待客户端连接...')

# 等待客户端连接
client_sock, addr = server_sock.accept()

print('客户端已连接，地址为：', addr)

# 接收数据并发送响应
while True:
    data = client_sock.recv(1024)

    # print(data.decode().strip())
    # print(type(data.decode()))

    if not data:
        break
    if data.decode().strip() in ["ls", "pwd", "id", "groups"]:
        # print("--" * 10)
        _, ret = subprocess.getstatusoutput(data.decode().strip())
        # print(f"[D] ret: {ret}")
        response = '反馈命令 {} 的执行结果：{}'.format(data.decode().strip(),ret)
        client_sock.sendall(response.encode())
    else:
        print('收到数据：', data.decode())
        response = '收到了你的消息：{}'.format(data.decode())
        client_sock.sendall(response.encode())

# 关闭socket连接
client_sock.close()
server_sock.close()
