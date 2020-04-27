#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-27 15:12'

"""
http://aiohttp.readthedocs.io
实现完全异步微服务
"""

from aiohttp import web
import time

async def handle(request):  # 指明handle是协程的
    return web.json_response({'time': time.time()})

if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/',handle)
    web.run_app(app)