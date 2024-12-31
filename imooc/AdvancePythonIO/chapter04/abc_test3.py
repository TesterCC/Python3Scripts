#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/4 13:43'

"""
4-2 抽象基类(abc模块) - 2
"""

import abc


# 要强制某个子类必须实现某些方法
# 比如实现一个web框架, 集成cache(redis, cache, memorycache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 如何去模拟一个抽象基类   实际一般并不直接用abc,这里是为了举例和理解
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass


class RedisCache(CacheBase):
    # pass  # TypeError: Can't instantiate abstract class RedisCache with abstract methods get
    def get(self, key):
        pass


redis_cache = RedisCache()
redis_cache.get("key")
