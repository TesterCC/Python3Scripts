# -*- coding=utf-8 -*-
import argparse
import json
import os.path
import socket
import struct
import sys
import textwrap
import time
import traceback

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


'''
testcase:
# python3 receiver.py genconf -r 192.168.100.3:9999
# python3 receiver.py genconf -r 192.168.100.3:9999 -o /opt/test/test.json

# python3 receiver.py -l 192.168.100.3:9999
# python3 receiver.py -c /opt/test/test.json

# python3 receiver.py genconf -r 192.168.100.3:9999
# python3 receiver.py genconf -r 192.168.100.3:9999 -o /opt/test/test.json
# python3 receiver.py genconf -r 192.168.100.3:9999 -e aes -k abcdef0123456789 -o /opt/test/test.json
'''

# because send data max is 1450
# RECEIVE_BUFFER_SIZE = 1450

iv = b'WirelessPost2@23'


def get_version():
    version = "1.0.3.20230509"
    ret = f"Current Version: {version}"
    return ret


# decrypt function
def decrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(data)
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data


def receive_packet_demo_v2(host, port, key=None, RECEIVE_BUFFER_SIZE=1450):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (host, port)
    s.bind(server_addr)

    print(f'[D] UDP receiver bind at {host}:{port}')

    rebuild_fn_set = set()
    rebuild_fn_list = list()
    rebuild_fc_set = set()
    rebuild_fc_list = list()

    # RECEIVE_BUFFER_SIZE = 1450
    # if key:
    #     RECEIVE_BUFFER_SIZE = 1452
    print(f"[D] RECEIVE_BUFFER_SIZE: {RECEIVE_BUFFER_SIZE}")

    while True:

        buffer, ack_addr = s.recvfrom(RECEIVE_BUFFER_SIZE)
        # print(f"[D0] ack_addr: {ack_addr}")

        # handle_receive_packet(buffer)
        data_len = len(buffer) - 12
        unpack_fmt = "!4sihbb%ds" % data_len
        unpack_data = struct.unpack(unpack_fmt, buffer)
        # print("unpack_data: ", unpack_data)
        header_data = unpack_data[0]
        poc_inc_data = unpack_data[1]
        len_data = unpack_data[2]
        retry_inc_data = unpack_data[3]
        reserve_data = unpack_data[4]
        comm_data = unpack_data[5]

        # print(f"header_data: {header_data}")
        # print(f"poc_inc_data: {poc_inc_data}")
        # print(f"len_data: {len_data}")
        # print(f"retry_inc_data: {retry_inc_data}")
        # print(f"reserve_data: {reserve_data}")
        # # print(f"comm_data: {comm_data}")

        if header_data == b'\xfe\xab\xfe\xab':
            # rebuild_fn_list, rebuild_fc_list = handle_receive_content(poc_inc_data, comm_data)
            if key:
                comm_data = decrypt(comm_data, key)

            data_len = len(comm_data) - 4
            unpack_fmt = "!bbh%ds" % data_len
            unpack_data = struct.unpack(unpack_fmt, comm_data)

            cmd_type = unpack_data[0]
            cmd_reserve = unpack_data[1]
            cmd_len = unpack_data[2]
            cmd_data = unpack_data[3]

            # print("@" * 33)
            # # print(cmd_type,cmd_reserve)
            # print(f"cmd_type: {cmd_type}")
            # print(f"cmd_reserve_data: {cmd_reserve}")
            # print(f"cmd_len: {cmd_len}")
            # # print(f"cmd_data: {cmd_data}")  # debug

            if cmd_type == 1:
                file_name = cmd_data.decode()
                # print(f"file_name: {file_name}")
                if (poc_inc_data, file_name) not in rebuild_fn_set:
                    rebuild_fn_set.add((poc_inc_data, file_name))
                    refn = dict()
                    refn['poc_inc'] = poc_inc_data
                    refn['file_name'] = file_name
                    # print("~" * 66)
                    # print(f"[D] cmd type: {cmd_type}")
                    # print("[D167] file_name: ", file_name)
                    # print("~" * 66)
                    rebuild_fn_list.append(refn)

            elif cmd_type == 2:
                # print("[D] cmd_type_2: ", cmd_data)
                cmd_content_len = len(cmd_data) - 8
                cc_unpack_fmt = "!II%ds" % cmd_content_len
                cc_unpack_data = struct.unpack(cc_unpack_fmt, cmd_data)
                file_total_len = cc_unpack_data[0]
                file_cur_pos = cc_unpack_data[1]
                cmd_content = cc_unpack_data[2]
                # print("$" * 66)
                # print(f"[D] cmd type: {cmd_type}")
                # print("file_total_len: ", file_total_len)
                # print("file_cur_pos: ", file_cur_pos)
                # print("cmd_content: ", cmd_content)  # for debug
                # print("real cmd_content len: ", len(cmd_content))
                # print("$" * 66)

                if (file_cur_pos, cmd_content) not in rebuild_fc_set:
                    rebuild_fc_set.add((file_cur_pos, cmd_content))
                    refc = dict()
                    refc['file_cur_pos'] = file_cur_pos
                    refc['cmd_content'] = cmd_content
                    refc['file_total_len'] = file_total_len
                    refc['cmd_content_len'] = len(cmd_content)
                    rebuild_fc_list.append(refc)

            file_name = rebuild_fn_list[0].get('file_name') if rebuild_fc_list else ""
            file_total_len = rebuild_fc_list[0].get('file_total_len') if rebuild_fc_list else ""
            # print(f'[D195] file_name: {file_name}, file_total_len: {file_total_len}')

            # check data is enough
            cc_len_list = [fc['cmd_content_len'] for fc in rebuild_fc_list]
            cc_sum = sum(cc_len_list)
            print(f"[D200] cc_sum: ", cc_sum)

            if cc_sum == file_total_len:
                # print(f"rebuild_fn_set: {rebuild_fn_set}")
                # print(f"rebuild_fn_list: {rebuild_fn_list}")
                # print(f"[D202>>>>] start to write file, file_name: {file_name}, file_total_len: {file_total_len}")
                # start to write file
                sort_fc_list = sorted(rebuild_fc_list, key=lambda x: x['file_cur_pos'])

                offset = 0
                with open(file_name, 'wb') as f:
                    # print(f'[D] sort_fc_list: {sort_fc_list}')  # for debug
                    for fc in sort_fc_list:
                        # write cmd_content info
                        f.seek(offset, 0)
                        f.write(fc['cmd_content'])
                        offset += fc['cmd_content_len']
                    print(f"[D] finish write file {file_name}")
                    time.sleep(0.3)
                    break  

    # print("[I] finish write a file, break while loop")
    print("+" * 33 + " break " + "+" * 33)
    s.close()


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
        if file_dir:
            os.makedirs(file_dir, exist_ok=True)

    print("[I] config content: ", config)

    with open(file_path, "w") as fc:
        fc.seek(0)
        fc.truncate()
        json.dump(config, fc, indent=4)
    print(f"Finish write config file at: {file_path}")


