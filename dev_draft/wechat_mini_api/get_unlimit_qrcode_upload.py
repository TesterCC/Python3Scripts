#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/13 14:53'


"""
For Manual Debug
https://mp.weixin.qq.com/debug

WeChat API Doc
https://developers.weixin.qq.com/miniprogram/dev/api/open-api/qr-code/getWXACodeUnlimit.html

接口B 无数量限制，但是必须传递scene
"""

import requests
import json
import time, datetime
import random

import upyun

from PIL import Image
from io import BytesIO

# from dev_draft.use_wx_token_by_redis.redis_cache import cache_method, cache_func

SECRET = ''
APPID = ''


# @cache_func(7200)    # 每次请求access_token过期是7200s=2hours  ，local_redis can use, but method need modify
def _get_wx_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'.format(appid=APPID, secret=SECRET)
    response = requests.get(url)
    if response:
        ret = json.loads(response.text)  # dict
        access_token = ret.get('access_token')
        if access_token:
            return access_token
        else:
            print(ret.get('errmsg'))
            return None
    else:
        print("Response doesn't exist")
        return None


def get_wx_qrcode_unlimit():
    """
    https://developers.weixin.qq.com/miniprogram/dev/api/open-api/qr-code/getWXACodeUnlimit.html
    """
    access_token = _get_wx_access_token()
    print(access_token)
    old_event_id = "1913199967"   # event.old_event_id

    if access_token:
        url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit?{}".format(access_token)

        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        querystring = {"access_token": access_token}

        payload = "{\"scene\": \"../event/event?id=%s\",\"page\": \"\",\"width\": 430,\"auto_color\": false,\"line_color\": {\"r\": \"0\",\"g\": \"0\",\"b\":\"0\"}}" % old_event_id

        try:
            res = requests.post(url, data=payload, params=querystring, headers=headers, timeout=10)

            # res.content图片字节流
            # i = Image.open(BytesIO(res.content))
            # i.show()
            return res.content

        except Exception as err:
            print(err)


def show_img():
    img_bytes = get_wx_qrcode_unlimit()

    # 本地打开查看采用，若是直接上传到服务器，可以直接用response.content
    # http://www.python-requests.org/en/master/user/quickstart/#response-content

    i = Image.open(BytesIO(img_bytes))

    print(i.format)   # JPEG

    i.show()

def upload_file_pic_by_ftp(img_bytes, spot='test'):
    '''
    用于上传详情页面的二维码
    '''

    import ftplib,time
    server1='v2.ftp.upyun.com'
    uid='eventpop/huodongjia-yun'
    pwd='wert@123'
    s = ftplib.FTP(server1, uid, pwd)
    try:
        s.cwd(spot)
    except ftplib.error_perm:
        s.mkd(spot)
    curTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    try:
        s.cwd(curTime)
    except ftplib.error_perm:
        s.mkd(curTime)
        try:
            s.cwd(curTime)
        except:
            pass

    img = Image.open(BytesIO(img_bytes))
    print(img.format.lower())

    # suffix = img.format.lower()   # 文件后缀
    suffix = "png"
    filename ="%s.%s" % (str(time.time()), suffix)

    url = 'http://pic.huodongjia.com/' + spot + '/' + curTime + '/' + filename
    print(url)
    return url


def upload_file_pic_by_http(file_obj, image_type="jpeg", directory='test'):
    '''
    use upyun sdk to upload file  -- please test before upload yx
    '''
    BUCKETNAME = ''
    USERNAME = ''
    PASSWORD = ''

    up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=20, endpoint=upyun.ED_AUTO)

    up.up_rest.endpoint = upyun.ED_AUTO

    sub_directory = datetime.date.strftime(datetime.date.today(),
                                           '%Y-%m-%d')
    server_directory = directory + '/' + sub_directory + '/'
    suffix = "." + image_type

    print("Server directory is {}".format(server_directory))

    upload_filename = str(time.time()) + str(random.randint(0, 9999)) + suffix

    try:
        up.put(server_directory + upload_filename, file_obj)
    except upyun.UpYunServiceException as se:
        # log.error('Except an UpYunServiceException ...')
        # log.error('Request Id: ' + se.request_id)
        # log.erorr('HTTP Status Code: ' + str(se.status))
        # log.error('Error Message:    ' + se.msg + '\n')
        print('Error Message:    ' + se.msg + '\n')
    except upyun.UpYunClientException as ce:
        # log.error('Except an UpYunClientException ...')
        # log.error('Error Message: ' + ce.msg + '\n')
        print('Error Message: ' + ce.msg + '\n')
    else:
        # log.info(self.IMAGE_DOMAIN + server_directory + upload_filename)
        print('https://pic.huodongjia.com/' + server_directory + upload_filename)
        return 'https://pic.huodongjia.com/' + server_directory + upload_filename


def upload_return_imgurl():
    img_bytes = get_wx_qrcode_unlimit()
    # ret = upload_file_pic_by_ftp(img_bytes)

    img = Image.open(BytesIO(img_bytes))
    img_type = img.format.lower()
    print(img_type)
    ret_url = upload_file_pic_by_http(img_bytes, image_type=img_type, directory='event_detail_qrcode')
    # ret_url = upload_file_pic_by_http(img_bytes, directory='event_detail_qrcode')

    return ret_url


if __name__ == '__main__':
    # print(_get_wx_access_token())
    # get_wx_qrcode_unlimit()

    ts = time.time()
    # show_img()
    upload_return_imgurl()
    te = time.time()

    print(te-ts)

