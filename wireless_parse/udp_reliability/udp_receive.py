import socket

# dst = input("save file dir:")
# BUFFER_SIZE = 4 * 1024 * 1024
BUFFER_SIZE = 32 * 1024

# ref: https://mp.weixin.qq.com/s/Js1nmaF70lculpMFOxGLaA

# 用来临时保存的数据
data = set()

sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv.bind(('0.0.0.0', 9999))

# 重复收包次数
repeat = 0

while True:
    buffer, ack_addr = sock_recv.recvfrom(BUFFER_SIZE)
    print(f"[D] ack_addr: {ack_addr}")

    ack_ip, _ = ack_addr
    # 确认反馈地址
    ack_address = (ack_ip, 9999)
    sock_ack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 全部接收完成，获取文件名
    if buffer.startswith(b'over_'):
        fn = buffer[5:].decode()
        # 多确认几次文件传输结束，防止发送方丢包收不到确认
        for i in range(3):
            sock_ack.sendto(fn.encode() + b'_ack', ack_address)
        break

    # 接收带编号的文件数据，临时保存，发送确认信息
    buffer = tuple(buffer.split(b'_', maxsplit=1))
    if buffer in data:
        repeat = repeat + 1
    else:
        data.add(buffer)
        print(f"[tmp data]\n", data)
    sock_ack.sendto(buffer[0] + b'_ack', ack_address)

sock_recv.close()
sock_ack.close()
print(f'重复接收数据{repeat}次')

data = sorted(data, key=lambda item: int(item[0]))
# with open(rf'{dst}/{fn}', 'wb') as fp:
with open(rf'{fn}', 'wb') as fp:
    for item in data:
        fp.write(item[1])
