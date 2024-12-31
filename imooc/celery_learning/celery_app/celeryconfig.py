#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/4 09:14'


from datetime import timedelta
from celery.schedules import crontab

# broker_url消息中间件
BROKER_URL = 'amqp://guest:guestpwd@localhost:port/vhost_name'   # with passwd, e.g. guestpwd is your password
# BROKER_URL = 'redis://127.0.0.1:6379/1'  # without passwd
# BROKER_URL = 'redis://:xxx@127.0.0.1:6379/1'   # with redis auth, e.g. xxx is your password

# backend_url主要用于存储任务执行结果
CELERY_RESULT_BACKEND = 'redis://:xxx@127.0.0.1:6379/4'
# localhost     redis-server /usr/local/redis-4.0.1/etc/redis.conf


CELERY_TIMEZONE = 'Asia/Shanghai'

# 忽略返回任务结果
CELERY_IGNORE_RESULT = False


# UTC

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
    'celery_app.task_send_email',
)

CELERYD_MAX_TASKS_PER_CHILD = 40


# 设置定时任务 task1 每10s执行一次， task2 每天17:30执行
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=7),
        'args': (2, 8)
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        # 'schedule': crontab(hour=17, minute=21),
        'schedule': timedelta(seconds=3),
        'args': (4, 5)
    },
    'task3': {
        'task': 'celery_app.task_send_email.send_email',
        # 'schedule': crontab(hour=17, minute=21),
        'schedule': timedelta(seconds=5),
    },
}

## Run in terminal: celery beat -A celery_app -l INFO
