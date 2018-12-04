#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/4 00:54'


import time
from celery import Celery

# broker_url消息中间件
broker = 'amqp://guest:guest@76543210@localhost'
# broker = 'redis://127.0.0.1:6379/1'

# backend_url主要用于存储任务执行结果
backend = 'redis://127.0.0.1:6379/2'

app = Celery("my_task", broker=broker, backend=backend)

@app.task
def add(x, y):
    print("enter call func...")
    time.sleep(3)
    return x + y