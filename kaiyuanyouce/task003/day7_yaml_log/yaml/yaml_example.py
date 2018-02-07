# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/6 03:15'


"""
多段yaml格式内容解析用用到load_all函数

demo.yaml
"""

import yaml
import codecs

print("多段yaml格式内容解析用用到load_all函数")
print("python yaml基本示例:")

fp = codecs.open("demo.yaml", "r", "utf-8")
document = fp.read()
fp.close()

# 将yaml格式内容 转换成 dict类型
# load_all返回的是一个迭代器对象，需要自己去遍历获取每一个段的转换后才python对象。
load = yaml.load_all(document)

# 遍历迭代器
for data in load:
    print(type(data))
    print(data)

    print("---" * 25)
    # dump 将python对象转换成为yaml格式文档
    output = yaml.dump(data)
    print(type(output))
    # print(output)  # \u4E2D\u6587\
    print(output.encode('utf-8').decode('unicode_escape'))


"""
先检查text是什么类型
如果type(text) is bytes，那么text.decode('unicode_escape')
如果type(text) is str，那么text.encode('utf-8').decode('unicode_escape')
"""