import ipaddress

"""
python3实现数据生成，每三个一组从172.16.0.1开始，取10002个不同的IP，且保证每3个IP要在同一个网段内，以3个ip为一组返回列表。
"""

def generate_ip_list(start_ip, n):
    ip_list = []
    current_ip = ipaddress.IPv4Address(start_ip)

    for _ in range(n):
        ip_list.append(str(current_ip))
        current_ip += 1

    return ip_list


def group_ips(ip_list, group_size):
    return [ip_list[i:i + group_size] for i in range(0, len(ip_list), group_size)]


if __name__ == '__main__':

    # start_ip = '172.16.0.1'
    start_ip = '192.168.20.1'
    n = 10002

    ip_list = generate_ip_list(start_ip, n)
    grouped_ips = group_ips(ip_list, 3)

    print(grouped_ips)
    print(len(grouped_ips))