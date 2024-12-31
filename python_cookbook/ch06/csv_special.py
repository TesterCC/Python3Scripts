# coding=utf-8
'''
DATE: 2020/09/18
AUTHOR: Yanxi Li
'''
# P178
# csv产生的数据都是字符串类型的，它不会做任何其他类型的转换。 如果你需要做这样的类型转换，你必须自己手动去实现。
# 转换字典中特定字段
import csv

print("Reading as dicts with type conversion")

field_types = [('Price', float),
               ('Change', float),
               ('Volume', int)]

with open('stocks2.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)

# 如果你读取CSV数据的目的是做数据分析和统计的话， 你可能需要看一看 Pandas 包。
# Pandas 包含了一个非常方便的函数叫 pandas.read_csv() ， 它可以加载CSV数据到一个 DataFrame 对象中去。 然后利用这个对象你就可以生成各种形式的统计、过滤数据以及执行其他高级操作了。
