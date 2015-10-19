import random


def rm_walks():
    y = None
    while True:
        x = random.uniform(0, 1)
        if x < 0.1:
            raise Exception("Number less than 0.1")
        if y is None:
            yield x
            y = x
            continue
        if abs(x-y) >= 0.4:
            yield x
            y = x

r = rm_walks()
