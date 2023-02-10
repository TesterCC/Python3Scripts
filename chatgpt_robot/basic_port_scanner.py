import socket


# too slow
def port_scanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    host = input("Enter the host to scan: ")
    for port in range(1, 65535):
        port_scanner(host, port)
