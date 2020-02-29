#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-02-29 11:49'

from threading import Timer
import time


def func():

    ct = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    print(ct)

if __name__ == '__main__':

    timer = Timer(3, func)
    timer.start()