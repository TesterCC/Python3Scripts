#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/12/3 21:56'


class UserModel(object):

    users = {
        1: {'name': 'Zack', 'age': 10},
        2: {'name': 'White', 'age': 12},
        3: {'name': 'Lily', 'age': 20},
        4: {'name': 'Zoe', 'age': 30},
    }

    @classmethod
    def get(cls, user_id):
        return cls.users[user_id]

    @classmethod
    def get_all(cls):
        return list(cls.users.values())

    @classmethod
    def create(cls, name, age):
        user_dict = {'name': name, 'age': int(age)}
        max_id = max(cls.users.keys()) + 1
        cls.users[max_id] = user_dict

    @classmethod
    def update(cls, user_id, age):
        cls.users[user_id]["age"] = int(age)

    @classmethod
    def delete(cls, user_id):
        if user_id in cls.users:
            return cls.users.pop(user_id)
        else:
            return "User isn't existed."




