# -*- coding=utf-8 -*-
import json

a = {"ip": "192.168.120.1", "port": 3333}

a_str = json.dumps(a)
print(type(a_str))
print(a_str)
print("*" * 33)


# robot
escaped_string = a_str.replace('"', '\\"')
escaped_string = '"' + escaped_string + '"'

print(type(escaped_string))   # "{\"ip\": \"192.168.120.1\", \"port\": 3333}"
print(escaped_string)

b_str = f"python aaa -j {escaped_string}"
print(type(b_str))
print(b_str)
print("*" * 33)

c_str = f"python bbb -v \'{b_str}\'"  # maybe need test
print(type(c_str))
print(c_str)


