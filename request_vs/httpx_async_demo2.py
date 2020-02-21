#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-02-21 06:33'

"""
ref:
https://zhuanlan.zhihu.com/p/103711201

关于测试用的API，请求发送的 ts 字段日期距离今天大于10天，那么返回{"success": false}，如果小于等于10天，那么返回{"success": true}。
"""

# 使用 httpx 发送异步请求, need python 3.7+

import httpx
import asyncio


async def main():
    async with httpx.AsyncClient() as client:
        resp = await client.post('http://122.51.39.219:8000/query',
                                 json={'ts': '2020-02-20 13:14:15'})
        result = resp.json()
        print(result)


asyncio.run(main())
