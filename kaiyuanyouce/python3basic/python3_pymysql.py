# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/18 23:15'


"""
主要讲解如何使用pymysql实现增删改查动作，并附上对应的示例。
在pymysql中提供了Connection和Cursor对象来管理操作MySQL。
对SQL要熟悉，才能更好的应用PyMySQL库
其次要注意在构造sql时，最好构建成参数化方式

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484072&idx=1&sn=0312f49a4674669fd652c46c8c5ccc72&scene=19#wechat_redirect
"""

import pymysql
import random


def pymysql_demo():
    """
    基本前提，假设你在本地已经安装了MySQL服务或是你拥有远程访问某个MySQL服务的权限。
    """
    print("PyMySQL基本示例")

    # 创建一个连接实例
    conn = pymysql.connect(
        host="localhost",  # mysql服务ip地址，若服务在本机则用localhost
        port=3306,  # mysql服务端口
        user="root",  # 访问mysql的用户名
        password="123456xx",  # 访问mysql的密码
        db="t1",  # 默认连接到的数据库
        charset="utf8"  # 连接字符集
    )

    try:
        # 创建用于交互的cursor对象
        cursor = conn.cursor()

        # 先插入10条测试数据

        # 构建插入数据的sql
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # sql = "INSERT INTO `sign_event` (`name`, `limit`, `address`, `status`, `time`) VALUES (%s, %s, %s, %s, %s)"

        # 生成10条测试数据
        sql_data = []
        for index in range(0, 3):
            email = "%.10f@126.com" % random.random()
            password = random.random()
            sql_data.append((email, password))

            # 执行sql,进行批量插入数据
        cursor.executemany(sql, sql_data)

        # 提交至数据库
        conn.commit()

        # 查询5条数据
        sql = "SELECT * FROM `users` LIMIT 5"

        # 执行sql
        cursor.execute(sql)

        # 取查询到的所有数据
        all_data = cursor.fetchall()

        # 遍历打印出来
        print("取所有查询到的数据")
        for data in all_data:
            print("id: %d email: %s password: %s" % (data[0], data[1], data[2]))

        # 取1条数据
        # sql = "SELECT * FROM `users`"
        cursor.execute(sql)
        one_data = cursor.fetchone()
        # print(type(one_data))
        # print(one_data)

        print("\n取1条数据: {0} ".format(one_data))   # format强大啊
        print("id: %d -> email: %s -> password: %s" % (one_data[0], one_data[1], one_data[2]))

    finally:
        # 最后把数据库连接关闭
        conn.close()


if __name__ == '__main__':
    pymysql_demo()
