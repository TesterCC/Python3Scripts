# coding:utf-8
# !/usr/bin/env python


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


print(enroll('Lily', 'F'))
print(enroll('Tom', 'M', city='Shenzhen'))
print(enroll('Eric', 'M', 20))
