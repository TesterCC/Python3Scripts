# coding=utf-8
'''
DATE: 2020/09/11
AUTHOR: Yanxi Li
'''

from websocket import create_connection

# 建立和WebSocket接口的链接
ws = create_connection("ws://echo.websocket.org")
# 打印日子
print("发送 'Hello, World'...")
# 发送Hello，World
ws.send("Hello, World, TEST")
# 将WebSocket的返回值存储result变量
result = ws.recv()
# 打印返回的result
print("返回"+result)
# 关闭WebSocket链接
ws.close()