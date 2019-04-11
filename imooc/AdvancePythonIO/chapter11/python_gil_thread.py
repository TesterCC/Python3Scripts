#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/22 23:51'

"""
11-1 python 中的 GIL  07:47
gil 会根据执行的字节码行数以及时间片释放gil，gil在遇到IO的操作时会主动释放
使得Python多线程在IO操作频繁的情况下也很适用
"""

import threading

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)    # total每次都不一样，说明GIL会释放的，py2和py3中会有不同

