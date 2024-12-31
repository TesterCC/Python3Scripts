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


# 1.通过Thread类实例化 -- 代码量小可以这样使用，代码复杂的情况见方法2

# 2. 通过继承Thread来实现多线程 -- 适合代码复杂的情况   重载run方法  实际更推荐这种写法  Method2最终版
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)   # 多线程编程时要学会调用父类的编程方法

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(2)
        print("get detail url end")


# 通过这2个类的实例直接来实现多线程编程
if __name__ == '__main__':
    thread1 = GetDetailHtml("get_detail_html")    # name = get_detail_html
    thread2 = GetDetailUrl("get_detail_url")

    start_time = time.time()
    thread1.start()
    thread2.start()

    # 等待线程执行完成才会执行最后那句  阻塞在这里  线程的运行时间是thread1和thread2中的最大时间，而不是相加，说明是并发
    thread1.join()
    thread2.join()

    # 当主线程退出的时候，子线程kill掉   因为thread1和thread2 setDaemon(True)
    print("last time:{}".format(time.time() - start_time))




