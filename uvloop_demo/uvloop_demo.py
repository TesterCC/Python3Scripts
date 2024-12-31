#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 21:36'

"""
http://coyee.com/article/10773-uvloop-blazing-fast-python-networking

>= Python 3.5

https://uvloop.readthedocs.io/user/index.html
"""

import asyncio
import uvloop

# To make asyncio use the event loop provided by uvloop, you install the uvloop event loop policy
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


# Alternatively, you can create an instance of the loop manually
loop = uvloop.new_event_loop()
print(loop)
asyncio.set_event_loop(loop)
