# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/13 23:17'

"""
Python3 for循环
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484031&idx=1&sn=669f92bf80d276b116225d147ab4d14b&scene=19#wechat_redirect
"""


def tuple_for():
    """
    for循环如何进行元组遍历输出
    """
    tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    print(u"遍历元组，并打印出来： ")
    for t in tuple:
        print(t)


def list_for():
    """
    用for循环如何进行列表遍历输出
    """
    list0 = [u'LearnTest', u'测试', u'快学Python3']

    print(u"遍历列表，并打印出来： ")
    for text in list0:
        print(text)


def dict_for():
    """
    用for循环如何进行字典遍历输出
    """
    dict = {u"开源": u"LearnTest", u"python": u"快学Python3"}

    print(u"遍历字典方式一，并打印出来:")
    for key, value in dict.items():
        print("%s : %s " % (key, value))

    print("\n-----------------------------")

    print(u"遍历字典方式二，并打印出来: ")
    for key in dict:
        print("%s : %s " % (key, dict[key]))


def range_for():
    """
    用for循环如何进行对range()遍历输出
    """
    print(u"range for循环实例")

    # 使用默认参数生成序列进行遍历
    for i in range(5):
        print(i, end=',')

        # 换行
    print('')

    # 指定范围生成序列进行遍历
    for i in range(0, 10):
        print(i, end=',')

        # 换行
    print('')

    # 带步长方式生成序列进行遍历
    for i in range(0, 10, 2):
        print(i, end=',')


if __name__ == '__main__':
    tuple_for()
    list_for()
    dict_for()
    range_for()