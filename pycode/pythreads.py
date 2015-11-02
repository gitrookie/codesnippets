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

def thread_func2(n):
    while n:
        print(n ** 2)
        n -= 1

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
# import queue
# queue module implements multiproducer and multiconsumer queues.
# queue module provides multiproducer and multiconsumer implementation suitable
# for multithreading. queue.Queue class implements all locking semantics. It
# depends upon the availability of thread support in python. Provides
# FIFO(queue.Queue), LIFO, priority queues.

'''
import datetime
import time


class MyThread(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print("%s says Hello World at time: %s" % (self.getName(), now))
        print("This is thread example from ibm")


for i in range(2):
    t = MyThread()
    t.start()
'''

'''
from queue import Queue
q = Queue()


class PThread(threading.Thread):
    def __init__(self, pq):
        self.pq = pq
        super().__init__()

    def run(self):
        for i in range(5):
            self.pq.put(i)


class CThread(threading.Thread):
    def __init__(self, cu):
        self.cu = cu
        super().__init__()

    def run(self):
        for i in range(5):
            print(self.cu.get() ** 2)
            self.cu.task_done()


pt = PThread(q)
pt.start()

ct = CThread(q)
ct.start()

q.join()
'''

# Main threads doesn't exit if the current threads is still running.
# if the daemon=True in the function main thread will exit.


def foo():
    input()

threading.Thread(target=foo, daemon=True).start()
