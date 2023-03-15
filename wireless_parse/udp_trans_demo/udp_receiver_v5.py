# -*- coding=utf-8 -*-
import socket
import sys
import threading
import time
from Crypto.Cipher import AES

# v5: support AES Cipher

def _unpad(data):
    # decrypt use
    padding_len = data[-1]
    return data[:-padding_len]


def aes_decrypt(key, encrypted_data):
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_data = aes.decrypt(encrypted_data)
    return _unpad(decrypted_data)


def receiver(host, port):
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (host, port)
    s.bind(server_addr)

    print(f'[D] Bind UDP at {host}:{port}')

    received_size = 0
    while True:
        if count == 0:
            data, client_addr = s.recvfrom(4096)
            print('connected from %s:%s' % client_addr)
            data = aes_decrypt(key, data)
            # Record the start time of the receiver running
            start = time.time()
            f = open(data, 'wb')
        data, client_addr = s.recvfrom(4096)
        data = aes_decrypt(key, data)
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
        host = sys.argv[1]
        port = sys.argv[2]
        key = bytes("wirelesspost2023", encoding="utf-8")
    else:
        print("usage: python3 % ip port" % sys.argv[0])
        sys.exit(-1)

    receiver(host, int(port))
