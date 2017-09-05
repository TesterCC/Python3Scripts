#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/5 21:51'


'''
P99
python网络爬虫实战--胡松涛

自定义日志模块 myLog
'''


import logging
import getpass
import sys


# define MyLog Class
class MyLog(object):
    '''这个类用于创建一个自用的log'''
    def __init__(self):      # class MyLog的构造函数
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        # logFile = './' + sys.argv[0][0:-3] + '.log'   # log file name
        logFile = sys.argv[0][0:-3] + '.log'   # log file name

        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

        '''日志显示到屏幕上并输出到日志文件内'''
        logHand = logging.FileHandler(logFile)
        logHand.setFormatter(formatter)
        logHand.setLevel(logging.ERROR)    # 只有错误才会被记录到logfile中

        logHandSt = logging.StreamHandler()
        logHandSt.setFormatter(formatter)

        self.logger.addHandler(logHand)
        self.logger.addHandler(logHandSt)

        '''日志的5个级别对应以下的5个函数'''
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    myLog = MyLog()
    myLog.debug("I'm debug.")
    myLog.info("I'm info.")
    myLog.warn("I'm warn.")
    myLog.error("I'm error.")
    myLog.critical("I'm critical.")