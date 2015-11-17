import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.bind(("", 50000))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    print(data)
    if data:
        break
conn.sendall(data)
sock.close()
