#!/usr/bin/env python
#coding=utf-8

# Web接口开发与自动化测试-基于Python语言 P68-P67

from pymysql import cursors,connect

# connect to database
conn = connect(host='127.0.0.1',
               user='root',
               password='yanxi76543210',
               db='guest',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        # query added guest
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql,('18800110002',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()