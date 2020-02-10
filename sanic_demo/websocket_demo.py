#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-02-10 17:10'


'''
WebSocket
Sanic provides an easy to use abstraction on top of websockets. Sanic Supports websocket versions 7 and 8.

REF:
https://sanic.readthedocs.io/en/latest/sanic/websocket.html
'''

from sanic import Sanic
from sanic.response import json
from sanic.websocket import WebSocketProtocol

app = Sanic()


@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'hello! This is Sanic.'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)

# app.add_websocket_route(feed, '/feed')   # 不用装饰器的话用这个注册

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, protocol=WebSocketProtocol)
    # 前端ws请求地址：ws://localhost:8000/feed