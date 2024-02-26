# -*- coding=utf-8 -*-
import json

a = {"ip": "192.168.120.1", "port": 3333}

a_str = json.dumps(a)
print(type(a_str))
print(a_str)
print("*" * 33)

d_str = json.dumps(a, ensure_ascii=False)
print(d_str)
print("*" * 33)

b_str = f"python aaa \'{a_str}\'"
print(type(b_str))
print(b_str)
print("*" * 33)

c_str = 'python bbb -v "{}"'.format(b_str)
print(type(c_str))
print(c_str)

print("*" * 44)
# robot
escaped_string = a_str.replace('"', '\\"')
escaped_string = '"' + escaped_string + '"'

print(type(escaped_string))   # "{\"ip\": \"192.168.120.1\", \"port\": 3333}"
print(escaped_string)
