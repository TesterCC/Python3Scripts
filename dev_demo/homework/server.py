# coding=utf-8

# multi-threaded TCP Server - block

import socket
import threading
import time
import traceback

IP = '0.0.0.0'
PORT = 9999


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # 当一个客户端成功建立链接的时候，将接收到的客户端socket对应保存到client变量中，将远程连接的详细信息保存到address变量中。
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        # 创建一个新线程，让它指向 handle_client 函数，并传入 变量 client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # 启动线程处理刚收到的连接，同时服务端的主循环已准备好处理下一个外来连接。
        client_handler.start()


def handle_client(client_socket):
    # 会调用recv()接收数据，并给客户端发送一段简单的回复
    with client_socket as sock:
        request = sock.recv(5)
        print(f'[*] Received:{request} , time: {int(time.time())}')
        if request == b"hello":
            try:
                sock.sendall(b"world\r\n")
                print("[+] send response ...")
            except ConnectionError:
                traceback.print_exc()
        sock.close()


if __name__ == '__main__':
    main()
