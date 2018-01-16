# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/17 00:30'

import time


# 格式化日期时间：strftime函数
# time.strftime(format[, t])
print("strftime函数示例：")

# 先看下当前默认格式化的时间

localtime = time.asctime(time.localtime())
print("当前默认日期时间格式: %s" % localtime)

# 格式化为： 年-月-日 时:分:秒 星期几
print("24小时制全格式 完整星期：", time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
print("12小时制缩写格式 简写星期：", time.strftime("%Y-%m-%d %I:%M:%S %a", time.localtime()))

# 带a.m. 或 p.m. 标识时间格式  %p
print("带a.m或p.m 24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))

# 把时区也带上看看 %z
print("带时区的全格式：", time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

# 格式乱排下试试
print("随意排格式：", time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))

