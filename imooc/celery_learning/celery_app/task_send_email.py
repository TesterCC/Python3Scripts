#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-01-21 18:01'

import time

from celery_app import app

@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2)
    print('mail sent.')