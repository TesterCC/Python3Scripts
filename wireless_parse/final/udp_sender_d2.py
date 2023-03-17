# -*- coding=utf-8 -*-
import binascii
import socket
import os
import struct
from os.path import basename
import sys
import time

from Crypto.Cipher import AES

BUFFER_SIZE = 1450

repeat_times = 5

positions = []

pos_inc = 0

# v7: same to v6, add ase 仅能勉强用，不能达标，要按照要求重构
# 最大问题是没有处理好UDP粘包问题
# d2: 基于加密版本和数据结构进行拼装
# ref: https://blog.csdn.net/weixin_58439331/article/details/127119632

# PS：未加密，仅测试封包解包是否正常

def _pad(data):
    # encrypt use
    padding_len = AES.block_size - (len(data) % AES.block_size)
    padding = chr(padding_len) * padding_len
    padded_data = data + padding.encode('utf-8')
    return padded_data


def aes_encrypt(key, data):
    aes = AES.new(key, AES.MODE_ECB)
    padded_data = _pad(data)
    encrypted_data = aes.encrypt(padded_data)
    return encrypted_data


# todo: refactor
def handle_send_packet(content, poc_inc, retry_inc):
    #  4 + 4 + 2 + 1 + 1 + n

    global pos_inc

    # id_header
    encrypt_header_hex = "FEABFEAB"
    encrypt_header_bin = binascii.unhexlify(encrypt_header_hex)
    encrypt_header_data = struct.pack('!4s', encrypt_header_bin)  # 4 bytes

    # poc_inc += 1
    poc_inc_data = struct.pack('!i', poc_inc)   # 4 bytes

    len_data = struct.pack('!h', BUFFER_SIZE)  # 2 bytes

    retry_inc_data = struct.pack('!b', retry_inc)   # 1 bytes

    reserve_data = struct.pack('!b', 0)   # 1 bytes

    send_data = encrypt_header_data + poc_inc_data + len_data + retry_inc_data + reserve_data + content
    return send_data


    # # 将二进制字符串转换为网络数据（大端序）
    # network_data = struct.pack('!I', int.from_bytes(encrypt_header, byteorder='big'))\
    # # 打印网络数据的二进制表示
    # print(binascii.hexlify(network_data))




def send_packet(host, port, filename, key):
    fname1, fname2 = os.path.split(filename)  # fname1 -> path  , fname2 -> file_name

    client_addr = (host, port)

    print(f"[D] target info: {host}:{port}")

    # read file
    with open(filename, 'rb') as fp:
        content = fp.read()

    # get the file size and prepare for chunked transfer
    fn_size = len(content)
    for start in range(fn_size // BUFFER_SIZE + 1):
        positions.append(start * BUFFER_SIZE)

    print(f"[D] {positions}")   # position = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



    # todo need to update，
    # send file according to positions list
    while positions:
        for pos in positions:
            # retransmit default retry 5 times, prevent packet loss

            for i in range(repeat_times):
                sdata = f"{pos}_".encode() + content[pos:pos + BUFFER_SIZE]
                encrypted_data = aes_encrypt(key, sdata)
                sock.sendto(encrypted_data, client_addr)
            positions.remove(pos)
            print(f"[D] del {pos}, current position {positions}")
        time.sleep(0.1)

    # notice send finish
    file_name = [f'{basename(fname2)}'.encode()]

    # 新方案应该不需要再发送over包了，全程应该只需要发送一个包
    sdata = b'over_' + file_name[0]
    encrypted_data = aes_encrypt(key, sdata)
    sock.sendto(encrypted_data, client_addr)
    sock.close()


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
