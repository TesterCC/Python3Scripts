import logging
import time
import socket
import threading


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s>%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)


class ClientClass(object):
    """docstring for ClientClass"""

    def __init__(self):
        self.__HOST = "127.0.0.1"
        self.__PORT = 9999
        self.__ADDR = (self.__HOST, self.__PORT)
        self.__TCP_SOCKET = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_STREAM)

    def start_client(self):
        """启动客户端"""
        with self.__TCP_SOCKET as sock:
            # 链接服务端地址
            sock.connect(self.__ADDR)
            logger.info("%s" % sock.recv(1024).decode("utf-8"))
            recv_t = threading.Thread(
                target=self.recv_data, args=(sock,))
            # 向服务端发送数据
            send_t = threading.Thread(
                target=self.send_data, args=(sock,))
            # 接收数据线程设置为守护线程
            recv_t.setDaemon(True)
            recv_t.start()
            send_t.start()
            send_t.join()

    def send_data(self, sock):
        while True:
            send_data = input()
            sock.sendall(send_data.encode("utf-8"))
            # 如果输入 quit 或者 exit 断开连接
            if send_data in "quit":
                logger.info("正在退出...")
                break

    def recv_data(self, sock):
        while True:
            try:
                recv_data = sock.recv(1024).decode("utf-8")
                logger.info(recv_data)
            except Exception as e:
                pass
                # logger.error(e, exc_info=True)
                time.sleep(0.5)
                break


if __name__ == '__main__':
    ClientClass().start_client()
