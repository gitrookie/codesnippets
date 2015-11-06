# pystructs.pydoc
# Writing data using struct module to a file.

import struct

data = struct.pack("<3s", b"hey")

with open("pystruct.txt", "wb") as f:
    f.write(data)
