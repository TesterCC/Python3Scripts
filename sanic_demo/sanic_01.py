#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-02 18:55'


# Python Microservice Development P263

# 如果视图函数返回字典，框架会自动将其转换成JSON

from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.middleware('response')
async def convert(request, response):
    if isinstance(response, dict):
        return json(response)
    return response

@app.route("/api")
async def api(request):
    return {'some': 'test_data', 'comments':'test'}

app.run()
# 如果微服务仅返回json映射，那这个小中间件函数就能简化视图代码