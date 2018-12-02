#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/30 13:36'

import os
import datetime

import tornado.ioloop
import tornado.web

"""
http://www.tornadoweb.org/en/stable/

cd  ~/tornado_web
python hello_world.py
"""


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("<h1>Hello, Tornado</h1>")
        self.render("base.html")


class SecondHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, <h2>Tornado2</h2>")


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        # self.render("500.html", msg=datetime.date.today())
        self.render("500.html", msg=datetime.datetime.now())


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/2ed", SecondHandler),
        (r"/500", ErrorHandler),
    ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
