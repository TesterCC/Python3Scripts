#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-01-29 23:01'

"""
https://docs.sentry.io/server/installation/docker/

https://docs.sentry.io/error-reporting/quickstart/?platform=python#pick-a-client-integration

Integrated with Python

pip install raven --upgrade

Install an SDK

pip install --upgrade sentry-sdk

"""

from raven import Client

DSN = ""   # find it on your sentry

client = Client(DSN)

try:
    1/0
except ZeroDivisionError:
    client.captureException()
