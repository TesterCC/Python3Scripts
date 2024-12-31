import socket
from Crypto.Cipher import AES

# 使用 pycryptodome 这个库来实现 AES-256 的加密。客户端代码

# 设置密钥，此处使用256位密钥
key = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'

# 需要加密的数据
plaintext = b'This is a test message!'

# 填充数据到16字节的倍数
padding = 16 - (len(plaintext) % 16)
plaintext += bytes([padding]) * padding

# 初始化AES加密器
cipher = AES.new(key, AES.MODE_ECB)

# 加密数据
ciphertext = cipher.encrypt(plaintext)

# 创建TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务端
s.connect(('127.0.0.1', 8080))

# 发送加密后的数据
s.sendall(ciphertext)

# 接收服务端的数据
data = s.recv(1024)

# 打印接收的数据
print(data)

# 关闭TCP socket
s.close()
