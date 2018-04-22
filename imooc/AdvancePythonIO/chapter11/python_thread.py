#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/23 00:25'

"""
11-2 多线程编程 - threading
线程是操作系统能够切换也调度的最小单元
线程依赖于进程
"""

import time
import threading

def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    start_time = time.time()
    thread1.start()
    thread2.start()

    print("last time:{}".format(time.time() - start_time))
