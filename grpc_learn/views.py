#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-27 21:56'


import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
import test_pb2


"""
3.编写server对应的view文件 views.py 
要用Django
"""

def grpc_request(func):
    """
    将grpc请求重新构造成django request
    (grpc request --> django request)
    并封装相应返回值
    :param func:
    :return:
    """

    def f(request, context):
        f = lambda x: {k: v for k, v in x.items()} if hasattr(x, 'items') else x
        args = {i[0].name: f(i[1]) for i in request.ListFields()}

        # 构造django request 对象，并添加参数信息
        dj_request = HttpRequest()
        dj_request.GET = args
        # dj_request.POST = args
        # dj_request._body = json.dumps(args)
        dj_request.META = args

        ret = func(dj_request)

        # 处理django的response 对象,转换为grpc的对象
        json_response = test_pb2.JSONResponse()
        json_response.rst_string = ret.getvalue()

        return json_response

    return f


def check_inenty(func):
    def f(request):
        if "identy" not in request.META:
            return JsonResponse(dict(status=403))
        else:
            return func(request)

    return f


@grpc_request
@check_inenty
def test(request):
    return JsonResponse(dict(test=1, name="333"))