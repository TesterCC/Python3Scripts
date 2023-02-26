#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import socket
from datetime import datetime
from uuid import getnode
import urllib

try:
    import urllib2
except Exception:
    from urllib import request as urllib2
try:
    import Cookie as cookies
except Exception:
    from http import cookies
import websocket


'''
# https://zohead.com/archives/wholeton-linux-client/
~$ pip install websocket-client==0.59.0
'''

wholeton_host = os.environ.get("HHOST")
wholeton_user = os.environ.get("HNAME")
wholeton_pass = os.environ.get("HPASSWD")
wholeton_ip = ''    # # run as Administrator, and manual set system environment vars
wholeton_mac = ''   # can ignore, if get can
update_secs = 32400


def url_encode(obj):
    try:
        return urllib.urlencode(obj)
    except Exception:
        return urllib.parse.urlencode(obj)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def get_mac():
    return ':'.join(("%012x" % getnode())[i:i + 2] for i in range(0, 12, 2))


if not wholeton_ip:
    wholeton_ip = get_ip()
    print(f"[D] wholeton_ip: {wholeton_ip}")

if not wholeton_mac:
    wholeton_mac = get_mac()

uri_keys = {'id': 0, 'url': 'http://www.wholeton.com/', 'user': wholeton_ip, 'mac': wholeton_mac}
uri_data = url_encode(uri_keys).replace('%3A', ':')

auth_data = url_encode(
    {'param[UserName]': wholeton_user, 'param[UserPswd]': wholeton_pass, 'uri': uri_data, 'force': 0})
# convert for python 3
if sys.version_info[0] == 3:
    auth_data = auth_data.encode('ascii')

ws = None

try:
    while True:
        resp = urllib2.urlopen('http://' + wholeton_host + '/user-login-auth?' + uri_data, timeout=5, data=auth_data)

        # get session cookie
        cookie = cookies.SimpleCookie()
        cookie.load(resp.info()['Set-Cookie'])

        resp_data = resp.read()
        if resp_data:
            print('Login response:')
            print(resp_data)

        ws = websocket.WebSocket()
        ws.connect('ws://' + wholeton_host + '/go-ws/user-auth',
                   cookie='fms_session=' + cookie.get('fms_session').value, origin='http://' + wholeton_host)

        dt_start = datetime.now()
        while ws:
            ws_data = ws.recv()
            if ws_data:
                dt_now = datetime.now()
                if (dt_now - dt_start).seconds >= update_secs:
                    break
                print(dt_now)
                print(ws_data)

        if ws:
            ws.close()
        ws = None
except KeyboardInterrupt:
    pass

if ws:
    ws.close()