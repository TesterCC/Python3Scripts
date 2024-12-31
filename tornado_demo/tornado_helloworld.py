#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/15 08:54'

"""
bigdata35: Python 3.5.2 + tornado 5.1
http://www.tornadoweb.org/en/stable/index.html
a simple “Hello, world” example web app for Tornado

部分参考红书 P241
"""

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world! -- GET method")

    def post(self):
        self.write("Hello, world! -- POST method")


class EntryHandler(tornado.web.RequestHandler):
    def get(self, slug):
        # entry = self.db.get("")
        entry = slug

        if not entry:
            raise tornado.web.HTTPError(404)

        self.render("entry.html", entry=entry)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),     # 固定字串路径
        (r"/entry/([^/]+)", EntryHandler)    # 参数字符串, 匹配以/entry/开头的URL模式
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)      # 127.0.0.1:8888
    tornado.ioloop.IOLoop.current().start()

# http://127.0.0.1:8888/
# http://127.0.0.1:8888/entry/English