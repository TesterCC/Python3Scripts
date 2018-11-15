#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/15 09:35'

import redis

from functools import wraps
import pickle as cPickle
from redis.connection import ConnectionError


redis_config = {}


POOL = redis.ConnectionPool(host=redis_config.get('host', '127.0.0.1'),
        port=redis_config.get('port', '6379'),
        password=redis_config.get('password', 'YourRedisPassword'),
        db=redis_config.get('db', '0'),
        )


class Redis:
    def __init__(self):
        self.r = redis.StrictRedis(connection_pool=POOL)

    def set(self, key, value, timeout=3600):
        '''
        store value if value is an object.
        '''
        pickled_value = cPickle.dumps(value)
        self.r.setex(key, timeout, pickled_value)

    def get(self, key):
        '''
        get plain string
        @param key: str
        @rtype: object or string
        '''
        try:
            value = self.r.get(key)
            try:
                unpickle_value = cPickle.loads(value)
                return unpickle_value
            except cPickle.UnpicklingError:
                return value
            except TypeError:
                return value
        except ConnectionError:
            return None
        except Exception as e:
            print(e)
            return None

    def delete(self, key):
        """
        delete a key-value by key
        @rtype: boolean
        """
        return self.r.delete(key)


cache = Redis()


def cache_method(cache_time):
    def decorate(func):
        cache_key_prefix = 'wxm' + func.__name__ + '_'
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            cache_key = cache_key_prefix + '_'.join(str(arg) for arg in args) + '_'.join(str(v) for v in kwargs.values())
            cache_value = cache.get(cache_key)
            if cache_value:
                return cache_value
            func_value = func(self, *args, **kwargs)
            cache.set(cache_key, func_value, cache_time)
            return func_value
        return wrapper
    return decorate


def cache_func(cache_time):
    def decorate(func):
        cache_key_prefix = 'wxf' + func.__name__ + '_'
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = cache_key_prefix + '_'.join(str(arg) for arg in args) + '_'.join(str(v) for v in kwargs.values())
            cache_value = cache.get(cache_key)
            if cache_value:
                return cache_value
            func_value = func(*args, **kwargs)
            cache.set(cache_key, func_value, cache_time)
            return func_value
        return wrapper
    return decorate