#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-25 17:02'

"""
A Demo of Monkey Patch
所谓monkey patch就是运行时属性替换
"""

import socket

print(socket.socket)

print("After monkey patch")

from gevent import monkey

monkey.patch_socket()
print(socket.socket)

print("-" * 60)

import select

print(select.select)
print("After monkey patch")
monkey.patch_select()
print(select.select)

print("-" * 60)

# self write monkey_patch
import time

print(time.time())


def _time():
    return 1234567


print("After monkey patch")
time.time = _time

print(time.time())
