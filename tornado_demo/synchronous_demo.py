#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/13 00:01'

"""
bigdata35: Python 3.5.2 + tornado 5.1
http://www.tornadoweb.org/en/stable/guide/async.html

Tornado 6.0 will drop support for Python 2.7 and 3.4. 
The minimum supported Python version will be 3.5.2.
"""

from tornado.httpclient import HTTPClient


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


if __name__ == '__main__':
    ret = synchronous_fetch("http://xueshu.baidu.com")     # attention url format
    print(ret)

