#!/usr/bin/env python
# coding=utf-8

'''
Python编程快速上手
4.5 神奇8球和列表
'''


import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages)-1)])  # randint Return random integer in range [a, b], including both end points