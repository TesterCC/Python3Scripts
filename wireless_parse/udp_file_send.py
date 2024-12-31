import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Send the file
with open('file.txt', 'rb') as f:
    data = f.read()
    sock.sendto(data, ('127.0.0.1', 10000))
    # Close the socket
    sock.close()
