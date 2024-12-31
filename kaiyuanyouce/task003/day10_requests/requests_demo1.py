# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/2 23:09'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484193&idx=1&sn=a7e4af30b8149e9b24efe3b4e8a6120e&scene=19#wechat_redirect

代码演示利用requests访问github的api，具体api说明请参见
https://developer.github.com/v3

演示了GET方法及如何获取响应状态码、响应头、编码、文本内容、json内容
"""

# 导入模块
import requests

if __name__ == "__main__":
    print("接口测试 - requests基本示例")

    # 发送HTTP GET请求，获取github API列表
    r = requests.get("https://api.github.com")
    # r = requests.get("http://httpbin.org/get")

    # 请求返回码
    status_code = r.status_code

    # 完整的返回头
    headers = r.headers

    # 请求返回头 content-type的值
    content_type = r.headers["content-type"]

    # 返回内容编码类型
    code = r.encoding

    # 返回内容文本
    text = r.text

    # 若返回结果为json格式，我们可以获取其json格式内容
    json_data = r.json()
    # print(type(json_data))   # dict

    # 打印上述所有获取到的值
    print("状态码： ", status_code)
    print("返回头： ", headers)
    print("content-type： ", content_type)
    print("编码：", code)
    print("文本内容： ", text)
    print("json串内容: ", json_data)