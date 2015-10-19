from contextlib import contextmanager
import time


@contextmanager
def timer(label):
    start = time.time()
    yield
    end = time.time()
    print("{}: {:f}".format(label, end - start))


with timer("counting"):
    n = 1000
    while n > 0:
        n -= 1


with open("pythontree.py", "r") as f:
    for file in f:
        print(file)
