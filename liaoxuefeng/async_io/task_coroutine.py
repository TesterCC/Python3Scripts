#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-20 15:05'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090954004980bd351f2cd4cc18c9e6c06d855c498000

asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。

1.我们从asyncio模块中直接获取一个EventLoop的引用，
2.然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
"""

# 用Task封装两个coroutine
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()

tasks = [hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
'''