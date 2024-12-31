# -*- coding:utf-8 -*-
import binascii
import struct
import time

current_timestamp = int(time.time())

hex_bytes = binascii.hexlify(struct.pack('I', current_timestamp))

hex_str = hex_bytes.decode().upper()

print(f"timestamp: {current_timestamp}, hex bytes: {hex_bytes} , hex string: {hex_str}")
