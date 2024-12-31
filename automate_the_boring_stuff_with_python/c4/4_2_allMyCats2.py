#!/usr/bin/env python
#coding=utf-8


catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.): ')
    name = input()    # input 'text'
    if name == '':
        break
    catNames = catNames + [name]   # list concatenation

print('The cat names are: ')
for name in catNames:
    print('  ' + name)

