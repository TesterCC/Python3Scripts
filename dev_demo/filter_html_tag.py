# coding=utf-8
'''
DATE: 2020/09/25
AUTHOR: Yanxi Li
'''

import re

# 正则过滤str中的html tag
# str = "<img /><a>srcd</a>hello</br><br/>"
str = "<img /><a>test测试</a>hello</br><br/>"
str = re.sub(r'</?\w+[^>]*>', '', str)
print(str)


