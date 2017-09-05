#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/5 17:35'

'''
P98
python网络爬虫实战--胡松涛

利用logging.basicConfig写个最基本的日志模块应用程序
'''

import logging


class TestLogging(object):
    def __init__(self):
        logFormat = '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s'
        logFileName = './testLog.txt'

        logging.basicConfig(level=logging.INFO,
                            format=logFormat,
                            filename=logFileName,
                            filemode='w')     # default level is INFO

        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warning message')
        logging.error('error message')
        logging.critical('critical message')


if __name__ == '__main__':
    tl = TestLogging()
