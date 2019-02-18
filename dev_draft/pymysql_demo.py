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
"""

import pymysql

HOST = '127.0.0.1'
PORT = 3306
USER = ''
PASSWORD = ''
DB = 'guest_test'

conn = pymysql.connect(
    host=HOST,
    port=PORT,
    user=USER,
    passwd=PASSWORD,
    db=DB,
)

cursor = conn.cursor()

# execute sql
delete_row = cursor.execute('delete from sign_guest where create_time < "2019-02-05 00:00:00"')
print(delete_row)

effect_row = cursor.execute('select * from sign_guest')

print(effect_row)

conn.commit()

cursor.close()

conn.close()
