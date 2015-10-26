import socket

sock_file = "./pysocket.sock"
s = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
s.connect(sock_file)
while True:
    data = input("Enter the data")
    # data = "hello"
    s.send(data.encode("utf-8"))
s.close()
