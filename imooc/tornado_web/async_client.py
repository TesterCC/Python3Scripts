#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/3 01:31'

import time

import tornado.gen
import tornado.httpclient
import tornado.ioloop
from tornado import gen

"""
Tornado docs:
http://www.tornadoweb.org/en/stable/http.html
"""

N = 5

URL = 'http://localhost:8888/sleep'


@gen.coroutine
def main():
    http_client = tornado.httpclient.AsyncHTTPClient()
    responses = yield [
        http_client.fetch(URL) for i in range(N)
    ]

start1 = time.time()
tornado.ioloop.IOLoop.current().run_sync(main)
print("async", time.time() - start1)


# 同步请求的client demo
import requests
start = time.time()

for i in range(N):
    requests.get(URL)

print('notes.md', time.time()-start)

