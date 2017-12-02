#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/2 22:35'


"""
Python网络爬虫--从入门到实践   P36 3.3.4 timeout
Crawler Target: http://train.fullstackpentest.com
"""

import requests

link = 'http://train.fullstackpentest.com'
r = requests.get(link, timeout=0.01)
