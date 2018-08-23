#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 17:00'

"""
.../Python3Demo/celery_demo

在文件所在目录下，开启worker
celery -A tasks worker --loglevel=info
"""

from celery import Celery

broker_url = 'amqp://guest:guest@76543210@localhost//'
backend_url = 'redis://127.0.0.1:6379/0'

app = Celery('tasks', broker=broker_url, backend=backend_url)

@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    result = add.delay(30, 42)
