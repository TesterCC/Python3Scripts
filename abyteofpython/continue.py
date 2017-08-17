#!/usr/bin/env python
# coding=utf-8

# A Byte of Python -- P56-57 -- Python3


while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')