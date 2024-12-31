#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-20 15:32'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00144661533005329786387b5684be385062a121e834ac7000

Python从3.5版本开始为asyncio提供了async和await的新语法，可以让coroutine的代码更简洁易读。

注意新语法只能用在Python 3.5以及后续版本，如果使用3.4版本，则仍需使用上一节的方案。 asyncio_XXX

请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：

1.把@asyncio.coroutine替换为async；
2.把yield from替换为await。
"""

import asyncio


# 参照：
# @asyncio.coroutine   # 把一个generator标记为coroutine类型，然后把这个coroutine扔到EventLoop中执行。
# def hello():
#     print("Hello world, asynico!")
#
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")

# 1.把@asyncio.coroutine替换为async；
async def hello():
    print("Hello, world, async/await!")
    r = await asyncio.sleep(1)    # 2.把yield from替换为await。
    print("Hello again!")


# Get EventLoop
loop = asyncio.get_event_loop()

# Excute coroutine
loop.run_until_complete(hello())
loop.close()

