# server.py
# Fibbonacci Microservice

from socket import *
from fib import fib
from threading import Thread
from concurrent.futures import ProcessPoolExecutor as Pool
import logging

inp = []
pool = Pool(4)

logger = logging.getLogger("microservice")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()  # Blocking
        logger.debug("Connection %s", addr)
        # fib_handler(client)
        Thread(target=fib_handler, args=(client,), daemon=True).start()
        # Thread(target=fib_handler, args=(client,)).start()
        # print("Thread Next")


def fib_handler(client):
    while True:
        req = client.recv(128)  # Blocking
        # logger.debug(req)
        if not req:
            break
        n = int(req)
        result = fib(n)
        # future = pool.submit(fib, n)
        # result = future.result()
        resp = str(result).encode('ascii') + b'\n'
        # logger.debug(resp)
        client.send(resp)       # Blocking
    logger.debug("Closed")


fib_server(("", 25000))
