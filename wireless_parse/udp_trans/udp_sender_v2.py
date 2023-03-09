# -*- coding=utf-8 -*-
import socket
import os
import time

# https://blog.csdn.net/qq_40177015/article/details/112402889
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input('please enter the filename you want to send:\n')
filesize = str(os.path.getsize(filename))
fname1, fname2 = os.path.split(filename)

client_addr = ('192.168.100.3', 9999)
f = open(filename, 'rb')
count = 0
# flag = 1
while True:
    if count == 0:
        data = bytes(fname2, encoding="utf8")
        # The start time of the sending end is recorded,
        # which is used to calculate the total running time and 1s respectively
        total_start = time.time()
        current_start = time.time()
        s.sendto(data, client_addr)
    data = f.read(4096)
    if str(data) != "b''":
        s.sendto(data, client_addr)
    else:
        s.sendto('end'.encode('utf-8'), client_addr)
        break
    current_end = time.time()
    # Print the timestamp of the sending end for every 1s
    if current_end - current_start > 1:
        print(current_end)
        current_start = time.time()
    data, server_addr = s.recvfrom(4096)
    count += 1

s.close()
total_end = time.time()
print('total cost: ' + str(round(total_end - total_start, 6)) + 's')