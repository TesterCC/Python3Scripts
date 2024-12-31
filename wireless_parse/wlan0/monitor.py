import argparse
import json
import os
import socket
import struct
import textwrap
import time
import traceback

from scapy.all import *

from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether


# mon_interface = "wlan0mon"
# wlan_interface = "wlan1"


def get_version():
    version = "1.0.3.20230509"
    ret = f"Current Version: {version}"
    return ret


def packet_forward(pkt):
    # del old checksum
    del pkt.chksum

    udp = pkt[UDP]

    udp.chksum = 0  # must del

    ip = pkt[IP]

    ip.src = nc_ip
    ip.dst = nd_ip

    # ether = scapy.all.Ether(src=mac, dst=mac, type="IPv4")
    packet = ip

    packet = packet.__class__(bytes(packet))

    # print("---new one---")
    # print(packet.summary())
    # print("@@" * 33)

    scapy.all.send(packet, iface=wlan_interface, verbose=0)  # verbose=0, don't output in terminal
    # time.sleep(0.001)


def run(args, conf=None):
    global nc_ip, nd_ip, wlan_interface

    # print(f"[D] in run, conf is: {conf}")

    if conf:
        na_ip = config["src"]
        nb_ip = config["fake_dst"]
        nc_ip = config["fake_src"]
        nd_ip = config["dst"]
        mon_interface = config["mon"]
        wlan_interface = config["nic"]

    else:
        na_ip = args.na
        nb_ip = args.nb
        nc_ip = args.nc
        nd_ip = args.nd
        mon_interface = args.mon
        wlan_interface = args.nic

    print(f'node a, src : {na_ip}')
    print(f'node b, fake dst : {nb_ip}')
    print(f'node c, fake src : {nc_ip}')
    print(f'node d, dst : {nd_ip}')
    print(f'monitor network interface card : {mon_interface}')
    print(f'network interface card : {wlan_interface}')

    # capture packets
    sniff(iface=mon_interface, prn=packet_forward, store=0, count=0, filter=f"udp and src {na_ip} and dst {nb_ip}")


def gen_conf(args):
    # print("[D] in gen_conf, args: ", args)
    config = dict()
    config["src"] = ""
    config["fake_dst"] = ""
    config["fake_src"] = ""
    config["dst"] = ""
    config["mon"] = ""
    config["nic"] = ""

    if args.src:
        config['src'] = args.src

    if args.fdst:
        config["fake_dst"] = args.fdst

    if args.fsrc:
        config["fake_src"] = args.fsrc

    if args.dst:
        config["dst"] = args.dst

    if args.mon:
        config["mon"] = args.mon

    if args.nic:
        config["nic"] = args.nic

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


if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser(
            description='Cheat Netflow Tool',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''Example:
            python3 monitor.py -a 192.168.100.2 -b 192.168.101.7 -c 192.168.101.3 -d 192.168.100.6 -m wlan0mon -i wlan1
            python3 monitor.py genconf -src 192.168.100.2 -fd 192.168.101.7 -fs 192.168.101.3 -dst 192.168.100.6 -mon wlan0mon -nic wlan1 -o mtest.json
            python3 monitor.py -j mtest.json
            '''))

        parser.add_argument('-a', '--na', type=str, default="", help='node src ip address')
        parser.add_argument('-b', '--nb', type=str, default="", help='tamper node fake dst ip address')
        parser.add_argument('-c', '--nc', type=str, default="", help='tamper node src ip address')
        parser.add_argument('-d', '--nd', type=str, default="", help='node dst ip address')
        parser.add_argument('-m', '--mon', type=str, default="wlan0mon", help='monitor wireless network card')
        parser.add_argument('-i', '--nic', type=str, default="wlan1", help='wireless network card')
        parser.add_argument('-j', '--json', type=str, help='run with config, config.json file path')
        parser.add_argument('-V', '--version', action='version', version=get_version(), help='display version info')

        sub_parsers = parser.add_subparsers()

        sub_parser = sub_parsers.add_parser('genconf', help='generate conf json')
        sub_parser.add_argument('-src', '--src', type=str, default="", help='node src ip address')
        sub_parser.add_argument('-fd', '--fdst', type=str, default="", help='tamper node dst ip address')
        sub_parser.add_argument('-fs', '--fsrc', type=str, default="", help='tamper node src ip address')
        sub_parser.add_argument('-dst', '--dst', type=str, default="", help='node dst ip address')
        sub_parser.add_argument('-mon', '--mon', type=str, default="wlan0mon", help='monitor wireless network card')
        sub_parser.add_argument('-nic', '--nic', type=str, default="wlan1", help='wireless network card')
        sub_parser.add_argument('-o', '--output', type=str, default="", required=False,
                                help='output config.json to specific directory, e.g. /test/test.json')
        sub_parser.add_argument('-V', '--version', action='version', version=get_version(), help='display version info')

        args = parser.parse_args()

        if args.na:
            run(args)

        if args.json:
            with open(args.json, 'r') as f:
                config = json.load(f)

            # print("[D] config info: ", config)
            run(args, conf=config)

        if "src" in args:
            gen_conf(args)

    except Exception as e:
        traceback.print_exc()
