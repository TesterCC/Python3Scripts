#!/usr/bin/python
# Filename s5.py
# Python Dynamic Socks5 Proxy
# Usage: python s5.py 1080
# Background Run: nohup python s5.py 1080 & 
 
import socket, sys, select, socketserver, struct, time 
 
class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer): pass
class Socks5Server(socketserver.StreamRequestHandler):
  def handle_tcp(self, sock, remote):
    fdset = [sock, remote]
    while True:
      r, w, e = select.select(fdset, [], [])
      if sock in r:
        if remote.send(sock.recv(4096)) <= 0: break
      if remote in r:
        if sock.send(remote.recv(4096)) <= 0: break
  def handle(self):
    try:
      pass # print 'from ', self.client_address nothing to do.
      sock = self.connection
      # 1. Version
      sock.recv(262)
      sock.send(bytes("\x05\x00",'utf-8'));
      # 2. Request
      data = self.rfile.read(4)
      mode = data[1]
      addrtype = data[3]
      if addrtype == 1:    # IPv4
        addr = socket.inet_ntoa(self.rfile.read(4))
      elif addrtype == 3:   # Domain name
        addr = self.rfile.read(ord(sock.recv(1)[0]))
      print(addr)
      port = struct.unpack('>H', self.rfile.read(2))
      print(port)
      reply = bytes("\x05\x00\x00\x01",'utf-8')
      try:
        if mode == 1: # 1. Tcp connect
          remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          remote.connect((addr, port[0]))
          pass # print 'To', addr, port[0] nothing do to.
        else:
          reply =bytes("\x05\x07\x00\x01",'utf-8') # Command not supported
        local = remote.getsockname()
        reply += socket.inet_aton(local[0]) + struct.pack(">H", local[1])
      except socket.error:
        # Connection refused
        reply = bytes("\x05\x05\x00\x01\x00\x00\x00\x00\x00\x00",'utf-8')
      sock.send(reply)
      # 3. Transfering
      print(reply[1])
      if reply[1] == 0: # Success
        if mode == 1:  # 1. Tcp connect
          self.handle_tcp(sock, remote)
    except socket.error:
      pass #print 'error' nothing to do .
    except IndexError:
      pass
def main():
  filename = sys.argv[0];
  if len(sys.argv)<2:
    print('usage: ' + filename + ' port')
    sys.exit()
  socks_port = int(sys.argv[1]);
  server = ThreadingTCPServer(('', socks_port), Socks5Server)
  print('bind port: %d' % socks_port + ' ok!')
  server.serve_forever()
if __name__ == '__main__':
  main()