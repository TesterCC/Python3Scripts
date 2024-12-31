#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/20 22:30'

import json

"""
注意json.loads/json.dumps和json.load/json.dump的不同，不带s的函数需要和文件结合。
"""


def read_json():
    """
    演示如何读取json_data.json的内容转化python对象
    """
    print("Python读取json内容文件转化成Python对象实例")

    fp = open('json_data.json', 'r')

    json_data = json.load(fp)   # 将已编码的json字符串解码为Python对象

    print(type(json_data))
    print(json_data)

    fp.close()


def write_json():
    """
    将python对象转化存json串存入文件
    """
    print("python写入json串实例:")

    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}]

    fp = open('json_write.json', 'w')

    # 以可读性格式写入json_write.json文件中
    content = json.dump(data, fp, sort_keys=True, indent=4, separators=(',', ': '))

    print(content)

    fp.close()


def write_json2():
    """
    将python对象转化存json串存入文件
    """
    print("python写入json串实例:")

    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}]

    with open('json_write2.json', 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4, separators=(',', ': '))

    fp.close()


if __name__ == '__main__':

    read_json()

    write_json()

    write_json2()

