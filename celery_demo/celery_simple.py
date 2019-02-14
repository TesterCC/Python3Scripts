#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 16:16'

# right demo
# celery -A celery_simple worker --loglevel=info

from celery import Celery

broker_url = 'amqp://yanxi:yanxi@76543210@127.0.0.1:5672/vhost_hdj_email'
backend_url = 'redis://:HereWithYou@127.0.0.1:6379/2'

app = Celery('celery_simple', broker=broker_url, backend=backend_url)
# print(dir(app))
# print(app.IS_macOS)
# print(app.SYSTEM)


@app.task
def hello(args='celery'):
    return 'hello world by {}'.format(args)


if __name__ == '__main__':
    list = ["test1","test2","test3"]
    for arg in list:
        result = hello.delay(args=arg)
        print(result)
