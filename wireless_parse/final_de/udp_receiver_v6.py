# -*- coding=utf-8 -*-
import socket
import sys
import time

BUFFER_SIZE = 512


def receiver(host, port):
    # 重复收包次数
    repeat = 0
    # 用来临时保存的数据
    data = set()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (host, port)
    s.bind(server_addr)

    print(f'[D] Bind UDP at {host}:{port}')
    while True:
        buffer, ack_addr = s.recvfrom(BUFFER_SIZE)
        # print(f"[D] ack_addr: {ack_addr}")

        # 全部接收完成，获取文件名
        if buffer.startswith(b'over_'):
            fn = buffer[5:].decode()  # filename

            break

        # 接收带编号的文件数据，临时保存
        buffer = tuple(buffer.split(b'_', maxsplit=1))
        print("tuple buffer", buffer)
        if buffer in data:
            repeat = repeat + 1
        else:
            data.add(buffer)
            # print(f"[tmp data]\n", data)

    print(f'重复接收数据{repeat}次')

    data = sorted(data, key=lambda item: int(item[0]))
    # with open(rf'{dst}/{fn}', 'wb') as fp:
    with open(rf'{fn}', 'wb') as fp:
        for item in data:
            fp.write(item[1])

    s.close()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = sys.argv[2]
    else:
        print("usage: python3 % ip port" % sys.argv[0])
        sys.exit(-1)

    receiver(host, int(port))
