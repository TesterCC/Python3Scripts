#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/23 00:25'

"""
11-2 多线程编程 - threading
线程是操作系统能够切换和调度的最小单元
线程依赖于进程

对于io操作来说，多线程和多进程性能差别不大（甚至多线程比多进程性能还高）。
对操作系统来说，线程的调度比进程的调度更轻量级  
"""

import time
import threading


# 1.通过Thread类实例化
def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))

    # setDaemon将thread1和thread2设置为守护进程
    thread1.setDaemon(True)
    thread2.setDaemon(True)

    # 实际上这里还有第三个线程，主线程
    start_time = time.time()
    thread1.start()
    thread2.start()

    # 当主线程退出的时候，子线程kill掉   因为thread1和thread2 setDaemon(True)
    print("last time:{}".format(time.time() - start_time))
