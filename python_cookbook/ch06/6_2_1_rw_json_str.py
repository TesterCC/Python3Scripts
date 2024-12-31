# -*- coding=utf-8 -*-
'''
DATE: 2020/09/18
AUTHOR: Yanxi Li
'''

# P181  6.2读写JSON数据

# 将Python数据结构转换为JSON字符串，即 序列化

import json

data = {
    "name": "TESTER",
    "shares": 100,
    "price": 547.16
}

print("1.Serialization: ")
json_str = json.dumps(data)
print(type(json_str), json_str)

# 将JSON编码的字符串再转换回Python数据结构，即 反序列化
print("2.Deserialization: ")
data = json.loads(json_str)
print(type(data), data)
