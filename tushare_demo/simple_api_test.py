#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-12 11:47'


import tushare as ts    # need pip install bs4

# get version
print(ts.__version__)


# data = ts.get_h_data('600166')
data = ts.get_k_data(code='600166')   # pandas.core.frame.DataFrame

# use ipython or jupyter is better
print(type(data))   # pandas.core.frame.DataFrame
print(data)

