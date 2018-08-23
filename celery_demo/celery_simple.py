#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 16:16'

from celery import Celery

broker_url = 'amqp://guest:guest@76543210@localhost//'
backend_url = 'redis://127.0.0.1:6379/0'

app = Celery('hello', broker=broker_url, backend=backend_url)
# print(dir(app))
# print(app.IS_macOS)
# print(app.SYSTEM)


@app.task
def hello(args='celery'):
    return 'hello world by {}'.format(args)


if __name__ == '__main__':
    result = hello('Lily')
    print(result)
