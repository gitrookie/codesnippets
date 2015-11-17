import os

path = "pipe"
fh = os.open(path, os.O_RDONLY)
data = os.read(fh, 512)
print(data.decode("ascii"))
