#!/usr/bin/env python
# -*- coding:utf-8 -*-
import jwt
import datetime
from jwt import exceptions

# pip3 install pyjwt -i https://pypi.tuna.tsinghua.edu.cn/simple

JWT_SALT = 'iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv='
ALG = "HS256"

def create_token(payload, timeout=20):
    """
    :param payload:  例如：{'user_id':1,'username':'tester'}用户信息
    :param timeout: token的过期时间，默认20分钟
    :return:
    """
    headers = {
        'typ': 'jwt',
        'alg': ALG
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers)  #.decode('utf-8')  要注释，这个估计是python2的实现改的，不然报错，Python3 ‘str’ object has no attribute 'decode
    print(f"result:{result}")
    return result


def parse_payload(token):
    """
    对token进行和发行校验并获取payload
    :param token:
    :return:
    """
    result = {'status': False, 'data': None, 'error': None}
    print(f"token:{token}")
    try:
        verified_payload = jwt.decode(token, JWT_SALT, ALG)
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的token'
    return result
