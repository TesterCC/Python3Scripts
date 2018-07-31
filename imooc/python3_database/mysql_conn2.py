#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/29 23:58'

"""
https://mysqlclient.readthedocs.io/
http://www.runoob.com/python/python-mysql.html

pip install mysqlclient
pip install mysqlclient -i https://pypi.douban.com/simple/
"""

import MySQLdb

# prepare sql
sql = 'SELECT * FROM news;'

try:

    # get connect
    conn = MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='news',
        port=3306,
        charset='utf8'
    )

except MySQLdb.Error as e:
    print("Error: %s" % e)

# get data
cursor = conn.cursor()
cursor.execute('SELECT * FROM news ORDER BY created_at DESC;')
ret = cursor.fetchone()
# ret = cursor.fetchall()
print(ret)

# close data
conn.close()
