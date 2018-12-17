#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/4 09:14'

from celery import Celery

app = Celery('demo')

# 通过Celery实例加载配置模块
app.config_from_object('celery_app.celeryconfig')

