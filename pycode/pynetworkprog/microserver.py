# server.py
# Fibbonacci Microservice

from socket import *
from fib import fib
from threading import Thread
from concurrent.futurs import ProcessPoolExecutor as Pool

inp = []


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        # fib_handler(client)
        Thread(target=fib_handler, args=(client,), daemon=True).start()
        # Thread(target=fib_handler, args=(client,)).start()
        # print("Thread Next")


def fib_handler(client):
    while True:
        req = client.recv(128)
        if not req:
            break
        n = int(req)
        # result = fib(n)
        future = pool.submit(fib, n)
        result = future.result()
        resp = str(result).encode('ascii') + b'\n'
        client.sendall(resp)
    print("Closed")


fib_server(("", 25000))
