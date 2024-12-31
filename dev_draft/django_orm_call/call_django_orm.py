#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/7 16:20'

"""
python脚本调用django orm映射的方法
http://blog.51cto.com/kexiaoke/2108517?utm_source=oschina-app

还是放在django项目下调试比较好
"""

import os
import sys
import django

# 定义django项目所在的路径
sys.path.append(r'/opt/CxOps/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CxOps.settings')
django.setup()

#测试settings文件是否可以import
#from CxOps import settings
#print(settings.ROOT_URLCONF)

#import models，和在jdango里面写法一样了

