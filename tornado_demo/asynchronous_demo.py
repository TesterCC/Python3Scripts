#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/13 00:08'

"""
bigdata35: Python 3.5.2 + tornado 5.1
http://www.tornadoweb.org/en/stable/guide/async.html

Tornado 6.0 will drop support for Python 2.7 and 3.4. 
The minimum supported Python version will be 3.5.2.
"""

# the same function rewritten asynchronously as a native coroutine

from tornado.httpclient import AsyncHTTPClient


# Python < 3.5 don't support async syntax and await syntax
async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body

if __name__ == '__main__':
    ret = asynchronous_fetch("http://xueshu.baidu.com")
    print(ret)  # sys:1: RuntimeWarning: coroutine 'asynchronous_fetch' was never awaited
