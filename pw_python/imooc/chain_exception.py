#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-25 15:40'


# Chained Exceptions

import shutil

def mycopy(source, dest):
    try:
        shutil.copy2(source,dest)
    except OSError:   # python2里raise会丢失原来的traceback信息
        raise NotImplementedError("automatic sudo injection") from OSError    # python3 raise from保留异常栈信息
mycopy('old','new')