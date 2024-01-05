#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-03-11 18:29'

import jwt
import datetime
from jwt import exceptions

# ref: https://jwt.io/ jwt揭秘

SALT = '@#$$2423523lkjklad#@#$_32344'
print(f"SALT length: {len(SALT)}")


def create_token():
    # build header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }

    # build payload
    payload = {
        'user_id': 10,
        'user_name': 'Test',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    }

    # payload = {
    #     "code": 0,
    #     "msg": "success",
    #     "Data": {
    #         "exp": 1584180854,
    #         "iss": "test",
    #         "user_id": "T25pb246MTc=",
    #         "role_id": "xxxxxx",
    #         "role_type": "SysAdmin",
    #         "name": "Tester001",
    #         "phone": "13*****3020"
    #     }
    # }

    result = jwt.encode(payload, key=SALT, algorithm="HS256", headers=headers).decode('utf-8')
    return result


if __name__ == '__main__':
    token = create_token()

    print(f"generate token length:{len(token)}")  # HS256 150+
    print(f'Token is:\n{token}')
