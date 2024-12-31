#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-01-21 18:01'

import time

from celery_app import app

@app.task
def sendmail(mail="ttt@test.com"):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2)
    print('mail sent.')


def send_email():
    email_list = ["11@test.com", "22@test.com", "33@test.com", "44@ttest.com"]
    for email in email_list:
        result = sendmail.delay(email)
        print(result)