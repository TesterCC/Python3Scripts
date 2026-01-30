# -*- coding=utf-8 -*-
import warnings
warnings.filterwarnings("ignore")

import argparse
import binascii
import json
import socket
import os
import struct
import textwrap
from os.path import basename
import sys
import time

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import scapy.all
from scapy.layers.inet import IP, TCP, UDP
from scapy.utils import PcapWriter

'''
testcase:
# python3 gen_pcap.py genconf -s 192.168.100.3:9999
# python3 gen_pcap.py genconf -s 192.168.100.3:9999 -o /opt/test/test.json
# python3 gen_pcap.py genconf -s 192.168.100.3:9999 -e aes -k 1234abcd4321efgh -o /opt/test/test3.json

# python3 gen_pcap.py -v 192.168.100.3:9999 -f test.txt
# python3 gen_pcap.py -c config.json -f test.txt
'''

# BUFFER_SIZE = 1426  # 1450-24 = 1426  # attention, don't modify, plain text use it

repeat_times = 5

positions = []

iv = b'WirelessPost2@23'

pktdump = PcapWriter(f"output_{int(time.time())}.pcap", append=True, sync=True)


def add_udp_packet(target_host="172.168.0.101", target_port=9999, send_data=None):
    # 创建一个Scapy UDP数据包，包含发送的数据
    # print(f"[D] {target_host}:{target_port} ")
    packet = IP(dst=target_host) / UDP(dport=target_port, sport=12345) / send_data
    # 将数据包写入PCAP文件
    pktdump.write(packet)



def get_version():
    version = "1.1.1.20230925"
    ret = f"Current Version: {version}"
    return ret


# encrypt function
def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data


def handle_send_content(cmd_type=0, cmd_content=None, cur_pos=0, total_len=0):
    # comm packet data
    cmd_content2 = None
    # 1+1+2+m
    if isinstance(cmd_content, bytes) is not True:
        cmd_content = cmd_content.encode("utf-8")

    cmd_type_data = struct.pack('!b', cmd_type)  # 1 bytes

    reserve_data = struct.pack('!b', 0)  # 1 bytes tran file content

    if cmd_type == 1:
        # cmd_type1, m
        cmd_content2 = cmd_content
    elif cmd_type == 2:
        # print("#" * 66)
        # print(total_len, cur_pos)

        # send files total length
        total_len_data = struct.pack('!I', total_len)  # 4 bytes

        # cur tran position;  cmd_content, detail content
        cur_pos_data = struct.pack('!I', cur_pos)  # 4 bytes
        # print("[D2] cmd type 2: ", total_len_data, cur_pos_data, cmd_content)
        # cmd_type2, m
        cmd_content2 = total_len_data + cur_pos_data + cmd_content

    # command length
    cmd_content_len_data = struct.pack('!h', len(cmd_content2))  # m

    # print(type(cmd_type_data), type(reserve_data), type(cmd_content_len_data), type(cmd_content2))
    # print(">> handle_send_content: ", cmd_type_data, reserve_data, cmd_content_len_data, cmd_content2)

    # print("cmd_type_data: ", cmd_type_data)
    # print("reserve_data: ", reserve_data)
    # print("cmd_content_len_data: ", cmd_content_len_data)

    handle_content = cmd_type_data + reserve_data + cmd_content_len_data + cmd_content2

    return handle_content


def handle_send_packet(poc_inc, retry_inc, content, key=None):
    #  4 + 4 + 2 + 1 + 1 + n
    # content length should be 1450

    # global pos_inc

    # id_header
    encrypt_header_hex = "FEABFEAB"
    encrypt_header_bin = binascii.unhexlify(encrypt_header_hex)
    encrypt_header_data = struct.pack('!4s', encrypt_header_bin)  # 4 bytes

    # poc_inc += 1
    poc_inc_data = struct.pack('!i', poc_inc)  # 4 bytes

    if key:
        content = encrypt(content, key)  # en

    len_data = struct.pack('!h', len(content))  # 2 bytes

    retry_inc_data = struct.pack('!b', retry_inc)  # 1 bytes

    reserve_data = struct.pack('!b', 0)  # 1 bytes

    # 1st send， file_name
    # handle_content = handle_send_content(1, file_name)

    # send_data = encrypt_header_data + poc_inc_data + len_data + retry_inc_data + reserve_data + content
    # different is in handle_content
    send_data = encrypt_header_data + poc_inc_data + len_data + retry_inc_data + reserve_data + content
    return send_data


