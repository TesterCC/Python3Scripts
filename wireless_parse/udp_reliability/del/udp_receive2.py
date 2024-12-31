import socket
import os
import hashlib

def receive_file(ip, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((ip, port))
    udp_socket.settimeout(5)

    buffer_size = 1024     # 定义缓冲区大小

    while True:
        try:
            # 接收发送方发送的文件信息（文件名、文件大小和校验值）
            data, addr = udp_socket.recvfrom(buffer_size)
            file_name, file_size, file_md5 = data.decode('utf-8').split(':')
            file_size = int(file_size)
            file_path = os.path.join(os.getcwd(), 'files')

            # 创建文件目录
            if not os.path.exists(file_path):
                os.mkdir(file_path)

            # 打开文件
            fp = open(os.path.join(file_path, file_name), 'wb')
            udp_socket.sendto('ACK'.encode('utf-8'), addr)

            # 接收文件数据
            try_times = 0
            while True:
                data, addr = udp_socket.recvfrom(buffer_size)
                if data.decode('utf-8') == 'FINISHED':
                    break
                fp.write(data)

                # 发送确认信息
                udp_socket.sendto('ACK'.encode('utf-8'), addr)
                try_times = 0

            fp.close()
            # 校验文件
            if md5(os.path.join(file_path, file_name)) == file_md5:
                print('文件{}接收成功。'.format(file_name))
            else:
                print('文件{}接收失败，校验和不正确。'.format(file_name))
        except socket.timeout:
            print('等待超时，停止接收。')
            break

    udp_socket.close()

def md5(file_name):
    m = hashlib.md5()
    with open(file_name, 'rb') as f:
        data = f.read()
        m.update(data)
    return m.hexdigest()

if __name__ == '__main__':
    ip = input('请输入本机IP地址：')
    port = int(input('请输入端口号：'))
    receive_file(ip, port)
