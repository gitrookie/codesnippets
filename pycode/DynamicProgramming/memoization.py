# Memoization
# Fibbonacci without memoization


def memdec(f):
    fib_cache = {}
    def wrapper(*args):
        if not args in fib_cache:
            fib_cache[args] = f(*args)
        return fib_cache[args]
    return wrapper


@memdec
def fib(n):
    '''Recursive Fibbonacci'''
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
