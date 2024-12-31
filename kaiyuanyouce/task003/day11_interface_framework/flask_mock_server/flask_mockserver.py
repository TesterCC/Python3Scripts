#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 16:17'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484164&idx=1&sn=41591ad4d1f68b309c19de4b0ec60c63&scene=19#wechat_redirect

构建一个简单的server，后续的接口测试分享实战都会基于这个server来进行交互实战。

为了让代码显得简洁，不会添加异常等容错处理。

下面基于flask实现HTTP的GET\POST\HEAD等方法，用于后续的测试，然后也可以基于这个代码进一步扩展成restful风格的API。

说明：

1.注意POST\HEAD\DELETE方法，响应头均被加入了Access-Control-Origin属性，其值为：*

2.注意即便给HEAD方法添加了响应内容，但你在实际接收到的内容是没有响应内容的，请思考为什么

3.上述仅用于简单的测试，不讨论其优雅、靠谱、高大上等等可能性
"""

from flask import Flask
from flask import jsonify
from flask import request, Response
import random
import time


app = Flask(__name__)

"""
这里有的接口我们才去返回json串
所有的json传对应的value值都为随机的
"""


def random_str():
    """
    生成随机字符串
    """

    # 待选随机数据
    data = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    # print("data lenth", len(data))   # 76

    # 用时间来做随机播种
    random.seed(time.time())

    # 随机选取数据
    sa = []
    for i in range(8):
        sa.append(random.choice(data))
        salt = ''.join(sa)

    return salt


def make_response():
    """
    构建response
    """
    content = '{"result": "%s", "data": "%s"}' % (random_str(), random_str())
    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'

    return resp


# http GET
@app.route("/query", methods=["GET"])
def query():
    return jsonify(
        username=random_str(),
        password=random_str()
    )


# http POST
@app.route("/update", methods=["POST"])
def update():
    return make_response()


# http DELETE
@app.route("/delete", methods=["DELETE"])
def delete():
    return make_response()


# http HEAD
@app.route("/head", methods=["HEAD"])
def head():
    return make_response()


if __name__ == '__main__':
    app.run(debug=True)
