# coding=utf-8
'''
DATE: 2020/09/23
AUTHOR: Yanxi Li
'''

# ref: https://www.runoob.com/python/python-continue-statement.html

peer_ip_list = ['a', 'b', 'o', 'y']

for letter in 'Python':  # 第一个实例
    for _peer_id in peer_ip_list:
        if _peer_id != letter:
            continue
        print('在Python中的字母 :', letter)
