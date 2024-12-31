#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/9 13:39'


# try except finally
def exe_try():
    try:
        print("code started")
        raise KeyError
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else:
        print("other error")
        return 3
    finally:  # rasie Except后会直接走到finally
        print("finally")
        return 4


if __name__ == '__main__':
    result = exe_try()
    print(result)
