import socket

x = socket.getaddrinfo("iisc.ernet.in", 80, proto=socket.IPPROTO_TCP)
print(x)
