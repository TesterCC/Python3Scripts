# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/8 23:37'


"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484163&idx=1&sn=f54f0fbf53cb44c4a16296a5941e120f&scene=19#wechat_redirect

urllib中parse、request模块的重点API进行说明，也是以后大家最常用到的API。
"""

import urllib.parse
import urllib.request


def basic_request():
    print("urllib API实例演示说明:")

    # 访问百度首页
    response = urllib.request.urlopen('http://www.baidu.com')

    # 打印下首页是html源码
    # 获取完整的响应内容，便于断言其中的特定值
    html = response.read()
    print(html)

    # 打印下http header信息
    # 有时候我们需要提取header值来用于下一个请求
    header = response.info()
    print(header)

    # 获取下状态码 http响应的status code
    # 接口测试的一个断言，就是断言状态码
    status_code = response.getcode()
    print(status_code)

    # 打印下本次请求的目标url
    url = response.geturl()
    print(url)


if __name__ == '__main__':
    basic_request()

