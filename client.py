import socket

s = socket.socket()
host = '172.17.105.102'
print (host)
port = 12345

s.connect((host, port))
print (s.recv(1024))
s.close
