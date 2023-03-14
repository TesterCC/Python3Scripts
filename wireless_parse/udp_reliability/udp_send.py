import socket
from os.path import basename
from threading import Thread, Event
from time import sleep

BUFFER_SIZE = 32 * 1024

# 要发送的文件和接收端地址
fn_path = ""
address = ("192.168.100.3", 9999)

'''
功能描述：

使用UDP协议传输文件，在应用层实现可靠传输，避免传输层不保序和可能丢包造成的不可靠传输问题。

基本思路：

在发送端使用一个线程把要发送的内容进行分块传输，发送时携带每个分块的序号，同时使用另外一个线程接收对方的确认信息，如果所有分块都得到对方的确认，停止传输。

在接收端对收到的每个分块进行确认，把每个分块临时存储在缓冲区中，全部分块接收完成之后按序号进行排序，最后写入文件。

ref:
https://mp.weixin.qq.com/s/Js1nmaF70lculpMFOxGLaA
'''

# 存放每块数据在文件中的起点

positions = []
file_name = [f'{basename(fn_path)}'.encode()]


def sendto(fn_path):
    """发送文件的线程函数"""
    # read file
    with open(fn_path, 'rb') as fp:
        content = fp.read()

    # 获取文件大小，做好分块传输的准备
    fn_size = len(content)
    for start in range(fn_size // BUFFER_SIZE + 1):
        positions.append(start * BUFFER_SIZE)

    # 设置事件，可以启动用来接收确认信息的线程。
    e.set()

    # 窗口套接字，设置发送缓冲区大小
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER_SIZE)

    # 发送文件数据，直到所有分块都收到确认，否则就不停地循环发送 todo 这里要改成重发N次就取消
    while positions:
        for pos in positions:
            sock.sendto(f"{pos}_".encode() + content[pos:pos + BUFFER_SIZE], address)
        sleep(0.1)

    # notice send finish
    while file_name:
        sock.sendto(b'over_' + file_name[0], address)

    sock.close()


def recv_ack():
    """用来接收确认信息的线程函数"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 7788))

    # 如果所有分块都确认过，就结束循环
    while positions:
        # 预期收到确认包1234_ack
        data, _ = sock.recvfrom(1024)
        pos = int(data.split(b'_')[0])
        if pos in positions:
            positions.remove(pos)

    # 确认对方收到文件名，并已接收全部数据
    while file_name:
        data, _ = sock.recvfrom(1024)
        fn = data.split(b'_')[0]
        if fn in file_name:
            file_name.remove(fn)
    sock.close()


if __name__ == '__main__':
    t1=Thread(target=sendto,args=(fn_path,))
    t1.start()

    e = Event()
    e.clear()
    e.wait()

    t2 = Thread(target=recv_ack)
    t2.start()

    # 等待发送线程和接收确认线程都结束
    t2.join()
    t1.join()

