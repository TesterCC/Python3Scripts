# coding=utf-8

"""
5.9 读取二进制数据到可变缓冲区中 todo
"""

import os


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, "rb") as f:
        f.readinto(buf)
    return buf


if __name__ == '__main__':
    with open("sample.bin", 'wb') as f:
        # write info in
        f.write(b"Hello Bin World")

    buf = read_into_buffer("sample.bin")

    print(buf[0:5])
    print(buf[0:15])

    with open("sample2.bin", "wb") as f:
        f.write(buf)
