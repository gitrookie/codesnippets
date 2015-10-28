# Any function containing yield statement is a generator
'''
def foo(n):
    while True:
        yield n
        n -= 1

f = foo(5)
'''


def bar():                      # yield from <generator object>
    "yield from <generator Object>"
    yield from [1, 2, 3, 4]     # Doing iteration
    yield from f
    

'''
def spam():
    while True:
        x = yield
        print(x)

spam()
'''
