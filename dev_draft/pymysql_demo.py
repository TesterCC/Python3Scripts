#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-02-18 16:11'

"""
python2:
pip install MySQL-python

python3:
pip install PyMySQL


PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。

PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。

ref:
https://www.cnblogs.com/smallmars/p/7155376.html

当使用字符串格式化时容易引起sql注入
"""

import pymysql
import datetime

HOST = '127.0.0.1'
PORT = 3306
USER = ''
PASSWORD = ''
DB = ''

conn = pymysql.connect(
    host=HOST,
    port=PORT,
    user=USER,
    passwd=PASSWORD,
    db=DB,
)

cursor = conn.cursor()

create_time = datetime.datetime.now()

# 前7天的日期
change_time = create_time + datetime.timedelta(days=-7)

s_create_time = change_time.strftime("%Y-%m-%d %H:%M:%S")

# execute sql
# uncomment before test
# delete_row = cursor.execute('delete from sign_guest where create_time < %s',[s_create_time])
# print(delete_row)

effect_row = cursor.execute('select * from sign_guest where create_time < %s',[s_create_time])
print(effect_row)


conn.commit()

cursor.close()

conn.close()
