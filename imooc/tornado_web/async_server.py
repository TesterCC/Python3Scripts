#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/3 00:54'

import time
import datetime

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web

"""
3-2 Tornado异步服务器和客户端模块 
https://www.imooc.com/video/18302

Tornado docs:
http://www.tornadoweb.org/en/stable/http.html
"""


class SleepHandler(tornado.web.RequestHandler):
    # 同步的sleep demo, 会等待第一个请求完成后再处理后面的请求
    def get(self):
        time.sleep(5)
        # self.write("when I sleep")
        self.write(str(datetime.datetime.now()))

    # 异步的sleep demo，几乎可以同时处理，可以使每个请求之间不会互相干扰
    @tornado.gen.coroutine
    def get(self):
        # time.sleep(5)
        yield tornado.gen.sleep(2.5)
        self.write(str(datetime.datetime.now()))


if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r"/sleep", SleepHandler)
        ],
        debug=True,
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    print("Start server...")
    tornado.ioloop.IOLoop.instance().start()
