#!/usr/bin/env python
#coding=utf-8

# method 1
# f = open('imooc3.txt', 'w')
#
# for i in range(10000):
#     f.write('test write ' + str(i) + '\n')
#
# f.close()


with open('testlog.log', 'w') as f:
    for i in range(1000):
        f.write('log line' + str(i) + '\n')
    f.close()

print("Finish create multi-lines log.")