#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/21 23:04'


# A Byte of Python -- Python3 -- P77

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print("I have", len(shoplist), 'items to purchase.')

print('These items are:', end=" ")
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
oldtime = shoplist[0]
del shoplist[0]
print('I bought the', oldtime)
print('My shopping list is now', shoplist)

