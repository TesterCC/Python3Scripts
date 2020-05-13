#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-05-11 17:15'


import os

def module_path():
    """
    return the programs/file parent directory
    """
    return os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    print(module_path())