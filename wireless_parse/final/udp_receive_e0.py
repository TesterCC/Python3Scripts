# -*- coding=utf-8 -*-
import binascii
import socket
import struct
import sys
import time

from Crypto.Cipher import AES

BUFFER_SIZE = 1450

# v7: same to v6, add ase   仅能勉强用，不能达标，要按照要求重构
# 最大问题是没有处理好UDP粘包问题
# d2: 基于加密版本和数据结构进行拼装


# def _unpad(data):
#     # decrypt use
#     padding_len = data[-1]
#     return data[:-padding_len]
#
#
# def aes_decrypt(key, encrypted_data):
#     aes = AES.new(key, AES.MODE_ECB)
#     decrypted_data = aes.decrypt(encrypted_data)
#     return _unpad(decrypted_data)