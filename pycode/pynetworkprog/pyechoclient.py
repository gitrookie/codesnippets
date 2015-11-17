import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect(("", 50000))
sock.sendall(b"hello world")
data = sock.recv(1024)
sock.close()
print(data)
