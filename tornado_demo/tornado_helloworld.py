#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/15 08:54'

"""
bigdata35: Python 3.5.2 + tornado 5.1
http://www.tornadoweb.org/en/stable/index.html
a simple “Hello, world” example web app for Tornado
"""

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world! -- GET method")

    def post(self):
        self.write("Hello, world! -- POST method")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)      # 127.0.0.1:8888
    tornado.ioloop.IOLoop.current().start()

