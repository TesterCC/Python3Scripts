#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-25 11:49'

"""
https://docs.python.org/zh-cn/3.7/library/asyncio.html
asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。
asyncio 往往是构建 IO 密集型和高层级 结构化 网络代码的最佳选择。

用asyncio开发需要注意的地方：
https://docs.python.org/zh-cn/3.7/library/asyncio-dev.html

workon py371
"""

import asyncio

async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())