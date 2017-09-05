#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/5 22:39'


'''
P101
python网络爬虫实战--胡松涛

在程序中导入myLog.py作为模块,测试自定义日志模块 myLog
'''


from myLog import MyLog


if __name__ == '__main__':
    ml = MyLog()
    ml.debug("I'm debug.")
    ml.info("I'm info.")
    ml.warn("I'm warn.")
    ml.error("I'm error.")
    ml.critical("I'm critical.")
