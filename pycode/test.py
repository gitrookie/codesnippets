# Adding thousand separator in a number
import time


def Timer(f):
    def wrapper(n):
        start = time.time()
        f(n)
        return time.time() - start
    return wrapper


@Timer
def f2(n):
    r = []
    for i, c in enumerate(reversed(str(n))):
        if i and (not (i % 3)):
            r.insert(0, ',')
        r.insert(0, c)
    return "".join(r)

# print(f2(1234567))

# Using str's format method


@Timer
def f1(n):
    return "{0:,}".format(n)

import re
patt = re.compile("(\d)(?=(\d{3})+(?!\d))")


@Timer
def f3(n):
    # patt = re.compile("(\d)(?=(\d{3})+(?!\d))")
    return re.sub(patt, r'\1,', n)

print(f2(str(123456789)))
print(f1(123456789))
print(f3(str(123456789)))
