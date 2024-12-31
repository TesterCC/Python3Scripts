#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-15 10:13'

'''
pip install nameko
https://nameko.readthedocs.io/en/stable/

Start Server in terminal, if you change default RabbitMQ user and password, need to set config yaml, such as foobar.yaml
nameko run --config ./foobar.yaml helloworld

Launch nameko shell
nameko shell --config ./foobar.yaml
n.rpc.greeting_service.hello(name="Tester")
'''

from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
