#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/12 13:29'

"""
https://stackoverflow.com/questions/9733638/post-json-using-python-requests
http://docs.python-requests.org/en/master/user/quickstart/#more-complicated-post-requests
"""

# For example, the GitHub API v3 accepts JSON-Encoded POST/PATCH data

import json
import requests

url = 'http://httpbin.org/post'

payload = {'some': 'data'}

r = requests.post(url, data=payload)

print(r.headers)
print(r.headers.get("Content-Type"))
print(r.status_code)
print(r.content)

print("--" * 40)

r1 = requests.post(url, data=json.dumps(payload))

print(r1.headers)
print(r1.headers.get("Content-Type"))
print(r1.status_code)
print(r1.content)

print("--" * 40)
# Instead of encoding the dict yourself, you can also pass it directly using the json parameter (added in version 2.4.2) and it will be encoded automatically

r2 = requests.post(url, json=payload)  # recommend

print(r2.headers)
print(r2.headers.get("Content-Type"))
print(r2.status_code)
print(r2.content)

# Note, the json parameter is ignored if either data or files is passed.
# Using the json parameter in the request will change the Content-Type in the header to application/json.
# 注意response的content-type
