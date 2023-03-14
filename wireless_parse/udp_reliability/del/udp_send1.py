import os
import socket


def send_file(file_path, addr, timeout=1):
    byte_size = 4096  # 每次传输的字节数
    seq_num = 0  # 序号
    ack_num = 0  # 确认号
    window_size = 4  # 窗口大小
    buffer = []  # 缓存

    # 建立UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)

    # 发送文件前，先发送文件名和文件大小
    file_name = os.path.basename(file_path).encode()
    file_size = os.path.getsize(file_path)
    sock.sendto(file_name, addr)
    sock.sendto(str(file_size).encode(), addr)

    with open(file_path, 'rb') as f:
        while True:
            # 发送未确认的数据
            while len(buffer) < window_size and seq_num < (file_size + byte_size - 1) // byte_size:
                data = f.read(byte_size)
                packet = str(seq_num).zfill(6).encode() + data
                sock.sendto(packet, addr)
                buffer.append(packet)
                seq_num += 1

            # 接收确认
            try:
                receive_data, _ = sock.recvfrom(byte_size)
                ack_num = int(receive_data.decode())
            except socket.timeout:
                # 超时重传
                for packet in buffer:
                    sock.sendto(packet, addr)
                continue

            # 删除已确认的数据
            while buffer and int(buffer[0][:6].decode()) < ack_num:
                buffer.pop(0)

            if ack_num == (file_size + byte_size - 1) // byte_size:
                break

    sock.close()


if __name__ == '__main__':
    file_path = "./testa.txt"
    addr = ("192.168.100.3", 9999)
    send_file(file_path, addr)
