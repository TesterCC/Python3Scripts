# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/5 20:37'

import os
from configparser import ConfigParser

path = "mysql.ini"

# 初始化
cf = ConfigParser()  # 读取ini文件,path为要读取的ini文件的路径
cf.read(path)

# 获取所有sections。即将配置文件中所有“[ ]”读取到列表中
s = cf.sections()

# 获取指定section的options。
# 即将配置文件某个section内key 读取到列表中
o = cf.options("mysql")

# 获取指定section 的配置信息
v = cf.items("mysql")    # 按照类型读取指定section 的option 信息
print(v)
#  同样的还有getfloat、getbooleandb_host = cf.get("mysql", "host")

# db_port = cf.getint("mysqldb", "port")  # no comment will report error

db_user = cf.get("mysql", "user")

db_pass = cf.get("mysql", "password")

# 设置某个option 的值。（记得最后要保存）
cf.set("mysql", "password", "654321")

# 添加一个section。（同样要保存）
cf.add_section('oracle')

cf.set('oracle', 'host', '127.0.0.1')
cf.set('oracle', 'port', '5555')

# 获取指定section 的配置信息
v = cf.items("oracle")    # 按照类型读取指定section 的option 信息
print(v)

#  移除section 或者option (同样要保存)
cf.remove_option('oracle', 'port')
cf.remove_section('oracle')

# 获取指定section 的配置信息
v = cf.items("mysql")    # 按照类型读取指定section 的option 信息
print(v)

