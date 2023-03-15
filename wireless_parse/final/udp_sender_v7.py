# -*- coding=utf-8 -*-
import socket
import os
from os.path import basename
import sys
import time

from Crypto.Cipher import AES

BUFFER_SIZE = 1400

repeat_times = 5

positions = []


# v7: same to v6, add ase 仅能勉强用，不能达标，要按照要求重构
# 最大问题是没有处理好UDP粘包问题

def _unpad(data):
    # decrypt use
    padding_len = data[-1]
    return data[:-padding_len]


def _pad(data):
    # encrypt use
    padding_len = AES.block_size - (len(data) % AES.block_size)
    padding = chr(padding_len) * padding_len
    padded_data = data + padding.encode('utf-8')
    return padded_data


# 定义AES加密和解密的函数
def aes_encrypt(key, data):
    aes = AES.new(key, AES.MODE_ECB)
    padded_data = _pad(data)
    encrypted_data = aes.encrypt(padded_data)
    return encrypted_data


def aes_decrypt(key, encrypted_data):
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_data = aes.decrypt(encrypted_data)
    return _unpad(decrypted_data)


def send_packet(host, port, filename, key):
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
                sdata = f"{pos}_".encode() + content[pos:pos + BUFFER_SIZE]
                encrypted_data = aes_encrypt(key, sdata)
                sock.sendto(encrypted_data, client_addr)
            positions.remove(pos)
            print(f"[D] del {pos}, current position {positions}")
        time.sleep(0.1)

    # notice send finish
    file_name = [f'{basename(fname2)}'.encode()]

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
