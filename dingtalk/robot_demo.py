# coding=utf-8
'''
DATE: 2020/09/11
AUTHOR: Yanxi Li
'''

import json
import requests

# ref: https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq

robot_token = "your_dingtalk_robot"

webhook = f'https://oapi.dingtalk.com/robot/send?access_token={robot_token}'
print(webhook)

dd_headers = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
}

dd_message = {
    "msgtype": "text",
    "text": {
        "content": '测试报告：Hello World by yx'  # content里要包含关键词
    }
}

r = requests.post(url=webhook, headers=dd_headers, data=json.dumps(dd_message))

print(r.json())
