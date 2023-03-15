# -*- coding=utf-8 -*-
import socket
import os
from os.path import basename
import sys
import time

BUFFER_SIZE = 4 * 1024

ALL_BUFFER_SIZE = 100*1024

repeat_times = 3

positions = []


# https://blog.csdn.net/qq_40177015/article/details/112402889

def send_packet(host, port, filename):
    fname1, fname2 = os.path.split(filename)  # fname1 -> path  , fname2 -> file_name

    client_addr = (host, port)

    print(f"[D] target info: {host}:{port}")

    # read file
    with open(filename, 'rb') as fp:
        content = fp.read()

    # 获取文件大小，做好分块传输的准备
    fn_size = len(content)
    for start in range(fn_size // BUFFER_SIZE + 1):
        positions.append(start * BUFFER_SIZE)

    print(f"[O] {positions}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送文件数据，直到所有分块都收到确认，否则就不停地循环发送
    while positions:
        for pos in positions:
            # 默认重传3次，以防丢包
            for i in range(repeat_times):
                sock.sendto(f"{pos}_".encode() + content[pos:pos + BUFFER_SIZE], client_addr)
            positions.remove(pos)
            print(f"[D] del {pos}, current position {positions}")
        time.sleep(0.1)

    # notice send finish
    file_name = [f'{basename(fname2)}'.encode()]

    sock.sendto(b'over_' + file_name[0], client_addr)
    sock.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        host = sys.argv[1]
        port = sys.argv[2]
        file_name = sys.argv[3]
    else:
        print("usage: python3 % ip port filename" % sys.argv[0])
        sys.exit(-1)

    send_packet(host, int(port), file_name)
