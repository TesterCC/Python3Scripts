# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/15 21:11'

"""
通过Python的ConfigParser模块来对ini文件进行读写操作

读取
read(filename) 读取ini文件内容

sections() 获取所有的section，并以列表的形式返回

options(sections) 获取指定section的所有option

get(section,option) 获取section中option的值，返回为string类型

写入
set( section, option, value) 对section中的option进行更新

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484051&idx=1&sn=9082bec8194914852764c33accf98411&scene=19#wechat_redirect
"""

import configparser

# 先构建一个对象
config = configparser.ConfigParser()

print("开始写入config.ini文件:")
# 写入几组数据, 先新增一个section
config.add_section("学习测试")

# 在新增的section下加key-value键值对
config.set("学习测试", "微号", "LearnTest")
config.set("学习测试", "口号", "每天敲代码")
config.set("学习测试", "号外", "其实多课程学习并行")

# 再新增一个section，但不加key-value键值对
config.add_section("单独一个")

# 写入文件
with open('config.ini', 'w') as configfile:
    config.write(configfile)

print("－"*50)
print("开始读取config.ini文件:")

config.read("config.ini")

# 获取它的所有section
print("获取它的所有section:")
sections = config.sections()
print(sections)

# 获取sections下所有的options
print("获取sections下所有的options:")
for sec in sections:
    # 获取指定section的所有option
    option = config.options(sec)
    print(option)        # section 单独一个下面无options，所以是[]

# 根据sections和options获取对应的value值
print("根据sections和options获取对应的value值:")
for sec in sections:
    for option in config.options(sec):
        print("[%s] %s=%s" % (sec, option, config.get(sec, option)))
