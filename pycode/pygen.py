def foo(n):
    while True:
        yield n
        n -= 1

f = foo(5)


def bar():
    "yield from <generator Object>"
    yield from [1, 2, 3, 4]
    yield from f
