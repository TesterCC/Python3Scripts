# coding=utf-8

# TCP client - non block, select

import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 不经过WAIT_TIME，直接关闭
sock.setblocking(False)  # 设置非阻塞

IP = '0.0.0.0'
PORT = 9999

try:
    sock.connect((IP, PORT))
except Exception as e:
    print(e)

r_inputs = set()
r_inputs.add(sock)
w_inputs = set()
w_inputs.add(sock)
e_inputs = set()
e_inputs.add(sock)

while True:
    try:
        # 读取列表，写入列表，错误列表
        r_list, w_list, e_list = select.select(r_inputs, w_inputs, e_inputs, 1)

        for event in r_list:  # 产生了可读事件，即服务端发送信息
            try:
                # data = event.recv(1024)
                data = event.recv(7)
            except Exception as e:
                print(e)

            if data and data[:5] == b"world" and data[-2:] == b"\r\n":
                print(f"[-] receive response: {data}")
                r_inputs.clear()
            else:
                print("[-] client close connection ...")
                r_inputs.clear()

        if len(w_list) > 0:  # 产生了可写的事件，即连接完成
            for event in w_list:
                try:
                    event.sendall(b"hello")
                    print("[+] send request ...")
                except Exception as e:
                    print(e)

            w_inputs.clear()  # 当连接完成之后，清除掉完成连接的socket

        if len(e_list) > 0:  # 产生了错误的事件，即连接错误
            print(e_list)
            e_inputs.clear()  # 当连接有错误发生时，清除掉发生错误的socket
    except OSError as e:
        print(e)
