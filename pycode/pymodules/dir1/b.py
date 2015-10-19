import c                 # Python3 requires dot syntax for imports within package
                         # 'from . import c' or 'dir1.c' will work in Python3 
def foo():
    print("Testing Module dir1/b")

global_b = 10
print("In module {}".format(__name__))
