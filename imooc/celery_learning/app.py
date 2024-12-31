#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/4 00:43'

"""
3-1 Celery基本使用
https://www.imooc.com/video/17953
"""

# # example 1
# from tasks import add    # 忽略，命令行和IDE都能正常执行
#
# if __name__ == '__main__':
#     print('Start task ...')
#     result = add.delay(2, 8)
#     print('End task ...')
#     print(result)
#
# # run in terminal command: celery worker -A tasks -l INFO


# example 2
from celery_app import task1
from celery_app import task2

task1.add.delay(2,4)
# task1.add.apply_async(2,4)  # 这种也可以，但这里有个坑 async在python3.6中是关键字，安装python3.5应该是正常的

task2.multiply.delay(4,5)

print('end app.py ...')


# run in terminal command: celery worker -A celery_app -l INFO
# cd ~/Python3Demo/imooc/celery_learning

# run in terminal command 2:
# cd ~/Python3Demo/imooc/celery_learning
# python app.py


# celery worker和celery beat在一条命令中启动
# run in terminal command 3:
# cd ~/Python3Demo/imooc/celery_learning
# celery -B -A celery_app worker -l INFO