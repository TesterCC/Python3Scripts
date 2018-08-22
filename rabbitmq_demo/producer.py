#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/22 17:16'

"""
https://www.cnblogs.com/alex3714/articles/5248247.html
"""

import pika


credentials = pika.PlainCredentials('guest', 'guest@76543210')

# 建立socket连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
)

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # when no set password

# 声明一个管道
channel = connection.channel()

# 声明queue（队列）
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',   # queue name
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()
