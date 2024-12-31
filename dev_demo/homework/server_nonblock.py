# coding=utf-8

# TCP server - non block, select

import socket
import select
import time
import traceback

IP = '0.0.0.0'
PORT = 9999

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((IP, PORT))
sock.setblocking(False)  # 设置非阻塞
sock.listen()

inputs = [sock, ]

while True:
    # 传递三个参数，一个为输入而观察的文件对象列表，一个为输出而观察的文件对象列表和一个观察错误异常的文件列表。第四个是一个可选参数，表示超时秒数。
    r_list, w_list, e_list = select.select(inputs, [], [], 1)
    for event in r_list:
        if event == sock:
            print("[+] new client connection ...")
            new_sock, addr = event.accept()
            inputs.append(new_sock)
        else:
            data = event.recv(5)
            if data:
                print(f'[*] received:{data} , time: {int(time.time())}')
                if data == b"hello":
                    try:
                        event.sendall(b"world\r\n")
                        print("[+] send response ...")
                    except ConnectionError:
                        traceback.print_exc()
            else:
                print("[-] client close connection ...")
                inputs.remove(event)
