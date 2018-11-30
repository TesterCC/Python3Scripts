#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/30 13:36'

import tornado.ioloop
import tornado.web

"""
http://www.tornadoweb.org/en/stable/

cd  ~/tornado_web
python hello_world.py
"""


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, Tornado</h1>")


class SecondHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, <h2>Tornado2</h2>")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/2ed", SecondHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
