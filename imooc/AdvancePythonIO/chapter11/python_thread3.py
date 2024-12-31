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


# 1.通过Thread类实例化 -- 代码量小可以这样使用，代码复杂的情况见方法2   这个是method 1的最终版
# method 1 适合建立线程池和动态建立线程或比较简单的

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
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    # 实际上这里还有第三个线程，主线程
    start_time = time.time()
    thread1.start()
    thread2.start()
    # 等这两句执行完后再来执行下面的逻辑，而不是3个线程并发运行

    # 等待线程执行完成才会执行最后那句  阻塞在这里  线程的运行时间是thread1和thread2中的最大时间，而不是相加，说明是并发
    thread1.join()
    thread2.join()

    # 当主线程退出的时候，子线程kill掉   因为thread1和thread2 setDaemon(True)
    print("last time:{}".format(time.time() - start_time))





