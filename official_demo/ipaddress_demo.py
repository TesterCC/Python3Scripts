# coding=utf-8
'''
DATE: 2020/09/15
AUTHOR: Yanxi Li
'''

from ipaddress import ip_address, ip_network


def check_ip_list(ip_list: list):
    ret_ip_list = []

    for ip in ip_list:
        # print(ip, type(ip))   # Debug
        a, b, c, d = ip.split(".")
        if d.find("-") != -1:
            e, f = d.split("-")
            d_ips = ["{}.{}.{}.{}".format(a, b, c, g) for g in range(int(e), int(f))]
            ret_ip_list += d_ips

        elif d.find("/") != -1:
            # print(d, ip)   # Debug
            ip_net = ip_network(ip)
            # print(ip_net)   # Debug
            d_ips = [str(dip) for dip in ip_net.hosts()]
            ret_ip_list += d_ips

        else:
            ret_ip_list.append(ip)

    return ret_ip_list


if __name__ == '__main__':
    # ret = check_ip_list(["192.168.0.1-24"])
    # ret = check_ip_list(["192.0.2.0/24"])
    # ret = check_ip_list(["10.0.2.1"])
    ret = check_ip_list([])
    # ret = check_ip_list(["192.168.0.1-24", "192.0.2.0/24", "10.0.2.208"])
    print(ret)
    print(len(ret))
