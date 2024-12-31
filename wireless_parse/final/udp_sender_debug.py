# -*- coding=utf-8 -*-
import binascii
import socket
import os
import struct
from os.path import basename
import sys
import time

BUFFER_SIZE = 1450

repeat_times = 5

positions = []

pos_inc = 0

poc_inc = 1
retry_inc = 1


def handle_send_content():
    # todo  file content also need cat
    pass


def handle_send_packet(poc_inc, retry_inc, content):
    #  4 + 4 + 2 + 1 + 1 + n

    global pos_inc

    # id_header
    encrypt_header_hex = "FEABFEAB"
    encrypt_header_bin = binascii.unhexlify(encrypt_header_hex)
    encrypt_header_data = struct.pack('!4s', encrypt_header_bin)  # 4 bytes

    # poc_inc += 1
    poc_inc_data = struct.pack('!i', poc_inc)  # 4 bytes

    len_data = struct.pack('!h', BUFFER_SIZE)  # 2 bytes

    retry_inc_data = struct.pack('!b', retry_inc)  # 1 bytes

    reserve_data = struct.pack('!b', 0)  # 1 bytes

    send_data = encrypt_header_data + poc_inc_data + len_data + retry_inc_data + reserve_data + content
    return send_data


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


def send_packet_demo(host, port, filename):
    fname1, fname2 = os.path.split(filename)  # fname1 -> path  , fname2 -> file_name

    client_addr = (host, port)

    print(f"[D] target info: {host}:{port}")

    # read file
    with open(filename, 'rb') as fp:
        content = fp.read()

    # key logic

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # step1: handle 1st udp data, filename
    # step2: handle 2ed udp data, file content
    # step3: send 1st data and 2ed data, duration 0.1s or 0.01s

    # todo no need to notice receive   # 对端收完0x01再收0x02即可
    send_content = handle_send_content(filename, content)
    send_data = handle_send_packet(poc_inc, retry_inc, send_content)
    sock.sendto(send_data, client_addr)

    sock.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        host = sys.argv[1]
        port = sys.argv[2]
        file_name = sys.argv[3]
    else:
        print("usage: python3 % ip port filename" % sys.argv[0])
        sys.exit(-1)

    # send_packet(host, int(port), file_name)
    send_packet_demo(host, int(port), file_name)
