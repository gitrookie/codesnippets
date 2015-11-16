from multiprocessing import Pool
from multiprocessing import Process
import os


'''
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
'''


import multiprocessing as mp
import time

'''
def foo(q):
    print("In spawned process")
    q.put("hello")


if __name__== "__main__":
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    time.sleep(3)
    print("Main Process")
    print(q.get())
    print("End of main thread")
    p.join()
'''

def deco(f):
    "Timing Decorator"

    def wrapper(*args):
        start = time.time()
        f(*args)
        return time.time() - start
    return wrapper


def foo(x):
    return x * x

# Start 4 worker processes
p = Pool(processes=4)
print(p.map(foo, range(1, 100)))
