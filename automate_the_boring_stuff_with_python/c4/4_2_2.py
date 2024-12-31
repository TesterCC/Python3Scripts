#!/usr/bin/env python
#coding=utf-8

myPets = ['Zophie', 'Pooka', 'Fai-tail']

print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I do not have a pet named '+name+'.')
else:
    print(name + ' is my pet.')