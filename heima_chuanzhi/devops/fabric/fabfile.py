#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/23 15:06'

"""
pip install fabric

python3的api和python2的api不同了，注意
http://docs.fabfile.org/en/2.3/

https://blog.csdn.net/tohearts/article/details/81060608
"""

from fabric import Connection

conn = Connection('192.33.33.33', port=22, user='ubuntu', connect_kwargs={'password': ''})

result = conn.run('uname -s', hide=True)

result2 = conn.run('cat /etc/issue', hide=True)

msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"

print(msg.format(result))
print('-'*60)
print(msg.format(result2))


