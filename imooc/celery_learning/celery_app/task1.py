#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/4 09:14'

import time

from celery_app import app

@app.task
def add(x,y):
    time.sleep(3)
    return x+y

