#
import math
import time


def dec(f):
    "Timing Decorator"
    def wrapper(*args):
        start = time.time()
        x = f(*args)
        print(time.time()-start)
        return x
    return wrapper


def fib(n):
    'Fibbonacci Recursive'

    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):
    'Fibbonacci Iterative'

    if n <= 2:
        return 1
    else:
        a, b = 0, 1
        while n-1:
            a, b = b, a+b
            n -= 1
        return b


@dec
def check_prime(n):
    'Checking for prime'

    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        else:
            i += 2

    return True


@dec
def check_prime2(n):
    'Checking for prime 2'

    l = range(2, int(math.sqrt(n))+1, 1)
    for i in l:
        if n % i == 0:
            return False
    return True


@dec
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def factors(n):
    i = 2
    a = []
    while i * i <= n:
        if n % i == 0:
            a.append(i)
            a.append(n//i)
        i += 1
    return sorted(a)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def factorial2(n):
    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    return fact
