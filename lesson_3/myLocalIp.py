import socket

ip_a = socket.gethostbyname(socket.getfqdn())
print(ip_a)