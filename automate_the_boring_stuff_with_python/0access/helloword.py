#!/usr/bin/env python
#coding=utf-8

'''
Python编程快速上手--让繁琐工作自动化
preface P3
'''
passwordFile = open('SecretPasswordFile.txt')

secretPassword = passwordFile.read()

print('Enter your password:')

typedPassword = input()    # raw_input() is abandon

if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '123456':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied.')