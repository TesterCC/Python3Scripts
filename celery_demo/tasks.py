#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 17:00'

"""
.../Python3Demo/celery_demo

在文件所在目录下，开启worker
celery -A tasks worker --loglevel=info

celery flower --broker=amqp://yanxi:yanxi@76543210@127.0.0.1:5672/vhost_hdj_email --basic_auth=yanxi:yanxi123456 --port=7777

write demo
"""
import time

from celery import Celery

# connect remote broker
# broker_url = 'amqp://username:passwd@remote_ip:remote_port/vhost_name'
# backend_url = 'redis://:passwd@127.0.0.1:6379/2'

# use local
broker_url = 'amqp://y:y@76543210@127.0.0.1:5672/vhost'
backend_url = 'redis://:y@127.0.0.1:6379/2'


app = Celery('tasks', broker=broker_url, backend=backend_url)

@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    result = add.delay(30, 42)
    print(result)

