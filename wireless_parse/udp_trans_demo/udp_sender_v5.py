# -*- coding=utf-8 -*-
import socket
import os
import sys
import time

from Crypto.Cipher import AES


# https://blog.csdn.net/qq_40177015/article/details/112402889
# v5: support AES Cipher


def _pad(data):
    # encrypt use
    padding_len = AES.block_size - (len(data) % AES.block_size)
    padding = chr(padding_len) * padding_len
    padded_data = data + padding.encode('utf-8')
    return padded_data


# AES encrypt
def aes_encrypt(key, data):
    aes = AES.new(key, AES.MODE_ECB)
    padded_data = _pad(data)
    encrypted_data = aes.encrypt(padded_data)
    return encrypted_data


def send_packet(host, port, filename, key):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # filename = input('please enter the filename you want to send:\n')
    filesize = str(os.path.getsize(filename))
    fname1, fname2 = os.path.split(filename)

    client_addr = (host, port)

    print(f"[D]target info, {host}:{port}")

    f = open(filename, 'rb')
    count = 0
    # flag = 1
    while True:
        if count == 0:

            data = bytes(fname2, encoding="utf8")
            edata = aes_encrypt(key, data)
            # The start time of the sending end is recorded,
            # which is used to calculate the total running time and 1s respectively
            total_start = time.time()
            current_start = time.time()
            s.sendto(edata, client_addr)
        data = f.read(4096)   # file data
        if str(data) != "b''":
            edata = aes_encrypt(key, data)
            s.sendto(edata, client_addr)
        else:
            data = 'end'
            edata = aes_encrypt(key, data.encode('utf-8'))
            s.sendto(edata, client_addr)
            break
        current_end = time.time()
        # Print the timestamp of the sending end for every 1s
        if current_end - current_start > 1:
            print(current_end)
            current_start = time.time()
        data, server_addr = s.recvfrom(4096)
        count += 1

    s.close()
    total_end = time.time()
    print('total cost: ' + str(round(total_end - total_start, 6)) + 's')


if __name__ == '__main__':
    if len(sys.argv) == 4:
        host = sys.argv[1]
        port = sys.argv[2]
        file_name = sys.argv[3]
        key = bytes("wirelesspost2023", encoding="utf-8")

    else:
        print("usage: python3 % ip port filename" % sys.argv[0])
        sys.exit(-1)

    send_packet(host, int(port), file_name, key)
