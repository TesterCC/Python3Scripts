import socket
from Crypto.Cipher import AES


def _unpad(data):
    # decrypt use
    padding_len = data[-1]
    return data[:-padding_len]


def _pad(data):
    # encrypt use
    padding_len = AES.block_size - (len(data) % AES.block_size)
    padding = chr(padding_len) * padding_len
    padded_data = data + padding.encode('utf-8')
    return padded_data


# 定义AES加密和解密的函数
def aes_encrypt(key, data):
    aes = AES.new(key, AES.MODE_ECB)
    padded_data = _pad(data)
    encrypted_data = aes.encrypt(padded_data)
    return encrypted_data


def aes_decrypt(key, encrypted_data):
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_data = aes.decrypt(encrypted_data)
    return _unpad(decrypted_data)


# 定义发送和接收数据的函数
def send_data(data, host, port, key):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        encrypted_data = aes_encrypt(key, data.encode('utf-8'))
        s.sendto(encrypted_data, (host, port))


def receive_data(port, key):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('0.0.0.0', port))
        encrypted_data, addr = s.recvfrom(1024)
        decrypted_data = aes_decrypt(key, encrypted_data).decode('utf-8')
        return decrypted_data


if __name__ == '__main__':
    # 设置密钥
    # key = b'mysecretaeskey12'  # keep key len(16)
    key = b"wirelesspost2023"

    # 发送数据
    send_data('Hello world!', '192.168.100.3', 9999, key)

    # # 接收数据
    # data = receive_data(12345, key)
    # print(data)
