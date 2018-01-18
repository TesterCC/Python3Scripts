# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/17 21:13'

"""
演示下urllib基本功能实例，例如如何获取返回码等等基本信息

https://docs.python.org/3/library/urllib.html

http://blog.csdn.net/c406495762/article/details/60137956

"""

import urllib.request


def basic_urllib():
    """
    urllib基本应用实例
    """
    print("urllib基本实例")

    url = "http://www.bing.com"

    # 访问下必应
    response = urllib.request.urlopen(url)

    # 打印下状态码
    print(response.status)

    # 打印下状态码对应的可读性文字说明，例如在http协议里，200 对应 OK
    print(response.reason)

    print("-" * 70)

    # 打印下请求返回的header
    print("打印下请求返回的header:")
    print(response.headers)

    # 打印下请求返回的数据
    print("-" * 70)
    print("打印下请求返回的数据:")
    print(response.read().decode("utf-8"))


def urllib_custom1():
    """
    设置User Agent的方法
    方法1: 在创建Request对象的时候传入headers参数
    """
    # 以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    head = {}
    # 写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    # 创建Request对象
    req = urllib.request.Request(url, headers=head)

    print("获取Request的headers:")
    print(req.headers)

    # 传入创建好的Request对象
    response = urllib.request.urlopen(req)

    print("-" * 70)

    # 读取响应信息并解码
    html = response.read().decode('utf-8')

    # 打印信息
    print("Print HTML:")
    print(html)


def urllib_custom2():
    """
    设置User Agent的方法
    方法2: 在创建Request对象时不传入headers参数，创建之后使用add_header()方法，添加headers
    """
    # 以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    # 创建Request对象
    req = urllib.request.Request(url)
    # 传入headers
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')

    print("获取Request的headers:")
    print(req.headers)

    # 传入创建好的Request对象
    response = urllib.request.urlopen(req)
    # 读取响应信息并解码
    html = response.read().decode('utf-8')
    # 打印信息
    print(html)


if __name__ == '__main__':
    basic_urllib()
    urllib_custom1()
    urllib_custom2()
