# -*- coding:utf-8 -*-
__author__ = 'TesterCC'
__time__ = '18/1/11 16:31'

"""
tuple
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484018&idx=1&sn=44f10b570f3136e584b0935882a9be0b&scene=19#wechat_redirect
"""

tuple1 = (u'MFCTest', u'测试开发', u'1')

tuple2 = (1, 2, 3, 4, 5)

tuple3 = ("a", "b", "c", "d", "e")

tuple_demo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# 计算tuple1中元素个数
print(len(tuple1))

# 返回tuple2中最大值的元素
print(max(tuple2))

# 返回tuple3中最小值的元素
print(min(tuple3))

# 将list转换成元组
print("-"*50)
print("列表转元组示例")
list_demo = [1, 2, 3, 4, 5, 6, 7]
tuple0 = tuple(list_demo)
print(type(tuple0))

# 打印转换后的元组
print(tuple0)

print("-"*50)

# 切片 Slice
print(u"元组切片操作示例!")

data_demo = (u"DeepTest", u"SET", u"MFC", u"hello", u"python3")

# 读取第2个元素SET, 注意索引下标从0开始
e = data_demo[1]
print(e)

# 读取倒数第2个hello
e = data_demo[-2]
print(e)

# 切片，截取从第2个元素开始后的所有元素
e = data_demo[1:]
print(e)

# 切片，截取第2-4个元素, 4是第5个元素，就是说左闭右开[a:b)
e = data_demo[1:4]
print(e)


print("-"*50)

print(u"元组合并或连接操作示例!")
tup1 = (u"LearnTest", u"appium")
tup2 = (u"MFC", u"hello", u"python3")

# 合并元组
tup3 = tup1 + tup2

print(tup1)
print(tup2)
print(tup3)

# 删除元组
print("-"*50)
print(u"元组合并或连接操作示例!")
tup1 = (u"LearnTest", u"appium")

print(tup1)

del tup1

# print(tup1)    # throw except

# 元组运算

print("-"*50)
print(u"元组运算示例")

tup1 = (u"LearnTest", u"测试开发")
tup2 = (1, 2, 3, 4)

# 计算元组长度
print(len(tup1))

# 元组连接
tup3 = tup1 + tup2
print(tup3)

# 元组复制
tup4 = tup1 * 2
print(tup4)

# 判断元素是否在元组中, 是则返回True, 否则返回
result = 5 in tup2
print(result)
result2 = 1 in tup2
print(result2)

# 遍历元组
for t in tup2:
    print(t)




