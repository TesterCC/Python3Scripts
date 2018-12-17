#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/4 09:14'


from datetime import timedelta
from celery.schedules import crontab

# broker_url消息中间件
# BROKER_URL = 'amqp://guest:guest@76543210@localhost'   # with passwd
# BROKER_URL = 'redis://127.0.0.1:6379/1'  without passwd
# with redis auth
# redis://:xxx@127.0.0.1:6379/2     xxx is your passwd
BROKER_URL = 'redis://:HereWithYou@127.0.0.1:6379/1'

# backend_url主要用于存储任务执行结果
CELERY_RESULT_BACKEND = 'redis://:HereWithYou@127.0.0.1:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

# UTC

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

# 设置定时任务 task1 每10s执行一次， task2 每天17:30执行
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=17, minute=21),
        'args': (4, 5)
    },
}

## Run in terminal: celery beat -A celery_app -l INFO