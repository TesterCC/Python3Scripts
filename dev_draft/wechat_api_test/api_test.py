#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/22 11:29'

import requests
import json


class WechatUtils(object):
    '''
    https://note.youdao.com/web/#/file/WEB719bb051c4b63b56021001b824678622/note/WEBafaf35fade771eb1ac9e6783b00fa312/
    '''

    def __init__(self):
        self.appid = ''
        self.secret = ''

        self.login_payload = {
            'grant_type': 'client_credential',
            'appid': self.appid,
            'secret': self.secret,
        }

    def get_access_token(self):
        '''
        获取微信公众号access_token
        '''

        url = 'https://api.weixin.qq.com/cgi-bin/token'


        r = requests.get(url, params=self.login_payload)
        #print(type(r.content))   # byte
        # print(type(r.text))     # str

        ret = json.loads(r.text)
        print(ret)
        # print(type(ret))   # dict
        return ret['access_token']

    def customer_service_reply_media(self, access_token, user_openid="oPbHyt4UFfQdOANBjVfjmGWaJZOo", media_id="JhATcpoBjhxv4YjstgraFBWO4d6oBejwDdPMYgq7v6DrFHnGc_oizGQtA9e36xwm"):
        url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(access_token)

        data = {
            "touser": user_openid,
            "msgtype": "image",
            "image": {
                "media_id": media_id,
            }
        }

        r = requests.post(url, data=json.dumps(data))
        print(r.text)

    def main(self):
        pass


if __name__ == '__main__':
    wu = WechatUtils()

    # Test get access_token
    access_token = wu.get_access_token()
    print(access_token)

    # Test auto custom reply info.
    req = wu.customer_service_reply_media(access_token)


