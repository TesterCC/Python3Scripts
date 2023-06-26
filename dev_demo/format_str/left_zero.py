ip_str = "192.168.120.21:00022"

port = ip_str.split(":")[1]

print(port)

print(port.lstrip("0"))
