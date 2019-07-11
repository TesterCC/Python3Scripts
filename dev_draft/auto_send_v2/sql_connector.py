#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-03 16:41'

import pymysql

from dev_draft.auto_send_v2 import config


"""
ignore:不走数据库获取数据
"""

class SqlConnector:
    def __init__(self):
        self.db_host = config.DB_HOST
        self.db_user = config.DB_USER
        self.db_passwd = config.DB_PASSWD
        self.db_name = config.DB_NAME
        self.db_port = config.DB_PORT
        self.db_charset = config.DB_CHARSET

        self.db = pymysql.connect(host=self.db_host, user=self.db_user, passwd=self.db_passwd, db=self.db_name,
                                  port=self.db_port,charset=self.db_charset)
        self.cursor = self.db.cursor()


    def query_db_version(self):
        # 使用 execute()  方法执行 SQL 查询
        self.cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        data = self.cursor.fetchone()

        # print("Database version : %s " % data)

        # 关闭数据库连接
        self.db.close()

        return "Database version : %s " % data



