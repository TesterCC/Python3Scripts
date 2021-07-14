# -*- coding: utf-8 -*-#

#  pip install pysocks
#  ref: https://www.cnblogs.com/fatalord/p/13850089.html    # request 直接加代理更简单
import requests
import socket
import socks
socks.set_default_proxy(socks.SOCKS5, "10.0.X.X", 1080)
socket.socket = socks.socksocket

def main():
  url = 'http://192.168.X.X:5000'
  html = requests.get(url).text
  print(html)


if __name__ == '__main__':
  main()