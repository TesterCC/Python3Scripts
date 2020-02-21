#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-02-21 22:22'

"""
ref:
https://zhuanlan.zhihu.com/p/103711201

关于测试用的API，请求发送的 ts 字段日期距离今天大于10天，那么返回{"success": false}，如果小于等于10天，那么返回{"success": true}。

先上结论：

如果你只发几条请求。那么使用 requests 或者 httpx 的同步模式，代码最简单。

如果你要发送很多请求，但是有些地方要发送同步请求，有些地方要发送异步请求，那么使用 httpx 最省事。

如果你要发送很多请求，并且越快越好，那么使用 aiohttp 最快。


aiohttp 的内存占用要比 httpx 低，因为aiohttp 有一部分 C 语言实现的代码。httpx 全部用的 Python。
"""

"""发送100次请求
现在随机生成一个距离今天在5-15天的日期，发送到 HTTP接口中。如果日期距离今天超过10天，那么返回的数据的 False，如果小于等于10天，那么返回的数据是 True。

发送100次请求，计算总共耗时。


使用requests.post每次都会创建新的连接，速度较慢。而如果首先初始化一个 Session，那么 requests 会保持连接，从而大大提高请求速度。
所以在这次测评中，我们分别对两种情况进行测试。
"""

import aiohttp
import random
import datetime
import asyncio
import time


async def request(client, body):
    resp = await client.post('http://122.51.39.219:8000/query', json=body)
    result = await resp.json()
    print(result)


async def main():
    async with aiohttp.ClientSession() as client:
        start = time.time()
        task_list = []
        for _ in range(100):
            now = datetime.datetime.now()
            delta = random.randint(5, 15)
            ts = (now - datetime.timedelta(days=delta)).strftime('%Y-%m-%d %H:%M:%S')
            req = request(client, {'ts': ts})
            task = asyncio.create_task(req)
            task_list.append(task)
        await asyncio.gather(*task_list)
        end = time.time()
    print(f'发送100次请求，耗时：{end - start}')

asyncio.run(main())   # 1.1405057907104492