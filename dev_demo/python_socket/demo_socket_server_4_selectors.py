import selectors
import logging
import socket

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s>%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)

'''
selectors模块
selectors模块是高级 I/O 复用库，它建立在 select 模块原型的基础之上。Python文档推荐用户改用此模块。

# 默认的选择器类，使用当前平台上可用的最高效选择器的实现

比select模块的select方法更简洁一些；

PS:比较接近生成环境，但看具体需求

ref:
https://blog.csdn.net/xiaomage0511/article/details/122104873
'''


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
        self.sele = selectors.DefaultSelector()

    def start_server(self):
        with self.__TCP_SOCKET as sock:
            sock.bind(self.ADDR)
            sock.listen()
            logger.info("Server is Running")
            self.sele.register(
                sock, selectors.EVENT_READ, self.accept_conn)
            while True:
                events = self.sele.select()
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)

    def accept_conn(self, sock, mask):
        conn, addr = sock.accept()
        logger.info(f"{addr} 已连接")
        conn.sendall(f"Hi,{addr}".encode("utf-8"))
        conn.setblocking(False)
        self.sele.register(conn, selectors.EVENT_READ, self.read)

    def read(self, conn, mask):
        try:
            client_addr = conn.getpeername()
            recv_data = conn.recv(1024)
            if recv_data and recv_data.decode("utf-8") != "quit":
                logger.info(
                    f"接收到来自 {client_addr} 的数据:{recv_data.decode('utf-8')}")
                conn.sendall(b'From Server ' + recv_data)
            else:
                logger.info(f"{client_addr} 已断开")
                self.sele.unregister(conn)
        except ConnectionResetError as e:
            logger.info(f"{client_addr} 异常断开")
            self.sele.unregister(conn)
            conn.close()


if __name__ == '__main__':
    ServerClass().start_server()
