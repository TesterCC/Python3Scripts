#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-09 23:45'

"""
非原子操作不是线程安全的
可以通过加锁保证线程安全
如何保证线程安全：给线程加锁 (会对程序性能有一定影响)

cProfile用法：
cd ~/pw_python/imooc
python -m cProfile -o test_thread.out thread_safe.py    # 分析结果在test_thread.out
python -c "import pstats; p=pstats.Stats('test_thread.out'); p.print_stats()"   # 展示分析结果
python -c "import pstats; p=pstats.Stats('test_thread.out'); p.sort_stats('time').print_stats()"  # 查看排序后的运行结果
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

# 没加线程锁的话，在一定环境下应该会有9998的情况出现，这个其实是线程不安全的