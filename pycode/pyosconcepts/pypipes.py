# pypipes.py
# Pipes an IPC mechanism require a common ancestor for data transfer.
# The communication channel is of stream type stream. Closing of one of the
# file descriptor is a convention not mandatory. But it is good idea to close
# one of the file descriptor since pipes are unidirectional in nature.

#  Names pipes created by FIFO act like regular files doesn't exist in
# filesystem instead it exist as data structure in kernel memory.

import os
'''
r, w = os.pipe()
if os.fork() == 0:
    os.close(w)
    while True:
        data = os.read(r, 512)
        if not data:
            break
        print(data.decode("ascii") + " Coming from parent")
else:
    os.close(r)
    os.write(w, b"Hey Child")
'''
path = "pipe"
os.mkfifo(path)
fh = os.open(path, os.O_WRONLY)
os.write(fh, b"Hey Client")
input()
os.unlink(path)
