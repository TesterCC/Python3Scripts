#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 11:10'

"""
用asyncio开发需要注意的地方：
https://docs.python.org/zh-cn/3.7/library/asyncio-dev.html

workon py371
python asyncio_dev.py
python -X dev asyncio_dev.py

当协程函数被调用而不是被等待时 (即执行 coro() 而不是 await coro()) 或者协程没有通过 asyncio.create_task() 被排入计划日程，asyncio 将会发出一条 RuntimeWarning

"""

import asyncio
import logging;logging.basicConfig(level=logging.DEBUG)

logging.getLogger("asyncio").setLevel(logging.WARNING)   # set log

async def test():
    print("never scheduled")

async def main():
    #test()   # warning
    await test()

# asyncio.run(main())
asyncio.run(main(), debug=True)   # activate debug mode