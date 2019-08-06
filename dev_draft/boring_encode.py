#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
作用：用于混淆url中各id之间的规律性
encode : int id -> string mess
decode : string mess -> int id
'''

import base64


def encode(number, length):
    def fill(number, length):
        raw_str = str(number)
        need_num = length - len(raw_str)
        prepared = "0" * need_num + raw_str[:len(raw_str)]
        return prepared

    z = base64.b64encode(fill(number, length).encode("utf-8"))
    result = ""
    print(z)
    for c in z:
        result += fill(c, 3)
    return result


def decode(string):
    length = len(string) // 3

    z = ""
    try:
        for i in range(length):
            z += chr(int(string[3 * i:3 * (i + 1)]))
    except ValueError:
        return 0

    try:
        result = int(base64.b64decode(z))
    except TypeError:
        result = 0
    except ValueError:
        result = 0

    return result


if __name__ == "__main__":
    r = encode(29571, 6)  # 077068073053078084099120
    print(r)

    de = decode("077068073053078084099120")  # 29571
    print(de)
