#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 15:39'

import redis


class RedisHelper():
    def __init__(self, host='localhost', port=6379, password='HereWithYou'):
        self.__redis = redis.StrictRedis(host, port, password)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""

    def set(self, key, value):
        self.__redis.set(key, value)
