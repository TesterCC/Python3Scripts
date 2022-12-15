# -*- coding: utf-8 -*-
import socket
import selectors

# ref: https://www.cnblogs.com/xiao-apple36/p/8683198.html
# 注册一个epoll事件
# 1. socket
# 2.事件可读
# 3.回调函数 把一个函数当成变量传到函数里

def receive_data(conn):
    data = conn.recv(1024)

    if data:
        print('接收的数据是：%s' % data.decode())
        conn.send(data)
    else:
        e_poll.unregister(conn)
        conn.close()


def accept_conn(p_server):
    conn, addr = p_server.accept()
    print('Connected by', addr)
    # 也有注册一个epoll
    e_poll.register(conn, selectors.EVENT_READ, receive_data)


CONN_ADDR = ('0.0.0.0', 9999)
server = socket.socket()
server.bind(CONN_ADDR)
server.listen(5)

# 生成一个epoll选择器实例 I/O多路复用，监控多个socket连接
e_poll = selectors.EpollSelector()  # window没有epoll使用selectors.DefaultSelector()实现多路复用
e_poll.register(server, selectors.EVENT_READ, accept_conn)

# 事件循环
while True:
    # 事件循环不断地调用select获取被激活的socket
    events = e_poll.select()
    # print(events)
    """[(SelectorKey(fileobj= < socket.socket
     laddr = ('127.0.0.1',9999) >,……data = < function acc_conn at 0xb71b96ec >), 1)]
    """
    for key, mask in events:
        call_back = key.data
        # print(key.data)
        call_back(key.fileobj)