if __name__ == '__main__':

    try:
        parser = argparse.ArgumentParser(
            description='File Transfer Tool',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''Example:                        
            python3 receiver.py -l 192.168.100.3:9999
            python3 receiver.py -c config.json
            
            python3 receiver.py genconf -r 192.168.100.3:9999
            python3 receiver.py genconf -r 192.168.100.3:9999 -o /opt/test/test.json
            python3 receiver.py genconf -r 192.168.100.3:9999 -e aes -k abcdef0123456789 -o /opt/test/test.json
            '''))

        parser.add_argument('-v', '--victim', type=str, default="",
                            help='sender use, ip address and port, e.g. 192.168.1.1:9999')
        parser.add_argument('-l', '--listen', type=str, default="",
                            help='receiver use, ip address and port, e.g. 192.168.1.1:9999')
        parser.add_argument('-c', '--config', type=str, default="", help='run with config, config.json file path')
        parser.add_argument('-f', '--file', type=str, default="", help='transfer file path')
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

        if args.config:

            with open(args.config, 'r') as f:
                config = json.load(f)

                # print("[D] config info: ", config)
                receiver = config.get("receiver")
                host, port = receiver.split(":")
                print("config listen: ", host, port)

                BUFFER_SIZE = 1450
                cipher_key = None
                if config.get("cipher_suite").lower() == "aes":
                    # global BUFFER_SIZE
                    BUFFER_SIZE = 1452
                # print(f"[D] BUFFER_SIZE: {BUFFER_SIZE}")

                if config.get("cipher_key"):
                    cipher_key = bytes(config.get("cipher_key"), encoding="utf-8")
                # print(f"[D] cipher_key: {cipher_key}")

                while True:
                    receive_packet_demo_v2(host, int(port), key=cipher_key, RECEIVE_BUFFER_SIZE=BUFFER_SIZE)

        if args.listen:
            print("[D] receiver: ", args.listen)

            host, port = args.listen.split(":")
            # print("args listen: ", host, port)
            while True:
                receive_packet_demo_v2(host, int(port))

        elif args.receiver:
            gen_conf(args)

    except Exception as e:
        traceback.print_exc()
