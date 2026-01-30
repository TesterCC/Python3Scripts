# -*- coding=utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import argparse
import ipaddress
import json
import os.path
import socket
import struct
import sys
import textwrap
import time
import traceback

import scapy.all
from scapy.layers.inet import IP, TCP, UDP
from scapy.all import Raw
from scapy.utils import hexdump

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

iv = b'WirelessPost2@23'


def get_version():
    version = "1.1.2.20230924"
    ret = f"Current Version: {version}"
    return ret


# vm = 'eth0'

# packet_list = scapy.all.rdpcap('udp9999.pcap')  # plain textwrap
# packet_list = scapy.all.rdpcap('20230705-100.3to100.6.pcap')  # cipher text
# packet_list = scapy.all.rdpcap('0923testsimpleudp.pcap')  # cipher text
# packet_list = scapy.all.rdpcap('test_read_pcap/0923testalludp.pcap')  # cipher text   # A udp aes to C

# packet_list = scapy.all.rdpcap('test_read_pcap/output_icon.pcap')  # cipher text   test by gen
# packet_list = scapy.all.rdpcap('test_read_pcap/output2.pcap')  # cipher text   test by gen
# packet_list = scapy.all.rdpcap('test_read_pcap/output3.pcap')  # cipher text   test by gen
# packet_list = scapy.all.rdpcap('test_read_pcap/output7.pcap')  # can recv cipher text   test by gen
#
# print(len(packet_list))


# decrypt function
def decrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(data)
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data


def handle_receive_packet(key=None, buffer=None):
    # print(f"[D] RECEIVE_BUFFER_SIZE: {RECEIVE_BUFFER_SIZE}")
    # print(f"[D] key: {key}")
    # print(f"[D] iv: {iv}")

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
    # print(f"comm_data: {comm_data}")

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
        # print(f"[D200] cc_sum: ", cc_sum)  # debug

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

                print(f"[D] finish write file {file_name}")  # debug


# def extract_pcap_file(key=b"abcdef0123456789", dst_host="", dst_port=9999, file_path="./"):
#     packet_list = scapy.all.rdpcap(file_path)  # can recv cipher text   test by gen
#     print(f"[D] file_path: {file_path}")
#     # print(len(packet_list))   # debug 0D0A packet show
#     for packet in packet_list:
#         # print(packet.summary())
#         packet.show()
#         if packet.haslayer(UDP) and packet[UDP].dport == dst_port and packet[IP].dst == dst_host:
#
#             # src_ip = packet[IP].src
#             # dst_ip = packet[IP].dst
#             # src_port = packet[UDP].sport
#             # dst_port = packet[UDP].dport
#
#             raw_data = packet[UDP].payload
#             # print(type(raw_data))  # debug
#             data = bytes(raw_data)
#             # print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")
#             # print(f"Source Port: {src_port}, Destination Port: {dst_port}")
#             # print(f"Data: {data}")
#             handle_receive_packet(key=key, buffer=data)
#     print("[D] finish extract pcap ...")


def extract_pcap_file(key=b"abcdef0123456789", dst_host="", dst_port=9999, file_path="./"):
    packet_list = scapy.all.rdpcap(file_path)  # can recv cipher text   test by gen
    print(f"[D] file_path: {file_path}")
    # print(len(packet_list))   # debug 0D0A packet show
    for packet in packet_list:
        # print(packet.summary())
        # packet.show()

        raw_data = bytes(packet)

        sub_raw_data = raw_data[32:]   # 直接偏移取32位后数据可以解开
        # 打印原始数据的十六进制表示
        # hex_data = sub_raw_data.hex()
        # print(hex_data)

        # src_ip = packet[IP].src
        # dst_ip = packet[IP].dst
        # src_port = packet[UDP].sport
        # dst_port = packet[UDP].dport
        # print("="*33)

        # print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")
        # print(f"Source Port: {src_port}, Destination Port: {dst_port}")
        # print(f"Data: {sub_raw_data}")
        handle_receive_packet(key=key, buffer=sub_raw_data)
    print("[D] finish extract pcap ...")


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description='Extract Pcap File',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''Example:                        
            python3 extract_pcap.py -c config.json -f output.pcap
            '''))

        parser.add_argument('-c', '--config', type=str, default="", help='config.json to filter')
        parser.add_argument('-f', '--file', type=str, default="", help='pcap file path')
        parser.add_argument('-V', '--version', action='version', version=get_version(), help='display version info')

        args = parser.parse_args()

        # print("[D] args: ", args)
        # print("--" * 33)

        if args.config and args.file:

            file_path = args.file
            with open(args.config, 'r') as f:
                config = json.load(f)

                # print("[D] config info: ", config)
                receiver = config.get("receiver")
                host, port = receiver.split(":")
                # print("config listen: ", host, port)

                BUFFER_SIZE = 1450
                cipher_key = None
                if config.get("cipher_suite").lower() == "aes":
                    # global BUFFER_SIZE
                    BUFFER_SIZE = 1452
                # print(f"[D] BUFFER_SIZE: {BUFFER_SIZE}")

                if config.get("cipher_key"):
                    cipher_key = bytes(config.get("cipher_key"), encoding="utf-8")
                # print(f"[D] cipher_key: {cipher_key}")

                # test decrypted
                rebuild_fn_set = set()
                rebuild_fn_list = list()
                rebuild_fc_set = set()
                rebuild_fc_list = list()

                extract_pcap_file(key=cipher_key, dst_host=host, dst_port=int(port), file_path=file_path)

    except Exception as e:
        traceback.print_exc()
