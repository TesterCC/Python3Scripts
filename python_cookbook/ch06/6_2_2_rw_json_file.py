# -*- coding=utf-8 -*-
'''
DATE: 2020/09/18
AUTHOR: Yanxi Li
'''

# P181-182  6.2.2 读写JSON数据 file

# 如果要同文件而不是字符串打交道，可使用 json.dump()以及json.load()来编码和解码JSON数据。

# 将Python数据结构转换为JSON字符串，即 序列化2023
import json

data = {
    "name": "TESTER",
    "shares": 100,
    "price": 678.12,
    "remark": "test use"
}

print("1.Serialization in file, writing json data: ")

with open('data.json', 'w') as f:
    json.dump(data, f)
print("[D] finish write ...")

# 将JSON编码的字符串再转换回Python数据结构，即 反序列化
print("2.Deserialization from file, reading data back: ")

with open('data.json', 'r') as f:
    data = json.load(f)
print(type(data), data)