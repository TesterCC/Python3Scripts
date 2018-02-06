# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/31 22:08'


"""
官方文档地址：

http://pyyaml.org/wiki/PyYAMLDocumentation

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484127&idx=1&sn=fb89289f24417afc8318714080147102&scene=19#wechat_redirect

作业：研究robotframework的yaml语法结构，并形成学习记录
"""

import yaml


print("python yaml基本示例")

document = """
公众号: Python全栈研习社
基本信息:
    创建人: MFC
    id: 02
"""

# 将yaml格式内容转换成 dict类型
# load：将yaml格式的字符串转换成Python对象
load = yaml.load(document)
print(type(load))
print(load)

print("---" * 20)

# 将python对象转换成为yaml格式文档
# dump：将Python对象转换成yaml格式文档
output = yaml.dump(load)
print(type(output))
print(output)

