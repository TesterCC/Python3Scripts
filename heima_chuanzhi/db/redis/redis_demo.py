#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 15:32'

"""
启动本机redis:
cd /usr/local/redis-4.0.1/etc    
redis-server redis.conf

查看redis配置信息
vim redis.conf

检查是否启动：
ps -ef | grep redis
或者（6379是redis的默认端口）
lsof -i:6379
"""

import redis

# connection to redis
try:
    r = redis.StrictRedis(host='localhost', port=6379, password='HereWithYou')
except Exception as e:
    print(e.message)

# Method 1: 方式一：根据数据类型的不同，调用相应的方法，完成读写
print(r.set('name', 'hello redis'))
print(r.get('name'))

print("*" * 60)
# Method 2: 方式二：pipline
# 缓冲多条命令，然后一次性执行，减少服务器-客户端之间TCP数据库包，从而提高效率
pipe = r.pipeline()
pipe.set('name', 'world')
pipe.set('test', 't_world')
pipe.get('name')
pipe.get('test')
print(pipe.execute())
