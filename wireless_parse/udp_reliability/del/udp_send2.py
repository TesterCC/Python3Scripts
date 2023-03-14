import socket
import os
import hashlib


def send_file(file_name, ip, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(1)
    udp_socket.connect((ip, port))

    buffer_size = 1024  # 定义缓冲区大小
    file_size = os.path.getsize(file_name)  # 获取文件大小
    fp = open(file_name, 'rb')  # 以读形式打开文件

    # 文件名、文件大小和文件校验和
    udp_socket.sendto((file_name + ':' + str(file_size)
                       + ':' + md5(file_name)).encode('utf-8'), (ip, port))

    # 接收反馈，表示对方已经准备好接收文件
    try:
        feedback = udp_socket.recvfrom(buffer_size)
    except socket.timeout:
        udp_socket.close()
        print('等待超时，接收方已关闭。')
        return

    # 开始发送文件
    while True:
        data = fp.read(buffer_size)
        if not data:
            break
        udp_socket.sendto(data, (ip, port))
        # 接收对方反馈
        try:
            feedback = udp_socket.recvfrom(buffer_size)
        except socket.timeout:
            udp_socket.sendto(data, (ip, port))  # 发送文件数据
            continue
        if feedback[0].decode('utf-8') != 'ACK':
            udp_socket.sendto(data, (ip, port))

    fp.close()
    udp_socket.sendto('FINISHED'.encode('utf-8'), (ip, port))  # 发送结束信号
    udp_socket.close()
    print('传输完成。')


def md5(file_name):
    m = hashlib.md5()
    with open(file_name, 'rb') as f:
        data = f.read()
        m.update(data)
    return m.hexdigest()


if __name__ == '__main__':
    file_name = input('请输入要发送的文件名：')
    ip = input('请输入接收方IP地址：')
    port = int(input('请输入接收方端口号：'))
    send_file(file_name, ip, port)
