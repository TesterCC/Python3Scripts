#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/29 11:07'

"""
test concurrency by python script
no response
"""

import threading
import requests

host = '127.0.0.1'


class TestLaunch(threading.Thread):
    def run(self):
        resp = requests.get(f"http://{host}:7703/admin/", timeout=5)
        print(resp.status_code)


if __name__ == '__main__':
    # 启动多线程运行有bug
    # threads = [TestLaunch() for i in range(10)]
    # map(lambda t: t.start(), threads)
    thread = TestLaunch()
    thread.start()
