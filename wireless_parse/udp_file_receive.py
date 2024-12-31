# Import the sockets library
import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the socket parameters
host = 'localhost'
port = 10000

# Bind the socket to the host and port
s.bind((host, port))

# Receive the file
while True:
    data, addr = s.recvfrom(1024)
    if not data:
        break
    print("Received file:")
    with open('file.txt', 'wb') as f:
        f.write(data)
        break

# Close the socket
s.close()