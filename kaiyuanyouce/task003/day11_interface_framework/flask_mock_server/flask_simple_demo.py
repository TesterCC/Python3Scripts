#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 16:15'


from flask import Flask

app = Flask(__name__)


@app.route('/api')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()