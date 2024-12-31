# -*- coding: utf-8 -*-
# @Time    : 2022/8/20
# @Author  : SecCodeCat

"""
序列化 Python对象
问题: 你需要将一个 Python对象 序列化为 一个字节流，以便将它保存到一个文件、存储到数据库或者通过网络传输它

pickle是一种Python特有的自描述的数据编码。
通过自描述，被序列化后的数据包含每个对象开始和结束以及它的类型信息。

注意：千万不要对不信任的数据使用pickle.load()，因为pickle在加载时的副作用是它会自动加载相应模块并构造实例对象。
"""

# 普通方案pickle
import pickle

data = {"secdev": ["Go", "Python", "Rust"]}

# serialization: python obj -> bytes stream, save in file
with open("./serialization","wb") as f:
    pickle.dump(data, f)

# deserialization: bytes stream -> python obj
with open("./serialization","rb") as f:
    # restore from a file
    data = pickle.load(f)

print(f"test data 1: {data}")

# python3 obj -> str, data = {"secdev": ["Go", "Python", "Rust"]}
t = pickle.dumps(data)
# print(t)  # debug

# restore from a string
data2 = pickle.loads(t)

print(f"test data 2: {data2}")