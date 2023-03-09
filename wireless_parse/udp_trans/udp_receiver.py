import socket
import tqdm
import os
import threading


# 使用UDP传输视频，全双工，但只需一方接，一方收即可

# 设置服务器的ip和 port
# 服务器信息
# sever_host = '127.0.0.1'
# sever_port =1234

def recvived(address, port):
    # 传输数据间隔符
    SEPARATOR = '<SEPARATOR>'
    # 文件缓冲区
    Buffersize = 4096 * 10

    while True:
        print('准备接收新的文件...')

        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((address, port))
        recv_data = udp_socket.recvfrom(Buffersize)
        recv_file_info = recv_data[0].decode('utf-8')  # 存储接收到的数据,文件名
        print(f'接收到的文件信息{recv_file_info}')
        c_address = recv_data[1]  # 存储客户的地址信息
        # 打印客户端ip
        print(f'客户端{c_address}连接')
        # recv_data = udp_socket.recv()
        # 接收客户端信息
        # received = udp_socket.recvfrom(Buffersize).decode()
        filename, file_size = recv_file_info.split(SEPARATOR)
        # 获取文件的名字,大小
        filename = os.path.basename(filename)
        file_size = int(file_size)

        # 文件接收处理
        progress = tqdm.tqdm(range(file_size), f'接收{filename}', unit='B', unit_divisor=1024, unit_scale=True)

        with open(f'8_18_' + filename, 'wb') as f:
            for _ in progress:
                # 从客户端读取数据

                bytes_read = udp_socket.recv(Buffersize)
                # 如果没有数据传输内容
                # print(bytes_read)
                if bytes_read == b'file_download_exit':
                    print('完成传输！')
                    print(bytes_read)
                    break
                # 读取写入
                f.write(bytes_read)
                # 更新进度条
                progress.update(len(bytes_read))
        udp_socket.close()


if __name__ == '__main__':
    # address = ("127.0.0.1", 1234)
    port = 4321
    address = "127.0.0.1"
    t = threading.Thread(target=recvived, args=(address, port))
    t.start()
    # send(address)
