#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-27 21:53'


"""
4.编写server端代码
"""

import time
import test_pb2_grpc
import grpc

from concurrent import futures
from views import test


class OrderHandler(test_pb2_grpc.OrderHandlerServicer):
    def create_order(self, request, context):
        return test(request, context)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_OrderHandlerServicer_to_server(
        OrderHandler(), server)
    server.add_insecure_port('[::]:{}'.format(12006))
    server.start()
    print("11111")
    try:
        while True:
            time.sleep(186400)
    except KeyboardInterrupt:
        server.stop(0)


serve()
