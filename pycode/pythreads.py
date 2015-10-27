# Threads in Python

import threading
# In Python3 *thread* has been renamed to *_thread* which is used to implement
# threading* module. Python3 applications should use thread module.
# args is argument tuple for target invocation


'''
class MyThread(threading.Thread):
    def start(self):
        print("In start")
        super().start()

    def run(self):
        print("In run method")
        super().run()

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
# t1 = threading.Thread(target=thread_func1, args=(5, 1))
# t2 = threading.Thread(target=thread_func1, args=(10, 2))

t1 = MyThread(target=thread_func1, args=(5, 1))
t2 = MyThread(target=thread_func1, args=(10, 2))

# start method starts the thread activity. Should be run once per thread object
# arranges for object's run method.
t1.start()
t2.start()

# t1.join()
# t2.join()
'''

# '''
# state = 0


# def func():
#     global state
#     print("Current Thread is")
#     state += 1

# t1 = threading.Thread(target=func)
# t2 = threading.Thread(target=func)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(state)
# '''

#####################################################################
################## Queues ###########################################
#####################################################################
import queue
# queue module implements multiproducer and multiconsumer queues.
# queue module provides multiproducer and multiconsumer implementation suitable
# for multithreading. queue.Queue class implements all locking semantics. It
# depends upon the availability of thread support in python. Provides
# FIFO(queue.Queue), LIFO, priority queues.
