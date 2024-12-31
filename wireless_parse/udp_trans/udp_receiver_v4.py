# -*- coding=utf-8 -*-
import socket
import sys
import threading
import time


# https://blog.csdn.net/qq_40177015/article/details/112402889


def receiver(address, port):
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (address, port)
    s.bind(server_addr)

    print(f'[D] Bind UDP at {address}:{port}')

    received_size = 0
    while True:
        if count == 0:
            data, client_addr = s.recvfrom(4096)
            print('connected from %s:%s' % client_addr)
            # Record the start time of the receiver running
            start = time.time()
            f = open(data, 'wb')
        data, client_addr = s.recvfrom(4096)
        if str(data) != "b'end'":
            received_size += len(data)
            f.write(data)
            # Record the current system time
            end = time.time()
            # Print the current time every 1s
            # while printing the cumulative amount of transmission
            if end - start > 1:
                print(end)
                print('Accept ', received_size, ' B')
                start = time.time()
        else:
            break
        s.sendto('ok'.encode('utf-8'), client_addr)
        count += 1
        print('[D] total received ', received_size, ' B')
        f.close()
    s.close()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        address = sys.argv[1]
        port = sys.argv[2]
    else:
        print("usage: python3 % ip port" % sys.argv[0])
        sys.exit(-1)

    receiver(address, int(port))
