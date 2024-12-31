# coding=utf-8
# demo_socket_server_3.py文件
import select
import logging
import socket
import queue

'''
select模块
把上面非阻塞的服务端修改下，利用select模块的select方法对套接字对象进行监控；

# select.select(rlist, wlist, xlist[, timeout])

rlist：等待，直到可以开始读取
wlist：等待，直到可以开始写入
xlist：等待“异常情况”
可选的 timeout 参数以一个浮点数表示超时秒数

现在设定的socket对象虽然是非阻塞的，但是因为select方法的作用，使用起来好像和阻塞的没有什么区别，是因为select把socket监控起来

rlist, wlist, xlist = select.select(self.inputlist, self.outputlist, self.inputlist)

如果在inputlist，outpulist中有活动的socket对象就会返回在rlist,wlist,xlist中；然后循环调用每个list去完成逻辑处理。
该方法同样是可以在单线程模式下实现服务端对多个客户端之间进行通信；

客户端代码同：demo_socket_server_3_select.py

https://blog.csdn.net/xiaomage0511/article/details/122104873
'''

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
        self.inputlist = list()
        self.outputlist = list()
        # 存放客户端发送过来的数据
        self.msg_dict = dict()

    def start_server(self):
        with self.__TCP_SOCKET as sock:
            sock.bind(self.ADDR)
            sock.listen()
            logger.info("Server is Running")
            # 将套接字对象添加到列表中
            self.inputlist.append(sock)
            while True:
                rlist, wlist, xlist = select.select(
                    self.inputlist, self.outputlist, self.inputlist)
                for r_conn in rlist:
                    # 如果套接字对象是self.__TCP_SOCKET；表示有新的连接进来了需要接受
                    if r_conn is sock:
                        conn, addr = r_conn.accept()
                        logger.info(f"{addr} 已连接")
                        # 和连接的客户端打个招呼
                        conn.sendall(f"Hi,{addr}".encode("utf-8"))
                        # 设置为非阻塞
                        conn.setblocking(False)
                        # 将新的连接添加到套接字对象列表进行监控
                        self.inputlist.append(conn)
                        # 每接受一个连接： 将连接作为键，一个空队列作为值
                        self.msg_dict[conn] = queue.Queue()
                    # 否则 是已经建立的连接发送过来数据了 需要接受数据
                    else:
                        client_addr = r_conn.getpeername()
                        try:
                            recv_data = r_conn.recv(1024)
                            # 如果有数据 接收；数据存储，将该连接添加到self.outputlist准备下一步发送数据
                            if recv_data and recv_data.decode("utf-8") != "quit":
                                logger.info(
                                    f"接收到来自 {client_addr} 的数据:{recv_data.decode('utf-8')}")
                                # msg_dict: 连接为 字典键  接收到的数据放到队列 为 字典值
                                self.msg_dict[r_conn].put(recv_data)
                                if r_conn not in self.outputlist:
                                    self.outputlist.append(r_conn)
                            # 否则 证明该连接已经断开了
                            else:
                                logger.info(f"{client_addr} 已断开")
                                # 执行清除
                                self.clear_conn(r_conn)
                        except ConnectionResetError as e:
                            # 捕获 ConnectionResetError 表示 客户端断开
                            logger.info(f"{client_addr} 异常断开")
                            # 执行清除
                            self.clear_conn(r_conn)
                for w_conn in wlist:
                    try:
                        if w_conn in self.msg_dict:
                            msg = self.msg_dict[w_conn].get(False)
                    except queue.Empty as e:
                        # 数据队列为空表示 该连接没有发送数据 服务端没有接收到
                        pass
                    else:
                        try:
                            w_conn.sendall(b'From Server ' + msg)
                        except ConnectionResetError as e:
                            # 捕获ConnectionResetError 客户端断开 执行清除
                            self.clear_conn(w_conn)

                for e_conn in xlist:
                    e_conn.close()
                    # 执行清除
                    self.clear_conn(e_conn)

    def clear_conn(self, conn):
        """清除已经断开的连接"""
        if conn in self.inputlist:
            self.inputlist.remove(conn)
        if conn in self.outputlist:
            self.outputlist.remove(conn)
        if conn in self.msg_dict:
            del self.msg_dict[conn]


if __name__ == '__main__':
    ServerClass().start_server()
