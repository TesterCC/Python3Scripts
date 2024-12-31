# coding:utf-8

import uuid


def gen_flags(flag_tag="flag", count=7):
    print(f"[+] Generate {count} flag(s): ")
    for i in range(count):
        print("{}{{{}}}".format(flag_tag, uuid.uuid4()))


if __name__ == '__main__':
    # gen_flags(10)
    gen_flags(flag_tag="CyberSpace", count=3)
