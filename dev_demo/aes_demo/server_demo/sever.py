import socket
import threading

# 客户端的IP和端口号
HOST = '192.168.200.10'
PORT = 8888


def send(sock):
    # 发送数据
    while True:
        data = input('请输入要发送的数据：')
        sock.sendall(data.encode())


def receive(sock):
    # 接收数据
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print('收到数据：', data.decode())


# 创建一个客户端socket对象
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
client_sock.connect((HOST, PORT))

# 启动发送和接收线程
t1 = threading.Thread(target=send, args=(client_sock,))
t2 = threading.Thread(target=receive, args=(client_sock,))
t1.start()
t2.start()

# 等待线程结束
t1.join()
t2.join()

# 关闭客户端socket连接
client_sock.close()
