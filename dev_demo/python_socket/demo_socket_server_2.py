# coding=utf-8

import logging
import socket

'''
# https://blog.csdn.net/xiaomage0511/article/details/122104873

# 在非阻塞模式下可以实现在单线程模式下实现与多个客户端连接的交互
# 服务端不需要多开启进程或者线程就可以实现与多个客户端之间通信

服务端非阻塞模式的情况下 主要通过循环控制不停的去捕获BlockingIOError 异常来判断是否有新的连接进来，或者是是否有数据可以接受到；该情况下CPU的使用率会很高

'''

# demo_socket_server_2.py
# 非阻塞模式的服务端

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s>%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)


class ServerClass(object):
    """docstring for ServerClass"""

    def __init__(self):
        self.__HOST = "127.0.0.1"
        self.__PORT = 9999
        self.ADDR = (self.__HOST, self.__PORT)
        self.__TCP_SOCKET = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_STREAM)
        # 设置非阻塞
        # self.__TCP_SOCKET.setblocking(False)
        self.__TCP_SOCKET.settimeout(0.0)
        # 用来存放套接字对象的列表
        self.connlist = list()

    def start_server(self):
        with self.__TCP_SOCKET as sock:
            sock.bind(self.ADDR)
            sock.listen()
            logger.info("Server is Running")
            while True:
                try:
                    conn, addr = sock.accept()
                    # logger.info(conn)
                    # 将连接的套接字对象设置为非阻塞
                    conn.setblocking(False)
                    msg = f"Hi,{addr}"
                    self.send_data(conn, msg)
                    # 添加到列表
                    self.connlist.append(conn)
                # 如果没有连接进来需要捕获BlockingIOError异常
                except BlockingIOError as e:
                    pass
                    # logger.debug("没有新的客户端连接")
                # 循环套接字对象列表 进行收发数据
                for conn in self.connlist:
                    msg = self.recv_data(conn)
                    self.send_data(conn, msg)

    def recv_data(self, conn):
        """接收数据"""
        try:
            msg = conn.recv(1024).decode("utf-8")
            if not msg or msg in ["quit"]:
                logger.debug("断开连接")
                # 将套接字对象从列表移除
                self.connlist.remove(conn)
            else:
                logger.info(msg)
                return msg
        except IOError as e:
            pass
            # logger.debug("没有接收到数据")

    def send_data(self, conn, msg):
        """发送数据"""
        if msg:
            msg = f"From Server {msg}"
            try:
                conn.sendall(msg.encode("utf-8"))
            except ConnectionResetError as e:
                pass
                logger.debug("连接已断开，无法再发送信息")


if __name__ == '__main__':
    ServerClass().start_server()
