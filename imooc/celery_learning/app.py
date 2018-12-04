#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/4 00:43'

"""
3-1 Celery基本使用
https://www.imooc.com/video/17953
"""


from tasks import add    # 忽略，命令行和IDE都能正常执行

if __name__ == '__main__':
    print('Start task ...')
    result = add.delay(2, 8)
    print('End task ...')
    print(result)
