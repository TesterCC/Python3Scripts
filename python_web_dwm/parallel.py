#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/4 13:29'


"""
Python Web开发实战 绿色
P686 使用MapReduce
使用multiprocessing实现并发计算的例子
Python3
"""

import os
import time
import multiprocessing


def task(args):
    time.sleep(1)
    pid = os.getpid()   # with some issue
    return pid, args


if __name__ == '__main__':

    start = time.time()
    pool = multiprocessing.Pool(processes=4)
    result = pool.map(task, range(10))
    print(result)
    print("Cost:{}".format(time.time() - start))

