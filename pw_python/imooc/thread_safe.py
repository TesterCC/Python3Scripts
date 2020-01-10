#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-09 23:45'

"""
非原子操作不是线程安全的
可以通过加锁保证线程安全

3-5 08：44
如何保证线程安全：给线程加锁
"""

import threading

lock = threading.Lock()


n = [0]

def foo():

    with lock:   # 这样就线程加锁了
        # n[0] = n[0]+1
        # n[0] = n[0]+1
        n[0] += 1   # 一样的，无差别
        n[0] += 1

threads = []

for i in range(5000):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

print(n)

# 在一定环境下应该会有9998的情况出现，这个其实是线程不安全的