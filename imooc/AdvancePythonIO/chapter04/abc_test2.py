#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/4 13:43'

"""
4-2 抽象基类(abc模块) - 2
"""


# 要强制某个子类必须实现某些方法
# 比如实现一个web框架, 集成cache(redis, cache, memorycache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 如何去模拟一个抽象基类
class CacheBase():
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    def set(self, key, value):
        pass

    def get(self, key):
        pass


redis_cache = RedisCache()
redis_cache.set("key", "value")
