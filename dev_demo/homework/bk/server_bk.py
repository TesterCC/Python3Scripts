# coding=utf-8
"""
DATE:   2021/10/28
AUTHOR: TesterCC
"""

# P12 multi-threaded TCP Server

import socket
import threading

IP = '0.0.0.0'
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # 当一个客户端成功建立链接的时候，将接收到的客户端socket对应保存到client变量中，将远程连接的详细信息保存到address变量中。
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        # todo debug
        with client as sock:
            request = sock.recv(1024)
            print(f'[*] 1st Received: {request.decode("utf-8")}')
            if request.decode("utf-8") == "aabbccdd":
                sock.send(b'ABCD11223344')
                ret2_header = sock.recv(4)
                if ret2_header.decode("utf-8") == "RETN":
                    ret2_content = sock.recv(8)
                    ret2_content_str = ret2_content.decode("utf-8")
                    print(f"[*] 2ed ret data: {ret2_content_str}")
        # todo debug

        # # 创建一个新线程，让它指向 handle_client 函数，并传入 变量 client
        # client_handler = threading.Thread(target=handle_client, args=(client,))
        # # 启动线程处理刚收到的连接，同时服务端的主循环已准备好处理下一个外来连接。
        # client_handler.start()

#
# def handle_client(client_socket):
#     # 会调用recv()接收数据，并给客户端发送一段简单的回复
#     with client_socket as sock:
#         request = sock.recv(1024)
#         print(f'[*] 1st Received: {request.decode("utf-8")}')
#         if request.decode("utf-8") == "aabbccdd":
#             sock.send(b'ABCD11223344')
#             ret2_header = sock.recv(4)
#             if ret2_header.decode("utf-8") == "RETN":
#                 ret2_content = sock.recv(8)
#                 ret2_content_str = ret2_content.decode("utf-8")
#                 print(f"[*] 2ed ret data: {ret2_content_str}")


if __name__ == '__main__':
    main()
