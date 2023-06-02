import socket
import threading

'''
no test
这个示例代码创建了一个简单的TCP服务器，它可以同时处理多个客户端连接。当服务器收到来自客户端的数据时，它会在控制台上显示收到的数据。
同时，你可以在控制台上输入数据并按Enter键发送给客户端。
注意：这个示例代码是一个简易版本，仅适用于演示目的。在实际应用中，你可能需要对异常情况进行更详细的处理，并在关闭套接字之前确保所有线程都已完成。
'''

# 创建一个TCP套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定套接字到地址和端口
host = "localhost"
port = 12345
server_socket.bind((host, port))

# 监听连接
server_socket.listen(5)

def handle_client(client_socket):
    while True:
        try:
            # 尝试接收数据
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received:", data.decode("utf-8"))

            # 尝试发送数据
            message = input("Send: ")
            client_socket.send(message.encode("utf-8"))
        except Exception as e:
            print("Error:", e)
            break

    client_socket.close()

def accept_connections():
    while True:
        # 接受新连接
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established")

        # 为每个连接创建一个新的线程
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# 创建一个线程用于接受新的连接
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

# 主线程等待accept线程结束
accept_thread.join()
server_socket.close()