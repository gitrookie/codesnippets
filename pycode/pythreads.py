# Threads in Python

import time
import threading
# In Python3 *thread* has been renamed to *_thread* which is used to implement
# threading* module. Python3 applications should use thread module.
# args is argument tuple for target invocation

lock = threading.Lock()

def thread_func1(n, i):
    with lock:
        while n:
            print(n ** i)
            n -= 1
'''
def thread_func2(n):
    while n:
        print(n ** 2)
        n -= 1
'''
# target is the callable object to be invoked by run() method.
t1 = threading.Thread(target=thread_func1, args=(5, 1))
t2 = threading.Thread(target=thread_func1, args=(10, 2))
# start method starts the thread activity. Should be run once per thread object
# arranges for object's run method.
t1.start()
t2.start()

'''
state = 0


def func():
    global state
    print("Current Thread is")
    state += 1

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)

t1.start()
t2.start()

t1.join()
t2.join()

print(state)
'''
