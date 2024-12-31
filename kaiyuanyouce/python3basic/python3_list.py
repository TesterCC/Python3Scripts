# -*- coding:utf-8 -*-
__author__ = 'TesterCC'
__time__ = '18/1/11 17:31'


list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(u"内置函数处理list示例:")

# 计算list_demo中元素个数
print(len(list_demo))

# 返回list_demo中最大值的元素
print(max(list_demo))

# 返回list_demo中最小值的元素
print(min(list_demo))

# 将元组转换成list
list_demo = (1, 2, 3, 4, 5, 6)
list1 = list(list_demo)
print(type(list1))

# 打印转换后的列表
print(list1)

# list方法
print("-"*50)
print(u"list方法代码示例： ")
list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
list2 = [7, 8, 9, 0, 10, 11]

# append，追加一个元素，加到最后
list1.append(100)
print(list1)

# count,统计1出现的次数
count = list1.count(1)
print(count)

# count,统计7出现的次数
count = list2.count(7)
print(count)

# extend, 将list2追加到list1中
list1.extend(list2)
print(list1)


# index, 返回第一个2的索引
index = list1.index(2)
print(index)

# index, 返回第一个7的索引
index2 = list1.index(7)
print(index2)

# insert, 在列表第一个位置插入200
list1.insert(0, 200)
print(list1)

# insert, 在列表倒数第二位置插入900
list1.insert(-1, 900)
print(list1)

# pop, 删除最后一个元素
list1.pop()
print(list1)

# reverse, 把列表反向
list1.reverse()
print(list1)

# sort, 对列表进行排序
list1.sort()
print(list1)

# copy，列表拷贝
print("copy list")
list3 = list1.copy()
print(list1)
print(list3)

# clear 清空列表
print("clear list")
list1.clear()
print(list1)
print(list3)

# slice
print("-"*50)
print(u"列表切片操作示例:")

data_demo = [u"LearnTest", u"selenium", u"SET", u"hello", u"python3"]

# 读取第二个元素selenium, 注意索引下标从0开始
e = data_demo[1]
print(e)

# 读取倒数第二个hello
e = data_demo[-2]
print(e)

# 切片，截取从第2个元素开始后的所有元素
e = data_demo[1:]
print(e)

# 切片，截取第2-4个元素
e = data_demo[1:4]
print(e)

# update
print("-"*50)
print(u"列表更新操作示例:")

data_demo = [u"LearnTest", u"selenium", u"SET", u"hello", u"python3"]
print(data_demo)

# 把hello改为hello word
data_demo[3] = u"hello word"
print(data_demo)

# 把最后的python3改为java
data_demo[-1] = u"java"
print(data_demo)

