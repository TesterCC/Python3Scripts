#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/29 14:06'

"""
Effective Python编写高质量Python代码的59个有效方法  P6
Python3  bytes(包含原始8位，等价Python2的str)    -- 原始8位:由于每个字节有8个二进制位，故是原始的8位
Python3  str(包含Unicode字符)

Python3
bytes.decode('utf-8')  -> str
str.encode('utf-8')   -> bytes

Python编程：编解码放在界面最外围来做，程序核心部分应该使用Unicode字符类型，且不要对字符编码做任何假设。
"""


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value  # Instance of str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str

    return value  # Instance of bytes


if __name__ == '__main__':
    print('str to bytes:')
    text1 = '编程'
    print(type(text1))
    text1u = to_bytes(text1)
    print(type(text1u))
    print(text1u)     # bytes

    print('bytes to str:')
    text2 = b'\xe7\xbc\x96\xe7\xa8\x8b'
    print(type(text2))
    text2u = to_str(text2)
    print(type(text2u))
    print(text2u)     # str