def send_packet_demo(host, port, filename, key=None, BUFFER_SIZE=1426):
    pos_inc = 0
    # poc_inc = 1

    fname1, fname2 = os.path.split(filename)  # fname1 -> path  , fname2 -> file_name

    file_name = f'{basename(fname2)}'.encode()
    print(f"file_name: {file_name}")
    # print(f"file_name type: {type(file_name)}")

    client_addr = (host, port)

    print(f"[D] target info: {host}:{port}")
    print(f"[D] BUFFER_SIZE: {BUFFER_SIZE}")

    # key logic

    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # step1: handle 1st udp data, filename
    send_fn_content = handle_send_content(cmd_type=1, cmd_content=file_name)
    retry_inc = 0
    for x in range(repeat_times):
        retry_inc += 1
        send_fn_packet = handle_send_packet(pos_inc, retry_inc, send_fn_content, key=key)
        # sock.sendto(send_fn_packet, client_addr)
        # add_udp_packet(send_data=send_file_packet)  # debug
        add_udp_packet(target_host=host, target_port=port, send_data=send_fn_packet)  # debug

        time.sleep(0.01)  # or 0.01

    # print("-" * 66)
    # step2: handle 2ed udp data, file content
    # no need to notice receive   # receiver first receive 0x01, then receive 0x02
    # read file
    with open(filename, 'rb') as f:
        content = f.read()

        total_len = len(content)
        # print("[D2] read file total len: ", total_len)
        # print("[D2] send 2ed file content...")

        for i in range(0, len(content), BUFFER_SIZE):
            retry_inc = 0
            pos_inc += 1
            data = content[i:i + BUFFER_SIZE]
            send_file_content = handle_send_content(cmd_type=2, cmd_content=data, cur_pos=pos_inc, total_len=total_len)
            # print(f"pos_inc: {pos_inc}")
            for j in range(repeat_times):
                retry_inc += 1
                send_file_packet = handle_send_packet(pos_inc, retry_inc, send_file_content, key=key)
                # sock.sendto(send_file_packet, client_addr)
                # add_udp_packet(send_data=send_file_packet)  # debug
                add_udp_packet(target_host=host, target_port=port, send_data=send_file_packet)
                # print("[D2] send file packet len: ", len(send_file_packet))
                # print(f"retry_inc: {retry_inc}")
                time.sleep(0.04)  # 0.02 2m  0.03 5m   0.04 8m
        # sock.close()


def gen_conf(args):
    # print("[D] in gen_conf, args: ", args)
    config = dict()
    config["receiver"] = ""
    config["sender"] = ""
    config["cipher_suite"] = ""
    config["cipher_key"] = ""

    if args.receiver:
        config['receiver'] = args.receiver

    if args.sender:
        config["sender"] = args.sender

    if args.encrypt:
        config["cipher_suite"] = args.encrypt

    if args.key:
        if len(args.key) != 16:
            raise "[E] Invalid key length"
        config["cipher_key"] = args.key

    file_path = "config.json"
    if args.output:
        file_path = args.output
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir, exist_ok=True)

    with open(file_path, "w") as fc:
        fc.seek(0)
        fc.truncate()
        json.dump(config, fc, indent=4)
    print(f"Finish write config file at: {file_path}")


if __name__ == '__main__':

    try:
        parser = argparse.ArgumentParser(
            description='Generate Send Pcap',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''Example:
            python3 gen_pcap.py -c config.json -f /file/icon.png
 
            python3 gen_pcap.py genconf -s 192.168.100.3:9999
            python3 gen_pcap.py genconf -s 192.168.100.3:9999 -o /opt/test/test.json
            python3 gen_pcap.py genconf -s 192.168.100.3:9999 -e aes -k abcdef0123456789 -o /opt/test/test.json
            '''))

        parser.add_argument('-c', '--config', type=str, default="", help='config.json file path')
        parser.add_argument('-f', '--file', type=str, default="", help='transfer file path')
        # parser.add_argument('-o', '--output', type=str, default="", help='output pcap file path')
        parser.add_argument('-V', '--version', action='version', version=get_version(), help='display version info')

        sub_parsers = parser.add_subparsers()
        sub_parser = sub_parsers.add_parser('genconf', help='generate conf json')
        sub_parser.add_argument('-s', '--sender', type=str, default="",
                                help='sender use, ip address and port, e.g. 192.168.1.1:9999')
        sub_parser.add_argument('-r', '--receiver', type=str, default="",
                                help='receiver use, ip address and port, e.g. 192.168.1.1:9999')
        sub_parser.add_argument('-o', '--output', type=str, default="", required=False,
                                help='output xxx.json to specific directory')
        sub_parser.add_argument('-e', '--encrypt', type=str, default="", required=False,
                                help='cipher suite, empty means plaintext')
        sub_parser.add_argument('-k', '--key', type=str, default="", required=False, help='cipher key')

        args = parser.parse_args()

        # print("[D] args: ", args)
        # print("--" * 33)

        # resolve judge sub cmd
        if args.config and args.file:
            with open(args.config, 'r') as f:
                config = json.load(f)

                BUFFER_SIZE = 1426
                cipher_key = None
                if config.get("cipher_suite").lower() == "aes":
                    # global BUFFER_SIZE
                    BUFFER_SIZE = 1412
                # print(f"[D] BUFFER_SIZE: {BUFFER_SIZE}")

                if config.get("cipher_key"):
                    cipher_key = bytes(config.get("cipher_key"), encoding="utf-8")
                # print(f"[D] cipher_key: {cipher_key}")

                # print("[D] config info: ", config)
                sender = config.get("sender")

                host, port = sender.split(":")
                # print(f"[D] config send, send {args.file} to {sender}")
                # print(host, port, args.file, cipher_key, BUFFER_SIZE)
                send_packet_demo(host, int(port), args.file, key=cipher_key, BUFFER_SIZE=BUFFER_SIZE)

        # print(type(args))
        # print(dir(args))
        if "sender" in args:
            gen_conf(args)

    except Exception as e:
        print(e)

