#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-02-21 06:33'

"""
ref:
https://zhuanlan.zhihu.com/p/103711201

关于测试用的API，请求发送的 ts 字段日期距离今天大于10天，那么返回{"success": false}，如果小于等于10天，那么返回{"success": true}。

aiohttp 的代码与 httpx 异步模式的代码重合度90%，只不过把AsyncClient换成了ClientSession，另外，在使用 httpx 时，当你await client.post时就已经发送了请求。但是当使用aiohttp时，只有在awiat resp.json() 时才会真正发送请求。
"""

# 使用 aiohttp 发送异步请求, need python 3.7+

import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as client:
        resp = await client.post('http://122.51.39.219:8000/query',
                                 json={'ts': '2020-02-20 13:14:15'})
        result = await resp.json()
        print(result)


asyncio.run(main())
