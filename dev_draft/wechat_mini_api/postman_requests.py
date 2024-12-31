#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/13 17:37'

from PIL import Image
from io import BytesIO

import requests

url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit"

querystring = {"access_token": "15_awQxxxxxxxxxxxxxxxxxxxxxxxx"}

payload = "{\n\t\"scene\": \"../event/event?id=1913199967\",\n\t\"page\": \"\",\n\t\"width\": 430,\n\t\"auto_color\": false,\n\t\"line_color\": {\n\t\t\"r\": \"0\",\n\t\t\"g\": \"0\",\n\t\t\"b\": \"0\"\n\t}\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(type(response.content))

# 本地打开查看采用，若是直接上传到服务器，可以直接用response.content
# http://www.python-requests.org/en/master/user/quickstart/#response-content
i = Image.open(BytesIO(response.content))
i.show()

# 直接上传upyun






