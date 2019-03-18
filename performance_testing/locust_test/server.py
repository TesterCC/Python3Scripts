#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-19 01:15'


"""
https://www.bilibili.com/video/av33363078
"""

import random

import tornado.ioloop
import tornado.web

from tornado import gen

from tornado.web import RequestHandler

class AsyncSleepHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random())
        self.write('sleep')

class Aysnc2SleepHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random()/10.0*2)
        self.write('sleep2')


if __name__ == '__main__':
    application = tornado.web.Application([
        (r"/sleep", AsyncSleepHandler),
        (r"/sleep2", Aysnc2SleepHandler),
    ], debug=1)
    application.listen(8888)

    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
