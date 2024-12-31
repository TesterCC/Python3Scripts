#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-28 13:18'


"""
5.编写client代码进行测试
"""

import grpc
import test_pb2_grpc, test_pb2


channel = grpc.insecure_channel("127.0.0.1:12006")
stub = test_pb2_grpc.OrderHandlerStub(channel)
ret = stub.create_order(test_pb2.OrderRequest(phone="333", price="50"))

print(ret.rst_string)