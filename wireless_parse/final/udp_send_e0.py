# -*- coding=utf-8 -*-
import binascii
import socket
import struct

BUFFER_SIZE = 1450

repeat_times = 5

positions = []

pos_inc = 0


# todo: test
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