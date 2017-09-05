#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/5 17:22'


'''
P95-86
python网络爬虫实战--胡松涛

Python Logging模块
'''


import logging

print(logging.NOTSET)     # 0
print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)

logging.debug("debug message - 10")
logging.info("info message - 20")
logging.warning("warning message - 30")    # default level
logging.error("error message - 40")
logging.critical("critical message - 50")