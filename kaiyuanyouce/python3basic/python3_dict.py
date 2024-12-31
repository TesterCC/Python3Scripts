#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'TesterCC'
__time__ = '18/1/11 23:09'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484021&idx=1&sn=7ffd91b6a45ab38a6892df2d0388ff4a&scene=19#wechat_redirect
"""


def basic_dict():
    # 字典基本示例
    print("字典基本示例")
    dict = {u"LearnTest": u"测试", u"book": u"快学Python3"}

    # 计算字典的长度
    print(len(dict))

    # 以字符方式输出字典,即将字典转换成字符串
    str_d = str(dict)
    print(str_d)
    print(dict)

    # 判断类型
    print(type(dict))  # 字典类型
    print(type(str_d))  # 字符串str类型


def dict_method():
    print(u"字典方法应用示例")
    dict_demo = {u"LearnTest": u"测试", u"ebook": u"快学Python3"}
    tup1 = [1, 2, 3, 4]

    # copy复制字典
    print("copy dict:")
    dict_cp = dict_demo.copy()
    print(dict_demo)
    print(dict_cp)
    print(id(dict_demo))
    print(id(dict_cp))

    # fromkeys创建字典
    print("use fromkeys")
    dict_new = dict.fromkeys(tup1, u"value")
    print(dict_new)

    # get获取指定key的value
    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    print("get specific key -> value")
    val1 = dict_demo.get(u"LearnTest", u"我是默认值")
    val2 = dict_demo.get(u"Python3", u"我是默认值")
    print(val1)
    print(val2)

    # in, 判断key是否存在
    key = u"LearnTest"
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)

    # items, 以元组形式返回字典所有的(key, value)
    items = dict_demo.items()
    print(items)

    # keys 以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    print("set default:")
    set_result1 = dict_demo.setdefault(u"LearnTest", u"设置值")
    set_result2 = dict_demo.setdefault(u"我是key", u"我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    # update, 更新字典
    print("update dict:")
    dict_demo.update(dict_new)
    print(dict_demo)

    # values,返回字典中所有的value
    values = dict_demo.values()
    print(values)


def dict_crud():
    """
    对字典进行遍历、修改、删除操作
    """
    print(u"字典遍历、修改、删除示例:")
    dict_demo = {u"LearnTest": u"测试", u"ebook": u"快学Python3"}

    # 遍历　Method1
    for key, value in dict_demo.items():
        print("%s : %s" % (key, value))

    # 遍历　Method2
    for key in dict_demo.keys():
        print("%s : %s" % (key, dict_demo[key]))

    # 修改
    dict_demo[u"ebook"] = u"修改后的值"
    print(dict_demo)

    # 删除指定元素
    print("删除指定元素")
    del dict_demo[u"ebook"]
    print(dict_demo)

    # 清空字典
    dict_demo.clear()
    print(dict_demo)


if __name__ == '__main__':
    basic_dict()
    dict_method()
    dict_crud()
