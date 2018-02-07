# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/7 17:11'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484143&idx=1&sn=bdafde94b9989550ffd2086cc6231fc4&scene=19#wechat_redirect

演示下如何使用http.client进行http的GET、POST、HEAD方法
"""

import http.client
import urllib.parse


def get_method():
    """
    http.client GET方法示例
    """
    print("http.client GET方法示例:")
    # 初始化
    conn = http.client.HTTPSConnection("www.python.org")
    # 发送GET请求
    conn.request("GET", "/")
    # 获取响应
    r1 = conn.getresponse()
    # 打印状态码、对应说明、协议版本
    print(r1.status, r1.reason, r1.version)
    # 读取整个响应内容
    data1 = r1.read()
    print("读取整个响应内容:")
    print(data1)
    conn.close()


def get_method_chunck():
    """
    下面代码演示如何分chunck读取内容
    """
    print("下面代码演示如何分chunck读取内容:")
    # 初始化
    conn = http.client.HTTPSConnection("www.python.org")
    # 发送GET请求
    conn.request("GET", "/")
    # 获取响应
    r1 = conn.getresponse()
    while not r1.closed:
        # 每次读取200bytes
        r1_data = r1.read(200)
        if len(r1_data) == 0:
            break
        print(r1_data)
    conn.close()


def get_not_found_url():
    """
    请求不存在的url
    """
    print("请求不存在的url:")
    # 初始化
    conn = http.client.HTTPSConnection("www.python.org")
    # 发送GET请求
    conn.request("GET", "/parrot.spam")
    r2 = conn.getresponse()
    print(r2.status, r2.reason)
    data2 = r2.read()
    print(data2)
    # 断开连接
    conn.close()


def head_method():
    """
    http.client HEAD方法
    """
    print("http.client HEAD方法:")
    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("HEAD", "/")
    res = conn.getresponse()
    print(res.status, res.reason)

    data = res.read()
    print(len(data))
    conn.close()


def post_method():
    """
    http.client POST方法
    """
    print("http.client POST方法:")
    # 请注意这里设置http headers的方法
    params = urllib.parse.urlencode({'@number': 19999,
                                     '@type': 'issue',
                                     '@action': 'show'})
    # http headers参数
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = http.client.HTTPConnection("bugs.python.org")
    # 把请求的data和头参数一起传入
    conn.request("POST", "", params, headers)
    # 获取响应对象
    response = conn.getresponse()
    # 打印响应状态
    print(response.status, response.reason)
    # 读取响应内容
    data = response.read()
    print(data)
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    print("http.client基本示例>>>>")
    get_method()
    print("---" * 30)
    get_method_chunck()
    print("---" * 30)
    get_not_found_url()
    print("---" * 30)
    head_method()
    print("---" * 30)
    post_method()



