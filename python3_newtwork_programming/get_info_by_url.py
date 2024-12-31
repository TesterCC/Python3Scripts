#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-25 17:15'

"""
用python提取url链接中的域名与端口
"""
from urllib import parse


def get_info_by_url(url):
    protocol, rest = parse.splittype(url)
    host, path = parse.splithost(rest)
    host, port = parse.splitport(host)
    if port is None:
        port = '80'
    return protocol, host, path, port


if __name__ == '__main__':
    url = "https://www.postgresql.org/docs/9.6/index.html"
    url2 = "https://www.postgresql.org:8000/docs/9.6/index.html"
    print(get_info_by_url(url))
    print(get_info_by_url(url2))
