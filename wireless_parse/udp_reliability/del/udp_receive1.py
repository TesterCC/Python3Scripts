import os
import socket


def receive_file(save_dir, addr, timeout=1):
    byte_size = 4096  # 每次传输的字节数
    seq_num = 0  # 序号
    ack_num = 0  # 确认号
    buffer = b''  # 缓存
    receive_buffer = [None] * ((os.path.getsize(save_dir) + byte_size - 1) // byte_size)

    # 建立UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addr)
    # sock.settimeout(timeout)

    # 接收文件名和文件大小
    file_name, _ = sock.recvfrom(byte_size)
    file_size, _ = sock.recvfrom(byte_size)
    file_size = int(file_size.decode())

    with open(save_dir, 'wb') as f:
        while True:
            # 发送确认
            sock.sendto(str(ack_num).encode(), addr)

            # 接收数据
            try:
                receive_data, _ = sock.recvfrom(byte_size + 6)
                seq_num = int(receive_data[:6].decode())
            except socket.timeout:
                continue

            # 缓存数据
            if seq_num == ack_num:
                buffer += receive_data[6:]
                ack_num += 1
                while receive_buffer and receive_buffer[0] is not None:
                    f.write(receive_buffer.pop(0))
                f.write(buffer)
                buffer = b''
            elif seq_num > ack_num:
                receive_buffer[seq_num - ack_num - 1] = receive_data[6:]

            # 结束传输
            if ack_num == (file_size + byte_size - 1) // byte_size:
                break

    sock.close()


if __name__ == '__main__':
    save_dir = "./testa.txt"
    addr = ("192.168.100.3", 9999)
    receive_file(save_dir, addr)
