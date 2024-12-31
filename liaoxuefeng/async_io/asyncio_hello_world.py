#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-20 14:51'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090954004980bd351f2cd4cc18c9e6c06d855c498000

asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。

1.我们从asyncio模块中直接获取一个EventLoop的引用，
2.然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
"""

import asyncio

@asyncio.coroutine   # 把一个generator标记为coroutine类型，然后把这个coroutine扔到EventLoop中执行。
def hello():
    print("Hello world, asynico!")

    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

'''
把asyncio.sleep(1)看成是一个耗时1秒的IO操作，
在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
'''

# Get EventLoop
loop = asyncio.get_event_loop()

# Excute coroutine
loop.run_until_complete(hello())
loop.close()