#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-25 14:51'

"""
9-6 生成器如何读取大文件

如何读取一个500G大小且仅有一行的文件。

备注：这样的话直接读取所有内容到内存是不可行的。
"""

def myreadlines(f, newline):
    buf = ""   # 可以视为缓存，存储已经读出的数据
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]   # 把已经yield的数据丢弃掉
        chunk = f.read(4096)  # 一次性读取的数据量

        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk  # 已经读到就会压到缓存buffer中

with open('input.txt') as f:
    for line in myreadlines(f, "{|}"):
        print(line)