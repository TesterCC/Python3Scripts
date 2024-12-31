# -*- coding=utf-8 -*-
import socket
import threading
import time


# https://blog.csdn.net/qq_40177015/article/details/112402889


def recvived(address, port):
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (address, port)
    s.bind(server_addr)

    print('Bind UDP....')

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
        print('total received ', received_size, ' B')
        f.close()
    # s.close()


if __name__ == '__main__':
    # address = ("127.0.0.1", 1234)
    port = 9999
    address = "192.168.100.3"
    t = threading.Thread(target=recvived, args=(address, port))
    t.start()
    # send(address)
