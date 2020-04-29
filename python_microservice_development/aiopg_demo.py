#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-28 12:50'

"""
P17
"""

import asyncio

import aiopg

dsn = 'dbname=aiopg user=aiopg password=passwd host=127.0.0.1'

# 添加少量async和await前缀，让执行SQL查询和返回结果的函数看起来接近于同步函数
async def go():
    pool = await aiopg.create_pool(dsn)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 1")
            ret = []
            async for row in cur:
                ret.append(row)
            assert ret == [(1,)]

loop = asyncio.get_event_loop()
loop.run_until_complete(go())