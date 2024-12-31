# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/2 23:19'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484201&idx=1&sn=7f272acf70a9d07edd91de69b09df44a&scene=19#wechat_redirect

请求头定制

POST请求
"""

import requests


def custom_header():
    print("接口测试 - requests自定义请求头基本示例:")

    url = "http://httpbin.org/get"

    # 定义自定义请求头数据
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
               "custom-head": "Pentest"}  # 发送带自定义头的请求
    r = requests.get(url, headers=headers)

    # 返回内容文本
    content = r.text

    print("返回内容:")
    print(content)


def post_demo():
    print("requests post示例")

    # 目标url
    url = "http://httpbin.org/post"

    # 请求头headers
    headers = {"custom-header": "mypost"}

    # 要post的数据
    data = {"data_1": "fullstackpentest", "data_2": "fullstackpentest.com"}

    # 发送post请求
    r = requests.post(url, data=data, headers=headers)

    # 输出结果
    print(r.text)


def post_json():
    """
    如何postjson数据到服务
    """
    print("requests post json数据示例:")

    # 目标服务url
    url = "http://jsonplaceholder.typicode.com/posts"

    # 自定义头
    headers = {
        "custom-post": "my-post",
        "custom-header": "my-json-header"
    }

    # 要post的数据
    json_data = {
        "title": "fullstackpentest",
        "body": "接口测试",
        "userId": "1"
    }

    # post json格式的数据  －－ 注意区别
    r = requests.post(url, json=json_data, headers=headers)

    # 打印下返回结果
    print(r.text)


if __name__ == '__main__':
    custom_header()

    print("-" * 80)
    post_demo()

    print("-" * 80)
    post_json()

    