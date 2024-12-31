#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 02:08'

import pika

# credentials = pika.PlainCredentials('guest', 'guest@76543210')
credentials = pika.PlainCredentials('tester', 'Tester_2020')

# 建立socket连接
# 1.连接rabbitmq服务器
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
)

channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
# 2.声明一个名为hello的队列
channel.queue_declare(queue='hello')

# 3.构建回调函数
def callback(ch, method, properties, body):
    print("[>>>>]", ch, method, properties)
    print(" [x] Received %r" % body)


# 消费消息
# 4.确定监听队列queue:hello,一旦有值出现，就触发回调函数：callback
channel.basic_consume(callback,  # 如果收到消息，就调用callback()来处理消息
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()   # 开始收消息，一支尝试收消息

