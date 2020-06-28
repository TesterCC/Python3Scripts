#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/28 01:06'

import uuid

"""
If all you want is a unique ID, you should probably call uuid1() or uuid4().
Note that uuid1() may compromise privacy since it creates a UUID containing
the computer's network address.  uuid4() creates a random UUID.
"""

print(uuid.uuid1())   # may compromise privacy
print(uuid.uuid1().hex)   # may compromise privacy
print(uuid.uuid4())
print(uuid.uuid4().hex)   # recommend